Name: wmclock
Version: 1.0.16
Release: alt1

Summary: Dockable clock applet for Window Maker
License: GPL
Group: Graphical desktop/Window Maker

Url: http://www.dockapps.net/wmclock
Source: %name-%version.tar.gz
Source100: %name.watch

# Automatically added by buildreq on Mon May 29 2017
# optimized out: libX11-devel perl pkg-config python-base python-modules xorg-xextproto-devel xorg-xproto-devel
BuildRequires: libXext-devel libXpm-devel

%description
%name is an applet which displays the date and time in a dockable
tile in the same style as the clock from the NEXTSTEP(tm) operating
system.  %name is specially designed for the Window Maker window
manager, by Alfredo Kojima, and features multiple language support,
twenty-four-hour and twelve-hour (am/pm) time display, and, optionally,
can run a user-specified program on a mouse click.  %name is derived
from asclock, a similar clock for the AfterStep window manager.

%prep
%setup -c

%build
cd dockapps-*
%autoreconf
%configure --with-lang=english
%make_build

%install
cd dockapps-*
%makeinstall_std
cp -a README COPYING ..

mkdir -p %buildroot%_menudir
cat <<__EOF >%buildroot%_menudir/%name
?package(%name): command="EXEC %_bindir/wmclock" \
    needs=wmaker \
    section="Window Maker/DockApps" title="wmclock"
__EOF

%files
%doc README COPYING
%_bindir/%name
%_man1dir/%name.1*
%dir %_datadir/%name
%_datadir/%name/*
%_menudir/%name

# TODO:
# - replace debian menufile with freedesktop one some day
#   (should WindowMaker cope with that)

%changelog
* Mon May 29 2017 Michael Shigorin <mike@altlinux.org> 1.0.16-alt1
- new version (watch file uupdate)
  + bits from fedora 1.0.16 spec
- updated Url:
- dropped Packager:
- buildreq

* Mon Jun 23 2014 Michael Shigorin <mike@altlinux.org> 1.0.14-alt1
- new version (watch file uupdate)
- dropped patch (merged upstream)

* Mon Mar 25 2013 Michael Shigorin <mike@altlinux.org> 1.0.12.2-alt4
- updated BR:

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

