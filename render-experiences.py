import json
import os
import datetime
import re

with open("experience.json", "r", encoding="utf-8") as f:
    _ = json.load(f)


def preprocess(s):
    s = s.replace("LaTeX", r"{\LaTeX}").replace("%", r"\%").replace("&", r"\&")

    s = re.compile(r"\$HREF\{(.*?)\}\{(.*?)\}").sub(
        lambda m_obj: "\\href{{{}}}{{{}}}".format(m_obj.group(2), m_obj.group(1)), s
    )

    s = re.compile(r"\$TEXTIT\{(.*?)\}").sub(lambda m_obj: "\\textit{{{}}}".format(m_obj.group(1)), s)
    return s


def format_time(raw_time, lang):
    assert lang in ["en", "zh"]
    start, stop = raw_time.split("-")
    start = start.strip()
    stop = stop.strip()

    start = string_to_time_general(start, lang)

    if stop.lower() == "now":
        if lang == "zh":
            stop = "至今"
        else:
            stop = "Present"
    else:
        stop = string_to_time_general(stop, lang)

    return start + " - " + stop


def string_to_time_general(t, lang):
    t = datetime.datetime.strptime(t, r"%Y/%m")
    if lang == "zh":
        t = t.strftime("%Y") + "年" + str(int(t.strftime("%m"))) + "月"
    else:
        t = t.strftime("%b %Y")
    return t


def get_content(lang):
    s = ""
    for v in _.values():
        if "experiences" in v:
            for e in v["experiences"]:
                if "sub-position" not in e[lang]:
                    s += """\\newcommand{{\\{}}}{{
    \\Experience
    {{{}}}
    {{{}}}
    {{{}}}
    {{{}}}{{
""".format(
                        e["command"],
                        preprocess(e[lang]["title"]),
                        preprocess(e[lang]["position"]),
                        format_time(e["time"], lang),
                        preprocess(e[lang]["location"]),
                    )

                else:
                    s += """\\newcommand{{\\{}}}{{
    \\Experience
    {{{}}}
    {{{}}}
    [{}]
    {{{}}}
    {{{}}}{{
""".format(
                        e["command"],
                        preprocess(e[lang]["title"]),
                        preprocess(e[lang]["position"]),
                        e[lang]["sub-position"],
                        format_time(e["time"], lang),
                        preprocess(e[lang]["location"]),
                    )

                for i in e[lang]["details"]:
                    s += r"    \item " + preprocess(i) + "\n"

                s += """    }
}

"""

    return s


def render(lang):
    with open(os.path.join(lang, "experience.tex"), "w", encoding="utf-8") as f:
        f.write(get_content(lang))


if __name__ == "__main__":
    render("en")
    render("zh")
