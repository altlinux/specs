%define xf86 XFree86

Name: xfs
Version: 1.1.0
Release: alt1
Serial: 1
Summary: X font server
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Obsoletes: xtt %xf86-xfs xorg-x11-xfs
Provides: %xf86-xfs = 4.4 xorg-x11-xfs = %serial:%version-%release
Conflicts: chkfontpath
Requires: xfsinfo fslsfonts
Requires: libXfont >= 1.3.0 fonts-bitmap-misc >= 7.0.0-alt2 setup >= 2.2.11-alt1
PreReq: shadow-utils

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libfreetype-devel libFS-devel libXfont-devel libfontenc-devel
BuildRequires: xorg-proto-devel zlib-devel xorg-util-macros xorg-xtrans-devel

%description
Xfs is the X Window System font server.  It supplies fonts to X  Window
System display servers.

%def_disable ipv6

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	%{subst_enable ipv6}

%make_build

%install
%make DESTDIR=%buildroot install

install -pD -m644 %name.sysconfig %buildroot%_sysconfdir/sysconfig/%name
install -pD -m755 %name.init %buildroot%_initdir/%name
install -pD -m644 %name.config %buildroot%_sysconfdir/X11/fs/config

%pre
%_sbindir/groupadd -r -f xfs >/dev/null 2>&1 ||:
%_sbindir/useradd -r -g xfs -d /etc/X11/fs -s /dev/null -c "X Font Server" -n xfs >/dev/null 2>&1 ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%dir %_sysconfdir/X11/fs
%config(noreplace) %_sysconfdir/X11/fs/config
%config(noreplace) %_sysconfdir/sysconfig/%name
%config %_initdir/%name
%_bindir/*
%_man1dir/*

%changelog
* Fri Jun 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.0-alt1
- 1.1.0

* Tue Nov 25 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.8-alt3
- updated build dependencies

* Thu Jun 05 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.8-alt2
- renamed xorg-x11-xfs to xfs

* Sat May 24 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.8-alt1
- 1.0.8

* Fri May 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.7-alt2
- fixed nasty typo in SetConfigValues

* Thu May 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.7-alt1
- 1.0.7

* Sat May 17 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.6-alt2
- return an error to the log instead of segfaulting (close #15186)

* Fri Mar 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.6-alt1
- 1.0.6

* Mon Dec 17 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.5-alt2
- added "PreReq: shadow-utils" (close #13730)

* Tue Oct 02 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.5-alt1
- 1.0.5:
  + fix for integer overflows in build_range() CVE-2007-4568.
  + fix for heap overwrite in swap_char2b() CVE-2007-4568.

* Sun Sep 02 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.4-alt2
- added %_sysconfdir/X11/fs/config
- conflict with chkfontpath
- drop all triggers from spec file
- remove parameter "XFS" from /etc/sysconfig/xfs

* Thu Nov 30 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.4-alt1
- 1.0.4

* Sat Oct 14 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.3-alt1
- 1.0.3

* Thu Apr 27 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.2-alt1
- 1.0.2

* Fri Mar 24 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt5
- fixed #9304

* Wed Mar 22 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt4
- removed rm -rf /tmp/.font-unix from initscript
- added new parameter XFS=yes|no to /etc/sysconfig/xfs

* Thu Mar 16 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt3
- CVS snapshot 2006-03-13

* Sun Jan 01 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt2
- fixed update with %name <= 6.9.0

* Tue Dec 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.3-alt1
- Xorg-7.0RC3

* Sun Nov 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt0.1
- initial release

