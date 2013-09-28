%define _name geocode-glib
%define ver_major 3.10
%define api_ver 1.0
%def_enable introspection

Name: lib%{_name}
Version: %ver_major.0
Release: alt1

Summary: Convenience library for the Yahoo! Place Finder APIs
License: LGPLv2+
Group: System/Libraries
Url: http://www.gnome.org/

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz

BuildPreReq: gnome-common libjson-glib-devel >= 0.16.2
BuildRequires: libgio-devel >= 2.34 libsoup-gnome-devel
BuildRequires: intltool gnome-doc-utils gtk-doc
%{?_enable_introspection:BuildRequires: libsoup-gnome-gir-devel libjson-glib-gir-devel}

%description
The %_name is a convenience library for the Yahoo! Place Finder APIs, as
described at http://developer.yahoo.com/geo/placefinder/

The Place Finder web service allows to do geocoding (finding longitude
and latitude from an address), and reverse geocoding (finding an address
from coordinates).

%package devel
Summary: Development files for %_name library
Group: Development/C
Requires: %name = %version-%release

%description devel
The %_name is a convenience library for the Yahoo! Place
Finder APIs, as described at http://developer.yahoo.com/geo/placefinder/

The Place Finder web service allows to do geocoding (finding longitude
and latitude from an address), and reverse geocoding (finding an address
from coordinates).

This package contains files needed to develop with %_name.

%package devel-doc
Summary: Development documentation for %_name
Group: Development/C
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
This package contains development documentation for %_name library.

%package gir
Summary: GObject introspection data for the %name
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the %_name library

%package gir-devel
Summary: GObject introspection devel data for the %name
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the %_name library

%prep
%setup -n %_name-%version

%build
%autoreconf
%configure --enable-gtk-doc
%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %_name

%files -f %_name.lang
%_libdir/*.so.*
%doc AUTHORS NEWS README

%files devel
%_includedir/%_name-%api_ver/
%_libdir/*.so
%_libdir/pkgconfig/%_name-%api_ver.pc

%files devel-doc
%_datadir/gtk-doc/html/%_name-%api_ver/

%if_enabled introspection
%files gir
%_typelibdir/GeocodeGlib-%api_ver.typelib

%files gir-devel
%_girdir/GeocodeGlib-%api_ver.gir
%endif

%changelog
* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Tue Jul 30 2013 Yuri N. Sedunov <aris@altlinux.org> 0.99.1-alt1
- 0.99.1

* Fri Sep 09 2011 Yuri N. Sedunov <aris@altlinux.org> 0.99.0-alt1
- first build for Sisyphus
