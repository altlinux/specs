Name: libwaylandpp
Version: 1.0.0
Release: alt1

Summary: C++ bindings for Wayland
License: BSD-2-Clause
Group: System/Libraries
Url: https://github.com/NilsBrause/waylandpp/

Source: %name-%version-%release.tar

BuildRequires: cmake gcc-c++ libglvnd-devel
BuildRequires: pkgconfig(pugixml)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(wayland-server)

%package devel
Summary: C++ bindings for Wayland
Group: Development/C++

%description
%summary

%description devel
%summary
This package contains development part of waylandpp

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%set_verify_elf_method relaxed

%files
%_libdir/libwayland-*++.so.*

%files devel
%_bindir/wayland-scanner++
%_libdir/libwayland-*++.so
%_libdir/cmake/waylandpp
%_pkgconfigdir/wayland-*++.pc
%_includedir/*.hpp
%_datadir/waylandpp

%changelog
* Wed May 04 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.0-alt1
- 1.0.0 released

* Mon Feb 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.9-alt1
- 0.2.9 released

* Tue Nov 10 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.8-alt1
- initial
