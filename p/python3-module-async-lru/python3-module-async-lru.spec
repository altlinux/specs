%define pypi_name async-lru
%define mname async_lru

%def_without check

Name:    python3-module-%pypi_name
Version: 2.0.2
Release: alt1

Summary: Simple LRU cache for asyncio
License: MIT
Group:   Development/Python3
URL:     https://github.com/aio-libs/async-lru

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
#%%tox_create_default_config
%tox_check_pyproject

%files
%doc README.rst
%python3_sitelibdir/%mname/
%python3_sitelibdir/%{pyproject_distinfo %mname}

%changelog
* Mon Apr 03 2023 Andrey Cherepanov <cas@altlinux.org> 2.0.2-alt1
- Initial build for Sisyphus
