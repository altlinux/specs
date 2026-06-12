%define pypi_name RecoverPy

%def_without check

Name:    python3-module-%pypi_name
Version: 2.3.0
Release: alt1

Summary: Interactively find and recover deleted or overwritten files from your terminal
License: GPL-3.0
Group:   Development/Python3
URL:     https://pypi.org/project/recoverpy/
Vcs:     https://github.com/PabloLec/RecoverPy

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-hatchling
Requires: progress

BuildArch: noarch

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
#%%tox_create_default_config
%tox_check_pyproject

%files
%doc CONTRIBUTING.* LICENSE README.*
%_bindir/recoverpy
%python3_sitelibdir/recoverpy/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Jun 12 2026 Sergey Palcheh <minergenon@altlinux.org> 2.3.0-alt1
- new version 2.3.0
- delete patch python3-module-RecoverPy-2.2.0-alt1-screen-params_fixes.patch

* Thu Jan 30 2025 Sergey Palcheh <minergenon@altlinux.org> 2.2.0-alt1
- Initial build for Sisyphus

