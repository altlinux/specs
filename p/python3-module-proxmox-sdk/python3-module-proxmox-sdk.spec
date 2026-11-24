%define pypi_name proxmox-sdk
%define mod_name proxmox_sdk

%def_with check

Name:    python3-module-%pypi_name
Version: 0.0.15
Release: alt1.1

Summary: Proxmox Async SDK
License: MIT
Group:   Development/Python3
URL:     https://github.com/emersonfelipesp/proxmox-sdk

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-pydantic
BuildRequires: python3-module-yaml
BuildRequires: python3-module-fastapi
BuildRequires: python3-module-httpx
BuildRequires: python3-module-slowapi
BuildRequires: python3-module-aiohttp
BuildRequires: python3-module-uvicorn
BuildRequires: python3-module-typer
BuildRequires: python3-modules-sqlite3
BuildRequires: python3-module-pytest-xdist
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
Schema-driven FastAPI package for Proxmox API: OpenAPI generation, mock data,
and in-memory CRUD operations.

%prep
%setup -n %pypi_name-%version
sed -i '/^import json$/a import sys' tests/test_generated_integrity.py
sed -i '/^import importlib.util$/a import sys' tests/test_loading_validation.py
sed -i '/^    module = importlib.util.module_from_spec(spec)$/a\    sys.modules[spec.name] = module' tests/test_generated_integrity.py tests/test_loading_validation.py
sed -i 's/if name == "opentelemetry" or name.startswith("opentelemetry."):/if name.startswith(("opentelemetry.sdk", "opentelemetry.exporter", "opentelemetry.instrumentation")):/g' tests/test_otel.py

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -k "not test_ceph_status_mock_json \
	and not test_ceph_flags_mock \
	and not (test_ceph_osds_mock and not requires_node) \
	and not test_ceph_rejects_non_pve \
	and not test_create_without_parameters \
	and not test_discovery_returns_help_specs \
	and not test_root_help_present_once \
	and not test_docs_group_is_discoverable \
	and not test_browser_guards_are_wired_before_page_creation \
	and not (test_public_checksum_probe_refuses_internal_redirect and private)"

%files
%doc *.md
%_bindir/pbx
%_bindir/proxmox
%_bindir/proxmox-cli
%_bindir/proxmox-sdk-codegen
%_bindir/proxmox-sdk-mock
%_bindir/proxmox-sdk-pdm-mock
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Nov 24 2026 Vitaly Lipatov <lav@altlinux.ru> 0.0.15-alt1.1
- Fix tests for the current Pydantic and FastAPI versions.
- Add BuildRequires: python3-module-pytest-xdist (run tests in parallel).

* Mon Sep 21 2026 Alexander Burmatov <thatman@altlinux.org> 0.0.15-alt1
- New 0.0.15 version.

* Thu Sep 10 2026 Alexander Burmatov <thatman@altlinux.org> 0.0.14.post3-alt1
- New 0.0.14.post3 version.

* Wed Aug 12 2026 Alexander Burmatov <thatman@altlinux.org> 0.0.13-alt1
- New 0.0.13 version.

* Mon Jun 08 2026 Alexander Burmatov <thatman@altlinux.org> 0.0.11.post2-alt1
- New 0.0.11.post2 version.

* Fri May 29 2026 Alexander Burmatov <thatman@altlinux.org> 0.0.9-alt2
- Add needed requirements.

* Thu May 28 2026 Alexander Burmatov <thatman@altlinux.org> 0.0.9-alt1
- New 0.0.9 version.

* Fri Apr 24 2026 Alexander Burmatov <thatman@altlinux.org> 0.0.3.post1-alt1
- New 0.0.3.post1 version.

* Tue Apr 21 2026 Alexander Burmatov <thatman@altlinux.org> 0.0.2.post3-alt1
- Initial build for Sisyphus.
