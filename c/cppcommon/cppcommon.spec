%define _unpackaged_files_terminate_build 1
%define soversion 1

Name: cppcommon
Version: 1.0.6.0
Release: alt1

Summary: C++ library of reusable components
License: MIT
Group: Development/C++
Url: https://github.com/chronoxor/CppCommon
VCS: https://github.com/chronoxor/CppCommon.git

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-cmake
BuildRequires: gcc-c++
BuildRequires: libfmt-devel
BuildRequires: libuuid-devel

%description
CppCommon is a C++ library of reusable components for error handling,
filesystem operations, string formatting and encoding, threading,
synchronization, shared memory and time management.

%package -n libcppcommon%soversion
Summary: CppCommon shared library
Group: System/Libraries

%description -n libcppcommon%soversion
CppCommon is a C++ library of reusable components for error handling,
filesystem operations, string formatting and encoding, threading,
synchronization, shared memory and time management.

This package contains the shared runtime library.

%package -n libcppcommon-devel
Summary: Development files for CppCommon
Group: Development/C++
Requires: libcppcommon%soversion = %EVR

%description -n libcppcommon-devel
This package contains the headers, linker symlink and pkg-config metadata
needed to develop applications using CppCommon.

%prep
%setup
%autopatch -p1

%build
%cmake -DCPPCOMMON_SYSTEM_DEPENDENCIES=ON
%cmake_build

%install
%cmake_install

%files -n libcppcommon%soversion
%doc LICENSE
%_libdir/libcppcommon.so.%soversion
%_libdir/libcppcommon.so.%soversion.*

%files -n libcppcommon-devel
%doc README.md
%_includedir/cppcommon/
%_libdir/libcppcommon.so
%_pkgconfigdir/cppcommon.pc

%changelog
* Tue Nov 10 2026 Ajrat Makhmutov <rauty@altlinux.org> 1.0.6.0-alt1
- First build for ALT.
