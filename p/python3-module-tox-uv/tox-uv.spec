%define _unpackaged_files_terminate_build 1
%define pypi_name tox-uv
%define mod_name tox_uv_meta

%def_with check

Name: python3-module-%pypi_name
Version: 1.35.1
Release: alt1
Summary: Integration of uv with tox (meta package)
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
pushd meta
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
popd
%if_with check
%pyproject_deps_resync_check_depgroup test
%endif

%build
pushd meta
%pyproject_build
popd

%install
pushd meta
%pyproject_install
popd

%check
pushd meta
%pyproject_run -- bash -s <<-'ENDTESTS'
set -eux
pushd ..
export UV_OFFLINE=1
export UV_NO_BUILD_ISOLATION=1
python -m pytest -vra meta/tests/
popd
ENDTESTS
popd

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Apr 13 2026 Stanislav Levin <slev@altlinux.org> 1.35.1-alt1
- 1.35.0 -> 1.35.1.

* Fri Apr 10 2026 Stanislav Levin <slev@altlinux.org> 1.35.0-alt1
- 1.34.0 -> 1.35.0.

* Mon Apr 06 2026 Stanislav Levin <slev@altlinux.org> 1.34.0-alt1
- 1.33.4 -> 1.34.0.

* Fri Mar 13 2026 Stanislav Levin <slev@altlinux.org> 1.33.4-alt1
- 1.33.2 -> 1.33.4.

* Tue Mar 10 2026 Stanislav Levin <slev@altlinux.org> 1.33.2-alt1
- 1.29.0 -> 1.33.2.

* Thu Dec 11 2025 Stanislav Levin <slev@altlinux.org> 1.29.0-alt1
- 1.28.0 -> 1.29.0.

* Thu Sep 04 2025 Stanislav Levin <slev@altlinux.org> 1.28.0-alt1
- Initial build for Sisyphus.
