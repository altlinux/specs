%define pypi_name strawberry-graphql
%define mod_name strawberry

%def_with check

Name:    python3-module-%pypi_name
Version: 0.320.0
Release: alt1

Summary: A GraphQL library for Python that leverages type annotations
License: MIT
Group:   Development/Python3
URL:     https://github.com/strawberry-graphql/strawberry

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-uv-build

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
BuildRequires: python3-module-multipart
BuildRequires: python3-module-channels
BuildRequires: python3-module-fastapi
BuildRequires: python3-module-django
BuildRequires: python3-module-uvicorn
BuildRequires: python3-module-aiohttp
BuildRequires: python3-module-email-validator
BuildRequires: python3-module-pytest-aiohttp
BuildRequires: python3-module-aiofiles
BuildRequires: python3-module-sanic-testing
BuildRequires: python3-module-websockets
BuildRequires: python3-module-lia-web
BuildRequires: python3-module-cross-web
BuildRequires: python3-module-protobuf
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
sed -i 's/version = "0.319.0"/version = "%version"/' pyproject.toml
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
    --deselect=tests/experimental/pydantic/test_fields.py \
    --deselect=tests/schema/test_lazy/test_lazy_generic.py::test_lazy_types_loaded_from_same_module[cli] \
    --ignore=tests/cli/ \
    --ignore=tests/http/

%files
%doc *.md
%_bindir/%mod_name
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Jul 01 2026 Alexander Burmatov <thatman@altlinux.org> 0.320.0-alt1
- New version 0.320.0.

* Wed May 27 2026 Alexander Burmatov <thatman@altlinux.org> 0.316.0-alt1
- New version 0.316.0.

* Tue May 05 2026 Alexander Burmatov <thatman@altlinux.org> 0.315.3-alt1
- New version 0.315.3.

* Tue Apr 28 2026 Alexander Burmatov <thatman@altlinux.org> 0.315.2-alt1
- New version 0.315.2.

* Mon Apr 13 2026 Alexander Burmatov <thatman@altlinux.org> 0.314.3-alt1
- New version 0.314.3.

* Wed Mar 18 2026 Alexander Burmatov <thatman@altlinux.org> 0.311.3-alt1
- New version 0.311.3.

* Wed Mar 04 2026 Alexander Burmatov <thatman@altlinux.org> 0.308.3-alt1
- New version 0.308.3.

* Wed Feb 18 2026 Alexander Burmatov <thatman@altlinux.org> 0.296.1-alt1
- New version 0.296.1.

* Wed Feb 04 2026 Alexander Burmatov <thatman@altlinux.org> 0.291.0-alt1
- New version 0.291.0.

* Wed Jan 21 2026 Alexander Burmatov <thatman@altlinux.org> 0.289.2-alt1
- New version 0.289.2.

* Mon Jan 12 2026 Alexander Burmatov <thatman@altlinux.org> 0.288.4-alt1
- New version 0.288.4.

* Wed Dec 24 2025 Alexander Burmatov <thatman@altlinux.org> 0.287.3-alt1
- New version 0.287.3.

* Wed Dec 10 2025 Alexander Burmatov <thatman@altlinux.org> 0.287.2-alt1
- New version 0.287.2.

* Wed Nov 26 2025 Alexander Burmatov <thatman@altlinux.org> 0.287.0-alt1
- New version 0.287.0.

* Wed Nov 12 2025 Alexander Burmatov <thatman@altlinux.org> 0.285.0-alt1
- New version 0.285.0.

* Thu Oct 30 2025 Alexander Burmatov <thatman@altlinux.org> 0.284.1-alt1
- New version 0.284.1.

* Wed Oct 15 2025 Alexander Burmatov <thatman@altlinux.org> 0.283.3-alt1
- New version 0.283.3.

* Mon Sep 22 2025 Alexander Burmatov <thatman@altlinux.org> 0.282.0-alt1
- New version 0.282.0.

* Wed Aug 27 2025 Alexander Burmatov <thatman@altlinux.org> 0.281.0-alt1
- New version 0.281.0.

* Wed Aug 13 2025 Alexander Burmatov <thatman@altlinux.org> 0.278.1-alt1
- New version 0.278.1.

* Mon Jul 28 2025 Alexander Burmatov <thatman@altlinux.org> 0.278.0-alt1
- New version 0.278.0.

* Mon Jun 30 2025 Alexander Burmatov <thatman@altlinux.org> 0.275.5-alt1
- New version 0.275.5.

* Fri Jun 06 2025 Alexander Burmatov <thatman@altlinux.org> 0.271.0-alt1
- New version 0.271.0.

* Wed May 28 2025 Alexander Burmatov <thatman@altlinux.org> 0.270.2-alt1
- New version 0.270.2.

* Wed May 28 2025 Alexander Burmatov <thatman@altlinux.org> 0.268.1-alt1
- New version 0.268.1.

* Sat Apr 26 2025 Alexander Burmatov <thatman@altlinux.org> 0.266.0-alt1
- New version 0.266.0.

* Wed Apr 16 2025 Alexander Burmatov <thatman@altlinux.org> 0.265.0-alt1
- New version 0.265.0.

* Fri Mar 14 2025 Alexander Burmatov <thatman@altlinux.org> 0.262.5-alt1
- New version 0.262.5.

* Thu Jan 30 2025 Alexander Burmatov <thatman@altlinux.org> 0.258.0-alt1
- New version 0.258.0.

* Thu Dec 19 2024 Alexander Burmatov <thatman@altlinux.org> 0.254.0-alt1
- New version 0.254.0.

* Mon Nov 11 2024 Alexander Burmatov <thatman@altlinux.org> 0.248.1-alt1
- New version 0.248.1.

* Sat Aug 10 2024 Alexander Burmatov <thatman@altlinux.org> 0.237.3-alt1
- New version 0.237.3.

* Tue Jul 16 2024 Alexander Burmatov <thatman@altlinux.org> 0.235.2-alt1
- Initial build for Sisyphus.
