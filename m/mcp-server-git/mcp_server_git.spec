%define _unpackaged_files_terminate_build 1
%def_with check
%define py_name mcp_server_git

Name: mcp-server-git
Version: 2026.7.10
Release: alt1

Summary: A git MCP server
License: MIT
Group: Development/Tools
Url: https://pypi.org/project/mcp-server-git/

# Note: Upstream git holds several MCP servers implemented
# in different programming languages. To simplify matters
# and avoid huge git histroy, we base our package on tarball
# from PyPy -- see  https://pypi.org/project/mcp-server-git/
Vcs: https://github.com/modelcontextprotocol/servers/tree/main/src/git
BuildArch: noarch

Source0: %py_name-%version.tar

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-pytest

BuildRequires: python3(click)
BuildRequires: python3(gitpython)
BuildRequires: python3(mcp)
BuildRequires: python3(pydantic)
%endif

Provides: python3-module-%py_name = %EVR

%description
A Model Context Protocol server providing tools to read, search,
and manipulate Git repositories programmatically via LLMs.

%prep
%setup -n %py_name-%version
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc README.md
%_bindir/*
%python3_sitelibdir_noarch/%{py_name}*

%changelog
* Thu Aug 06 2026 Ivan A. Melnikov <iv@altlinux.org> 2026.7.10-alt1
- build for Sisyphus
