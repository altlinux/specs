%def_enable snapshot
%define _name osm-gps-map
%define libname osmgpsmap
%define namespace OsmGpsMap
%define api_ver 1.0

%def_enable gtk_doc

Name: lib%_name%api_ver
Version: 1.2.1
Release: alt1

Summary: Gtk+3 widget for displaying map tiles
Group: System/Libraries
License: GPL-2.0-or-later
Url: https://github.com/nzjrs/osm-gps-map/

Vcs: https://github.com/nzjrs/osm-gps-map.git
%if_disabled snapshot
Source: %url/releases/download/%version/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif

BuildRequires: autoconf-archive gtk-doc
BuildRequires: libgtk+3-devel libcairo-devel pkgconfig(libsoup-3.0)
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel

%description
%_name is a Gtk+3 mapping widget that when given GPS co-ordinates,
draws a GPS track, and points of interest on a moving map display.

%name downloads map data from a number of websites, including
openstreetmap.org, openaerialmap.org and others and can be used to build
desktop mapping or geolocation applications.

%package devel
Summary: Development files for the %_name Gtk+3 widget
Group: Development/C
Requires: %name = %EVR

%description devel
This package provides development files for the %_name Gtk+3 widget

%package gir
Summary: GObject introspection data for the %_name library
Group: System/Libraries
Requires: %name = %EVR

%description gir
GObject introspection data for the %_name library.

%package gir-devel
Summary: GObject introspection devel data for the %_name library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %EVR
Requires: %name-devel = %EVR

%description gir-devel
GObject introspection devel data for the %_name library.

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
This package provides development documentation for %_name library.


%prep
%setup -n %_name-%version

%build
%autoreconf
%configure \
    --disable-static \
    %{subst_enable gtk_doc}
%nil
%make_build

%install
%makeinstall_std

%if_enabled gtk_doc
# move documentation to avoid conflict with gtk+2 version
mv %buildroot%_datadir/gtk-doc/html/lib%libname{,-%api_ver}
%endif

%files
%doc AUTHORS README NEWS
%_libdir/lib%libname-%api_ver.so.*

%files devel
%_includedir/%libname-%api_ver/
%_libdir/lib%libname-%api_ver.so
%_pkgconfigdir/%libname-%api_ver.pc

%files gir
%_typelibdir/%namespace-%api_ver.typelib

%files gir-devel
%_girdir/%namespace-%api_ver.gir

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/lib%libname-%api_ver/
%endif

%exclude %_datadir/doc/%_name


%changelog
* Sun Oct 04 2026 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- updated to 1.2.1-47-gd4f2b75 (ported to libsoup-3.0)

* Mon Feb 08 2021 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Sat Apr 16 2016 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0

* Wed Nov 04 2015 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- first build for Sisyphus

