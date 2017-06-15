%def_without check
%def_without python3

%define modulename pydoctor
Name: python-module-pydoctor
Version: 16.3.0
Release: alt1

Summary: API doc generator

Url: http://github.com/twisted/pydoctor
License: X11
Group: Development/Python


Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://pypi.io/packages/source/p/%modulename/%modulename-%version.tar.gz
Source: %name-%version.tar

BuildRequires: python-dev python-module-setuptools

BuildArch: noarch

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

#setup_python_module %modulename

%description
This is 'pydoctor', an API documentation generator that works by
static analysis.


%package -n python3-module-pydoctor
Summary: API doc generator
Group: Development/Python3

%description -n python3-module-pydoctor
This is 'pydoctor', an API documentation generator that works by
static analysis.
an emphasis on correctness.


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
%_bindir/pydoctor
%python_sitelibdir/*

%if_with python3
%files -n python3-module-pydoctor
%python3_sitelibdir/*
%endif


%changelog
* Thu Jun 15 2017 Vitaly Lipatov <lav@altlinux.ru> 16.3.0-alt1
- initial build for ALT Sisyphus

