%define  oname pytest-trio

%def_with check

Name:    python3-module-%oname
Version: 0.8.0
Release: alt2.1

Summary: Pytest plugin for trio

License: MIT or Apache-2.0
Group:   Development/Python3
URL:     https://pypi.org/project/pytest-trio

# https://github.com/python-trio/pytest-trio
Source:  %name-%version.tar
# trio >= 0.22.1
Patch0: pytest-trio-0.8.0-Remove-trio.tests-import-causing-warnings.patch

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-trio
BuildRequires: python3-module-trio-tests
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-hypothesis
%endif

BuildArch: noarch

%description
%summary

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%python3_sitelibdir/pytest_trio
%python3_sitelibdir/%{pyproject_distinfo pytest_trio}
%doc *.md

%changelog
* Wed Nov 08 2023 Stanislav Levin <slev@altlinux.org> 0.8.0-alt2.1
- NMU: fixed FTBFS (trio 0.22.1).

* Tue Sep 12 2023 Grigory Ustinov <grenka@altlinux.org> 0.8.0-alt2
- Fixed FTBFS.

* Wed Feb 08 2023 Grigory Ustinov <grenka@altlinux.org> 0.8.0-alt1
- Initial build for Sisyphus.
