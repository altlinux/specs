# vim: set ft=spec: -*- rpm-spec -*-
# $Id: wmmenu,v 1.3 2005/04/11 14:36:26 raorn Exp $

Name: wmmenu
Version: 1.2
Release: alt1.qa1

Packager: Sir Raorn <raorn@altlinux.ru>

Summary: Window Maker dockable menu application
Group: Graphical desktop/Window Maker
License: GPL
Url: http://www.fcoutant.freesurf.fr/wmmenu.html

Source: http://www.fcoutant.freesurf.fr/download/%name-%version.tar.gz
Source1: %name.defaults

# Automatically added by buildreq on Mon Apr 11 2005
BuildRequires: gdk-pixbuf-devel glib-devel gtk+-devel libdockapp-devel 
BuildRequires: libXt-devel libXext-devel

%description
This is a "dock application" for Windowmaker, that provides a button bar to
launch applications from.

The bar opens automatically when either the mouse enters the button or you
click on it (this is configurable) [not yet implemented: you don't have to
click].

Multiple instances of the program can run at the same time: each one provides
a menu that it reads from a separate file, so you can have as many different
menus as you want (you can also display the same menu more than once if you
want; dunno what it's useful for...).

%prep
%setup -q -n %name

%build
%make_build ETCDIR=%_sysconfdir/X11/%name

%install
%__mkdir_p %buildroot%_sysconfdir/X11/%name
%__mkdir_p %buildroot%_x11bindir
%__mkdir_p %buildroot%_x11datadir/%name
%__mkdir_p %buildroot%_x11mandir/man1
#%__mkdir_p %buildroot

%__install -m755 wmmenu   %buildroot%_x11bindir
%__install -m755 wmmenu.1 %buildroot%_x11mandir/man1

%__install -m644 defaultIcon.xpm  %buildroot%_x11datadir/%name
%__install -m644 defaultTile.xpm  %buildroot%_x11datadir/%name
%__install -m644 target-white.xpm %buildroot%_x11datadir/%name

%__install -m644 %SOURCE1 %buildroot%_sysconfdir/X11/%name/defaults

%files
%doc COPYING README TODO example
%dir %_sysconfdir/X11/%name
%config(noreplace) %_sysconfdir/X11/%name/*
%_x11bindir/wmmenu
%dir %_x11datadir/%name
%_x11datadir/%name/*.xpm
%_x11mandir/man1/wmmenu.1*

%changelog
* Tue May 10 2011 Andrey Cherepanov <cas@altlinux.org> 1.2-alt1.qa1
- Remove xorg-x11-devel build requires

* Mon Apr 11 2005 Sir Raorn <raorn@altlinux.ru> 1.2-alt1
- [1.2]
- spec cleanup
- Updated build deps

* Fri Jan 24 2003 Alexey Voinov <voins@altlinux.ru> 0.9-alt3
- rebuilt with gcc3.2

* Tue Jul 09 2002 Sir Raorn <raorn@altlinux.ru> 0.9-alt2
- Removed apps menu from %_sysconfdir/X11/%name (wmmenu looks only in
  ~/.wmmenu for menus)
- Added BuildRequires

* Tue Jul 09 2002 Sir Raorn <raorn@altlinux.ru> 0.9-alt1
- Built for Sisyphus

