# -*- coding: utf-8 -*-
%define targetdir  %_datadir/python-doc-tools

# Hack! Hack! Hack!
%define _perl_lib_path %targetdir/tools
%define __find_provides %SOURCE1
%define __find_requires %SOURCE2

Name: python-doc-tools
Version: 0.0.1
Release: alt5.1
BuildArch: noarch
Packager: Alexey Morozov <morozov@altlinux.org>

Requires: make python perl-base latex2html lynx
Requires: /usr/bin/dvips /usr/bin/latex

Summary: A set of standard tools to convert python modules documentation
License: PSF
Group: Development/Python
Url: http://www.python.org

Source0: %name-%version.tar.bz2
Source1: %name.find-provides
Source2: %name.find-requires

%description
This package contains a set of scripts (python, perl), images, TeX
style files, etc. to build unified-styled documentation for python
modules from TeX/LaTeX sources.

%description -l ru_RU.UTF-8
Этот пакет содержит набор сценариев (python, perl), изображений,
файлов стилей TeX и т.д. для построения выдержанной в едином стиле
документации для модулей питон из исходников на TeX/LaTex

%prep
%setup -q -n %name
cat >README <<EOF
Usage:

    make -f %targetdir/Makefile MODULE=<YourModuleName> [<TargetFormat>]

Supported formats:
    html
    text
    dvi
    ps
EOF
rm -rf tools/push-docs.sh
rm -rf tools/update-docs.sh

%install
mkdir -p %buildroot%targetdir
cp -pr * %buildroot%targetdir
unset RPM_PYTHON

%files
%doc README
%targetdir

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.1-alt5.1
- Rebuild with Python-2.7

* Tue Feb 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt5
- Rollback creating texmf subtree (inspired by kirill@)

* Fri Feb 12 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt2
- Really don't require tetex

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.1.1
- Rebuilt with python 2.6
- Don't require tetex (ALT #22173)

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.0.1-alt1.1
- Rebuilt with python-2.5.

* Tue Jan 13 2004 Alexey Morozov <morozov@altlinux.org> 0.0.1-alt1
- Initial build (sources shamelessly stolen from python-pyOpenSSL
  package)


