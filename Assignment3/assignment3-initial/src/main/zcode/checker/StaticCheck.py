from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class Zcode(Type):
    pass

class FuncZcode(Zcode):
    def __init__(self, param = [], typ = None, body = False):
        self.param = param
        self.typ = typ
        self.body = body

class VarZcode(Zcode):  
    def __init__(self, typ = None):
        self.typ = typ    

class ArrayZcode(Type):
    def __init__(self, eleType):
        self.eleType = eleType

class StaticChecker(BaseVisitor, Utils):
    def __init__(self,ast):
        self.ast = ast 
        self.BlockFor = 0
        self.function = None
        self.Return = False
        self.listFunction = {
            "readNumber" : FuncZcode([], NumberType(), True),
            "readBool" : FuncZcode([], BoolType(), True),
            "readString" : FuncZcode([], StringType(), True),
            "writeNumber" : FuncZcode([NumberType()], VoidType(), True),
            "writeBool" : FuncZcode([BoolType()], VoidType(), True),
            "writeString" : FuncZcode([StringType()], VoidType(), True)
        }
        
        
    def check(self):
        self.visit(self.ast, [{}])
        return None
    

    def comparType(self, LHS, RHS):

        if isinstance(LHS, (VoidType, NumberType, StringType, BoolType, ArrayType)) and isinstance(RHS, (VoidType, NumberType, StringType, BoolType, ArrayType)):
            
            if (type(LHS) is ArrayType and RHS is ArrayType):
                if LHS.size != RHS.size or type(LHS.eleType) is not type(RHS.eleType):
                    return False 
                
                else:
                    for idx in range(len(LHS)):
                        if LHS[idx].typ != RHS[idx].typ:
                            return False 
            
            else:
                if type(LHS) is not type(RHS):
                    return False

            return True 
        
        return False
                        
    
    def comparListType(self, LHS, RHS):
        if len(LHS) != len(RHS):
            return False 
        
        else:
            for idx in range(len(LHS)):
                self.comparType(LHS[idx], RHS[idx])  


    
    def setTypeArray(self, typeArray, typeArrayZcode):

        if len(typeArray.size) != len(typeArrayZcode.size):
            return False
        
        if len(typeArray.size) == 1:

            for idx in range(len(typeArrayZcode.size)):
                if type(typeArrayZcode.size[idx]) is Zcode:
                    typeArrayZcode.size[idx].typ = typeArray.eleType

                else:
                    if typeArrayZcode.size[idx] is ArrayZcode:
                        return False  
        else:

            for idx in range(len(typeArrayZcode.size)):
                if type(typeArrayZcode.size[idx]) is Zcode:
                    typeArrayZcode.size[idx].typ = typeArray.eleType

                else:
                    if typeArrayZcode.size[idx] is ArrayZcode:
                        self.setTypeArray(ArrayType(typeArray.size[1:], typeArray.eleType),typeArrayZcode[idx])
        
        return True

    def setType(self, expr: Id | CallExpr | CallStmt, typ: Type, param):

        if type(expr) is Id:
            idex = None 
            for idx in range(len(param)):
                sym = param[idx].get(expr.name)
                if sym is not None and isinstance(sym, VarZcode):
                    idex = idx
                    break 

            if idex is not None:
                if isinstance(param[idex][expr.name], VarZcode) and param[idex][expr.name].typ is None:
                    param[idex][expr.name] = VarZcode(typ)

        else:
            sym = self.listFunction.get(expr.name.name)

            if sym is not None:
                if sym.typ is None:
                    param[-1][expr.name.name] = FuncZcode(sym.param, typ, sym.body)
                    self.listFunction[expr.name.name] = FuncZcode(sym.param, typ, sym.body)


    def visitProgram(self, ast, param):

        for decl in ast.decl: 
            self.visit(decl, param)
        
        for name, func in self.listFunction.items():
            if func.body == False:
                raise NoDefinition(name)

        flag = False

        main_function = self.listFunction.get("main")

        if main_function is not None and main_function.param == [] and type(main_function.typ) is VoidType:
            flag = True 

        if not flag:
            raise NoEntryPoint()

    def visitVarDecl(self, ast, param):

        if ast.name.name in param[0]:
            raise Redeclared(Variable(), ast.name.name)
        
        param[0][ast.name.name] = VarZcode(ast.varType)

        if ast.varInit:
            
            LHS = ast.varType
            RHS_type = self.visit(ast.varInit, param)
            RHS = None

            if isinstance(RHS_type, VarZcode):
                RHS = RHS_type.typ
            else:
                RHS = RHS_type
           
            if LHS is None and RHS is None:
                raise TypeCannotBeInferred(ast)
            
            elif LHS is None and type(RHS) is ArrayType:
                raise TypeCannotBeInferred(ast)
            
            elif LHS is not None and type(RHS) is ArrayType:
                if isinstance(LHS, (StringType, BoolType, NumberType)):
                    raise TypeMismatchInStatement(ast)
                
                else:
                    if type(LHS) is ArrayType:
                        if not self.setTypeArray(LHS, RHS):
                            raise TypeMismatchInStatement(ast)
            
            elif LHS is None and isinstance(RHS, (StringType, BoolType, NumberType, ArrayType)):
                param[0][ast.name.name].typ = RHS

            elif isinstance(LHS, (StringType, BoolType, NumberType, ArrayType)) and RHS is None:
                param[0][ast.varInit.name].typ = LHS
            
            else:
                if isinstance(LHS, (StringType, BoolType, NumberType, ArrayType)) and isinstance(RHS, (StringType, BoolType, NumberType, ArrayType)):
                    if not self.comparType(LHS, RHS):
                        raise TypeMismatchInStatement(ast)
        

    def visitFuncDecl(self, ast, param):

        method = param[-1].get(ast.name.name)

        if method is not None:
            if isinstance(method, FuncZcode):
                if method.body == True or (method.body == False and ast.body is None):
                    raise Redeclared(Function(), ast.name.name)
            else:
                raise Redeclared(Function(), ast.name.name)
        
        
        listParam = {}
        typeParam = []

        for para in ast.param:

            if listParam.get(para.name.name) is not None:
                raise Redeclared(Parameter(), para.name.name)

            typeParam += [para.varType]
            listParam[para.name.name] = VarZcode(para.varType)
      
        self.Return = False
        if ast.body is None:
            if method is None:
                self.listFunction[ast.name.name] = FuncZcode(ast.param, None, False)
                param[-1][ast.name.name] = FuncZcode(ast.param, None, False)

        else:
            if method:
                if len(method.param) != len(typeParam):
                    raise Redeclared(Function(), ast.name.name)

                for idx in range(len(method.param)):
                    if not self.comparType(method.param[idx].varType, typeParam[idx]):
                        raise Redeclared(Function(), ast.name.name)

                self.listFunction[ast.name.name].body = True 
                
                self.function = method
                self.visit(ast.body, [listParam] + param)

                if self.function.typ is None:
                    self.Return = False
                else: 
                    self.Return = True

                if not self.Return:
                    if self.function.typ is None or isinstance(self.function.typ, VoidType):
                        self.function.typ = VoidType()
                        
                    else:
                        raise TypeMismatchInStatement(Return(None))
                
                self.listFunction[ast.name.name] = FuncZcode(ast.param, self.function.typ, True)  
                param[-1][ast.name.name] = FuncZcode(ast.param, self.function.typ, True)
                
            else:
                self.listFunction[ast.name.name] = FuncZcode(ast.param, None, True)  
                
                self.function = self.listFunction[ast.name.name] 

                self.visit(ast.body, [listParam] + param)
                         
                if self.function.typ is None:
                    self.Return = False
                else: 
                    self.Return = True
                                   
                if not self.Return:
                    if self.function.typ is None or isinstance(self.function.typ, VoidType):
                        self.function.typ = VoidType()
                    else:
                        raise TypeMismatchInStatement(Return(None))
                
                self.listFunction[ast.name.name] = FuncZcode(ast.param, self.function.typ, True)  
                param[-1][ast.name.name] = FuncZcode(ast.param, self.function.typ, True) 
                
                

    def visitId(self, ast, param):

        found = None 
        
        for para in param:
            sym = para.get(ast.name)

            if sym is not None and isinstance(sym, VarZcode):
                found = sym
                break
        
        if found is None:
            raise Undeclared(Identifier(), ast.name)
        
        else:
            return found.typ


    def visitCallExpr(self, ast, param):

        method = self.listFunction.get(ast.name.name)

        if method is None or (method is not None and type(method) is not FuncZcode):
            raise Undeclared(Function(), ast.name.name)
        
        else:
            if len(method.param) != len(ast.args):
                raise TypeMismatchInExpression(ast)
            
            else:
                LHS_typ = method.param
                
                for idx in range(len(ast.args)):
                    LHS = None
                    if isinstance(LHS_typ[idx], VarZcode) or isinstance(LHS_typ[idx], FuncZcode):
                        LHS = LHS_typ[idx].typ 

                    elif isinstance(LHS_typ[idx], VarDecl):
                        LHS = LHS_typ[idx].varType

                    else: 
                        LHS = LHS_typ[idx]
                               
                    RHS = self.visit(ast.args[idx], param)
                    
                    if RHS is None:
                        self.setType(ast.args[idx], LHS, param)
                        RHS = self.visit(ast.args[idx], param)
                                  
                    if not self.comparType(LHS, RHS):
                        raise TypeMismatchInExpression(ast)
                            
            if method.typ is None:
                return method 
            
            elif self.comparType(method.typ, VoidType()):
                raise TypeMismatchInExpression(ast)
            
            else:
                return method.typ

    def visitCallStmt(self, ast, param):

        method = self.listFunction.get(ast.name.name)

        if method is None or (method is not None and type(method) is not FuncZcode):
            raise Undeclared(Function(), ast.name.name)
        
        else:
            if len(method.param) != len(ast.args):
                raise TypeMismatchInStatement(ast)
            
            else:
                LHS_typ = method.param

                for idx in range(len(ast.args)):
                    LHS = None
                    if isinstance(LHS_typ[idx], VarZcode) or isinstance(LHS_typ[idx], FuncZcode):
                        LHS = LHS_typ[idx].typ 

                    elif isinstance(LHS_typ[idx], VarDecl):
                        LHS = LHS_typ[idx].varType

                    else: 
                        LHS = LHS_typ[idx]

                    RHS = self.visit(ast.args[idx], param)
                    if RHS is None:
                        self.setType(ast.args[idx], LHS, param)
                        RHS = self.visit(ast.args[idx], param)
                    

                    if not self.comparType(LHS, RHS):
                        raise TypeMismatchInStatement(ast)
            
            if method.typ is None:
                return method 
            
            elif not self.comparType(method.typ, VoidType()):
                raise TypeMismatchInStatement(ast)
            
            else:
                return method.typ        


    def visitIf(self, ast, param):

        expr = self.visit(ast.expr, param)
        typExpr = None

        if type(expr) is FuncZcode or type(expr) is VarZcode:
            if expr.typ is None:
                self.setType(ast.expr, BoolType(), param)
                typExpr = BoolType()

            else:
                typExpr = expr.typ

        elif expr is None: 
            self.setType(ast.expr, BoolType(), param)
            typExpr = BoolType()

        else:
            typExpr = expr

        if not self.comparType(typExpr, BoolType()):          
            raise TypeMismatchInStatement(ast)
        
        self.visit(ast.thenStmt, [{}] + param)

        for elifExpr, elif_stmt in ast.elifStmt:
            elifStmt = self.visit(elifExpr, param)
            typElifStmt = None

            if type(elifStmt) is FuncZcode or type(expr) is VarZcode:
                if elifStmt.typ is None:
                    self.setType(ast.elifExpr, BoolType(), param)
                    typElifStmt = BoolType()

                else:
                    typElifStmt = elifStmt.typ

            elif elifStmt is None: 
                self.setType(ast.elifExpr, BoolType(), param)
                typElifStmt = BoolType()

            else:
                typElifStmt = elifStmt
               
            if not self.comparType(BoolType(), typElifStmt):
                raise TypeMismatchInStatement(ast)
            
            self.visit(elif_stmt, param)
          
        if ast.elseStmt is not None:
            self.visit(ast.elseStmt, [{}] + param)
        
    def visitFor(self, ast, param):

        typId = self.visit(ast.name, param)

        if typId is None:
            self.setType(ast.name, NumberType(), param)
            typId = self.visit(ast.name, param)  

        if not self.comparType(NumberType(), typId):
            raise TypeMismatchInStatement(ast)
        
        typCondExpr = self.visit(ast.condExpr, param)

        if typCondExpr is None:
            self.setType(ast.condExpr, BoolType(), param)
            typCondExpr = self.visit(ast.condExpr, param)

        if not self.comparType(BoolType(), typCondExpr):
            raise TypeMismatchInStatement(ast)
 
        typUpdExpr = self.visit(ast.updExpr, param)

        if typUpdExpr is None:
            self.setType(ast.updExpr, NumberType(), param)
            typUpdExpr = self.visit(ast.updExpr, param)      

        if not self.comparType(NumberType(), typUpdExpr):
            raise TypeMismatchInStatement(ast)        
        
        self.BlockFor += 1
        self.visit(ast.body, [{}] + param)
        self.BlockFor -= 1
    
    def visitReturn(self, ast, param):
        
        self.Return = True

        LHS = self.function.typ

        RHS_type = self.visit(ast.expr, param) if ast.expr else VoidType()
          
        RHS = None
        
        if isinstance(RHS_type, VarZcode) or isinstance(RHS_type, FuncZcode):
            RHS = RHS_type.typ
        
        else: 
            RHS = RHS_type

        if LHS is None and RHS is None:
            raise TypeCannotBeInferred(ast)
        
        elif LHS is None and type(RHS) is ArrayZcode:
            raise TypeCannotBeInferred(ast)
        
        elif LHS is not None and type(RHS) is ArrayZcode:
            if isinstance(LHS, (StringType, BoolType, NumberType)):
                raise TypeMismatchInStatement(ast)
            
            else:
                if LHS is ArrayType:
                    if not self.setTypeArray(LHS, RHS):
                        raise TypeMismatchInStatement(ast)
        
        elif LHS is None and isinstance(RHS, (StringType, BoolType, NumberType, ArrayType)):
            self.function.typ = RHS
            
        elif isinstance(LHS, (StringType, BoolType, NumberType, ArrayType)) and RHS is None:
            self.setType(ast.expr, LHS, param)
        
        else:
            if isinstance(LHS, (StringType, BoolType, NumberType, ArrayType)) and isinstance(RHS, (StringType, BoolType, NumberType, ArrayType)):
                if not self.comparType(LHS, RHS):
                    raise TypeMismatchInStatement(ast)


    def visitAssign(self, ast, param):

        LHS_type = self.visit(ast.lhs, param)
        RHS_type = self.visit(ast.rhs, param)
        LHS = None 
        RHS = None
        if isinstance(LHS_type, VarZcode) or isinstance(LHS_type, FuncZcode):
            LHS = LHS_type.typ 
        else:
            LHS = LHS_type

        if isinstance(RHS_type, VarZcode) or isinstance(RHS_type, FuncZcode):
            RHS = RHS_type.typ 
        else:
            RHS = RHS_type

        if LHS is None and RHS is None:
            raise TypeCannotBeInferred(ast)
        
        elif LHS is None and type(RHS) is ArrayZcode:
            raise TypeCannotBeInferred(ast)
        
        elif LHS is not None and type(RHS) is ArrayZcode:
            if isinstance(LHS, (StringType, BoolType, NumberType)):
                raise TypeMismatchInStatement(ast)
            
            else:
                if type(LHS) is ArrayType:
                    if not self.setTypeArray(LHS, RHS):
                        raise TypeMismatchInStatement(ast)
        
        elif LHS is None and isinstance(RHS, (StringType, BoolType, NumberType, ArrayType)):
            LHS = RHS

        elif isinstance(LHS, (StringType, BoolType, NumberType, ArrayType)) and RHS is None:
            RHS = LHS
        
        else:
            if isinstance(LHS, (StringType, BoolType, NumberType, ArrayType)) and isinstance(RHS, (StringType, BoolType, NumberType, ArrayType)):
                if not self.comparType(LHS, RHS):
                    raise TypeMismatchInStatement(ast) 
                           
    def visitBinaryOp(self, ast, param):

        op = ast.op
           
        left = self.visit(ast.left, param)
  
        if op in ['+', '-', '*', '/', '%', '=', '!=', '<', '>', '>=', '<=']:
            LHS = NumberType()
            if left is None:
                self.setType(ast.left, LHS, param)
            else:
                if type(left) is not NumberType:
                    raise TypeMismatchInExpression(ast)
                
        elif op in ['and', 'or']:
            LHS = BoolType()
            if left is None:
                self.setType(ast.left, LHS, param)
            else:
                if type(left) is not BoolType:
                    raise TypeMismatchInExpression(ast)    

        else:
            LHS = StringType()
            if left is None:
                self.setType(ast.left, LHS, param)
            else:
                if type(left) is not StringType:
                    raise TypeMismatchInExpression(ast)     
                                  
        right = self.visit(ast.right, param)

        if op in ['+', '-', '*', '/', '%', '=', '!=', '<', '>', '>=', '<=']:
            LHS = NumberType()
            if right is None:
                self.setType(ast.right, LHS, param)
            else:
                if type(right) is not NumberType:
                    raise TypeMismatchInExpression(ast)
            
        elif op in ['and', 'or']:
            LHS = BoolType()
            if right is None:
                self.setType(ast.right, LHS, param)
            else:
                if type(right) is not BoolType:
                    raise TypeMismatchInExpression(ast)   

        else:
            LHS = StringType()
            if right is None:
                self.setType(ast.right, LHS, param)
            else:
                if type(right) is not StringType:
                    raise TypeMismatchInExpression(ast)  
            
        if ast.op in ['+', '-', '*', '/', '%']:
            return NumberType()
        elif ast.op in ['=', '!=', '<', '>', '>=', '<=', 'and', 'or', '==']:
            return BoolType()
        else:
            return StringType()


    def visitUnaryOp(self, ast, param):

        right = self.visit(ast.operand, param)
        op = ast.op

        if op in ['+', '-']:
            LHS = NumberType()
            if right is None:
                self.setType(ast.operand, LHS, param)

            else:
                if type(right) is not NumberType:
                    raise TypeMismatchInExpression(ast)
                
            return NumberType() 
        
        else:
            LHS = BoolType()
            if right is None:
                self.setType(ast.operand, LHS, param)

            else:
                if type(right) is not BoolType:
                    raise TypeMismatchInExpression(ast)
                
            return BoolType()             

            

    def visitArrayCell(self, ast, param):

        left = self.visit(ast.arr, param)
        if type(left) is not ArrayType:
            raise TypeMismatchInExpression(ast)

        for idx in range(len(ast.idx)):
            typ =self.visit(ast.idx[idx], param)
            LHS = NumberType()
            if typ is None:
                self.setType(ast.idx[idx], LHS, param)

            else:
                if type(typ) is not NumberType:
                    raise TypeMismatchInExpression(ast)

        if len(left.size) < len(ast.idx):
            raise TypeMismatchInExpression(ast)
        
        elif len(left.size) == len(ast.idx):
            return left.eleType
        
        else:
            return ArrayType(left.size[len(ast.idx):], left.eleType)

    def visitArrayLiteral(self, ast, param):
        typ = None
        for item in ast.value:

            checkTyp = self.visit(item, param)

            if not (isinstance(checkTyp, Zcode) or isinstance(checkTyp, ArrayZcode)):

                typ = checkTyp
                break

        if typ is None:
            return typ
        
        elif type(typ) in [StringType, BoolType, NumberType]:
            for idx in ast.value:
                idxType = self.visit(idx, param)
                if (isinstance(idxType, ArrayZcode) or not self.comparType(idxType, typ)):
                    raise TypeMismatchInExpression(ast)
                
            return ArrayType([len(ast.value)], typ)
        else:
            if type(typ) is ArrayType:
                for idx in ast.value:       
                    idxType = self.visit(idx, param)
                    if not self.comparType(idxType, typ):
                        raise TypeMismatchInExpression(ast)
                    
                    if idxType is ArrayType:
                        self.setTypeArray(typ, idxType)

            return ArrayType([len(ast.value)] + typ.size, typ.eleType)
            

    def visitBlock(self, ast, param):
        for item in ast.stmt:
            if type(item) is Block: 
                self.visit(item, [{}] + param)
            else: 
                self.visit(item, param) 


    def visitContinue(self, ast, param):
        if self.BlockFor == 0: 
            raise MustInLoop(ast)


    def visitBreak(self, ast, param):
        if self.BlockFor == 0: 
            raise MustInLoop(ast)   
        

    def visitNumberType(self, ast, param): 
        return ast
    

    def visitBoolType(self, ast, param): 
        return ast
    

    def visitStringType(self, ast, param): 
        return ast
    

    def visitArrayType(self, ast, param): 
        return ast
    

    def visitNumberLiteral(self, ast, param): 
        return NumberType()
    

    def visitBooleanLiteral(self, ast, param): 
        return BoolType()
    

    def visitStringLiteral(self, ast, param): 
        return StringType()