%def_disable snapshot

%define _libexecdir %_prefix/libexec
%define xdg_name org.gnome.Shell
%define ver_major 46
%define beta %nil
%define api_ver 14
%define gst_api_ver 1.0
%define gvc_ver 5f9768a

%def_enable extensions_tool
%def_enable extensions_app
%def_disable gtk_doc
%def_disable check
# removed in 3.31.x
%def_disable browser_plugin

Name: gnome-shell
Version: %ver_major.4
Release: alt1%beta

Summary: Window management and application launching for GNOME
Group: Graphical desktop/GNOME
License: GPL-2.0
Url: https://wiki.gnome.org/Projects/GnomeShell

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version%beta.tar.xz
%else
Source: %name-%version%beta.tar
%endif
%{?_enable_snapshot:Source1: libgnome-volume-control-%gvc_ver.tar}

Patch3: %name-3.8.4-alt-invalid_user_shell.patch

Obsoletes: gnome-shell-extension-per-window-input-source

%define session_ver 3.26
%define gjs_ver 1.73.1
%define mutter_ver %ver_major
%define gtk_ver 3.16.0
%define adwaita_ver 1.0
%define gio_ver 2.56.0
%define gstreamer_ver 1.0
%define eds_ver 3.34.0
%define telepathy_ver 0.17.5
%define telepathy_logger_ver 0.2.4
%define polkit_ver 0.100
%define bt_api_ver 3.0
%define bluetooth_ver 3.11.3
%define folks_ver 0.5.2
%define gi_ver 1.49.1
%define sn_ver 0.11
%define gcr_api_ver 4
%define gcr_ver 3.90.0
%define atspi_ver 2.5.91
%define menus_ver 3.5.3
%define desktop_ver 3.35.90
%define json_glib_ver 0.13.2
%define nm_ver 1.10.4
%define ibus_ver 1.5.19
%define gsds_ver 42
%define libsecret_ver 0.18
%define malcontent_ver 0.11
%define gweather_api_ver 4.0
%define webkit_api_ver 6.0

Requires: %name-data = %EVR
# to avoid circular dependency
%filter_from_requires /\/usr\/bin\/%name/d
Requires: mutter-gnome >= %mutter_ver libmutter-gir >= %mutter_ver
Requires: gnome-session >= %session_ver
Requires: dconf at-spi2-core gnome-icon-theme gnome-icon-theme-symbolic
Requires: at-spi2-atk ca-certificates polkit
# since 3.11.x requires org.gnome.login-screen schema
Requires: gdm-data
Requires: tecla
# network.js requires
Requires: gnome-control-center
# since 3.16
# 
#Requires: polari
# for OSK
Requires: ibus ibus-gtk4
# for zipped extensions
Requires: unzip
# synce 3.38
Requires: malcontent >= %malcontent_ver
Requires: pipewire
Requires: xdg-desktop-portal-gnome

# find ./ -name "*.js" |/usr/lib/rpm/gir-js.req |sort|uniq|sed -e 's/^/Requires: /'
# js/misc/dependencies.js
Requires: typelib(AccountsService)
Requires: typelib(Atk)
Requires: typelib(Atspi)
Requires: typelib(Clutter)
Requires: typelib(Gcr) = %gcr_api_ver
Requires: typelib(GDesktopEnums) = 3.0
Requires: typelib(Gdk) = 4.0
Requires: typelib(GdkPixbuf)
Requires: typelib(Gdm)
Requires: typelib(Geoclue)
Requires: typelib(Gio)
Requires: typelib(GLib)
Requires: typelib(GnomeBluetooth) = %bt_api_ver
Requires: typelib(GnomeDesktop)
Requires: typelib(GObject)
Requires: typelib(Graphene)
Requires: typelib(Gst)
Requires: typelib(Gtk) = 4.0
Requires: typelib(Gvc)
Requires: typelib(GWeather) = %gweather_api_ver
Requires: typelib(IBus)
Requires: typelib(Malcontent)
Requires: typelib(Meta)
Requires: typelib(NM)
Requires: typelib(NMA4) = 1.0
Requires: typelib(Pango)
Requires: typelib(Polkit)
Requires: typelib(PolkitAgent)
Requires: typelib(Rsvg)
Requires: typelib(Shell)
Requires: typelib(Shew)
Requires: typelib(Soup) = 3.0
Requires: typelib(St)
Requires: typelib(TelepathyGLib)
Requires: typelib(TelepathyLogger)
Requires: typelib(UPowerGlib)
Requires: typelib(WebKit) = %webkit_api_ver

