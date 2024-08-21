%define pypi_name syrupy

%def_with check

Name:    python3-module-%pypi_name
Version: 4.6.4
Release: alt1

Summary: Pytest Snapshot Test Utility

License: Apache-2.0
Group:   Development/Python3
URL:     https://pypi.org/project/syrupy
VCS:     https://github.com/tophat/syrupy

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry

%if_with check
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
Syrupy is a pytest snapshot plugin. It enables developers
to write tests which assert immutability of computed results.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE *.md
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Aug 21 2024 Grigory Ustinov <grenka@altlinux.org> 4.6.4-alt1
- Automatically updated to 4.6.4.

* Tue Mar 26 2024 Grigory Ustinov <grenka@altlinux.org> 4.6.1-alt1
- Initial build for Sisyphus.
