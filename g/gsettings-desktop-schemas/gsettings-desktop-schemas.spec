%define ver_major 3.4
%def_enable introspection

Name: gsettings-desktop-schemas
Version: %ver_major.2
Release: alt1

Summary: A collection of GSettings schemas
License: %lgpl21plus
Group: Graphical desktop/GNOME
URL: ftp://ftp.gnome.org/
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

Requires: %name-data = %version-%release

%define gio_ver 2.31.0
PreReq: libgio >= %gio_ver
BuildPreReq: rpm-build-licenses rpm-build-gnome
BuildRequires: libgio-devel >= %gio_ver intltool
%{?_enable_introspection:BuildRequires: gobject-introspection-devel}

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
Requires: %name = %version-%release

%description devel
This package contains development files for %name

%package gir
Summary: GObject introspection data for %name
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for %name.

%package gir-devel
Summary: GObject introspection devel data for %name
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for %name.

%prep
%setup -q

%build
%configure --disable-schemas-compile \
	%{?_enable_introspection:--enable-introspection=yes}

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %name

%files

%files data -f %name.lang
%_datadir/glib-2.0/schemas/org.gnome.desktop.a11y.applications.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.desktop.a11y.keyboard.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.desktop.a11y.magnifier.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.desktop.a11y.mouse.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.desktop.background.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.desktop.default-applications.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.desktop.enums.xml
%_datadir/glib-2.0/schemas/org.gnome.desktop.interface.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.system.locale.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.desktop.lockdown.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.desktop.media-handling.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.desktop.screensaver.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.desktop.session.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.desktop.sound.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.desktop.thumbnail-cache.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.desktop.thumbnailers.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.desktop.wm.keybindings.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.desktop.wm.preferences.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.system.proxy.gschema.xml
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


