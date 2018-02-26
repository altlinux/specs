Name: lbuscd
Version: 0.6
Release: alt10

Summary: LTSP.org's appserver side remote media service
License: %gpl2only
Group: Networking/Remote access

Url: http://www.altlinux.org/LTSP
Source0: ftp://ltsp.mirrors.tds.net/pub/ltsp/tarballs/%name-%version.tar.bz2
# cvs -d :pserver:anonymous@cvs.ltsp.org:/usr/local/cvsroot checkout %name
Source1: add_fstab_entry
Source2: remove_fstab_entry
Source3: ltsp-udev.rules
Patch0: lbuscd-0.6-format.patch
Patch1: lbuscd-0.6-cdrom.patch
Patch2: lbuscd-0.6-alt-fixes.patch

Requires: udev
BuildRequires: libpopt-devel rpm-build-licenses

%description
The 'lbus' is a network channel created between the LTSP client and the
session running on the server. It's a way of passing device events from
the thin client to the server session, so that cool things will happen,
like icons appearing on the desktop when a USB Memory stick is plugged
in.

%name runs on the LTSP client and receives events from udev and also
accepts connections from the server session. When a new device event is
received, a message will be sent through the network connection to the
server.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%define _optlevel s
%configure
%make_build

%install
%makeinstall_std bindir=%_sbindir
install -pDm755 %SOURCE1 %buildroot/lib/udev/add_fstab_entry
install -pDm755 %SOURCE2 %buildroot/lib/udev/remove_fstab_entry
install -pDm644 %SOURCE3 %buildroot%_sysconfdir/udev/rules.d/88-ltsp.rules

%files
%doc README
%_sbindir/*
/lib/udev/*
%_sysconfdir/udev/rules.d/*

%changelog
* Thu Mar 08 2012 Michael Shigorin <mike@altlinux.org> 0.6-alt10
- added patch (thx Valentin Nechaev) to fill in netaddr properly
  (takes care for IPv4/v6 unification issues and corrects memset)

* Sun Feb 21 2010 Michael Shigorin <mike@altlinux.org> 0.6-alt9
- fixed /lib/udev/add_fstab_entry, /etc/udev/rules.d/88-ltsp.rules
  (thanks led@; see also #22929)
- minor spec cleanup

* Mon May 19 2008 Led <led@altlinux.ru> 0.6-alt8
- fixed /lib/udev/add_fstab_entry

* Wed May 07 2008 Led <led@altlinux.ru> 0.6-alt7
- updated /lib/udev/add_fstab_entry

* Wed May 07 2008 Led <led@altlinux.ru> 0.6-alt6
- added:
  + %name-0.6-format.patch
  + %name-0.6-cdrom.patch

* Wed Mar 19 2008 Led <led@altlinux.ru> 0.6-alt5
- fixed /lib/udev/add_fstab_entry

* Thu Mar 06 2008 Led <led@altlinux.ru> 0.6-alt4
- added support cdfs (for AudioCD, etc.)
- disabled trying mount block devices when ID_FS_TYPE == swap

* Thu Dec 27 2007 Led <led@altlinux.ru> 0.6-alt3
- fixed /lib/udev/add_fstab_entry
- fixed Requires

* Thu Oct 25 2007 Led <led@altlinux.ru> 0.6-alt2
- added support ntfsmount-2.x (with fuse)

* Wed Oct 10 2007 Led <led@altlinux.ru> 0.6-alt1
- added ntfs-3g support

* Wed May 16 2007 Led <led@altlinux.ru> 0.6-alt0.3
- fixed add_fstab_entry: set vfat FS type for floppy

* Mon May 07 2007 Led <led@altlinux.ru> 0.6-alt0.2
- added udev rules and scripts for mount local devices

* Fri Apr 06 2007 Led <led@altlinux.ru> 0.6-alt0.1
- initial build
