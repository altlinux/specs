Name: python-module-pycurl
Version: 7.19.0
Release: alt1.2.1.1

Summary: Python bindings to libcurl

Group: Development/Python
License: LGPL
Url: http://pycurl.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

%setup_python_module pycurl

#Source: http://dl.sf.net/%modulename/%modulename-%version.tar.bz2
Source: http://pycurl.sourceforge.net/download/pycurl-%version.tar.bz2

BuildRequires: libcurl-devel libssh2-devel python-devel

BuildPreReq: libssl-devel libidn-devel zlib-devel

%description
This module provides the Python bindings to libcurl.

%prep
%setup -n %modulename-%version

%build
%python_build_debug

%install
%python_install

%files
%python_sitelibdir/*
%_docdir/%modulename/

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 7.19.0-alt1.2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 7.19.0-alt1.2.1
- Rebuild with Python-2.7

* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.19.0-alt1.2
- Rebuilt for debuginfo

* Sun Mar 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.19.0-alt1.1
- Fixed build

* Thu Dec 02 2010 Ivan Fedorov <ns@altlinux.org> 7.19.0-alt1
- 7.19.0

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.16.4-alt2
- Rebuilt with python 2.6

* Tue Jan 29 2008 Grigory Batalov <bga@altlinux.ru> 7.16.4-alt1.1
- Rebuilt with python-2.5.

* Wed Jan 02 2008 Vitaly Lipatov <lav@altlinux.ru> 7.16.4-alt1
- new version 7.16.4 (with rpmrb script)

* Sat Apr 07 2007 Vitaly Lipatov <lav@altlinux.ru> 7.16.1-alt1
- new version 7.16.1 (with rpmrb script)

* Sun Feb 04 2007 Vitaly Lipatov <lav@altlinux.ru> 7.16-alt0.1cvs
- build from CVS 20070204

* Sat Nov 11 2006 Vitaly Lipatov <lav@altlinux.ru> 7.15.5.1-alt0.1
- initial build for ALT Linux Sisyphus
