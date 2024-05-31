%define sover 8
%def_enable check

%define stdxx 17

Name: libphonenumber
Version: 8.13.38
Release: alt1

Summary: Library to handle international phone numbers
License: Apache-2.0 and BSD-3-Clause and MIT
Group: System/Libraries
Url: https://github.com/google/libphonenumber

Vcs: https://github.com/google/libphonenumber.git
Source: %url/archive/v%version/%name-%version.tar.gz
# link libgeocoding against libphonenumber
Patch1: %name-8.13.4-alt-link.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: boost-devel
BuildRequires: libicu-devel
BuildRequires: protobuf-compiler
BuildRequires: libprotobuf-devel
# required libabseil-cpp built with -DCMAKE_POSITION_INDEPENDENT_CODE=ON
BuildRequires: libabseil-cpp-devel >= 20211102.0-alt3
BuildRequires: /proc /usr/bin/java
#BuildRequires: /usr/bin/mvn junit mockito
%{?_enable_check:BuildRequires: ctest libgtest-devel}

%description
Google's common C++ library for parsing, formatting, storing and validating
international phone numbers.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -n %name-%version/cpp
%patch1 -b .link

%ifarch %e2k
# the problematic warning actually sits in protobuf (-Winvalid-offsetof)
sed -i 's/-Werror/-Wno-error/g' {,../tools/cpp/}CMakeLists.txt
%endif

# gtest > 1.13 requires >= C++14
sed -i 's|\(CMAKE_CXX_STANDARD \)11|\1%stdxx|' ../tools/cpp/CMakeLists.txt

%build
# libabseil compiled with -std=gnu++17
%cmake \
    -DCMAKE_CXX_STANDARD=%stdxx \
    %{?_disable_check:-DBUILD_TESTING=OFF} \
    -DBUILD_SHARED_LIBS=ON
%nil
%cmake_build

