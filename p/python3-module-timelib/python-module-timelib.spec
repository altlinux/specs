%define oname timelib
%define fname python3-module-%oname
%define descr \
timelib is a short wrapper around php's internal timelib module. \
It currently only provides a few functions: \
 * timelib.strtodatetime \
 * timelib.strtotime

Name: %fname
Version: 0.2.4
Release: alt2

Summary: Parse english textual date descriptions
Group: Development/Python3

License: zlib / PHP
Url: http://pypi.python.org/pypi/timelib
Source: %name-%version.tar

BuildPreReq: python3-devel python3-module-setuptools

%description
%descr

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc README.rst
%python3_sitelibdir/*

%changelog
* Fri Mar 23 2018 Grigory Ustinov <grenka@altlinux.org> 0.2.4-alt2
- Tranfer package to subst-packaging system.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.4-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Mon Sep 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.4-alt1
- Version 0.2.4
- Added module for Python 3

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.1-alt1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.1-alt1.1
- Rebuild with Python-2.7

* Mon Feb 08 2010 Vitaly Lipatov <lav@altlinux.ru> 0.2.1-alt1
- initial build for ALT Linux Sisyphus
