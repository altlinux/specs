%define modulename timelib

%def_with python3

Name: python-module-%modulename
Version: 0.2.4
Release: alt1

Summary: Parse english textual date descriptions

Group: Development/Python
License: zlib / PHP
Url: http://pypi.python.org/pypi/%modulename

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pypi.python.org/packages/source/t/%modulename/%modulename-%version.tar

%setup_python_module %modulename
BuildPreReq: python-devel python-module-setuptools python-module-Cython
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools python3-module-Cython
%endif

%description
timelib is a short wrapper around php's internal timelib module.
It currently only provides a few functions:
 * timelib.strtodatetime
 * timelib.strtotime

%package -n python3-module-%modulename
Summary: Parse english textual date descriptions
Group: Development/Python3

%description -n python3-module-%modulename
timelib is a short wrapper around php's internal timelib module.
It currently only provides a few functions:
 * timelib.strtodatetime
 * timelib.strtotime

%prep
%setup -n %modulename-%version
rm -f timelib.c

%if_with python3
cp -fR . ../python3
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
%doc README.rst
%python_sitelibdir/%modulename.so
%python_sitelibdir/%modulename-%version-*.egg-info

%if_with python3
%files -n python3-module-%modulename
%doc README.rst
%python3_sitelibdir/*
%endif

%changelog
* Mon Sep 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.4-alt1
- Version 0.2.4
- Added module for Python 3

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.1-alt1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.1-alt1.1
- Rebuild with Python-2.7

* Mon Feb 08 2010 Vitaly Lipatov <lav@altlinux.ru> 0.2.1-alt1
- initial build for ALT Linux Sisyphus
