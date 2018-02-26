%define oname python-xlib
Name: python-module-xlib
Version: 0.15
Release: alt1.rc1.1

Summary: Python X Library

Group: Development/Python
License: LGPL
Url: http://python-xlib.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://dl.sf.net/%oname/%oname-%version.tar.bz2

#%%setup_python_module Xlib
#%add_python_req_skip audio image video misc

# manually removed: eric
# Automatically added by buildreq on Sun Dec 18 2005
BuildRequires: python-devel python-modules-compiler python-modules-encodings

%description
The Python X Library is a complete X11R6 client-side implementation,
written in pure Python. It can be used to write low-levelish X Windows
client applications in Python.

%package docs
Summary: Documentation and examples for Python X Library
Group: Development/Documentation
BuildArch: noarch

%description docs
The Python X Library is a complete X11R6 client-side implementation,
written in pure Python. It can be used to write low-levelish X Windows
client applications in Python.

This package contains documentation and examples for Python X Library.

%prep
%setup -n %oname-%version

%build
%python_build

pushd doc/html
%make SRCS=$PWD/../src TOPSRC=$PWD/../src/python-xlib.texi
popd

%install
CFLAGS="%optflags" python setup.py install --root %buildroot

# hack for x86_64 build
test -d %buildroot%_libdir || mv %buildroot%prefix/lib %buildroot%_libdir || :

%files
%doc NEWS README
%python_sitelibdir/*

%files docs
%doc examples doc/html/*.html

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.15-alt1.rc1.1
- Rebuild with Python-2.7

* Sun Nov 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15-alt1.rc1
- Version 0.15rc1

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14-alt1.1.1
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.14-alt1.1
- Rebuilt with python-2.5.

* Tue Oct 16 2007 Vitaly Lipatov <lav@altlinux.ru> 0.14-alt1
- new version 0.14 (with rpmrb script)

* Tue Sep 12 2006 Vitaly Lipatov <lav@altlinux.ru> 0.12-alt2
- override alt1 in incoming :)
- fix hack for x86_64 :)

* Tue Jun 20 2006 Vitaly Lipatov <lav@altlinux.ru> 0.12-alt0.2
- hack for build at x86_64 (fix bug #9710)

* Sun Dec 18 2005 Vitaly Lipatov <lav@altlinux.ru> 0.12-alt0.1
- initial build for ALT Linux Sisyphus
