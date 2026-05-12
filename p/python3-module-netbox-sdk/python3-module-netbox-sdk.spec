%define pypi_name netbox-sdk
%define mod_name netbox_sdk

%def_with check

Name:    python3-module-%pypi_name
Version: 0.0.8.post1
Release: alt1

Summary: Modern NetBox toolkit with an SDK, CLI and TUI (terminal UI) for faster automation
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/emersonfelipesp/netbox-sdk

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-pytest-timeout
BuildRequires: python3-module-pytest-xdist
BuildRequires: python3-module-aiohttp
BuildRequires: python3-module-pydantic
BuildRequires: python3-module-email-validator
BuildRequires: python3-module-rich
BuildRequires: python3-module-pyyaml
BuildRequires: python3-module-typer
BuildRequires: python3-module-textual
BuildRequires: python3-module-fastapi
BuildRequires: python3-module-httpx
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
netbox-sdk is a modern SDK-first NetBox integration toolkit. It provides
a standalone async REST API client for NetBox with Pydantic-based data
models, schema-driven operation discovery via OpenAPI, HTTP caching,
multi-profile configuration, and structured JSON logging.

%package -n %name-cli
Summary: CLI for NetBox based on netbox-sdk
Group:   Development/Python3
Requires: python3-module-%pypi_name = %EVR

%description -n %name-cli
Typer-based command-line interface for NetBox built on top of netbox-sdk.
Provides the nbx command with dynamic resource routing:
nbx <group> <resource> <action> [options]

%package -n %name-tui
Summary: Terminal UI for NetBox based on netbox-sdk
Group:   Development/Python3
Requires: python3-module-%pypi_name = %EVR

%description -n %name-tui
Textual-based terminal user interface for NetBox built on top of netbox-sdk.
Includes interactive resource browser, GraphQL explorer, log viewer,
Django model browser and developer tools TUI.

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
%python3_sitelibdir/%mod_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%files -n %name-cli
%_bindir/nbx
%_bindir/nbx-mock
%python3_sitelibdir/netbox_cli

%files -n %name-tui
%python3_sitelibdir/netbox_tui

%changelog
* Fri May 08 2026 Alexander Burmatov <thatman@altlinux.org> 0.0.8.post1-alt1
- New 0.0.8.post1 version.

* Fri Apr 24 2026 Alexander Burmatov <thatman@altlinux.org> 0.0.7.post6-alt1
- New 0.0.7.post6 version.

* Mon Apr 20 2026 Alexander Burmatov <thatman@altlinux.org> 0.0.7-alt1
- Initial build for Sisyphus.
