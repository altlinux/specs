%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%define soversion 2

Name: zlib-ng
Version: 2.2.1
Release: alt1.1

Summary: Zlib replacement with optimizations
Summary(ru_RU.UTF-8): Замена Zlib с оптимизацией
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
Summary(ru_RU.UTF-8): Замена Zlib с оптимизацией
Group: System/Libraries
Provides: %name = %EVR
Obsoletes: %name <= 2.0.5-alt1.1

%description -n libz-ng%soversion
%name is a zlib replacement that provides optimizations for "next generation"
systems.

%description -l ru_RU.UTF-8 -n libz-ng%soversion
%name — это замена zlib, обеспечивающая оптимизацию
для систем «следующего поколения».

%package devel
Summary: Development files for %name
Summary(ru_RU.UTF-8): Файлы разработки для %name
Group: Development/C

%description devel
The %name-devel package contains development files for
developing application that use %name.

%description -l ru_RU.UTF-8 devel
Пакет %name-devel содержит файлы для
разработки приложений, использующих %name.

%package devel-static
Summary: Static library for %name
Summary(ru_RU.UTF-8): Статическая библиотека для %name
Group: Development/C
Requires: %name-devel = %EVR

%description devel-static
The %name-devel package contains static library for
developing application that use %name.

%description -l ru_RU.UTF-8 devel-static
Пакет %name-devel содержит статическую библиотеку для
разработки приложений, использующих %name.

%prep
%setup
%ifarch %e2k
%patch2000 -p1
%endif

%build
%ifarch %arm
%remove_optflags %optflags_lto
%endif

%cmake \
	-DCMAKE_SKIP_RPATH:BOOL=OFF \
	-DWITH_GTEST:BOOL=OFF \
%ifarch aarch64
	-DWITH_ARMV6:BOOL=OFF \
%endif

%cmake_build

%install
%cmake_install

%check
%ctest

%files -n libz-ng%soversion
%doc FAQ.zlib PORTING.md README.md doc/*.txt
%_libdir/libz-ng.so.*

%files devel
%_includedir/*.h
%_libdir/libz-ng.so
%_libdir/cmake/%name
%_pkgconfigdir/%name.pc

%files devel-static
%_libdir/libz-ng.a

%changelog
* Sat Jul 06 2024 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2.2.1-alt1.1
- e2k patch update

* Tue Jul 02 2024 Nazarov Denis <nenderus@altlinux.org> 2.2.1-alt1
- New version 2.2.1.

* Wed Jun 19 2024 Nazarov Denis <nenderus@altlinux.org> 2.2.0-alt1
- New version 2.2.0.

* Thu Jan 25 2024 Nazarov Denis <nenderus@altlinux.org> 2.1.6-alt1
- New version 2.1.6.

* Wed Nov 29 2023 Nazarov Denis <nenderus@altlinux.org> 2.1.5-alt1
- New version 2.1.5.

* Sun Oct 22 2023 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2.1.4-alt1.1
- e2k patch update

* Thu Oct 19 2023 Nazarov Denis <nenderus@altlinux.org> 2.1.4-alt1
- New version 2.1.4.

* Sat Jul 01 2023 Nazarov Denis <nenderus@altlinux.org> 2.1.3-alt1
- New version 2.1.3.

* Wed Jun 21 2023 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2.1.2-alt1.1
- e2k patch update

* Fri Jun 09 2023 Nazarov Denis <nenderus@altlinux.org> 2.1.2-alt1
- Version 2.1.2

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
