%define _libexecdir %_prefix/libexec/udisks

Name: udisks
Version: 1.0.4
Release: alt2
Epoch: 1
Summary: Disk Management Service
License: GPLv2+
Group: System/Libraries
URL: http://cgit.freedesktop.org/udisks/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: DeviceKit-disks = %epoch:%version
Obsoletes: DeviceKit-disks <= 009

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: gcc-c++ gtk-doc intltool libatasmart-devel libdbus-glib-devel libdevmapper-devel libgio-devel liblvm2-devel
BuildRequires: libparted-devel libpolkit1-devel libsqlite3-devel libudev-devel libgudev-devel libsgutils-devel

%description
%name provides a daemon, D-Bus API and command line tools
for managing disks and storage devices

%package devel
Summary: D-Bus interface definitions for %name
Group: Development/C++
BuildArch: noarch
Provides: DeviceKit-disks-devel = %epoch:%version
Obsoletes: DeviceKit-disks-devel <= 009

%description devel
D-Bus interface definitions for %name

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--libexecdir=%_libexecdir \
	--localstatedir=%_var \
	--enable-gtk-doc \
	--disable-static
%make

%install
%make DESTDIR=%buildroot install

mkdir -p %buildroot%_var/run/%name
touch %buildroot%_var/lib/%name/mtab

%files
%doc AUTHORS NEWS README
%_sysconfdir/avahi/services/*.service
%_sysconfdir/dbus-1/system.d/*.conf
#_sysconfdir/profile.d/*.sh
/lib/udev/rules.d/*.rules
/lib/udev/%name-*
/sbin/*
%_bindir/*
#_libdir/polkit-1/extensions/*.so
%_libexecdir/%name-*
%_datadir/dbus-1/system-services/*.service
%_datadir/polkit-1/actions/*.policy
%_man1dir/*.1*
%_man7dir/*.7*
%_man8dir/*.8*
%attr(0700,root,root) %dir %_var/lib/%name
%ghost %_var/lib/%name/mtab
%attr(0700,root,root) %dir %_var/run/%name

%files devel
%_datadir/pkgconfig/*.pc
%_datadir/dbus-1/interfaces/*.xml
%_datadir/gtk-doc/html/%name

%changelog
* Sat May 12 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.4-alt2
- don't requires mdadm (closes: #25648)

* Fri Aug 26 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.4-alt1
- 1.0.4

* Thu Jun 30 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.3-alt1
- 1.0.3

* Fri Jan 14 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.2-alt2
- added exFAT support

* Sat Jan 01 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.2-alt1
- 1.0.2

* Tue Nov 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt4
- readded mount option "fmask=0177" for vfat

* Fri Nov 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt3
- dropped unused DeviceKit

* Thu Aug 26 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt2
- rebuild with liblvm2app.so.2.2

* Fri Apr 09 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt1
- 1.0.1

* Fri Mar 19 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.0-alt4
- fixed exit code of umount.udisks

* Tue Mar 16 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.0-alt3
- 1.0.0 release

* Mon Mar 15 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.0-alt2.df917d
- GIT snapshot 2010-03-15 (df917d90494728a1e17c4af6eade19a3ad75c16d)

* Tue Mar 09 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.0-alt1.c83bdd
- GIT snapshot 2010-03-09 (c83bdd5c4616f0a6cbcbbd22062184bb95107d43)

* Mon Mar 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.0-alt0.fa313b.1
- rebuild with libparted.so.0

* Sun Mar 07 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.0-alt0.fa313b
- GIT snapshot 2010-03-05 (fa313b2e7d7522626b9515d942366b53e7992735)

* Tue Feb 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 009-alt3
- updated udev rules to cope better with device-mapper

* Mon Jan 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 009-alt2
- added mount option "fmask=0177" for vfat

* Sun Nov 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 009-alt1
- 009

* Mon Oct 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 008-alt1
- 008

* Sat Sep 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 007-alt1
- 007

* Thu Aug 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 006-alt1
- 006

* Mon Aug 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 005-alt1
- 005

* Tue May 05 2009 Valery Inozemtsev <shrek@altlinux.ru> 004-alt1
- 004

* Sat Apr 04 2009 Valery Inozemtsev <shrek@altlinux.ru> 003-alt1
- initial release

