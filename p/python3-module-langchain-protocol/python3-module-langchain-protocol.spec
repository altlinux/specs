%define _unpackaged_files_terminate_build 1
%define pypi_name langchain-protocol
%define mod_name langchain_protocol

Name: python3-module-%pypi_name
Version: 0.0.19
Release: alt1

Summary: Python bindings for the LangChain agent streaming protocol
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/langchain-protocol/
Vcs: https://github.com/langchain-ai/agent-protocol

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%description
%summary.
This package provides generated TypedDict and Literal definitions for
the protocol's commands, events, results, and payload shapes. It does
not include a runtime client, transport, or helper APIs - it is
intended as a source of typing primitives only.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Aug 27 2026 Anton Zhukharev <ancieg@altlinux.org> 0.0.19-alt1
- Packaged for ALT Sisyphus.
