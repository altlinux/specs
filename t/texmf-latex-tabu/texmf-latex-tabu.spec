Name: texmf-latex-tabu
Version: 2.8
Release: alt1
License: LPPL
Summary: Flexible LaTeX tabulars
Group: Publishing
BuildArch: noarch
Source: http://mirrors.ctan.org/macros/latex/contrib/tabu.zip

BuildRequires: texlive-latex-recommended rpm-build-texmf
# Automatically added by buildreq on Mon Apr 24 2017
# optimized out: python-base python-modules tex-common texlive-base-bin texlive-common texlive-latex-base
BuildRequires: unzip

%description
tabu provides a single environment:          tabu
designed to make all kind of tabulars provided that they do
not split accross pages.

%prep
%setup -n tabu

%build
latex '\let\install=y\input{tabu.dtx}'

%install
install -D tabu.sty  %buildroot%_texmfmain/tex/latex/tabu/tabu.sty

%files
%doc *pdf README*
%_texmfmain/tex/latex/tabu


%changelog
* Mon Apr 24 2017 Fr. Br. George <george@altlinux.ru> 2.8-alt1
- Initial build for ALT

