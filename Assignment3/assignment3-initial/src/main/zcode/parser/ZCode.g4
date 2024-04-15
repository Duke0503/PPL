/* ID :2113206 */ 
grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

// Program Rule
program: (COMMENTS NEWLINE | NEWLINE)* decllist EOF;

decllist: decl decllist | decl;

// Combined Declaration Rule
decl: vardecl ignore | funcdecl;

// Variable Decleration
vardecl: type_var | implicit_var | implicit_dynamic;

type_var: typ ID (ASSIGN expr)? | typ ID LS arraydecllist RS (ASSIGN expr)?;

// Array Declaration
arraydecllist: NUMLIT COMMA arraydecllist | NUMLIT ;

typ: BOOL | NUMBER | STRING;

implicit_var: VAR ID ASSIGN expr;

implicit_dynamic: DYNAMIC ID (ASSIGN expr)?;

// Function Declaration
funcdecl: FUNC ID LP paramlist RP (ignore? returnstmt | ignore? blockstmt | ignore);
paramlist: paramprime | ;
paramprime: param COMMA paramprime | param;
param: typ (ID | ID LS arraydecllist RS);

// Index Operators
idxOp: (ID | callexpr) LS exprlist RS;

exprlist: expr COMMA exprlist | expr;

// Expression
expr: expr1 CONCAT expr1 | expr1;
expr1: expr2 (EQ | LEQ | NE | LT | GT | LTE | GTE) expr2 | expr2 ;
expr2: expr2 (AND | OR) expr3 | expr3;
expr3: expr3 (ADD | SUB) expr4 | expr4;
expr4: expr4 (MUL | DIV | MOD) expr5 | expr5;
expr5: (NOT) expr5 | expr6; 
expr6: (SUB | ADD) expr6 | expr7;
expr7: idxOp | expr8 ;
expr8: ID | literal | subexpr | callexpr;

// List Of Operands

subexpr: LP expr RP;
callexpr: ID LP exprlist? RP;

// Statements
stmtlist: stmt stmtlist | ;
stmt 
	: declstmt
	| assignstmt
	| ifstmt
	| forstmt
	| breakstmt
	| continuestmt
	| returnstmt
	| callstmt
	| blockstmt
	;

// Variable Declaration Statement
declstmt: vardecl ignore;

lhs: ID | idxOp;

// Assignment Statement
assignstmt: lhs ASSIGN expr ignore;

// If Statement
ifstmt: IF LP expr RP ignore? stmt ignore? elifstmtlist (elsestmt | );
elifstmtlist: elifstmtprime | ;
elifstmtprime: elifstmt elifstmtprime | elifstmt;
elifstmt: ELIF LP expr RP ignore? stmt ignore?;
elsestmt: ELSE ignore? stmt ignore?;

// For Statement
forstmt: FOR ID UNTIL expr BY expr ignore?
	stmt;

// Break Statement
breakstmt: BREAK ignore;

// Continue Statement
continuestmt: CONTINUE ignore;

// Return Statement
returnstmt: RETURN expr? ignore;

// Function Call Statement
callstmt: ID LP (exprlist| ) RP ignore;

// Block Statement
blockstmt: 
	BEGIN ignore
		stmtlist
	END ignore;

// Ignore Keyword
ignore: NEWLINE+;

// KeyWords
TRUE: 'true';
FALSE: 'false';
NUMBER: 'number';
BOOL: 'bool';
STRING: 'string';
RETURN: 'return';
VAR: 'var';
DYNAMIC: 'dynamic';
FUNC: 'func';
FOR: 'for';
UNTIL: 'until';
BY: 'by';
BREAK: 'break';
CONTINUE: 'continue';
IF: 'if';
ELSE: 'else';
ELIF: 'elif';
BEGIN: 'begin';
END: 'end';
NOT: 'not';
AND: 'and';
OR: 'or';

// Operators
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
EQ: '=';
ASSIGN: '<-';
NE: '!=';
LT: '<';
LTE: '<=';
GT: '>';
GTE: '>=';
CONCAT: '...';
LEQ: '==';

// Separators
LP: '(';
RP: ')';
LS: '[';
RS: ']';
COMMA: ',';

// Identifiers
ID: [a-zA-Z_][a-zA-Z0-9_]*;

// Literals
literal: NUMLIT | TRUE | FALSE | STRINGLIT | array_literal;

NUMLIT 
		: DigitSequence
    | DigitSequence DecimalPart ExponentPart
    | DigitSequence DecimalPart
    | DigitSequence ExponentPart
    ;

fragment DIGIT: [0-9];
fragment DigitSequence: DIGIT+;
fragment Exponent: [Ee];
fragment SIGN: [+-];
fragment DOT: '.';
fragment DecimalPart: DOT DigitSequence?;
fragment ExponentPart: Exponent SIGN? DigitSequence;

STRINGLIT: '"' (CHAR)* '"'{self.text = self.text[1:-1];};
fragment CHAR: (~[\r\n\f\\"] | '\\' [bfrnt'\\] | '\'"' );
fragment ILLEGAL: [\r\f] | '\\' ~[bfrnt'\\];

array_literal: LS (exprlist |) RS;


// Comments
NEWLINE: '\n';
COMMENTS: '##' .*? ~[\n\r\f]* -> skip; 

WS : [ \t\r]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: '"' (CHAR)* ('\r\n' | '\n' | EOF)
	{
		if self.text[-1] == '\n' and self.text[-2] == '\r':
			raise UncloseString(self.text[1:-2])
		elif self.text[-1] == '\n':
			raise UncloseString(self.text[1:-1])
		else:
			raise UncloseString(self.text[1:])
	};
ILLEGAL_ESCAPE: '"' (CHAR)* ILLEGAL
	{
		raise IllegalEscape(self.text[1:])
	};