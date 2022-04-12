%define _unpackaged_files_terminate_build 1

Name: clickhouse-cpp
Version: 1.2.2
Release: alt2
Summary: ClickHouse C++ client library
Group: System/Libraries
License: Apache-2.0
Url: https://github.com/artpaul/clickhouse-cpp

# https://github.com/artpaul/clickhouse-cpp.git
Source: %name-%version.tar
Source1: %name.watch

Patch1: %name-alt-build.patch

BuildRequires: gcc-c++ cmake
BuildRequires: liblz4-devel
BuildRequires: libcityhash-devel

%description
C++ client for Yandex ClickHouse.
Supported data types:
- Array(T)
- Date
- DateTime
- Enum8, Enum16
- FixedString(N)
- Float32, Float64
- Nullable(T)
- String
- Tuple
- UInt8, UInt16, UInt32, UInt64, Int8, Int16, Int32, Int64

%package -n lib%name
Summary: ClickHouse C++ client library
Group: System/Libraries

%description -n lib%name
C++ client for Yandex ClickHouse.
Supported data types:
- Array(T)
- Date
- DateTime
- Enum8, Enum16
- FixedString(N)
- Float32, Float64
- Nullable(T)
- String
- Tuple
- UInt8, UInt16, UInt32, UInt64, Int8, Int16, Int32, Int64

%package -n lib%name-devel
Summary: Development files for ClickHouse C++ client library
Group: Development/C++
Requires: lib%name = %EVR
Conflicts: libabseil-cpp-devel

%description -n lib%name-devel
C++ client for Yandex ClickHouse.
Supported data types:
- Array(T)
- Date
- DateTime
- Enum8, Enum16
- FixedString(N)
- Float32, Float64
- Nullable(T)
- String
- Tuple
- UInt8, UInt16, UInt32, UInt64, Int8, Int16, Int32, Int64

This package contains development files.

%prep
%setup
%patch1 -p1

# ensure 3rd-party bundled libraries are not used
rm -rf contrib/{cityhash,gtest,lz4}

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files -n lib%name
%doc LICENSE
%doc README.md
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/%name
%_includedir/absl
%_libdir/*.so

%changelog
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
