%define _unpackaged_files_terminate_build 1
%define pypi_name duckdb
%define mod_name duckdb

# too many heavy dependencies
%def_without check

Name: python3-module-%pypi_name
Version: 1.5.4
Release: alt1

Summary: The DuckDB Python package
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/duckdb/
Vcs: https://github.com/duckdb/duckdb-python

# sync with duckdb package
ExclusiveArch: x86_64 aarch64 loongarch64 riscv64

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: libicu-devel
BuildRequires: python3-dev
BuildRequires: duckdb-src
%add_pyproject_deps_build_filter cmake
%add_pyproject_deps_build_filter ninja
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
%summary.

%prep
%setup
%autopatch -p1
%pyproject_scm_init v%version
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup test
%endif

# entire duckdb source code is required to build the client
cp -rT %_datadir/duckdb external/duckdb

%build
export LDFLAGS='-lpython3'
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/_duckdb.*.so
%python3_sitelibdir/_duckdb-stubs/
%python3_sitelibdir/adbc_driver_duckdb/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Jun 23 2026 Artem Krasovskiy <aibure@altlinux.org> 1.5.4-alt1
- Updated to 1.5.4.

* Thu May 28 2026 Anton Zhukharev <ancieg@altlinux.org> 1.5.3-alt1
- Packaged for ALT Sisyphus.
