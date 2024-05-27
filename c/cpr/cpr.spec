%define _unpackaged_files_terminate_build 1

%define libname lib%name
%define sover 1

Name: cpr
Version: 1.10.5
Release: alt1

Summary: C++ Requests: Curl for People, a spiritual port of Python Requests
License: MIT
Group: System/Libraries
Url: https://docs.libcpr.org
VCS: https://github.com/libcpr/cpr

# Source-url: https://github.com/%libname/%name/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(openssl)

%description
C++ Requests is a simple wrapper around libcurl inspired by the
excellent Python Requests project.

Despite its name, libcurl's easy interface is anything but, and making
mistakes, misusing it is a common source of error and frustration.
Using the more expressive language facilities of C++17 (or C++11 in
case you use cpr < 1.10.0), this library captures the essence of making
network calls into a few concise idioms.

%package -n %libname%sover
Summary: %summary
Group: System/Libraries

%description -n %libname%sover
C++ Requests is a simple wrapper around libcurl inspired by the
excellent Python Requests project.

Despite its name, libcurl's easy interface is anything but, and making
mistakes, misusing it is a common source of error and frustration.
Using the more expressive language facilities of C++17 (or C++11 in
case you use cpr < 1.10.0), this library captures the essence of making
network calls into a few concise idioms.

%package -n %libname-devel
Summary: Development files for the %name
Group: Development/C++
Requires: %libname%sover = %EVR

%description -n %libname-devel
The package contains libraries and header files for developing
applications that use %name.

%prep
%setup

%build
%cmake \
    -DCPR_USE_SYSTEM_CURL=ON \
    -DCMAKE_POLICY_DEFAULT_CMP0135=NEW
%cmake_build

%install
%cmake_install

%files -n %libname%sover
%doc README.md LICENSE
%_libdir/%libname.so.%{sover}*

%files -n %libname-devel
%_includedir/%name/*
%_libdir/%libname.so
%_libdir/cmake/%name/*.cmake

%changelog
* Mon May 27 2024 Dmitrii Fomchenkov <sirius@altlinux.org> 1.10.5-alt1
- Initial build for ALT Linux
