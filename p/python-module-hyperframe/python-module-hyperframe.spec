%def_without check
%def_with python3

%define modulename hyperframe
Name: python-module-hyperframe
Version: 5.1.0
Release: alt1

Summary: HTTP/2 framing layer for Python

Url: http://hyper.rtfd.org
License: MIT
Group: Development/Python


Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://pypi.io/packages/source/h/%modulename/%modulename-%version.tar.gz
Source: %name-%version.tar

BuildRequires: python-dev python-module-setuptools

BuildArch: noarch

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

#setup_python_module %modulename

%description
This library contains the HTTP/2 framing code used in the `hyper`_ project. It
provides a pure-Python codebase that is capable of decoding a binary stream
into HTTP/2 frames.

This library is used directly by `hyper`_ and a number of other projects to
provide HTTP/2 frame decoding logic.

%package -n python3-module-hyperframe
Summary: HTTP/2 framing layer for Python
Group: Development/Python3

%description -n python3-module-hyperframe
This library contains the HTTP/2 framing code used in the `hyper`_ project. It
provides a pure-Python codebase that is capable of decoding a binary stream
into HTTP/2 frames.

This library is used directly by `hyper`_ and a number of other projects to
provide HTTP/2 frame decoding logic.

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
%files -n python3-module-hyperframe
%python3_sitelibdir/*
%endif


%changelog
* Thu Jun 15 2017 Vitaly Lipatov <lav@altlinux.ru> 5.1.0-alt1
- initial build for ALT Sisyphus
