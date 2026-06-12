%define _unpackaged_files_terminate_build 1
%define abiversion 2.6.0
Name: clickhouse-cpp
Version: 2.6.2
Release: alt1
Summary: ClickHouse C++ client library
Group: System/Libraries
License: Apache-2.0
Url: https://github.com/ClickHouse/clickhouse-cpp
VCS: https://github.com/ClickHouse/clickhouse-cpp.git
Source: %name-%version.tar
Source1: %name.watch

Patch1: %name-2.6.0-alt-build.patch

BuildRequires: gcc-c++ cmake
BuildRequires: liblz4-devel
BuildRequires: libcityhash-devel
BuildRequires: libabseil-cpp-devel
BuildRequires: libzstd-devel

%description
C++ client library for ClickHouse, a fast open-source column-oriented
database management system. Supports the native ClickHouse binary protocol
and a wide range of ClickHouse data types.

%package -n lib%name%abiversion
Summary: ClickHouse C++ client library
Group: System/Libraries

%description -n lib%name%abiversion
C++ client library for ClickHouse, a fast open-source column-oriented
database management system. Supports the native ClickHouse binary protocol
and a wide range of ClickHouse data types.

%package -n lib%name-devel
Summary: Development files for ClickHouse C++ client library
Group: Development/C++
Requires: lib%name%abiversion = %EVR

%description -n lib%name-devel
C++ client library for ClickHouse, a fast open-source column-oriented
database management system. Supports the native ClickHouse binary protocol
and a wide range of ClickHouse data types.

This package contains development files.

%prep
%setup
%patch1 -p1

# ensure 3rd-party bundled libraries are not used
rm -rf contrib/{cityhash,gtest,lz4,absl,zstd}

%build
%cmake -DWITH_SYSTEM_CITYHASH=ON -DWITH_SYSTEM_LZ4=ON -DWITH_SYSTEM_ABSEIL=ON -DWITH_SYSTEM_ZSTD=ON -DBUILD_SHARED_LIBS=ON \
%ifarch %ix86
	-DCMAKE_CXX_FLAGS:STRING="%optflags -Wno-error=conversion" \
%endif
	%nil
%cmake_build

%install
%cmakeinstall_std
ln -s clickhouse %buildroot/%_includedir/clickhouse-cpp

%files -n lib%name%abiversion
%doc LICENSE
%doc README.md
%_libdir/*.so.%abiversion

%files -n lib%name-devel
%_includedir/clickhouse-cpp
%_includedir/clickhouse
%_libdir/*.so

%changelog
* Fri Jun 12 2026 Anton Farygin <rider@altlinux.org> 2.6.2-alt1
- 2.6.1 -> 2.6.2

* Mon Mar 30 2026 Anton Farygin <rider@altlinux.org> 2.6.1-alt1
- 2.6.0 -> 2.6.1

* Tue Mar 03 2026 Anton Farygin <rider@altlinux.org> 2.6.0-alt1
- 2.4.0 -> 2.6.0

* Fri Jan 05 2024 Pavel Vainerman <pv@altlinux.ru> 2.4.0-alt3
- build with system libabseil

* Tue Jun 27 2023 Pavel Vainerman <pv@altlinux.ru> 2.4.0-alt2
- headers of the libabseail are packed together with clickhouse (Closes: #42411)

* Fri Apr 28 2023 Pavel Vainerman <pv@altlinux.ru> 2.4.0-alt1
- new version (2.4.0) with rpmgs script

* Tue Apr 12 2022 Anton Farygin <rider@altlinux.ru> 1.2.2-alt2
- libclickhouse-cpp-devel: add conflict with libabseil-cpp-devel (Closes: #42411)

* Wed Sep 30 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.2-alt1
- Updated to upstream version 1.2.2.

* Fri Sep 25 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.1-alt1
- Updated to upstream release version 1.2.1.

* Mon Jun 29 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.0-alt1
- Updated to upstream release version 1.2.0.

* Thu Aug 15 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.0.1-alt1.git3b1e996
- Initial build for ALT.
