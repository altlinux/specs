Name: openbox
Version: 3.5.0
Release: alt1.1

Summary: Openbox is a standards compliant, fast, light-weight, extensible window manager
Summary(ru_RU.UTF-8): Openbox это следующий стандартам, быстрый, лёгкий, расширяемый оконный менеджер
License: GPLv2+
Group: Graphical desktop/Other
Url: http://openbox.org/

Packager: Igor Zubkov <icesik@altlinux.org>

Source0: %name-%version.tar.gz
Source2: %name-icons.tar.bz2
Source3: %name.menu
Source4: %name.menu-method
Source5: %name.wmsession
Source6: %name-kde.wmsession
Source7: %name-gnome.wmsession

# Debian
Source11: kdetrayproxy.pod
Source12: gnome-panel-control.pod
Source13: menu.xml

# ALT Linux
Patch2: openbox-alt-menu-rc.xml.in.patch
Patch3: openbox-3.3.1-alt-TheBear-theme.patch
Patch4: openbox-3.4.4-alt-TheBear-theme-2.patch
Patch5: openbox-3.4.9-alt-desktop-file.patch

Requires: lib%name = %version-%release
# for menu "Run" item
Requires: Xdialog

Conflicts: openbox-extras

BuildPreReq: gettext >= 0.15

# Automatically added by buildreq on Tue Jan 12 2010 (-bi)
BuildRequires: cvs gnome-session imake kdebase-wm libSM-devel libXau-devel libXcursor-devel libXext-devel libXinerama-devel libXrandr-devel libpango-devel libstartup-notification-devel libxml2-devel xorg-cf-files
BuildRequires: perl-podlators

%description
Openbox is a standards compliant, fast, light-weight, extensible window manager.
Openbox works with your applications, and makes your desktop easier to manage.
This is because the approach to its development was the opposite of what seems
to be the general case for window managers. Openbox was written first to comply
with standards and to work properly. Only when that was in place did the team
turn to the visual interface.
Openbox is fully functional as a stand-alone working environment, or can be
usedas a drop-in replacement for the default window manager in the GNOME or KDE
desktop environments.

%package -n lib%name
Summary: Openbox libraries
Group: System/Libraries

%description -n lib%name
This package contains libraries for Openbox window manager:
libobparser - Openbox config file parsing library,
libobrender - Openbox Render Library.

%package -n lib%name-devel
Summary: Development files for Openbox
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains the header files and libraries for
developing with Openbox window manager.

%package -n lib%name-devel-static
Summary: Development static library for Openbox
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
This package contains static libraries for developing with
Openbox window manager.

%package kde
Summary: Run KDE with Openbox as the WM
Group: Graphical desktop/Other
Requires: %name = %version-%release

%description kde
Run KDE with Openbox as the WM.

%package gnome
Summary: Run GNOME with Openbox as the WM
Group: Graphical desktop/Other
Requires: %name = %version-%release

%description gnome
Run GNOME with Openbox as the WM.

%package autostart
Summary: XDG support for Openbox
Group: Graphical desktop/Other
Requires: %name = %version-%release
Requires: python-module-pyxdg

%description autostart
XDG support for Openbox.

%prep
%setup -q -a2
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
sed -i '/^obrender_libobrender_la_LIBADD/ a\\tobt/libobt.la \\' Makefile.am

%build
%autoreconf
%configure \
	--disable-rpath \
	--disable-static
%make_build

cp %SOURCE11 .
cp %SOURCE12 .

pod2man --section=1 --release=%version --center "Openbox documentation" kdetrayproxy.pod > kdetrayproxy.1
pod2man --section=1 --release=%version --center "Openbox documentation" gnome-panel-control.pod > gnome-panel-control.1

%install
%make_install DESTDIR=%buildroot install

rm -rf %buildroot%_datadir/doc/

# manual pages
mkdir -p %buildroot%_man1dir/
install -pD -m 644 kdetrayproxy.1 %buildroot%_man1dir/
install -pD -m 644 gnome-panel-control.1 %buildroot%_man1dir/

