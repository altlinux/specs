%define ver_major 3.4
%define _libexecdir %_prefix/libexec
%def_enable systemd

Name: gnome-session
Version: %ver_major.2
Release: alt1

Summary: The gnome session programs for the GNOME GUI desktop environment
License: GPLv2+
Group: Graphical desktop/GNOME
URL: ftp://ftp.gnome.org
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz
Source1: gnome-nautilus.png
Source2: gnome.svg
Patch: %name-2.91.6-alt-autosave_session.patch

# From configure.in
%define glib_ver 2.28.0
%define gtk_ver 3.0.0
%define dbus_glib_ver 0.76
%define polkit_ver 0.91
%define upower_ver 0.9
%define systemd_ver 40

PreReq: xinitrc libcanberra-gnome libcanberra-gtk3
Requires: altlinux-freedesktop-menu-gnome3
Requires: gstreamer dbus-tools-gui
Requires: gnome-filesystem metacity-gnome
Requires: gnome-settings-daemon >= 3.0.0
Requires: upower polkit-gnome gcr

Requires: icon-theme-hicolor gnome-icon-theme-symbolic gnome-themes-standard

BuildPreReq: rpm-build-gnome >= 0.5
BuildPreReq: gnome-common

# From configure.in
BuildPreReq: intltool >= 0.35.0 libGConf-devel
BuildPreReq: libgio-devel glib2-devel >= %glib_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libdbus-glib-devel >= %dbus_glib_ver
BuildPreReq: libupower-devel >= %upower_ver
BuildRequires: libgnome-desktop3-devel librsvg-devel libjson-glib-devel
BuildRequires: libX11-devel libXau-devel libXrandr-devel libXrender-devel libXt-devel
BuildRequires: libSM-devel libXext-devel libXtst-devel libXi-devel libXcomposite-devel libGL-devel
BuildRequires: GConf browser-plugins-npapi-devel perl-XML-Parser xorg-xtrans-devel
%{?_enable_systemd:BuildRequires: systemd-devel >= %systemd_ver libpolkit-devel}

%description
GNOME (GNU Network Object Model Environment) is a user-friendly
set of applications and desktop tools to be used in conjunction with a
window manager for the X Window System.

This package provides tools for the the gnome desktop.

%prep
%setup -q
%patch

%build
%configure PATH=$PATH:/sbin \
    %{subst_enable systemd} \
    --disable-schemas-compile

%make_build

%install
%make_install install DESTDIR=%buildroot

cat <<__START_GNOME__ >startgnome
#!/bin/sh

# turn on fonts antialiasing
export GDK_USE_XFT=1

# set default browser to whatever GNOME user likes
export BROWSER=gnome-open

# tell restored browsers where plugins are
export MOZ_PLUGIN_PATH="\${MOZ_PLUGIN_PATH:+"\$MOZ_PLUGIN_PATH:"}\${HOME:+"\$HOME/.mozilla/plugins:"}%_libdir/mozilla/plugins:%_libdir/netscape/plugins:%browser_plugins_path"

export HELP_BROWSER=yelp

# use prefixed .menu files
export XDG_MENU_PREFIX="gnome3-"

#### use /usr/share/gnome as a part of XDG_DATA_DIRS
#### export XDG_DATA_DIRS="\${XDG_DATA_DIRS:+"\$XDG_DATA_DIRS:"}%_datadir/gnome"

# Since shared-mime-info-0.90-alt3 XDG_DATA_DIRS not exported. We need to define
# the set of base directories explicitly.

export XDG_DATA_DIRS="%_datadir/gnome:%_datadir:/usr/local/share"

# to avoid gnome-shell crash
/bin/rm -f "\$HOME"/.config/gnome-session/saved-session/gnome-shell.desktop >/dev/null 2>&1

exec %_bindir/gnome-session "\$@"
__START_GNOME__

install -pD -m755 startgnome %buildroot%_bindir/startgnome

mkdir -p %buildroot%_sysconfdir/X11/wmsession.d/
cat << __EOF__ > %buildroot%_sysconfdir/X11/wmsession.d/02Gnome
NAME=Gnome
ICON=%_iconsdir/gnome.svg
DESC=Gnome Environment
EXEC=%_bindir/startgnome
SCRIPT:
exec %_bindir/startgnome
__EOF__

