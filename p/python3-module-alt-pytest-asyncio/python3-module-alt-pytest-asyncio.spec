%define pypi_name alt-pytest-asyncio
%define mod_name alt_pytest_asyncio

%def_with check

Name:    python3-module-%pypi_name
Version: 0.8.2
Release: alt1

Summary: An alternative plugin for pytest to make it support async tests and fixtures
License: MIT
Group:   Development/Python3
URL:     https://github.com/delfick/alt-pytest-asyncio

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-order
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
export PYTHONPATH=$PWD/helpers
%pyproject_run_pytest

%files
%doc *.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Oct 14 2024 Alexander Burmatov <thatman@altlinux.org> 0.8.2-alt1
- Initial build for Sisyphus.
