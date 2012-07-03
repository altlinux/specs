Name: python-module-egenix-mx-experimental
Version: 3.0.0
Release: alt3.1.1

Summary: eGenix mx-Extensions - EXPERIMENTAL package
Summary(ru_RU.KOI8-R): eGenix mx-Extensions - Экспериментальный пакет
License: eGenix.com Public License Agreement
Group: Development/Python

Packager: Python Development Team <python@packages.altlinux.org>

Url: http://www.egenix.com/products/python/mxExperimental/

Source: %name-%version.tar

BuildPreReq: libgmp-devel

%setup_python_module egenix-mx-experimental
%python_module_declare %python_sitelibdir/mx

%description
The eGenix mx Extension Series are a collection of
Python extensions written in ANSI C and Python
which provide a large spectrum of useful additions
to everyday Python programming.

This package includes experimental subpackages of the
series. Please understand that the software in these
packages is still in alpha state and does not meet the
quality standards of production quality software.

This software is brought to you by eGenix.com. The included
subpackages are either covered by the eGenix.com Public
License or the eGenix.com Commercial License and/or other
licenses. Please check the  subpackage documentation for
details or contact eGenix.com for more license information.

%prep
%setup

%build
%python_build_debug

%install
%python_install
find %buildroot/%python_sitelibdir/mx/ -type f -name 'test*.py' -delete
rm -rf %buildroot%python_sitelibdir/mx/__init__.py*
rm -rf %buildroot%python_sitelibdir/mx/Tidy/mxTidy/input.html

%files
%python_sitelibdir/mx/
%python_sitelibdir/*.egg-info
%doc COPYRIGHT* LICENSE* README mx/Number/Doc/* mx/Tidy/Doc/*

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.0-alt3.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.0-alt3.1
- Rebuild with Python-2.7

* Sun Mar 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0-alt3
- Rebuilt for debuginfo

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0-alt2
- Rebuilt with python 2.6

* Mon Aug 03 2009 Andrey Rahmatullin <wrar@altlinux.ru> 3.0.0-alt1
- 3.0.0

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.9.0-alt1.1
- Rebuilt with python-2.5.

* Tue Jan 11 2005 Andrey Orlov <cray@altlinux.ru> 0.9.0-alt1
-  New VErsion

* Sat Sep 11 2004 Andrey Orlov <cray@altlinux.ru> 0.8.0-alt8
- Invalid encoding delaration in russian description was fixed (bug #5121)

* Tue May 18 2004 Andrey Orlov <cray@altlinux.ru> 0.8.0-alt6
- Conditional operators excluded from spec

* Mon May 10 2004 Andrey Orlov <cray@altlinux.ru> 0.8.0-alt5.d
- Rebuild

* Thu Apr 22 2004 Andrey Orlov <cray@altlinux.ru> 0.8.0-alt4.d
- Rebuild with new rpm/python macros

* Tue Apr 13 2004 Andrey Orlov <cray@altlinux.ru> 0.8.0-alt3.d
- Rebuild with new rpm/python macros

* Thu Mar 25 2004 Andrey Orlov <cray@altlinux.ru> 0.8.0-alt2.d
- Initial release

