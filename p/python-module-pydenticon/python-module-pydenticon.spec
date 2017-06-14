%def_without check
%def_with python3

%define modulename pydenticon
Name: python-module-pydenticon
Version: 0.3
Release: alt1

Summary: Library for generating identicons

Url: https://github.com/azaghal/pydenticon
License: BSD
Group: Development/Python


Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/azaghal/pydenticon/archive/%version.tar.gz
Source: %name-%version.tar

BuildRequires: python-dev python-module-setuptools

BuildArch: noarch

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

#setup_python_module %modulename

%description
Pydenticon is a small utility library that can be used for deterministically
enerating identicons based on the hash of provided data.


%package -n python3-module-pydenticon
Summary: Library for generating identicons
Group: Development/Python3

%description -n python3-module-pydenticon
Pydenticon is a small utility library that can be used for deterministically
enerating identicons based on the hash of provided data.


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
%doc README.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-pydenticon
%doc README.rst
%python3_sitelibdir/*
%endif


%changelog
* Wed Jun 14 2017 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- initial build for ALT Sisyphus

