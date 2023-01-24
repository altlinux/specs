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

%define soname 4

Name: ddcutil
Version: 1.4.1
Release: alt1

Summary: Utility to query and update monitor settings
Group: System/Configuration/Hardware
License: GPLv2+
Url: http://github.com/rockowitz/%name

Source: %url/archive/v%version/%name-%version.tar.gz

BuildRequires: libi2c-devel i2c-tools
BuildRequires: python-devel
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(libkmod)
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(zlib)

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
NOCONFIGURE=1 ./autogen.sh
%configure \
    --enable-lib \
    --enable-drm \
    --enable-usb \
    --enable-x11 \
    --docdir="%_defaultdocdir/%name-%version"
%make_build

%install
%makeinstall_std rulesdir=%_udevrulesdir

%check
%make check

%files
%_bindir/%name
%_udevrulesdir/60-%name.rules
%dir %_datadir/%name
%dir %_datadir/%name/data
%_datadir/%name/data/*rules
%_datadir/%name/data/90-nvidia-i2c.conf
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
