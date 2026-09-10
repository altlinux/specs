%define _unpackaged_files_terminate_build 1
%define pypi_name anthropic
%define mod_name anthropic

# check requires the Internet connection
%def_without check

%define add_python_extra() \
%{expand:%%package -n %%name+%1 \
Summary: %%summary \
Group: Development/Python3 \
Requires: %%name \
%%pyproject_runtimedeps_metadata_extra %1 \
%%description -n %%name+%1' \
Extra "%1" for %%pypi_name. \
%%files -n %%name+%1 \
}

Name: python3-module-%pypi_name
Version: 1.4.0
Release: alt1

Summary: The official Python library for the anthropic API
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/anthropic/
Vcs: https://github.com/anthropics/anthropic-sdk-python

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
The Anthropic Python SDK provides convenient access to the Claude API from
Python applications. It supports both synchronous and asynchronous operations,
streaming, and integrations with Amazon Bedrock, Claude Platform on AWS, Google
Cloud, and Microsoft Foundry.

%add_python_extra aiohttp
%add_python_extra aws
%add_python_extra bedrock
%add_python_extra mcp
%add_python_extra webhooks

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
%pyproject_run_pytest -vra

%files
%python3_sitelibdir_noarch/%mod_name/
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Sep 10 2026 Anton Zhukharev <ancieg@altlinux.org> 1.4.0-alt1
- Updated to 1.4.0.

* Mon Apr 14 2025 David Sultaniiazov <x1z53@altlinux.org> 0.49.0-alt1
- Initial build
