%define _libexecdir %_prefix/libexec
%define ver_major 3.4
%def_enable gnome_bluetooth
%def_with systemd

Name: gnome-shell
Version: %ver_major.1
Release: alt1

Summary: Window management and application launching for GNOME
Group: Graphical desktop/GNOME
License: GPLv2+
Url: http://live.gnome.org/GnomeShell
Packager: GNOME Maintainers Team <gnome at packages.altlinux.org>

Source: http://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
Patch1: %name-3.3.91-alt-gir.patch
# use gnome3-applications.menu
Patch2: %name-3.2.0-avoid-alt-menus.patch
Patch3: %name-3.4.1-alt-invalid_user_shell.patch

# https://bugzilla.gnome.org/show_bug.cgi?id=645433
Patch10: gnome-shell-3.2.1-subpixel_font_rendering.patch

# boyarch@
Patch20: 0001-org-gnome-shell-use-litebox-setting-introduced.patch
# manowar@
Patch21: gnome-shell-show-hide-timer.patch

Requires: %name-data = %version-%release

%define clutter_ver 1.9.12
%define gjs_ver 1.29.16
%define mutter_ver 3.4.1
%define gtk_ver 3.3.9
%define gio_ver 2.31.6
%define gstreamer_ver 0.10.16
%define eds_ver 2.91.6
%define telepathy_ver 0.17.5
%define telepathy_logger_ver 0.2.4
%define polkit_ver 0.100
%define bluetooth_ver 3.2.0
%define folks_ver 0.5.2
%define gi_ver 0.10.1
%define sn_ver 0.11
%define gcr_ver 3.3.90

Requires: mutter-gnome >= %mutter_ver
Requires: ca-certificates
Requires: at-spi2-atk
Requires: caribou

BuildRequires: gnome-common intltool gtk-doc
BuildRequires: python-devel
BuildRequires: libX11-devel libXfixes-devel
BuildRequires: libclutter-devel >= %clutter_ver libclutter-gir-devel
BuildRequires: libdbus-glib-devel
BuildRequires: libgjs-devel >= %gjs_ver
BuildRequires: glib2-devel libgio-devel >= %gio_ver
BuildRequires: libxml2-devel
BuildRequires: libgnome-menus-devel libgnome-menus-gir-devel
BuildRequires: libGConf-devel
BuildRequires: libgnome-desktop3-devel
BuildRequires: libgnome-keyring-devel
BuildRequires: gcr-libs-devel >= %gcr_ver
BuildRequires: libstartup-notification-devel >= %sn_ver
BuildRequires: gobject-introspection-devel >= %gi_ver
BuildRequires: libcroco-devel
BuildRequires: libcanberra-devel
BuildRequires: libpulseaudio-devel
%{?_enable_gnome_bluetooth:BuildRequires: libgnome-bluetooth-devel >= %bluetooth_ver libgnome-bluetooth-gir-devel gnome-bluetooth}
BuildRequires: evolution-data-server-devel >= %eds_ver
# for screencast recorder functionality
BuildRequires: gstreamer-devel >= %gstreamer_ver
BuildRequires: libXfixes-devel
BuildRequires: libgtk+3-devel >= %gtk_ver libgtk+3-gir-devel
# used in unused BigThemeImage
BuildRequires: libmutter-devel >= %mutter_ver libmutter-gir-devel
BuildRequires: mutter >= %mutter_ver
BuildRequires: libpolkit-devel >= %polkit_ver
BuildRequires: libtelepathy-glib-devel >= %telepathy_ver libtelepathy-glib-gir-devel libtelepathy-logger-gir-devel
BuildRequires: libtelepathy-logger-devel >= %telepathy_logger_ver
BuildRequires: libfolks-devel >= %folks_ver libfolks-gir-devel
BuildRequires: libgudev-devel libgudev-gir-devel
BuildRequires: gsettings-desktop-schemas-devel >= 0.1.7
BuildRequires: NetworkManager-glib-devel >= 0.8.995 NetworkManager-glib-gir-devel
BuildRequires: libsoup-gir-devel ca-certificates
# for browser plugin
BuildRequires: browser-plugins-npapi-devel
%{?_with_systemd:BuildRequires: systemd-devel}

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

%prep
%setup -q
%patch1 -p1 -b .gir
%patch2 -p1 -b .menu
%patch3 -b .shells
#%patch10 -p1 -b .font_rend
%patch20 -p2 -b .modal
%patch21 -p2 -b .timer

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
	--enable-gtk-doc \
    --disable-schemas-compile \
    --enable-compile-warnings=minimum \
    --with-ca-certificates=%_datadir/ca-certificates/ca-bundle.crt \
    %{subst_with systemd}
%make

%check
%make check

%install
%make DESTDIR=%buildroot \
	mozillalibdir=%browser_plugins_path install

rm -f %buildroot%_libdir/%name/*.la

%find_lang %name

%files
%_bindir/*
%_libexecdir/gnome-shell-calendar-server
%_libexecdir/gnome-shell-perf-helper
%_libexecdir/gnome-shell-hotplug-sniffer
%dir %_libdir/%name
%_libdir/%name/libgnome-shell.so
%_libdir/%name/libgnome-shell-js.so
%_typelibdir/*.typelib
# browser plugin
%browser_plugins_path/libgnome-shell-browser-plugin.so
%exclude %browser_plugins_path/libgnome-shell-browser-plugin.la

%files data -f %name.lang
%_datadir/applications/%name.desktop
%_datadir/applications/%name-extension-prefs.desktop
%_datadir/%name/
%_datadir/dbus-1/services/org.gnome.Shell.CalendarServer.service
%_datadir/dbus-1/services/org.gnome.Shell.HotplugSniffer.service
%_datadir/dbus-1/interfaces/org.gnome.ShellSearchProvider.xml
%_datadir/GConf/gsettings/gnome-shell-overrides.convert
%config %_datadir/glib-2.0/schemas/org.gnome.shell.gschema.xml
%_man1dir/*
%doc README NEWS

%files devel-doc
%_datadir/gtk-doc/html/shell/
%_datadir/gtk-doc/html/st/

%changelog
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
