%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: omath
Version: 5.5.1
Release: alt1

Summary: OMath is an independent, constexpr template framework.
License: ZLib
Group: System/Libraries

Url: https://github.com/orange-cpp/omath
Vcs: https://github.com/orange-cpp/omath
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: ninja-build

%description
A library for constructing allocators and memory pools. It also contains
broadly useful abstractions and utilities for memory management. UMF allows
users to manage multiple memory pools characterized by different attributes,
allowing certain allocation types to be isolated from others and allocated
using different hardware resources as required.

%package devel
Summary: Development files for omath
Group: Development/C++
Requires: %name = %EVR

%description devel
A library for constructing allocators and memory pools. It also contains
broadly useful abstractions and utilities for memory management. UMF allows
users to manage multiple memory pools characterized by different attributes,
allowing certain allocation types to be isolated from others and allocated
using different hardware resources as required.

%prep
%setup
%cmake \
	--preset linux-release \
	-DOMATH_BUILD_AS_SHARED_LIBRARY=ON

%build
%cmake_build

%install
%cmake_install

%files
%_libexecdir/libomath.so

%files devel
%_includedir/%name/
%_libexecdir/cmake/%name/

%changelog
* Tue Aug 04 2026 Pavel Mitrofanov <cobalt@altlinux.org> 5.5.1-alt1
- Initial build.