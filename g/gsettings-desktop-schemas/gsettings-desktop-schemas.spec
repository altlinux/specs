%define _unpackaged_files_terminate_build 1

%define ver_major 44
%define beta %nil
%def_enable introspection

Name: gsettings-desktop-schemas
Version: %ver_major.0
Release: alt1%beta

Summary: A collection of GSettings schemas
License: %lgpl21plus
Group: Graphical desktop/GNOME
Url: ftp://ftp.gnome.org/

Source: %gnome_ftp/%name/%ver_major/%name-%version%beta.tar.xz

Requires: %name-data = %EVR

%define gio_ver 2.31.0
Requires(pre): libgio >= %gio_ver

BuildRequires(pre): rpm-macros-meson rpm-build-licenses rpm-build-gnome
BuildRequires: meson libgio-devel >= %gio_ver
%{?_enable_introspection:BuildRequires(pre): rpm-build-gir
BuildRequires: gobject-introspection-devel}

%description
%name contains a collection of GSettings schemas for settings shared by
various components of a desktop.

%package data
Summary: Shared GSettings schemas for the GNOME desktop
Group: Graphical desktop/GNOME
BuildArch: noarch

%description data
This package contains a collection of GSettings schemas for settings
shared by various components of a desktop.

%package devel
Summary: Development package for %name
Group: Development/Other
BuildArch: noarch
Requires: %name = %EVR

%description devel
This package contains development files for %name

%package gir
Summary: GObject introspection data for %name
Group: System/Libraries
Requires: %name = %EVR

%description gir
GObject introspection data for %name.

%package gir-devel
Summary: GObject introspection devel data for %name
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %EVR
Requires: %name-devel = %EVR

%description gir-devel
GObject introspection devel data for %name.

%prep
%setup -n %name-%version%beta

%build
%meson \
	%{?_enable_introspection:-Dintrospection=true}
%meson_build

%install
%meson_install
%find_lang %name

%files

%files data -f %name.lang
%_datadir/glib-2.0/schemas/org.gnome.desktop.a11y.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.desktop.a11y.interface.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.desktop.a11y.applications.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.desktop.a11y.keyboard.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.desktop.a11y.magnifier.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.desktop.a11y.mouse.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.desktop.app-folders.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.desktop.background.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.desktop.calendar.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.desktop.datetime.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.desktop.default-applications.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.desktop.enums.xml
%_datadir/glib-2.0/schemas/org.gnome.desktop.input-sources.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.desktop.interface.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.system.locale.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.desktop.lockdown.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.desktop.media-handling.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.desktop.peripherals.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.desktop.screensaver.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.desktop.session.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.desktop.sound.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.desktop.thumbnail-cache.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.desktop.thumbnailers.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.desktop.wm.keybindings.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.desktop.wm.preferences.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.system.location.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.system.proxy.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.desktop.notifications.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.desktop.privacy.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.desktop.search-providers.gschema.xml

%_datadir/GConf/gsettings/gsettings-desktop-schemas.convert
%_datadir/GConf/gsettings/wm-schemas.convert
%doc AUTHORS README NEWS

%files devel
%_includedir/gsettings-desktop-schemas/gdesktop-enums.h
%_datadir/pkgconfig/gsettings-desktop-schemas.pc

%if_enabled introspection
%files gir
%_typelibdir/GDesktopEnums-3.0.typelib

%files gir-devel
%_girdir/GDesktopEnums-3.0.gir
%endif

%changelog
* Mon Mar 20 2023 Yuri N. Sedunov <aris@altlinux.org> 44.0-alt1
- 44.0

* Tue Sep 20 2022 Yuri N. Sedunov <aris@altlinux.org> 43.0-alt1
- 43.0

* Sun Mar 20 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0-alt1
- 42.0

* Sat Sep 18 2021 Yuri N. Sedunov <aris@altlinux.org> 41.0-alt1
- 41.0

* Sun Mar 21 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt1
- 40.0

* Mon Sep 14 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Thu Apr 30 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.1-alt1
- 3.36.1

* Mon Mar 09 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1
- 3.36.0

* Tue Sep 10 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Mon Sep 09 2019 Yuri N. Sedunov <aris@altlinux.org> 3.33.92-alt1
- 3.33.92

* Tue Mar 12 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Tue Sep 04 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt1
- 3.28.1

* Mon Mar 12 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Mon Sep 04 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt1
- 3.24.1

* Mon Mar 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Tue Sep 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Tue Oct 20 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Mon Apr 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Thu Mar 26 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Wed Oct 15 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Tue May 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Mon Mar 24 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Wed Oct 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Tue May 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Mon Mar 25 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Tue Nov 13 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Tue Oct 09 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt2
- updated to f5b671c

* Tue Sep 25 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Tue May 15 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Mon Apr 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon Mar 19 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.92-alt1
- 3.3.92

* Mon Sep 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Wed Apr 27 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Fri Apr 08 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt2
- fixed https://bugzilla.gnome.org/show_bug.cgi?id=647039

* Mon Apr 04 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Tue Mar 22 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.92-alt1
- 2.91.92

* Tue Feb 22 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.7-alt1
- 0.1.7

* Wed Nov 17 2010 Yuri N. Sedunov <aris@altlinux.org> 0.1.1-alt1
- 0.1.1

* Fri Aug 06 2010 Yuri N. Sedunov <aris@altlinux.org> 0.0.1-alt1
- first build for Sisyphus


