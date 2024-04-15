from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class VoidType(Type): 
    def __str__(self):
        return "VoidType"

class VarSym:
    def __init__(self, name:str,  typ : Type = None) -> None:
        self.name = name
        self.typ = typ

class FuncSym:
    def __init__(self, name: str, params: List[VarSym] = [], typ: Type = None, body: Stmt = None) -> None:
        self.name = name
        self.params = params
        self.typ = typ
        self.body = body


class StaticChecker(BaseVisitor, Utils):

    def __init__(self, ast: AST) -> None:
        self.ast = ast 
        self.env = [[
            FuncSym("readNumber", [], NumberType()),
            FuncSym("readString", [], StringType()),
            FuncSym("readBool", [], BoolType()),
            FuncSym("writeBool", [VarSym("", BoolType())], VoidType()),
            FuncSym("writeString", [VarSym("", StringType())], VoidType()),
            FuncSym("writeNumber", [VarSym("", NumberType())], VoidType())
        ]]
        self.return_type = None 
        self.has_return = False
        self.func_name = None 
        self.resolved = True 
        self.no_body = []
        self.in_loop = []
        self.is_called = False 
        self.return_list = []
        self.arr_ast = []
        self.curr_var_name = None

    def check(self) -> None:
        self.visit(self.ast, self.env)

    def resolveType(self, expr: Id | CallExpr | CallStmt | ArrayLiteral, typ: Type, param):
        if type(expr) is Id:
            idex = None 
            for idx in range(len(param)):
                sym = self.lookup(expr.name, param[idx], lambda x: x.name)
                if sym is not None and type(sym) is VarSym:
                    idex = idx
                    break 

            if idex is not None:
                for idx in range(len(param[idex])):
                    if type(param[idex][idx]) is VarSym and param[idex][idx].name == expr.name and param[idex][idx].typ is None:
                        param[idex][idx] = VarSym(sym.name, typ)
            
        elif type(expr) in [CallExpr, CallStmt]:
            for idx in range(len(param-[-1])):
                if type(param[-1][idx]) is FuncSym and param[-1][idx].name == expr.name.name and param[-1][idx].typ is None:
                    sym = param[-1][idx]
                    param[-1][idx] = FuncSym(sym.name, sym.params, typ, sym.body)
                    self.is_called = True 
                    self.visit(FuncDecl(Id(sym.name), list(map(lambda x: VarDecl(ID(x.name), x.typ, None, None), sym.params)), sym.body), param)
                    self.is_called = False

        else:
            if type(typ) is not ArrayType:
                self.resolved = False 

            else:
                for val in expr.value:
                    self.resolveType(val, typ.eleType if len(typ.size) == 1 else ArrayType(typ.size[1:], typ.eleType), param)

    def visitProgram(self, ast: Program, param):
        for decl in ast.decl:
            self.visit(decl, param)
      
        if self.no_body != []:
           raise NoDefinition(self.no_body[0].name.name)
        
        flag = False
        for func in param[0]:
            if type(func) is FuncSym and func.name == "main" and type(func.typ) is VoidType and func.params == []:
                flag = True 
                break
        
        if not flag:
            raise NoEntryPoint()
        
    def visitVarDecl(self, ast: VarDecl, param): 

        if self.lookup(ast.name.name, param[0], lambda x: x.name) is not None:
            raise Redeclared(Variable(), ast.name.name)
             
        self.curr_var_name = ast.name.name
        lhsType = ast.varType
        if ast.varInit is not None:
            rhsType = self.visit(ast.varInit, param)
            if lhsType is not None and rhsType is not None:
                if type(lhsType) is not type(rhsType):
                    raise TypeMismatchInStatement(ast)

                else:
                    if type(lhsType) is ArrayType:
                        if lhsType.size[:len(rhsType.size)] != rhsType.size:
                            raise TypeMismatchInStatement(ast)
                        
                        else:
                            if rhsType.eleType is None:
                                self.resolveType(ast.varInit, lhsType, param)
                                if self.resolved == False:
                                    raise TypeCannotBeInferred(ast)
                                
                                param[0] += [VarSym(ast.name.name, lhsType)]

                            else:
                                if type(rhsType.eleType) is not type(lhsType.eleType):
                                    raise TypeMismatchInStatement(ast)
                                
                    param[0] += [VarSym(ast.name.name, lhsType)]

            else:
                if rhsType is None and lhsType is not None:
                    raise TypeCannotBeInferred(ast)
                
                elif rhsType is None and rhsType is not None:
                    if type(ast.varInit) in [Id, CallExpr, ArrayLiteral]:
                        self.resolveType(ast.varInit, lhsType, param)
                        if self.resolved == False:
                            raise TypeCannotBeInferred(ast)
                        
                        param[0] += [VarSym(ast.name.name, lhsType)]

                    else:
                        raise TypeCannotBeInferred(ast)
                    
                else:
                    param[0] += [VarSym(ast.name.name, rhsType)]
        
        else:
            param[0] += [VarSym(ast.name.name, lhsType)]
            
        self.arr_ast = []
        self.curr_var_name = None
                
    def visitFuncDecl(self, ast: FuncDecl, param):
        func = self.lookup(self.name.name, param[-1], lambda x: x.name)
        if func is not None and func.body is not None and self.is_called == False:
            raise Redeclared(Function(), ast.name.name)
        
        params = []
        for param_decl in ast.param:
            if self.lookup(param_decl.name.name, params, lambda x: x.name) is not None:
                raise Redeclared(Parameter(), param_decl.name.name)

            else:
                params += [VarSym(param_decl.name.name, self.visit(param_decl.varType, param))]

        param = [params] + param 

        if ast.body is None:
            if self.is_called == False:
                self.no_body += [ast]

            param[-1] += [FuncSym(ast.name.name, params, None, None)]

        else:
            self.func_name = ast.name.name
            for f in self.no_body:
                if f.name.name == self.func_name:
                    self.no_body.remove(f)

            func_found = False 
            for idx in range(len(param[-1])):
                if type(param[-1][idx]) is FuncSym and param[-1][idx].nmae == ast.name.name:
                    func_found = True 
                    if len(param[-1][idx].params) != len(params):
                        raise Redeclared(Function(), ast.name.name)
                    
                    for idex in range(len(params)):
                        if type(param[-1][idx].params[idex].typ) is not type(params[idex].typ) or (type(param[-1][idx].params[idex].typ) is ArrayType and param[-1][idx].params[idex].typ.size != params[idex].typ.size):
                            raise Redeclared(Function(), ast.name.name)
                        
                    self.visit(ast.body, param)
                    param[-1][idx] = FuncSym(ast.name.name, params, self.return_type if self.return_type is not None else (VoidType() if self.return_list == [] else None))
                    break 
            if not func_found:
                param[-1] += [FuncSym(ast.name.name, params, self.return_type, ast.body)]
                self.visit(ast.body, param)
                rettype = self.return_type if self.return_type is not None else (VoidType() if self.return_list == [] else None)
                if param[-1][-1].typ is None:
                    param[-1][-1] = FuncSym(ast.name.name, params, rettype, ast.body)

        self.return_type = None 
        self.has_return = False 
        param = param[1:]
        self.return_list = []
        

    def visitId(self, ast: Id, param):
        if self.curr_var_name is not None and ast.name == self.curr_var_name:
            raise Undeclared(Identifier(), ast.name)
        
        self.resolved = True 
        found = None 
        for para in param:
            sym = self.lookup(ast.name, para, lambda x: x.name)
            if sym is not None and isinstance(sym, VarSym):
                found = para 
                break 
        
        if found is None:
            raise Undeclared(Identifier(), ast.name)
        
        else:
            for idx in range(len(found)):
                if found[idx].name == ast.name and type(found[idx]) is VarSym:
                    return found[idx].typ
                    
    def visitCallExpr(self, ast, param):
        if self.curr_var_name is not None and ast.name.name == self.curr_var_name:
            raise TypeMismatchInExpression(ast)
        
        self.resolved = True 
        exclude_last = param[:-1]
        for para in exclude_last:
            if self.lookup(ast.name.name, para, lambda x: x.name) is not None:
                raise TypeMismatchInExpression(ast)
            
        found = self.lookup(ast.name.name, param[-1], lambda x: x.name)
        if found is None or (found is not None and type(found) is not FuncSym):
            raise Undeclared(Function(), ast.name.name)

        else: 
            if type(found.typ) is VoidType:
                raise TypeMismatchInExpression(ast)
            
            if len(ast.args) != len(found.params):
                raise TypeMismatchInExpression(ast) 
            
            for idx in range(len(ast.args)):
                arg_typ = self.visit(ast.args[idx], param)
                
                if arg_typ is None:
                    if type(ast.args[idx]) in [Id, CallExpr, ArrayLiteral]:
                        self.resolveType(ast.args[idx], found.param[idx].typ, param)
                        if self.resolved == False:
                            return None
                    
                    else:
                        return None

                else:
                    if type(arg_typ) is not type(found.param[idx].typ):
                        raise TypeMismatchInExpression(ast)
                    
                    else:
                        if type(arg_typ) is ArrayType:
                            if found.params[idx].typ.size[:len(arg_typ.suze)] != arg_typ.size:
                                raise TypeMismatchInExpression(ast)
                            
                            if arg_typ.eleType is None:
                                if type(ast.args[idx]) in [Id, CallExpr, ArrayLiteral]:
                                    self.resolveType(ast.args[idx], found.params[idx].typ, param)
                                    if self.resolved == False:
                                        raise TypeCannotBeInferred(ast)
                                    
                            if type(arg_typ.eleType) is not type(found.params[idx].typ.eleType) or found.params[idx].typ.size != arg_typ.eleType.size:
                                raise TypeMismatchInExpression(ast)
                            
            return found.typ

    def visitCallStmt(self, ast, param):

        self.resolved = True 
        exclude_last = param[:-1]
        for para in exclude_last:
            if self.lookup(ast.name.name, para, lambda x: x.name) is not None:
                raise TypeMismatchInStatement(ast)
            
        found = self.lookup(ast.name.name, param[-1], lambda x: x.name)
        if found is None or (found is not None and type(found) is not FuncSym):
            raise Undeclared(Function(), ast.name.name)

        else: 
            if found.typ is not None and type(found.typ) is not VoidType:
                raise TypeMismatchInStatement(ast)
            
            if len(ast.args) != len(found.params):
                raise TypeMismatchInStatement(ast) 
            
            for idx in range(len(ast.args)):
                arg_typ = self.visit(ast.args[idx], param)
                
                if arg_typ is None:
                    if type(ast.args[idx]) in [Id, CallExpr, ArrayLiteral]:
                        self.resolveType(ast.args[idx], found.param[idx].typ, param)
                        if self.resolved == False:
                            raise TypeCannotBeInferred(ast)
                    
                    else:
                        raise TypeCannotBeInferred(ast)

                else:
                    if type(arg_typ) is not type(found.param[idx].typ):
                        raise TypeMismatchInStatement(ast)
                    
                    else:
                        if type(arg_typ) is ArrayType:
                            if found.params[idx].typ.size[:len(arg_typ.suze)] != arg_typ.size:
                                raise TypeMismatchInStatement(ast)
                            
                            if arg_typ.eleType is None:
                                if type(ast.args[idx]) in [Id, CallExpr, ArrayLiteral]:
                                    self.resolveType(ast.args[idx], found.params[idx].typ, param)
                                    if self.resolved == False:
                                        raise TypeCannotBeInferred(ast)
                                    
                                    arg_typ = found.params[idx].typ
                                    
                            if type(arg_typ.eleType) is not type(found.params[idx].typ.eleType) or found.params[idx].typ.size != arg_typ.eleType.size:
                                raise TypeMismatchInStatement(ast)
                            
            if found.typ is None:
                self.resolveType(ast, VoidType(), param)
        
        self.arr_ast = []

    def visitIf(self, ast, param):

        condTyp = self.visit(ast.expr, param)

        if condTyp is None:
            if type(ast.expr) in [Id, CallExpr, ArrayLiteral]:
                self.typeInfer(ast.expr, BoolType(), param)
                condTyp = BoolType()
            
            else: 
                raise TypeCannotBeInferred(ast)
        
        if type(condTyp) is not BoolType():
            raise TypeMismatchInStatement(ast)

        self.visit(ast.thenStmt, param)
        self.has_return = False
        
        for elifExpr, elif_stmt in ast.elifStmt:
            condTyp = self.visit(elifExpr, param)

            if condTyp is None:
                if type(ast.expr) in [Id, CallExpr]:
                    self.typeInfer(ast.elifExpr, BoolType(), param)
                    condTyp = BoolType()
                
            else: 
                raise TypeCannotBeInferred(ast)
            
            if type(condTyp) is not BoolType():
                raise TypeMismatchInStatement(ast)
            
            self.visit(elif_stmt, param)
  
        if ast.elseStmt:
            self.visit(self.elseStmt, param)        

        self.arr_ast = [] 

    def visitFor(self, ast, param):
        self.in_loop += [True]
        scala_typ = self.visit(ast.name, param)
        if scala_typ is None:
            self.resolveType(ast.name, NumberType(), param)
            scala_typ = NumberType()

        if type(scala_typ) is not NumberType:
            raise TypeMismatchInStatement(ast)
        
        cond_typ = self.visit(ast.condExpr, param)
        if cond_typ is None:
            if type(ast.condExpr) in [Id, CallExpr]:
                self.resolveType(ast.condExpr, BoolType(), param)
                cond_typ = BoolType()
                if self.resolved == False:
                    raise TypeCannotBeInferred(ast)
                
        if type(cond_typ) is not BoolType:
            raise TypeMismatchInStatement(ast)
        
        update_typ = self.visit(ast.updpExpr, param)
        if update_typ is None:
            if type(ast.updpExpr) in [Id, CallExpr]:
                self.resolveType(ast.updpExpr, NumberType(), param)
                cond_typ = NumberType()
                if self.resolved == False:
                    raise TypeCannotBeInferred(ast)
                
        if type(cond_typ) is not NumberType:
            raise TypeMismatchInStatement(ast)
        
        self.visit(ast.body, param)
        self.arr_ast = []
        self.in_loop = self.in_loop[:-1]
    

    def visitReturn(self, ast: Return, param):
        if self.has_return:
            return 
        self.has_return = True 
        if ast.expr is None:
            self.returnType = VoidType()
        
        else: 
            rettype = self.visit(ast.expr, param)
            func = self.lookup(self.func_name, param[-1], lambda x: x.name)

            if func.typ is None:
                if rettype is None:
                    if self.resolved == False:
                        raise TypeCannotBeInferred(ast)
                    
                    else: 
                        self.return_list += [ast]
                
                else:
                    self.return_type = rettype
                    for idx in range(len(param[-1])):
                        if type(param[-1][idx]) is FuncSym and type(param[-1][idx]).name == self.func_name:
                            sym = param[-1][idx]
                            param[-1][idx] = FuncSym(sym.name, sym.params, rettype, sym.body)

                    if self.return_list != []:  
                        while self.return_list != []:
                            if type(self.return_list[0].expr) in [Id, CallExpr, ArrayLiteral]:
                                self.resolveType(self.return_list[0].expr, rettype, param)

                                if self.resolved == False:
                                    raise TypeCannotBeInferred(self.return_list[0])
                                
                                else:
                                    self.return_list = self.return_list[1:]
                            
                            else:
                                raise TypeCannotBeInferred(self.return_list[0])
                        
            else:
                if type(func.typ) is VoidType():
                    raise TypeMismatchInStatement(ast)
                
                if rettype is None:
                    if self.resolved == False:
                        raise TypeCannotBeInferred(ast)
                    
                    elif type(ast.expr) in [Id, CallExpr, ArrayLiteral]:
                        self.resolveType(ast.expr, func.typ, param)
                        if self.resolved == False:
                            raise TypeCannotBeInferred(ast)
                        
                    else: 
                        raise TypeCannotBeInferred(ast)
                
                else:
                    if type(func.typ) is not type(rettype):
                        raise TypeMismatchInStatement(ast)
                    
                    else:
                        if type(func.typ) is ArrayType:
                            if func.typ.size[:len(rettype.size)] != rettype.size:
                                raise TypeMismatchInStatement(ast)
                            
                            if rettype.eleType is None:
                                if type(ast.expr) in [Id, CallExpr, ArrayLiteral]:
                                    if self.resolved == False:
                                        raise TypeCannotBeInferred(ast)
                                    
                                    rettype = func.typ
                                
                                else:
                                    raise TypeCannotBeInferred(ast)
                            
                            if type(rettype.eleType) is not type(func.typ.eleType) or func.typ.size != rettype.size:
                                raise TypeMismatchInExpression(ast)
                
                        self.return_type = func.typ
        
        self.arr_ast = []
           
    def visitAssign(self, ast, param):
        lhsType = self.visit(ast.lhs, param)
        rhsType = self.visit(ast.exp, param)
        

        if lhsType is None and rhsType is None:
            raise TypeCannotBeInferred(ast)
        
        if lhsType is None and rhsType is not None:
            if type(ast.lhs) is Id:
                self.typeInfer(ast.lhs, rhsType, param)

            else:
                raise TypeCannotBeInferred(ast)
            
        if lhsType is not None and rhsType is None:
            if type(ast.exp) in [Id, CallExpr, ArrayLiteral]:
                self.resolveType(ast.exp, lhsType, param)
                if self.resolved == False:
                    raise TypeCannotBeInferred(ast)
            else:
                raise TypeCannotBeInferred(ast)
        
        elif rhsType is None and lhsType is not None:
            if type(ast.exp) in [Id, CallExpr, ArrayLiteral]:
                self.resolveType(ast.exp, lhsType, param)
                if self.resolved == False:
                    raise TypeCannotBeInferred(ast)

            else:
                raise TypeCannotBeInferred(ast)   

        else:
            if type(lhsType) is VoidType:
                raise TypeMismatchInStatement(ast)
            
            elif type(lhsType) is not type(rhsType):
                raise TypeMismatchInStatement(ast)
            
            else:
                if type(lhsType) is ArrayType:
                    if lhsType.size[:len(rhsType.size)] != rhsType.size:
                        raise TypeMismatchInStatement(ast)
                    
                    else:
                        if rhsType.eleType is None:
                            if type(ast.exp) in [Id, CallExpr, ArrayLiteral]:
                                self.resolveType(ast.exp, lhsType, param)
                                if self.resolved == False:
                                    raise TypeCannotBeInferred(ast)
                                
                                rhsType = lhsType

                            else:
                                raise TypeCannotBeInferred(ast)
                            
                        if type(lhsType.eleType) is not type(rhsType.eleType) or lhsType.size != rhsType.size:
                            raise TypeMismatchInStatement(ast)
        self.arr_ast = []
            
    def visitBinaryOp(self, ast: BinaryOp, param):
      
        expr1, expr2 = self.visit(ast.left, param), self.visit(ast.right, param)

        if ast.op in ['+', '-', '*', '/', '%', '=', '!=', '<', '>', '>=', '<=']:
            if expr1 is None:
                if type(ast.left) in [Id, CallExpr]:
                    self.resolveType(ast.left, NumberType(), param)
                    expr1 = NumberType()
                    if self.resolved == False:
                        return None
                
                else:
                    return None 
            
            if expr2 is None:
                if type(ast.right) in [Id, CallExpr]:
                    self.resolveType(ast.right, NumberType(), param)
                    expr2 = NumberType()
                    if self.resolved == False:
                        return None 
                    
                else:
                    return None 
                
            if type(expr1) is not NumberType() or type(expr2) is not NumberType():
                raise TypeMismatchInExpression(ast)
            
            return NumberType() if ast.op in ['+', '-', '*', '/', '%'] else BoolType()
        
        elif ast.op in ['and', 'or']:
            if expr1 is None:
                if type(ast.left) in [Id, CallExpr]:
                    self.resolveType(ast.left, BoolType(), param)
                    expr1 = BoolType()
                    if self.resolved == False:
                        return None
                
                else:
                    return None 

            if expr2 is None:
                if type(ast.right) in [Id, CallExpr]:
                    self.resolveType(ast.right, BoolType(), param)
                    expr1 = BoolType()
                    if self.resolved == False:
                        return None
                
                else:
                    return None 

            if type(expr1) is not BoolType() or type(expr2) is not BoolType():
                raise TypeMismatchInExpression(ast)
            
            return BoolType()
        
        else:
            if expr1 is None:
                if type(ast.left) in [Id, CallExpr]:
                    self.resolveType(ast.left, StringType(), param)
                    expr1 = StringType()
                    if self.resolved == False:
                        return None
                
                else:
                    return None 

            if expr2 is None:
                if type(ast.right) in [Id, CallExpr]:
                    self.resolveType(ast.right, StringType(), param)
                    expr1 = StringType()
                    if self.resolved == False:
                        return None
                
                else:
                    return None 

            if type(expr1) is not StringType() or type(expr2) is not StringType():
                raise TypeMismatchInExpression(ast)  

            return StringType() if ast.op == '...' else BoolType()          
  
    def visitUnaryOp(self, ast: UnaryOp, param):
        exprType = self.visit(ast.operand, param)
        if ast.op in ['+', '-']:
            if exprType is None:
                if type(ast.operand) in [Id, CallExpr]:
                    self.resolveType(ast.operand, NumberType(), param)
                    if self.resolveType == False:
                        raise None

                    else:
                        return NumberType()
                else:
                    return None
            
            else:
                if type(exprType) is not NumberType:
                    raise TypeMismatchInExpression(ast)
                
                else:
                    return NumberType()
        
        else:
            if exprType is None:
                if type(ast.operand) in [Id, CallExpr]:
                    self.resolveType(ast.operand, BoolType(), param)
                    if self.resolved == False:
                        return None 
                    
                    else:
                        return BoolType()
                
                else:
                    return None
            
            else:
                if type(exprType) is not BoolType:
                    raise TypeMismatchInExpression(ast)
                else:
                    return BoolType()
    
    def visitArrayCell(self, ast: ArrayCell, param):
        self.resolved = True
        first = self.visit(ast.arr, param)
        if first is None:
            self.resolved = False
            return None 
        
        else: 
            if type(first) is not ArrayType:
                raise TypeMismatchInExpression(ast)
            
            else:
                if len(first.size) < len(ast.idx):
                    raise TypeMismatchInExpression(ast)
                
                else:
                    for idx in range(len(ast.idx)):
                        typ = self.visit(ast.idx[idx], param)
                        if typ is None:
                            if typ(ast.idx[idx]) in [Id, CallExpr]:
                                self.resolveType(ast.idx[idx], NumberType(), param)
                                if self.resolved == False:
                                    return None 
                                
                                else:
                                    return NumberType()
                                
                            else:
                                return None
                        
                        if type(typ) is not NumberType:
                            raise TypeMismatchInExpression(ast)
                        
                    return first.eleType if len(first.size) == len(ast.idx) else ArrayType(first.size[len(ast.idx):], first.eleType)

    def visitBlock(self, ast: Block, param):
        param = [[]] + param 
        for stmt in ast.stmt:
            self.visit(stmt, param)

        self.has_return = False 
        param = param[1:]
        self.arr_ast = []
          
    def visitContinue(self, ast: Continue, param):
        if self.in_loop == []:
            raise MustInLoop(ast)      

    def visitBreak(self, ast: Break, param):
        if self.in_loop == []:
            raise MustInLoop(ast)

    def visitNumberType(self, ast: NumberType, param): 
        return NumberType()
    
    def visitBoolType(self, ast: BoolType, param): 
        return BoolType()
    
    def visitStringType(self, ast: StringType, param): 
        return StringType()
    
    def visitArrayType(self, ast: ArrayType, param): 
        return ArrayType(ast.size, ast.eleType)

    def visitNumberLiteral(self, ast: NumberLiteral, param): 
        return NumberType()
    
    def visitBooleanLiteral(self, ast: BooleanLiteral, param): 
        return BoolType()
    
    def visitStringLiteral(self, ast: StringLiteral, param): 
        return StringType()

    def visitArrayLiteral(self, ast: ArrayLiteral, param):
        if ast not in self.arr_ast:
            self.arr_ast += [ast]

        typ = None 
        for val in ast.value:
            typ = self.visit(val, param)
            if typ is not None:
                break

        if typ is not None:
            for idx in range(len(ast.value)):
                val_typ = self.visit(ast.value[idx], param)
                if val_typ is None:
                    if type(ast.value[idx]) in [Id, CallExpr, ArrayLiteral]:
                        self.resolveType(ast.value[idx], typ, param)
                        if self.resolved == False:
                            return None
                        
                        else:
                            val_typ = typ
                    
                    else: 
                        return None 
                    
                if type(val_typ) is not type(typ):
                    raise TypeMismatchInExpression(self.arr_ast[0])
                
                else:
                    if type(val_typ) is ArrayType:
                        if val_typ.size[:len(typ.size)] != typ.size:
                            raise TypeMismatchInExpression(self.arr_ast[0])
                        
                        else:
                            if val_typ.eleType is None:
                                if type(ast.value) in [Id, CallExpr, ArrayLiteral]:
                                    self.resolveType(ast.value, typ, param)
                                    if self.resolved == False:
                                        return None
                                    
                                    val_typ = typ 
                                
                                else:
                                    return None 
                                
                            if type(val_typ.eleType) is not type(typ.eleType) or val_typ.size != typ.size:
                                raise TypeMismatchInExpression(self.arr_ast[0])
                            
            if type(typ) is not ArrayType:
                self.arr_ast = self.arr_ast[:-1]
                return ArrayType([len(ast.value)], typ)
            
            else: 
                self.arr_ast = self.arr_ast[:-1]
                return ArrayType([len(ast.value)] + typ.size, typ.eleType)
