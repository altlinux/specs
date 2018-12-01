%def_without check
%def_with python3

%define modulename lzf
Name: python-module-lzf
Version: 0.2.4
Release: alt1

Summary: liblzf python bindings

Url: https://github.com/matrix-org/python-canonicaljson
License: the liblzf bsd 2-clause and gpl, and own bsd 3-clause
Group: Development/Python


Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/teepark/python-lzf/archive/release-%version.tar.gz
Source: %name-%version.tar

BuildRequires: python-dev python-module-setuptools

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

#setup_python_module %modulename

BuildRequires: liblzf-devel

%description
This package is just a straight translation of the C api of liblzf to python.
It has two functions: compress() and decompress().

%package -n python3-module-lzf
Summary: liblzf python bindings
Group: Development/Python3

%description -n python3-module-lzf
This package is just a straight translation of the C api of liblzf to python.
It has two functions: compress() and decompress().

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
%doc README.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-lzf
%doc README.txt
%python3_sitelibdir/*
%endif


%changelog
* Sat Dec 01 2018 Vitaly Lipatov <lav@altlinux.ru> 0.2.4-alt1
- initial build for ALT Sisyphus

