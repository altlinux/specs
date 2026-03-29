%define _unpackaged_files_terminate_build 1
%define pypi_name detect-test-pollution
%define mod_name detect_test_pollution

%def_with check

Name: python3-module-%pypi_name
Version: 1.2.0
Release: alt1.1
Summary: A tool to detect test pollution
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/detect-test-pollution
Vcs: https://github.com/asottile/detect-test-pollution
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-covdefaults
BuildRequires: python3-module-coverage
BuildRequires: python3-module-pytest
%endif

%description
%summary.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra tests

%files
%doc README.*
%_bindir/detect-test-pollution
%python3_sitelibdir/%mod_name.py
%python3_sitelibdir/__pycache__/%mod_name.*.pyc
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 1.2.0-alt1.1
- Demodernized packaging.

* Sat Apr 27 2024 Stanislav Levin <slev@altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus.
