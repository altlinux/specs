%define _unpackaged_files_terminate_build 1
%define pypi_name pydocket
%define mod_name docket

# tests require running docker
%def_without check

Name: python3-module-%pypi_name
Version: 0.24.1
Release: alt1

Summary: A distributed background task system for Python functions
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pydocket/
Vcs: https://github.com/chrisguidry/docket

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
# 'codespell' is provided by 'codespell' package, not 'python3-module-codespell'
%add_pyproject_deps_check_filter codespell
BuildRequires: codespell
%add_pyproject_deps_check_filter loq
%add_pyproject_deps_check_filter pytest-flakefinder
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Docket is a distributed background task system for Python functions with
a focus on the scheduling of future work as seamlessly and efficiently
as immediate work.

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra -o=addopts= tests/cli

%files
%_bindir/docket
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Aug 20 2026 Anton Zhukharev <ancieg@altlinux.org> 0.24.1-alt1
- Packaged for ALT Sisyphus.
