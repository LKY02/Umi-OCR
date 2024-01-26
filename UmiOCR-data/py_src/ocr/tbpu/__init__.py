# tbpu : text block processing unit 文本块后处理

from .parser_none import ParserNone
from .parser_multi_para import MultiPara
from .ignore_area import IgnoreArea

# 排版解析
Parser = {
    "none": ParserNone,  # 不做处理
    "multi_para": MultiPara,  # 多栏-自然段
    "multi_line": MultiPara,  # 多栏-单行
    "single_para": MultiPara,  # 单栏-自然段
    "single_line": MultiPara,  # 单栏-单行
    "single_code": MultiPara,  # 单栏-代码段
}


# 获取排版解析器对象
def getParser(key):
    if key in Parser:
        return Parser[key]()
    else:
        return Parser["none"]()
