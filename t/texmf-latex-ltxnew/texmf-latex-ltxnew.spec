Name: texmf-latex-ltxnew
Version: 1.3
Release: alt1
License: LPPL
Summary: Flexible LaTeX ltxnewlars
Group: Publishing
BuildArch: noarch
Source: http://mirrors.ctan.org/macros/latex/contrib/ltxnew.zip

BuildRequires: texlive-latex-recommended rpm-build-texmf
# Automatically added by buildreq on Mon Apr 24 2017
# optimized out: python-base python-modules tex-common texlive-base-bin texlive-common texlive-latex-base
BuildRequires: unzip

%description
ltxnew provides a single environment:          ltxnew
designed to make all kind of ltxnewlars provided that they do
not split accross pages.

%prep
%setup -n ltxnew

%build
latex '\let\install=y\input{ltxnew.dtx}'

%install
install -D ltxnew.sty  %buildroot%_texmfmain/tex/latex/ltxnew/ltxnew.sty

%files
%doc *pdf README*
%_texmfmain/tex/latex/ltxnew

%changelog
* Mon Apr 24 2017 Fr. Br. George <george@altlinux.ru> 1.3-alt1
- Initial build for ALT


