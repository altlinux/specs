Name: libsdbus-cpp
Version: 1.4.0
Release: alt1
Summary: A C++ bindings for libdbus
License: LGPLv2.1
Group: System/Libraries
Url: https://github.com/Kistler-Group/sdbus-cpp.git
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: cmake gcc-c++ libsystemd-devel

%description
sdbus-c++ is a high-level C++ D-Bus library for Linux designed to provide expressive,
easy-to-use API in modern C++. It adds another layer of abstraction on top of sd-bus,
a nice, fresh C D-Bus implementation by systemd.

%package devel
Group: Development/C++
Summary:  Development libraries for %name

%description devel
Development libraries for %name

%prep
%setup -q
%patch -p1

%build
%cmake

%cmake_build

%install
%cmake_install

%files
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/cmake/*
%_pkgconfigdir/*.pc

%changelog
* Fri Oct 20 2023 Valery Inozemtsev <shrek@altlinux.ru> 1.4.0-alt1
- initial release
