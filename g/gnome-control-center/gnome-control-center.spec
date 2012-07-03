%define _name control-center
%define ver_major 3.4
%define api_ver 2.0

%def_disable debug
%def_disable static
%def_with libsocialweb
%def_with cheese
%def_enable systemd

Name: gnome-control-center
Version: %ver_major.2
Release: alt1

Summary: GNOME Control Center
License: GPLv2+
Group: Graphical desktop/GNOME
Url: http://www.gnome.org
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

# git archive --format=tar --prefix=gnome-control-center-3.2.2/ --output=gnome-control-center-3.2.2.tar HEAD
#Source: %name-%version.tar
Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

# From configure.ac
%define gtk_ver 3.3.5
%define glib_ver 2.29.14
%define desktop_ver 3.3.90
%define fontconfig_ver 1.0.0
%define xft_ver 2.1.2
%define gnome_menu_ver 3.3.5
%define libmetacity_ver 2.30.0
%define libgnomekbd_ver 3.3.90
%define libxklavier_ver 5.2.1
%define gsds_ver 3.3.90
%define notify_ver 0.7.3
%define nm_ver 0.9.1.90
%define goa_ver 3.2.0
%define sett_daemon_ver 3.3.92
%define cheese_ver 3.2.0
%define bt_ver 3.3.4
%define systemd_ver 40

Requires: %name-data = %version-%release

# For /usr/share/gnome
Requires: gnome-filesystem
Requires: gnome-settings-daemon >= %sett_daemon_ver
# for graphical passwd changing apps
Requires: accountsservice
#Requires: userpasswd
Requires: gnome-online-accounts >= %goa_ver
%{?_with_cheese:Requires: cheese >= %cheese_ver}
BuildPreReq: rpm-build-gnome >= 0.9

# From configure.in
BuildPreReq: intltool >= 0.37.1 gnome-common desktop-file-utils gnome-doc-utils gtk-doc
BuildPreReq: fontconfig-devel >= %fontconfig_ver
BuildPreReq: libXft-devel >= %xft_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: libgnome-menus-devel >= %gnome_menu_ver
BuildPreReq: libgnome-desktop3-devel >= %desktop_ver
BuildPreReq: libgnomekbd-devel >= %libgnomekbd_ver
BuildPreReq: libxklavier-devel >= %libxklavier_ver
BuildPreReq: gsettings-desktop-schemas-devel >= %gsds_ver
BuildPreReq: libnotify-devel >= %notify_ver
BuildPreReq: gnome-settings-daemon-devel >= %sett_daemon_ver
%{?_with_cheese:BuildPreReq: libcheese-devel >= %cheese_ver}
BuildRequires: libGConf-devel libdbus-glib-devel libupower-devel libpolkit1-devel
BuildRequires: libgio-devel librsvg-devel libxml2-devel libcanberra-gtk3-devel
BuildRequires: libX11-devel libXext-devel libSM-devel libXScrnSaver-devel libXt-devel
BuildRequires: libXft-devel libXi-devel libXrandr-devel libXrender-devel libXcursor-devel libXcomposite-devel
BuildRequires: libgtop-devel libcups-devel libpulseaudio-devel iso-codes-devel
# for test-endianess
BuildRequires: glibc-i18ndata
BuildRequires: libnm-gtk-devel >= %nm_ver
BuildRequires: libgnome-online-accounts-devel >= %goa_ver colord-devel
BuildRequires: libgnome-bluetooth-devel >= %bt_ver
BuildRequires: libwacom-devel
BuildRequires: libclutter-gst-devel
%{?_with_libsocialweb:BuildRequires: libsocialweb-devel}
%{?_enable_systemd:BuildRequires: systemd-devel >= %systemd_ver}

%description
GNOME (the GNU Network Object Model Environment) is an attractive and
easy-to-use GUI desktop environment. The control-center package
provides the GNOME Control Center utilities that allow you to setup
and configure your system's GNOME environment (things like the desktop
background and theme, the screensaver, the window manager, system
sounds, and mouse behavior).

If you install GNOME, you need to install control-center.

%package data
Summary: Arch independent files for GNOME Control Center
Group: Networking/Instant messaging
BuildArch: noarch

%description data
This package provides noarch data needed for GNOME Control Center to work.

%package devel
Summary: GNOME Control Center development files
Group: Development/GNOME and GTK+
BuildArch: noarch
Requires: %name = %version-%release

%description devel
If you're interested in developing panels for the GNOME control center,
you'll want to install this package.

%name-devel helps you create the panels for the control center.

