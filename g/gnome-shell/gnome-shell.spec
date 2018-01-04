%def_disable snapshot

%define _libexecdir %_prefix/libexec
%define xdg_name org.gnome.Shell
%define ver_major 3.26
%define gst_api_ver 1.0
%def_enable gnome_bluetooth

Name: gnome-shell
Version: %ver_major.2
Release: alt2

Summary: Window management and application launching for GNOME
Group: Graphical desktop/GNOME
License: GPLv2+
Url: https://wiki.gnome.org/Projects/GnomeShell

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif
Patch3: %name-3.8.4-alt-invalid_user_shell.patch

Obsoletes: gnome-shell-extension-per-window-input-source

# use python3
AutoReqProv: nopython
%define __python %nil

%define session_ver 3.25
%define clutter_ver 1.21.5
%define gjs_ver 1.47.0
%define mutter_ver 3.26.2
%define gtk_ver 3.16.0
%define gio_ver 2.53.0
%define gstreamer_ver 1.0
%define eds_ver 3.17.2
%define telepathy_ver 0.17.5
%define telepathy_logger_ver 0.2.4
%define polkit_ver 0.100
%define bluetooth_ver 3.11.3
%define folks_ver 0.5.2
%define gi_ver 1.49.1
%define sn_ver 0.11
%define gcr_ver 3.8
%define atspi_ver 2.5.91
%define menus_ver 3.5.3
%define desktop_ver 3.8
%define json_glib_ver 0.13.2
%define nm_ver 0.9.8
%define caribou_ver 0.4.8

Requires: %name-data = %version-%release
Requires: mutter-gnome >= %mutter_ver libmutter-gir >= %mutter_ver
Requires: gnome-session >= %session_ver
Requires: dconf gnome-icon-theme gnome-icon-theme-symbolic
Requires: at-spi2-atk ca-certificates polkit caribou
# since 3.11.x requires org.gnome.login-screen schema
Requires: gdm-data
# gkbd-keyboard-display required to show keyboard layouts
Requires: libgnomekbd
# network.js requires
Requires: gnome-control-center
# since 3.16
Requires: polari

# find ./ -name "*.js" |/usr/lib/rpm/gir-js.req |sort|uniq|sed -e 's/^/Requires: /'
Requires: typelib(AccountsService)
Requires: typelib(Atk)
Requires: typelib(Atspi)
Requires: typelib(Caribou)
Requires: typelib(Clutter)
Requires: typelib(Cogl)
Requires: typelib(Gcr)
Requires: typelib(GDesktopEnums)
Requires: typelib(Gdk)
Requires: typelib(GdkPixbuf)
Requires: typelib(Gdm)
Requires: typelib(Geoclue)
Requires: typelib(Gio)
Requires: typelib(GLib)
Requires: typelib(GnomeBluetooth)
Requires: typelib(GnomeDesktop)
Requires: typelib(GObject)
Requires: typelib(Gtk)
Requires: typelib(Gvc)
Requires: typelib(GWeather)
Requires: typelib(IBus)
Requires: typelib(Meta)
Requires: typelib(NetworkManager)
Requires: typelib(NMClient)
Requires: typelib(NMGtk)
Requires: typelib(Pango)
Requires: typelib(Polkit)
Requires: typelib(PolkitAgent)
Requires: typelib(Rsvg)
Requires: typelib(Shell)
Requires: typelib(ShellMenu)
Requires: typelib(Soup)
Requires: typelib(St)
Requires: typelib(TelepathyGLib)
Requires: typelib(TelepathyLogger)
Requires: typelib(UPowerGlib)
Requires: typelib(WebKit2)

