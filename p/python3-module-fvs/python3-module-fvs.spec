%define pypi_name FVS

%def_without check

Name:    python3-module-fvs
Version: 0.3.4
Release: alt1

Summary: File Versioning System with hash comparison, deduplication and data storage to create unlinked states that can be deleted
License: MIT
Group:   Development/Python3
URL:     https://github.com/mirkobrombin/FVS

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
%doc README.md
%_bindir/fvs
%python3_sitelibdir/fvs
%python3_sitelibdir/FVS-*.dist-info

%changelog
* Wed Sep 13 2023 Andrey Cherepanov <cas@altlinux.org> 0.3.4-alt1
- Initial build for Sisyphus.