BuildRequires(pre): rpm-macros-meson rpm-build-gir
BuildRequires(pre): rpm-build-python3 rpm-build-xdg rpm-build-systemd
BuildRequires: meson gcc-c++ xsltproc asciidoc-a2x sassc
BuildRequires: /usr/bin/appstream-util /usr/bin/appstreamcli desktop-file-utils
BuildRequires: bash-completion
BuildRequires: python3-devel
BuildRequires: libX11-devel libXfixes-devel
BuildRequires: libmutter-devel >= %mutter_ver libmutter-gir-devel
BuildRequires: libgjs-devel >= %gjs_ver
BuildRequires: libgio-devel >= %gio_ver
BuildRequires: libgtk+3-devel >= %gtk_ver libgtk+3-gir-devel
# for Shew
BuildRequires: libgtk4-devel libgtk4-gir-devel pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: at-spi2-atk-devel >= %atspi_ver
BuildRequires: gobject-introspection-devel >= %gi_ver
BuildRequires: libxml2-devel
BuildRequires: libgnome-menus-devel >= %menus_ver libgnome-menus-gir-devel
BuildRequires: libGConf-devel
BuildRequires: libgnome-desktop3-devel >= %desktop_ver
BuildRequires: pkgconfig(gcr-%gcr_api_ver) >= %gcr_ver
BuildRequires: libstartup-notification-devel >= %sn_ver
BuildRequires: libjson-glib-devel >= %json_glib_ver
BuildRequires: libcanberra-devel libcanberra-gtk3-devel
BuildRequires: libalsa-devel libpulseaudio-devel
BuildRequires: pkgconfig(gnome-bluetooth-%bt_api_ver) >= %bluetooth_ver libgnome-bluetooth%bt_api_ver-gir-devel
BuildRequires: evolution-data-server-devel >= %eds_ver libicu-devel
# for screencast recorder functionality
BuildRequires: gstreamer%gst_api_ver-devel >= %gstreamer_ver gst-plugins%gst_api_ver-devel pkgconfig(libpipewire-0.3)
BuildRequires: libXfixes-devel
BuildRequires: mutter >= %mutter_ver
BuildRequires: libpolkit-devel >= %polkit_ver
BuildRequires: libtelepathy-glib-devel >= %telepathy_ver libtelepathy-glib-gir-devel libtelepathy-logger-gir-devel
BuildRequires: libtelepathy-logger-devel >= %telepathy_logger_ver
BuildRequires: libfolks-devel >= %folks_ver libfolks-gir-devel
BuildRequires: libnm-devel >= %nm_ver libnm-gir-devel
BuildRequires: libgudev-devel libgudev-gir-devel
BuildRequires: gsettings-desktop-schemas-devel >= %gsds_ver
BuildRequires: libsoup3.0-gir-devel ca-certificates
BuildRequires: gnome-control-center-devel
BuildRequires: pkgconfig(systemd)
BuildRequires: libibus-devel >= %ibus_ver
BuildRequires: gir(Gcr) = %gcr_api_ver libsecret-devel >= %libsecret_ver libpolkit-gir-devel
BuildRequires: libgnome-autoar-devel
BuildRequires: pkgconfig(tecla)
%{?_enable_gtk_doc:BuildRequires: gtk-doc}
%{?_enable_browser_plugin:BuildRequires: browser-plugins-npapi-devel}

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

%package -n gnome-extensions-app
Summary: GNOME Shell extensions manager
Group: Graphical desktop/GNOME
Requires: %name = %EVR

%description -n gnome-extensions-app
GNOME Extensions handles updating extensions, configuring extension
preferences and removing or disabling unwanted extensions.

%set_typelibdir %_libdir/%name