%install
%cmake_install
rm -f %buildroot%_libdir/*.a

%check
%cmake_build -t tests

%files
%_libdir/%name.so.%{sover}*
%_libdir/libgeocoding.so.%{sover}*
%doc README

%files devel
%_includedir/phonenumbers/
%_libdir/libgeocoding.so
%_libdir/%name.so
%_libdir/cmake/%name/

%changelog
* Fri May 31 2024 Yuri N. Sedunov <aris@altlinux.org> 8.13.38-alt1
- 8.13.38

* Thu May 16 2024 Yuri N. Sedunov <aris@altlinux.org> 8.13.37-alt1
- 8.13.37

* Thu May 02 2024 Yuri N. Sedunov <aris@altlinux.org> 8.13.36-alt1
- 8.13.36

* Fri Apr 19 2024 Yuri N. Sedunov <aris@altlinux.org> 8.13.35-alt1
- 8.13.35

* Wed Apr 03 2024 Yuri N. Sedunov <aris@altlinux.org> 8.13.34-alt1
- 8.13.34

* Fri Mar 22 2024 Yuri N. Sedunov <aris@altlinux.org> 8.13.33-alt1
- 8.13.33

* Sat Mar 09 2024 Yuri N. Sedunov <aris@altlinux.org> 8.13.32-alt1
- 8.13.32

* Fri Mar 01 2024 Yuri N. Sedunov <aris@altlinux.org> 8.13.31-alt1.1
- E2K: ftbfs workaround (ilyakurdyukov@)

* Sat Feb 24 2024 Yuri N. Sedunov <aris@altlinux.org> 8.13.31-alt1
- 8.13.31

* Fri Feb 09 2024 Yuri N. Sedunov <aris@altlinux.org> 8.13.30-alt1
- 8.13.30

* Fri Jan 26 2024 Yuri N. Sedunov <aris@altlinux.org> 8.13.29-alt1
- 8.13.29

* Sun Jan 14 2024 Yuri N. Sedunov <aris@altlinux.org> 8.13.28-alt1
- 8.13.28

* Thu Dec 07 2023 Yuri N. Sedunov <aris@altlinux.org> 8.13.27-alt1
- 8.13.27

* Thu Nov 23 2023 Yuri N. Sedunov <aris@altlinux.org> 8.13.26-alt1
- 8.13.26

* Thu Nov 09 2023 Yuri N. Sedunov <aris@altlinux.org> 8.13.25-alt1
- 8.13.25

* Sat Oct 28 2023 Yuri N. Sedunov <aris@altlinux.org> 8.13.24-alt1
- 8.13.24

* Fri Sep 29 2023 Yuri N. Sedunov <aris@altlinux.org> 8.13.22-alt1
- 8.13.22

* Wed Sep 20 2023 Yuri N. Sedunov <aris@altlinux.org> 8.13.21-alt1
- 8.13.21

* Fri Sep 01 2023 Yuri N. Sedunov <aris@altlinux.org> 8.13.20-alt1
- 8.13.20

* Sat Aug 19 2023 Yuri N. Sedunov <aris@altlinux.org> 8.13.19-alt1
- 8.13.19

* Thu Aug 03 2023 Yuri N. Sedunov <aris@altlinux.org> 8.13.18-alt1
- 8.13.18

* Thu Jul 20 2023 Yuri N. Sedunov <aris@altlinux.org> 8.13.17-alt1
- 8.13.17

* Sat Jul 08 2023 Yuri N. Sedunov <aris@altlinux.org> 8.13.16-alt1
- 8.13.16

* Thu Jun 22 2023 Yuri N. Sedunov <aris@altlinux.org> 8.13.15-alt1
- 8.13.15

* Sun Jun 11 2023 Yuri N. Sedunov <aris@altlinux.org> 8.13.14-alt1
- 8.13.14

* Sat May 27 2023 Yuri N. Sedunov <aris@altlinux.org> 8.13.13-alt1
- 8.13.13

* Fri May 12 2023 Yuri N. Sedunov <aris@altlinux.org> 8.13.12-alt1
- 8.13.12

* Thu Apr 27 2023 Yuri N. Sedunov <aris@altlinux.org> 8.13.11-alt1
- 8.13.11

* Tue Apr 18 2023 Yuri N. Sedunov <aris@altlinux.org> 8.13.10-alt1
- 8.13.10

* Thu Mar 30 2023 Yuri N. Sedunov <aris@altlinux.org> 8.13.9-alt1
- 8.13.9

* Wed Mar 22 2023 Yuri N. Sedunov <aris@altlinux.org> 8.13.8-alt1
- 8.13.8

* Fri Feb 24 2023 Yuri N. Sedunov <aris@altlinux.org> 8.13.7-alt1
- 8.13.7

* Wed Feb 08 2023 Yuri N. Sedunov <aris@altlinux.org> 8.13.6-alt1
- 8.13.6

* Mon Jan 09 2023 Yuri N. Sedunov <aris@altlinux.org> 8.13.4-alt1
- 8.13.4

* Fri Dec 23 2022 Yuri N. Sedunov <aris@altlinux.org> 8.13.3-alt1
- 8.13.3

* Thu Dec 08 2022 Yuri N. Sedunov <aris@altlinux.org> 8.13.2-alt1
- 8.13.2

* Sat Nov 19 2022 Yuri N. Sedunov <aris@altlinux.org> 8.13.1-alt1
- 8.13.1

* Sun Nov 13 2022 Yuri N. Sedunov <aris@altlinux.org> 8.13.0-alt1
- 8.13.0

* Wed Oct 12 2022 Yuri N. Sedunov <aris@altlinux.org> 8.12.57-alt1
- 8.12.57

* Sat Sep 10 2022 Yuri N. Sedunov <aris@altlinux.org> 8.12.55-alt1
- 8.12.55

* Tue Aug 30 2022 Yuri N. Sedunov <aris@altlinux.org> 8.12.54-alt1
- first build for Sisyphus



