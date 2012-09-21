%define srcName tabulary

Name: tetex-latex-%srcName
Version: 0.9
Release: alt1.qa1
Summary: Tabular environment with variable width columns balanced
License: LPPL (LaTeX Project Public License)
Group: Publishing
Url: http://www.ctan.org/tex-archive/macros/latex/contrib/tabulary
Packager: Kirill Maslinsky <kirill@altlinux.org>

BuildArch: noarch

Requires: tetex-core tetex-latex

Source0: %srcName-%version.tar.bz2

# Automatically added by buildreq on Tue Sep 04 2007
BuildRequires: tetex-latex

%description
The package defines a tabular*-like tabulary environment, taking a
"total width" argument as well as the column specifications.  It then
defines column types L, C, R and J for variable width columns
(\raggedright, \centering, \raggedleft, and normally justified).
In contrast to tabularx's X columns,
the width of each column is weighted according to the natural
width of the widest cell in the column.

%prep
%setup -q -n %srcName-%version

%build
latex tabulary.ins

%install
mkdir -p %buildroot%_datadir/texmf/tex/latex/carlisle
install -pD -m644 tabulary.sty %buildroot%_datadir/texmf/tex/latex/carlisle/

%files
%_datadir/texmf/tex/latex/carlisle/tabulary.sty
%doc README tabulary.pdf

%changelog
* Fri Sep 21 2012 Repocop Q. A. Robot <repocop@altlinux.org> 0.9-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * altlinux-policy-tex-obsolete-util-calls-in-post for tetex-latex-tabulary
  * postclean-03-private-rpm-macros for the spec file

* Thu Nov 22 2007 Kirill Maslinsky <kirill@altlinux.org> 0.9-alt1
- Initial build for Sisyphus

