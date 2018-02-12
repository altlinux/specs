%define xorg xorg-x11
%define xf86 XFree86

Name: xdm
Version: 1.1.10
Release: alt2
Serial: 2
Summary: X Display Manager with support for XDMCP, host chooser
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Obsoletes: %xf86-%name %xorg-%name < %serial:%version-%release
Provides: %xf86-%name = 4.4 %xorg-%name = %serial:%version-%release

# Automatically added by buildreq on Wed Jun 23 2010
BuildRequires: libXau-devel libXaw-devel libXdmcp-devel libXext-devel libXft-devel libXinerama-devel libXpm-devel libpam-devel xorg-util-macros xorg-xtrans-devel

%description
Xdm  manages a collection of X displays, which may be on the local host
or remote servers.  The design of xdm was guided by the needs of X ter-
minals  as well as The Open Group standard XDMCP, the X Display Manager
Control Protocol.  Xdm provides services similar to those  provided  by
init,  getty and login on character terminals: prompting for login name
and password, authenticating the user, and running a ``session.''

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
	--with-xdmlibdir=%_libdir/X11/xdm \
	--with-xdmconfigdir=%_sysconfdir/X11/xdm \
	--with-xdmscriptdir=%_sysconfdir/X11/xdm \
	--with-pixmapdir=%_datadir/X11/xdm/pixmaps \
	--with-xft \
	--enable-xdm-auth \
	--enable-xdmshell \
	--disable-static

%make_build

%install
%makeinstall_std
find %buildroot -type f -name 'lib*.la' -delete

install -pD -m644 xdm.pamd %buildroot%_sysconfdir/pam.d/xdm
install -pD -m640 xdm.logrotate %buildroot%_sysconfdir/logrotate.d/xdm

# explicitly create X authdir
mkdir -p %buildroot%_localstatedir/xdm
ln -snf ../../..%_localstatedir/xdm %buildroot%_sysconfdir/X11/xdm/authdir

%files
%config(noreplace) %_sysconfdir/X11/app-defaults/*
%dir %_sysconfdir/X11/xdm/
%_sysconfdir/X11/xdm/authdir
%config(noreplace) %_sysconfdir/logrotate.d/xdm
%config(noreplace) %_sysconfdir/pam.d/xdm
%_bindir/*
%_libdir/X11/xdm
%_datadir/X11/xdm
%dir %attr(700,root,root) %_localstatedir/xdm/
%_man1dir/*

%changelog
* Mon Feb 12 2018 Andrey Cherepanov <cas@altlinux.org> 2:1.1.10-alt2
- Remove requirements of pam-ck-connector2 (ALT #34523)

* Sat Jun 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:1.1.10-alt1.1
- Fixed build

* Thu Jun 24 2010 Dmitry V. Levin <ldv@altlinux.org> 2:1.1.10-alt1
- Updated to xdm-1.1.10-6-g0a4c314.
- Updated build requirements.
- Rewritten /etc/pam.d/xdm.

* Tue Mar 16 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2:1.1.9-alt3.M51.2
- Applied a workaround (closes #23108), see also
  http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=363856

* Tue Jan 12 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1.9-alt4
- droped consolekit patch, used pam_ck_connector

* Mon Jan 11 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1.9-alt3
- disabled syslog
- updated build dependencies

* Tue Jan 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1.9-alt2
- fixed segfault of session exit (closes: #22362)

* Sat Sep 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1.9-alt1
- 1.1.9

* Fri Mar 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1.8-alt2.M50.1
- build for branch 5.0

* Fri Mar 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1.8-alt3
- pam: required pam_loginuid.so (close #19358)

* Tue Nov 25 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1.8-alt2
- fixed build with libXaw7

* Thu May 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1.8-alt1
- 1.1.8

* Wed Apr 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1.7-alt2
- build with ConsoleKit

* Sat Mar 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1.7-alt1
- 1.1.7
- build without ConsoleKit

* Thu Dec 13 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1.6-alt2
- support ConsoleKit

* Fri Aug 17 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1.6-alt1
- 1.1.6

* Sat Aug 11 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1.5-alt1
- 1.1.5

* Tue Jun 12 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1.4-alt4
- added xdm-1.1.4-git-policy.c.patch: fixed race condition in policy.c:Willing()

* Wed Apr 04 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1.4-alt3
- added lost %_datadir/X11/xdm dir

* Mon Mar 12 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1.4-alt2
- fixed DEF_USER_PATH and DEF_SYSTEM_PATH (clased #11060)

* Tue Feb 06 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1.4-alt1
- 1.1.4:
  + Bug #8561: xdm painfully slow at cursor redraws
  + Make sure windowPath is properly initialized & freed
  + Reset username prompt to default string at start of PAM loop
  + Rearrange checks for maximum username & password length

* Sat Dec 16 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1.3-alt1
- 1.1.3
- rename package %xorg-%name to %name

* Thu Nov 30 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1.2-alt1
- 1.1.2

* Mon Oct 16 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:1.0.5-alt1
- rollback to 1.0.5 (1.1.0 problem with pam_console)

* Fri Oct 13 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.0-alt2
- build --with-xft

* Wed Oct 04 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.0-alt1
- 1.1.0

* Fri Jun 30 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.4-alt2
- added xdm-1.0.4-setuid.patch

* Fri Apr 28 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.4-alt1
- 1.0.4

* Sun Apr 16 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.3-alt2
- CVS snapchot 2006-04-14
- fixed Provides/Obsoletes

* Sat Apr 01 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.3-alt1
- 1.0.3

* Tue Mar 28 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.2-alt1
- 1.0.2

* Thu Mar 16 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt5
- CVS snapshot 2006-03-10

* Sun Mar 05 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt4
- fixed segfault in netaddr.c:ConvertAddr if ifa_addr is NULL

* Fri Jan 13 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt3
- Rebuilt for new style PAM dependencies generated by rpm-build-4.0.4-alt55

* Mon Jan 09 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt2
- fixed BuildRequires
- added servonly patch

* Tue Dec 27 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.1-alt1
- Xorg-7.0

* Mon Dec 05 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.4-alt1
- Xorg-7.0RC3

* Wed Nov 23 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.3-alt0.1
- initial release