%if 0
cat << __EOF__ > %buildroot%_sysconfdir/X11/wmsession.d/02Gnome-fallback
NAME=Gnome fallback
ICON=%_iconsdir/gnome.svg
DESC=Gnome Environment (fallback mode)
EXEC=%_bindir/startgnome
SCRIPT:
exec %_bindir/startgnome --session gnome-fallback
__EOF__
%endif

install -pD -m644 %SOURCE1 %buildroot%_datadir/pixmaps/gnome-nautilus.png
install -pD -m644 %SOURCE2 %buildroot%_iconsdir/gnome.svg

%find_lang --with-gnome --output=%name.lang %name-3.0

%files -f %name.lang
%_bindir/*
%_libexecdir/gnome-session-check-accelerated
%_libexecdir/gnome-session-check-accelerated-helper
%_desktopdir/*.desktop
%dir %_datadir/%name
%_datadir/%name/*.ui
%_datadir/%name/hardware-compatibility
%dir %_datadir/%name/sessions
%_datadir/%name/sessions/gnome.session
%_datadir/%name/sessions/gnome-fallback.session
%_pixmapsdir/*
%_iconsdir/gnome.svg
%_iconsdir/hicolor/*/apps/session-properties.*
%config %_sysconfdir/X11/wmsession.d/*Gnome*
%config %_datadir/glib-2.0/schemas/org.gnome.SessionManager.gschema.xml
%_datadir/GConf/gsettings/%name.convert
%_mandir/man?/*
%doc AUTHORS NEWS README

%exclude %_datadir/xsessions/gnome.desktop

%changelog
* Mon May 14 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Mon Apr 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Sun Oct 16 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Mon Oct 03 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt2
- fixed string format in show_fallback_dialog()

* Mon Sep 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Tue Sep 20 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.92-alt1
- 3.1.92

* Tue Sep 13 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.91-alt2
- added /etc/X11/wmsession.d/02Gnome-fallback for fallback mode

* Mon Sep 05 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.91-alt1
- 3.1.91

* Thu Sep 01 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.90-alt1
- 3.1.90

* Thu Sep 01 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt2
- fixed a set of base directories exported by XDG_DATA_DIRS variable
  in startgnome script

* Tue May 24 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Sat May 21 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt6
- use gnome3- as XDG_MENU_PREFIX
- updated reqs/buildreqs

* Tue May 03 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt5
- added %%_datadir/gnome to $XDG_DATA_DIRS for use with gnome-specific
  defaults.list as in 2.32.1-alt2

* Tue May 03 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt4
- /usr/bin/startgnome removes
  ~/.config/gnome-session/saved-session/gnome-shell.desktop
  to avoid gnome-shell crash when
  /apps/gnome-session/options/auto_save_session is set to true
- Gconf-sanity-check reqs
- gnome-icon-theme-symbolic, gnome-icon-theme-standard temporarily added
  to reqs
- obsolete reqs and conflicts removed

* Tue May 03 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt2
- added %%_datadir/gnome to $XDG_DATA_DIRS for use with gnome-specific
  defaults.list

* Wed Nov 17 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1
- 2.32.1

* Wed Nov 03 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt3
- added libcanbera-gnome to rqs

* Thu Oct 21 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt2
- debugging code removed

* Tue Oct 05 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Wed Aug 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.31.6-alt1
- 2.31.6

* Tue Jun 22 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt1
- 2.30.2

* Sun Apr 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt2
- updared buildreqs

* Tue Mar 30 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Tue Mar 09 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.92-alt1
- 2.29.92

* Wed Jan 27 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.6-alt1
- 2.29.6

* Sat Sep 26 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt2
- splash screen enabled by default
- rebuild with new %%browser_plugins_path

* Tue Sep 22 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Wed Sep 09 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.92-alt1
- 2.27.92

* Thu Aug 27 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.91-alt1
- 2.27.91
- PolicyKit-gnome -> polkit-gnome

* Tue Aug 18 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.5-alt2
- fixed http://bugzilla.gnome.org/show_bug.cgi?id=585614
- requires PolicyKit-gnome

* Wed Aug 12 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.5-alt1
- 2.27.5
- updated {build,}reqs
- set metacity as default wm

* Thu Jul 23 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt2
- set XDG_MENU_PREFIX variable to "gnome-" in startgnome2 (closes #20852)

* Wed Jul 01 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt1
- 2.26.2

* Fri May 22 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt2
- not packaged /usr/share/xsessions/gnome.desktop

* Tue Apr 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Wed Apr 08 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0.90-alt1
- new version

* Tue Mar 31 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt2
- told where at-spi-registryd is

* Tue Mar 17 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Wed Mar 04 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.92-alt1
- 2.25.92

* Tue Feb 17 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.91-alt1
- 2.25.91

* Fri Jan 23 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.5-alt1
- 2.25.5
- updated buildreqs

* Tue Jan 13 2009 Yuri N. Sedunov <aris@altlinux.org> 2.24.3-alt1
- 2.24.3

* Thu Dec 11 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt2
- requires GConf-sanity-check

* Tue Nov 25 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt1
- 2.24.2
- removed obsolete %%{update,clean}_wms from %%post* scripts
- drop upstreamed patches
- don't package useless gnome-wm
- conflicts with old gdm (altbug #16911)

* Fri Oct 31 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt2
- fix gnome bug #536915 (patch0)
- fix altbug #12333
- updated buildreqs

* Wed Oct 22 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1

* Sun Sep 28 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt1
- 2.24.0
- drop obsoleted 2.13.4-no-crashes.patch
- Fedora's patches (5,6)

* Mon Jun 30 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.3-alt1
- new version (2.22.3)

* Mon Jun 02 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.2-alt1
- new version (2.22.2)

* Sat May 03 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.1.1-alt1
- new version (2.22.1.1)

* Tue Apr 08 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.1-alt1
- new version (2.22.1)

* Sat Mar 29 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1
- new version (2.22.0)

* Mon Dec 10 2007 Alexey Rusakov <ktirf@altlinux.org> 2.20.2-alt2
- Moved autostart directory from gnome-session to gnome-filesystem.
- Updated buildreqs.

* Tue Dec 04 2007 Alexey Shabalin <shaba@altlinux.ru> 2.20.2-alt1
- new version (2.20.2)

* Fri Nov 23 2007 Alexey Shabalin <shaba@altlinux.ru> 2.20.1-alt1
- new version (2.20.1)
- add Packager

* Mon Aug 13 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.3-alt4
- fixed Bug #12333 (thanks to raorn@ for gnome-wm script).
- use more macros

* Fri Jul 06 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.3-alt3
- fixed building on x86_64

* Fri Jul 06 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.3-alt2
- removed dbus-launch from startgnome2 script - the session bus is already
  launched at the start of X session (see dbus-tools-gui package).

* Wed Jul 04 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.3-alt1
- new version (2.18.3)
- BROWSER is now always set to gnome-open in /usr/bin/startgnome2, so that the
  preferred browser is always used no matter how invoked
- WINDOW_MANAGER is no more initialized in /usr/bin/startgnome2,
  /usr/bin/gnome-wm can choose a proper window manager without hints
- temporarily removed splash-screen customization, since there is no GNOME
  artworks in the version 4.0 of design-graphics-desktop package
- updated dependencies and files list

* Wed Oct 04 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.0-alt3
- added dependency on dbus-tools-gui (for dbus-launch).

* Wed Sep 27 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.0-alt2
- fixed various problems with applying settings (incl. themes) in GNOME,
  due to DBus session unlaunched or launched improperly.

* Sun Sep 24 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.0-alt1
- new version (2.16.0)
- added /usr/share/gnome/autostart directory.

* Fri Sep 01 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.92-alt3
- add dependency on gnome-control-center >= 2.15.90 due to transtion from Bonobo to DBus.

* Wed Aug 30 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.92-alt2
- rebuilt with new gstreamer.

* Sun Aug 27 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.92-alt1
- new version (2.15.92)

* Fri Aug 18 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.91-alt1
- new version (2.15.91)
- updated dependencies
- spec cleanup

* Thu Jun 01 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.2-alt1
- new version 2.14.2 (with rpmrb script)

* Tue Apr 11 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.1-alt1
- new version 2.14.1 (with rpmrb script)

* Sun Feb 11 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.90-alt1
- new version
- Fixed Bug #8442.
- don't flip the cursor in startgnome2 script.

* Tue Feb 07 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.12.0-alt1.1
- Rebuild with libgnomeui which has been fixed up for modular Xorg
- Correct xsetroot path since it was moved to /usr/bin
- Removed Debian-style menu
- Buildreq

* Sat Sep 10 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.0-alt1
- 2.12.0
- Removed excess buildreqs.

* Tue Aug 30 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.11.91-alt1
- 2.11.91

* Mon Mar 07 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Sun Feb 06 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.4-alt1
- 2.9.4

* Thu Oct 28 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.1-alt1
- 2.8.1

* Tue Sep 14 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.0-alt1
- 2.8.0

* Mon Sep 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.7.91-alt1
- 2.7.91

* Thu Jun 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.2-alt1
- 2.6.2

* Wed Apr 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Tue Mar 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Tue Feb 24 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.90-alt1
- 2.5.90

* Wed Feb 04 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.4-alt1
- 2.5.4

* Fri Jan 16 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.3-alt1
- 2.5.3

* Mon Oct 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1-alt1
- 2.4.1

* Mon Sep 29 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt3
- Another fix gnome-splash location.

* Fri Sep 26 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt2
- fix gnome-splash location.

* Tue Sep 09 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Wed Sep 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.90-alt1
- 2.3.90

* Tue Aug 19 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.6.2-alt1
- 2.3.6.2

* Wed Jul 16 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.4-alt1
- 2.3.4

* Sat Jul 05 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.3.1-alt1
- 2.3.3.1

* Sun Jun 08 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.3-alt1
- 2.3.3
- Epiphany is a default BROWSER.
- Requires gnome-wm.

* Wed May 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.2-alt1
- 2.3.2

* Mon May 05 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Mon Apr 28 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.0-alt2
- Changed reboot-command to %_bindir/reboot and halt-command
  to %_bindir/poweroff (slava). Requires SysVinit-usermode to use.
  Close ## 2106, 1506

* Sun Mar 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.0-alt1
- 2.3.0

* Thu Mar 13 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Wed Feb 19 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0.2-alt2
- export BROWSER=galeon

* Tue Feb 04 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0.2-alt1
- 2.2.0.2

* Wed Jan 22 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0.1-alt1
- 2.2.0.1

* Tue Jan 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Tue Jan 07 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.90-alt1
- 2.1.90

* Tue Dec 17 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.5-alt1
- 2.1.5

* Tue Dec 10 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.4-alt1
- 2.1.4

* Thu Nov 28 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.3-alt1
- 2.1.3

* Mon Nov 11 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.2-alt2
- Built with new libwrap.

* Mon Nov 04 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.2-alt1
- 2.1.2

* Fri Oct 04 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.0-alt1
- 2.1.0

* Fri Oct 04 2002 Stanislav Ievlev <inger@altlinux.ru> 2.0.7-alt1.3
- remove pixmaps into design package (this package must provides
  "gnome-session-splash")

* Wed Oct 02 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.7-alt1.2
- Fonts antialiasing turned on by default.
- Metacity is a default window manager.

* Mon Sep 30 2002 Stanislav Ievlev <inger@altlinux.ru> 2.0.7-alt1.1
- update buildreq to remove rsh

* Wed Sep 18 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.7-alt1
- 2.0.7
- Metacity added to requires list.

* Sat Jun 22 2002 Igor Androsov <blake@altlinux.ru> 2.0.1-alt1
- New release
- gnome-session-2.0.1-splash.patch
- Fix from Yuri Sedunov <aris@altlinux.ru>
	+ Added Gnome2.xpm
	+ Replace command by macros
	+ cleanup spec
	+ clean_wms run in postun
	
* Thu May 16 2002 Igor Androsov <blace@mail.ru> 1.5.19-blk1
- New version from CVS

* Mon May 13 2002 Igor Androsov <blace@mail.ru> 1.5.18-blk1
- Changes for AltLinux
- cleanup spec
- Added wmsession and script

* Tue Mar 05 2002 Chris Chabot <chabotc@reviewboard.com>
- Final cleanups
- make .spec.in

* Sun Feb 15 2002 Chris Chabot <chabotc@reviewboard.com>
- initial spec file for gnome-session
