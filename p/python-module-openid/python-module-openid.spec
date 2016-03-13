%def_with python3

Name: python-module-openid
Version: 2.2.5
Release: alt2.1

Summary: OpenID support for servers and consumers

Group: Development/Python
License: GPL
Url: http://www.openidenabled.com/

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

#setup_python_module openid
%define modulename openid

Source: http://openidenabled.com/files/python-openid/packages/python-openid-%version.tar.bz2

# Automatically added by buildreq on Wed May 14 2008
BuildRequires: python-devel

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildPreReq: python-tools-2to3
%endif

%description
This is a set of Python packages to support use of the OpenID
decentralized identity system in your application.
Want to enable single sign-on for your web site?
Use the openid.consumer package.
Want to run your own OpenID server? Check out openid.server.
Includes example code and support for a variety of storage back-ends.

%package -n python3-module-%modulename
Summary: OpenID support for servers and consumers
Group: Development/Python3

%description -n python3-module-%modulename
This is a set of Python packages to support use of the OpenID
decentralized identity system in your application.
Want to enable single sign-on for your web site?
Use the openid.consumer package.
Want to run your own OpenID server? Check out openid.server.
Includes example code and support for a variety of storage back-ends.

%package examples
Summary: Examples for OpenOD Python package
Group: Development/Python
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
%setup -n python-%modulename-%version

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc README CHANGES* LICENSE NEWS NOTICE *.txt
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%files examples
%doc examples

%if_with python3
%files -n python3-module-%modulename
%doc README CHANGES* LICENSE NEWS NOTICE *.txt
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%endif

%changelog
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
