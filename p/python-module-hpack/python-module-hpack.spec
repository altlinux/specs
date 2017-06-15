%def_without check
%def_with python3

%define modulename hpack
Name: python-module-hpack
Version: 3.0.0
Release: alt1

Summary: Pure-Python HPACK header compression

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
This module contains a pure-Python HTTP/2 header encoding (HPACK) logic for use
in Python programs that implement HTTP/2. It also contains a compatibility
layer that automatically enables the use of ``nghttp2`` if it's available.

%package -n python3-module-hpack
Summary: Pure-Python HPACK header compression
Group: Development/Python3

%description -n python3-module-hpack
This module contains a pure-Python HTTP/2 header encoding (HPACK) logic for use
in Python programs that implement HTTP/2. It also contains a compatibility
layer that automatically enables the use of ``nghttp2`` if it's available.
%prep
%setup
# hack encoding issue
echo > README.rst
echo > HISTORY.rst

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
%files -n python3-module-hpack
%python3_sitelibdir/*
%endif


%changelog
* Thu Jun 15 2017 Vitaly Lipatov <lav@altlinux.ru> 3.0.0-alt1
- initial build for ALT Sisyphus
