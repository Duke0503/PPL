# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\64")
        buf.write("\u01a1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\3")
        buf.write("\2\3\2\3\2\7\2`\n\2\f\2\16\2c\13\2\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\5\3l\n\3\3\4\3\4\3\4\3\4\5\4r\n\4\3\5\3\5\3\5")
        buf.write("\5\5w\n\5\3\6\3\6\3\6\3\6\5\6}\n\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\5\6\u0086\n\6\5\6\u0088\n\6\3\7\3\7\3\7\3\7\5")
        buf.write("\7\u008e\n\7\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\n\5\n\u009b\n\n\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00a3")
        buf.write("\n\13\3\13\3\13\5\13\u00a7\n\13\3\13\3\13\5\13\u00ab\n")
        buf.write("\13\3\f\3\f\5\f\u00af\n\f\3\r\3\r\3\r\3\r\3\r\5\r\u00b6")
        buf.write("\n\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00bf\n\16")
        buf.write("\3\17\3\17\5\17\u00c3\n\17\3\17\3\17\3\17\3\17\3\20\3")
        buf.write("\20\3\20\3\20\3\20\5\20\u00ce\n\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\5\21\u00d5\n\21\3\22\3\22\3\22\3\22\3\22\5\22\u00dc")
        buf.write("\n\22\3\23\3\23\3\23\3\23\3\23\3\23\7\23\u00e4\n\23\f")
        buf.write("\23\16\23\u00e7\13\23\3\24\3\24\3\24\3\24\3\24\3\24\7")
        buf.write("\24\u00ef\n\24\f\24\16\24\u00f2\13\24\3\25\3\25\3\25\3")
        buf.write("\25\3\25\3\25\7\25\u00fa\n\25\f\25\16\25\u00fd\13\25\3")
        buf.write("\26\3\26\3\26\5\26\u0102\n\26\3\27\3\27\3\27\5\27\u0107")
        buf.write("\n\27\3\30\3\30\5\30\u010b\n\30\3\31\3\31\3\31\3\31\5")
        buf.write("\31\u0111\n\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33\5\33")
        buf.write("\u011a\n\33\3\33\3\33\3\34\3\34\3\34\3\34\5\34\u0122\n")
        buf.write("\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35")
        buf.write("\u012d\n\35\3\36\3\36\3\36\3\37\3\37\5\37\u0134\n\37\3")
        buf.write(" \3 \3 \3 \3 \3!\3!\3!\3!\3!\5!\u0140\n!\3!\3!\5!\u0144")
        buf.write("\n!\3!\3!\3!\5!\u0149\n!\3\"\3\"\5\"\u014d\n\"\3#\3#\3")
        buf.write("#\3#\5#\u0153\n#\3$\3$\3$\3$\3$\5$\u015a\n$\3$\3$\5$\u015e")
        buf.write("\n$\3%\3%\5%\u0162\n%\3%\3%\5%\u0166\n%\3&\3&\3&\3&\3")
        buf.write("&\3&\3&\5&\u016f\n&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\5")
        buf.write(")\u017b\n)\3)\3)\3*\3*\3*\3*\5*\u0183\n*\3*\3*\3*\3+\3")
        buf.write("+\3+\3+\3+\3+\3,\6,\u018f\n,\r,\16,\u0190\3-\3-\3-\3-")
        buf.write("\3-\5-\u0198\n-\3.\3.\3.\5.\u019d\n.\3.\3.\3.\2\5$&(/")
        buf.write("\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\668:<>@BDFHJLNPRTVXZ\2\7\3\2\5\7\5\2\36\36 $&&\3\2")
        buf.write("\27\30\3\2\31\32\3\2\33\35\2\u01af\2a\3\2\2\2\4k\3\2\2")
        buf.write("\2\6q\3\2\2\2\bv\3\2\2\2\n\u0087\3\2\2\2\f\u008d\3\2\2")
        buf.write("\2\16\u008f\3\2\2\2\20\u0091\3\2\2\2\22\u0096\3\2\2\2")
        buf.write("\24\u009c\3\2\2\2\26\u00ae\3\2\2\2\30\u00b5\3\2\2\2\32")
        buf.write("\u00b7\3\2\2\2\34\u00c2\3\2\2\2\36\u00cd\3\2\2\2 \u00d4")
        buf.write("\3\2\2\2\"\u00db\3\2\2\2$\u00dd\3\2\2\2&\u00e8\3\2\2\2")
        buf.write("(\u00f3\3\2\2\2*\u0101\3\2\2\2,\u0106\3\2\2\2.\u010a\3")
        buf.write("\2\2\2\60\u0110\3\2\2\2\62\u0112\3\2\2\2\64\u0116\3\2")
        buf.write("\2\2\66\u0121\3\2\2\28\u012c\3\2\2\2:\u012e\3\2\2\2<\u0133")
        buf.write("\3\2\2\2>\u0135\3\2\2\2@\u013a\3\2\2\2B\u014c\3\2\2\2")
        buf.write("D\u0152\3\2\2\2F\u0154\3\2\2\2H\u015f\3\2\2\2J\u0167\3")
        buf.write("\2\2\2L\u0172\3\2\2\2N\u0175\3\2\2\2P\u0178\3\2\2\2R\u017e")
        buf.write("\3\2\2\2T\u0187\3\2\2\2V\u018e\3\2\2\2X\u0197\3\2\2\2")
        buf.write("Z\u0199\3\2\2\2\\]\7\60\2\2]`\7/\2\2^`\7/\2\2_\\\3\2\2")
        buf.write("\2_^\3\2\2\2`c\3\2\2\2a_\3\2\2\2ab\3\2\2\2bd\3\2\2\2c")
        buf.write("a\3\2\2\2de\5\4\3\2ef\7\2\2\3f\3\3\2\2\2gh\5\6\4\2hi\5")
        buf.write("\4\3\2il\3\2\2\2jl\5\6\4\2kg\3\2\2\2kj\3\2\2\2l\5\3\2")
        buf.write("\2\2mn\5\b\5\2no\5V,\2or\3\2\2\2pr\5\24\13\2qm\3\2\2\2")
        buf.write("qp\3\2\2\2r\7\3\2\2\2sw\5\n\6\2tw\5\20\t\2uw\5\22\n\2")
        buf.write("vs\3\2\2\2vt\3\2\2\2vu\3\2\2\2w\t\3\2\2\2xy\5\16\b\2y")
        buf.write("|\7,\2\2z{\7\37\2\2{}\5 \21\2|z\3\2\2\2|}\3\2\2\2}\u0088")
        buf.write("\3\2\2\2~\177\5\16\b\2\177\u0080\7,\2\2\u0080\u0081\7")
        buf.write(")\2\2\u0081\u0082\5\f\7\2\u0082\u0085\7*\2\2\u0083\u0084")
        buf.write("\7\37\2\2\u0084\u0086\5 \21\2\u0085\u0083\3\2\2\2\u0085")
        buf.write("\u0086\3\2\2\2\u0086\u0088\3\2\2\2\u0087x\3\2\2\2\u0087")
        buf.write("~\3\2\2\2\u0088\13\3\2\2\2\u0089\u008a\7-\2\2\u008a\u008b")
        buf.write("\7+\2\2\u008b\u008e\5\f\7\2\u008c\u008e\7-\2\2\u008d\u0089")
        buf.write("\3\2\2\2\u008d\u008c\3\2\2\2\u008e\r\3\2\2\2\u008f\u0090")
        buf.write("\t\2\2\2\u0090\17\3\2\2\2\u0091\u0092\7\t\2\2\u0092\u0093")
        buf.write("\7,\2\2\u0093\u0094\7\37\2\2\u0094\u0095\5 \21\2\u0095")
        buf.write("\21\3\2\2\2\u0096\u0097\7\n\2\2\u0097\u009a\7,\2\2\u0098")
        buf.write("\u0099\7\37\2\2\u0099\u009b\5 \21\2\u009a\u0098\3\2\2")
        buf.write("\2\u009a\u009b\3\2\2\2\u009b\23\3\2\2\2\u009c\u009d\7")
        buf.write("\13\2\2\u009d\u009e\7,\2\2\u009e\u009f\7\'\2\2\u009f\u00a0")
        buf.write("\5\26\f\2\u00a0\u00aa\7(\2\2\u00a1\u00a3\5V,\2\u00a2\u00a1")
        buf.write("\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4")
        buf.write("\u00ab\5P)\2\u00a5\u00a7\5V,\2\u00a6\u00a5\3\2\2\2\u00a6")
        buf.write("\u00a7\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\u00ab\5T+\2\u00a9")
        buf.write("\u00ab\5V,\2\u00aa\u00a2\3\2\2\2\u00aa\u00a6\3\2\2\2\u00aa")
        buf.write("\u00a9\3\2\2\2\u00ab\25\3\2\2\2\u00ac\u00af\5\30\r\2\u00ad")
        buf.write("\u00af\3\2\2\2\u00ae\u00ac\3\2\2\2\u00ae\u00ad\3\2\2\2")
        buf.write("\u00af\27\3\2\2\2\u00b0\u00b1\5\32\16\2\u00b1\u00b2\7")
        buf.write("+\2\2\u00b2\u00b3\5\30\r\2\u00b3\u00b6\3\2\2\2\u00b4\u00b6")
        buf.write("\5\32\16\2\u00b5\u00b0\3\2\2\2\u00b5\u00b4\3\2\2\2\u00b6")
        buf.write("\31\3\2\2\2\u00b7\u00be\5\16\b\2\u00b8\u00bf\7,\2\2\u00b9")
        buf.write("\u00ba\7,\2\2\u00ba\u00bb\7)\2\2\u00bb\u00bc\5\f\7\2\u00bc")
        buf.write("\u00bd\7*\2\2\u00bd\u00bf\3\2\2\2\u00be\u00b8\3\2\2\2")
        buf.write("\u00be\u00b9\3\2\2\2\u00bf\33\3\2\2\2\u00c0\u00c3\7,\2")
        buf.write("\2\u00c1\u00c3\5\64\33\2\u00c2\u00c0\3\2\2\2\u00c2\u00c1")
        buf.write("\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\u00c5\7)\2\2\u00c5")
        buf.write("\u00c6\5\36\20\2\u00c6\u00c7\7*\2\2\u00c7\35\3\2\2\2\u00c8")
        buf.write("\u00c9\5 \21\2\u00c9\u00ca\7+\2\2\u00ca\u00cb\5\36\20")
        buf.write("\2\u00cb\u00ce\3\2\2\2\u00cc\u00ce\5 \21\2\u00cd\u00c8")
        buf.write("\3\2\2\2\u00cd\u00cc\3\2\2\2\u00ce\37\3\2\2\2\u00cf\u00d0")
        buf.write("\5\"\22\2\u00d0\u00d1\7%\2\2\u00d1\u00d2\5\"\22\2\u00d2")
        buf.write("\u00d5\3\2\2\2\u00d3\u00d5\5\"\22\2\u00d4\u00cf\3\2\2")
        buf.write("\2\u00d4\u00d3\3\2\2\2\u00d5!\3\2\2\2\u00d6\u00d7\5$\23")
        buf.write("\2\u00d7\u00d8\t\3\2\2\u00d8\u00d9\5$\23\2\u00d9\u00dc")
        buf.write("\3\2\2\2\u00da\u00dc\5$\23\2\u00db\u00d6\3\2\2\2\u00db")
        buf.write("\u00da\3\2\2\2\u00dc#\3\2\2\2\u00dd\u00de\b\23\1\2\u00de")
        buf.write("\u00df\5&\24\2\u00df\u00e5\3\2\2\2\u00e0\u00e1\f\4\2\2")
        buf.write("\u00e1\u00e2\t\4\2\2\u00e2\u00e4\5&\24\2\u00e3\u00e0\3")
        buf.write("\2\2\2\u00e4\u00e7\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e5\u00e6")
        buf.write("\3\2\2\2\u00e6%\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e8\u00e9")
        buf.write("\b\24\1\2\u00e9\u00ea\5(\25\2\u00ea\u00f0\3\2\2\2\u00eb")
        buf.write("\u00ec\f\4\2\2\u00ec\u00ed\t\5\2\2\u00ed\u00ef\5(\25\2")
        buf.write("\u00ee\u00eb\3\2\2\2\u00ef\u00f2\3\2\2\2\u00f0\u00ee\3")
        buf.write("\2\2\2\u00f0\u00f1\3\2\2\2\u00f1\'\3\2\2\2\u00f2\u00f0")
        buf.write("\3\2\2\2\u00f3\u00f4\b\25\1\2\u00f4\u00f5\5*\26\2\u00f5")
        buf.write("\u00fb\3\2\2\2\u00f6\u00f7\f\4\2\2\u00f7\u00f8\t\6\2\2")
        buf.write("\u00f8\u00fa\5*\26\2\u00f9\u00f6\3\2\2\2\u00fa\u00fd\3")
        buf.write("\2\2\2\u00fb\u00f9\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc)")
        buf.write("\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fe\u00ff\7\26\2\2\u00ff")
        buf.write("\u0102\5*\26\2\u0100\u0102\5,\27\2\u0101\u00fe\3\2\2\2")
        buf.write("\u0101\u0100\3\2\2\2\u0102+\3\2\2\2\u0103\u0104\t\5\2")
        buf.write("\2\u0104\u0107\5,\27\2\u0105\u0107\5.\30\2\u0106\u0103")
        buf.write("\3\2\2\2\u0106\u0105\3\2\2\2\u0107-\3\2\2\2\u0108\u010b")
        buf.write("\5\34\17\2\u0109\u010b\5\60\31\2\u010a\u0108\3\2\2\2\u010a")
        buf.write("\u0109\3\2\2\2\u010b/\3\2\2\2\u010c\u0111\7,\2\2\u010d")
        buf.write("\u0111\5X-\2\u010e\u0111\5\62\32\2\u010f\u0111\5\64\33")
        buf.write("\2\u0110\u010c\3\2\2\2\u0110\u010d\3\2\2\2\u0110\u010e")
        buf.write("\3\2\2\2\u0110\u010f\3\2\2\2\u0111\61\3\2\2\2\u0112\u0113")
        buf.write("\7\'\2\2\u0113\u0114\5 \21\2\u0114\u0115\7(\2\2\u0115")
        buf.write("\63\3\2\2\2\u0116\u0117\7,\2\2\u0117\u0119\7\'\2\2\u0118")
        buf.write("\u011a\5\36\20\2\u0119\u0118\3\2\2\2\u0119\u011a\3\2\2")
        buf.write("\2\u011a\u011b\3\2\2\2\u011b\u011c\7(\2\2\u011c\65\3\2")
        buf.write("\2\2\u011d\u011e\58\35\2\u011e\u011f\5\66\34\2\u011f\u0122")
        buf.write("\3\2\2\2\u0120\u0122\3\2\2\2\u0121\u011d\3\2\2\2\u0121")
        buf.write("\u0120\3\2\2\2\u0122\67\3\2\2\2\u0123\u012d\5:\36\2\u0124")
        buf.write("\u012d\5> \2\u0125\u012d\5@!\2\u0126\u012d\5J&\2\u0127")
        buf.write("\u012d\5L\'\2\u0128\u012d\5N(\2\u0129\u012d\5P)\2\u012a")
        buf.write("\u012d\5R*\2\u012b\u012d\5T+\2\u012c\u0123\3\2\2\2\u012c")
        buf.write("\u0124\3\2\2\2\u012c\u0125\3\2\2\2\u012c\u0126\3\2\2\2")
        buf.write("\u012c\u0127\3\2\2\2\u012c\u0128\3\2\2\2\u012c\u0129\3")
        buf.write("\2\2\2\u012c\u012a\3\2\2\2\u012c\u012b\3\2\2\2\u012d9")
        buf.write("\3\2\2\2\u012e\u012f\5\b\5\2\u012f\u0130\5V,\2\u0130;")
        buf.write("\3\2\2\2\u0131\u0134\7,\2\2\u0132\u0134\5\34\17\2\u0133")
        buf.write("\u0131\3\2\2\2\u0133\u0132\3\2\2\2\u0134=\3\2\2\2\u0135")
        buf.write("\u0136\5<\37\2\u0136\u0137\7\37\2\2\u0137\u0138\5 \21")
        buf.write("\2\u0138\u0139\5V,\2\u0139?\3\2\2\2\u013a\u013b\7\21\2")
        buf.write("\2\u013b\u013c\7\'\2\2\u013c\u013d\5 \21\2\u013d\u013f")
        buf.write("\7(\2\2\u013e\u0140\5V,\2\u013f\u013e\3\2\2\2\u013f\u0140")
        buf.write("\3\2\2\2\u0140\u0141\3\2\2\2\u0141\u0143\58\35\2\u0142")
        buf.write("\u0144\5V,\2\u0143\u0142\3\2\2\2\u0143\u0144\3\2\2\2\u0144")
        buf.write("\u0145\3\2\2\2\u0145\u0148\5B\"\2\u0146\u0149\5H%\2\u0147")
        buf.write("\u0149\3\2\2\2\u0148\u0146\3\2\2\2\u0148\u0147\3\2\2\2")
        buf.write("\u0149A\3\2\2\2\u014a\u014d\5D#\2\u014b\u014d\3\2\2\2")
        buf.write("\u014c\u014a\3\2\2\2\u014c\u014b\3\2\2\2\u014dC\3\2\2")
        buf.write("\2\u014e\u014f\5F$\2\u014f\u0150\5D#\2\u0150\u0153\3\2")
        buf.write("\2\2\u0151\u0153\5F$\2\u0152\u014e\3\2\2\2\u0152\u0151")
        buf.write("\3\2\2\2\u0153E\3\2\2\2\u0154\u0155\7\23\2\2\u0155\u0156")
        buf.write("\7\'\2\2\u0156\u0157\5 \21\2\u0157\u0159\7(\2\2\u0158")
        buf.write("\u015a\5V,\2\u0159\u0158\3\2\2\2\u0159\u015a\3\2\2\2\u015a")
        buf.write("\u015b\3\2\2\2\u015b\u015d\58\35\2\u015c\u015e\5V,\2\u015d")
        buf.write("\u015c\3\2\2\2\u015d\u015e\3\2\2\2\u015eG\3\2\2\2\u015f")
        buf.write("\u0161\7\22\2\2\u0160\u0162\5V,\2\u0161\u0160\3\2\2\2")
        buf.write("\u0161\u0162\3\2\2\2\u0162\u0163\3\2\2\2\u0163\u0165\5")
        buf.write("8\35\2\u0164\u0166\5V,\2\u0165\u0164\3\2\2\2\u0165\u0166")
        buf.write("\3\2\2\2\u0166I\3\2\2\2\u0167\u0168\7\f\2\2\u0168\u0169")
        buf.write("\7,\2\2\u0169\u016a\7\r\2\2\u016a\u016b\5 \21\2\u016b")
        buf.write("\u016c\7\16\2\2\u016c\u016e\5 \21\2\u016d\u016f\5V,\2")
        buf.write("\u016e\u016d\3\2\2\2\u016e\u016f\3\2\2\2\u016f\u0170\3")
        buf.write("\2\2\2\u0170\u0171\58\35\2\u0171K\3\2\2\2\u0172\u0173")
        buf.write("\7\17\2\2\u0173\u0174\5V,\2\u0174M\3\2\2\2\u0175\u0176")
        buf.write("\7\20\2\2\u0176\u0177\5V,\2\u0177O\3\2\2\2\u0178\u017a")
        buf.write("\7\b\2\2\u0179\u017b\5 \21\2\u017a\u0179\3\2\2\2\u017a")
        buf.write("\u017b\3\2\2\2\u017b\u017c\3\2\2\2\u017c\u017d\5V,\2\u017d")
        buf.write("Q\3\2\2\2\u017e\u017f\7,\2\2\u017f\u0182\7\'\2\2\u0180")
        buf.write("\u0183\5\36\20\2\u0181\u0183\3\2\2\2\u0182\u0180\3\2\2")
        buf.write("\2\u0182\u0181\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0185")
        buf.write("\7(\2\2\u0185\u0186\5V,\2\u0186S\3\2\2\2\u0187\u0188\7")
        buf.write("\24\2\2\u0188\u0189\5V,\2\u0189\u018a\5\66\34\2\u018a")
        buf.write("\u018b\7\25\2\2\u018b\u018c\5V,\2\u018cU\3\2\2\2\u018d")
        buf.write("\u018f\7/\2\2\u018e\u018d\3\2\2\2\u018f\u0190\3\2\2\2")
        buf.write("\u0190\u018e\3\2\2\2\u0190\u0191\3\2\2\2\u0191W\3\2\2")
        buf.write("\2\u0192\u0198\7-\2\2\u0193\u0198\7\3\2\2\u0194\u0198")
        buf.write("\7\4\2\2\u0195\u0198\7.\2\2\u0196\u0198\5Z.\2\u0197\u0192")
        buf.write("\3\2\2\2\u0197\u0193\3\2\2\2\u0197\u0194\3\2\2\2\u0197")
        buf.write("\u0195\3\2\2\2\u0197\u0196\3\2\2\2\u0198Y\3\2\2\2\u0199")
        buf.write("\u019c\7)\2\2\u019a\u019d\5\36\20\2\u019b\u019d\3\2\2")
        buf.write("\2\u019c\u019a\3\2\2\2\u019c\u019b\3\2\2\2\u019d\u019e")
        buf.write("\3\2\2\2\u019e\u019f\7*\2\2\u019f[\3\2\2\2\60_akqv|\u0085")
        buf.write("\u0087\u008d\u009a\u00a2\u00a6\u00aa\u00ae\u00b5\u00be")
        buf.write("\u00c2\u00cd\u00d4\u00db\u00e5\u00f0\u00fb\u0101\u0106")
        buf.write("\u010a\u0110\u0119\u0121\u012c\u0133\u013f\u0143\u0148")
        buf.write("\u014c\u0152\u0159\u015d\u0161\u0165\u016e\u017a\u0182")
        buf.write("\u0190\u0197\u019c")
        return buf.getvalue()


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
                     "<INVALID>", "<INVALID>", "<INVALID>", "'\n'" ]

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
        self.checkVersion("4.9.2")
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE or _la==ZCodeParser.COMMENTS:
                self.state = 93
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.COMMENTS]:
                    self.state = 90
                    self.match(ZCodeParser.COMMENTS)
                    self.state = 91
                    self.match(ZCodeParser.NEWLINE)
                    pass
                elif token in [ZCodeParser.NEWLINE]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecllist" ):
                return visitor.visitDecllist(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 111
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.vardecl()
                self.state = 108
                self.ignore()
                pass
            elif token in [ZCodeParser.FUNC]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = ZCodeParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vardecl)
        try:
            self.state = 116
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.type_var()
                pass
            elif token in [ZCodeParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
                self.implicit_var()
                pass
            elif token in [ZCodeParser.DYNAMIC]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_var" ):
                return visitor.visitType_var(self)
            else:
                return visitor.visitChildren(self)




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
                if _la==ZCodeParser.ASSIGN:
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
                if _la==ZCodeParser.ASSIGN:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraydecllist" ):
                return visitor.visitArraydecllist(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = ZCodeParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicit_var" ):
                return visitor.visitImplicit_var(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicit_dynamic" ):
                return visitor.visitImplicit_dynamic(self)
            else:
                return visitor.visitChildren(self)




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
            if _la==ZCodeParser.ASSIGN:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




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
                if _la==ZCodeParser.NEWLINE:
                    self.state = 159
                    self.ignore()


                self.state = 162
                self.returnstmt()
                pass

            elif la_ == 2:
                self.state = 164
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = ZCodeParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_paramlist)
        try:
            self.state = 172
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.paramprime()
                pass
            elif token in [ZCodeParser.RP]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamprime" ):
                return visitor.visitParamprime(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdxOp" ):
                return visitor.visitIdxOp(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlist" ):
                return visitor.visitExprlist(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




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
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQ) | (1 << ZCodeParser.NE) | (1 << ZCodeParser.LT) | (1 << ZCodeParser.LTE) | (1 << ZCodeParser.GT) | (1 << ZCodeParser.GTE) | (1 << ZCodeParser.LEQ))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



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
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



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
                    if not(_la==ZCodeParser.ADD or _la==ZCodeParser.SUB):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



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
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = ZCodeParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expr5)
        try:
            self.state = 255
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                self.match(ZCodeParser.NOT)
                self.state = 253
                self.expr5()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.ADD, ZCodeParser.SUB, ZCodeParser.LP, ZCodeParser.LS, ZCodeParser.ID, ZCodeParser.NUMLIT, ZCodeParser.STRINGLIT]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = ZCodeParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expr6)
        self._la = 0 # Token type
        try:
            self.state = 260
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ADD, ZCodeParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 257
                _la = self._input.LA(1)
                if not(_la==ZCodeParser.ADD or _la==ZCodeParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 258
                self.expr6()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.LP, ZCodeParser.LS, ZCodeParser.ID, ZCodeParser.NUMLIT, ZCodeParser.STRINGLIT]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubexpr" ):
                return visitor.visitSubexpr(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallexpr" ):
                return visitor.visitCallexpr(self)
            else:
                return visitor.visitChildren(self)




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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.ADD) | (1 << ZCodeParser.SUB) | (1 << ZCodeParser.LP) | (1 << ZCodeParser.LS) | (1 << ZCodeParser.ID) | (1 << ZCodeParser.NUMLIT) | (1 << ZCodeParser.STRINGLIT))) != 0):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtlist" ):
                return visitor.visitStmtlist(self)
            else:
                return visitor.visitChildren(self)




    def stmtlist(self):

        localctx = ZCodeParser.StmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_stmtlist)
        try:
            self.state = 287
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 283
                self.stmt()
                self.state = 284
                self.stmtlist()
                pass
            elif token in [ZCodeParser.END]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclstmt" ):
                return visitor.visitDeclstmt(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignstmt" ):
                return visitor.visitAssignstmt(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




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
            if _la==ZCodeParser.NEWLINE:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifstmtlist" ):
                return visitor.visitElifstmtlist(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifstmtprime" ):
                return visitor.visitElifstmtprime(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifstmt" ):
                return visitor.visitElifstmt(self)
            else:
                return visitor.visitChildren(self)




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
            if _la==ZCodeParser.NEWLINE:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElsestmt" ):
                return visitor.visitElsestmt(self)
            else:
                return visitor.visitChildren(self)




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
            if _la==ZCodeParser.NEWLINE:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstmt" ):
                return visitor.visitForstmt(self)
            else:
                return visitor.visitChildren(self)




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
            if _la==ZCodeParser.NEWLINE:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakstmt" ):
                return visitor.visitBreakstmt(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinuestmt" ):
                return visitor.visitContinuestmt(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstmt" ):
                return visitor.visitReturnstmt(self)
            else:
                return visitor.visitChildren(self)




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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.TRUE) | (1 << ZCodeParser.FALSE) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.ADD) | (1 << ZCodeParser.SUB) | (1 << ZCodeParser.LP) | (1 << ZCodeParser.LS) | (1 << ZCodeParser.ID) | (1 << ZCodeParser.NUMLIT) | (1 << ZCodeParser.STRINGLIT))) != 0):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallstmt" ):
                return visitor.visitCallstmt(self)
            else:
                return visitor.visitChildren(self)




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
            if token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.NOT, ZCodeParser.ADD, ZCodeParser.SUB, ZCodeParser.LP, ZCodeParser.LS, ZCodeParser.ID, ZCodeParser.NUMLIT, ZCodeParser.STRINGLIT]:
                self.state = 382
                self.exprlist()
                pass
            elif token in [ZCodeParser.RP]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockstmt" ):
                return visitor.visitBlockstmt(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIgnore" ):
                return visitor.visitIgnore(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = ZCodeParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_literal)
        try:
            self.state = 405
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 400
                self.match(ZCodeParser.NUMLIT)
                pass
            elif token in [ZCodeParser.TRUE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 401
                self.match(ZCodeParser.TRUE)
                pass
            elif token in [ZCodeParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 402
                self.match(ZCodeParser.FALSE)
                pass
            elif token in [ZCodeParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 403
                self.match(ZCodeParser.STRINGLIT)
                pass
            elif token in [ZCodeParser.LS]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




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
            if token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.NOT, ZCodeParser.ADD, ZCodeParser.SUB, ZCodeParser.LP, ZCodeParser.LS, ZCodeParser.ID, ZCodeParser.NUMLIT, ZCodeParser.STRINGLIT]:
                self.state = 408
                self.exprlist()
                pass
            elif token in [ZCodeParser.RS]:
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
         




