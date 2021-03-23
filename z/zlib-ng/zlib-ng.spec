Name: zlib-ng
Version: 2.0.2
Release: alt1

Summary: Zlib replacement with optimizations
License: Zlib
Group: System/Libraries

Url: https://github.com/%name/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

ExcludeArch: armh

# https://github.com/%name/%name/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar

BuildRequires: ctest

%description
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

%build
%cmake -DCMAKE_SKIP_RPATH:BOOL=OFF
%cmake_build

%install
%cmakeinstall_std

%check
%make -C BUILD test

%files
%doc FAQ.zlib PORTING.md README.md doc/*.txt
%_libdir/libz-ng.so.*

%files devel
%_includedir/*.h
%_libdir/libz-ng.so
%_pkgconfigdir/%name.pc

%files devel-static
%_libdir/libz-ng.a

%changelog
* Tue Mar 23 2021 Nazarov Denis <nenderus@altlinux.org> 2.0.2-alt1
- Version 2.0.2

* Thu Mar 18 2021 Nazarov Denis <nenderus@altlinux.org> 2.0.1-alt1
- Initial build for ALT Linux
