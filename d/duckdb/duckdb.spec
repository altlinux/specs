%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%add_findreq_skiplist %_datadir/duckdb/*
%add_findreq_skiplist %_datadir/duckdb/**/*
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method unresolved=relaxed
%ifarch loongarch64 riscv64
    %define spinwait_value 0
    %global optflags_debug -g1
%else
    %define spinwait_value 1
%endif

#Disabling tests due to the need to use the network,
#but it is not available in the build environment.
%def_without check

Name: duckdb
Version: 1.5.4
Release: alt1

Summary: An analytical in-process SQL database management system
License: MIT
Group: Development/Databases
Url: http://duckdb.org/
Vcs: https://github.com/duckdb/duckdb

ExclusiveArch: x86_64 aarch64 loongarch64 riscv64

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: /proc
BuildRequires: gcc-c++
BuildRequires: python3-dev
BuildRequires: cmake
BuildRequires: libssl-devel
BuildRequires: libicu-devel

%package libduckdb
Summary: Shared library for DuckDB
Group: Development/C++

%package devel-static
Summary: Development static libraries for DuckDB
Group: Development/C++

%package src
Summary: Source code for DuckDB
Group: Development/C++
BuildArch: noarch

%description
DuckDB is a high-performance analytical database system.
It is designed to be fast, reliable, portable, and easy to use.
DuckDB provides a rich SQL dialect, with support far beyond basic SQL.
DuckDB supports arbitrary and nested correlated subqueries, window functions,
collations, complex types (arrays, structs, maps), and several extensions
designed to make SQL easier to use.

%description libduckdb
This package contains the DuckDB shared library.

%description devel-static
This package contains the development static libraries
necessary to develop DuckDB extensions.

%description src
This package contains the source code of DuckDB.

%prep
%setup
%autopatch0 -p1

# Remove vendored icu just to be sure
find extension/icu/third_party/icu -name unicode -type d | xargs rm -rf

%build
%cmake	-DWITH_INTERNAL_ICU=FALSE \
	-DHAVE_CPU_SPINWAIT=%{spinwait_value} \
	-DOVERRIDE_GIT_DESCRIBE="v%version" \
	-DOVERRIDE_GIT_RELEASE="%release" \
	-DOVERRIDE_GIT_NOHASH=1 \
	-DBUILD_EXTENSIONS="autocomplete;icu;tpch;tpcds;json;jemalloc" \
	-DCMAKE_BUILD_TYPE=Release

%cmake_build

%install
%cmake_install
find %buildroot%_libdir -maxdepth 1 \( -name 'lib*_extension.a' -o -name 'libduckdb_*.a' ! -name 'libduckdb_static.a' -o -name 'libdummy_static_extension_loader.a' \) -delete

mkdir -p %buildroot%_datadir/duckdb
cp -r CMakeLists.txt extension src third_party tools %buildroot%_datadir/duckdb

%check
%_cmake__builddir/test/unittest

%files
%_bindir/duckdb

%files libduckdb
%_libdir/libduckdb.so

%files devel-static
%_libdir/libduckdb_static.a
%_includedir/duckdb
%_includedir/duckdb.h
%_includedir/duckdb.hpp
%_cmakedir/DuckDB/

%files src
%_datadir/duckdb

%changelog
* Tue Jun 23 2026 Artem Krasovskiy <aibure@altlinux.org> 1.5.4-alt1
- New version 1.5.4.

* Thu May 28 2026 Artem Krasovskiy <aibure@altlinux.org> 1.5.3-alt2
- Reduce debuginfo on riscv64 and loongarch64 (thx iv@).

* Wed May 27 2026 Artem Krasovskiy <aibure@altlinux.org> 1.5.3-alt1
- New version 1.5.3.

* Thu Jan 29 2026 Artem Krasovskiy <aibure@altlinux.org> 1.4.4-alt1
- New version 1.4.4.

* Tue Dec 23 2025 Artem Krasovskiy <aibure@altlinux.org> 1.4.3-alt1
- New version 1.4.3 (closes: CVE-2025-64429).

* Fri Oct 24 2025 Artem Krasovskiy <aibure@altlinux.org> 1.4.1-alt1
- New version 1.4.1.

* Tue Sep 02 2025 Artem Krasovskiy <aibure@altlinux.org> 1.3.2-alt1
- New version 1.3.2.

* Wed Mar 26 2025 Ilya Sorochan <k0tran@altlinux.org> 1.2.1-alt2
- Switch to sisyphus libicu instead of vendored.
- Fix jemalloc for loongarch64 and riscv64.

* Tue Mar 25 2025 Artem Krasovskiy <aibure@altlinux.org> 1.2.1-alt1
- New version 1.2.1-alt1

* Thu Feb 13 2025 Artem Krasovskiy <aibure@altlinux.org> 1.2.0-alt1
- New version 1.2.0-alt1.

* Sat Dec 28 2024 Artem Krasovskiy <aibure@altlinux.org> 1.1.3-alt1
- Initial build for ALT.
