Name:    texmf-standalone
Version: 1.1b
Release: alt1
Summary: Compile TeX pictures stand-alone or as part of a document
Summary(ru_RU.UTF-8): LaTeX класс для раздельной компиляции изображений TeX
License: GPL
Group:	Publishing
URL:	http://www.ctan.org/pkg/standalone 

BuildArchitectures: noarch
BuildRequires(pre): rpm-build-texmf

Packager: Andrey Bergman <vkni@altlinux.org>

Source: %name-%version.tar

%description 
A class and package is provided which allows TeX pictures or
other TeX code to be compiled standalone or as part of a main
document. Special support for pictures with beamer overlays is
also provided.

The package is used in the main document and skips extra preambles
in subfiles. The class may be used to simplify the preamble in
subfiles. By default the preview package is used to display the
code without margins.

The behaviour in standalone mode may adjusted using a configuration
file standalone.cfg to redefine the standalone environment.

%prep
%setup -q -n %name-%version

%install
# Основные каталоги
mkdir -p %buildroot%_texmfdoc/standalone
mkdir -p %buildroot%_texmfmain/tex/{plain,latex}/standalone

# Документация
%__mkdir_p %buildroot%_texmfdoc/tex/latex/standalone

install -pD -m644 tex/latex/standalone/standalone.cfg %buildroot%_texmfmain/tex/latex/standalone/
install -pD -m644 tex/latex/standalone/standalone.cls %buildroot%_texmfmain/tex/latex/standalone/
install -pD -m644 tex/latex/standalone/standalone.sty %buildroot%_texmfmain/tex/latex/standalone/

install -pD -m644 tex/plain/standalone/standalone.tex %buildroot%_texmfmain/tex/plain/standalone/

# Документация
install -pD -m644 doc/latex/standalone/* %buildroot%_texmfdoc/tex/latex/standalone/

%files
%dir %_texmfmain/tex/latex/standalone
%dir %_texmfmain/tex/plain/standalone
%dir %_texmfdoc/tex/latex/standalone

%_texmfmain/tex/latex/standalone/*
%_texmfmain/tex/plain/standalone/*
%_texmfdoc/tex/latex/standalone/*

%changelog
* Sat Mar 29 2014 Andrey Bergman <vkni@altlinux.org> 1.1b-alt1
- Initial release for Sisyphus

