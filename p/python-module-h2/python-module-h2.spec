%def_without check
%def_without python3

%define modulename h2
Name: python-module-h2
Version: 3.0.1
Release: alt1

Summary: HTTP/2 State-Machine based protocol implementation

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
This repository contains a pure-Python implementation of a HTTP/2 protocol
stack. It's written from the ground up to be embeddable in whatever program you
choose to use, ensuring that you can speak HTTP/2 regardless of your
programming paradigm.

%package -n python3-module-h2
Summary: HTTP/2 State-Machine based protocol implementation
Group: Development/Python3

%description -n python3-module-h2
This repository contains a pure-Python implementation of a HTTP/2 protocol
stack. It's written from the ground up to be embeddable in whatever program you
choose to use, ensuring that you can speak HTTP/2 regardless of your
programming paradigm.
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
%files -n python3-module-h2
%python3_sitelibdir/*
%endif


%changelog
* Thu Jun 15 2017 Vitaly Lipatov <lav@altlinux.ru> 3.0.1-alt1
- initial build for ALT Sisyphus