BuildRequires: meson gcc-c++ gnome-common intltool gtk-doc
BuildRequires: python3-devel rpm-build-python3
BuildRequires: libX11-devel libXfixes-devel
BuildRequires: libclutter-devel >= %clutter_ver libclutter-gir-devel
BuildRequires: libdbus-glib-devel
BuildRequires: libgjs-devel >= %gjs_ver
BuildRequires: libgio-devel >= %gio_ver
BuildRequires: at-spi2-atk-devel >= %atspi_ver
BuildRequires: libxml2-devel
BuildRequires: libgnome-menus-devel >= %menus_ver libgnome-menus-gir-devel
BuildRequires: libGConf-devel
BuildRequires: libgnome-desktop3-devel >= %desktop_ver
BuildRequires: libgnome-keyring-devel
BuildRequires: gcr-libs-devel >= %gcr_ver
BuildRequires: libstartup-notification-devel >= %sn_ver
BuildRequires: gobject-introspection-devel >= %gi_ver
BuildRequires: libjson-glib-devel >= %json_glib_ver
BuildRequires: libcroco-devel
BuildRequires: libcanberra-devel
BuildRequires: libalsa-devel libpulseaudio-devel
%{?_enable_gnome_bluetooth:BuildRequires: libgnome-bluetooth-devel >= %bluetooth_ver libgnome-bluetooth-gir-devel gnome-bluetooth}
BuildRequires: evolution-data-server-devel >= %eds_ver libicu-devel
# for screencast recorder functionality
BuildRequires: gstreamer%gst_api_ver-devel >= %gstreamer_ver gst-plugins%gst_api_ver-devel
BuildRequires: libXfixes-devel
BuildRequires: libgtk+3-devel >= %gtk_ver libgtk+3-gir-devel
# used in unused BigThemeImage
BuildRequires: libmutter-devel >= %mutter_ver libmutter-gir-devel
BuildRequires: mutter >= %mutter_ver
BuildRequires: libpolkit-devel >= %polkit_ver
BuildRequires: libtelepathy-glib-devel >= %telepathy_ver libtelepathy-glib-gir-devel libtelepathy-logger-gir-devel
BuildRequires: libtelepathy-logger-devel >= %telepathy_logger_ver
BuildRequires: libfolks-devel >= %folks_ver libfolks-gir-devel
BuildRequires: libnm-gtk-devel >= %nm_ver
BuildRequires: libcaribou-devel >= %caribou_ver
BuildRequires: libcanberra-gtk3-devel
BuildRequires: libgudev-devel libgudev-gir-devel
BuildRequires: gsettings-desktop-schemas-devel >= 0.1.7
BuildRequires: NetworkManager-glib-devel >= 0.8.995 NetworkManager-glib-gir-devel
BuildRequires: libsoup-gir-devel ca-certificates
BuildRequires: gnome-control-center-devel
BuildRequires: libsystemd-journal-devel
# for browser plugin
BuildRequires: browser-plugins-npapi-devel

%description
GNOME Shell provides core user interface functions for the GNOME 3 desktop,
like switching to windows and launching applications. GNOME Shell takes
advantage of the capabilities of modern graphics hardware and introduces
innovative user interface concepts to provide a visually attractive and
easy to use experience.

%package data
Summary: Arch independent files for GNOME Shell
Group: Graphical desktop/GNOME
BuildArch: noarch

%description data
This package provides noarch data needed for Gnome Shell to work.

%package devel-doc
Group: Development/Other
Summary: Development documentation for GNOME Shell
Conflicts: %name < %version
BuildArch: noarch

%description devel-doc
This package contains documentation needed to develop extensions for
GNOME Shell.

%set_typelibdir %_libdir/%name

%prep
%setup
%patch3 -b .shells
# fix rpath
subst 's|\(install_rpath: pkg\)datadir|\1libdir|' subprojects/gvc/meson.build
# browser plugin dir
subst "s|\(mozplugindir = \).*$|\1'%browser_plugins_path'|" meson.build
%build
%meson \
	-Denable-documentation=true \
	-Denable-schemas-compile=false
%meson_build

%install
%meson_install
%find_lang %name

%check
#%%meson_test

