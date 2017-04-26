Name: texmf-latex-linegoal
Version: 2.9
Release: alt1
License: LPPL
Summary: Flexible LaTeX linegoallars
Group: Publishing
BuildArch: noarch
Source: http://mirrors.ctan.org/macros/latex/contrib/linegoal.zip

BuildRequires: texlive-latex-recommended rpm-build-texmf
# Automatically added by buildreq on Mon Apr 24 2017
# optimized out: python-base python-modules tex-common texlive-base-bin texlive-common texlive-latex-base
BuildRequires: unzip

%description
linegoal provides a single environment:          linegoal
designed to make all kind of linegoallars provided that they do
not split accross pages.

%prep
%setup -n linegoal

%build
latex '\let\install=y\input{linegoal.dtx}'

%install
install -D linegoal.sty  %buildroot%_texmfmain/tex/latex/linegoal/linegoal.sty

%files
%doc *pdf README*
%_texmfmain/tex/latex/linegoal


%changelog
* Mon Apr 24 2017 Fr. Br. George <george@altlinux.ru> 2.9-alt1
- Initial build for ALT

