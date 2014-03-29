Name:    texmf-latex-filehook
Version: 0.5d
Release: alt1
Summary: Hooks for input files
License: GPL
Group:	Publishing
URL:	http://www.ctan.org/pkg/filehook

BuildArchitectures: noarch
BuildRequires(pre): rpm-build-texmf

Packager: %packager

Source: %name-%version.tar

%description 
The package provides several file hooks (AtBegin, AtEnd, etc.)
for files read by \input, \include and \InputIfFileExists.
General hooks for all such files (e.g. all \include'd ones)
and file specific hooks only used for named files are provided;
two hooks are provided for the end of \included files - one before,
and one after the final \clearpage.

%prep

%setup -q -n %name-%version

%install
# Основные каталоги
mkdir -p %buildroot%_texmfdoc/filehook
mkdir -p %buildroot%_texmfmain/tex/latex/filehook

# Документация
%__mkdir_p %buildroot%_texmfdoc/tex/latex/filehook

install -pD -m644 tex/latex/filehook/pgf-filehook.sty %buildroot%_texmfmain/tex/latex/filehook/
install -pD -m644 tex/latex/filehook/filehook-memoir.sty %buildroot%_texmfmain/tex/latex/filehook/
install -pD -m644 tex/latex/filehook/filehook-listings.sty %buildroot%_texmfmain/tex/latex/filehook/
install -pD -m644 tex/latex/filehook/filehook-scrlfile.sty %buildroot%_texmfmain/tex/latex/filehook/
install -pD -m644 tex/latex/filehook/filehook.sty %buildroot%_texmfmain/tex/latex/filehook/
install -pD -m644 tex/latex/filehook/filehook-fink.sty %buildroot%_texmfmain/tex/latex/filehook/

# Документация
install -pD -m644 doc/latex/filehook/* %buildroot%_texmfdoc/tex/latex/filehook/

%files
%dir %_texmfmain/tex/latex/filehook
%dir %_texmfdoc/tex/latex/filehook

%_texmfmain/tex/latex/filehook/*
%_texmfdoc/tex/latex/filehook/*

%changelog
* Sat Mar 29 2014 Andrey Bergman <vkni@altlinux.org> 0.5d-alt1
- Initial release for Sisyphus

