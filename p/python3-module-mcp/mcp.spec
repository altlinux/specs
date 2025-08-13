%define _unpackaged_files_terminate_build 1
%define pypi_name mcp

%def_with check

Name: python3-module-%pypi_name
Version: 1.12.4
Release: alt1
Summary: The official Python SDK for Model Context Protocol servers and clients.
License: MIT
Group:  Development/Python3
Url: https://github.com/modelcontextprotocol/python-sdk
Vcs: https://pypi.org/project/mcp/

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

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

%if_with check
BuildRequires: python3(pytest)
%endif

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

%prep
%setup
%autopatch -p1
sed -ri 's/^dynamic = \[.*"version".*\]/version = "%{version}"/' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

%check
#pyproject_run_pytest

%files
%doc *.md
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Aug 08 2025 Pavel Shilov <zerospirit@altlinux.org> 1.12.4-alt1
- Initial build for Sisyphus.