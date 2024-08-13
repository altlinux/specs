%define pypi_name strawberry-graphql
%define mod_name strawberry

%def_with check

Name:    python3-module-%pypi_name
Version: 0.237.3
Release: alt1

Summary: A GraphQL library for Python that leverages type annotations
License: MIT
Group:   Development/Python3
URL:     https://github.com/strawberry-graphql/strawberry

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-poetry

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-rich
BuildRequires: python3-module-typing_extensions
BuildRequires: python3-module-graphql-core
BuildRequires: python3-module-dateutil
BuildRequires: python3-module-pytest-emoji
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-pytest-mock
BuildRequires: python3-module-libcst
BuildRequires: python3-module-pytest-snapshot
BuildRequires: python3-module-pydantic
BuildRequires: python3-module-freezegun
BuildRequires: python3-module-inline-snapshot
BuildRequires: python3-module-litestar
BuildRequires: python3-module-pytest-codspeed
BuildRequires: python3-module-typer
BuildRequires: python3-module-starlette
BuildRequires: python3-module-asgiref
BuildRequires: python3-module-httpx
BuildRequires: python3-module-opentelemetry-api
BuildRequires: python3-module-opentelemetry-sdk
BuildRequires: python3-module-pyinstrument
BuildRequires: python3-module-python-multipart
BuildRequires: python3-module-channels
BuildRequires: python3-module-fastapi
BuildRequires: python3-module-django
BuildRequires: python3-module-uvicorn
BuildRequires: python3-module-aiohttp
BuildRequires: python3-module-email-validator
BuildRequires: python3-module-pytest-aiohttp
%endif

# Requires only for dev
%add_python3_req_skip ddtrace
# Optional dependency
%add_python3_req_skip starlite
%add_python3_req_skip starlite.exceptions
%add_python3_req_skip starlite.status_codes

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary.

%prep
%setup -n %pypi_name-%version
rm -fr strawberry/litestar
rm -fr tests/litestar

%build
%pyproject_build

%install
%pyproject_install

%check
export DJANGO_SETTINGS_MODULE=tests.django.django_settings
%pyproject_run_pytest --deselect=tests/websockets/test_graphql_transport_ws.py \
    --deselect=tests/schema/test_lazy/test_lazy_generic.py::test_lazy_types_loaded_from_same_module[script] \
    --deselect=tests/django/test_dataloaders.py \
    --deselect=tests/websockets/test_graphql_ws.py \
    --ignore=tests/cli/ \
    --ignore=tests/http/

%files
%doc *.md
%_bindir/%mod_name
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sat Aug 10 2024 Alexander Burmatov <thatman@altlinux.org> 0.237.3-alt1
- New version 0.237.3.

* Tue Jul 16 2024 Alexander Burmatov <thatman@altlinux.org> 0.235.2-alt1
- Initial build for Sisyphus.
