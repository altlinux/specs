Name: python-module-GeoIP
Version: 1.2.3
Release: alt1.2.1.1

Summary: Python language bindings for GeoIP

Group: Development/Python
License: GPL
Url: http://www.maxmind.com/app/python

Packager: Vitaly Lipatov <lav@altlinux.ru>

%setup_python_module GeoIP

Source: http://www.maxmind.com/download/geoip/api/python/GeoIP-Python-%version.tar.bz2

BuildPreReq: rpm-build-compat >= 1.2

# Automatically added by buildreq on Sat Oct 11 2008
BuildRequires: libGeoIP-devel python-devel GeoIP-Lite-Country

%description
%name are the python language bindings for GeoIP.

%prep
%setup -n GeoIP-Python-%version

%build
%python_build_debug

%install
%python_install

%files
%doc README
%python_sitelibdir/*

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.3-alt1.2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.3-alt1.2.1
- Rebuild with Python-2.7

* Mon Mar 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3-alt1.2
- Rebuilt for debuginfo

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3-alt1.1
- Rebuilt with python 2.6

* Fri Oct 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.3-alt1
- new version 1.2.3 (with rpmrb script)
- cleanup spec

* Wed Jun 13 2007 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt0.1
- initial build for ALT Linux Sisyphus
