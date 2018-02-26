Name:    tetex-latex-bibtopic
Version: 1.0k
Release: alt2.1
Summary: LaTeX package for including several bibliographies in a document
License: GPL
Group:   Publishing
URL:     http://www.ctan.org

BuildArch: noarch

BuildRequires: tetex-core tetex-latex
Requires: tetex-core tetex-latex

Source0: bibtopic.tar.bz2

%description 
bibtopic is a LaTeX package for including several bibliographies in a document.
These bibliographies might be considered to cover different topics (hence the name)
or bibliographic material (e.g., primary and secondary literature) and the like.

%prep
%setup -q -n bibtopic

%build
latex bibtopic.ins

%install
%__mkdir_p %buildroot{%_datadir/texmf/tex/latex/bibtopic,%_docdir}
install -m644 *.sty %buildroot%_datadir/texmf/tex/latex/bibtopic/

%files
%_datadir/texmf/tex/latex/bibtopic/*.sty
%doc README bibtopic.pdf sample.tex

%changelog
* Thu Nov 05 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.0k-alt2.1
- NMU (by repocop): the following fixes applied:
  * altlinux-policy-tex-obsolete-util-calls-in-post for tetex-latex-bibtopic

* Sun Feb 26 2006 Vladimir Lettiev <crux@altlinux.ru> 1.0k-alt2
- release update (no changes)

* Tue Mar 22 2005 Vladimir Lettiev <crux@altlinux.ru> 1.0k-alt1
- initial build for ALTLinux Sisyphus


