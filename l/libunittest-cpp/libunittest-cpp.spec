%define _name unittest-cpp
%define ver_major 2.0
%define libname libUnitTest++
%define api_ver 2.0

Name: lib%_name
Version: %ver_major.0
Release: alt1

Summary: A lightweight unit testing framework for C++
Group: System/Libraries
License: MIT
Url: https://github.com/%_name

Source: %url/%_name/releases/download/v%version/%_name-%version.tar.gz

BuildRequires: gcc-c++

%description
UnitTest++ is a lightweight unit testing framework for C++. It was
designed to do test-driven development on a wide variety of platforms.
Simplicity, portability, speed, and small footprint are all very
important aspects of UnitTest++. UnitTest++ is mostly standard C++ and
makes minimal use of advanced library and language features, which means
it should be easily portable to just about any platform. Out of the box,
the following platforms are supported: Windows, Linux, Mac OS X.

%package devel
Summary: A lightweight unit testing framework for C++ development package
Group: Development/C++
Requires: %name = %version-%release

%description devel
This package contains development libraries and header files
that are needed to write applications that use %name.

%prep
%setup -n %_name-%version

%build
%configure --disable-static

%make_build

%install
%makeinstall_std

%check
%make check

%files
%_libdir/%libname.so.*
%doc AUTHORS

%files devel
%_includedir/UnitTest++/
%_libdir/%libname.so
%_pkgconfigdir/UnitTest++.pc


%changelog
* Fri Jan 27 2017 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1
- first build for Sisyphus

