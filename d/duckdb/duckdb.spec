%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method unresolved=relaxed

#Disabling tests due to the need to use the network,
#but it is not available in the build environment.
%def_without check

Name: duckdb
Version: 1.2.1
Release: alt2

Summary: An analytical in-process SQL database management system
License: MIT
Group: Development/Databases
Url: http://duckdb.org/
Vcs: https://github.com/duckdb/duckdb

ExclusiveArch: x86_64 aarch64 loongarch64 riscv64

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-ninja
BuildRequires: /proc
BuildRequires: gcc-c++
BuildRequires: python3-dev
BuildRequires: cmake
BuildRequires: libssl-devel
BuildRequires: libicu-devel

%package devel
Summary: Development header files for DuckDB
Group: Development/C++

%description
DuckDB is a high-performance analytical database system.
It is designed to be fast, reliable, portable, and easy to use.
DuckDB provides a rich SQL dialect, with support far beyond basic SQL.
DuckDB supports arbitrary and nested correlated subqueries, window functions,
collations, complex types (arrays, structs, maps), and several extensions
designed to make SQL easier to use.

%description devel
This package contains the development header files and libraries
necessary to develop DuckDB applications.

%prep
%setup
%autopatch0 -p1

# Remove vendored icu just to be sure
find extension/icu/third_party/icu -name unicode -type d | xargs rm -rf

%build
%cmake  -GNinja \
	-DWITH_INTERNAL_ICU=FALSE \
	-DOVERRIDE_GIT_DESCRIBE="v%version" \
	-DOVERRIDE_GIT_RELEASE="%release" \
	-DOVERRIDE_GIT_NOHASH=1 \
	-DBUILD_EXTENSIONS="autocomplete;icu;tpch;tpcds;json;jemalloc" \
	-DCMAKE_BUILD_TYPE=Release

%ninja_build -C "%_cmake__builddir"

%install
%ninja_install -C "%_cmake__builddir"
mkdir -p %buildroot%_sysconfdir/ld.so.conf.d
cat << EOF >> %buildroot%_sysconfdir/ld.so.conf.d/duckdb.conf
%_libdir/duckdb
EOF

%check
%_cmake__builddir/test/unittest
%_cmake__builddir/tools/sqlite3_api_wrapper/test_sqlite3_api_wrapper

%files
%_bindir/duckdb
%_libdir/libduckdb*.so
%_libdir/duckdb/
%_libdir/libsqlite3_api_wrapper.so
%_libdir/libcore_functions_extension.so

%_sysconfdir/ld.so.conf.d/duckdb.conf

%files devel
%_includedir/*
%_cmakedir/DuckDB/

%changelog
* Wed Mar 26 2025 Ilya Sorochan <k0tran@altlinux.org> 1.2.1-alt2
- Switch to sisyphus libicu instead of vendored.
- Fix jemalloc for loongarch64 and riscv64.

* Tue Mar 25 2025 Artem Krasovskiy <aibure@altlinux.org> 1.2.1-alt1
- New version 1.2.1-alt1

* Thu Feb 13 2025 Artem Krasovskiy <aibure@altlinux.org> 1.2.0-alt1
- New version 1.2.0-alt1.

* Sat Dec 28 2024 Artem Krasovskiy <aibure@altlinux.org> 1.1.3-alt1
- Initial build for ALT.
