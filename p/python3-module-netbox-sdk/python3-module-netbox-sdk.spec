%define pypi_name netbox-sdk
%define mod_name netbox_sdk

%def_with check

Name:    python3-module-%pypi_name
Version: 0.0.11
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
BuildRequires: python3-module-click
BuildRequires: python3-module-jsonschema
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
rm -rf %buildroot%python3_sitelibdir/netbox_mcp
rm -f %buildroot%_bindir/nbx-mcp

%check
%pyproject_run_pytest -k "not ( \
	TestDevHttpInputValidation or \
	test_parse_select_requires_value or \
	test_parse_columns_requires_value or \
	test_parse_max_columns_requires_value or \
	test_parse_max_columns_invalid or \
	test_parse_max_columns_zero_raises or \
	test_main_handles_unknown_command_without_traceback or \
	test_metadata_generation_rejects_source_version_mismatch or \
	test_metadata_generation_rejects_materially_different_same_version_ancestor or \
	test_release_commit_must_already_be_on_canonical_main or \
	test_immutable_tag_requires_exact_annotated_object_and_commit or \
	test_built_wheel_exposes_the_catalog_outside_the_checkout or \
	test_v46_typed_regeneration_matches_committed_artifact or \
	test_v47_typed_regeneration_matches_committed_artifact)" \
    --ignore=tests/test_gitea_release.py \
    --ignore=tests/test_mcp.py \
    --ignore=tests/test_mcp_connected_line.py \
    --ignore=tests/test_mcp_plugin_bridge.py

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
* Fri Aug 28 2026 Alexander Burmatov <thatman@altlinux.org> 0.0.11-alt1
- New 0.0.11 version.

* Wed Aug 12 2026 Alexander Burmatov <thatman@altlinux.org> 0.0.10-alt1
- New 0.0.10 version.

* Tue Jun 09 2026 Alexander Burmatov <thatman@altlinux.org> 0.0.9.post2-alt1
- New 0.0.9.post2 version.

* Mon Jun 08 2026 Alexander Burmatov <thatman@altlinux.org> 0.0.9.post1-alt1
- New 0.0.9.post1 version.

* Thu May 28 2026 Alexander Burmatov <thatman@altlinux.org> 0.0.9-alt1
- New 0.0.9 version.

* Fri May 08 2026 Alexander Burmatov <thatman@altlinux.org> 0.0.8.post1-alt1
- New 0.0.8.post1 version.

* Fri Apr 24 2026 Alexander Burmatov <thatman@altlinux.org> 0.0.7.post6-alt1
- New 0.0.7.post6 version.

* Mon Apr 20 2026 Alexander Burmatov <thatman@altlinux.org> 0.0.7-alt1
- Initial build for Sisyphus.
