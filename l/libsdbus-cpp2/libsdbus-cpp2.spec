%define soversion 2
%define _name sdbus-c++
%define libname lib%_name

Name: libsdbus-cpp2
Version: 2.1.0
Release: alt2
License: LGPLv2.1

Summary: High-level C++ D-Bus library for Linux

Group: System/Libraries

Url: https://github.com/Kistler-Group/sdbus-cpp
Vcs: https://github.com/Kistler-Group/sdbus-cpp.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: gcc-c++ cmake
BuildRequires: pkgconfig(libsystemd)

%description
sdbus-c++ is a high-level C++ D-Bus library for Linux designed to provide expressive,
easy-to-use API in modern C++. It adds another layer of abstraction on top of sd-bus,
a nice, fresh C D-Bus implementation by systemd.

%package -n %name-devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %EVR
Conflicts: libsdbus-cpp-devel

%description -n %name-devel
This package provides development files for %name library.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

#install alternative
mv %buildroot/%_pkgconfigdir/sdbus-c++{,-2}.pc
install -d %buildroot/%_sysconfdir/alternatives/packages.d/
cat > %buildroot/%_sysconfdir/alternatives/packages.d/%name-devel <<__EOF__
%_pkgconfigdir/sdbus-c++.pc %_pkgconfigdir/sdbus-c++-2.pc %version
__EOF__

%files
%_libdir/%libname.so.%soversion
%_libdir/%libname.so.%version

%files -n %name-devel
%doc %_defaultdocdir/%_name/*
%config %_sysconfdir/alternatives/packages.d/%name-devel
%_libdir/*.so
%_pkgconfigdir/*.pc
%_includedir/%_name
%_libdir/cmake/%_name

%changelog
* Wed Mar 26 2025 Sergey V Turchin <zerg@altlinux.org> 2.1.0-alt2
- put pkgconfig-file on alternatives

* Mon Mar 24 2025 Kirill Unitsaev <fiersik@altlinux.org> 2.1.0-alt1
- Initial build
