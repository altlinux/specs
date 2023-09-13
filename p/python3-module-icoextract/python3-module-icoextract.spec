%define pypi_name icoextract

%def_without check

Name:    python3-module-%pypi_name
Version: 0.1.4
Release: alt1

Summary: Extract icons from Windows PE files (.exe/.dll)
License: MIT
Group:   Development/Python3
URL:     https://github.com/jlu5/icoextract

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
%_bindir/*
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Sep 13 2023 Andrey Cherepanov <cas@altlinux.org> 0.1.4-alt1
- Initial build for Sisyphus.
