%define cvsdate 20070416

Summary: Tool used to mount local media on an Xterminal from the terminals server
Name: ltspfsd
Version: 0.3
Release: alt0.2.1
License: GPL
Group: Networking/Other
URL: http://wiki.ltsp.org/twiki/bin/view/Ltsp/LtspFS
%ifdef cvsdate
Source0: %name-cvs-%cvsdate.tar.bz2
%else
Source0: %name-%version.tar.bz2
%endif
# cvs :pserver:anonymous@cvs.ltsp.org:/usr/local/cvsroot co %name
Source1: %name.1
Source2: ltspfs_mount.sh
Source3: ltspfs_umount.sh
Patch: %name-0.3-mount_hal+info.patch
Requires: fuse >= 2.5.2

BuildRequires: libX11-devel libXau-devel

%description
ltspfs is a remote filesystem consisting of two parts: 
  1) A network server daemon that runs on the LTSP terminal.
  2) A FUSE module that runs in user-space on the server, that connects
     with the daemon on the client.
The goals of ltspfs are:
  1. Provide a lightweight file access mechanism that will be feasable
     on lower end hardware.
  2. Provide a stateless file access method that will feature "atomic"
     reads and writes to minimize impact from client network
     disruptions.
  3. Provide a network filesystem that handles client reboots and
     disconnections in a manner that doesn't leave inaccesible,
     unmountable filesystems on the LTSP server.
  4. Provide a network filesystem that can easily handle the oddities
     of dealing with removable media, and integrate well with udev
     (LTSP's preferred device handling support).


%prep
%setup %{?cvsdate:-n %name-cvs-20070416}
%patch0 -p1

%build
%define _optlevel s
%configure
%make_build


%install
%make_install DESTDIR=%buildroot bindir=%_sbindir install
install -pD -m 0644 %SOURCE1 %buildroot%_man1dir/%name.1
install -d -m 0755 %buildroot/sbin
install -m 0700 %SOURCE2 %buildroot/sbin/ltspfs_mount
install -m 0700 %SOURCE3 %buildroot/sbin/ltspfs_umount


%files
%doc AUTHORS README
/sbin/*
%_sbindir/*
%_man1dir/*


%changelog
* Mon Feb 23 2009 Michael Shigorin <mike@altlinux.org> 0.3-alt0.2.1
- NMU: updated BuildRequires

* Wed May 16 2007 Led <led@altlinux.ru> 0.3-alt0.2
- fixed mount/umount scripts names
- fixed ltspfs_umount
- replaced %name-0.2-mount_hal.patch with %name-0.3-mount_hal+info.patch

* Mon Apr 23 2007 Led <led@altlinux.ru> 0.3-alt0.1
- initial build for Sisyphus
- added %name-0.2-mount_hal.patch (from Mandriva?)
- added %name.1 (from Gentoo?)
- added ltsp_mount and ltsp_umount scripts
