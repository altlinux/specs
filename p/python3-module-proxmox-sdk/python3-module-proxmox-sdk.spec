%define pypi_name proxmox-sdk
%define mod_name proxmox_sdk

%def_with check

Name:    python3-module-%pypi_name
Version: 0.0.9
Release: alt2

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
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
Schema-driven FastAPI package for Proxmox API: OpenAPI generation, mock data,
and in-memory CRUD operations.

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
%_bindir/pbx
%_bindir/proxmox
%_bindir/proxmox-cli
%_bindir/proxmox-sdk-codegen
%_bindir/proxmox-sdk-mock
%_bindir/proxmox-sdk-pdm-mock
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri May 29 2026 Alexander Burmatov <thatman@altlinux.org> 0.0.9-alt2
- Add needed requirements.

* Thu May 28 2026 Alexander Burmatov <thatman@altlinux.org> 0.0.9-alt1
- New 0.0.9 version.

* Fri Apr 24 2026 Alexander Burmatov <thatman@altlinux.org> 0.0.3.post1-alt1
- New 0.0.3.post1 version.

* Tue Apr 21 2026 Alexander Burmatov <thatman@altlinux.org> 0.0.2.post3-alt1
- Initial build for Sisyphus.
