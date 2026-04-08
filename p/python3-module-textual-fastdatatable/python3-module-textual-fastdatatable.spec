%define _unpackaged_files_terminate_build 1

%define pypi_name textual-fastdatatable
%define mod_name textual_fastdatatable
%def_with check

Name: python3-module-%pypi_name
Version: 0.14.0
Release: alt1

Summary: Reimplementation of Textual's DataTable widget
Group: Development/Python3
License: MIT
Url: https://github.com/tconbeer/textual-fastdatatable
VCS: https://github.com/tconbeer/textual-fastdatatable.git
BuildArch: noarch

# Source-url: https://github.com/tconbeer/%pypi_name/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch1: alt-remove-polars-backend.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
A performance-focused reimplementation of Textual's DataTable widget,
with a pluggable data storage backend.

Textual's built-in DataTable widget is beautiful and powerful, but it
can be slow to load large datasets.

%prep
%setup
%if_with check
%patch1 -p1
%endif
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest \
    --ignore=tests/snapshot_tests/test_snapshots.py \
    --ignore=tests/unit_tests/test_create_backend.py

%files
%doc README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir_noarch/%{pyproject_distinfo %mod_name}

%changelog
* Wed Apr 08 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.14.0-alt1
- initial build for ALT Linux
