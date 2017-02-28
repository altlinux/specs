Name: libwlc0
Version: 0.0.8
Release: alt1

%define oname wlc

Summary: wlc wayland compositor library

License: MIT
Group: System/Libraries
Packager: Vladimir D. Seleznev <vseleznv@altlinux.org>
Source0: %oname-%version.tar
Source1: chck.tar
Url: https://github.com/Cloudef/wlc

BuildRequires(pre): rpm-macros-cmake
# Automatically added by buildreq on Mon Sep 26 2016
# optimized out: cmake-modules libEGL-devel libX11-devel libgpg-error libudev-devel libwayland-client libwayland-client-devel libwayland-server libxcb-devel libxcbutil-icccm libxcbutil-image pkg-config python-base wayland-devel xorg-xproto-devel
BuildRequires: cmake libGLES-devel libXfixes-devel libdbus-devel libdrm-devel libgbm-devel libinput-devel libpixman-devel libsystemd-devel libwayland-egl-devel libwayland-server-devel libxcbutil-icccm-devel libxcbutil-image-devel libxkbcommon-devel wayland-protocols

Requires: wayland-protocols

%description
wlc wayland compositor library

%package devel
Summary: headers for wlc wayland compositor library
Group: Development/C
Provides: lib%oname-devel = %version-%release

%description devel
headers for wlc wayland compositor library

%prep
%setup -n %oname-%version
tar xvf %SOURCE1 -C lib

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_libdir/*.so.*

%files devel
%_includedir/%oname
%_libdir/*.so
%_libdir/pkgconfig/%oname.pc

%changelog
* Tue Feb 28 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.0.8-alt1
- 0.0.8

* Sat Oct 29 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.0.7-alt1
- 0.0.7

* Tue Oct 04 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.0.6-alt1
- 0.0.6

* Wed Aug 03 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.0.5-alt1
- Initial build
