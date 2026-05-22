%define rname uvg266

Name: lib%rname
Version: 0.8.1
Release: alt1
Summary: An open-source VVC encoder
Group: System/Libraries
License: BSD-3-Clause
URL: https://ultravideo.fi/uvg266.html
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %rname-%version.tar.xz
Patch0: %rname-shared.patch
Patch1: %rname-pc.patch
Patch2: %rname-lm.patch

BuildRequires: cmake gcc-c++
# ctest ffmpeg

%description
Open source VVC encoder based on Kvazaar.

%package devel
Summary: Development files for %name
Group: Development/C++

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %rname.

%prep
%setup -q -n %rname-%version
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%cmake
%cmake_build

%install
%cmake_install

#check
#ctest

%files
%doc LICENSE* README.md CREDITS
%_bindir/%rname
%_libdir/*.so.*
%_man1dir/%rname.*

%files devel
%_libdir/*.so
%_pkgconfigdir/*.pc
%_includedir/*.h

%changelog
* Fri May 22 2026 Valery Inozemtsev <shrek@altlinux.ru> 0.8.1-alt1
- initial release


