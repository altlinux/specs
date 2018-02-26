Name: irda-utils
Version: 0.9.18
Release: alt3

Summary: Utilities for infrared communication between devices
License: GPL
Group: System/Servers

Url: http://irda.sourceforge.net
Source: ftp://irda.sourceforge.net/pub/irda/%name/%name-%version.tar.gz
Source1: irda.rc
Source2: irda.sysconfig
Patch1: irda-utils-0.9.18-rootonly.patch
Patch2: irda-utils-0.9.16-irkbd.patch
Patch3: irda-utils-gcc3.4-fix.patch
Patch4: irda-utils-rh1.patch
Patch5: irda-utils-0.9.16-alt-irattach-daemonize.patch
Patch6: irda-utils-0.9.18-io.h.diff
Patch7: irda-utils-0.9.18-smcinit.diff
Patch8: irda-utils-0.9.18-alt-as-needed.patch
Patch9: irda-utils-0.9.18-alt-makefile.patch
Packager: Michael Shigorin <mike@altlinux.org>

Summary(ru_RU.KOI8-R): Утилиты для управления соединениями через инфракрасный порт

# Automatically added by buildreq on Wed Dec 31 2008
BuildRequires: glib2-devel libpci-devel

%description
IrDA(TM) (Infrared Data Association) is an industry standard for
wireless, infrared communication between devices. IrDA speeds range
from 2400 bps to 4 Mbps, and IrDA can be used by many modern devices
including laptops, LAN adapters, PDAs, printers, and mobile phones.

The Linux-IrDA project is a GPLed implementation, written from
scratch, of the IrDA protocols. Supported IrDA protocols include
IrLAP, IrLMP, IrIAP, IrTTP, IrLPT, IrLAN, IrCOMM and IrOBEX.

The %name package contains a collection of programs that enable
the use of IrDA protocols. Most IrDA features are implemented in the
kernel, so IrDA support must be enabled in the kernel before any IrDA
tools or programs can be used. Some configuration outside the kernel
is required, however, and some IrDA features, like IrOBEX, are
actually implemented outside the kernel.

%prep
%setup
%patch1 -p1 -b .rootonly
#patch2 -p1 -b .irkbd
#patch3 -p1 -b .gcc34
%patch4 -p1 -b .rh1
%patch5 -p1 -b .daemonize
%patch6 -p1 -b .io.h
%patch7 -p0 -b .smcinit
%patch8 -p1 -b .as-needed
%patch9 -p1 -b .makefile

%build
%make_build all ROOT="%buildroot" RPM_OPT_FLAGS="%optflags"

%install
mkdir -p %buildroot{%_bindir,%_sbindir}
%make_install install ROOT="%buildroot" MANDIR="%buildroot%_mandir"

install -pm755 %SOURCE1 %buildroot%_initdir/irda
install -pm644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/irda
mv %buildroot%_sysconfdir/sysconfig/network-scripts/ifcfg-irlan0 .

find -mindepth 2 -name README | while read d; do
	install -p -m644 "$d" "README.`dirname $d | cut -c3-`"
done

%files
%_bindir/*
%_sbindir/*
%config(noreplace) %_initdir/*
%config(noreplace) %_sysconfdir/sysconfig/irda
#config(noreplace) %_sysconfdir/sysconfig/network-scripts/ifcfg-irlan0
%doc README* ifcfg-irlan0
%_man4dir/*
%_man7dir/*
%_man8dir/*

%changelog
* Mon Sep 14 2009 Michael Shigorin <mike@altlinux.org> 0.9.18-alt3
- moved ifcfg-irlan0 to docs (closes: #21560)

* Wed Dec 31 2008 Michael Shigorin <mike@altlinux.org> 0.9.18-alt2
- fixed 0.9.18 build for ALT:
  + updated rootonly patch
  + removed irkbd, gcc34 patches (merged/fixed upstream)
  + added Gentoo smcinit, io.h patches
  + fixed --as-needed issue
- removed unneeded package scriptlets
- added manpages to the package
- tweaked build
- buildreq

* Sat Nov 11 2006 Michael Shigorin <mike@altlinux.org> 0.9.18-alt1
- 0.9.18

* Sun Sep 03 2006 Michael Shigorin <mike@altlinux.org> 0.9.16-alt3
- fixed #6257 (bad error message on TIOCSETD failure);
  thanks vsu@ for bug/patch, damir@ and ruslandh@ for explanation
- fixed macro (ab)use in pre-ALT changelog
- 0.9.18 would need patch update, so sticking with 0.9.16 right now

* Wed Oct 19 2005 Michael Shigorin <mike@altlinux.org> 0.9.16-alt2
- rehash docs install
- get findchip (#4695)
- added Gentoo and RH patches
- spec cleanup

* Tue Apr 13 2004 Grigory Milev <week@altlinux.ru> 0.9.16-alt1
- new version released
- update root only patch
- fix start/stop scripts

* Sat Oct 05 2002 Rider <rider@altlinux.ru> 0.9.15-alt2
- gcc 3.2 rebuild

* Wed Aug 14 2002 Rider <rider@altlinux.ru> 0.9.15-alt1
- 0.9.15

* Wed Mar 20 2002 Rider <rider@altlinux.ru> 0.9.14-alt2
- libtool fix
- patch1 from RH (fix irdadump crash)
- russian summary

* Fri Aug 17 2001 Rider <rider@altlinux.ru> 0.9.14-alt1
- 0.9.14

* Sat Jan 20 2001 Dmitry V. Levin <ldv@fandra.org> 0.9.13-ipl2mdk
- RE adaptions.
- Fixed init script.

* Thu Nov 23 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.9.13-1mdk
- 0.9.13

* Thu Nov 16 2000 David BAUDENS <baudens@mandrakesoft.com> 0.9.10-2mdk
- Allow to build (fix %%doc)

* Tue Aug 29 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.9.10-1mdk
- 0.9.10

* Wed Apr  5 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.9.9-1mdk
- group fix.

* Mon Feb  7 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.9.9-1mdk
- new version.
- init.d script activated.
- added a printer config file.

* Mon Dec 06 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Build release.

* Wed Nov 10 1999 Dag Brattli <dagb@cs.uit.no>
- 0.9.5
- Some fixes to irattach, so it works with the latest kernels and patches
- Removed OBEX which will now become its own distribution
- Removed irdadump-X11 which will be replaced with a GNOME version

* Wed Sep 8 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- 0.9.4
- include new stuff (palm3, psion, obex_tcp, ...)
- various fixes

* Tue Sep 7 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Fix .spec bug

* Tue Sep 7 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- add README to %%doc
- compile gnobex, now in irda-utils-X11

* Tue Sep 7 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- initial RPM:
  - handle RPM_OPT_FLAGS and RPM_BUILD_ROOT
  - fix build
  - split in normal and X11 packages

