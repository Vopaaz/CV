import re


def preprocess(s):
    s = s.replace("LaTeX", r"{\LaTeX}").replace("%", r"\%").replace("&", r"\&")

    s = re.compile(r"\$HREF\{(.*?)\}\{(.*?)\}").sub(
        lambda m_obj: "\\href{{{}}}{{{}}}".format(m_obj.group(2), m_obj.group(1)), s
    )

    s = re.compile(r"\$TEXTIT\{(.*?)\}").sub(lambda m_obj: "\\textit{{{}}}".format(m_obj.group(1)), s)
    return s
