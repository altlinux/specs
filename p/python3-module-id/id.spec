%define _unpackaged_files_terminate_build 1
%define pypi_name id
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.5.0
Release: alt1
Summary: A tool for generating OIDC identities
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/id
Vcs: https://github.com/di/id
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
%endif

%description
%pypi_name is a Python tool for generating OIDC identities. It can automatically
detect and produce OIDC credentials on a number of environments, including
GitHub Actions, GitLab pipelines and Google Cloud.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra test/

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Jan 22 2025 Stanislav Levin <slev@altlinux.org> 1.5.0-alt1
- Initial build for Sisyphus.
