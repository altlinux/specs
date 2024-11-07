%define pypi_name aiohttp_retry

%def_without check

Name:    python3-module-aiohttp-retry
Version: 2.9.1
Release: alt1

Summary: Simple retry client for aiohttp
License: MIT
Group:   Development/Python3
URL:     https://github.com/inyutin/aiohttp_retry

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary

%prep
%setup -n %pypi_name-%version
sed -i 's/version=".*/version="%version",/' setup.py

%build
%pyproject_build

%install
%pyproject_install

%check
#%%tox_create_default_config
%tox_check_pyproject

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Nov 07 2024 Andrey Cherepanov <cas@altlinux.org> 2.9.1-alt1
- New version.

* Sun Oct 27 2024 Andrey Cherepanov <cas@altlinux.org> 2.9.0-alt1
- New version.

* Mon Jul 22 2024 Andrey Cherepanov <cas@altlinux.org> 2.8.3-alt1
- Initial build for Sisyphus.
