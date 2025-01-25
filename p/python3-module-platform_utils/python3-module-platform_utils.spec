%define _unpackaged_files_terminate_build 1
%define pypi_name platform_utils

Name:    python3-module-%pypi_name
Version: 1.5.4
Release: alt1

Summary: Basic platform-agnostic utilities for paths, clipboard, and stdout management
License: MIT
Group:   Development/Python3
URL:     https://github.com/accessibleapps/platform_utils

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
%tox_create_default_config
%tox_check_pyproject

%files
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Jan 21 2025 Artem Semenov <savoptik@altlinux.org> 1.5.4-alt1
- Initial build for Sisyphus
