import json
import os
import datetime
from collections import OrderedDict

with open("experience.json", "r", encoding="utf-8") as f:
    _ = json.load(f)

EN_CLASS = "resumeEN"
ZH_CLASS = "resumeZH"

EN_BASE_LINE_STRETCH = 1.1
ZH_BASE_LINE_STRETCH = 1.12

EN_NAME = "YiFan Li"
ZH_NAME = "李逸凡"

EN_PHONE = "+86-18811019056"
ZH_PHONE = "18811019056"


def head(class_, baselinestretch, name, phone):
    return '''\\documentclass{{{}}}

\\usepackage{{geometry}}
\\geometry{{a4paper, top=1cm, bottom=1cm, left=1.2cm,right=1.2cm, nohead, nofoot}}

% --- Adjust the overall stretch here ---
\\renewcommand{{\\baselinestretch}}{{{}}}
% ---------------------------------------

\\input{{experience.tex}}

\\begin{{document}}

\\contact{{{}}}{{{}}}{{liyifan.steven616@gmail.com}}
'''.format(class_, baselinestretch, name, phone)


HEAD = {
    "en": head(EN_CLASS, EN_BASE_LINE_STRETCH, EN_NAME, EN_PHONE),
    "zh": head(ZH_CLASS, ZH_BASE_LINE_STRETCH, ZH_NAME, ZH_PHONE)
}

TAIL = r"\end{document}"


def get_content(lang, verbose):
    assert lang in ["zh", "en"]

    s = ""

    s += std_section("education", lang, verbose, sort_time=False)
    s += std_section("internship", lang, verbose)
    s += std_section("research", lang, verbose)
    s += std_section("others", lang, verbose)

    s += skills_section(lang)

    return s


def std_section(sec, lang, verbose, sort_time=True):
    s = ""
    experiences = _[sec]["experiences"]
    if sort_time:
        experiences = sorted(experiences, key=lambda x: datetime.datetime.strptime(
            x["time"].split("-")[0].strip(), r"%Y/%m"), reverse=True)

    if verbose:
        s += "\\section{{{}}}\n\n".format(_[sec][lang])
        for e in experiences:
            s += "\\{}\n".format(e["command"])

    else:
        for e in experiences:
            if e[lang+"-on"] == "true":
                s += "\\section{{{}}}\n\n".format(_[sec][lang])
                break

        for e in experiences:
            if e[lang+"-on"] == "true":
                s += "\\{}\n".format(e["command"])

    s += "\n"
    return s


def skills_section(lang):
    assert lang in ["zh", "en"]

    s = "\\section{{{}}}\n\n".format(_["skills"][lang])

    s += "\\vspace{0.618ex}\n"
    s += r"\begin{itemize}"
    s += "\n"

    for i in _["skills"]["details"][lang]:
        s += "\\item " + i.replace("LaTeX", r"{\LaTeX}")+"\n"
    s += r"\end{itemize}"
    s += "\n"
    return s


def render(lang, verbose):
    assert lang in ["en", "zh"]
    content = HEAD[lang] + get_content(lang, verbose) + TAIL
    path = os.path.join(lang, "CV-"+lang.upper() +
                        ("-verbose" if verbose else "") + ".tex")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


if __name__ == "__main__":
    for lang, verbose in [(x, y) for x in ("en", "zh") for y in (True, False)]:
        render(lang, verbose)
