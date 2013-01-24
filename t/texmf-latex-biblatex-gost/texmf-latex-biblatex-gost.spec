%define srcName biblatex-gost

Name: texmf-latex-%srcName
Version: 0.7.1
Release: alt1
Summary: Biblatex support for GOST bibliography style 
License: LPPL (LaTeX Project Public License)
Group: Publishing
Url: http://sourceforge.net/projects/biblatexgost
Packager: Kirill Maslinsky <kirill@altlinux.org>

BuildRequires(pre): rpm-build-texmf

BuildArch: noarch

Source0: %srcName.tar

%description
Biblatex style to format bibliography according to Russian standard 
GOST 7.0.5-2008

%prep
%setup %srcName.tar

%build

%install
mkdir -p %buildroot%_texmfmain/tex/
mkdir -p %buildroot%_texmfdoc/
cp -a tex/* %buildroot%_texmfmain/tex/
cp -a doc/* %buildroot/%_texmfdoc/

%files
%_texmfmain/tex/latex/%srcName
%_texmfdoc/latex/%srcName

%changelog
* Thu Jan 24 2013 Kirill Maslinsky <kirill@altlinux.org> 0.7.1-alt1
- initial build for ALT Linux Sisyphus

