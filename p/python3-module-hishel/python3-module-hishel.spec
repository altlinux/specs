%define pypi_name hishel

%def_with check

Name:    python3-module-%pypi_name
Version: 0.1.1
Release: alt1

Summary: An elegant HTTP Cache implementation for HTTPX and HTTP Core
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/karpetrosyan/hishel

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-fancy-pypi-readme

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-httpcore
BuildRequires: python3-module-httpx
BuildRequires: python3-module-anyio
BuildRequires: python3-modules-sqlite3
BuildRequires: python3-module-anysqlite
BuildRequires: python3-module-pyaml
BuildRequires: python3-module-trio
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
Hishel is a library that implements HTTP Caching for HTTPX and HTTP Core
libraries in accordance with RFC 9111, the most recent caching specification.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest --ignore tests/_async/test_storages.py --ignore tests/_sync/test_storages.py

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Dec 19 2024 Alexander Burmatov <thatman@altlinux.org> 0.1.1-alt1
- Initial build for Sisyphus.
