Name: streamvbyte
Version: 1.0.0
Release: alt1

Summary: Fast integer compression in C using the StreamVByte codec

License: Apache-2.0
Group: Development/C
Url: https://github.com/lemire/streamvbyte

# Source-url: https://github.com/lemire/streamvbyte/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
# CMakeLists.txt from manticoresoftware/columnar (adds cmake export/find_package support)
Source1: CMakeLists.txt

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake >= 3.17
BuildRequires: gcc gcc-c++

%description
StreamVByte is a integer compression technique that applies SIMD
instructions (vectorization) to Google's Group Varint approach.

%package -n lib%name-devel-static
Summary: Static library and headers for streamvbyte
Group: Development/C

%description -n lib%name-devel-static
Static library, header files and CMake configuration for streamvbyte.

%prep
%setup
cp %SOURCE1 CMakeLists.txt
# Fix install destination - remove generator expression, use correct libdir
subst 's|"lib/$<CONFIG>"|"%_lib"|g' CMakeLists.txt
subst 's|"lib/cmake/streamvbyte"|"%_lib/cmake/streamvbyte"|g' CMakeLists.txt

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%build
%ifarch x86_64 %ix86
%cmake -DCMAKE_C_FLAGS="%optflags -msse4.1"
%else
%cmake
%endif
%cmake_build

%install
%cmake_install

%files -n lib%name-devel-static
%doc LICENSE
%_includedir/streamvbyte*.h
%_libdir/libstreamvbyte.a
%_cmakedir/streamvbyte/

%changelog
* Tue Mar 31 2026 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Sisyphus

