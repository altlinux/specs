%define ver_major 3.14
%define api_ver 2.0

Name: glade
Version: %ver_major.2
Release: alt1

Summary: A user interface designer for Gtk+ and GNOME
Group: Development/GNOME and GTK+
License: %gpl2plus, %lgpl2plus
URL: http://glade.gnome.org/
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

Requires: libgladeui%api_ver = %version-%release

BuildPreReq: rpm-build-licenses rpm-build-gnome
# From configure.ac
BuildPreReq: intltool >= 0.50
BuildPreReq: libgtk+3-devel >= 3.6.0
BuildRequires: gnome-common gtk-doc yelp-tools
BuildRequires: libxml2-devel
BuildRequires: python-module-pygobject3-devel
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel

%description
Glade is a Widget builder for Gtk/gnome. It allows to create a GTK+/GNOME
interface files that can be loaded with GladeUI library.

%package -n libgladeui%api_ver
Summary: GTK+/GNOME3 widget builder library
Group:   Development/GNOME and GTK+

%description -n libgladeui%api_ver
Glade is a Widget builder for Gtk/gnome. It allows to create a GTK+/GNOME
interface files that can be loaded with libgladeui.
This is library that can be used for embed builder into other
applications.

%package -n libgladeui%api_ver-devel
Summary: GTK+3/GNOME3 widget builder library
Group:   Development/GNOME and GTK+
Requires: libgladeui%api_ver = %version-%release

%description -n libgladeui%api_ver-devel
Glade is a Widget builder for Gtk/gnome. It allows to create a GTK+/GNOME
interface files that can be loaded with libgladeui.

This package contains development files for GladeUI library.

%package -n libgladeui%api_ver-devel-doc
Summary: GladeUI development documentation
Group: Development/Documentation
BuildArch: noarch
Conflicts: libgladeui%api_ver-devel < %version

%description -n libgladeui%api_ver-devel-doc
This package contains documentation needed to develop applications using
GladeUI library.

%package -n libgladeui%api_ver-gir
Summary: GObject introspection data for the GladeUI
Group: System/Libraries
Requires: libgladeui%api_ver = %version-%release

%description -n libgladeui%api_ver-gir
GObject introspection data for the GladeUI library.

%package -n libgladeui%api_ver-gir-devel
Summary: GObject introspection devel data for the GladeUI
Group: Development/Other
BuildArch: noarch
Requires: libgladeui%api_ver-gir = %version-%release
Requires: libgladeui%api_ver-devel = %version-%release

%description -n libgladeui%api_ver-gir-devel
GObject introspection devel data for the GladeUI library.

%prep
%setup

%build
%autoreconf
%configure \
	--enable-gtk-doc

%make_build

%install
%makeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/*
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*.png
%doc AUTHORS COPYING NEWS README TODO

%files -n libgladeui%api_ver
%dir %_libdir/%name
%dir %_libdir/%name/modules
%_libdir/%name/modules/*.so
%_libdir/*.so.*
%dir %_datadir/%name
%dir %_datadir/%name/catalogs
%_datadir/%name/catalogs/*.xml
%_datadir/%name/catalogs/glade-catalog.dtd
%_datadir/%name/pixmaps

%exclude %_libdir/%name/modules/*.la

%files -n libgladeui%api_ver-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%files -n libgladeui%api_ver-devel-doc
%_datadir/gtk-doc/html/*

%files -n libgladeui%api_ver-gir
%_typelibdir/Gladeui-2.0.typelib

%files -n libgladeui%api_ver-gir-devel
%_girdir/Gladeui-2.0.gir

%changelog
* Tue Dec 04 2012 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- first build for Sisyphus

