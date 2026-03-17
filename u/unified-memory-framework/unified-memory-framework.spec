%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%define soname 0
%set_verify_elf_method strict

Name: unified-memory-framework
Version: 1.0.3
Release: alt1

Summary: The Unified Memory Framework (UMF) is a library for constructing allocators and memory pools
License: Apache-2.0
Group: Development/C++

Url: https://oneapi-src.github.io/unified-memory-framework/
Vcs: https://github.com/oneapi-src/unified-memory-framework.git
Source: %name-%version.tar

ExclusiveArch: x86_64

BuildRequires: gcc-c++
BuildRequires(pre): cmake
BuildRequires: libze-devel libtbb-devel libhwloc-devel

%description
A library for constructing allocators and memory pools. It also contains
broadly useful abstractions and utilities for memory management. UMF allows
users to manage multiple memory pools characterized by different attributes,
allowing certain allocation types to be isolated from others and allocated
using different hardware resources as required.

%package -n libumf%soname
Summary: UMF shared library
Group: System/Libraries
Provides: libumf = %EVR

%description -n libumf%soname
UMF shared library

%package -n libumf-devel
Summary: UMF development headers and libraries
Group: Development/C++
Requires: libumf = %EVR

%description -n libumf-devel
UMF development headers and libraries

%prep
%setup

%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DUMF_BUILD_SHARED_LIBRARY=ON \
	-DUMF_USE_FETCH_CONTENT=OFF \
	-DUMF_LEVEL_ZERO_INCLUDE_DIR=%_includedir/level_zero \
	-DUMF_BUILD_CUDA_PROVIDER=OFF \
	-DUMF_BUILD_TESTS=OFF \
	-DUMF_BUILD_EXAMPLES=OFF

%build
%cmake_build

%install
%cmake_install
rm -rf %buildroot%_docdir/umf

%files -n libumf%soname
%doc LICENSE.TXT README.md security.md
%_libdir/libumf.so.*
%_libdir/libumf_proxy.so.*

%files -n libumf-devel
%doc examples
%_includedir/umf.h
%_includedir/umf
%_libdir/libumf.so
%_libdir/libumf_proxy.so
%_libdir/cmake/umf

%changelog
* Sat Mar 14 2026 L.A. Kostis <lakostis@altlinux.ru> 1.0.3-alt1
- 1.0.3.

* Thu Jun 19 2025 L.A. Kostis <lakostis@altlinux.ru> 0.11.2-alt1
- 0.11.2.

* Thu May 01 2025 L.A. Kostis <lakostis@altlinux.ru> 0.11.0-alt1
- 0.11.0.
- Fix ze_loader name.

* Tue Apr 29 2025 L.A. Kostis <lakostis@altlinux.ru> 0.10.0-alt1
- Initial build for ALTLinux.
