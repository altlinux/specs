%define pypi_name strict-rfc3339
%define mod_name strict_rfc3339

%def_with check

Name: python3-module-%pypi_name
Version: 0.7
Release: alt1

Summary: Strict, simple, lightweight RFC3339 functions
License: GPL-3.0
Group: Development/Python3
URL: https://github.com/danielrichman/strict-rfc3339
BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
%endif

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -k 'not test_leap_year and not test_y2038'

%files
%doc README.*
%python3_sitelibdir/__pycache__
%python3_sitelibdir/%mod_name.py
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Jun 19 2023 Anton Vyatkin <toni@altlinux.org> 0.7-alt1
- Initial build for Sisyphus
