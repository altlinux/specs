%def_without check
%def_with python3

%define modulename matrix-angular-sdk
Name: python-module-matrix-angular-sdk
Version: 0.6.8
Release: alt1

Summary: Matrix Angular Sdk

Url: https://pypi.python.org/pypi/matrix-angular-sdk
License: Apache 2.0
Group: Development/Python


Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://pypi.io/packages/source/m/%modulename/%modulename-%version.tar.gz
Source: %name-%version.tar

BuildRequires: python-dev python-module-setuptools

BuildArch: noarch

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

#setup_python_module %modulename

%description
This project provides AngularJS services for implementing the Client-Server API on Matrix:
an open standard for interoperable Instant Messaging and VoIP.

%package -n python3-module-matrix-angular-sdk
Summary: A featureful, correct URL for Python
Group: Development/Python3

%description -n python3-module-matrix-angular-sdk
This project provides AngularJS services for implementing the Client-Server API on Matrix:
an open standard for interoperable Instant Messaging and VoIP.

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
%files -n python3-module-matrix-angular-sdk
%python3_sitelibdir/*
%endif


%changelog
* Thu Jun 15 2017 Vitaly Lipatov <lav@altlinux.ru> 0.6.8-alt1
- initial build for ALT Sisyphus