%files
%_bindir/*
%_libexecdir/gnome-shell-calendar-server
%_libexecdir/gnome-shell-perf-helper
%_libexecdir/gnome-shell-hotplug-sniffer
%_libexecdir/%name-portal-helper
%dir %_libdir/%name
%_libdir/%name/libgnome-shell.so
%_libdir/%name/libgnome-shell-menu.so
%_libdir/%name/libgvc.so
%_libdir/%name/libst-1.0.so
%_libdir/%name/*.typelib
# browser plugin
%browser_plugins_path/libgnome-shell-browser-plugin.so

%files data -f %name.lang
%_desktopdir/%xdg_name.desktop
%_desktopdir/%name-extension-prefs.desktop
%_desktopdir/evolution-calendar.desktop
%_desktopdir/%xdg_name.PortalHelper.desktop
%_datadir/%name/
%_datadir/dbus-1/services/%xdg_name.CalendarServer.service
%_datadir/dbus-1/services/%xdg_name.HotplugSniffer.service
%_datadir/dbus-1/interfaces/org.gnome.Shell.PadOsd.xml
%_datadir/dbus-1/interfaces/org.gnome.ShellSearchProvider.xml
%_datadir/dbus-1/interfaces/%xdg_name.Screenshot.xml
%_datadir/dbus-1/interfaces/org.gnome.ShellSearchProvider2.xml
%_datadir/dbus-1/interfaces/%xdg_name.Screencast.xml
%_datadir/GConf/gsettings/gnome-shell-overrides.convert
%_datadir/dbus-1/services/%xdg_name.PortalHelper.service
%_datadir/gnome-control-center/keybindings/50-gnome-shell-system.xml
%_datadir/xdg-desktop-portal/portals/%name.portal
%config %_datadir/glib-2.0/schemas/org.gnome.shell.gschema.xml
%_man1dir/*
%doc README NEWS

%files devel-doc
%_datadir/gtk-doc/html/shell/
%_datadir/gtk-doc/html/st/

%changelog
* Thu Jan 04 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt2
- rebuilt against libical.so.3

* Thu Nov 02 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt1
- 3.26.2

* Wed Oct 04 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Tue Sep 12 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0-5-ge5ed0ab

* Thu Jul 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.3-alt1
- 3.24.3

* Thu May 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.2-alt1
- 3.24.2

* Tue Apr 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt1
- 3.24.1

* Mon Mar 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Fri Feb 17 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.3-alt1
- 3.22.3

* Thu Nov 10 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.2-alt1
- 3.22.2

* Tue Oct 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Tue Sep 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Sat Aug 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.4-alt1
- 3.20.4

* Wed Jun 29 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.3-alt2
- updated to 3.20.3-1-g71c26cc (fixed BGO #766353)

* Wed Jun 29 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.3-alt1
- 3.20.3

* Wed May 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Wed Apr 13 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Wed Apr 13 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt2
- updated to 3.20.0-20-g2edfd45
- applied patch for BGO #764898 (ALT #31968)

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.18.4-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Mar 08 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.4-alt1
- 3.18.4

* Fri Jan 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.3-alt2
- rebuilt against libical.so.2

* Wed Nov 18 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.3-alt1
- 3.18.3

* Thu Nov 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Thu Oct 22 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt2
- 3.18.1_a83f8225

* Thu Oct 15 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Tue Sep 22 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Thu Jul 02 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.3-alt1
- 3.16.3

* Thu May 14 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Wed Apr 15 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.14.4-alt1
- 3.14.4

* Sat Dec 20 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.3-alt1
- 3.14.3

* Fri Nov 28 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt2
- updated to 3.14.2_2ceaa05a (fixed BGO #740141, 740227)
- requires: added libgnomekbd (gkbd-keyboard-display) to show keyboard layouts

* Wed Nov 12 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Thu Oct 30 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1.5-alt1
- 3.14.1.5

* Fri Oct 17 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1.1
- fixed reqs

* Wed Oct 15 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Wed May 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Wed Apr 16 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Thu Apr 03 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1.1
- updated to 2d68bbf94

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Thu Feb 20 2014 Yuri N. Sedunov <aris@altlinux.org> 3.10.4-alt1
- 3.10.4

* Sat Feb 08 2014 Yuri N. Sedunov <aris@altlinux.org> 3.10.3-alt2
- updated to a5370ce3 (fixed BGO ##723308, 722840, 722690, 722434, 722547, 723197)

* Thu Jan 16 2014 Yuri N. Sedunov <aris@altlinux.org> 3.10.3-alt1
- 3.10.3

* Wed Dec 25 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2.1-alt3
- updated to 3b73f792 (fixed BGO ##719965, 719824, 709853, 688331...)

* Tue Nov 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2.1-alt2
- fixed BGO #710456

* Wed Nov 20 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2.1-alt1
- 3.10.2.1 snapshot (43f6739), fixed BGO #711694

* Thu Nov 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

* Tue Oct 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Fri Oct 04 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0.1-alt2
- updated to 56c4873 (fixed BGO ## 702309, 709043, 709286,
  709248(ALT #29410))

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0.1-alt1
- 3.10.0.1

* Wed Jul 31 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.4-alt1
- 3.8.4

* Fri Jul 05 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.3-alt2
- updated to 1020d8a0

* Sat Jun 08 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.3-alt1
- 3.8.3

* Tue May 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Thu May 09 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt3
- updated to eb2e66c

* Mon Apr 22 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt2
- removed useless gnome-shell-3.5.91-avoid-alt-menus.patch

* Tue Apr 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Thu Apr 04 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0.1-alt2
- after 3.8.0.1 snapshot (ae5cdea5)

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0.1-alt1
- 3.8.0.1

* Thu Feb 21 2013 Yuri N. Sedunov <aris@altlinux.org> 3.6.3.1-alt1
- 3.6.3.1

* Sun Feb 17 2013 Yuri N. Sedunov <aris@altlinux.org> 3.6.3-alt1
- 3.6.3

* Thu Dec 20 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt3
- added missed gnome-control-center-devel to buildreqs and packaged
  keybindings files

* Sat Dec 15 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt2
- after 3.6.2 snapshot (2fd4e286)
- %%check section

* Tue Nov 13 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1
- 3.6.2

* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Mon Oct 01 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1.1
- current snapshot (e8ab0b3)

* Wed Sep 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Sat Jul 21 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Tue Apr 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Wed Apr 11 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt0.1
- 3.4.1 snapshot

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Tue Mar 06 2012 Yuri N. Sedunov <aris@altlinux.org> 3.2.2.1-alt4
- updated gnome-shell-show-hide-timer.patch (manovar@)

* Sat Mar 03 2012 Yuri N. Sedunov <aris@altlinux.org> 3.2.2.1-alt3
- manovar@: partially fixed OSK automatic popup

* Fri Mar 02 2012 Yuri N. Sedunov <aris@altlinux.org> 3.2.2.1-alt2
- boyarsh@: introduced new /org/gnome/shell/use-litebox key ("If set to
  'false' user is able to use virtual keyboard in Gnome modal windows")

* Fri Jan 20 2012 Yuri N. Sedunov <aris@altlinux.org> 3.2.2.1-alt1
- 3.2.2.1

* Wed Jan 18 2012 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Mon Dec 12 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt4
- fixed js/gdm/loginDialog.js to skip nonsystem users with invalid
  shells such as "hasher sitellite"

* Sat Dec 03 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt3.1
- properly split noarch data

* Sat Dec 03 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt3
- applied patch proposed in gnome bug #645433
- split up noarch data in separate -data subpackage

* Mon Oct 31 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.2.1-alt2.1
- Rebuild with Python-2.7

* Wed Oct 19 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt2
- rebuilt against libfolks-0.6.4.1

* Tue Oct 18 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Sat Oct 15 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt4
- updated from upstream git
- requires at-spi2-atk, caribou
- load proper gnome3-application.menu

* Wed Oct 12 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt3
- updated from upstream git

* Sun Sep 11 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt2
- rebuild against latest libgjs (ALT #26278)

* Thu May 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Tue Apr 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Sun Apr 17 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0.2-alt3
- rebuild against xulrunner-2.0

* Sat Apr 16 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0.2-alt2
- snapshot

* Thu Apr 07 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0.2-alt1
- 3.0.0.2

* Wed Apr 06 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0.1-alt1
- 3.0.0.1

* Tue Apr 05 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Sun Apr 03 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.93-alt2
- don't prepend private directories while search gnome-bluetooth and
  mutter .typelib's
- requires >= libgnome-bluetooth-2.91.92-alt2 for build and run

* Wed Mar 30 2011 Alexey Shabalin <shaba@altlinux.ru> 2.91.93-alt1
- 2.91.93

* Wed Mar 23 2011 Alexey Shabalin <shaba@altlinux.ru> 2.91.92-alt1
- 2.91.92

* Wed Mar 09 2011 Alexey Shabalin <shaba@altlinux.ru> 2.91.91-alt1
- 2.91.91

* Thu Mar 03 2011 Alexey Shabalin <shaba@altlinux.ru> 2.91.90-alt1.git.20110224
- snapshot 20110224

* Fri Feb 25 2011 Alexey Shabalin <shaba@altlinux.ru> 2.91.90-alt1
- 2.91.90

* Fri Feb 04 2011 Alexey Shabalin <shaba@altlinux.ru> 2.91.6-alt1
- 2.91.6

* Thu Jan 20 2011 Alexey Shabalin <shaba@altlinux.ru> 2.91.5-alt1
- 2.91.5

* Mon Oct 11 2010 Alexey Shabalin <shaba@altlinux.ru> 2.91.0-alt1
- 2.91.0

* Wed Mar 24 2010 Alexey Shabalin <shaba@altlinux.ru> 2.29.1-alt1
- 2.29.1

* Sun Mar 14 2010 Alexey Shabalin <shaba@altlinux.ru> 2.29.0-alt0.3
- requires only mutter-gnome (all other auto find)

* Sat Mar 13 2010 Alexey Shabalin <shaba@altlinux.ru> 2.29.0-alt0.2
- git snapshot 20d3b1f8b18507cd8644ed98ff06659d04eb2c84
- cleanup requires, use automatic dependency

* Fri Mar 05 2010 Alexey Shabalin <shaba@altlinux.ru> 2.29.0-alt0.1
- 2.29.0

* Wed Feb 03 2010 Alexey Shabalin <shaba@altlinux.ru> 2.28.1-alt0.1
- git snapshot fa6016576486e47a89c0de95873d6de9cb5acc3c
- disable CFLAGS -Werror

* Tue Dec 15 2009 Alexey Shabalin <shaba@altlinux.ru> 2.28.0-alt1.b03fa1
- git snapshot

* Sun Oct 11 2009 Alexey Shabalin <shaba@altlinux.ru> 2.28.0-alt1
- 2.28.0

* Wed Sep 16 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.3-alt1
- 2.27.3

* Thu Aug 13 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.0-alt1
- adapted for sisyphus
