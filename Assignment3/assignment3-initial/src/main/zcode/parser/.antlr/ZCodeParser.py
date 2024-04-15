# Generated from d:/.LEARN/HK6/PPL/Assignment3/assignment3-initial/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,50,415,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,1,0,1,0,1,0,5,
        0,94,8,0,10,0,12,0,97,9,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,106,8,
        1,1,2,1,2,1,2,1,2,3,2,112,8,2,1,3,1,3,1,3,3,3,117,8,3,1,4,1,4,1,
        4,1,4,3,4,123,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,132,8,4,3,4,134,
        8,4,1,5,1,5,1,5,1,5,3,5,140,8,5,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,8,
        1,8,1,8,1,8,3,8,153,8,8,1,9,1,9,1,9,1,9,1,9,1,9,3,9,161,8,9,1,9,
        1,9,3,9,165,8,9,1,9,1,9,3,9,169,8,9,1,10,1,10,3,10,173,8,10,1,11,
        1,11,1,11,1,11,1,11,3,11,180,8,11,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,3,12,189,8,12,1,13,1,13,3,13,193,8,13,1,13,1,13,1,13,1,13,1,
        14,1,14,1,14,1,14,1,14,3,14,204,8,14,1,15,1,15,1,15,1,15,1,15,3,
        15,211,8,15,1,16,1,16,1,16,1,16,1,16,3,16,218,8,16,1,17,1,17,1,17,
        1,17,1,17,1,17,5,17,226,8,17,10,17,12,17,229,9,17,1,18,1,18,1,18,
        1,18,1,18,1,18,5,18,237,8,18,10,18,12,18,240,9,18,1,19,1,19,1,19,
        1,19,1,19,1,19,5,19,248,8,19,10,19,12,19,251,9,19,1,20,1,20,1,20,
        3,20,256,8,20,1,21,1,21,1,21,3,21,261,8,21,1,22,1,22,3,22,265,8,
        22,1,23,1,23,1,23,1,23,3,23,271,8,23,1,24,1,24,1,24,1,24,1,25,1,
        25,1,25,3,25,280,8,25,1,25,1,25,1,26,1,26,1,26,1,26,3,26,288,8,26,
        1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,3,27,299,8,27,1,28,
        1,28,1,28,1,29,1,29,3,29,306,8,29,1,30,1,30,1,30,1,30,1,30,1,31,
        1,31,1,31,1,31,1,31,3,31,318,8,31,1,31,1,31,3,31,322,8,31,1,31,1,
        31,1,31,3,31,327,8,31,1,32,1,32,3,32,331,8,32,1,33,1,33,1,33,1,33,
        3,33,337,8,33,1,34,1,34,1,34,1,34,1,34,3,34,344,8,34,1,34,1,34,3,
        34,348,8,34,1,35,1,35,3,35,352,8,35,1,35,1,35,3,35,356,8,35,1,36,
        1,36,1,36,1,36,1,36,1,36,1,36,3,36,365,8,36,1,36,1,36,1,37,1,37,
        1,37,1,38,1,38,1,38,1,39,1,39,3,39,377,8,39,1,39,1,39,1,40,1,40,
        1,40,1,40,3,40,385,8,40,1,40,1,40,1,40,1,41,1,41,1,41,1,41,1,41,
        1,41,1,42,4,42,397,8,42,11,42,12,42,398,1,43,1,43,1,43,1,43,1,43,
        3,43,406,8,43,1,44,1,44,1,44,3,44,411,8,44,1,44,1,44,1,44,0,3,34,
        36,38,45,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
        40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,
        84,86,88,0,5,1,0,3,5,3,0,28,28,30,34,36,36,1,0,21,22,1,0,23,24,1,
        0,25,27,429,0,95,1,0,0,0,2,105,1,0,0,0,4,111,1,0,0,0,6,116,1,0,0,
        0,8,133,1,0,0,0,10,139,1,0,0,0,12,141,1,0,0,0,14,143,1,0,0,0,16,
        148,1,0,0,0,18,154,1,0,0,0,20,172,1,0,0,0,22,179,1,0,0,0,24,181,
        1,0,0,0,26,192,1,0,0,0,28,203,1,0,0,0,30,210,1,0,0,0,32,217,1,0,
        0,0,34,219,1,0,0,0,36,230,1,0,0,0,38,241,1,0,0,0,40,255,1,0,0,0,
        42,260,1,0,0,0,44,264,1,0,0,0,46,270,1,0,0,0,48,272,1,0,0,0,50,276,
        1,0,0,0,52,287,1,0,0,0,54,298,1,0,0,0,56,300,1,0,0,0,58,305,1,0,
        0,0,60,307,1,0,0,0,62,312,1,0,0,0,64,330,1,0,0,0,66,336,1,0,0,0,
        68,338,1,0,0,0,70,349,1,0,0,0,72,357,1,0,0,0,74,368,1,0,0,0,76,371,
        1,0,0,0,78,374,1,0,0,0,80,380,1,0,0,0,82,389,1,0,0,0,84,396,1,0,
        0,0,86,405,1,0,0,0,88,407,1,0,0,0,90,91,5,46,0,0,91,94,5,45,0,0,
        92,94,5,45,0,0,93,90,1,0,0,0,93,92,1,0,0,0,94,97,1,0,0,0,95,93,1,
        0,0,0,95,96,1,0,0,0,96,98,1,0,0,0,97,95,1,0,0,0,98,99,3,2,1,0,99,
        100,5,0,0,1,100,1,1,0,0,0,101,102,3,4,2,0,102,103,3,2,1,0,103,106,
        1,0,0,0,104,106,3,4,2,0,105,101,1,0,0,0,105,104,1,0,0,0,106,3,1,
        0,0,0,107,108,3,6,3,0,108,109,3,84,42,0,109,112,1,0,0,0,110,112,
        3,18,9,0,111,107,1,0,0,0,111,110,1,0,0,0,112,5,1,0,0,0,113,117,3,
        8,4,0,114,117,3,14,7,0,115,117,3,16,8,0,116,113,1,0,0,0,116,114,
        1,0,0,0,116,115,1,0,0,0,117,7,1,0,0,0,118,119,3,12,6,0,119,122,5,
        42,0,0,120,121,5,29,0,0,121,123,3,30,15,0,122,120,1,0,0,0,122,123,
        1,0,0,0,123,134,1,0,0,0,124,125,3,12,6,0,125,126,5,42,0,0,126,127,
        5,39,0,0,127,128,3,10,5,0,128,131,5,40,0,0,129,130,5,29,0,0,130,
        132,3,30,15,0,131,129,1,0,0,0,131,132,1,0,0,0,132,134,1,0,0,0,133,
        118,1,0,0,0,133,124,1,0,0,0,134,9,1,0,0,0,135,136,5,43,0,0,136,137,
        5,41,0,0,137,140,3,10,5,0,138,140,5,43,0,0,139,135,1,0,0,0,139,138,
        1,0,0,0,140,11,1,0,0,0,141,142,7,0,0,0,142,13,1,0,0,0,143,144,5,
        7,0,0,144,145,5,42,0,0,145,146,5,29,0,0,146,147,3,30,15,0,147,15,
        1,0,0,0,148,149,5,8,0,0,149,152,5,42,0,0,150,151,5,29,0,0,151,153,
        3,30,15,0,152,150,1,0,0,0,152,153,1,0,0,0,153,17,1,0,0,0,154,155,
        5,9,0,0,155,156,5,42,0,0,156,157,5,37,0,0,157,158,3,20,10,0,158,
        168,5,38,0,0,159,161,3,84,42,0,160,159,1,0,0,0,160,161,1,0,0,0,161,
        162,1,0,0,0,162,169,3,78,39,0,163,165,3,84,42,0,164,163,1,0,0,0,
        164,165,1,0,0,0,165,166,1,0,0,0,166,169,3,82,41,0,167,169,3,84,42,
        0,168,160,1,0,0,0,168,164,1,0,0,0,168,167,1,0,0,0,169,19,1,0,0,0,
        170,173,3,22,11,0,171,173,1,0,0,0,172,170,1,0,0,0,172,171,1,0,0,
        0,173,21,1,0,0,0,174,175,3,24,12,0,175,176,5,41,0,0,176,177,3,22,
        11,0,177,180,1,0,0,0,178,180,3,24,12,0,179,174,1,0,0,0,179,178,1,
        0,0,0,180,23,1,0,0,0,181,188,3,12,6,0,182,189,5,42,0,0,183,184,5,
        42,0,0,184,185,5,39,0,0,185,186,3,10,5,0,186,187,5,40,0,0,187,189,
        1,0,0,0,188,182,1,0,0,0,188,183,1,0,0,0,189,25,1,0,0,0,190,193,5,
        42,0,0,191,193,3,50,25,0,192,190,1,0,0,0,192,191,1,0,0,0,193,194,
        1,0,0,0,194,195,5,39,0,0,195,196,3,28,14,0,196,197,5,40,0,0,197,
        27,1,0,0,0,198,199,3,30,15,0,199,200,5,41,0,0,200,201,3,28,14,0,
        201,204,1,0,0,0,202,204,3,30,15,0,203,198,1,0,0,0,203,202,1,0,0,
        0,204,29,1,0,0,0,205,206,3,32,16,0,206,207,5,35,0,0,207,208,3,32,
        16,0,208,211,1,0,0,0,209,211,3,32,16,0,210,205,1,0,0,0,210,209,1,
        0,0,0,211,31,1,0,0,0,212,213,3,34,17,0,213,214,7,1,0,0,214,215,3,
        34,17,0,215,218,1,0,0,0,216,218,3,34,17,0,217,212,1,0,0,0,217,216,
        1,0,0,0,218,33,1,0,0,0,219,220,6,17,-1,0,220,221,3,36,18,0,221,227,
        1,0,0,0,222,223,10,2,0,0,223,224,7,2,0,0,224,226,3,36,18,0,225,222,
        1,0,0,0,226,229,1,0,0,0,227,225,1,0,0,0,227,228,1,0,0,0,228,35,1,
        0,0,0,229,227,1,0,0,0,230,231,6,18,-1,0,231,232,3,38,19,0,232,238,
        1,0,0,0,233,234,10,2,0,0,234,235,7,3,0,0,235,237,3,38,19,0,236,233,
        1,0,0,0,237,240,1,0,0,0,238,236,1,0,0,0,238,239,1,0,0,0,239,37,1,
        0,0,0,240,238,1,0,0,0,241,242,6,19,-1,0,242,243,3,40,20,0,243,249,
        1,0,0,0,244,245,10,2,0,0,245,246,7,4,0,0,246,248,3,40,20,0,247,244,
        1,0,0,0,248,251,1,0,0,0,249,247,1,0,0,0,249,250,1,0,0,0,250,39,1,
        0,0,0,251,249,1,0,0,0,252,253,5,20,0,0,253,256,3,40,20,0,254,256,
        3,42,21,0,255,252,1,0,0,0,255,254,1,0,0,0,256,41,1,0,0,0,257,258,
        7,3,0,0,258,261,3,42,21,0,259,261,3,44,22,0,260,257,1,0,0,0,260,
        259,1,0,0,0,261,43,1,0,0,0,262,265,3,26,13,0,263,265,3,46,23,0,264,
        262,1,0,0,0,264,263,1,0,0,0,265,45,1,0,0,0,266,271,5,42,0,0,267,
        271,3,86,43,0,268,271,3,48,24,0,269,271,3,50,25,0,270,266,1,0,0,
        0,270,267,1,0,0,0,270,268,1,0,0,0,270,269,1,0,0,0,271,47,1,0,0,0,
        272,273,5,37,0,0,273,274,3,30,15,0,274,275,5,38,0,0,275,49,1,0,0,
        0,276,277,5,42,0,0,277,279,5,37,0,0,278,280,3,28,14,0,279,278,1,
        0,0,0,279,280,1,0,0,0,280,281,1,0,0,0,281,282,5,38,0,0,282,51,1,
        0,0,0,283,284,3,54,27,0,284,285,3,52,26,0,285,288,1,0,0,0,286,288,
        1,0,0,0,287,283,1,0,0,0,287,286,1,0,0,0,288,53,1,0,0,0,289,299,3,
        56,28,0,290,299,3,60,30,0,291,299,3,62,31,0,292,299,3,72,36,0,293,
        299,3,74,37,0,294,299,3,76,38,0,295,299,3,78,39,0,296,299,3,80,40,
        0,297,299,3,82,41,0,298,289,1,0,0,0,298,290,1,0,0,0,298,291,1,0,
        0,0,298,292,1,0,0,0,298,293,1,0,0,0,298,294,1,0,0,0,298,295,1,0,
        0,0,298,296,1,0,0,0,298,297,1,0,0,0,299,55,1,0,0,0,300,301,3,6,3,
        0,301,302,3,84,42,0,302,57,1,0,0,0,303,306,5,42,0,0,304,306,3,26,
        13,0,305,303,1,0,0,0,305,304,1,0,0,0,306,59,1,0,0,0,307,308,3,58,
        29,0,308,309,5,29,0,0,309,310,3,30,15,0,310,311,3,84,42,0,311,61,
        1,0,0,0,312,313,5,15,0,0,313,314,5,37,0,0,314,315,3,30,15,0,315,
        317,5,38,0,0,316,318,3,84,42,0,317,316,1,0,0,0,317,318,1,0,0,0,318,
        319,1,0,0,0,319,321,3,54,27,0,320,322,3,84,42,0,321,320,1,0,0,0,
        321,322,1,0,0,0,322,323,1,0,0,0,323,326,3,64,32,0,324,327,3,70,35,
        0,325,327,1,0,0,0,326,324,1,0,0,0,326,325,1,0,0,0,327,63,1,0,0,0,
        328,331,3,66,33,0,329,331,1,0,0,0,330,328,1,0,0,0,330,329,1,0,0,
        0,331,65,1,0,0,0,332,333,3,68,34,0,333,334,3,66,33,0,334,337,1,0,
        0,0,335,337,3,68,34,0,336,332,1,0,0,0,336,335,1,0,0,0,337,67,1,0,
        0,0,338,339,5,17,0,0,339,340,5,37,0,0,340,341,3,30,15,0,341,343,
        5,38,0,0,342,344,3,84,42,0,343,342,1,0,0,0,343,344,1,0,0,0,344,345,
        1,0,0,0,345,347,3,54,27,0,346,348,3,84,42,0,347,346,1,0,0,0,347,
        348,1,0,0,0,348,69,1,0,0,0,349,351,5,16,0,0,350,352,3,84,42,0,351,
        350,1,0,0,0,351,352,1,0,0,0,352,353,1,0,0,0,353,355,3,54,27,0,354,
        356,3,84,42,0,355,354,1,0,0,0,355,356,1,0,0,0,356,71,1,0,0,0,357,
        358,5,10,0,0,358,359,5,42,0,0,359,360,5,11,0,0,360,361,3,30,15,0,
        361,362,5,12,0,0,362,364,3,30,15,0,363,365,3,84,42,0,364,363,1,0,
        0,0,364,365,1,0,0,0,365,366,1,0,0,0,366,367,3,54,27,0,367,73,1,0,
        0,0,368,369,5,13,0,0,369,370,3,84,42,0,370,75,1,0,0,0,371,372,5,
        14,0,0,372,373,3,84,42,0,373,77,1,0,0,0,374,376,5,6,0,0,375,377,
        3,30,15,0,376,375,1,0,0,0,376,377,1,0,0,0,377,378,1,0,0,0,378,379,
        3,84,42,0,379,79,1,0,0,0,380,381,5,42,0,0,381,384,5,37,0,0,382,385,
        3,28,14,0,383,385,1,0,0,0,384,382,1,0,0,0,384,383,1,0,0,0,385,386,
        1,0,0,0,386,387,5,38,0,0,387,388,3,84,42,0,388,81,1,0,0,0,389,390,
        5,18,0,0,390,391,3,84,42,0,391,392,3,52,26,0,392,393,5,19,0,0,393,
        394,3,84,42,0,394,83,1,0,0,0,395,397,5,45,0,0,396,395,1,0,0,0,397,
        398,1,0,0,0,398,396,1,0,0,0,398,399,1,0,0,0,399,85,1,0,0,0,400,406,
        5,43,0,0,401,406,5,1,0,0,402,406,5,2,0,0,403,406,5,44,0,0,404,406,
        3,88,44,0,405,400,1,0,0,0,405,401,1,0,0,0,405,402,1,0,0,0,405,403,
        1,0,0,0,405,404,1,0,0,0,406,87,1,0,0,0,407,410,5,39,0,0,408,411,
        3,28,14,0,409,411,1,0,0,0,410,408,1,0,0,0,410,409,1,0,0,0,411,412,
        1,0,0,0,412,413,5,40,0,0,413,89,1,0,0,0,46,93,95,105,111,116,122,
        131,133,139,152,160,164,168,172,179,188,192,203,210,217,227,238,
        249,255,260,264,270,279,287,298,305,317,321,326,330,336,343,347,
        351,355,364,376,384,398,405,410
    ]

