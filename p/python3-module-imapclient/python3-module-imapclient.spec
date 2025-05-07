%define pypi_name imapclient

%def_without check

Name:    python3-module-%pypi_name
Version: 3.0.1
Release: alt1.1

Summary: An easy-to-use, Pythonic and complete IMAP client library
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/mjs/imapclient

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
%doc *.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 3.0.1-alt1.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Sun Dec 03 2023 Andrey Cherepanov <cas@altlinux.org> 3.0.1-alt1
- New version.

* Sun Oct 29 2023 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt1
- New version.

* Tue Sep 19 2023 Andrey Cherepanov <cas@altlinux.org> 2.3.1-alt1
- Initial build for Sisyphus.
