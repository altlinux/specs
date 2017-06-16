%def_without check
%def_with python3

%define modulename vk_api
Name: python-module-vk_api
Version: 8.8
Release: alt1

Summary: Module for writing scripts for vk.com (vkontakte)

Url: https://github.com/python273/vk_api
License: Apache 2.0
Group: Development/Python


Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/python273/vk_api/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires: python-dev python-module-setuptools

BuildArch: noarch

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

#setup_python_module %modulename

%description
Module for writing scripts for vk.com (vkontakte).

%package -n python3-module-vk_api
Summary: Module for writing scripts for vk.com (vkontakte)
Group: Development/Python3

%description -n python3-module-vk_api
Module for writing scripts for vk.com (vkontakte).


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
%doc README.md examples/
%python_sitelibdir/*

%if_with python3
%files -n python3-module-vk_api
%doc README.md
%python3_sitelibdir/*
%endif


%changelog
* Fri Jun 16 2017 Vitaly Lipatov <lav@altlinux.ru> 8.8-alt1
- initial build for ALT Sisyphus

