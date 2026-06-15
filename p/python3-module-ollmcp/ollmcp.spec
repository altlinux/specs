Name: python3-module-ollmcp
Version: 0.29.1
Release: alt1

Summary: MCP Client for Ollama
License: MIT
Group: Development/Python
URL: https://pypi.org/project/ollmcp
VCS: https://github.com/jonigl/mcp-client-for-ollama

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%description
A text-based user interface (TUI) client for interacting with MCP servers using
Ollama. Features include agent mode, multi-server, model switching, streaming
responses, tool management, human-in-the-loop, thinking mode, model params config,
MCP prompts, custom system prompt and saved preferences. Built for developers
working with local LLMs.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_depgroup dev

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o addopts= tests

%files
%_bindir/ollmcp
%python3_sitelibdir/mcp_client_for_ollama
%python3_sitelibdir/mcp_client_for_ollama-%version.dist-info

%changelog
* Mon Jun 15 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.29.1-alt1
- 0.29.1 released

* Wed May 27 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.29.0-alt1
- 0.29.0 released

* Fri May 15 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.28.1-alt1
- 0.28.1 released
