%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-check
%define mod_name pytest_check

%def_with check

Name: python3-module-%pypi_name
Version: 2.7.6
Release: alt1

Summary: A pytest plugin that allows multiple failures per test

License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytest-check/
Vcs: https://github.com/okken/pytest-check

BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-build
BuildRequires: python3-module-hatchling
%if_with check
BuildRequires: python3-module-tox
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
%pyproject_run_pytest

%files
%doc LICENSE.txt README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %mod_name}

%changelog
* Mon Mar 3 2026 Timofei Fedotov <sovtouch@altlinux.org> 2.7.6-alt1
- Updated to 2.7.6.

* Mon Nov 17 2025 Timofei Fedotov <sovtouch@altlinux.org> 2.6.0-alt1
- Updated to 2.6.0

* Tue Aug 25 2025 Timofei Fedotov <sovtouch@altlinux.org> 2.5.3-alt1
- Initial build for ALT Sisyphus.
