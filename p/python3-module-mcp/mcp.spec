%define _unpackaged_files_terminate_build 1
%define pypi_name mcp

%def_with check

Name: python3-module-%pypi_name
Version: 2.1.1
Release: alt1
Summary: The official Python SDK for Model Context Protocol servers and clients.
License: MIT
Group:  Development/Python3
Url: https://github.com/modelcontextprotocol/python-sdk
Vcs: https://pypi.org/project/mcp/

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch
Patch1: mcp-fastmcp-compat.patch

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(hatchling)
BuildRequires: python3-module-uv-dynamic-versioning
BuildRequires: python3(pip)
BuildRequires: python3(anyio)
BuildRequires: python3(httpx)
BuildRequires: python3-module-httpx-sse
BuildRequires: python3(pydantic)
BuildRequires: python3(starlette)
BuildRequires: python3-module-python-multipart
BuildRequires: python3-module-sse-starlette
BuildRequires: python3-module-pydantic-settings
BuildRequires: python3(jsonschema)
BuildRequires: python3(typer)
BuildRequires: python3(uv)
BuildRequires: python3-module-uv-build
BuildRequires: python3(websockets)
BuildRequires: python3-module-inline-snapshot
BuildRequires: python3-module-dirty-equals
BuildRequires: python3-module-pydantic-core
BuildRequires: python3-module-ruff
BuildRequires: python3(httpcore)
BuildRequires: python3-module-typing_extensions

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3-module-pytest-xdist
BuildRequires: python3-module-pytest-examples
BuildRequires: python3(uvicorn)
BuildRequires: python3(requests)
%endif

Requires: python3-module-mcp-types = %{version}-%{release}
Requires: python3(anyio)
Requires: python3(httpx)
Requires: python3(uvicorn)
Requires: python3(typer)
Requires: python3-module-sse-starlette
Requires: python3-module-pydantic-settings
Requires: python3(websockets)
Requires: python3-module-inline-snapshot
Requires: python3-module-dirty-equals

%py3_provides %pypi_name

%description
The Model Context Protocol allows applications to provide context for
LLMs in a standardized way, separating the concerns of providing
context from the actual LLM interaction.
This Python SDK implements the full MCP specification, making it easy to:
- Build MCP clients that can connect to any MCP server
- Create MCP servers that expose resources, prompts and tools
- Use standard transports like stdio, SSE, and Streamable HTTP
- Handle all MCP protocol messages and lifecycle events

%package -n python3-module-mcp-types
Group: Development/Python3
Summary: Model Context Protocol wire types
Requires: python3(pydantic)
Requires: python3-module-typing_extensions
%py3_provides mcp_types

%description -n python3-module-mcp-types
Standalone MCP protocol wire types used by python3-module-mcp.

%prep
%setup
%autopatch -p1
sed -ri 's/^dynamic = \[.*"version".*\]/version = "%{version}"/' pyproject.toml
sed -ri 's/^dynamic = \[.*"version".*\]/version = "%{version}"/' src/mcp-types/pyproject.toml

%build
pushd src/mcp-types
%pyproject_build
popd
%pyproject_build

%install
pushd src/mcp-types
%pyproject_install
popd
%pyproject_install

%check
#pyproject_run_pytest

%files
%doc *.md
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%files -n python3-module-mcp-types
%python3_sitelibdir/mcp_types/
%python3_sitelibdir/%{pyproject_distinfo mcp-types}/

%changelog
* Thu Aug 27 2026 Pavel Shilov <zerospirit@altlinux.org> 2.1.1-alt1
- updated from 2.0.0 to 2.1.1

* Tue Aug 04 2026 Pavel Shilov <zerospirit@altlinux.org> 2.0.0-alt1
- 1.26.0 -> 2.0.0

* Fri Feb 20 2026 Pavel Shilov <zerospirit@altlinux.org> 1.26.0-alt1
- 1.18.0 -> 1.26.0

* Fri Oct 24 2025 Pavel Shilov <zerospirit@altlinux.org> 1.18.0-alt1
- 1.12.4 -> 1.18.0

* Fri Aug 08 2025 Pavel Shilov <zerospirit@altlinux.org> 1.12.4-alt1
- Initial build for Sisyphus.
