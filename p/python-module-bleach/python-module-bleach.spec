%def_without check
%def_with python3

%define modulename bleach
Name: python-module-bleach
Version: 2.0
Release: alt1

Summary: An easy whitelist-based HTML-sanitizing tool

Url: http://github.com/jsocol/bleach
License: ASL 2.0
Group: Development/Python


Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/mozilla/bleach/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires: python-dev python-module-setuptools

BuildArch: noarch

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

#setup_python_module %modulename

%description
Bleach is an HTML sanitizing library that escapes or strips markup and
attributes based on a white list.


%package -n python3-module-bleach
Summary: An easy whitelist-based HTML-sanitizing tool
Group: Development/Python3

%description -n python3-module-bleach
Bleach is an HTML sanitizing library that escapes or strips markup and
attributes based on a white list.


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
%files -n python3-module-bleach
%doc README.rst
%python3_sitelibdir/*
%endif


%changelog
* Wed Jun 14 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt1
- initial build for ALT Sisyphus

