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

Name: ddcutil
Version: 0.9.2
Release: alt1

Summary: Utility to query and update monitor settings
License: GPLv2+
Group: System/Configuration/Hardware

Url: http://github.com/rockowitz/%name
Source: %url/archive/v%version.tar.gz#/%name-%version.tar.gz

BuildRequires: i2c-tools
BuildRequires: python-devel
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libudev)
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

%package -n libddcutil0
Summary: Shared library to query and update monitor settings
Group: System/Libraries

%description -n libddcutil0
Shared library version of ddcutil, exposing a C API.

ddcutil communicates with monitors implementing MCCS (Monitor Control Command
Set), using either the DDC/CI protocol on the I2C bus or as a Human Interface
Device on USB.

%package -n libddcutil-devel
Summary: Development files for libddcutil
Group: Development/C
Requires: libddcutil0 = %version

%description -n libddcutil-devel
Header files and pkgconfig control file for libddcutil.

%prep
%setup

%build
./autogen.sh
%configure \
	--enable-lib=yes \
	--enable-drm=yes \
	--enable-usb=yes \
	--docdir="%_defaultdocdir/%name-%version"
%make_build

%check
%make check

%install
%makeinstall_std

%files
%doc AUTHORS NEWS.md README.md ChangeLog
%dir %_datadir/%name
%dir %_datadir/%name/data
%_datadir/%name/data/*rules
%_datadir/%name/data/90-nvidia-i2c.conf
%_mandir/man1/ddcutil.1*
%_bindir/ddcutil

%files -n libddcutil0
%doc AUTHORS NEWS.md README.md ChangeLog
%_libdir/libddcutil.so.*

%files -n libddcutil-devel
%_includedir/ddcutil_types.h
%_includedir/ddcutil_c_api.h
%_includedir/ddcutil_macros.h
%_includedir/ddcutil_status_codes.h
%_libdir/pkgconfig/ddcutil.pc
%_libdir/libddcutil.so
%dir %_datadir/%name
%dir %_datadir/%name/data/
%_datadir/%name/data/FindDDCUtil.cmake

%changelog
* Thu Feb 14 2019 Michael Shigorin <mike@altlinux.org> 0.9.2-alt1
- built for sisyphus (based on opensuse package by alarrosa@suse)
