%define soversion 5

Name: libhyprtoolkit
Version: 0.5.3
Release: alt1
License: BSD-3-Clause

Summary: A modern C++ Wayland-native GUI toolkit

Group: System/Libraries

Url: https://github.com/hyprwm/hyprtoolkit
Vcs: https://github.com/hyprwm/hyprtoolkit.git

ExcludeArch: %ix86
Source: %name-%version.tar

Patch1: fix-cover-tile-pixels.patch

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: clang libstdc++-devel

BuildRequires: pkgconfig(hyprwayland-scanner)
BuildRequires: pkgconfig(hyprutils)
BuildRequires: pkgconfig(hyprlang)
BuildRequires: pkgconfig(hyprgraphics)
BuildRequires: pkgconfig(aquamarine)

BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(iniparser)

BuildRequires: pkgconfig(opengl)

%description
%summary.

%package -n %name%soversion
Summary: A modern C++ Wayland-native GUI toolkit
Group: System/Libraries

%description -n %name%soversion
%summary.

%package -n %name-devel
Summary: Development files for %name
Group: Development/C++
Requires: %name%soversion = %EVR

%description -n %name-devel
This package provides development files for %name library.

%prep
%setup
%autopatch -p1

%build
%cmake -DCMAKE_CXX_COMPILER=clang++
%cmake_build 

%install
%cmake_install

%files -n %name%soversion
%_libdir/%name.so.%soversion
%_libdir/%name.so.%version

%files -n %name-devel
%_includedir/hyprtoolkit/
%_libdir/%name.so
%_pkgconfigdir/hyprtoolkit.pc

%changelog
* Wed Apr 15 2026 Kirill Unitsaev <fiersik@altlinux.org> 0.5.3-alt1
- new version 0.5.3

* Fri Dec 05 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.4.1-alt1
- new version 0.4.1 (with rpmrb script)

* Tue Oct 28 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.2.0-alt1
- Initial build
