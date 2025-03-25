Name: libsdbus-cpp
Version: 1.6.0
Release: alt2

Summary: A C++ bindings for libdbus
License: LGPLv2.1
Group: System/Libraries
Url: https://github.com/Kistler-Group/sdbus-cpp.git
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
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
%setup
%patch -p1

%build
%cmake

%cmake_build

%install
%cmake_install
mv %buildroot%_pkgconfigdir/sdbus-c++{,-1}.pc

%files
%_libdir/*.so.*

%files devel
%doc %_defaultdocdir/sdbus-c++/*
%_includedir/*
%_libdir/*.so
%_libdir/cmake/*
%_pkgconfigdir/*.pc

%changelog
* Mon Mar 24 2025 Kirill Unitsaev <fiersik@altlinux.org> 1.6.0-alt2
- devel: rename pkg-config file
- devel: pack docs

* Tue Nov 19 2024 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Fri Oct 20 2023 Valery Inozemtsev <shrek@altlinux.ru> 1.4.0-alt1
- initial release
