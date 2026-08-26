%define _unpackaged_files_terminate_build 1
%define pypi_name ghapi
%define mod_name ghapi

Name: python3-module-%pypi_name
Version: 2.1.2
Release: alt1

Summary: A python client for the GitHub API
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/ghapi/
VCS: https://github.com/AnswerDotAI/ghapi/

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
A Python client for the GitHub REST API, generated from the official
OpenAPI specification. It provides full coverage of all endpoints
(issues, PRs, actions, admin, etc.) with both asynchronous and
synchronous interfaces, plus a command-line tool for shell scripting.

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
%_bindir/completion-ghapi
%_bindir/gh-create-workflow
%_bindir/ghapi
%_bindir/ghpath
%_bindir/ghraw
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Aug 21 2026 Anton Zhukharev <ancieg@altlinux.org> 2.1.2-alt1
- Updated to 2.1.2.

* Wed Feb 12 2025 Anastasia Doronina <swaggyglice@altlinux.org> 1.0.6-alt1
- Initial Build for Sisyphus.
