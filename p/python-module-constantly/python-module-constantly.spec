%def_without check
%def_without python3

%define modulename constantly
Name: python-module-constantly
Version: 15.1.0
Release: alt1

Summary: Symbolic constants in Python

Url: http://github.com/twisted/constantly
License: X11
Group: Development/Python


Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://pypi.io/packages/source/c/%modulename/%modulename-%version.tar.gz
Source: %name-%version.tar

BuildRequires: python-dev python-module-setuptools

BuildArch: noarch

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

#setup_python_module %modulename

%description
A library that provides symbolic constant support.
It includes collections and constants with text, numeric, and bit flag values.
Originally ``twisted.python.constants`` from the `Twisted <https://twistedmatrix.com/>`_ project.


%package -n python3-module-constantly
Summary: Symbolic constants in Python
Group: Development/Python3

%description -n python3-module-constantly
A library that provides symbolic constant support.
It includes collections and constants with text, numeric, and bit flag values.
Originally ``twisted.python.constants`` from the `Twisted <https://twistedmatrix.com/>`_ project.


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
%files -n python3-module-constantly
%python3_sitelibdir/*
%endif


%changelog
* Thu Jun 15 2017 Vitaly Lipatov <lav@altlinux.ru> 15.1.0-alt1
- initial build for ALT Sisyphus

