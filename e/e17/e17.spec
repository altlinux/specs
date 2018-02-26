%define _name enlightenment
%define cvs_date 20070918
%undefine cvs_date
%define snapshot 2012-04-26
%define rel alt1

%def_disable static

# TODO: pam CoreFoundation

Name: e17
Version: 0.16.999.70492

%ifdef cvs_date
Release: %rel.%cvs_date
%else
Release: %rel
%endif
Serial: 1

Summary: The Enlightenment window manager
License: BSD
Group: Graphical desktop/Enlightenment
URL: http://www.enlightenment.org/

Source: http://download.enlightenment.org/snapshots/%snapshot/%_name-%version.tar.bz2
Patch: e17-default-menus.patch

Source1: E-17.xpm
Source2: start%name
Source3: %name.wmsession
Source6: %name.xpm
Source7: %name-32.xpm
Source8: %_name.desktop
Source9: %_name-wm.desktop

Requires: edbus
# for menu
Requires: wm-common-freedesktop
Requires: altlinux-freedesktop-menu-%_name

BuildPreReq: libeet-devel >= 1.6.0
BuildPreReq: libecore-devel >= 1.2.0
BuildRequires: libpam-devel libX11-devel libevas-devel libecore-devel
BuildRequires: edje libedje-devel libeet-devel libeet-utils libembryo-devel libefreet-devel
BuildRequires: libXext-devel embryo_cc libdbus-devel libedbus-devel
BuildRequires: libalsa-devel libeina-devel libeeze-devel libudev-devel

%description
Enlightenment is a window manager.
E-17 is a non-stable Enlightenment version from CVS.
	
%package devel
Summary: Development headers for Enlightenment.
Group: Development/C
Requires: %name = %version-%release

%description devel
Development headers for Enlightenment.

%package gnome
Summary: GNOME-specific parts of Enlightenment
Group: Graphical desktop/GNOME
BuildArch: noarch
Provides: gnome-wm
Requires: %name = %version-%release
Requires: gnome-session >= 2.24

%description gnome
Install this package and run:
"gconftool-2 --set --type string /desktop/gnome/session/required_components/windowmanager enlightenment"
to use Enlightenment as windowmanager in GNOME session

%prep
%ifdef cvs_date
%setup -q -n %_name
%else
%setup -q -n %_name-%version
%endif

%patch -b .menus

%build
%autoreconf
export CFLAGS="$CFLAGS `pkg-config --cflags dbus-1`"
%configure \
	--with-profile=FAST_PC \
	--enable-files \
	%{subst_enable static} \
	--enable-shared
%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang enlightenment

mkdir -p %buildroot%_sysconfdir/X11/wmsession.d
mkdir -p %buildroot%_bindir/
install -p -m755 %SOURCE2 %buildroot%_bindir/
install -D -pm 644 %SOURCE3 %buildroot%_sysconfdir/X11/wmsession.d/05E-17

# Install icons
install -pD -m644 %SOURCE6 %buildroot%_miconsdir/%name.xpm
install -pD -m644 %SOURCE7 %buildroot%_niconsdir/%name.xpm
install -p -m644 %SOURCE1 %buildroot%_niconsdir/

# desktop file
install -pD -m 644 %SOURCE8 %buildroot%_datadir/applications/enlightenment.desktop
# be gnome-wm
install -pD -m 644 %SOURCE9 %buildroot%_datadir/gnome/wm-properties/enlightenment-wm.desktop

%find_lang enlightenment

