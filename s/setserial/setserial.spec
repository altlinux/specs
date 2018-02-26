Name: setserial
Version: 2.17
Release: alt2
Epoch: 1

Summary: A utility for configuring serial ports
License: GPL
Group: System/Configuration/Hardware

Url: http://setserial.sourceforge.net
Source: %name-%version.tar.bz2
Patch0: setserial-2.17-error.diff
Patch1: setserial-2.17-spelling.patch
Patch2: setserial-2.17-alt-kheaders.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Sat May 03 2008
BuildRequires: groff-base

Summary(ru_RU.KOI8-R): Утилита для настройки последовательных портов

%description
Setserial is a basic system utility for displaying or setting
serial port information. Setserial can reveal and allow you
to alter the I/O port and IRQ that a particular serial device
is using, and more.

You should install %name when you may find it useful
for detecting and/or altering device information.

%prep
%setup
%patch0 -p0
%patch1 -p1
%patch2 -p2

%build
rm -f config.cache
%configure

%ifarch %ix86
%make_build
%else
%make_build DEFS="-DHAVE_ASM_IOCTLS_H=1"
%endif

%install
install -pDm755 %name %buildroot/bin/%name
install -pDm644 %name.8 %buildroot%_man8dir/%name.8

%files
/bin/*
%_mandir/man?/*
%doc README rc.serial

%changelog
* Sun Mar 28 2010 Michael Shigorin <mike@altlinux.org> 1:2.17-alt2
- dropped hardwired HAYES ESP support from spec
  as it was dropped from kernel headers (thanks kas@)
- worked around incomplete kernel fix
- applied a subset of openSUSE+Gentoo crop of patches
- freshened description a bit

* Sat May 03 2008 Michael Shigorin <mike@altlinux.org> 1:2.17-alt1
- rebuild (bluez-utils buildreq this)
- bump release, add epoch for that matter (current version)
- current url

* Fri Oct 18 2002 Rider <rider@altlinux.ru> 2.17-ipl6mdk
- Russian Summary
- rebuild (gcc 3.2)

* Wed Dec 05 2001 Konstantin Volckov <goldhead@altlinux.ru> 2.17-ipl5mdk
- Rebuild for Sisyphus
- Some spec cleanup

* Wed Aug  2 2000 Dmitry V. Levin <ldv@fandra.org> 2.17-ipl4mdk
- RE adaptions.

* Fri Mar 17 2000 Francis Galiegue <francis@mandrakesoft.com>
- Let spec-helper handle strip and compressed man/info files
- 2.17
- Some spec file fixes

* Tue Oct 26 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Fix a users.

* Sat Apr 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- bzip2 man/info pages
- add de locale

* Thu Feb 11 1999 Michael Maher <mike@redhat.com>
- fixed bug #363

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- built package for 6.0

* Sat Jun 20 1998 Jeff Johnson <jbj@redhat.com>
- upgraded to 2.1.14

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Oct 23 1997 Donnie Barnes <djb@redhat.com>
- pulled into distribution
- used setserial-2.12_CTI.tgz instead of setserial-2.12.tar.gz (former is
  all that sunsite has) - not sure what the difference is.

* Thu Sep 25 1997 Christian 'Dr. Disk' Hechelmann <drdisk@ds9.au.s.shuttle.de>
- added %%attr's
- added sanity check for RPM_BUILD_ROOT
- setserial is now installed into /bin, where util-linux puts it and all
  startup scripts expect it.
