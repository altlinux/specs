%define _unpackaged_files_terminate_build 1
%define pypi_name openai-agents
%define mod_name agents

# a lot of test dependencies
%def_without check

Name: python3-module-%pypi_name
Version: 0.22.0
Release: alt1

Summary: A lightweight, powerful framework for multi-agent workflows
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/openai-agents/
Vcs: https://github.com/openai/openai-agents-python

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
# python3-module-griffe-lib doesn't provide 'griffelib'
%add_pyproject_deps_runtime_filter griffelib
Requires: python3-module-griffe-lib
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
# python3-module-griffe-lib doesn't provide 'griffelib'
%add_pyproject_deps_check_filter griffelib
BuildRequires: python3-module-griffe-lib
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
The OpenAI Agents SDK is a lightweight yet powerful framework for building
multi-agent workflows. It is provider-agnostic, supporting the OpenAI Responses
and Chat Completions APIs, as well as 100+ other LLMs.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_depgroup dev

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra -o=addopts=-Wignore

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Aug 31 2026 Anton Zhukharev <ancieg@altlinux.org> 0.22.0-alt1
- Packaged for ALT Sisyphus.
