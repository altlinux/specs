%define _unpackaged_files_terminate_build 1
%define soversion %version

Name: xlnt
Version: 1.6.1
Release: alt1

Summary: Cross-platform C++ library for reading and writing XLSX files
License: MIT and BSD-3-Clause
Group: System/Libraries
Url: https://xlnt-community.gitbook.io/xlnt/
VCS: https://github.com/xlnt-community/xlnt.git

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: ctest
BuildRequires: gcc-c++
BuildRequires: pkgconfig
BuildRequires: libstudxml-devel
BuildRequires: libfmt-devel
BuildRequires: libutfcpp-devel
BuildRequires: libfast_float-devel
BuildRequires: zlib-devel
BuildRequires: libssl-devel

%description
Xlnt is a modern C++ library for manipulating spreadsheets in memory and
reading and writing XLSX files as described in ECMA-376.

%package -n libxlnt%soversion
Summary: Xlnt shared library
Group: System/Libraries

%description -n libxlnt%soversion
Xlnt is a modern C++ library for manipulating spreadsheets in memory and
reading and writing XLSX files as described in ECMA-376.

%package devel
Summary: Development files for xlnt
Group: Development/C++
Requires: libxlnt%soversion = %EVR

%description devel
This package contains the headers, shared library symlink, CMake config and
pkg-config file required to develop applications with xlnt.

%prep
%setup
%autopatch -p1
# Fail closed if an upstream dependency copy reappears.
test ! -d third-party

%build
%cmake \
  -DXLNT_USE_SYSTEM_LIBS:BOOL=ON \
  -DSTATIC:BOOL=OFF \
  -DTESTS:BOOL=ON \
  -DXLNT_SKIP_INTERNAL_TESTS:BOOL=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files -n libxlnt%soversion
%doc LICENSE.md
%_libdir/libxlnt.so.%soversion

%files devel
%_includedir/xlnt/
%_libdir/libxlnt.so
%_cmakedir/xlnt/
%_pkgconfigdir/xlnt.pc
%_man3dir/xlnt.3*

%changelog
* Tue Nov 10 2026 Ajrat Makhmutov <rauty@altlinux.org> 1.6.1-alt1
- Initial build for ALT Sisyphus.
- Fix installation paths in pkg-config metadata.
- Use system libraries instead of bundled dependencies.
- Use OpenSSL for AES and SHA instead of copied implementations.
