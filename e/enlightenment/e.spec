Name: enlightenment
Version: 0.16.8.9
Release: alt2
%define prefix %_x11dir
Serial: 1

Summary: The Enlightenment window manager
License: GPL
Group: Graphical desktop/Enlightenment
Url: http://www.enlightenment.org/
Packager: Pavlov Konstantin <thresh@altlinux.ru>

Source: %name-%version.2.tar.gz
Source1: Enlightenment.xpm
Source2: start%name
Source3: %name.wmsession

Source5: %name-menu.method
Source6: %name.xpm
Source7: %name-32.xpm
Source8: winter.tar

# Automatically added by buildreq on Tue Dec 14 2004
BuildRequires: esound-devel freetype2-devel imlib2-devel libaudiofile-devel zlib-devel
BuildRequires: libSM-devel libpango-devel libXft-devel libGLU-devel
BuildRequires: libXext-devel libXinerama-devel libXxf86vm-devel
BuildRequires: libXScrnSaver-devel libXrandr-devel libXcomposite-devel
BuildRequires: libXdamage-devel libXfixes-devel libXrender-devel
BuildRequires: xorg-x11-bitmaps

%description
Enlightenment is a window manager for the X Window System that is designed to
be powerful, extensible, configurable and pretty darned good looking! It is one
of the more graphically intense window managers.

Enlightenment goes beyond managing windows by providing a useful and appealing
graphical shell from which to work. It is open in design and instead of
dictating a policy, allows the user to define their own policy, down to every
last detail.

This package will install the Enlightenment window manager.

%prep
%setup -q -n %name-%version.2
%setup -q -T -D -c -n %name-%version.2 -a 8

perl -pi -e 's,/\$\(datadir\),%_datadir,g' po/Makefile.in.in
perl -pi -e 's,\${prefix}/\${DATADIRNAME}/locale,%_datadir/locale,g' configure

%build
CFLAGS="$CFLAGS -I%_includedir/gnome-1.0" LOCALEDIR=%_datadir/locale %configure \
	--prefix=%_x11dir \
	--bindir=\${prefix}/bin \
	--mandir=\${prefix}/man \
	--datadir=\${prefix}/share \
	--libexecdir=\${prefix}/lib/X11 \
	--sysconfdir=%_sysconfdir/X11/%name \
	--enable-fsstd \
	--enable-sound \
	--enable-upgrade \
	--enable-pango \
	--enable-glx \
	--with-esd-prefix=%_prefix \
	--with-imlib-prefix=%_prefix \
	--enable-zoom \
	--enable-xrandr

%make_build

%install
# configure script has a bug, localedir uses the prefix value instead
# of $prefix so it is needed to redefine it here with the build root value
%make_install install DESTDIR=%buildroot localedir=%_datadir/locale

# Menu
mkdir -p %buildroot%_sysconfdir/X11/%name/menus
perl -lwne '/^__E_CFG_VERSION 0$/ and print("$_\n\n", qw@BEGIN_NEW_FILE_MENU("ALTLINUX_MENU", "ROOT", "/etc/X11/%name/menus/altlinux.menu")@, "\nEND_MENU") or /^ADD_MENU_SUBMENU_TEXT_ITEM.*APPS_SUBMENU/ and print("$_\n", qw@ADD_MENU_SUBMENU_TEXT_ITEM("Applications",        "ALTLINUX_MENU")@) or print;' config/menus.cfg > %buildroot/%prefix/share/e16/config/menus.cfg

# Menu method
%__install -pD -m755 %SOURCE5 %buildroot%_sysconfdir/menu-methods/%name

# Install icons
%__install -pD -m644 %SOURCE6 %buildroot%_miconsdir/%name.xpm
%__install -pD -m644 %SOURCE7 %buildroot%_niconsdir/%name.xpm
%__install -pD -m644 %SOURCE1 %buildroot%_iconsdir/hicolor/64x64/apps/%name.xpm

%__install -d %buildroot%_menudir
cat << EOF > %buildroot%_menudir/%name
?package(%name): needs=wm section=Session/Windowmanagers icon=%name.xpm title=Enlightenment command=%_x11bindir/%name
EOF

