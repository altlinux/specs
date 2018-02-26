Name: wmnd
Version: 0.4.17
Release: alt1

Summary: WindowMaker dock-app for network device traffic monitoring
License: GPL
Group: Graphical desktop/Window Maker

Url: http://www.thregr.org/~wavexx/software/wmnd/
Source0: %name-%version.tar
Source1: %name.menu
Packager: Alexey Voinov <voins@altlinux.ru>

# Automatically added by buildreq on Fri Mar 07 2008
BuildRequires: imake libSM-devel libXext-devel libXpm-devel xorg-cf-files

#BuildRequires: libdockapp-devel

%description
The wmnd is a WindowMaker dock-app for network device traffic
monitoring. The wmnd is originally based on WMiFS 1.3b but has been
almost re-written after version 0.2.0 to improve the performance.
Opinions and suggestions are welcome.

%prep
%setup

%build
%configure --enable-drivers=linux_proc
make

%install
%makeinstall_std
install -pDm644 %SOURCE1 %buildroot%_menudir/%name
rm -f %buildroot%_defaultdocdir/%name/examples/wmndrc

%files
%doc AUTHORS ChangeLog examples/ INSTALL NEWS README TODO
%_bindir/*
%_man1dir/*
%_menudir/*

%changelog
* Sat Jun 16 2012 Michael Shigorin <mike@altlinux.org> 0.4.17-alt1
- 0.4.17

* Wed Apr 07 2010 Michael Shigorin <mike@altlinux.org> 0.4.15-alt1
- 0.4.15
- dropped obsolete patch

* Tue Mar 30 2010 Michael Shigorin <mike@altlinux.org> 0.4.14-alt1
- 0.4.14
- minor spec cleanup

* Sat Nov 07 2009 Alexey Voinov <voins@altlinux.ru> 0.4.13-alt2
- update_menus removed

* Sun Mar 09 2008 Alexey Voinov <voins@altlinux.ru> 0.4.13-alt1
- Thanks to mike@altlinux.org for spec update
- new version (0.4.13)
  + fixed crashes under 64bit OSes
  + fixed incorrect displays under Linux
  + enhanced trend support
- minor spec cleanup
- buildreq

* Tue Jun 12 2007 Alexey Voinov <voins@altlinux.ru> 0.4.12-alt2
- updated ./configure options [#12004]
- /usr/X11R6 -> /usr

* Mon Jun 04 2007 Alexey Voinov <voins@altlinux.ru> 0.4.12-alt1
- new version (0.4.12)
- nozombies patch no longer needed
- buildreqs updated

* Sat Sep 03 2005 Alexey Voinov <voins@altlinux.ru> 0.4.11-alt2
- nozombies patch added [#7268]

* Fri Oct 22 2004 Alexey Voinov <voins@altlinux.ru> 0.4.11-alt1
- new version (0.4.11)

* Mon Sep 20 2004 Alexey Voinov <voins@altlinux.ru> 0.4.10-alt1
- new version (0.4.10)

* Mon May 24 2004 Alexey Voinov <voins@altlinux.ru> 0.4.9-alt1
- new version (0.4.9)

* Wed Apr 21 2004 Alexey Voinov <voins@altlinux.ru> 0.4.8-alt2
- remove prefix redefinition. this fixes post/postun scripts.

* Wed Apr 14 2004 Alexey Voinov <voins@altlinux.ru> 0.4.8-alt1
- new version (0.4.7)
- url tag fixed

* Thu Jun 05 2003 Alexey Voinov <voins@voins.program.ru> 0.4.7-alt1
- new version (0.4.7)

* Sat May 24 2003 Alexey Voinov <voins@voins.program.ru> 0.4.6-alt1
- new version (0.4.6)

* Thu Jan 16 2003 Alexey Voinov <voins@voins.program.ru> 0.4.4-alt1
- new version (0.4.4) (This fixes bug#0001876)

* Mon Oct 14 2002 Alexey Voinov <voins@voins.program.ru> 0.4.3-alt2
- manually enable linux_proc driver, because i don't have access
  to /proc/net/dev on altair, and configure cannot determine needed
  drivers automatically (fixes bug #1374)

* Sun Oct 06 2002 Alexey Voinov <voins@voins.program.ru> 0.4.3-alt1
- new version(0.4.3)
- spec clean up
- autodock patch removed

* Fri Sep 14 2001 Alexey Voinov <voins@voins.program.ru>
- autodock patch added

* Sat Jun  9 2001 Alexey Voinov <voins@voins.program.ru>
- menu rearranged

* Thu May 3 2001 Alexey Voinov <voins@voins.program.ru>
- initial build

