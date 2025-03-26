Name: libsdbus-cpp
Version: 1.6.0
Release: alt3

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
Provides: pkgconfig(sdbus-c++) = %version
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

#install alternative
mv %buildroot/%_pkgconfigdir/sdbus-c++{,-1}.pc
install -d %buildroot/%_sysconfdir/alternatives/packages.d/
cat > %buildroot/%_sysconfdir/alternatives/packages.d/%name-devel <<__EOF__
%_pkgconfigdir/sdbus-c++.pc %_pkgconfigdir/sdbus-c++-1.pc %version
__EOF__

%files
%_libdir/*.so.*

%files devel
%doc %_defaultdocdir/sdbus-c++/*
%config %_sysconfdir/alternatives/packages.d/%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/cmake/*
%_pkgconfigdir/*.pc

%changelog
* Wed Mar 26 2025 Sergey V Turchin <zerg@altlinux.org> 1.6.0-alt3
- put pkgconfig-file on alternatives

* Mon Mar 24 2025 Kirill Unitsaev <fiersik@altlinux.org> 1.6.0-alt2
- devel: rename pkg-config file
- devel: pack docs

* Tue Nov 19 2024 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Fri Oct 20 2023 Valery Inozemtsev <shrek@altlinux.ru> 1.4.0-alt1
- initial release
