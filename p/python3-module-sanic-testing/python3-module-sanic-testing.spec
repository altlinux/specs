%define pypi_name sanic-testing
%define mod_name sanic_testing

%def_with check

Name:    python3-module-%pypi_name
Version: 24.6.0
Release: alt1

Summary: Test clients for Sanic
License: MIT
Group:   Development/Python3
URL:     https://github.com/sanic-org/sanic-testing

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-sanic
BuildRequires: python3-module-html5tagger
BuildRequires: python3-module-tracerite
BuildRequires: python3-module-aiofiles
BuildRequires: python3-module-httpx
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-anyio
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
This package is meant to be the core testing utility and clients for testing
Sanic applications. It is mainly derived from sanic.testing which has (or will
be) removed from the main Sanic repository in the future.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%pyproject_run_pytest

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Jul 19 2024 Alexander Burmatov <thatman@altlinux.org> 24.6.0-alt1
- Initial build for Sisyphus.
