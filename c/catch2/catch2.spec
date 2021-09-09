%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%global optflags_lto %optflags_lto -ffat-lto-objects

Name: catch2
Version: 2.13.4
Release: alt2

Summary: C++ Unit Test framework ("all in one header")

License: BSL-1.0
Group: Development/C++
Url: https://github.com/catchorg/Catch2

Packager: Pavel Vainerman <pv@altlinux.ru>

BuildRequires: rpm-macros-cmake cmake gcc-c++

# run tests
BuildRequires: ctest python-modules

# Source-url: https://github.com/catchorg/Catch2/archive/v%{version}.tar.gz
Source: %name-%version.tar

%description
Catch stands for C++ Automated Test Cases in Headers 
and is a multi-paradigm automated 
test framework for C++ and Objective-C (and, maybe, C). 
It is implemented entirely in a set of header files, 
but is packaged up as a single header for extra convenience.

%package devel
Summary: C++ Unit Test framework ("all in one header")
Group: Development/C++

%description devel
Catch stands for C++ Automated Test Cases in Headers 
and is a multi-paradigm automated 
test framework for C++ and Objective-C (and, maybe, C). 
It is implemented entirely in a set of header files, 
but is packaged up as a single header for extra convenience.

%prep
%setup
%__subst "s|set(CATCH_CMAKE_CONFIG_DESTINATION .*|set(CATCH_CMAKE_CONFIG_DESTINATION "%_datadir/cmake/Catch2")|" CMakeLists.txt

%build
%cmake -DCATCH_ENABLE_WERROR=OFF -DBUILD_SHARED_LIBS=OFF
%cmake_build

%install
%cmake_install

%check
cd %_cmake__builddir
ctest -V

%files devel
%doc %_docdir/Catch2/
%dir %_includedir/catch2/
%_includedir/catch2/*.hpp
%_libdir/libCatch2WithMain.a
%_datadir/Catch2/
%_datadir/cmake/Catch2/
%_datadir/pkgconfig/catch2.pc

%changelog
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
