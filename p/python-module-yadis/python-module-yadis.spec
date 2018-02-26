Name: python-module-yadis
Version: 1.1.0
Release: alt4.1

Summary: Yadis service discovery library.

Group: Development/Python
License: GPL
Url: http://www.openidenabled.com/

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

%setup_python_module yadis

Source: http://www.openidenabled.com/resources/downloads/python-openid/python-yadis-%version.tar.bz2

# Automatically added by buildreq on Sat Apr 07 2007
BuildRequires: python-devel python-modules-compiler rpm-build-python

%description
Yadis is a protocol for discovering services applicable to a URL.
This package provides a client implementation of the Yadis protocol.

%prep
%setup -q -n python-%modulename-%version

%build
%python_build

%install
%python_install

%files
%doc README
%python_sitelibdir/*

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt4.1
- Rebuild with Python-2.7

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt4
- Rebuilt with python 2.6

* Wed Oct 14 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt3
- cleanup spec

* Thu Jan 31 2008 Grigory Batalov <bga@altlinux.ru> 1.1.0-alt2.1
- Rebuilt with python-2.5.

* Thu Jan 31 2008 Grigory Batalov <bga@altlinux.ru> 1.1.0-alt2
- Build as noarch.

* Sat Apr 07 2007 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- initial build for ALT Linux Sisyphus
