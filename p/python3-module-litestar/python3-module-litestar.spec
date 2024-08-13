%define pypi_name litestar

%ifarch i586
%def_without check
%else
%def_with check
%endif

Name:    python3-module-%pypi_name
Version: 2.9.1
Release: alt2

Summary: Production-ready, Light, Flexible and Extensible ASGI API framework | Effortlessly Build Performant APIs
License: MIT
Group:   Development/Python3
URL:     https://github.com/litestar-org/litestar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-lazy-fixtures
BuildRequires: python3-module-pytest-xdist
BuildRequires: python3-module-pytest-mock
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-pytest-rerunfailures
BuildRequires: python3-module-pytest-timeout
BuildRequires: python3-module-trio
BuildRequires: python3-module-pydantic
BuildRequires: python3-module-msgspec
BuildRequires: python3-module-multidict
BuildRequires: python3-module-yaml
BuildRequires: python3-module-anyio
BuildRequires: python3-module-redis-py
BuildRequires: python3-module-time-machine
BuildRequires: python3-module-httpx
BuildRequires: python3-module-picologging
BuildRequires: python3-module-asyncpg
BuildRequires: python3-module-psutil
BuildRequires: python3-module-jinja2
BuildRequires: python3-module-hypothesis
BuildRequires: python3-module-fsspec
BuildRequires: python3-module-mako
BuildRequires: python3-module-starlette
BuildRequires: python3-module-brotli
BuildRequires: python3-module-jose
BuildRequires: python3-module-structlog
BuildRequires: python3-module-polyfactory
BuildRequires: python3-module-email-validator
BuildRequires: python3-module-advanced-alchemy
BuildRequires: python3-module-minijinja
BuildRequires: python3-module-pydantic-extra-types
BuildRequires: python3-module-prometheus_client
BuildRequires: python3-module-httpx-sse
BuildRequires: python3-module-psycopg
BuildRequires: python3-module-opentelemetry-sdk
BuildRequires: python3-module-opentelemetry-instrumentation-asgi
BuildRequires: python3-module-beanie
BuildRequires: python3-module-sanic
BuildRequires: python3-module-aiosqlite
BuildRequires: python3-module-uvicorn
%endif

%add_python3_req_skip starlite
%add_python3_req_skip starlite.exceptions
%add_python3_req_skip starlite.status_codes

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
Litestar is a powerful, flexible yet opinionated ASGI framework, focused on
building APIs, and offers high-performance data validation and parsing,
dependency injection, first-class ORM integration, authorization primitives,
and much more that's needed to get applications up and running.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%pyproject_run_pytest --ignore=tests/examples/ \
    --ignore=tests/unit/test_contrib/ \
    --deselect=tests/unit/test_testing/test_test_client.py \
    --deselect=tests/unit/test_channels/test_plugin.py \
    --deselect=tests/unit/test_channels/test_backends.py \
    --deselect=tests/unit/test_stores.py \
    --deselect=tests/e2e/test_response_caching.py::test_with_stores \
    --deselect=tests/unit/test_utils/test_version.py::test_formatted \
    --deselect=tests/unit/test_template/test_template.py::test_media_type_inferred \
    --deselect=tests/unit/test_file_system.py::test_file_adapter_info

%files
%doc *.md
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Aug 09 2024 Alexander Burmatov <thatman@altlinux.org> 2.9.1-alt2
- Enable tests.

* Wed Jul 17 2024 Alexander Burmatov <thatman@altlinux.org> 2.9.1-alt1
- Initial build for Sisyphus.
