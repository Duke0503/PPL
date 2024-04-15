from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *


class ASTGeneration(ZCodeVisitor):
    # Checked
    # program: (COMMENTS NEWLINE | NEWLINE)* decllist EOF;
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return Program(self.visit(ctx.decllist()))

    # Checked
    # decllist: decl decllist | decl;
    def visitDecllist(self, ctx:ZCodeParser.DecllistContext):
        if ctx.decllist(): 
            decl = self.visit(ctx.decl()) 
            decllist = self.visit(ctx.decllist())
            return [decl] + decllist 
        else: 
            return [self.visit(ctx.decl())]

    # Checked
    # decl: vardecl ignore | funcdecl;.
    def visitDecl(self, ctx:ZCodeParser.DeclContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl())
        else:
            return self.visit(ctx.funcdecl())

    # Checked
    # vardecl: type_var | implicit_var | implicit_dynamic;
    def visitVardecl(self, ctx:ZCodeParser.VardeclContext):
        if ctx.type_var():
            return self.visit(ctx.type_var())
        elif ctx.implicit_var():
            return self.visit(ctx.implicit_var())
        else: 
            return self.visit(ctx.implicit_dynamic())

    # Checked
    # type_var: typ ID (ASSIGN expr)? | typ ID LS arraydecllist RS (ASSIGN expr)?;
    def visitType_var(self, ctx:ZCodeParser.Type_varContext):
        var_type = self.visit(ctx.typ())
        var_name = Id(ctx.ID().getText())
        var_init = None
        if ctx.arraydecllist():
            array_type = ArrayType(self.visit(ctx.arraydecllist()), var_type)
            if ctx.expr():
                var_init = self.visit(ctx.expr())
            return VarDecl(var_name, array_type, None, var_init)
        elif ctx.expr():
            var_init = self.visit(ctx.expr())
        return VarDecl(var_name, var_type, None, var_init)


    # arraydecllist: NUMLIT COMMA arraydecllist | NUMLIT;
    def visitArraydecllist(self, ctx:ZCodeParser.ArraydecllistContext):
        if ctx.arraydecllist():
            return [float(ctx.NUMLIT().getText())] + self.visit(ctx.arraydecllist())
        return [float(ctx.NUMLIT().getText())]


    # Checked
    # typ: BOOL | NUMBER | STRING;
    def visitTyp(self, ctx:ZCodeParser.TypContext):
        if ctx.BOOL():
            return BoolType()
        elif ctx.NUMBER():
            return NumberType()
        else:
            return StringType()

    # Checked
    # implicit_var: VAR ID ASSIGN expr;
    def visitImplicit_var(self, ctx:ZCodeParser.Implicit_varContext):
        name = Id(ctx.ID().getText())
        var_init = self.visit(ctx.expr())
        return VarDecl(name, None, "var", var_init)

    # Checked
    # implicit_dynamic: DYNAMIC ID (ASSIGN expr)?;
    def visitImplicit_dynamic(self, ctx:ZCodeParser.Implicit_dynamicContext):
        name = Id(ctx.ID().getText())
        var_init = None
        if ctx.expr():
            var_init = self.visit(ctx.expr())
        return VarDecl(name, None, "dynamic", var_init)

    # Checked
    # funcdecl: FUNC ID LP paramlist RP (ignore? returnstmt | ignore? blockstmt | ignore);
    def visitFuncdecl(self, ctx:ZCodeParser.FuncdeclContext):
        func_name = Id(ctx.ID().getText())
        params = self.visit(ctx.paramlist())
        body = None
        if ctx.returnstmt():
            body = self.visit(ctx.returnstmt())
        elif ctx.blockstmt():
            body = self.visit(ctx.blockstmt())
        return FuncDecl(func_name, params, body)

    # Checked
    # paramlist: paramprime | ;
    def visitParamlist(self, ctx:ZCodeParser.ParamlistContext):
        if ctx.getChildCount() == 0:
            return []
        else: 
            return self.visit(ctx.paramprime())

    # Checked
    # paramprime: param COMMA paramprime | param;
    def visitParamprime(self, ctx:ZCodeParser.ParamprimeContext):
        if ctx.paramprime():
            return [self.visit(ctx.param())] + self.visit(ctx.paramprime())
        return [self.visit(ctx.param())]

    # Checked
    # param: typ (ID | ID LS arraydecllist RS);
    def visitParam(self, ctx:ZCodeParser.ParamContext):
        if ctx.arraydecllist():
            typ = ArrayType(self.visit(ctx.arraydecllist()), self.visit(ctx.typ()))
            return VarDecl(Id(ctx.ID().getText()), typ)
        return VarDecl(Id(ctx.ID().getText()), self.visit(ctx.typ()))

    # Checked
    # idxOp: (ID | callexpr) LS exprlist RS;
    def visitIdxOp(self, ctx:ZCodeParser.IdxOpContext):
        name = None
        if ctx.ID():
            name = Id(ctx.ID().getText())
        else:
            name = self.visit(ctx.callexpr())
        exprlist = self.visit(ctx.exprlist())
        return ArrayCell(name, exprlist)
            

    # Checked
    # exprlist: expr COMMA exprlist | expr;
    def visitExprlist(self, ctx:ZCodeParser.ExprlistContext):
        if ctx.exprlist():
            return [self.visit(ctx.expr())] + self.visit(ctx.exprlist())
        return [self.visit(ctx.expr())]

    # Checked
    # expr: expr1 CONCAT expr1 | expr1;
    def visitExpr(self, ctx:ZCodeParser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr1(0))
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.expr1(0))
        right = self.visit(ctx.expr1(1))
        return BinaryOp(op, left, right)

    # Checked
    # expr1: expr2 (EQ | LEQ | NE | LT | GT | LTE | GTE) expr2 | expr2 ;
    def visitExpr1(self, ctx:ZCodeParser.Expr1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr2(0))
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.expr2(0))
        right = self.visit(ctx.expr2(1))
        return BinaryOp(op, left, right)        

    # Checked
    # expr2: expr2 (AND | OR) expr3 | expr3;
    def visitExpr2(self, ctx:ZCodeParser.Expr2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr3())
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.expr2())
        right = self.visit(ctx.expr3())
        return BinaryOp(op, left, right)

    # Checked
    # expr3: expr3 (ADD | SUB) expr4 | expr4;
    def visitExpr3(self, ctx:ZCodeParser.Expr3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr4())
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.expr3())
        right = self.visit(ctx.expr4())
        return BinaryOp(op, left, right)

    # Checked
    # expr4: expr4 (MUL | DIV | MOD) expr5 | expr5;
    def visitExpr4(self, ctx:ZCodeParser.Expr4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr5())
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.expr4())
        right = self.visit(ctx.expr5())
        return BinaryOp(op, left, right)

    # Checked
    # expr5: (NOT) expr5 | expr6; 
    def visitExpr5(self, ctx:ZCodeParser.Expr5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr6())
        op = ctx.getChild(0).getText()
        operand = self.visit(ctx.expr5())
        return UnaryOp(op, operand)

    # Checked
    # expr6: (SUB | ADD) expr6 | expr7;
    def visitExpr6(self, ctx:ZCodeParser.Expr6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr7())
        op = ctx.getChild(0).getText()
        operand = self.visit(ctx.expr6())
        return UnaryOp(op, operand)

    # Checked
    # expr7: idxOp | expr8;
    def visitExpr7(self, ctx:ZCodeParser.Expr7Context):
        if ctx.idxOp():
            return self.visit(ctx.idxOp())
        return self.visit(ctx.expr8())

    # Checked
    # expr8: ID | literal | subexpr | callexpr;
    def visitExpr8(self, ctx:ZCodeParser.Expr8Context):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.subexpr():
            return self.visit(ctx.subexpr())
        else:
            return self.visit(ctx.callexpr())

    # Checked
    # subexpr: LP expr RP;
    def visitSubexpr(self, ctx:ZCodeParser.SubexprContext):
        return self.visit(ctx.expr())

    # Checked
    # callexpr: ID LP exprlist? RP;
    def visitCallexpr(self, ctx:ZCodeParser.CallexprContext):
        args = []
        name = Id(ctx.ID().getText())
        if ctx.exprlist():
            args = self.visit(ctx.exprlist())
        return CallExpr(name, args)

    
    # stmtlist: stmt stmtlist | ;
    def visitStmtlist(self, ctx:ZCodeParser.StmtlistContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.stmt())] + self.visit(ctx.stmtlist())


    # stmt:
    def visitStmt(self, ctx:ZCodeParser.StmtContext):
        if ctx.declstmt():
            return self.visit(ctx.declstmt())
        elif ctx.assignstmt():
            return self.visit(ctx.assignstmt())
        elif ctx.ifstmt():
            return self.visit(ctx.ifstmt())
        elif ctx.forstmt():
            return self.visit(ctx.forstmt())
        elif ctx.breakstmt():
            return self.visit(ctx.breakstmt())
        elif ctx.continuestmt():
            return self.visit(ctx.continuestmt())
        elif ctx.returnstmt():
            return self.visit(ctx.returnstmt())
        elif ctx.callstmt():
            return self.visit(ctx.callstmt())
        else:
            return self.visit(ctx.blockstmt())


    # declstmt: vardecl ignore;
    def visitDeclstmt(self, ctx:ZCodeParser.DeclstmtContext):
        return self.visit(ctx.vardecl())


    # lhs: ID | idxOp;
    def visitLhs(self, ctx:ZCodeParser.LhsContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        return self.visit(ctx.idxOp())


    # assignstmt: lhs ASSIGN expr ignore;
    def visitAssignstmt(self, ctx:ZCodeParser.AssignstmtContext):
        return Assign(self.visit(ctx.lhs()), self.visit(ctx.expr()))


    # ifstmt: IF LP expr RP ignore? stmt ignore? elifstmtlist (elsestmt | );
    def visitIfstmt(self, ctx:ZCodeParser.IfstmtContext):
        expr = self.visit(ctx.expr())
        thenStmt = self.visit(ctx.stmt())
        elifStmt = []
        elseStmt = None
        if ctx.elifstmtlist():
            elifStmt = self.visit(ctx.elifstmtlist())
        if ctx.elsestmt():
            elseStmt = self.visit(ctx.elsestmt())
        return If(expr, thenStmt, elifStmt, elseStmt)


    # elifstmtlist: elifstmtprime | ;
    def visitElifstmtlist(self, ctx:ZCodeParser.ElifstmtlistContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.elifstmtprime())


    # elifstmtprime: elifstmt elifstmtprime | elifstmt;
    def visitElifstmtprime(self, ctx:ZCodeParser.ElifstmtprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.elifstmt())]
        return [self.visit(ctx.elifstmt())] + self.visit(ctx.elifstmtprime())


    # elifstmt: ELIF LP expr RP ignore? stmt ignore?;
    def visitElifstmt(self, ctx:ZCodeParser.ElifstmtContext):
        return [self.visit(ctx.expr()), self.visit(ctx.stmt())]


    # elsestmt: ELSE ignore? stmt ignore?;
    def visitElsestmt(self, ctx:ZCodeParser.ElsestmtContext):
        return self.visit(ctx.stmt())


    # forstmt: FOR ID UNTIL expr BY expr ignore? stmt;
    def visitForstmt(self, ctx:ZCodeParser.ForstmtContext):
        name = Id(ctx.ID().getText())
        condExpr = self.visit(ctx.expr(0))
        updExpr = self.visit(ctx.expr(1))
        body = self.visit(ctx.stmt())
        return For(name, condExpr, updExpr, body)


    # breakstmt: BREAK ignore;
    def visitBreakstmt(self, ctx:ZCodeParser.BreakstmtContext):
        return Break()


    # continuestmt: CONTINUE ignore;
    def visitContinuestmt(self, ctx:ZCodeParser.ContinuestmtContext):
        return Continue()
    

    # returnstmt: RETURN expr? ignore;
    def visitReturnstmt(self, ctx:ZCodeParser.ReturnstmtContext):
        expr = None
        if ctx.expr():
            expr = self.visit(ctx.expr())
        return Return(expr)


    # callstmt: ID LP (exprlist| ) RP ignore;
    def visitCallstmt(self, ctx:ZCodeParser.CallstmtContext):
        name = Id(ctx.ID().getText())
        args = []
        if ctx.exprlist():
            args = self.visit(ctx.exprlist())
        return CallStmt(name, args)


    # blockstmt: BEGIN ignore stmtlist END ignore;
    def visitBlockstmt(self, ctx:ZCodeParser.BlockstmtContext):
        return Block(self.visit(ctx.stmtlist()))


    # ignore: NEWLINE+;
    def visitIgnore(self, ctx:ZCodeParser.IgnoreContext):
        return None


    # literal: NUMLIT | TRUE | FALSE | STRINGLIT | array_literal;
    def visitLiteral(self, ctx:ZCodeParser.LiteralContext):
        if ctx.NUMLIT():
            return NumberLiteral(float(ctx.NUMLIT().getText()))
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        else:
            return self.visit(ctx.array_literal())        


    # array_literal: LS (exprlist |) RS;
    def visitArray_literal(self, ctx:ZCodeParser.Array_literalContext):
        exprlist = []
        if ctx.exprlist():
            exprlist = self.visit(ctx.exprlist())
        return ArrayLiteral(exprlist)
