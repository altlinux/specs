%define _unpackaged_files_terminate_build 1
%define pypi_name tox-uv-bare
%define mod_name tox_uv

%def_with check

Name: python3-module-%pypi_name
Version: 1.34.0
Release: alt1
Summary: Integration of uv with tox (bare package, bring your own uv)
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/tox-uv-bare
Vcs: https://github.com/tox-dev/tox-uv
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
# tox_uv directory was previously packaged in tox-uv
Conflicts: python3-module-tox-uv <= 1.29.0-alt1
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
# install system uv
BuildRequires: uv
%endif

%description
%summary.

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
export UV_OFFLINE=1
%pyproject_run_pytest -vra tests

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Apr 06 2026 Stanislav Levin <slev@altlinux.org> 1.34.0-alt1
- 1.33.4 -> 1.34.0.

* Fri Mar 13 2026 Stanislav Levin <slev@altlinux.org> 1.33.4-alt1
- 1.33.2 -> 1.33.4.

* Tue Mar 10 2026 Stanislav Levin <slev@altlinux.org> 1.33.2-alt1
- Initial build for sisyphus.
