%define soversion 2
Name: sdbus-cpp
Version: 2.1.0
Release: alt3
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

%package -n libsdbus-cpp%soversion
Summary: High-level C++ D-Bus library for Linux
Group: System/Libraries

%description -n libsdbus-cpp%soversion
sdbus-c++ is a high-level C++ D-Bus library for Linux designed to provide expressive,
easy-to-use API in modern C++. It adds another layer of abstraction on top of sd-bus,
a nice, fresh C D-Bus implementation by systemd.

%package -n libsdbus-cpp-devel
Summary: Development files for %name
Group: Development/C++
Requires: libsdbus-cpp%soversion = %EVR
Obsoletes: libsdbus-cpp2-devel < %EVR

%description -n libsdbus-cpp-devel
This package provides development files for %name library.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files -n libsdbus-cpp%soversion
%_libdir/libsdbus-c++.so.%soversion
%_libdir/libsdbus-c++.so.%soversion.*

%files -n libsdbus-cpp-devel
%doc %_defaultdocdir/sdbus-c++/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_includedir/sdbus-c++
%_libdir/cmake/sdbus-c++

%changelog
* Wed Mar 26 2025 Anton Farygin <rider@altlinux.com> 2.1.0-alt3
- renamed source package to sdbus-cpp according upstream
- dropped support for devel packages of several libsdbus-cpp library versions
  due to instability and potential future issues

* Wed Mar 26 2025 Sergey V Turchin <zerg@altlinux.org> 2.1.0-alt2
- put pkgconfig-file on alternatives

* Mon Mar 24 2025 Kirill Unitsaev <fiersik@altlinux.org> 2.1.0-alt1
- Initial build
