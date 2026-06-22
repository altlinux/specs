%global _unpackaged_files_terminate_build 1
%define pypi_name pr-agent

%def_without check

Name: pr-agent
Version: 0.37.0
Release: alt1
Summary: Open-Source AI-powered code review agent
Group: Development/Python3
License: AGPL-3.0
BuildArch: noarch
Url: https://pypi.org/project/pr-agent/
VCS: https://github.com/qodo-ai/pr-agent
AutoReq: yes, nopython3
AutoProv: yes, nopython3

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

BuildRequires(pre): rpm-build-pyproject

%pyproject_builddeps_build

%add_pyproject_deps_runtime_filter atlassian-python-api
%add_pyproject_deps_runtime_filter azure-devops
%add_pyproject_deps_runtime_filter google-generativeai
%add_pyproject_deps_runtime_filter google-cloud-
%add_pyproject_deps_runtime_filter giteapy
%add_pyproject_deps_runtime_filter mangum
%add_pyproject_deps_runtime_filter retry
%add_pyproject_deps_runtime_filter a2a-sdk
%add_pyproject_deps_runtime_filter langfuse
%pyproject_runtimedeps_metadata

%if_with check
%add_pyproject_deps_check_filter atlassian-python-api
%add_pyproject_deps_check_filter azure-devops
%add_pyproject_deps_check_filter google-generativeai
%add_pyproject_deps_check_filter google-cloud-
%add_pyproject_deps_check_filter giteapy
%add_pyproject_deps_check_filter mangum
%add_pyproject_deps_check_filter retry
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
QodoAI PR-Agent aims to help efficiently review and handle pull
requests, by providing AI feedbacks and suggestions.

%prep
%setup

sed -i 's/version = .*/version = "%version"/' ./pyproject.toml

%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements-dev.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%_bindir/pr-agent
%python3_sitelibdir/pr_agent/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Jun 22 2026 Egor Ignatov <egori@altlinux.org> 0.37.0-alt1
- Initial build for ALT Linux.