# icons
install -pD -m 644 %name-64.xpm %buildroot%_iconsdir/hicolor/64x64/apps/OpenBox.xpm
install -pD -m 644 %name-48.xpm %buildroot%_liconsdir/%name.xpm
install -pD -m 644 %name-32.xpm %buildroot%_niconsdir/%name.xpm
install -pD -m 644 %name-16.xpm %buildroot%_miconsdir/%name.xpm

# Menu isn't cooked yet, because it's hard to implement menu-method
# for Openbox XML based menu
install -pD -m 755 %SOURCE4 %buildroot%_sysconfdir/menu-methods/%name
install -pD -m 644 %SOURCE5 %buildroot%_sysconfdir/X11/wmsession.d/09%name
install -pD -m 644 %SOURCE6 %buildroot%_sysconfdir/X11/wmsession.d/10%name-kde
install -pD -m 644 %SOURCE7 %buildroot%_sysconfdir/X11/wmsession.d/11%name-gnome

mkdir -p %buildroot%_sysconfdir/xdg/openbox/

install -pD -m 644 %SOURCE13 %buildroot%_sysconfdir/xdg/openbox/

%find_lang --output=%name.lang %name

%files -f %name.lang
%doc AUTHORS CHANGELOG COMPLIANCE README
%doc data/menu.xsd doc/rc-mouse-focus.xml data/rc.xsd data/xbm
%_sysconfdir/xdg/openbox/*
%config(noreplace) %_sysconfdir/menu-methods/*
%config %_sysconfdir/X11/wmsession.d/09openbox
%_bindir/*
%exclude %_bindir/openbox-kde-session
%exclude %_bindir/openbox-gnome-session
%exclude %_bindir/gdm-control
%exclude %_bindir/gnome-panel-control
%_man1dir/*
%exclude %_man1dir/openbox-kde-session.*
%exclude %_man1dir/openbox-gnome-session.*
%exclude %_man1dir/gnome-panel-control.*
%_datadir/gnome/wm-properties/*
%_datadir/pixmaps/*
%_datadir/themes/*
%_liconsdir/%name.xpm
%_niconsdir/%name.xpm
%_iconsdir/hicolor/64x64/apps/OpenBox.xpm
%_miconsdir/%name.xpm
%_datadir/xsessions/openbox.desktop
%_datadir/applications/openbox.desktop

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_pkgconfigdir/*
%_libdir/*.so
%_includedir/*

%files kde
%config %_sysconfdir/X11/wmsession.d/10openbox-kde
%_bindir/openbox-kde-session
%_datadir/xsessions/openbox-kde.desktop
%_man1dir/openbox-kde-session.*

%files gnome
%config %_sysconfdir/X11/wmsession.d/11openbox-gnome
%_bindir/openbox-gnome-session
%_bindir/gdm-control
%_bindir/gnome-panel-control
%_datadir/xsessions/openbox-gnome.desktop
%_man1dir/openbox-gnome-session.*
%_man1dir/gnome-panel-control.*

%files autostart
%_libexecdir/openbox-xdg-autostart
%_libexecdir/openbox-autostart

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.0-alt1.1
- Rebuild with Python-2.7

* Fri Aug 05 2011 Mykola Grechukh <gns@altlinux.ru> 3.5.0-alt1
3.4.11.1 -> 3.5.0

* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 3.4.11.1-alt1.1.1
- repair after perl 5.12 upgrade using girar-nmu

* Wed Nov 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.11.1-alt1.1
- Rebuilt for soname set-versions

* Tue Apr 20 2010 Mykola Grechukh <gns@altlinux.ru> 3.4.11.1-alt1
- new version

* Sat Jan 23 2010 Igor Zubkov <icesik@altlinux.org> 3.4.10-alt2
- update Url:

* Tue Jan 12 2010 Igor Zubkov <icesik@altlinux.org> 3.4.10-alt1
- 3.4.9 -> 3.4.10

* Thu Dec 24 2009 Igor Zubkov <icesik@altlinux.org> 3.4.9-alt2
- fix desktop file

* Sat Dec 19 2009 Igor Zubkov <icesik@altlinux.org> 3.4.9-alt1
- 3.4.7.2 -> 3.4.9

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.7.2-alt5.qa1.1
- Rebuilt with python 2.6

* Sun Nov 08 2009 Repocop Q. A. Robot <repocop@altlinux.org> 3.4.7.2-alt5.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for openbox
  * postclean-05-filetriggers for spec file

* Thu Mar 26 2009 Igor Zubkov <icesik@altlinux.org> 3.4.7.2-alt5
- add Conflicts with openbox-extras

* Tue Dec 02 2008 Igor Zubkov <icesik@altlinux.org> 3.4.7.2-alt4
- apply patch from repocop
- buildreq

* Tue Dec 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 3.4.7.2-alt3.1
- NMU:
  * updated build dependencies

* Sat Jun 21 2008 Igor Zubkov <icesik@altlinux.org> 3.4.7.2-alt3
- move kde and gnome parts to subpackages (closes #15771)

* Fri May 23 2008 Igor Zubkov <icesik@altlinux.org> 3.4.7.2-alt2
- add BuildRequires: gettext >= 0.15 (closes #15762)

* Thu Apr 24 2008 Igor Zubkov <icesik@altlinux.org> 3.4.7.2-alt1
- 3.4.7.1 -> 3.4.7.2

* Thu Apr 17 2008 Igor Zubkov <icesik@altlinux.org> 3.4.7.1-alt1
- 3.4.7 -> 3.4.7.1

* Wed Apr 16 2008 Igor Zubkov <icesik@altlinux.org> 3.4.7-alt1
- 3.4.6.1 -> 3.4.7
- buildreq

* Thu Feb 21 2008 Igor Zubkov <icesik@altlinux.org> 3.4.6.1-alt1
- 3.4.5 -> 3.4.6.1

* Tue Jan 08 2008 Igor Zubkov <icesik@altlinux.org> 3.4.5-alt1
- 3.4.4 -> 3.4.5

* Wed Nov 14 2007 Igor Zubkov <icesik@altlinux.org> 3.4.4-alt2
- bump release

* Tue Nov 13 2007 Igor Zubkov <icesik@altlinux.org> 3.4.4-alt1
- 3.3.1 -> 3.4.4
- "Run" and "Terminal" menu items (bga@)
- buildreq

* Tue Nov 13 2007 Igor Zubkov <icesik@altlinux.org> 3.3.1-alt6
- clean up spec file

* Wed May 23 2007 Igor Zubkov <icesik@altlinux.org> 3.3.1-alt5
- buildreq to fix rebuild

* Tue Apr 10 2007 Igor Zubkov <icesik@altlinux.org> 3.3.1-alt4
- add TheBear theme from old openbox source package (closes #11379)

* Thu Nov 02 2006 Igor Zubkov <icesik@altlinux.org> 3.3.1-alt3
- add menu method from debian (closes #10332)

* Sat Oct 28 2006 Igor Zubkov <icesik@altlinux.org> 3.3.1-alt2
- sync with debian openbox_3.3-2
  + add manual pages (closes #10333)

* Fri Sep 08 2006 Igor Zubkov <icesik@altlinux.ru> 3.3.1-alt1
- 3.3 -> 3.3.1
- buildreq

* Wed Sep 06 2006 Igor Zubkov <icesik@altlinux.ru> 3.3-alt4
- s/ru_RU.KOI8-R/ru_RU.UTF-8/
- buildreq

* Tue Aug 29 2006 Igor Zubkov <icesik@altlinux.ru> 3.3-alt3
- 3.3rc2 -> 3.3
- convert spec to utf-8

* Fri May 26 2006 Igor Zubkov <icesik@altlinux.ru> 3.3-alt2.rc2
- x86_64 fix

* Fri Mar 17 2006 Igor Zubkov <icesik@altlinux.ru> 3.3-alt1.rc2
- 3.3rc2
- move binary from /usr/X11R6/bin/ to /usr/bin/
- update url
- buildreq
- fix build with new ld / -Wl,--as-needed

* Thu Jan 22 2004 Anton V. Denisov <avd@altlinux.org> 3.1-alt1.1
- BuildRequires tuned by hands in hope what
  /usr/lib/pkgconfig/xft.pc is in XFree86-devel package in
  current Sisyphus (I have ALT Linux Sisyphus (20030704)).

* Tue Jan 20 2004 Anton V. Denisov <avd@altlinux.org> 3.1-alt1
- Initial release for ALT Linux Sisyphus.
- TODO:
  + Menu system (it's hard because Openbox use XML based menu);
  + Russian translation for %%description.
