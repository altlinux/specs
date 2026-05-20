#
# spec file for package ddcutil
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2019 Michael Shigorin
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugzilla.altlinux.org

%define soname 5

Name: ddcutil
Version: 2.2.7
Release: alt1

Summary: Utility to query and update monitor settings
Group: System/Configuration/Hardware
License: GPL-2.0-or-later
Url: http://github.com/rockowitz/%name
Vcs: http://github.com/rockowitz/ddcutil

Requires: i2c-tools

Source: %url/archive/v%version/%name-%version.tar

BuildRequires: libi2c-devel i2c-tools
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(jansson)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(libkmod)
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(libacl)
BuildRequires: pkgconfig(dbus-1)

%description
ddcutil communicates with monitors implementing MCCS (Monitor Control Command
Set), using either the DDC/CI protocol on the I2C bus or as a Human Interface
Device on USB.

A particular use case for ddcutil is as part of color profile management.
Monitor calibration is relative to the monitor color settings currently in
effect, e.g. red gain.  ddcutil allows color related settings to be saved at
the time a monitor is calibrated, and then restored when the calibration is
applied.

%package -n lib%name%soname
Summary: Shared library to query and update monitor settings
Group: System/Libraries

%description -n lib%name%soname
Shared library version of ddcutil, exposing a C API.

ddcutil communicates with monitors implementing MCCS (Monitor Control Command
Set), using either the DDC/CI protocol on the I2C bus or as a Human Interface
Device on USB.

%package -n libddcutil-devel
Summary: Development files for libddcutil
Group: Development/C
Requires: lib%name%soname = %EVR

%description -n libddcutil-devel
Header files and pkgconfig control file for libddcutil.

%prep
%setup

%build
%add_optflags %(getconf LFS_CFLAGS)
NOCONFIGURE=1 ./autogen.sh
%configure \
    --enable-lib \
    --enable-drm \
    --enable-usb \
    --docdir="%_defaultdocdir/%name-%version"
%make_build

%install
%makeinstall_std rulesdir=%_udevrulesdir \
installed_modulesdir=%_modulesloaddir

%check
%make check

%files
%_bindir/%name
%_modulesloaddir/%name.conf
%_udevrulesdir/60-%name-i2c.rules
#%_udevrulesdir/60-%name-usb.rules
%dir %_datadir/%name
%dir %_datadir/%name/data
%_datadir/%name/data/60-%name-i2c.rules
%_datadir/%name/data/60-%name-usb.rules
%_datadir/%name/data/90-nvidia-i2c.conf
%_datadir/%name/data/nvidia-i2c.conf
%_man1dir/%name.1*
%doc AUTHORS NEWS.md README.md CHANGELOG.md

%files -n libddcutil%soname
%_libdir/libddcutil.so.%{soname}*
%doc AUTHORS NEWS.md README.md CHANGELOG.md

%files -n libddcutil-devel
%_includedir/%{name}_types.h
%_includedir/%{name}_c_api.h
%_includedir/%{name}_macros.h
%_includedir/%{name}_status_codes.h
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc
%_libdir/cmake/%name/FindDDCUtil.cmake

# TODO: python subpackage?

%changelog
* Wed May 20 2026 Sergey V Turchin <zerg@altlinux.org> 2.2.7-alt1
- 2.2.7 (closes: 59246)

* Wed Mar 11 2026 Yuri N. Sedunov <aris@altlinux.org> 2.2.6-alt1
- 2.2.6

* Tue Jan 27 2026 Yuri N. Sedunov <aris@altlinux.org> 2.2.5-alt1
- 2.2.5

* Sat Nov 15 2025 Yuri N. Sedunov <aris@altlinux.org> 2.2.3-alt1
- 2.2.3

* Fri Nov 14 2025 Yuri N. Sedunov <aris@altlinux.org> 2.2.2-alt1
- 2.2.2

* Thu Jul 10 2025 Yuri N. Sedunov <aris@altlinux.org> 2.2.1-alt1
- 2.2.1

* Tue Feb 18 2025 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- 2.2.0

* Sat Feb 24 2024 Yuri N. Sedunov <aris@altlinux.org> 2.1.4-alt1
- 2.1.4

* Thu Feb 08 2024 Yuri N. Sedunov <aris@altlinux.org> 2.1.3-alt1
- 2.1.3

* Sun Jan 28 2024 Yuri N. Sedunov <aris@altlinux.org> 2.1.2-alt1
- 2.1.2

* Thu Jan 18 2024 Yuri N. Sedunov <aris@altlinux.org> 2.1.0-alt1
- 2.1.0

* Fri Sep 29 2023 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1
- 2.0.0

* Tue Jan 24 2023 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt1
- 1.4.1

* Mon Jul 25 2022 Yuri N. Sedunov <aris@altlinux.org> 1.3.0-alt1
- 1.3.0

* Sat May 07 2022 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt1
- 1.2.2

* Wed May 06 2020 Michael Shigorin <mike@altlinux.org> 0.9.8-alt1
- 0.9.8 (thx aris@)

* Thu Feb 14 2019 Michael Shigorin <mike@altlinux.org> 0.9.2-alt1
- built for sisyphus (based on opensuse package by alarrosa@suse)
