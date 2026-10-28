%define _unpackaged_files_terminate_build 1
%define pypi_name fastmcp
%define mod_name fastmcp

# check requires the Internet connection
%def_without check

%define add_python_extra() \
%{expand:%%package -n python3-module-%{expand:%%pep503_name %1}+%2 \
Summary: %%summary \
Group: Development/Python3 \
Requires: python3-module-%{expand:%%pep503_name %1} \
%%pyproject_runtimedeps_metadata_extra %2 \
%%description -n python3-module-%{expand:%%pep503_name %1}+%2 \
Extra "%2" for %1. \
%%files -n python3-module-%{expand:%%pep503_name %1}+%2 \
}

Name: python3-module-fastmcp
Version: 4.1.4
Release: alt1

Summary: The fast, Pythonic way to build MCP servers and clients
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/fastmcp/
Vcs: https://github.com/PrefectHQ/fastmcp

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-pyproject >= 0.3.0

# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps -- fastmcp_metadata --depformatextra=%pyproject_depextra_format
%pyproject_builddeps -- fastmcp_pep518
%pyproject_builddeps -- fastmcp_pep517
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
The Model Context Protocol (MCP) connects LLMs to tools and data.
FastMCP is a full MCP application framework for servers, clients, and
interactive apps.

%add_python_extra fastmcp anthropic
# %%add_python_extra fastmcp apps # -- no 'prefab-ui' in the repo
# %%add_python_extra fastmcp azure # -- skip azure
%add_python_extra fastmcp client
# %%add_python_extra fastmcp code-mode # -- no 'pydantic-monty' in the repo
%add_python_extra fastmcp gemini
%add_python_extra fastmcp mcp
%add_python_extra fastmcp openai
%add_python_extra fastmcp server

%package slim
Summary: The dependency-slim FastMCP package
Group: Development/Python3
Url: https://pypi.org/project/fastmcp-slim/
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps -- fastmcp_slim_metadata --depformatextra=%pyproject_depextra_format
%pyproject_builddeps -- fastmcp_slim_pep518
%pyproject_builddeps -- fastmcp_slim_pep517

%description slim
The Model Context Protocol (MCP) connects LLMs to tools and data.
FastMCP is a full MCP application framework for servers, clients, and
interactive apps.

%add_python_extra fastmcp-slim anthropic
# %%add_python_extra fastmcp-slim apps # -- no 'prefab-ui' in the repo
# %%add_python_extra fastmcp-slim azure # -- skip azure
%add_python_extra fastmcp-slim client
# %%add_python_extra fastmcp-slim code-mode # -- no 'pydantic-monty' in the repo
%add_python_extra fastmcp-slim gemini
%add_python_extra fastmcp-slim mcp
%add_python_extra fastmcp-slim openai
%add_python_extra fastmcp-slim server

%prep
%setup
%autopatch -p1
%pyproject_scm_init v%version

# fastmcp
%pyproject_deps_resync fastmcp_pep518 pep518
%pyproject_deps_resync fastmcp_pep517 pep517
%pyproject_deps_resync fastmcp_metadata metadata
%if_with check
%pyproject_deps_resync_check_depgroup dev
%endif

# fastmcp-slim
cd fastmcp_slim
%pyproject_deps_resync fastmcp_slim_pep518 pep518
%pyproject_deps_resync fastmcp_slim_pep517 pep517
%pyproject_deps_resync fastmcp_slim_metadata metadata

%build
# fastmcp
%pyproject_build

# fastmcp-slim
cd fastmcp_slim
%pyproject_build

%install
# fastmcp
%pyproject_install

# fastmcp-slim
cd fastmcp_slim
%pyproject_install

%check
%pyproject_run_pytest -vra -o=addopts=

%files
%python3_sitelibdir/fastmcp-%version.dist-info/

%files slim
%_bindir/fastmcp
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/fastmcp_slim-%version.dist-info/

%changelog
* Wed Oct 28 2026 Anton Zhukharev <ancieg@altlinux.org> 4.1.4-alt1
- Updated to 4.1.4.
- Set correct unversioned requirements.

* Fri Oct 16 2026 Anton Zhukharev <ancieg@altlinux.org> 4.1.0-alt1
- Updated to 4.1.0.

* Tue Sep 08 2026 Anton Zhukharev <ancieg@altlinux.org> 3.4.7-alt1
- Packaged for ALT Sisyphus.
