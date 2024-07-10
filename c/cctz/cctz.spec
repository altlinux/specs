%define _unpackaged_files_terminate_build 1

%global soname 2

Name: cctz
Version: 2.4
Release: alt1
License: Apache-2.0
Summary: Translating between absolute and civil times using time zone rules
Group: Development/C++
Url: https://github.com/google/cctz
Source: %name-%version.tar

# https://sources.debian.org/patches/cctz/2.2+dfsg1-1/0001-Compile-shared-lib-and-install-it.patch/
Patch0: cctz-2.3-debian-compile-library-as-shared.patch

BuildRequires: tzdata
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ctest
BuildRequires: make
BuildRequires: libgtest-devel
BuildRequires: libgmock-devel
BuildRequires: libbenchmark-devel

Requires: tzdata

%description
CCTZ contains two libraries that cooperate with <chrono> to give C++
programmers all the necessary tools for computing with dates, times, and time
zones in a simple and correct manner. The libraries in CCTZ are:
  * The Civil-Time Library - This is a header-only library that supports
    computing with human-scale time, such as dates (which are represented by
    the cctz::civil_day class).
  * The Time-Zone Library - This library uses the IANA time zone database that
    is installed on the system to convert between absolute time and civil time.

%package devel
Summary: %summary
Group: Development/C++
Requires: %name = %EVR
Requires: cmake

%description devel
Development files for %name library.

%prep
%setup
%patch0 -p1

%build
%cmake -DVERSION=%version -DSOVERSION=%soname
%cmake_build

%install
%cmake_install

%check
cd %_cmake__builddir
LD_LIBRARY_PATH=./ ctest -V

%files
%doc README.md LICENSE.txt
%_bindir/time_tool
%_libdir/libcctz.so.%soname
%_libdir/libcctz.so.%version

%files devel
%doc examples
%_includedir/cctz
%_libdir/libcctz.so
%_libdir/cmake/cctz

%changelog
* Wed May 22 2024 Anton Farygin <rider@altlinux.ru> 2.4-alt1
- 2.3 -> 2.4

* Tue Jun 08 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3-alt3
- Applied changes from upstream needed by clickhouse.
- Cleaned up spec.

* Tue Apr 27 2021 Arseny Maslennikov <arseny@altlinux.org> 2.3-alt2.1
- NMU: spec: adapted to new cmake macros.

* Sat Feb 27 2021 Anton Farygin <rider@altlinux.org> 2.3-alt2
- run tests with tzdata, distributed with cctz

* Thu Jun 20 2019 Anton Farygin <rider@altlinux.ru> 2.3-alt1
- first build for ALT
