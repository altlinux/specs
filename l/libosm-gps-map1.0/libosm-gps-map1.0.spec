%define _name osm-gps-map
%define api_ver 1.0

Name: lib%_name%api_ver
Version: 1.1.0
Release: alt1

Summary: Gtk+3 widget for displaying map tiles

Group: System/Libraries
License: GPLv2+
Url: https://github.com/nzjrs/%_name/

Source: %url/releases/download/%version/%_name-%version.tar.gz

BuildRequires: gnome-common gtk-doc libgtk+3-devel libcairo-devel libsoup-devel
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
Requires: %name = %version-%release

%description devel
This package provides development files for the %_name Gtk+3 widget

%package gir
Summary: GObject introspection data for the %_name library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the %_name library.

%package gir-devel
Summary: GObject introspection devel data for the %_name library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

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
%configure --disable-static
%make_build

%install
%makeinstall_std

# move documentation to avoid conflict with gtk+2 version
mv %buildroot%_datadir/gtk-doc/html/libosmgpsmap{,-%api_ver}

%files
%doc AUTHORS README NEWS
%_libdir/libosmgpsmap-%api_ver.so.*

%files devel
%_includedir/osmgpsmap-%api_ver/
%_libdir/libosmgpsmap-%api_ver.so
%_pkgconfigdir/osmgpsmap-%api_ver.pc

%files gir
%_typelibdir/OsmGpsMap-%api_ver.typelib

%files gir-devel
%_girdir/OsmGpsMap-%api_ver.gir

%files devel-doc
%_datadir/gtk-doc/html/libosmgpsmap-%api_ver/

%exclude %_datadir/doc/%_name


%changelog
* Sat Apr 16 2016 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0

* Wed Nov 04 2015 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- first build for Sisyphus