%prep
%setup -n %name-%version%beta %{?_enable_snapshot:-a1
mkdir subprojects/gvc
cp -a libgnome-volume-control-%gvc_ver/* subprojects/gvc/}

%patch3 -b .shells
# set full path to gsettings
sed -i 's|=\(gsettings\)|=%_bindir/\1|' data/%xdg_name-disable-extensions.service

# browser plugin dir
%{?_enable_browser_plugin:subst "s|\(mozplugindir = \).*$|\1'%browser_plugins_path'|" meson.build}
%build
%meson \
    %{?_enable_gtk_doc:-Dgtk_doc=true} \
    %{subst_enable_meson_bool extensions_tool extensions_tool} \
    %{subst_enable_meson_bool extensions_app extensions_app} \
    %{?_enable_snapshot:%meson_build %name-pot %name-update-po}
#%meson_build %name-pot %name-update-po
%nil
%meson_build -v

%install
%meson_install
%find_lang %name

%check
%meson_test

%files
%_bindir/%name
%_bindir/%name-extension-prefs
%_bindir/%name-test-tool
%{?_enable_extensions_tool:%_bindir/gnome-extensions
%_bindir/gnome-shell-extension-tool}
%_libexecdir/%name-calendar-server
%_libexecdir/%name-perf-helper
%_libexecdir/%name-hotplug-sniffer
%_libexecdir/%name-portal-helper
%dir %_libdir/%name
%_libdir/%name/lib%name-menu.so
%_libdir/%name/libgvc.so
%_libdir/%name/libshell-%api_ver.so
%_libdir/%name/libst-%api_ver.so
%_libdir/%name/libshew-0.so
%_libdir/%name/*.typelib
%dir %_libdir/%name/girepository-1.0
%_libdir/%name/girepository-1.0/Shew-0.typelib
%{?_enable_browser_plugin:%browser_plugins_path/libgnome-shell-browser-plugin.so}

%files data -f %name.lang
%{?_enable_extensions_tool:%_datadir/bash-completion/completions/gnome-extensions}
%_desktopdir/%xdg_name.desktop
%_desktopdir/%xdg_name.Extensions.desktop
%_desktopdir/%xdg_name.PortalHelper.desktop
%_datadir/%name/
%_datadir/dbus-1/services/%xdg_name.CalendarServer.service
%_datadir/dbus-1/services/%xdg_name.HotplugSniffer.service
%_datadir/dbus-1/interfaces/%xdg_name.Introspect.xml
%_datadir/dbus-1/interfaces/%xdg_name.PadOsd.xml
%_datadir/dbus-1/interfaces/%{xdg_name}SearchProvider.xml
%_datadir/dbus-1/interfaces/%xdg_name.Screenshot.xml
%_datadir/dbus-1/interfaces/%{xdg_name}SearchProvider2.xml
%_datadir/dbus-1/interfaces/%xdg_name.Screencast.xml
%_datadir/dbus-1/interfaces/%xdg_name.Extensions.xml
%_datadir/dbus-1/services/%xdg_name.Extensions.service
%_datadir/dbus-1/services/%xdg_name.Notifications.service
%_datadir/dbus-1/services/%xdg_name.PortalHelper.service
%_datadir/dbus-1/services/%xdg_name.Screencast.service
%_datadir/dbus-1/services/org.gnome.ScreenSaver.service
%_datadir/gnome-control-center/keybindings/50-%name-launchers.xml
%_datadir/gnome-control-center/keybindings/50-%name-system.xml
%_datadir/gnome-control-center/keybindings/50-%name-screenshots.xml
%config %_datadir/glib-2.0/schemas/org.gnome.shell.gschema.xml
%config %_datadir/glib-2.0/schemas/00_org.gnome.shell.gschema.override
%_userunitdir/%xdg_name-disable-extensions.service
%_userunitdir/%xdg_name.target
%_userunitdir/%{xdg_name}@wayland.service
%_userunitdir/%{xdg_name}@x11.service

%_man1dir/*
%_iconsdir/hicolor/*/*/%xdg_name.Extensions*.svg
%doc README* NEWS

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/shell/
%_datadir/gtk-doc/html/st/
%endif

%{?_enable_extensions_app:
%files -n gnome-extensions-app
%_bindir/gnome-extensions-app
%_desktopdir/org.gnome.Extensions.desktop
%config %_datadir/glib-2.0/schemas/org.gnome.Extensions.gschema.xml
%_datadir/metainfo/org.gnome.Extensions.metainfo.xml
%_datadir/dbus-1/services/org.gnome.Extensions.service
%_iconsdir/hicolor/*/*/org.gnome.Extensions*.svg
}

%changelog
* Mon Aug 05 2024 Yuri N. Sedunov <aris@altlinux.org> 46.4-alt1
- 46.4

* Wed Jul 03 2024 Yuri N. Sedunov <aris@altlinux.org> 46.3.1-alt1.1
- split gnome-extensions-app into a separate subpackage (ALT #49630)

* Sun Jun 30 2024 Yuri N. Sedunov <aris@altlinux.org> 46.3.1-alt1
- 46.3.1

* Sun May 26 2024 Yuri N. Sedunov <aris@altlinux.org> 46.2-alt1
- 46.2

* Wed May 15 2024 Yuri N. Sedunov <aris@altlinux.org> 46.1-alt2
- updated to 46.1-16-gb03a68314, probably fixed (ALT #50367)

* Sun Apr 21 2024 Yuri N. Sedunov <aris@altlinux.org> 46.1-alt1
- 46.1

* Sun Mar 17 2024 Yuri N. Sedunov <aris@altlinux.org> 46.0-alt1
- 46.0

* Mon Mar 04 2024 Yuri N. Sedunov <aris@altlinux.org> 46-alt0.9.rc
- 46.rc

* Mon Feb 12 2024 Yuri N. Sedunov <aris@altlinux.org> 45.4-alt1
- 45.4

* Sun Jan 07 2024 Yuri N. Sedunov <aris@altlinux.org> 45.3-alt1
- 45.3

* Sat Dec 02 2023 Yuri N. Sedunov <aris@altlinux.org> 45.2-alt1
- 45.2

* Wed Nov 01 2023 Yuri N. Sedunov <aris@altlinux.org> 45.1-alt1
- 45.1

* Sun Sep 17 2023 Yuri N. Sedunov <aris@altlinux.org> 45.0-alt1
- 45.0

* Sun Sep 17 2023 Yuri N. Sedunov <aris@altlinux.org> 44.5-alt1
- 44.5

* Wed Aug 30 2023 Yuri N. Sedunov <aris@altlinux.org> 44.4-alt1.1
- removed useless libcroco-devel from BR (gnome-shell includes
  the libcroco sources directly under src/st/croco)

* Thu Aug 24 2023 Yuri N. Sedunov <aris@altlinux.org> 44.4-alt1
- 44.4

* Thu Jul 13 2023 Yuri N. Sedunov <aris@altlinux.org> 44.3-alt1.1
- filtered from requires /usr/bin/gnome-shell to avoid circular
  dependencies (ALT#46895)

* Fri Jul 07 2023 Yuri N. Sedunov <aris@altlinux.org> 44.3-alt1
- 44.3

* Sat Jun 03 2023 Yuri N. Sedunov <aris@altlinux.org> 44.2-alt1
- 44.2
- bonus: polari-free build

* Tue Apr 25 2023 Yuri N. Sedunov <aris@altlinux.org> 44.1-alt1
- 44.1

* Mon Mar 20 2023 Yuri N. Sedunov <aris@altlinux.org> 44.0-alt1
- 44.0

* Mon Mar 20 2023 Yuri N. Sedunov <aris@altlinux.org> 43.4-alt1
- 43.4

* Tue Feb 14 2023 Yuri N. Sedunov <aris@altlinux.org> 43.3-alt1
- 43.3

* Thu Dec 08 2022 Yuri N. Sedunov <aris@altlinux.org> 43.2-alt1
- 43.2

* Thu Nov 10 2022 Yuri N. Sedunov <aris@altlinux.org> 43.1-alt1
- 43.1

* Tue Sep 20 2022 Yuri N. Sedunov <aris@altlinux.org> 43.0-alt1
- 43.0

* Thu Aug 11 2022 Yuri N. Sedunov <aris@altlinux.org> 42.4-alt1
- 42.4

* Mon Jul 25 2022 Yuri N. Sedunov <aris@altlinux.org> 42.3.1-alt1.1
- explicitly required typelib(Gcr) = 3 (ALT #43332)

* Mon Jul 04 2022 Yuri N. Sedunov <aris@altlinux.org> 42.3.1-alt1
- 42.3.1

* Sun May 29 2022 Yuri N. Sedunov <aris@altlinux.org> 42.2-alt1
- 42.2

* Fri May 06 2022 Yuri N. Sedunov <aris@altlinux.org> 42.1-alt1
- 42.1

* Fri Mar 25 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0-alt2
- updated to 42.0-40-g90fdd1169

* Mon Mar 21 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0-alt1
- 42.0

* Mon Mar 21 2022 Yuri N. Sedunov <aris@altlinux.org> 41.5-alt1
- 41.5

* Sun Feb 27 2022 Yuri N. Sedunov <aris@altlinux.org> 41.4-alt1
- 41.4

* Tue Jan 11 2022 Yuri N. Sedunov <aris@altlinux.org> 41.3-alt1
- 41.3

* Mon Dec 13 2021 Yuri N. Sedunov <aris@altlinux.org> 41.2-alt1
- 41.2

* Thu Nov 04 2021 Yuri N. Sedunov <aris@altlinux.org> 41.1-alt1
- 41.1

* Thu Nov 04 2021 Yuri N. Sedunov <aris@altlinux.org> 40.6-alt1
- 40.6

* Tue Sep 21 2021 Yuri N. Sedunov <aris@altlinux.org> 40.5-alt1
- 40.5

* Wed Aug 18 2021 Yuri N. Sedunov <aris@altlinux.org> 40.4-alt1
- 40.4

* Mon Jul 12 2021 Yuri N. Sedunov <aris@altlinux.org> 40.3-alt1
- 40.3

* Fri Jun 25 2021 Yuri N. Sedunov <aris@altlinux.org> 40.2-alt2
- 40.2-2-g8e5e7821a (updated russian translation)

* Thu Jun 10 2021 Yuri N. Sedunov <aris@altlinux.org> 40.2-alt1
- 40.2

* Fri May 14 2021 Yuri N. Sedunov <aris@altlinux.org> 40.1-alt1
- 40.1

* Sat Mar 20 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt1
- 40.0

* Tue Mar 16 2021 Yuri N. Sedunov <aris@altlinux.org> 40-alt0.8.rc
- 40.rc

* Tue Mar 16 2021 Yuri N. Sedunov <aris@altlinux.org> 3.38.4-alt1
- 3.38.4

* Thu Jan 14 2021 Yuri N. Sedunov <aris@altlinux.org> 3.38.3-alt1
- 3.38.3

* Thu Dec 03 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.2-alt1
- 3.38.2

* Sat Oct 24 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.1-alt2
- updated to 3.38.1-31-gf5d1a2858

* Sat Oct 24 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.1-alt1
- 3.38.1

* Tue Sep 15 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Tue Sep 08 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.6-alt1
- 3.36.6

* Thu Aug 20 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.5-alt1
- 3.36.5

* Tue Jul 07 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.4-alt1
- 3.36.4

* Wed Jun 03 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.3-alt1
- 3.36.3

* Thu Apr 30 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.2-alt1
- 3.36.2

* Tue Mar 31 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.1-alt1
- 3.36.1

* Sun Mar 08 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1
- 3.36.0

* Mon Feb 17 2020 Yuri N. Sedunov <aris@altlinux.org> 3.34.4-alt1
- 3.34.4

* Sun Jan 05 2020 Yuri N. Sedunov <aris@altlinux.org> 3.34.3-alt1
- 3.34.3

* Thu Dec 12 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.2-alt1
- 3.34.2

* Wed Oct 09 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.1-alt1
- 3.34.1

* Mon Sep 09 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Sat May 25 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.2-alt1
- 3.32.2

* Wed May 01 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt2
- updated to 3.32.1-10-g059c729da
  (fixed https://gitlab.gnome.org/GNOME/gnome-shell/issues/1054)

* Wed Apr 17 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Tue Mar 12 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- updated to 3.32.0-14-g62233a4db

* Sat Jan 19 2019 Yuri N. Sedunov <aris@altlinux.org> 3.30.2-alt4
- updated to 3.30.2-9-gee97f7352
  (fixed https://gitlab.gnome.org/GNOME/gnome-shell/issues/391)

* Mon Jan 14 2019 Yuri N. Sedunov <aris@altlinux.org> 3.30.2-alt3
- updated to 3.30.2-7-g999cc1214

* Thu Dec 20 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.2-alt2
- fixed buildreqs for network-manager support

* Mon Nov 19 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.2-alt1
- 3.30.2

* Tue Oct 09 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Sun Sep 30 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt2
- updated to 3.30.0-50-gef5e195f3

* Tue Sep 04 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Sun Aug 19 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.3-alt2
- updated to 3.28.3-7-g721ce5403
- removed obsolete deps on caribou

* Thu Jul 19 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.3-alt1
- 3.28.3

* Tue Jul 03 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt2
- updated to 3.28.2-10-gda96408

* Wed May 09 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt1
- 3.28.2

* Sat Apr 14 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt1
- updated to 3.28.1-5-g69afe77

* Thu Mar 22 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt2
- update to 3.28.0-12-g526834e

* Tue Mar 13 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

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
