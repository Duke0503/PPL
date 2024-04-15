# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\64")
        buf.write("\u0190\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\31")
        buf.write("\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3#\3")
        buf.write("$\3$\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3")
        buf.write("+\3+\7+\u011d\n+\f+\16+\u0120\13+\3,\3,\3,\3,\3,\3,\3")
        buf.write(",\3,\3,\3,\3,\5,\u012d\n,\3-\3-\3.\6.\u0132\n.\r.\16.")
        buf.write("\u0133\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\5\62\u013e")
        buf.write("\n\62\3\63\3\63\5\63\u0142\n\63\3\63\3\63\3\64\3\64\7")
        buf.write("\64\u0148\n\64\f\64\16\64\u014b\13\64\3\64\3\64\3\64\3")
        buf.write("\65\3\65\3\65\3\65\3\65\5\65\u0155\n\65\3\66\3\66\3\66")
        buf.write("\5\66\u015a\n\66\3\67\3\67\38\38\38\38\78\u0162\n8\f8")
        buf.write("\168\u0165\138\38\78\u0168\n8\f8\168\u016b\138\38\38\3")
        buf.write("9\69\u0170\n9\r9\169\u0171\39\39\3:\3:\3:\3;\3;\7;\u017b")
        buf.write("\n;\f;\16;\u017e\13;\3;\3;\3;\5;\u0183\n;\3;\3;\3<\3<")
        buf.write("\7<\u0189\n<\f<\16<\u018c\13<\3<\3<\3<\3\u0163\2=\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W-Y\2[\2]\2_\2a\2c\2e\2g.i\2k\2m/o\60q\61s\62u\63")
        buf.write("w\64\3\2\r\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\4\2GGgg\4")
        buf.write("\2--//\6\2\f\f\16\17$$^^\t\2))^^ddhhppttvv\3\2\16\17\4")
        buf.write("\2\f\f\16\17\5\2\13\13\17\17\"\"\3\3\f\f\2\u0197\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2")
        buf.write("\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2")
        buf.write("\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3")
        buf.write("\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2")
        buf.write("\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3")
        buf.write("\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K")
        buf.write("\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2")
        buf.write("U\3\2\2\2\2W\3\2\2\2\2g\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2")
        buf.write("\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\3y\3\2\2")
        buf.write("\2\5~\3\2\2\2\7\u0084\3\2\2\2\t\u008b\3\2\2\2\13\u0090")
        buf.write("\3\2\2\2\r\u0097\3\2\2\2\17\u009e\3\2\2\2\21\u00a2\3\2")
        buf.write("\2\2\23\u00aa\3\2\2\2\25\u00af\3\2\2\2\27\u00b3\3\2\2")
        buf.write("\2\31\u00b9\3\2\2\2\33\u00bc\3\2\2\2\35\u00c2\3\2\2\2")
        buf.write("\37\u00cb\3\2\2\2!\u00ce\3\2\2\2#\u00d3\3\2\2\2%\u00d8")
        buf.write("\3\2\2\2\'\u00de\3\2\2\2)\u00e2\3\2\2\2+\u00e6\3\2\2\2")
        buf.write("-\u00ea\3\2\2\2/\u00ed\3\2\2\2\61\u00ef\3\2\2\2\63\u00f1")
        buf.write("\3\2\2\2\65\u00f3\3\2\2\2\67\u00f5\3\2\2\29\u00f7\3\2")
        buf.write("\2\2;\u00f9\3\2\2\2=\u00fc\3\2\2\2?\u00ff\3\2\2\2A\u0101")
        buf.write("\3\2\2\2C\u0104\3\2\2\2E\u0106\3\2\2\2G\u0109\3\2\2\2")
        buf.write("I\u010d\3\2\2\2K\u0110\3\2\2\2M\u0112\3\2\2\2O\u0114\3")
        buf.write("\2\2\2Q\u0116\3\2\2\2S\u0118\3\2\2\2U\u011a\3\2\2\2W\u012c")
        buf.write("\3\2\2\2Y\u012e\3\2\2\2[\u0131\3\2\2\2]\u0135\3\2\2\2")
        buf.write("_\u0137\3\2\2\2a\u0139\3\2\2\2c\u013b\3\2\2\2e\u013f\3")
        buf.write("\2\2\2g\u0145\3\2\2\2i\u0154\3\2\2\2k\u0159\3\2\2\2m\u015b")
        buf.write("\3\2\2\2o\u015d\3\2\2\2q\u016f\3\2\2\2s\u0175\3\2\2\2")
        buf.write("u\u0178\3\2\2\2w\u0186\3\2\2\2yz\7v\2\2z{\7t\2\2{|\7w")
        buf.write("\2\2|}\7g\2\2}\4\3\2\2\2~\177\7h\2\2\177\u0080\7c\2\2")
        buf.write("\u0080\u0081\7n\2\2\u0081\u0082\7u\2\2\u0082\u0083\7g")
        buf.write("\2\2\u0083\6\3\2\2\2\u0084\u0085\7p\2\2\u0085\u0086\7")
        buf.write("w\2\2\u0086\u0087\7o\2\2\u0087\u0088\7d\2\2\u0088\u0089")
        buf.write("\7g\2\2\u0089\u008a\7t\2\2\u008a\b\3\2\2\2\u008b\u008c")
        buf.write("\7d\2\2\u008c\u008d\7q\2\2\u008d\u008e\7q\2\2\u008e\u008f")
        buf.write("\7n\2\2\u008f\n\3\2\2\2\u0090\u0091\7u\2\2\u0091\u0092")
        buf.write("\7v\2\2\u0092\u0093\7t\2\2\u0093\u0094\7k\2\2\u0094\u0095")
        buf.write("\7p\2\2\u0095\u0096\7i\2\2\u0096\f\3\2\2\2\u0097\u0098")
        buf.write("\7t\2\2\u0098\u0099\7g\2\2\u0099\u009a\7v\2\2\u009a\u009b")
        buf.write("\7w\2\2\u009b\u009c\7t\2\2\u009c\u009d\7p\2\2\u009d\16")
        buf.write("\3\2\2\2\u009e\u009f\7x\2\2\u009f\u00a0\7c\2\2\u00a0\u00a1")
        buf.write("\7t\2\2\u00a1\20\3\2\2\2\u00a2\u00a3\7f\2\2\u00a3\u00a4")
        buf.write("\7{\2\2\u00a4\u00a5\7p\2\2\u00a5\u00a6\7c\2\2\u00a6\u00a7")
        buf.write("\7o\2\2\u00a7\u00a8\7k\2\2\u00a8\u00a9\7e\2\2\u00a9\22")
        buf.write("\3\2\2\2\u00aa\u00ab\7h\2\2\u00ab\u00ac\7w\2\2\u00ac\u00ad")
        buf.write("\7p\2\2\u00ad\u00ae\7e\2\2\u00ae\24\3\2\2\2\u00af\u00b0")
        buf.write("\7h\2\2\u00b0\u00b1\7q\2\2\u00b1\u00b2\7t\2\2\u00b2\26")
        buf.write("\3\2\2\2\u00b3\u00b4\7w\2\2\u00b4\u00b5\7p\2\2\u00b5\u00b6")
        buf.write("\7v\2\2\u00b6\u00b7\7k\2\2\u00b7\u00b8\7n\2\2\u00b8\30")
        buf.write("\3\2\2\2\u00b9\u00ba\7d\2\2\u00ba\u00bb\7{\2\2\u00bb\32")
        buf.write("\3\2\2\2\u00bc\u00bd\7d\2\2\u00bd\u00be\7t\2\2\u00be\u00bf")
        buf.write("\7g\2\2\u00bf\u00c0\7c\2\2\u00c0\u00c1\7m\2\2\u00c1\34")
        buf.write("\3\2\2\2\u00c2\u00c3\7e\2\2\u00c3\u00c4\7q\2\2\u00c4\u00c5")
        buf.write("\7p\2\2\u00c5\u00c6\7v\2\2\u00c6\u00c7\7k\2\2\u00c7\u00c8")
        buf.write("\7p\2\2\u00c8\u00c9\7w\2\2\u00c9\u00ca\7g\2\2\u00ca\36")
        buf.write("\3\2\2\2\u00cb\u00cc\7k\2\2\u00cc\u00cd\7h\2\2\u00cd ")
        buf.write("\3\2\2\2\u00ce\u00cf\7g\2\2\u00cf\u00d0\7n\2\2\u00d0\u00d1")
        buf.write("\7u\2\2\u00d1\u00d2\7g\2\2\u00d2\"\3\2\2\2\u00d3\u00d4")
        buf.write("\7g\2\2\u00d4\u00d5\7n\2\2\u00d5\u00d6\7k\2\2\u00d6\u00d7")
        buf.write("\7h\2\2\u00d7$\3\2\2\2\u00d8\u00d9\7d\2\2\u00d9\u00da")
        buf.write("\7g\2\2\u00da\u00db\7i\2\2\u00db\u00dc\7k\2\2\u00dc\u00dd")
        buf.write("\7p\2\2\u00dd&\3\2\2\2\u00de\u00df\7g\2\2\u00df\u00e0")
        buf.write("\7p\2\2\u00e0\u00e1\7f\2\2\u00e1(\3\2\2\2\u00e2\u00e3")
        buf.write("\7p\2\2\u00e3\u00e4\7q\2\2\u00e4\u00e5\7v\2\2\u00e5*\3")
        buf.write("\2\2\2\u00e6\u00e7\7c\2\2\u00e7\u00e8\7p\2\2\u00e8\u00e9")
        buf.write("\7f\2\2\u00e9,\3\2\2\2\u00ea\u00eb\7q\2\2\u00eb\u00ec")
        buf.write("\7t\2\2\u00ec.\3\2\2\2\u00ed\u00ee\7-\2\2\u00ee\60\3\2")
        buf.write("\2\2\u00ef\u00f0\7/\2\2\u00f0\62\3\2\2\2\u00f1\u00f2\7")
        buf.write(",\2\2\u00f2\64\3\2\2\2\u00f3\u00f4\7\61\2\2\u00f4\66\3")
        buf.write("\2\2\2\u00f5\u00f6\7\'\2\2\u00f68\3\2\2\2\u00f7\u00f8")
        buf.write("\7?\2\2\u00f8:\3\2\2\2\u00f9\u00fa\7>\2\2\u00fa\u00fb")
        buf.write("\7/\2\2\u00fb<\3\2\2\2\u00fc\u00fd\7#\2\2\u00fd\u00fe")
        buf.write("\7?\2\2\u00fe>\3\2\2\2\u00ff\u0100\7>\2\2\u0100@\3\2\2")
        buf.write("\2\u0101\u0102\7>\2\2\u0102\u0103\7?\2\2\u0103B\3\2\2")
        buf.write("\2\u0104\u0105\7@\2\2\u0105D\3\2\2\2\u0106\u0107\7@\2")
        buf.write("\2\u0107\u0108\7?\2\2\u0108F\3\2\2\2\u0109\u010a\7\60")
        buf.write("\2\2\u010a\u010b\7\60\2\2\u010b\u010c\7\60\2\2\u010cH")
        buf.write("\3\2\2\2\u010d\u010e\7?\2\2\u010e\u010f\7?\2\2\u010fJ")
        buf.write("\3\2\2\2\u0110\u0111\7*\2\2\u0111L\3\2\2\2\u0112\u0113")
        buf.write("\7+\2\2\u0113N\3\2\2\2\u0114\u0115\7]\2\2\u0115P\3\2\2")
        buf.write("\2\u0116\u0117\7_\2\2\u0117R\3\2\2\2\u0118\u0119\7.\2")
        buf.write("\2\u0119T\3\2\2\2\u011a\u011e\t\2\2\2\u011b\u011d\t\3")
        buf.write("\2\2\u011c\u011b\3\2\2\2\u011d\u0120\3\2\2\2\u011e\u011c")
        buf.write("\3\2\2\2\u011e\u011f\3\2\2\2\u011fV\3\2\2\2\u0120\u011e")
        buf.write("\3\2\2\2\u0121\u012d\5[.\2\u0122\u0123\5[.\2\u0123\u0124")
        buf.write("\5c\62\2\u0124\u0125\5e\63\2\u0125\u012d\3\2\2\2\u0126")
        buf.write("\u0127\5[.\2\u0127\u0128\5c\62\2\u0128\u012d\3\2\2\2\u0129")
        buf.write("\u012a\5[.\2\u012a\u012b\5e\63\2\u012b\u012d\3\2\2\2\u012c")
        buf.write("\u0121\3\2\2\2\u012c\u0122\3\2\2\2\u012c\u0126\3\2\2\2")
        buf.write("\u012c\u0129\3\2\2\2\u012dX\3\2\2\2\u012e\u012f\t\4\2")
        buf.write("\2\u012fZ\3\2\2\2\u0130\u0132\5Y-\2\u0131\u0130\3\2\2")
        buf.write("\2\u0132\u0133\3\2\2\2\u0133\u0131\3\2\2\2\u0133\u0134")
        buf.write("\3\2\2\2\u0134\\\3\2\2\2\u0135\u0136\t\5\2\2\u0136^\3")
        buf.write("\2\2\2\u0137\u0138\t\6\2\2\u0138`\3\2\2\2\u0139\u013a")
        buf.write("\7\60\2\2\u013ab\3\2\2\2\u013b\u013d\5a\61\2\u013c\u013e")
        buf.write("\5[.\2\u013d\u013c\3\2\2\2\u013d\u013e\3\2\2\2\u013ed")
        buf.write("\3\2\2\2\u013f\u0141\5]/\2\u0140\u0142\5_\60\2\u0141\u0140")
        buf.write("\3\2\2\2\u0141\u0142\3\2\2\2\u0142\u0143\3\2\2\2\u0143")
        buf.write("\u0144\5[.\2\u0144f\3\2\2\2\u0145\u0149\7$\2\2\u0146\u0148")
        buf.write("\5i\65\2\u0147\u0146\3\2\2\2\u0148\u014b\3\2\2\2\u0149")
        buf.write("\u0147\3\2\2\2\u0149\u014a\3\2\2\2\u014a\u014c\3\2\2\2")
        buf.write("\u014b\u0149\3\2\2\2\u014c\u014d\7$\2\2\u014d\u014e\b")
        buf.write("\64\2\2\u014eh\3\2\2\2\u014f\u0155\n\7\2\2\u0150\u0151")
        buf.write("\7^\2\2\u0151\u0155\t\b\2\2\u0152\u0153\7)\2\2\u0153\u0155")
        buf.write("\7$\2\2\u0154\u014f\3\2\2\2\u0154\u0150\3\2\2\2\u0154")
        buf.write("\u0152\3\2\2\2\u0155j\3\2\2\2\u0156\u015a\t\t\2\2\u0157")
        buf.write("\u0158\7^\2\2\u0158\u015a\n\b\2\2\u0159\u0156\3\2\2\2")
        buf.write("\u0159\u0157\3\2\2\2\u015al\3\2\2\2\u015b\u015c\7\f\2")
        buf.write("\2\u015cn\3\2\2\2\u015d\u015e\7%\2\2\u015e\u015f\7%\2")
        buf.write("\2\u015f\u0163\3\2\2\2\u0160\u0162\13\2\2\2\u0161\u0160")
        buf.write("\3\2\2\2\u0162\u0165\3\2\2\2\u0163\u0164\3\2\2\2\u0163")
        buf.write("\u0161\3\2\2\2\u0164\u0169\3\2\2\2\u0165\u0163\3\2\2\2")
        buf.write("\u0166\u0168\n\n\2\2\u0167\u0166\3\2\2\2\u0168\u016b\3")
        buf.write("\2\2\2\u0169\u0167\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u016c")
        buf.write("\3\2\2\2\u016b\u0169\3\2\2\2\u016c\u016d\b8\3\2\u016d")
        buf.write("p\3\2\2\2\u016e\u0170\t\13\2\2\u016f\u016e\3\2\2\2\u0170")
        buf.write("\u0171\3\2\2\2\u0171\u016f\3\2\2\2\u0171\u0172\3\2\2\2")
        buf.write("\u0172\u0173\3\2\2\2\u0173\u0174\b9\3\2\u0174r\3\2\2\2")
        buf.write("\u0175\u0176\13\2\2\2\u0176\u0177\b:\4\2\u0177t\3\2\2")
        buf.write("\2\u0178\u017c\7$\2\2\u0179\u017b\5i\65\2\u017a\u0179")
        buf.write("\3\2\2\2\u017b\u017e\3\2\2\2\u017c\u017a\3\2\2\2\u017c")
        buf.write("\u017d\3\2\2\2\u017d\u0182\3\2\2\2\u017e\u017c\3\2\2\2")
        buf.write("\u017f\u0180\7\17\2\2\u0180\u0183\7\f\2\2\u0181\u0183")
        buf.write("\t\f\2\2\u0182\u017f\3\2\2\2\u0182\u0181\3\2\2\2\u0183")
        buf.write("\u0184\3\2\2\2\u0184\u0185\b;\5\2\u0185v\3\2\2\2\u0186")
        buf.write("\u018a\7$\2\2\u0187\u0189\5i\65\2\u0188\u0187\3\2\2\2")
        buf.write("\u0189\u018c\3\2\2\2\u018a\u0188\3\2\2\2\u018a\u018b\3")
        buf.write("\2\2\2\u018b\u018d\3\2\2\2\u018c\u018a\3\2\2\2\u018d\u018e")
        buf.write("\5k\66\2\u018e\u018f\b<\6\2\u018fx\3\2\2\2\21\2\u011e")
        buf.write("\u012c\u0133\u013d\u0141\u0149\u0154\u0159\u0163\u0169")
        buf.write("\u0171\u017c\u0182\u018a\7\3\64\2\b\2\2\3:\3\3;\4\3<\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TRUE = 1
    FALSE = 2
    NUMBER = 3
    BOOL = 4
    STRING = 5
    RETURN = 6
    VAR = 7
    DYNAMIC = 8
    FUNC = 9
    FOR = 10
    UNTIL = 11
    BY = 12
    BREAK = 13
    CONTINUE = 14
    IF = 15
    ELSE = 16
    ELIF = 17
    BEGIN = 18
    END = 19
    NOT = 20
    AND = 21
    OR = 22
    ADD = 23
    SUB = 24
    MUL = 25
    DIV = 26
    MOD = 27
    EQ = 28
    ASSIGN = 29
    NE = 30
    LT = 31
    LTE = 32
    GT = 33
    GTE = 34
    CONCAT = 35
    LEQ = 36
    LP = 37
    RP = 38
    LS = 39
    RS = 40
    COMMA = 41
    ID = 42
    NUMLIT = 43
    STRINGLIT = 44
    NEWLINE = 45
    COMMENTS = 46
    WS = 47
    ERROR_CHAR = 48
    UNCLOSE_STRING = 49
    ILLEGAL_ESCAPE = 50

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'number'", "'bool'", "'string'", "'return'", 
            "'var'", "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
            "'break'", "'continue'", "'if'", "'else'", "'elif'", "'begin'", 
            "'end'", "'not'", "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'='", "'<-'", "'!='", "'<'", "'<='", "'>'", "'>='", 
            "'...'", "'=='", "'('", "')'", "'['", "']'", "','", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", "VAR", 
            "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
            "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "ADD", 
            "SUB", "MUL", "DIV", "MOD", "EQ", "ASSIGN", "NE", "LT", "LTE", 
            "GT", "GTE", "CONCAT", "LEQ", "LP", "RP", "LS", "RS", "COMMA", 
            "ID", "NUMLIT", "STRINGLIT", "NEWLINE", "COMMENTS", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", 
                  "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
                  "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", 
                  "AND", "OR", "ADD", "SUB", "MUL", "DIV", "MOD", "EQ", 
                  "ASSIGN", "NE", "LT", "LTE", "GT", "GTE", "CONCAT", "LEQ", 
                  "LP", "RP", "LS", "RS", "COMMA", "ID", "NUMLIT", "DIGIT", 
                  "DigitSequence", "Exponent", "SIGN", "DOT", "DecimalPart", 
                  "ExponentPart", "STRINGLIT", "CHAR", "ILLEGAL", "NEWLINE", 
                  "COMMENTS", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[50] = self.STRINGLIT_action 
            actions[56] = self.ERROR_CHAR_action 
            actions[57] = self.UNCLOSE_STRING_action 
            actions[58] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1];
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            		if self.text[-1] == '\n' and self.text[-2] == '\r':
            			raise UncloseString(self.text[1:-2])
            		elif self.text[-1] == '\n':
            			raise UncloseString(self.text[1:-1])
            		else:
            			raise UncloseString(self.text[1:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            		raise IllegalEscape(self.text[1:])
            	
     


