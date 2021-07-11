%define oname python3-openid

Name: python3-module-openid
Version: 3.2.0
Release: alt1

Summary: OpenID support for servers and consumers

Group: Development/Python3
License: GPL
Url: http://www.openidenabled.com/

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

%description
This is a set of Python packages to support use of the OpenID
decentralized identity system in your application.
Want to enable single sign-on for your web site?
Use the openid.consumer package.
Want to run your own OpenID server? Check out openid.server.
Includes example code and support for a variety of storage back-ends.

%package examples
Summary: Examples for OpenOD Python package
Group: Development/Python3
BuildArch: noarch
Conflicts: %name < %version-%release

%description examples
This is a set of Python packages to support use of the OpenID
decentralized identity system in your application.
Want to enable single sign-on for your web site?
Use the openid.consumer package.
Want to run your own OpenID server? Check out openid.server.
Includes example code and support for a variety of storage back-ends.

This package contains examples for OpenOD Python package.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc README.md NEWS.md
%python3_sitelibdir/*

%files examples
%doc examples

%changelog
* Sat Jul 10 2021 Vitaly Lipatov <lav@altlinux.ru> 3.2.0-alt1
- build new python3 module separately

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.2.5-alt2.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.2.5-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.5-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.5-alt1.1
- Rebuild with Python-2.7

* Sat Nov 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.5-alt1
- Version 2.2.5
- Added examples

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.4-alt1.1
- Rebuilt with python 2.6

* Wed Oct 14 2009 Vitaly Lipatov <lav@altlinux.ru> 2.2.4-alt1
- new version 2.2.4 (with rpmrb script)

* Sat Jul 05 2008 Vitaly Lipatov <lav@altlinux.ru> 2.2.1-alt1
- new version 2.2.1 (with rpmrb script)

* Wed May 14 2008 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt3
- update buildreqs
- do not use setup_python-module macros

* Thu Jan 31 2008 Grigory Batalov <bga@altlinux.ru> 2.1.1-alt2.1
- Rebuilt with python-2.5.

* Thu Jan 31 2008 Grigory Batalov <bga@altlinux.ru> 2.1.1-alt2
- Build as noarch.

* Wed Jan 23 2008 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt1
- new version 2.1.1 (with rpmrb script)

* Tue Oct 16 2007 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt1
- new version 2.0.1 (with rpmrb script)

* Sat Apr 07 2007 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- new version 1.2.0 (with rpmrb script)

* Sat Nov 11 2006 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt0.1
- new version 1.1.0 (with rpmrb script)

* Sat Nov 11 2006 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt0.1
- new version 1.1.1 (with rpmrb script)

* Thu Dec 22 2005 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt0.1
- initial build for ALT Linux Sisyphus