class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'true'", "'false'", "'number'", "'bool'", 
                     "'string'", "'return'", "'var'", "'dynamic'", "'func'", 
                     "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'", "'not'", 
                     "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'='", "'<-'", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'...'", "'=='", "'('", "')'", "'['", "']'", "','", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", 
                      "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", 
                      "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", 
                      "END", "NOT", "AND", "OR", "ADD", "SUB", "MUL", "DIV", 
                      "MOD", "EQ", "ASSIGN", "NE", "LT", "LTE", "GT", "GTE", 
                      "CONCAT", "LEQ", "LP", "RP", "LS", "RS", "COMMA", 
                      "ID", "NUMLIT", "STRINGLIT", "NEWLINE", "COMMENTS", 
                      "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_decllist = 1
    RULE_decl = 2
    RULE_vardecl = 3
    RULE_type_var = 4
    RULE_arraydecllist = 5
    RULE_typ = 6
    RULE_implicit_var = 7
    RULE_implicit_dynamic = 8
    RULE_funcdecl = 9
    RULE_paramlist = 10
    RULE_paramprime = 11
    RULE_param = 12
    RULE_idxOp = 13
    RULE_exprlist = 14
    RULE_expr = 15
    RULE_expr1 = 16
    RULE_expr2 = 17
    RULE_expr3 = 18
    RULE_expr4 = 19
    RULE_expr5 = 20
    RULE_expr6 = 21
    RULE_expr7 = 22
    RULE_expr8 = 23
    RULE_subexpr = 24
    RULE_callexpr = 25
    RULE_stmtlist = 26
    RULE_stmt = 27
    RULE_declstmt = 28
    RULE_lhs = 29
    RULE_assignstmt = 30
    RULE_ifstmt = 31
    RULE_elifstmtlist = 32
    RULE_elifstmtprime = 33
    RULE_elifstmt = 34
    RULE_elsestmt = 35
    RULE_forstmt = 36
    RULE_breakstmt = 37
    RULE_continuestmt = 38
    RULE_returnstmt = 39
    RULE_callstmt = 40
    RULE_blockstmt = 41
    RULE_ignore = 42
    RULE_literal = 43
    RULE_array_literal = 44

    ruleNames =  [ "program", "decllist", "decl", "vardecl", "type_var", 
                   "arraydecllist", "typ", "implicit_var", "implicit_dynamic", 
                   "funcdecl", "paramlist", "paramprime", "param", "idxOp", 
                   "exprlist", "expr", "expr1", "expr2", "expr3", "expr4", 
                   "expr5", "expr6", "expr7", "expr8", "subexpr", "callexpr", 
                   "stmtlist", "stmt", "declstmt", "lhs", "assignstmt", 
                   "ifstmt", "elifstmtlist", "elifstmtprime", "elifstmt", 
                   "elsestmt", "forstmt", "breakstmt", "continuestmt", "returnstmt", 
                   "callstmt", "blockstmt", "ignore", "literal", "array_literal" ]

    EOF = Token.EOF
    TRUE=1
    FALSE=2
    NUMBER=3
    BOOL=4
    STRING=5
    RETURN=6
    VAR=7
    DYNAMIC=8
    FUNC=9
    FOR=10
    UNTIL=11
    BY=12
    BREAK=13
    CONTINUE=14
    IF=15
    ELSE=16
    ELIF=17
    BEGIN=18
    END=19
    NOT=20
    AND=21
    OR=22
    ADD=23
    SUB=24
    MUL=25
    DIV=26
    MOD=27
    EQ=28
    ASSIGN=29
    NE=30
    LT=31
    LTE=32
    GT=33
    GTE=34
    CONCAT=35
    LEQ=36
    LP=37
    RP=38
    LS=39
    RS=40
    COMMA=41
    ID=42
    NUMLIT=43
    STRINGLIT=44
    NEWLINE=45
    COMMENTS=46
    WS=47
    ERROR_CHAR=48
    UNCLOSE_STRING=49
    ILLEGAL_ESCAPE=50

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decllist(self):
            return self.getTypedRuleContext(ZCodeParser.DecllistContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def COMMENTS(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.COMMENTS)
            else:
                return self.getToken(ZCodeParser.COMMENTS, i)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45 or _la==46:
                self.state = 93
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [46]:
                    self.state = 90
                    self.match(ZCodeParser.COMMENTS)
                    self.state = 91
                    self.match(ZCodeParser.NEWLINE)
                    pass
                elif token in [45]:
                    self.state = 92
                    self.match(ZCodeParser.NEWLINE)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 98
            self.decllist()
            self.state = 99
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecllistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(ZCodeParser.DeclContext,0)


        def decllist(self):
            return self.getTypedRuleContext(ZCodeParser.DecllistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decllist




    def decllist(self):

        localctx = ZCodeParser.DecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decllist)
        try:
            self.state = 105
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.decl()
                self.state = 102
                self.decllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.VardeclContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(ZCodeParser.FuncdeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 111
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5, 7, 8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.vardecl()
                self.state = 108
                self.ignore()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self.funcdecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_var(self):
            return self.getTypedRuleContext(ZCodeParser.Type_varContext,0)


        def implicit_var(self):
            return self.getTypedRuleContext(ZCodeParser.Implicit_varContext,0)


        def implicit_dynamic(self):
            return self.getTypedRuleContext(ZCodeParser.Implicit_dynamicContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vardecl




    def vardecl(self):

        localctx = ZCodeParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vardecl)
        try:
            self.state = 116
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.type_var()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
                self.implicit_var()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 115
                self.implicit_dynamic()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(ZCodeParser.TypContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def LS(self):
            return self.getToken(ZCodeParser.LS, 0)

        def arraydecllist(self):
            return self.getTypedRuleContext(ZCodeParser.ArraydecllistContext,0)


        def RS(self):
            return self.getToken(ZCodeParser.RS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_type_var




    def type_var(self):

        localctx = ZCodeParser.Type_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_type_var)
        self._la = 0 # Token type
        try:
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.typ()
                self.state = 119
                self.match(ZCodeParser.ID)
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==29:
                    self.state = 120
                    self.match(ZCodeParser.ASSIGN)
                    self.state = 121
                    self.expr()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                self.typ()
                self.state = 125
                self.match(ZCodeParser.ID)
                self.state = 126
                self.match(ZCodeParser.LS)
                self.state = 127
                self.arraydecllist()
                self.state = 128
                self.match(ZCodeParser.RS)
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==29:
                    self.state = 129
                    self.match(ZCodeParser.ASSIGN)
                    self.state = 130
                    self.expr()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraydecllistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMLIT(self):
            return self.getToken(ZCodeParser.NUMLIT, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def arraydecllist(self):
            return self.getTypedRuleContext(ZCodeParser.ArraydecllistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arraydecllist




    def arraydecllist(self):

        localctx = ZCodeParser.ArraydecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_arraydecllist)
        try:
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.match(ZCodeParser.NUMLIT)
                self.state = 136
                self.match(ZCodeParser.COMMA)
                self.state = 137
                self.arraydecllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.match(ZCodeParser.NUMLIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_typ




    def typ(self):

        localctx = ZCodeParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Implicit_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_implicit_var




    def implicit_var(self):

        localctx = ZCodeParser.Implicit_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_implicit_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(ZCodeParser.VAR)
            self.state = 144
            self.match(ZCodeParser.ID)
            self.state = 145
            self.match(ZCodeParser.ASSIGN)
            self.state = 146
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Implicit_dynamicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_implicit_dynamic




    def implicit_dynamic(self):

        localctx = ZCodeParser.Implicit_dynamicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_implicit_dynamic)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(ZCodeParser.DYNAMIC)
            self.state = 149
            self.match(ZCodeParser.ID)
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 150
                self.match(ZCodeParser.ASSIGN)
                self.state = 151
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def paramlist(self):
            return self.getTypedRuleContext(ZCodeParser.ParamlistContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def returnstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ReturnstmtContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(ZCodeParser.BlockstmtContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_funcdecl




    def funcdecl(self):

        localctx = ZCodeParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(ZCodeParser.FUNC)
            self.state = 155
            self.match(ZCodeParser.ID)
            self.state = 156
            self.match(ZCodeParser.LP)
            self.state = 157
            self.paramlist()
            self.state = 158
            self.match(ZCodeParser.RP)
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==45:
                    self.state = 159
                    self.ignore()


                self.state = 162
                self.returnstmt()
                pass

            elif la_ == 2:
                self.state = 164
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==45:
                    self.state = 163
                    self.ignore()


                self.state = 166
                self.blockstmt()
                pass

            elif la_ == 3:
                self.state = 167
                self.ignore()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramprime(self):
            return self.getTypedRuleContext(ZCodeParser.ParamprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramlist




    def paramlist(self):

        localctx = ZCodeParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_paramlist)
        try:
            self.state = 172
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.paramprime()
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(ZCodeParser.ParamContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def paramprime(self):
            return self.getTypedRuleContext(ZCodeParser.ParamprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramprime




    def paramprime(self):

        localctx = ZCodeParser.ParamprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_paramprime)
        try:
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.param()
                self.state = 175
                self.match(ZCodeParser.COMMA)
                self.state = 176
                self.paramprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(ZCodeParser.TypContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LS(self):
            return self.getToken(ZCodeParser.LS, 0)

        def arraydecllist(self):
            return self.getTypedRuleContext(ZCodeParser.ArraydecllistContext,0)


        def RS(self):
            return self.getToken(ZCodeParser.RS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_param




    def param(self):

        localctx = ZCodeParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.typ()
            self.state = 188
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 182
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.state = 183
                self.match(ZCodeParser.ID)
                self.state = 184
                self.match(ZCodeParser.LS)
                self.state = 185
                self.arraydecllist()
                self.state = 186
                self.match(ZCodeParser.RS)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdxOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(ZCodeParser.LS, 0)

        def exprlist(self):
            return self.getTypedRuleContext(ZCodeParser.ExprlistContext,0)


        def RS(self):
            return self.getToken(ZCodeParser.RS, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def callexpr(self):
            return self.getTypedRuleContext(ZCodeParser.CallexprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_idxOp




    def idxOp(self):

        localctx = ZCodeParser.IdxOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_idxOp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 190
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.state = 191
                self.callexpr()
                pass


            self.state = 194
            self.match(ZCodeParser.LS)
            self.state = 195
            self.exprlist()
            self.state = 196
            self.match(ZCodeParser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def exprlist(self):
            return self.getTypedRuleContext(ZCodeParser.ExprlistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exprlist




    def exprlist(self):

        localctx = ZCodeParser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_exprlist)
        try:
            self.state = 203
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.expr()
                self.state = 199
                self.match(ZCodeParser.COMMA)
                self.state = 200
                self.exprlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr1Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr1Context,i)


        def CONCAT(self):
            return self.getToken(ZCodeParser.CONCAT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr




    def expr(self):

        localctx = ZCodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expr)
        try:
            self.state = 210
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 205
                self.expr1()
                self.state = 206
                self.match(ZCodeParser.CONCAT)
                self.state = 207
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr2Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr2Context,i)


        def EQ(self):
            return self.getToken(ZCodeParser.EQ, 0)

        def LEQ(self):
            return self.getToken(ZCodeParser.LEQ, 0)

        def NE(self):
            return self.getToken(ZCodeParser.NE, 0)

        def LT(self):
            return self.getToken(ZCodeParser.LT, 0)

        def GT(self):
            return self.getToken(ZCodeParser.GT, 0)

        def LTE(self):
            return self.getToken(ZCodeParser.LTE, 0)

        def GTE(self):
            return self.getToken(ZCodeParser.GTE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr1




    def expr1(self):

        localctx = ZCodeParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 217
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.expr2(0)
                self.state = 213
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 102273908736) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 214
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 216
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(ZCodeParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(ZCodeParser.Expr2Context,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr2



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 227
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 222
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 223
                    _la = self._input.LA(1)
                    if not(_la==21 or _la==22):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 224
                    self.expr3(0) 
                self.state = 229
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(ZCodeParser.Expr3Context,0)


        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr3



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 238
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 233
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 234
                    _la = self._input.LA(1)
                    if not(_la==23 or _la==24):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 235
                    self.expr4(0) 
                self.state = 240
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def MUL(self):
            return self.getToken(ZCodeParser.MUL, 0)

        def DIV(self):
            return self.getToken(ZCodeParser.DIV, 0)

        def MOD(self):
            return self.getToken(ZCodeParser.MOD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr4



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 249
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 244
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 245
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 234881024) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 246
                    self.expr5() 
                self.state = 251
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr5




    def expr5(self):

        localctx = ZCodeParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expr5)
        try:
            self.state = 255
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                self.match(ZCodeParser.NOT)
                self.state = 253
                self.expr5()
                pass
            elif token in [1, 2, 23, 24, 37, 39, 42, 43, 44]:
                self.enterOuterAlt(localctx, 2)
                self.state = 254
                self.expr6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def expr7(self):
            return self.getTypedRuleContext(ZCodeParser.Expr7Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr6




    def expr6(self):

        localctx = ZCodeParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expr6)
        self._la = 0 # Token type
        try:
            self.state = 260
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23, 24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 257
                _la = self._input.LA(1)
                if not(_la==23 or _la==24):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 258
                self.expr6()
                pass
            elif token in [1, 2, 37, 39, 42, 43, 44]:
                self.enterOuterAlt(localctx, 2)
                self.state = 259
                self.expr7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idxOp(self):
            return self.getTypedRuleContext(ZCodeParser.IdxOpContext,0)


        def expr8(self):
            return self.getTypedRuleContext(ZCodeParser.Expr8Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr7




    def expr7(self):

        localctx = ZCodeParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_expr7)
        try:
            self.state = 264
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 262
                self.idxOp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 263
                self.expr8()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralContext,0)


        def subexpr(self):
            return self.getTypedRuleContext(ZCodeParser.SubexprContext,0)


        def callexpr(self):
            return self.getTypedRuleContext(ZCodeParser.CallexprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr8




    def expr8(self):

        localctx = ZCodeParser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expr8)
        try:
            self.state = 270
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 267
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 268
                self.subexpr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 269
                self.callexpr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_subexpr




    def subexpr(self):

        localctx = ZCodeParser.SubexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_subexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(ZCodeParser.LP)
            self.state = 273
            self.expr()
            self.state = 274
            self.match(ZCodeParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def exprlist(self):
            return self.getTypedRuleContext(ZCodeParser.ExprlistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_callexpr




    def callexpr(self):

        localctx = ZCodeParser.CallexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_callexpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(ZCodeParser.ID)
            self.state = 277
            self.match(ZCodeParser.LP)
            self.state = 279
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 31473546559494) != 0):
                self.state = 278
                self.exprlist()


            self.state = 281
            self.match(ZCodeParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def stmtlist(self):
            return self.getTypedRuleContext(ZCodeParser.StmtlistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmtlist




    def stmtlist(self):

        localctx = ZCodeParser.StmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_stmtlist)
        try:
            self.state = 287
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5, 6, 7, 8, 10, 13, 14, 15, 18, 42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 283
                self.stmt()
                self.state = 284
                self.stmtlist()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declstmt(self):
            return self.getTypedRuleContext(ZCodeParser.DeclstmtContext,0)


        def assignstmt(self):
            return self.getTypedRuleContext(ZCodeParser.AssignstmtContext,0)


        def ifstmt(self):
            return self.getTypedRuleContext(ZCodeParser.IfstmtContext,0)


        def forstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ForstmtContext,0)


        def breakstmt(self):
            return self.getTypedRuleContext(ZCodeParser.BreakstmtContext,0)


        def continuestmt(self):
            return self.getTypedRuleContext(ZCodeParser.ContinuestmtContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ReturnstmtContext,0)


        def callstmt(self):
            return self.getTypedRuleContext(ZCodeParser.CallstmtContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(ZCodeParser.BlockstmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt




    def stmt(self):

        localctx = ZCodeParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_stmt)
        try:
            self.state = 298
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 289
                self.declstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 290
                self.assignstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 291
                self.ifstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 292
                self.forstmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 293
                self.breakstmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 294
                self.continuestmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 295
                self.returnstmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 296
                self.callstmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 297
                self.blockstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(ZCodeParser.VardeclContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declstmt




    def declstmt(self):

        localctx = ZCodeParser.DeclstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_declstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.vardecl()
            self.state = 301
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def idxOp(self):
            return self.getTypedRuleContext(ZCodeParser.IdxOpContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_lhs




    def lhs(self):

        localctx = ZCodeParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_lhs)
        try:
            self.state = 305
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 303
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 304
                self.idxOp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(ZCodeParser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assignstmt




    def assignstmt(self):

        localctx = ZCodeParser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.lhs()
            self.state = 308
            self.match(ZCodeParser.ASSIGN)
            self.state = 309
            self.expr()
            self.state = 310
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def elifstmtlist(self):
            return self.getTypedRuleContext(ZCodeParser.ElifstmtlistContext,0)


        def elsestmt(self):
            return self.getTypedRuleContext(ZCodeParser.ElsestmtContext,0)


        def ignore(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.IgnoreContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.IgnoreContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_ifstmt




    def ifstmt(self):

        localctx = ZCodeParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_ifstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.match(ZCodeParser.IF)
            self.state = 313
            self.match(ZCodeParser.LP)
            self.state = 314
            self.expr()
            self.state = 315
            self.match(ZCodeParser.RP)
            self.state = 317
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==45:
                self.state = 316
                self.ignore()


            self.state = 319
            self.stmt()
            self.state = 321
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 320
                self.ignore()


            self.state = 323
            self.elifstmtlist()
            self.state = 326
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 324
                self.elsestmt()
                pass

            elif la_ == 2:
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifstmtlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elifstmtprime(self):
            return self.getTypedRuleContext(ZCodeParser.ElifstmtprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elifstmtlist




    def elifstmtlist(self):

        localctx = ZCodeParser.ElifstmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_elifstmtlist)
        try:
            self.state = 330
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 328
                self.elifstmtprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifstmtprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elifstmt(self):
            return self.getTypedRuleContext(ZCodeParser.ElifstmtContext,0)


        def elifstmtprime(self):
            return self.getTypedRuleContext(ZCodeParser.ElifstmtprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elifstmtprime




    def elifstmtprime(self):

        localctx = ZCodeParser.ElifstmtprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_elifstmtprime)
        try:
            self.state = 336
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                self.elifstmt()
                self.state = 333
                self.elifstmtprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 335
                self.elifstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def ignore(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.IgnoreContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.IgnoreContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elifstmt




    def elifstmt(self):

        localctx = ZCodeParser.ElifstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_elifstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.match(ZCodeParser.ELIF)
            self.state = 339
            self.match(ZCodeParser.LP)
            self.state = 340
            self.expr()
            self.state = 341
            self.match(ZCodeParser.RP)
            self.state = 343
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==45:
                self.state = 342
                self.ignore()


            self.state = 345
            self.stmt()
            self.state = 347
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 346
                self.ignore()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElsestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def ignore(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.IgnoreContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.IgnoreContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elsestmt




    def elsestmt(self):

        localctx = ZCodeParser.ElsestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_elsestmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.match(ZCodeParser.ELSE)
            self.state = 351
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==45:
                self.state = 350
                self.ignore()


            self.state = 353
            self.stmt()
            self.state = 355
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 354
                self.ignore()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_forstmt




    def forstmt(self):

        localctx = ZCodeParser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_forstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(ZCodeParser.FOR)
            self.state = 358
            self.match(ZCodeParser.ID)
            self.state = 359
            self.match(ZCodeParser.UNTIL)
            self.state = 360
            self.expr()
            self.state = 361
            self.match(ZCodeParser.BY)
            self.state = 362
            self.expr()
            self.state = 364
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==45:
                self.state = 363
                self.ignore()


            self.state = 366
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_breakstmt




    def breakstmt(self):

        localctx = ZCodeParser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            self.match(ZCodeParser.BREAK)
            self.state = 369
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_continuestmt




    def continuestmt(self):

        localctx = ZCodeParser.ContinuestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.match(ZCodeParser.CONTINUE)
            self.state = 372
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_returnstmt




    def returnstmt(self):

        localctx = ZCodeParser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_returnstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.match(ZCodeParser.RETURN)
            self.state = 376
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 31473546559494) != 0):
                self.state = 375
                self.expr()


            self.state = 378
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def exprlist(self):
            return self.getTypedRuleContext(ZCodeParser.ExprlistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_callstmt




    def callstmt(self):

        localctx = ZCodeParser.CallstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_callstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self.match(ZCodeParser.ID)
            self.state = 381
            self.match(ZCodeParser.LP)
            self.state = 384
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 20, 23, 24, 37, 39, 42, 43, 44]:
                self.state = 382
                self.exprlist()
                pass
            elif token in [38]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 386
            self.match(ZCodeParser.RP)
            self.state = 387
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def ignore(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.IgnoreContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.IgnoreContext,i)


        def stmtlist(self):
            return self.getTypedRuleContext(ZCodeParser.StmtlistContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_blockstmt




    def blockstmt(self):

        localctx = ZCodeParser.BlockstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_blockstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self.match(ZCodeParser.BEGIN)
            self.state = 390
            self.ignore()
            self.state = 391
            self.stmtlist()
            self.state = 392
            self.match(ZCodeParser.END)
            self.state = 393
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IgnoreContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_ignore




    def ignore(self):

        localctx = ZCodeParser.IgnoreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_ignore)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 395
                    self.match(ZCodeParser.NEWLINE)

                else:
                    raise NoViableAltException(self)
                self.state = 398 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMLIT(self):
            return self.getToken(ZCodeParser.NUMLIT, 0)

        def TRUE(self):
            return self.getToken(ZCodeParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(ZCodeParser.FALSE, 0)

        def STRINGLIT(self):
            return self.getToken(ZCodeParser.STRINGLIT, 0)

        def array_literal(self):
            return self.getTypedRuleContext(ZCodeParser.Array_literalContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_literal




    def literal(self):

        localctx = ZCodeParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_literal)
        try:
            self.state = 405
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [43]:
                self.enterOuterAlt(localctx, 1)
                self.state = 400
                self.match(ZCodeParser.NUMLIT)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 401
                self.match(ZCodeParser.TRUE)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 402
                self.match(ZCodeParser.FALSE)
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 4)
                self.state = 403
                self.match(ZCodeParser.STRINGLIT)
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 5)
                self.state = 404
                self.array_literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(ZCodeParser.LS, 0)

        def RS(self):
            return self.getToken(ZCodeParser.RS, 0)

        def exprlist(self):
            return self.getTypedRuleContext(ZCodeParser.ExprlistContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_literal




    def array_literal(self):

        localctx = ZCodeParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.match(ZCodeParser.LS)
            self.state = 410
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 20, 23, 24, 37, 39, 42, 43, 44]:
                self.state = 408
                self.exprlist()
                pass
            elif token in [40]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 412
            self.match(ZCodeParser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[17] = self.expr2_sempred
        self._predicates[18] = self.expr3_sempred
        self._predicates[19] = self.expr4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




