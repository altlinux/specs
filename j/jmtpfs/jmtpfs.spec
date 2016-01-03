#
# spec file for package jmtpfs
#
# Copyright (c) 2012 Malcolm J Lewis <malcolmlewis@opensuse.org>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

Name: jmtpfs
Version: 0.5
Release: alt1

Summary: FUSE based MTP filesystem
License: GPLv3
Group: Communications

Url: http://research.jacquette.com/jmtpfs-exchanging-files-between-android-devices-and-linux/
Source: http://research.jacquette.com/wp-content/uploads/2012/05/jmtpfs-%version.tar.gz
Source1: 51-android.rules
Source2: jmtpfs.1
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: libmagic-devel
BuildRequires: libfuse-devel
BuildRequires: gcc-c++
BuildRequires: libmtp-devel
BuildRequires: libusb-devel
BuildRequires: pkg-config

%description
FUSE and libmtp based filesystem for accessing MTP
(Media Transfer Protocol) devices. It was specifically
designed for exchanging files between Linux systems
and newer Android devices that support MTP
but not USB Mass Storage.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std
# udev rules (only for non-systemd)
install -pDm644 %SOURCE1 %buildroot%_udevrulesdir/51-android.rules
install -pDm644 %SOURCE2 %buildroot%_man1dir/jmtpfs.1

%files
%doc AUTHORS COPYING NEWS README
%_bindir/%name
%_udevrulesdir/51-android.rules
%_man1dir/jmtpfs.1*

%changelog
* Sun Jan 03 2016 Michael Shigorin <mike@altlinux.org> 0.5-alt1
- initial build for ALT Linux Sisyphus (based on openSUSE/Nux packages)
