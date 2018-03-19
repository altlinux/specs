%define modulename vk_api

Name: python-module-vk_api
Version: 9.3.1
Release: alt1

Summary: Module for writing scripts for vk.com (vkontakte)
License: Apache 2.0
Group: Development/Python

Url: https://github.com/python273/vk_api
Packager: Andrey Bychkov <mrdrew@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar

BuildRequires: python-dev
BuildRequires: python-module-setuptools

%py_requires requests enum34 urllib3

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
BuildPreReq: python3-module-setuptools

%description
Module for writing scripts for vk.com (vkontakte).

%package -n python3-module-vk_api
Summary: Module for writing scripts for vk.com (vkontakte)
Group: Development/Python3
%py3_requires enum34

%description -n python3-module-vk_api
Module for writing scripts for vk.com (vkontakte).

%prep
%setup

cp -fR . ../python3

%build
%python_build_debug

pushd ../python3
%python3_build_debug
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%files
%doc README.md examples/


%files -n python3-module-vk_api
%doc README.md
%python3_sitelibdir/*


%changelog
* Mon Mar 19 2018 Andrey Bychkov <mrdrew@altlinux.ru> 9.3.1-alt1
- Version 9.3.1

* Fri Jun 16 2017 Vitaly Lipatov <lav@altlinux.ru> 8.8-alt1
- initial build for ALT Sisyphus

