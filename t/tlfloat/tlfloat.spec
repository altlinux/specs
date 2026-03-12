%define _unpackaged_files_terminate_build 1
%define optflags_lto %nil

%define abiversion 1

Name:    tlfloat
Version: 1.15.0
Release: alt2

Summary: C++ template library for floating point operations
License: BSL-1.0 AND CC-BY-SA-4.0
Group:   System/Libraries
Url:     https://shibatch.github.io/tlfloat-doxygen
Vcs:     https://github.com/shibatch/tlfloat

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build
%ifarch x86_64
BuildRequires: libquadmath-devel
%endif
BuildRequires: libmpfr-devel

%description
This library implements C++ classes with which half, single, double, quadruple
and octuple precision IEEE 754 floating point numbers can be operated.

Internally, these classes are implemented as class templates on top of
arbitrary-precision integer class templates so that the templates are expanded
as arbitrary precision floating-point operations by just changing the template
parameters, rather than implementing each floating-point operation for each
precision. The arbitrary-precision integer class templates are also included in
this library.

%package -n lib%name%abiversion
Summary: %summary
Group: System/Libraries

%description -n lib%name%abiversion
This library implements C++ classes with which half, single, double, quadruple
and octuple precision IEEE 754 floating point numbers can be operated.

Internally, these classes are implemented as class templates on top of
arbitrary-precision integer class templates so that the templates are expanded
as arbitrary precision floating-point operations by just changing the template
parameters, rather than implementing each floating-point operation for each
precision. The arbitrary-precision integer class templates are also included in
this library.

%package -n lib%name-devel
Summary: Development files for TLFloat
Group: Development/C++
Requires: lib%name%abiversion = %EVR

%description -n lib%name-devel 
The tlfloat-devel package contains libraries and header files for
developing applications that use TLFloat.

%prep
%setup

# Fix include directory in pkgconfig file
sed -i 's|^Cflags: -I${includedir}$|Cflags: -I${includedir}/tlfloat|' src/tlfloat/tlfloat.pc.in


%build
%cmake \
  -GNinja \
  -DBUILD_UTILS:BOOL=FALSE \
  -DBUILD_SHARED_LIBS=ON \
  -DCMAKE_POSITION_INDEPENDENT_CODE=ON
%cmake_build

%install
%cmake_install

%files -n lib%name%abiversion
%doc README.adoc LICENSE.txt
%_libdir/lib%name.so.%{abiversion}*

%files -n lib%name-devel
%_includedir/tlfloat/
%_libdir/lib%name.so
%_pkgconfigdir/tlfloat.pc

%changelog
* Tue Mar 10 2026 Nikita Shmatko <nash@altlinux.org> 1.15.0-alt2
- Minor specfile fixes.
- Fixed ABI versioning.

* Thu Aug 28 2025 Nikita Shmatko <nash@altlinux.org> 1.15.0-alt1
- Initial build for Sisyphus.
