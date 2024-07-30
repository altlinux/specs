%define pypi_name pytest-codspeed
%define mod_name pytest_codspeed

%def_with check

Name:    python3-module-%pypi_name
Version: 2.2.1
Release: alt1

Summary: Pytest plugin to create CodSpeed benchmarks
License: MIT
Group:   Development/Python3
URL:     https://github.com/CodSpeedHQ/pytest-codspeed

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-cffi
BuildRequires: python3-module-filelock
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Jul 19 2024 Alexander Burmatov <thatman@altlinux.org> 2.2.1-alt1
- Initial build for Sisyphus.
