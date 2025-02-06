%define _unpackaged_files_terminate_build 1
%define pypi_name platform_utils

%def_with check

Name:    python3-module-%pypi_name
Version: 1.5.4
Release: alt1.1

Summary: Basic platform-agnostic utilities for paths, clipboard, and stdout management
License: MIT
Group:   Development/Python3
URL:     https://github.com/accessibleapps/platform_utils

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
%endif

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
%tox_create_default_config
%tox_check_pyproject

%files
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Feb 06 2025 Stanislav Levin <slev@altlinux.org> 1.5.4-alt1.1
- NMU: fixed FTBFS (tox 4).

* Tue Jan 21 2025 Artem Semenov <savoptik@altlinux.org> 1.5.4-alt1
- Initial build for Sisyphus
