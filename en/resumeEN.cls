\LoadClass{article}

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{resumeZH}[2019/2/24 Resume Class by Vopaaz]

\RequirePackage{titlesec}
\RequirePackage{hyperref}
\hypersetup{colorlinks,allcolors=black}

\RequirePackage{titlesec}

\pagestyle{empty}

\RequirePackage{enumerate}
\RequirePackage{enumitem}
\setitemize[1]{itemsep=0pt,partopsep=0pt,parsep=0pt,topsep=0pt}
\setitemize[2]{itemsep=0pt,partopsep=0pt,parsep=0pt,topsep=0pt}

\setlength{\parindent}{0pt}

\titlespacing{\section}{0pt}{*0.5}{*0.9}

\titleformat{\section}
{\Large\scshape\raggedright}
{}{0em}
{}
[\titlerule]

\newcommand{\contact}[3]{
    \begin{center}
        {\huge\scshape #1}\\
        #2 | \href{mailto:#3}{#3}
    \end{center}
}

\newcommand{\Experience}[4]{
    \vspace{0.618ex}
    \textbf{#1} \hfill #2 \\
    #3 \hfill #4
}

