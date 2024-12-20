%define pypi_name anysqlite

%def_with check

Name:    python3-module-%pypi_name
Version: 0.0.5
Release: alt1

Summary: sqlite3 for asyncio and trio
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/karpetrosyan/anysqlite

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-fancy-pypi-readme

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-modules-sqlite3
BuildRequires: python3-module-anyio
BuildRequires: python3-module-trio
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
Anysqlite provides an async/await interface to the standard sqlite3 library and
supports both trio and asyncio backends using the power of Anyio.

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
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Dec 19 2024 Alexander Burmatov <thatman@altlinux.org> 0.0.5-alt1
- Initial build for Sisyphus.
