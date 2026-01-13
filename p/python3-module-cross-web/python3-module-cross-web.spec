%define pypi_name cross-web
%define mod_name cross_web

%def_with check

Name:    python3-module-%pypi_name
Version: 0.4.1
Release: alt1

Summary: A universal web framework adapter for Python that lets you write code once and use it across multiple web frameworks
License: MIT
Group:   Development/Python3
URL:     https://github.com/usecross/cross-web

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-typing_extensions
BuildRequires: python3-module-fastapi
BuildRequires: python3-module-quart
BuildRequires: python3-module-httpx
BuildRequires: python3-module-chalice
BuildRequires: python3-module-django
BuildRequires: python3-module-aiohttp
BuildRequires: python3-module-aiohttp-tests
BuildRequires: python3-module-sanic
BuildRequires: python3-module-sanic-testing
BuildRequires: python3-module-python-multipart
BuildRequires: python3-module-django-dbbackend-sqlite3
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
Cross provides a unified interface for common web framework operations, allowing
you to write framework-agnostic code that can be easily adapted to work with
FastAPI, Flask, Django, and other popular Python web frameworks.

%prep
%setup -n %pypi_name-%version
sed -i 's/version = "0.4.0"/version = "0.4.1"/' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -k "not litestar"

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Jan 12 2026 Alexander Burmatov <thatman@altlinux.org> 0.4.1-alt1
- Initial build for Sisyphus.
