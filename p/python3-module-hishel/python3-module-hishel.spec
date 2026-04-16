%define pypi_name hishel

%def_with check

Name:    python3-module-%pypi_name
Version: 1.1.9
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
BuildRequires: python3-module-httpx
BuildRequires: python3-module-anyio
BuildRequires: python3-module-anysqlite
BuildRequires: python3-module-inline-snapshot
BuildRequires: python3-module-time-machine
BuildRequires: python3-module-requests
BuildRequires: python3-module-msgpack
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
%pyproject_run_pytest -k "not (test_simple_caching or test_encoded_content_caching)"

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Apr 15 2026 Alexander Burmatov <thatman@altlinux.org> 1.1.9-alt1
- New 1.1.9 version.

* Thu Dec 19 2024 Alexander Burmatov <thatman@altlinux.org> 0.1.1-alt1
- Initial build for Sisyphus.
