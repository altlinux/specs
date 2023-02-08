%define  oname pytest-trio

%def_with check

Name:    python3-module-%oname
Version: 0.8.0
Release: alt1

Summary: Pytest plugin for trio

License: MIT or Apache-2.0
Group:   Development/Python3
URL:     https://pypi.org/project/pytest-trio

# https://github.com/python-trio/pytest-trio
Source:  %name-%version.tar

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-trio
BuildRequires: python3-module-trio-tests
BuildRequires: python3-module-pytest-cov
%endif

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
%tox_create_default_config
%tox_check_pyproject

%files
%python3_sitelibdir/pytest_trio
%python3_sitelibdir/%{pyproject_distinfo pytest_trio}
%doc *.md

%changelog
* Wed Feb 08 2023 Grigory Ustinov <grenka@altlinux.org> 0.8.0-alt1
- Initial build for Sisyphus.
