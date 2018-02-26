Name: cdemu-daemon
Version: 1.5.0
Release: alt1

Summary: CDEmu daemon
License: GPLv2+
Group: System/Servers

URL: http://cdemu.sourceforge.net
Packager: Nazarov Denis <nenderus@altlinux.org>

Source0: %name-%version.tar.bz2 

BuildRequires: libao-devel >= 0.8.0
BuildRequires: libgio-devel >= 2.28
BuildRequires: libmirage-devel >= 1.5.0

%description
This is CDEmu daemon, the userspace daemon part of the userspace-cdemu suite, a 
free, GPL CD/DVD-ROM device emulator for linux.

It receives SCSI commands from kernel module and processes them, passing the 
requested data back to the kernel. Daemon implements the actual virtual device; 
one instance per each device registered by kernel module. It uses libMirage, an 
image access library that is part of userspace-cdemu suite, for the image access 
(e.g. sector reading).

The daemon registers itself on D-BUS' system or session bus (depending on the
options passed to it) where it exposes an interface that can be used by clients
to control it.

%prep
%setup -q

%build
%configure
%make_build

%install
%make DESTDIR=%buildroot install

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%_bindir/cdemud
%_libexecdir/%name-*
%_mandir/man8/*
%dir %_datadir/dbus-1
%dir %_datadir/dbus-1/services
%_datadir/dbus-1/services/*.service
%dir %_datadir/dbus-1/system-services
%_datadir/dbus-1/system-services/*.service
%dir %_sysconfdir/dbus-1
%dir %_sysconfdir/dbus-1/system.d
%_sysconfdir/dbus-1/system.d/cdemud-dbus.conf

%changelog
* Wed Jan 25 2012 Nazarov Denis <nenderus@altlinux.org> 1.5.0-alt1
- Version 1.5.0

* Tue Sep 20 2011 Nazarov Denis <nenderus@altlinux.org> 1.4.0-alt1
- Version 1.4.0

* Tue Jan 25 2011 Nazarov Denis <nenderus@altlinux.org> 1.3.0-alt2
- Add LSB init headers

* Fri Nov 19 2010 Nazarov Denis <nenderus@altlinux.org> 1.3.0-alt1
- Initial build for ALT Linux

* Sat Sep 18 2010 tuoma_mel@inbox.ru
- Updated to 1.3.0

* Mon Mar 29 2010 tuoma_mel@inbox.ru
- Updated to 1.2.0

* Sat Jun 28 2008 Rok Mandeljc <rok.mandeljc@email.si> - 1.1.0-1
- Updated to 1.1.0

* Thu Dec 20 2007 Rok Mandeljc <rok.mandeljc@email.si> - 1.0.0-1
- Initial RPM release.
