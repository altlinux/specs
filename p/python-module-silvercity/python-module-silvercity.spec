Name: python-module-silvercity
Version: 0.9.7
Release: alt4.1.1

Summary: SilverCity is a lexing package, based on Scintilla

Url: http://silvercity.sourceforge.net/
Group: Development/Python
License: BSD License

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/silvercity/SilverCity-%version.tar.bz2

#setup_python_module silvercity

# manually removed: eric
# Automatically added by buildreq on Sat Sep 23 2006
BuildRequires: gcc-c++ linux-libc-headers python-devel python-modules-encodings

%description
SilverCity is a lexing package, based on Scintilla, that can provide
lexical analysis for over 20 programming and markup langauges.
SilverCity can be used as a C++ library and also has scripting language
bindings for Python.

%prep
%setup -n SilverCity-%version
subst "1i#!/usr/bin/env python" PySilverCity/Scripts/*.py

%build
%python_build_debug

%install
%python_install

%files
%_bindir/*
%python_sitelibdir/*

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.7-alt4.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.7-alt4.1
- Rebuild with Python-2.7

* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.7-alt4
- Rebuilt for debuginfo

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.7-alt3
- Rebuilt with python 2.6

* Wed Nov 12 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9.7-alt2
- fix trailing CR in the first line

* Sat Apr 07 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9.7-alt1
- new version 0.9.7 (with rpmrb script)

* Sat Sep 23 2006 Vitaly Lipatov <lav@altlinux.ru> 0.9.6-alt0.1
- new version 0.9.6

* Wed Mar 23 2005 Vitaly Lipatov <lav@altlinux.ru> 0.9.5-alt3
- rebuild with python 2.4

* Thu Mar 03 2005 Vitaly Lipatov <lav@altlinux.ru> 0.9.5-alt2
- fix broken python require in cgi file

* Thu Mar 03 2005 Vitaly Lipatov <lav@altlinux.ru> 0.9.5-alt1
- first build for ALT Linux Sisyphus
