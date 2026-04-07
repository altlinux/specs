%define _unpackaged_files_terminate_build 1
%define pypi_name igraph
%define mod_name igraph

# WONTFIX: ARPACK error on i586
%ifarch %ix86
%def_without check
%else
%def_with check
%endif

%python3_set_limited_api

Name: python3-module-%pypi_name
Version: 1.0.0
Release: alt1

Summary: High performance graph data structures and algorithms
License: GPL-2.0
Group: Development/Python3
Url: https://pypi.org/project/igraph/
Vcs: https://github.com/igraph/python-igraph

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%add_pyproject_deps_build_filter cmake
%pyproject_builddeps_build
BuildRequires: gcc-c++
BuildRequires: pkgconfig(igraph)
%if_with check
# plotly isn't in sisyphus
%add_pyproject_deps_check_filter plotly
%pyproject_builddeps_metadata_extra test
%endif

%description
igraph is a library for creating and manipulating graphs.
It is intended to be as powerful (ie. fast) as possible to enable
the analysis of large graphs.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
export SKIP_HEADER_INSTALL=1
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- pytest -vra -o=addopts= --import-mode=importlib tests

%files
%_bindir/igraph
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Apr 07 2026 Anton Zhukharev <ancieg@altlinux.org> 1.0.0-alt1
- Packaged for ALT Sisyphus.
