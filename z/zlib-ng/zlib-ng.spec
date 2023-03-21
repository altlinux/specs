%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%define soversion 2

Name: zlib-ng
Version: 2.0.7
Release: alt1

Summary: Zlib replacement with optimizations
License: Zlib
Group: System/Libraries

Url: https://github.com/%name/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/%name/%name/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar
Patch2000: %name-e2k-simd.patch

BuildRequires: ctest

%description
%name is a zlib replacement that provides optimizations for "next generation"
systems.

%package -n libz-ng%soversion
Summary: Zlib replacement with optimizations
Group: System/Libraries
Provides: %name = %EVR
Obsoletes: %name <= 2.0.5-alt1.1

%description -n libz-ng%soversion
%name is a zlib replacement that provides optimizations for "next generation"
systems.

%package devel
Summary: Development files for %name
Group: Development/C

%description devel
The %name-devel package contains development files for
developing application that use %name.

%package devel-static
Summary: Static library for %name
Group: Development/C
Requires: %name-devel = %EVR

%description devel-static
The %name-devel package contains static library for
developing application that use %name.

%prep
%setup
%ifarch %e2k
%patch2000 -p1
%endif

%build
%ifarch %arm
%remove_optflags %optflags_lto
%endif

%cmake -DCMAKE_SKIP_RPATH:BOOL=OFF
%cmake_build

%install
%cmake_install

%check
%make -C %_cmake__builddir test

%files -n libz-ng%soversion
%doc FAQ.zlib PORTING.md README.md doc/*.txt
%_libdir/libz-ng.so.*

%files devel
%_includedir/*.h
%_libdir/libz-ng.so
%_pkgconfigdir/%name.pc

%files devel-static
%_libdir/libz-ng.a

%changelog
* Tue Mar 21 2023 Nazarov Denis <nenderus@altlinux.org> 2.0.7-alt1
- Version 2.0.7

* Sat Dec 25 2021 Nazarov Denis <nenderus@altlinux.org> 2.0.6-alt1
- Version 2.0.6
- Rename library subpackage

* Wed Aug 25 2021 Nazarov Denis <nenderus@altlinux.org> 2.0.5-alt1.1
- Fix LTO

* Sat Jun 26 2021 Nazarov Denis <nenderus@altlinux.org> 2.0.5-alt1
- Version 2.0.5

* Sat Jun 12 2021 Nazarov Denis <nenderus@altlinux.org> 2.0.4-alt1
- Version 2.0.4

* Wed Jun 09 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2.0.3-alt2
- added SIMD patch for Elbrus

* Mon May 31 2021 Nazarov Denis <nenderus@altlinux.org> 2.0.3-alt1.1
- Adapted to new cmake macros

* Thu May 13 2021 Nazarov Denis <nenderus@altlinux.org> 2.0.3-alt1
- Version 2.0.3

* Tue Mar 23 2021 Nazarov Denis <nenderus@altlinux.org> 2.0.2-alt1
- Version 2.0.2

* Thu Mar 18 2021 Nazarov Denis <nenderus@altlinux.org> 2.0.1-alt1
- Initial build for ALT Linux