%files -f enlightenment.lang
%config %_sysconfdir/X11/wmsession.d/*
%config %_sysconfdir/enlightenment/sysactions.conf
%dir %_libdir/enlightenment/
%_libdir/enlightenment/*
%_niconsdir/*.xpm
%_miconsdir/*.xpm
%_bindir/*
%_datadir/enlightenment/
%_datadir/xsessions/enlightenment.desktop
%_datadir/applications/*.desktop
%doc AUTHORS COPYING README

%files devel
%dir %_includedir/enlightenment/
%_includedir/enlightenment/*.h
%_libdir/pkgconfig/enlightenment.pc
%_libdir/pkgconfig/everything.pc

%files gnome
%_datadir/gnome/wm-properties/*.desktop

%changelog
* Fri May 11 2012 Yuri N. Sedunov <aris@altlinux.org> 1:0.16.999.70492-alt1
- 0.16.999.70492

* Mon Dec 05 2011 Yuri N. Sedunov <aris@altlinux.org> 1:0.16.999.65643-alt1
- 0.16.999.65643

* Sun May 01 2011 Yuri N. Sedunov <aris@altlinux.org> 1:0.16.999.55225-alt2
- set default_system_menu to enlightenment-applications.menu,
  requires wm-common-freedesktop and altlinux-freedesktop-menu-enlightenment (ALT #16132)

* Sun Jan 30 2011 Yuri N. Sedunov <aris@altlinux.org> 1:0.16.999.55225-alt1
- 0.16.999.55225

* Thu Nov 18 2010 Yuri N. Sedunov <aris@altlinux.org> 1:0.16.999.54504-alt1
- 0.16.999.54504

* Fri Oct 29 2010 Yuri N. Sedunov <aris@altlinux.org> 1:0.16.999.52995-alt1
- new snapshot

* Mon Jan 04 2010 Yuri N. Sedunov <aris@altlinux.org> 1:0.16.999.063-alt1
- new version

* Tue Nov 10 2009 Yuri N. Sedunov <aris@altlinux.org> 1:0.16.999.062-alt1
- new version
- removed obsolete %%update_wms calls
- icons moved in proper location

* Thu Nov 13 2008 Yuri N. Sedunov <aris@altlinux.org> 1:0.16.999.050-alt2
- new e17-gnome package to be gnome-wm as metacity or sawfish. Install this package and do
  "gconftool-2 --set --type string /desktop/gnome/session/required_components/windowmanager enlightenment" to take effect
- install desktop-file instead old menu-file
- remove post{,un}_ldconfig, {update,clean}_menus calls

* Sat Oct 18 2008 Yuri N. Sedunov <aris@altlinux.org> 1:0.16.999.050-alt1
- 0.16.999.050
- added serial due to version downgrade
- don't use bundled vera font, it doesn't support national glyphs

* Wed Sep 19 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.17.0.pre10-alt1.20070918
- CVS from 20070918.

* Tue Jul 31 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.17.0.pre10-alt1.20070731
- CVS from 20070731.

* Wed May 16 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.17.0.pre10-alt1.20070516
- CVS from 20070516.

* Thu May 10 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.17.0.pre10-alt1.20070509
- CVS from 20070509.
- Fix BuildRequires.
- Fix --as-needed problems.

* Wed Sep 20 2006 Igor Zubkov <icesik@altlinux.org> 0.17.0.pre10-alt1.20060920
- 20060910 -> 20060920

* Tue Sep 12 2006 Igor Zubkov <icesik@altlinux.org> 0.17.0.pre10-alt1.20060910
- update from cvs (20060327 -> 20060910)
- buildreq

* Mon Apr 10 2006 Igor Zubkov <icesik@altlinux.ru> 0.17.0.pre10-alt1.20060327
- update from cvs

* Mon May 30 2005 Denis Klykvin <nikon@altlinux.ru> 0.17.0.pre10-alt1.20050530
- updated from cvs.

* Mon May 16 2005 Denis Klykvin <nikon@altlinux.ru> 0.17.0.pre10-alt1.20050516
- updated from cvs.


* Mon May 16 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.17.0.pre10-alt1.1.20050428
-  small fixes in the spec (wmsession.d path corrected).
-  %_menudir filesystem intersections repaired.

* Sat May 14 2005 Denis Klykvin <nikon@altlinux.ru> 0.17.0.pre10-alt1.20050514
- updated from cvs.

* Thu Apr 28 2005 Denis Klykvin <nikon@altlinux.ru> 0.17.0.pre10-alt1.20050428
- updated from cvs.

* Mon Apr 25 2005 Denis Klykvin <nikon@altlinux.ru> 0.17.0.pre10-alt1.20050425
- updated from cvs.

* Thu Apr 21 2005 Denis Klykvin <nikon@altlinux.ru> 0.17.0.pre10-alt1.20050421
- updated from cvs.

* Mon Apr 11 2005 Denis Klykvin <nikon@altlinux.ru> 0.17.0_pre10-alt1.cvs20050420
- Initial build from CVS

* Tue Mar 29 2005 Alex Murygin <murygin@altlinux.ru> 1:0.16.999-alt0.1_003_20050329
- updated from cvs.
- added serial due to version downgrade
- added lib%name and lib%name-devel packages

* Sat Jan 22 2005 Alex Murygin <murygin@altlinux.ru> 0.17.0-alt0.1_pre10_20050122
- updated from cvs.

* Fri Jun 13 2003 Alex Murygin <murygin@altlinux.ru> 0.17.0-alt0.1_20030613
- Updated from cvs.
- Moved to /usr/X11 dir
- added check to fam

* Sat Mar 15 2003 Alex Murygin <murygin@altlinux.ru> 0.17.0-alt0.1_20030530
- Updated from cvs.
- Fix borders
- Fix font link
- Add menu-method support
- Change standart font borzoib.ttf for n019003l.ttf (val-ttf)
- Added requires to efsd, imlib2_loaders

* Sat Nov 23 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.17.0-alt0.1_20021123
- First build for Sisyphus.
