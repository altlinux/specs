
%define oname IceSSL

Name: python-module-%oname
Version: 0.0.5
Release: alt4

Summary: Some usfull functions for better integrating IceSSL and Python.

License: GPLv2
Group: System/Libraries
Url: http://git.etersoft.ru/people/imelnikov/packages/IcePySSL.git

%setup_python_module %oname

Source: IcePySSL-%version.tar.bz2
Patch: %name-alt-debuginfo.patch
Patch1: IcePySSL-0.0.5-alt-gcc4.6.patch

# Automatically added by buildreq on Fri Apr 18 2008
BuildRequires: boost-python-devel gcc-c++ libice-devel python-devel scons

BuildRequires: boost-devel >= 1.39.0

%description
IcePySSL is a python module, which provides some usefull functions for using
Ice (www.zeroc.com) in python (www.python.org) with secure connections 
over IceSSL.

Currently python mapping for IceSSL::getConnectionInfo() function is implemented.

%prep
%setup -q -n IcePySSL-%version
%patch0 -p2
%patch1 -p2

%build
scons

%install
scons install DESTDIR=%buildroot

%files
%python_sitelibdir/*

%changelog
* Wed Jun 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt4
- Fixed build

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.5-alt3.1.3.3.1
- Rebuild to remove redundant libpython2.7 dependency

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt3.1.3.3
- Rebuilt with Boost 1.49.0

* Sat Dec 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt3.1.3.2
- Rebuilt with Boost 1.48.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.5-alt3.1.3.1
- Rebuild with Python-2.7

* Wed Jul 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt3.1.3
- Rebuilt with Boost 1.47.0

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt3.1.2
- Rebuilt with Boost 1.46.1 and for debuginfo

* Wed Dec 08 2010 Igor Vlasenko <viy@altlinux.ru> 0.0.5-alt3.1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt3.1
- Rebuilt with python 2.6

* Sat Jun 27 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.0.5-alt3
- rebuild with boost-1.39.0

* Fri Jan 23 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.0.5-alt2
- build for sisyphus

* Fri Sep 12 2008 Ivan A. Melnikov <iv@altlinux.org> 0.0.5-alt1
- new version: intal support for IceSSL CertificateVerifier

* Thu Sep 11 2008 Ivan A. Melnikov <iv@altlinux.org> 0.0.4-alt1
- new version
  - support for Ice 3.3.0

* Thu Jun 05 2008 Ivan A. Melnikov <iv@altlinux.org> 0.0.3-alt1
- new version

* Sun May 04 2008 Ivan A. Melnikov <iv@altlinux.org> 0.0.2-alt1
- new version

* Fri Apr 18 2008 Ivan A. Melnikov <iv@altlinux.org> 0.0.2-alt1
- inital build


