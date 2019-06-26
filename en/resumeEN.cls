\LoadClass{article}

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{resumeEN}[2019/2/24 Resume Class by Vopaaz]

\RequirePackage{titlesec}
\RequirePackage{hyperref}
\hypersetup{colorlinks,allcolors=black}

\pagestyle{empty}

\RequirePackage{enumitem}

\setitemize[1]{itemsep=0pt,partopsep=0pt,parsep=0pt,topsep=0pt}
\setitemize[2]{itemsep=0pt,partopsep=0pt,parsep=0pt,topsep=0pt}

\RequirePackage{fontspec}

\setmainfont{Times New Roman}

\setlength{\parindent}{0pt}

\RequirePackage{titlesec}

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

\DeclareDocumentCommand{\Experience}{ m m o m m m }{%

    \vspace{0.618ex}

    \textbf{#1} \hfill #4 \\
    \IfNoValueTF{#3}{
        #2 \hfill #5
    }{
        #2 \hfill #5\\
        #3
    }
    \begin{itemize}
        #6
    \end{itemize}

}

