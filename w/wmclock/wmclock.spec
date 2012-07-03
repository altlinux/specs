# vim: set ft=spec: -*- mode: rpm-spec; -*-
# $Id: wmclock,v 1.3 2006/02/06 07:50:11 raorn Exp $

Name: wmclock
Version: 1.0.12.2
Release: alt3

Summary: Dockable clock applet for Window Maker
License: GPL
Group: Graphical desktop/Window Maker

Url: http://www.jmknoble.net/WindowMaker/wmclock
Source: %url/%name-%version.tar.gz
Patch: wmclock-1.0.12.2-debian-nopolling.patch
Packager: Sir Raorn <raorn@altlinux.ru>

# Automatically added by buildreq on Mon Feb 06 2006
BuildRequires: gccmakedep imake libX11-devel libXext-devel libXpm-devel xorg-cf-files xorg-x11-proto-devel

%description
%name is an applet which displays the date and time in a dockable
tile in the same style as the clock from the NEXTSTEP(tm) operating
system.  %name is specially designed for the Window Maker window
manager, by Alfredo Kojima, and features multiple language support,
twenty-four-hour and twelve-hour (am/pm) time display, and, optionally,
can run a user-specified program on a mouse click.  %name is derived
from asclock, a similar clock for the AfterStep window manager.

%prep
%setup
%patch -p1

%build
./configure --lang english
%make_build

%install
%makeinstall_std install.man install.share

mkdir -p %buildroot%_menudir
cat <<__EOF >%buildroot%_menudir/%name
?package(%name): command="EXEC %_bindir/wmclock" \
    needs=wmaker \
    section="Window Maker/DockApps" title="wmclock"
__EOF

%files
%_bindir/%name
%_man1dir/%name.1*
%dir %_datadir/%name
%_datadir/%name/*
%_menudir/%name

# TODO:
# - replace debian menufile with freedesktop one some day
#   (should WindowMaker cope with that)

%changelog
* Mon Sep 14 2009 Michael Shigorin <mike@altlinux.org> 1.0.12.2-alt3
- built for Sisyphus (closes: #16028)

* Sat Jan 17 2009 Michael Shigorin <mike@altlinux.org> 1.0.12.2-alt2.1
- NMU: applied debian nopolling patch
  + see project webpage
  + commented out debug messages (~/.xsession-errors:$DISPLAY)
- added Packager:
- updated Url:

* Mon Feb 06 2006 Sir Raorn <raorn@altlinux.ru> 1.0.12.2-alt2
- Rebuilt with new Xorg, buildreqs updated

* Tue Sep 23 2003 Sir Raorn <raorn@altlinux.ru> 1.0.12.2-alt1
- Built for Sisyphus

