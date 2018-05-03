%def_without check
%def_with python3

%define modulename dukpy
Name: python-module-dukpy
Version: 0.1.0
Release: alt1.1

Summary: Simple JavaScript interpreter for Python

Url: https://pypi.python.org/pypi/dukpy/
License: MIT License
Group: Development/Python


Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://pypi.io/packages/source/d/%modulename/%modulename-%version.tar.gz
Source: %name-%version.tar

BuildRequires: python-dev python-module-setuptools

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

#setup_python_module %modulename

%description
DukPy is a simple javascript interpreter for Python
built on top of duktape engine without any external dependency.
It comes with a bunch of common transpilers built-in for convenience:
CoffeeScript, BabelJS, TypeScript, JSX, LESS
Dukpy has been tested on Python 2.7 and Python 3.4,
dukpy is currently not production ready and might
actually crash your program as it is mostly implemented in C.


%package -n python3-module-dukpy
Summary: Simple JavaScript interpreter for Python
Group: Development/Python3

%description -n python3-module-dukpy
DukPy is a simple javascript interpreter for Python
built on top of duktape engine without any external dependency.
It comes with a bunch of common transpilers built-in for convenience:
CoffeeScript, BabelJS, TypeScript, JSX, LESS
Dukpy has been tested on Python 2.7 and Python 3.4,
dukpy is currently not production ready and might
actually crash your program as it is mostly implemented in C.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
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
%python_sitelibdir/*

%if_with python3
%files -n python3-module-dukpy
%python3_sitelibdir/*
%endif


%changelog
* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.0-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Mon Oct 02 2017 Vitaly Lipatov <lav@altlinux.ru> 0.1.0-alt1
- initial build for ALT Sisyphus

