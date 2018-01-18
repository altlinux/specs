#
# spec file for package neard
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2010-2012 B1 Systems GmbH, Vohburg, Germany
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

Name: neard
Version: 0.16
Release: alt1

Summary: NFC for Linux
License: GPLv2
Group: System/Kernel and hardware

# git://git.kernel.org/pub/scm/network/nfc/neard
Url: http://01.org/linux-nfc/
Source0: https://www.kernel.org/pub/linux/network/nfc/neard-%version.tar
Source1: neard.service
Source2: 99-neard.rules
Source3: neard.init
Patch: neard-0.13-fix-dbus_send_destination_config.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Fri Feb 27 2015
# optimized out: libcloog-isl4 pkg-config
BuildRequires: glib2-devel libdbus-devel libnl-devel

# unit dirs
BuildRequires: systemd systemd-devel

%description
NFC support for Linux.

%package devel
Summary: Files needed for NFC development
Group: Development/C

%description devel
Files needed to develop applications for the NFC stack.

%package test
Summary: Files needed for NFC development
Group: Development/Other
Requires: neard

%description test
Files needed to test applications for the NFC stack.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure --enable-tools --enable-test
%make_build

%install
%makeinstall_std
install -pDm644 %SOURCE1 %buildroot%_unitdir/neard.service
install -pDm644 %SOURCE2 %buildroot%_libdir/udev/rules.d/99-neard.rules
install -pDm755 %SOURCE3 %buildroot%_initdir/neard

%files
%doc AUTHORS COPYING ChangeLog README
%config %_sysconfdir/dbus-1/system.d/org.neard.conf
%dir %_libexecdir/nfc/
%_libexecdir/nfc/neard
%_libdir/udev/rules.d/99-neard.rules
%_unitdir/neard.service
%_initdir/neard
%_bindir/nfctool
%_man1dir/*
%_man5dir/*
%_man8dir/*

%files devel
%_includedir/near/
%_pkgconfigdir/*.pc

%files test
%dir %_libdir/%name/
%_libdir/%name/test/

%changelog
* Thu Jan 18 2018 Michael Shigorin <mike@altlinux.org> 0.16-alt1
- 0.16

* Thu Jan 07 2016 Michael Shigorin <mike@altlinux.org> 0.15-alt3
- mark compressed manpages properly

* Sat Feb 28 2015 Michael Shigorin <mike@altlinux.org> 0.15-alt2
- added initscript (adapted from yoctoproject's poky recipe)

* Fri Feb 27 2015 Michael Shigorin <mike@altlinux.org> 0.15-alt1
- built for ALT Linux (package based on openSUSE 0.13-21.6 one)