# wmsession.d
%__install -p -m755 %SOURCE2 %buildroot%_x11bindir/
%__install -pD -m644 %SOURCE3 %buildroot%_sysconfdir/X11/wmsession.d/05Enlightenment

%__rm %buildroot%_x11bindir/starte16

%find_lang e16

%add_findreq_skiplist %_bindir/*.pl
%add_findreq_skiplist %_datadir/e16/E-docs/*.pl
%add_findreq_skiplist %_datadir/e16/config/*.pl
%add_findreq_skiplist %_datadir/e16/themes/*
%add_findprov_skiplist %_bindir/*.pl
%add_findprov_skiplist %_datadir/%name/E-docs/*.pl
%add_findprov_skiplist %_datadir/%name/config/*.pl
%add_findprov_skiplist %_datadir/%name/themes/*

%files -f e16.lang
%doc AUTHORS COMPLIANCE ChangeLog README
%config(noreplace) %_sysconfdir/menu-methods/*
%dir %_sysconfdir/X11/enlightenment
%config(noreplace) %_sysconfdir/X11/enlightenment/menus
%config %_sysconfdir/X11/wmsession.d/*
%_menudir/*
%_iconsdir/*/*/*/*.xpm
%_bindir/*
%_libdir/*.so
%_datadir/e16
%_datadir/xsessions/*

%changelog
* Tue Apr 19 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1:0.16.8.9-alt2
- fix build

* Sun Nov 08 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1:0.16.8.9-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for enlightenment
  * update_wms for enlightenment
  * pixmap-in-deprecated-location for enlightenment
  * postclean-05-filetriggers for spec file

* Wed Sep 19 2007 Pavlov Konstantin <thresh@altlinux.ru> 1:0.16.8.9-alt1
- 0.16.8.9 release.

* Wed Dec 15 2004 Alex Murygin <murygin@altlinux.ru> 1:0.16.7-alt1_2
- new version
- removed starte16 (due to unnecessary dependence)

* Tue Dec 14 2004 Alex Murygin <murygin@altlinux.ru> 1:0.16.7-alt1_1
- new version
- old themes moved to separate packages (upstream)
- doc files moved to separate packages (upstream)
- added russian support to default theme
- added --enable-xrandr
- spec cleaning
- added doc files
- patches rediffed
- buildreq regenerated

* Sat Dec 06 2003 Alex Murygin <murygin@altlinux.ru> 1:0.16.6-alt2
- new version
- patches rediffed
- spec cleaning

* Sun Oct 05 2003 Alex Murygin <murygin@altlinux.ru> 1:0.16.6-alt1_pre7
- new version
- patches rediffed
- added add_findreq_skip & add_findprov_skiplist macroses for polish files

* Sat Jun 14 2003 Alex Murygin <murygin@altlinux.ru> 1:0.16.6-alt1_pre3
- new version
- patches cleaning

* Sat Apr 12 2003 Alex Murygin <murygin@altlinux.ru> 1:0.16.6-alt1_pre2
- new version
- removed user check in themes installation

* Wed Apr 09 2003 Alex Murygin <murygin@altlinux.ru> 1:0.16.6-alt1_pre0
- new version
- fixed locale dir

* Thu Oct 17 2002 AEN <aen@altlinux.ru> 1:0.16.5-alt5
- rebuild in new environment

* Fri Jan 11 2002 AEN <aen@logic.ru> 1:0.16.5-alt4
- menu fixed

* Wed Jan 09 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:0.16.5-alt3
- Updated wmsession.d and startup scripts.
- Moved locale files to %_datadir/locale.
- Minor specfile cleanup.

* Fri Jan 04 2002 AEN <aen@logic.ru> 0.16.5-alt2
- patches & menu method from MDK
- move to /usr/X11R6

* Thu Oct 11 2001 AEN <aen@logic.ru> 0.16.5-alt1
- Serial 1
- rebuild with libpng.so.3

* Sat Feb 17 2001 AEN <aen@logic.ru>
- group name fixed

* Wed Dec 06 2000 AEN <aen@logic.ru>
- build for 7.2RE

* Sat Sep 30 2000 AEN <aen@logic.ru>
- 0.16.5
- clean up spec

* Fri May 12 2000 AEN <aen@logic.ru>
- built for Appendix
- po-files problem fixed
