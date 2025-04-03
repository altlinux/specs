%define pypi_name pamela

%def_without check

Name:    python3-module-%pypi_name
Version: 1.2.0
Release: alt1

Summary: Python PAM interface
License: MIT
Group:   Development/Python3
URL:     https://github.com/jupyterhub/pamela

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
%doc *.md
%python3_sitelibdir/*

%changelog
* Wed Jan 29 2025 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus.