%prep
%setup

%build
#NOCONFIGURE=1 ./autogen.sh
%autoreconf
%configure \
	%{subst_enable debug} \
	%{subst_enable static} \
	--disable-update-mimedb \
	%{subst_with libsocialweb} \
	%{subst_with cheese} \
	%{subst_enable systemd}

%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang --with-gnome --output=%name.lang %name-%api_ver %name-%api_ver-timezones %_name


%files
%_bindir/*
%dir %_libdir/control-center-1/panels
%_libdir/control-center-1/panels/libbackground.so
%_libdir/control-center-1/panels/libbluetooth.so
%_libdir/control-center-1/panels/libcolor.so
%_libdir/control-center-1/panels/libdate_time.so
%_libdir/control-center-1/panels/libdisplay.so
%_libdir/control-center-1/panels/libinfo.so
%_libdir/control-center-1/panels/libkeyboard.so
%_libdir/control-center-1/panels/libmouse-properties.so
%_libdir/control-center-1/panels/libnetwork.so
%_libdir/control-center-1/panels/libonline-accounts.so
%_libdir/control-center-1/panels/libpower.so
%_libdir/control-center-1/panels/libprinters.so
%_libdir/control-center-1/panels/libregion.so
%_libdir/control-center-1/panels/libscreen.so
%_libdir/control-center-1/panels/libsound.so
%_libdir/control-center-1/panels/libuniversal-access.so
%_libdir/control-center-1/panels/libuser-accounts.so
%_libdir/control-center-1/panels/libwacom-properties.so

%exclude %_libdir/control-center-1/panels/*.la

%files data -f %name.lang
%dir %_datadir/%name
%_datadir/%name/ui
# need to move to ui subdir
%_datadir/%name/bluetooth.ui
%_datadir/%name/keybindings
%_datadir/%name/pixmaps
%dir %_datadir/%name/sounds
%_datadir/%name/sounds/gnome-sounds-default.xml
%dir %_datadir/%name/datetime
%_datadir/%name/datetime/backward
%_datadir/%name/icons/
%_desktopdir/*.desktop
%_sysconfdir/xdg/menus/gnomecc.menu
%_datadir/desktop-directories/*
%_sysconfdir/xdg/autostart/gnome-sound-applet.desktop
%_datadir/pixmaps/faces/
%_iconsdir/hicolor/*/*/*
%_datadir/sounds/gnome/default/alerts/*.ogg
%_datadir/polkit-1/actions/org.gnome.controlcenter.datetime.policy
%doc AUTHORS NEWS README

%files devel
%_datadir/pkgconfig/gnome-keybindings.pc

%changelog
* Tue May 15 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Tue Apr 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon Mar 19 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.92-alt1
- 3.3.92

* Sat Dec 03 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt2
- updated from upstream git (fixed some GNOME and RH bugs)
- added gnome-online-accounts to reqs
- enabled cheese webcam support
- split up noarch data in separate -data subpackage

* Wed Nov 09 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Mon Oct 17 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Mon Sep 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Thu Sep 01 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.90-alt1
- 3.1.90
- no more -devel-doc subpackage

* Wed Aug 24 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt2
- updated from upstream git

* Tue May 24 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Sat Apr 30 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.1.1-alt1
- 3.0.1.1

* Sat Apr 30 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt2
- using URL handlers for browsers and mailers to be compatible with
  glib-2.28
- updated russian translation from git

* Thu Nov 18 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1
- 2.32.1

* Tue Oct 05 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Sun May 02 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt2
- fixed translation error (patch0)

* Tue Apr 27 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Mon Mar 29 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Tue Mar 16 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.92-alt2
- new desktop-effects-integration.patch (tnx to Valery V. Inozemtsev)

* Mon Mar 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.92-alt1
- 2.29.92

* Sat Feb 27 2010 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt3
- fixed find_lang usage

* Thu Feb 25 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.91-alt1
- 2.29.91

* Mon Feb 08 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.90-alt1
- 2.29.90

* Tue Jan 26 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.6-alt1
- 2.29.6

* Thu Dec 24 2009 Yuri N. Sedunov <aris@altlinux.org> 2.29.4-alt1
- 2.29.4
- temporarily disabled compiz configuration dialog patch
- updated buildreqs

* Tue Oct 20 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1

* Mon Sep 28 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.28.0-alt2
- readded compiz configuration dialog

* Mon Sep 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Mon Aug 24 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.91-alt1
- 2.27.91

* Mon Aug 17 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.90-alt1
- 2.27.90

* Wed Jun 03 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt3
- added russian translation for compiz configuration dialog (shrek@)

* Fri May 29 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt2
- removed dependence on xscreensaver
- implemented compiz configuration dialog based on ubuntu
  95_desktop-effects-integration.patch (tnks to Valery V. Inozemtsev)
- applied ubuntu patches add touchpad configuration
- updated buildreqs

* Tue Mar 17 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Tue Mar 03 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.92-alt1
- 2.25.92

* Tue Jan 27 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.3-alt1
- 2.25.3
- removed obsolete %%post{,un} scripts
- updated buildreqs

* Sun Oct 26 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.0.1-alt3
- rebuild

* Tue Sep 30 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.0.1-alt2
- fix schemas list

* Sun Sep 28 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.0.1-alt1
- 2.24.0.1

* Sun Sep 07 2008 Yuri N. Sedunov <aris@altlinux.org> 2.22.2.1-alt2
- fix gnome bug #529773 (requires patched libxklavier-3.7)
- small fix in russian translation.

* Fri May 30 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.2.1-alt1
- 2.22.2.1
- make about me capplet use userpasswd for passwords (patch7)(#15742)
- fix problems with the home address not being saved,
  and addresses being swapped or the like (patch8) (GNOME #317835,#15742)

* Mon Apr 14 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.1-alt1
- 2.22.1
- changed path background(updated patch5)
- updated randr patch

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 2.22.0-alt1.1.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for gnome-control-center

* Tue Mar 18 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1.1
- build for Sisyphus

* Fri Mar 14 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1
- new version (2.22.0)

* Mon Mar 10 2008 Alexey Shabalin <shaba@altlinux.ru> 2.21.92-alt1
- new version (2.21.92)
- remove package gnome-setting-daemon
- update section %%files

* Mon Feb 04 2008 Alexey Shabalin <shaba@altlinux.ru> 2.20.3-alt1
- new version (2.20.3)
- removed patches:
  + for RH bug #330501 (more key defaults) (fixed upstream)
  + for GNOME bug #489973 (orca command) (fixed upstream)

* Tue Dec 11 2007 Alexey Shabalin <shaba@altlinux.ru> 2.20.1-alt1
- new version (2.20.1)
- add Packager
- add patches from fedora8
- disabled patch1 (control-center-2.18-custom-keybinding.diff)
- add a "valid" OnlyShowIn entry, otherwise desktop-file-install complains 
- fix section files
- update buildreq

* Sun Jul 01 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.1-alt1
- new version (2.18.1)
- updated dependencies
- applied a patch from OpenSolaris that enables editing custom keybindings.
- invoke gnome-doc-prepare and autoreconf to get around GNOME Bug 427939
- use new macros from rpm-build-gnome
- gnome-settings-daemon now resides in its own subpackage; maintainers of GNOME
  programs that interact with it are encouraged to add a corresponding Requires
- updated the files list and the schemas list; schemas list is split into two,
  one for g-s-d, the other one installed with control-center.

* Wed Apr 25 2007 Alexey Rusakov <ktirf@altlinux.org> 2.16.3-alt4
- fixed bug #11610

* Tue Apr 10 2007 Alexey Rusakov <ktirf@altlinux.org> 2.16.3-alt3
- switched debug off by default

* Wed Apr 04 2007 Alexey Rusakov <ktirf@altlinux.org> 2.16.3-alt2
- introduced 'debug' switch.

* Thu Feb 01 2007 Alexey Rusakov <ktirf@altlinux.org> 2.16.3-alt1
- new version 2.16.3 (with rpmrb script)

* Wed Dec 27 2006 Alexey Rusakov <ktirf@altlinux.org> 2.16.2-alt2
- rebuild with new dbus

* Thu Dec 21 2006 Alexey Rusakov <ktirf@altlinux.org> 2.16.2-alt1
- new version 2.16.2 (with rpmrb script)

* Tue Oct 03 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.1-alt1
- new version 2.16.1 (with rpmrb script)

* Sat Sep 23 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.0-alt3
- enabled aboutme capplet
- let pkgconfig handle dependencies of the -devel subpackage.
- added gnome-filesystem as a container of /usr/share/gnome path.
- added /usr/share/gnome/help/control-center to the files list.
- gnome-settings-daemon now lives in plain %%_libexecdir

* Wed Sep 06 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.0-alt2
- removed spurious dependency on gnome-session.

* Tue Sep 05 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.0-alt1
- new version 2.16.0.
- removed unneeeded dependency on kernel-headers.

* Fri Sep 01 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.92-alt3
- added dependency on gnome-session >= 2.15.92 due to transition from Bonobo to DBus.

* Wed Aug 30 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.92-alt2
- rebuilt with new gstreamer.

* Sun Aug 27 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.92-alt1
- new version 2.15.92 (with rpmrb script)

* Sat Aug 19 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.91-alt1
- new version (2.15.91)
- updated dependencies
- added 'aboutme' switch
- disabled about-me capplet, waiting for evolution-data-server >= 1.7.90
- replaced Bonobo with DBus for gnome-settings-daemon

* Sun Jul 02 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.2-alt2
- Bumped up the release to bump up the robot to build g-c-c with
  gstreamer-0.10.

* Wed May 31 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.2-alt1
- new version 2.14.2 (with rpmrb script)

* Wed Apr 12 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.1-alt1
- new version (2.14.1)
- removed Debian menu support.

* Wed Feb 22 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.92-alt1
- new version
- buildreqs revised

* Thu Feb 02 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.90-alt1
- new version

* Wed Feb 01 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.5.1-alt2
- added switches for alsa and gstreamer.
- enabled aboutme capplet, themes:/// and fonts:/// uri schemes.

* Sun Jan 29 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.5.1-alt1
- new version
- updated dependencies
- cleaned up the files list

* Mon Jan 16 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.5-alt1
- new version

* Tue Jan 10 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.4-alt1
- new version

* Sat Nov 19 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.13.2-alt1
- new version
- %%exclude .la files instead of removing them before packaging.
- rewritten schemas installing, now changes of the schemas list won't go unnoticed by a maintainer.

* Mon Oct 24 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.13.1-alt1
- new version

* Tue Oct 04 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.1-alt1
- new version

* Sat Sep 10 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.0-alt1
- 2.12.0

* Sun Sep 04 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.11.92-alt1
- 2.11.92

* Wed Jul 06 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.2-alt1
- 2.10.2

* Tue Apr 05 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.1-alt1
- 2.10.1

* Tue Mar 08 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Thu Feb 10 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.91-alt1
- 2.9.91

* Mon Feb 07 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.4-alt1
- 2.9.4

* Thu Oct 28 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.1-alt1
- 2.8.1

* Wed Sep 15 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.0-alt1
- 2.8.0

* Mon Sep 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.7.1-alt1
- 2.7.1

* Fri Apr 16 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Thu Apr 01 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0.3-alt1
- 2.6.0.3

* Sat Mar 20 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.4-alt1
- 2.5.4

* Fri Feb 13 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.3-alt1
- 2.5.3

* Thu Feb 05 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.2-alt3
- fix GNOME_SettingsDaemon.server

* Mon Feb 02 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.2-alt2
- rebuild with libxklavier-0.97

* Fri Jan 16 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.2-alt1
- 2.5.2

* Sat Jan 03 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt2
- do not package .la files.
- do not build %%name-devel-static subpackage by default.

* Tue Sep 09 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Wed Sep 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.6-alt1
- 2.3.6

* Tue Aug 19 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.5-alt1
- 2.3.5

* Tue Jul 08 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.4-alt2
- remove %%preun with %%gconf2_uninstall.

* Mon Jul 07 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.4-alt1
- 2.3.4

* Wed Jun 25 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.3-alt1
- 2.3.3

* Wed May 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.2-alt1
- 2.3.2

* Thu May 08 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Fri Mar 14 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Wed Feb 05 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0.1-alt1
- 2.2.0.1

* Tue Jan 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Thu Jan 16 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.7-alt1
- 2.1.7

* Fri Jan 10 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.6-alt1
- 2.1.6

* Thu Dec 19 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.5-alt1
- 2.1.5

* Sun Dec 01 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.3-alt2
- ugly theme_switcher updated from cvs.

* Sun Nov 24 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.3-alt1
- 2.1.3

* Sun Nov 03 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.2-alt1
- 2.1.2

* Tue Oct 22 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.1-alt1
- 2.1.1

* Fri Oct 11 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.1.1-alt2
- Renamed to gnome-control-center.

* Sat Oct 05 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.1.1-alt1.2
- Rebuild with new pango, gtk, gnome-desktop (soname changed).

* Mon Sep 30 2002 Stanislav Ievlev <inger@altlinux.ru> 2.0.1.1-alt1.1
- fixed %post script (Yuri don't use comma in %gconf2_install macros)

* Wed Sep 18 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.1.1-alt1
- 2.0.1.1

* Fri Jul 05 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.0-alt1
- First build control-center for GNOME2.
