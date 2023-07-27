%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

# TODO: nobody knowns how to run tests

%global optflags_lto %optflags_lto -ffat-lto-objects

Name: catch
Version: 3.4.0
Release: alt1
# src package `catch' version `3.4.0-alt1' is less than its version `v1.6.0-alt1' in sisyphus/task/archive/_172/176589
Epoch: 3

Summary: C++ Unit Test framework ("all in one header")

License: BSL-1.0
Group: Development/C++
Url: https://github.com/catchorg/Catch2

Packager: Pavel Vainerman <pv@altlinux.ru>

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++

BuildRequires: ctest python3

# Source-url: https://github.com/catchorg/Catch2/archive/v%{version}.tar.gz
Source: %name-%version.tar

%description
Catch stands for C++ Automated Test Cases in Headers 
and is a multi-paradigm automated 
test framework for C++ and Objective-C (and, maybe, C). 
It is implemented entirely in a set of header files, 
but is packaged up as a single header for extra convenience.

%package -n catch-devel
Summary: C++ Unit Test framework ("all in one header")
Group: Development/C++
Conflicts: catch2-devel
# fix unowned files
Requires: cmake

%description -n catch-devel
Catch stands for C++ Automated Test Cases in Headers 
and is a multi-paradigm automated 
test framework for C++ and Objective-C (and, maybe, C). 
It is implemented entirely in a set of header files, 
but is packaged up as a single header for extra convenience.

%prep
%setup

%build
%cmake \
    -DCATCH_BUILD_EXTRA_TESTS=ON \
    -DCATCH_ENABLE_WERROR=OFF \
    -DBUILD_SHARED_LIBS=OFF \
    -DBUILD_TESTING=ON
%cmake_build

%install
%cmake_install
# NEW duplicate provides detected:
#  pkgconfig(catch2)  catch-devel catch2-devel
mv %buildroot%_datadir/pkgconfig/catch2.pc %buildroot%_datadir/pkgconfig/catch3.pc
subst 's|catch2|catch3|' %buildroot%_datadir/pkgconfig/catch2-with-main.pc

%check
# TODO: No tests were found!!!
%ctest

%files -n catch-devel
%doc %_docdir/Catch2/
%_includedir/catch2/
%_libdir/libCatch2.a
%_libdir/libCatch2Main.a
%_datadir/Catch2/
%_libdir/cmake/Catch2/
%_datadir/pkgconfig/catch3.pc
%_datadir/pkgconfig/catch2-with-main.pc

%changelog
* Thu Jul 27 2023 Vitaly Lipatov <lav@altlinux.ru> 3:3.4.0-alt1
- new version 3.4.0 (with rpmrb script)
- patch catch2.pc as catch3.pc

* Thu Jul 27 2023 Vitaly Lipatov <lav@altlinux.ru> 3.3.2-alt2
- build as catch-devel from new source package

* Sun May 28 2023 Nazarov Denis <nenderus@altlinux.org> 3.3.2-alt1
- new version (3.3.2) with rpmgs script

* Sat Oct 16 2021 Pavel Vainerman <pv@altlinux.ru> 2.13.7-alt1
- new version (2.13.7) with rpmgs script

* Thu Sep 09 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.13.4-alt2
- Fixed build with LTO.

* Tue Apr 27 2021 Arseny Maslennikov <arseny@altlinux.org> 2.13.4-alt1.1
- NMU: spec: adapted to new cmake macros.

* Wed Mar 10 2021 Nazarov Denis <nenderus@altlinux.org> 2.13.4-alt1
- new version 2.13.4

* Sun Jan 26 2020 Vitaly Lipatov <lav@altlinux.ru> 2.11.1-alt1
- new version 2.11.1 (with rpmrb script)

* Sun Jan 26 2020 Vitaly Lipatov <lav@altlinux.ru> 2.11.0-alt2
- fix cmake files placement

* Mon Nov 18 2019 Pavel Vainerman <pv@altlinux.ru> 2.11.0-alt1
- new version (2.11.0) with rpmgs script

* Sun Jun 10 2018 Vitaly Lipatov <lav@altlinux.ru> 2.2.2-alt2
- build with cmake, pack cmake modules and pkgconfig

* Sun Jun 03 2018 Pavel Vainerman <pv@altlinux.ru> 2.2.2-alt1
- new version (2.2.2) with rpmgs script
