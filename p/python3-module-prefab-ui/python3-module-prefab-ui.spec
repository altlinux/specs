%define _unpackaged_files_terminate_build 1
%define pypi_name prefab-ui
%define mod_name prefab_ui

%def_with check

Name: python3-module-%pypi_name
Version: 0.21.1
Release: alt1

Summary: The generative UI framework that even humans can use
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/prefab-ui/
Vcs: https://github.com/PrefectHQ/prefab

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
%add_pyproject_deps_check_filter pdbpp
%add_pyproject_deps_check_filter polars
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Prefab is a UI framework for building rich, interactive interfaces in Python.
Create MCP Apps, data dashboards, interactive tools, and more with 100+ prebuilt
components. A bundled React renderer turns everything into a self-contained
application.

%prep
%setup
%autopatch -p1
%pyproject_scm_init v%version
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_depgroup dev

%build
%pyproject_build

%install
%pyproject_install

%check
# tests/test_packaging.py::test_guides_work_in_direct_and_sdist_built_wheels -- requires the Internet connection
%pyproject_run_pytest -vra --deselect tests/test_packaging.py::test_guides_work_in_direct_and_sdist_built_wheels

%files
%_bindir/prefab
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Oct 29 2026 Anton Zhukharev <ancieg@altlinux.org> 0.21.1-alt1
- Packaged for ALT Sisyphus.
