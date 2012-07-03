Name: pcmciautils
Version: 018
Release: alt1
Summary: PCMCIA utilities
Group: System/Configuration/Hardware
License: GPL
Url: http://www.kernel.org/pub/linux/utils/kernel/pcmcia/pcmcia.html
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: udev >= 118

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: flex libpci-devel

%description
%name contains udev config and initialization tools necessary
to allow the PCMCIA subsystem to behave (almost) as every other
hotpluggable bus system

%prep
%setup -q
%patch -p1

%build
%make all

%install
%make DESTDIR=%buildroot install

%files
/lib/udev/rules.d/*.rules
%dir %_sysconfdir/pcmcia
%config(noreplace) %_sysconfdir/pcmcia/config.opts
/sbin/lspcmcia
/sbin/pccardctl
/lib/udev/pcmcia-*
%_man8dir/*.8*

%changelog
* Fri Apr 22 2011 Valery Inozemtsev <shrek@altlinux.ru> 018-alt1
- 018

* Mon Nov 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 017-alt2
- updated to master git.c96724a

* Sat Jan 09 2010 Valery Inozemtsev <shrek@altlinux.ru> 017-alt1
- 017

* Sun Sep 28 2008 Valery Inozemtsev <shrek@altlinux.ru> 015-alt1
- 015

* Sat Jun 14 2008 Valery Inozemtsev <shrek@altlinux.ru> 014-alt7
- added %_sysconfdir/pcmcia/cis
- fixed segfault on pcmcia-socket-startup

* Sun Feb 10 2008 Valery Inozemtsev <shrek@altlinux.ru> 014-alt6
- fixed udev rules
- droped cis

* Sun Apr 01 2007 Valery Inozemtsev <shrek@altlinux.ru> 014-alt5
- added -b option to all modprobe invocations
- removed exclude irq 7
- drop %name-hotplug subpackage

* Tue Feb 27 2007 Valery Inozemtsev <shrek@altlinux.ru> 014-alt4
- added exclude irq 3,4,7 for config.opts

* Fri Jan 19 2007 Valery Inozemtsev <shrek@altlinux.ru> 014-alt3
- correct update %_sysconfdir/sysconfig/hotplug

* Wed Jan 17 2007 Valery Inozemtsev <shrek@altlinux.ru> 014-alt2
- added udev rules
- moved hotplug scripts to %name-hotplug subpackage

* Sun Jun 04 2006 Valery Inozemtsev <shrek@altlinux.ru> 014-alt1
- 014

* Sun May 07 2006 Valery Inozemtsev <shrek@altlinux.ru> 013-alt2
- used optimization flags from RPM_OPT_FLAGS

* Mon Mar 27 2006 Valery Inozemtsev <shrek@altlinux.ru> 013-alt1
- 013

* Tue Feb 21 2006 Valery Inozemtsev <shrek@altlinux.ru> 012-alt4
- removed obsoleted probe io options
- removed support APM

* Thu Feb 02 2006 Valery Inozemtsev <shrek@altlinux.ru> 012-alt3
- fixed post scripts (#9006)

* Sat Jan 28 2006 Valery Inozemtsev <shrek@altlinux.ru> 012-alt2
- fixed #8733

* Tue Dec 20 2005 Valery Inozemtsev <shrek@altlinux.ru> 012-alt1
- 012

* Tue Sep 20 2005 Valery Inozemtsev <shrek@altlinux.ru> 010-alt1
- 010

* Thu Sep 15 2005 Valery Inozemtsev <shrek@altlinux.ru> 009-alt1
- 009

* Tue Sep 06 2005 Valery Inozemtsev <shrek@altlinux.ru> 008-alt1
- 008

* Tue Jul 26 2005 Valery Inozemtsev <shrek@altlinux.ru> 007-alt1
- 007
- added apm support

* Sat Jul 16 2005 Valery Inozemtsev <shrek@altlinux.ru> 006-alt1
- 006

* Mon Jul 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 005-alt1
- 005

* Sun Jun 19 2005 Valery Inozemtsev <shrek@altlinux.ru> 003-alt1
- initial release

