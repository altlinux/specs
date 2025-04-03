%define pypi_name certipy

%def_without check

Name:    python3-module-%pypi_name
Version: 0.2.1
Release: alt1

Summary: Wraps pyOpenSSL for quick and easy PKI
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/LLNL/certipy

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
%_bindir/certipy
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Jan 29 2025 Andrey Cherepanov <cas@altlinux.org> 0.2.1-alt1
- Initial build for Sisyphus.
