%define _unpackaged_files_terminate_build 1
%define pypi_name tox-uv
%define mod_name tox_uv

%def_with check

Name: python3-module-%pypi_name
Version: 1.28.0
Release: alt1
Summary: Integration of uv with tox
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/tox-uv
Vcs: https://github.com/tox-dev/tox-uv
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
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
tox-uv is a tox plugin, which replaces virtualenv and pip with uv in your tox
environments. Note that you will get both the benefits (performance) or
downsides (bugs) of uv.

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup test
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Sep 04 2025 Stanislav Levin <slev@altlinux.org> 1.28.0-alt1
- Initial build for Sisyphus.
