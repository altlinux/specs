%def_without check
%def_with python3

%define modulename unpaddedbase64
Name: python-module-unpaddedbase64
Version: 1.1.0
Release: alt1

Summary: Encode and decode Base64 without "=" padding

Url: https://github.com/matrix-org/python-unpaddedbase64
License: ASL 2.0
Group: Development/Python


Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/matrix-org/python-unpaddedbase64/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires: python-dev python-module-setuptools

BuildArch: noarch

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

#setup_python_module %modulename

%description
RFC 4648 specifies that Base64 should be padded to a multiple of 4 bytes
using "=" characters. However this conveys no benefit so many protocols
choose to use Base64 without the "=" padding.


%package -n python3-module-unpaddedbase64
Summary: Encode and decode Base64 without "=" padding
Group: Development/Python3

%description -n python3-module-unpaddedbase64
RFC 4648 specifies that Base64 should be padded to a multiple of 4 bytes
using "=" characters. However this conveys no benefit so many protocols
choose to use Base64 without the "=" padding.


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
%files -n python3-module-unpaddedbase64
%doc README.rst
%python3_sitelibdir/*
%endif


%changelog
* Wed Jun 14 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- initial build for ALT Sisyphus

