Name: lomoco
Version: 1.0
Release: alt6

Summary: Logitech mouse control tool
License: GPL
Group: System/Configuration/Hardware

Url: http://www.lomoco.org
Source0: %url/%name-%version.tar.gz
Source1: lomoco.sysconfig
Patch0: lomoco-1.0-alt-logger-path.patch
Patch1: lomoco-1.0-alt-headers.patch
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: libusb-compat-devel

%description
Lomoco can configure vendor-specific options on Logitech USB mice
(or dual-personality mice plugged into the USB port). A number
of recent devices are supported. The program is mostly useful
in setting the resolution to 800 cpi or higher on mice that boot
at 400 cpi (such as the MX500, MX510, MX1000 etc.), and disabling
SmartScroll or Cruise Control for those who would rather use the
two extra buttons as ordinary mouse buttons.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
./autogen.sh
%configure
%make
make udev-rules

%install
%makeinstall
install -pD -m755 udev/udev.lomoco %buildroot/lib/udev/lomoco
install -pD -m644 udev/lomoco.rules %buildroot%_sysconfdir/udev/rules.d/40-lomoco.rules
install -pD -m644 %SOURCE1 %buildroot%_sysconfdir/sysconfig/logitech_mouse

%files
%doc AUTHORS ChangeLog NEWS README
%_bindir/%name
%_sysconfdir/sysconfig/logitech_mouse
%_sysconfdir/udev/rules.d/*.rules
/lib/udev/lomoco
%_man1dir/*

%changelog
* Sun Sep 26 2010 Michael Shigorin <mike@altlinux.org> 1.0-alt6
- rebuilt with helper in /lib/udev, thanks ldv@

* Mon Apr 06 2009 Michael Shigorin <mike@altlinux.org> 1.0-alt5
- built against libusb-compat-devel

* Wed Nov 05 2008 Michael Shigorin <mike@altlinux.org> 1.0-alt4
- fixed build (thx thresh@, wrar@ and shrek@ for replies)
- updated Url:

* Mon Sep 17 2007 Michael Shigorin <mike@altlinux.org> 1.0-alt3
- fixed udev script to avoid specifying any hardwired path
  to logger at all; thanks at@ and ldv@

* Sun Sep 16 2007 Michael Shigorin <mike@altlinux.org> 1.0-alt2
- fixed udev script (path to logger)
- added initial sysconfig sample

* Wed Jan 10 2007 Michael Shigorin <mike@altlinux.org> 1.0-alt1
- built for ALT Linux (spec based on Mandriva 2007 contrib)

* Sun Sep 03 2006 David Walluck <walluck@mandriva.org> 1.0-2mdv2007.0
- rebuild
- use /%%{_lib}/udev not /lib/udev

* Wed Mar 1 2006 Austin Acton <austin@mandriva.org> 1.0-1mdk
- initial package
