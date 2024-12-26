%define _unpackaged_files_terminate_build 1
%define soversion 3

%def_with check

Name: date
Version: 3.0.3
Release: alt1

Summary: A date and time library based on the C++11/14/17 <chrono> header
License: BSD-2-Clause and BSL-1.0
Group: Development/C++
Url: https://github.com/HowardHinnant/date
Vcs: https://github.com/HowardHinnant/date

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: tzdata
%if_with check
BuildRequires: ctest
%endif

%description
This is actually several separate C++11/C++14/C++17 libraries:
 - "date.h" is a header-only library which builds upon <chrono>.
   It adds some new duration types, and new time_point types. It
   also adds "field" types such as year_month_day which is a
   struct {year, month, day}. And it provides convenient means
   to convert between the "field" types and the time_point types.
 - "tz.h" / "tz.cpp" are a timezone library built on top of the
   "date.h" library. This timezone library is a complete parser
   of the IANA timezone database. It provides for an easy way to
   access all of the data in this database, using the types from
   "date.h" and <chrono>. The IANA database also includes data
   on leap seconds, and this library provides utilities to compute
   with that information as well.
Slightly modified versions of "date.h" and "tz.h" were voted into
the C++20 standard.

%package devel
Summary: A date and time library based on the C++11/14/17 <chrono> header
Group: Development/C++

%description devel
%{summary devel}.

%package -n lib%name-tz%soversion
Summary: A timezone library built on top of the "date.h"
Group: System/Libraries

%description -n lib%name-tz%soversion
This timezone library is a complete parser of the IANA timezone database.
It provides for an easy way to access all of the data in this database,
using the types from "date.h" and <chrono>. The IANA database also includes data
on leap seconds, and this library provides utilities to compute with that
information as well.

%prep
%setup
%autopatch -p1

%build
%cmake \
	-DBUILD_SHARED_LIBS=ON \
	-DUSE_SYSTEM_TZ_DB=ON \
	-DBUILD_TZ_LIB=ON \
	-DCOMPILE_WITH_C_LOCALE=ON \
	-DDISABLE_STRING_VIEW=ON \
	-DHAS_REMOTE_API=0 \
%if_with check
        -DENABLE_DATE_TESTING=ON \
        -DEXCLUDED_TESTS="ptz;zoned_time;parse" \

%cmake_build --target testit
%endif
    %nil

%cmake_build

%install
%cmake_install

%check
%ctest

%files devel
%_includedir/date
%_cmakedir/date
%_libdir/libdate-tz.so

%doc README.md LICENSE.txt

%files -n lib%name-tz%soversion
%_libdir/libdate-tz.so.*

%changelog
* Tue Dec 25 2024 Artem Krasovskiy <aibure@altlinux.org> 3.0.3-alt1
- Initial build for Sisyphus

