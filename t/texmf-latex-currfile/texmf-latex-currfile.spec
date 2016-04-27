Name:    texmf-latex-currfile
Version: 0.7c
Release: alt1
Summary: Provide file name and path of input files
License: GPL
Group:	Publishing
URL:	http://www.ctan.org/pkg/currfile

BuildArchitectures: noarch
BuildRequires(pre): rpm-build-texmf

Packager: %packager

Source: %name-%version.tar

%description 
The package provides macros holding file name information
(directory, base name, extension, full name and full path)
for files read by LaTeX \input and \include macros; it uses
the file hooks provided by the author's filehook. In particular,
it restores the parent file name after the trailing \clearpage of
an \included file; as a result, the macros may be usefully
employed in the page header and footer of the last printed page
of such a file.

The depth of inclusion is made available, together with
the "parent" (including file) and "parents" (all including
files to the root of the tree).

The package supersedes FiNK.

%prep
%setup -q -n %name-%version

%install
# Основные каталоги
mkdir -p %buildroot%_texmfdoc/currfile
mkdir -p %buildroot%_texmfmain/tex/latex/currfile

# Документация
%__mkdir_p %buildroot%_texmfdoc/tex/latex/currfile

install -pD -m644 tex/latex/currfile/currfile-abspath.sty %buildroot%_texmfmain/tex/latex/currfile/
install -pD -m644 tex/latex/currfile/currfile.sty %buildroot%_texmfmain/tex/latex/currfile/

# Документация
install -pD -m644 doc/latex/currfile/* %buildroot%_texmfdoc/tex/latex/currfile/

%files
%dir %_texmfmain/tex/latex/currfile
%dir %_texmfdoc/tex/latex/currfile

%_texmfmain/tex/latex/currfile/*
%_texmfdoc/tex/latex/currfile/*

%changelog
* Tue Apr 26 2016 Andrey Bergman <vkni@altlinux.org> 0.7c-alt1
- Version update.

* Sat Mar 29 2014 Andrey Bergman <vkni@altlinux.org> 0.7b-alt1
- Initial release for Sisyphus

