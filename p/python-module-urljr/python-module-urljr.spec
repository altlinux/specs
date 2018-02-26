Name: python-module-urljr
Version: 1.0.1
Release: alt1.1.1

Summary: URL-related utilites

Group: Development/Python
License: LGPL
Url: http://www.openidenabled.com/

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

%setup_python_module urljr

Source: http://openidenabled.com/files/python-openid/files/python-urljr-%version.tar.bz2

# Automatically added by buildreq on Sat Nov 11 2006
BuildRequires: python-devel python-modules-encodings
BuildPreReq: rpm-build-compat >= 1.2

%description
URL-related utilites, including a common interface to HTTP fetchers for PycURL and urllib2.

%prep
%setup -q -n python-%modulename-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/*

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.1-alt1.1.1
- Rebuild with Python-2.7

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.1
- Rebuilt with python 2.6

* Sat Jul 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- new version 1.0.1 (with rpmrb script)

* Sat Nov 11 2006 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt0.1
- initial build for ALT Linux Sisyphus
