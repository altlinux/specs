%define sover 8
%def_enable check

Name: libphonenumber
Version: 8.13.4
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
BuildRequires: /usr/bin/java /proc
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

%build
# libabseil compiled with -std=gnu++17
%cmake \
    -DCMAKE_CXX_STANDARD=17 \
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



