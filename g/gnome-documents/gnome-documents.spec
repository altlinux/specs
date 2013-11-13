%define ver_major 3.10
%define api_ver 1.0
%define _libexecdir %_prefix/libexec

Name: gnome-documents
Version: %ver_major.1
Release: alt1

Summary: A document manager application for GNOME
Group: Office
License: GPLv2+
Url: https://live.gnome.org/Design/Apps/Documents

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

Requires: %name-data = %version-%release
Requires: gnome-online-miners

%define pkglibdir %_libdir/%name
%define pkgdatadir %_datadir/%name
%set_typelibdir %pkglibdir
%set_girdir %pkgdatadir

%define glib_ver 2.37.0
%define gtk_ver 3.9.11
%define evince_ver 3.7.4
%define tracker_ver 0.15.2
%define goa_ver 3.2.0
%define gdata_ver 0.13.3
%define soup_ver 2.41.3
%define gi_ver 1.31.6


BuildRequires: intltool yelp-tools desktop-file-utils docbook-style-xsl
BuildRequires: libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver
BuildRequires: libgnome-desktop3-devel libgdata-devel >= %gdata_ver
BuildRequires: liboauth-devel libgnome-online-accounts-devel >= %goa_ver
BuildRequires: tracker-devel >= %tracker_ver libevince-devel >= %evince_ver
BuildRequires: libsoup-devel >= %soup_ver
BuildRequires: libwebkitgtk3-devel
BuildRequires: libzapojit-devel
BuildRequires: gobject-introspection-devel >= %gi_ver
BuildRequires: libgtk+3-gir-devel libgjs-devel libevince-gir-devel
BuildRequires: libgdata-gir-devel libgnome-online-accounts-gir-devel libtracker-gir-devel
BuildRequires: libzapojit-gir-devel

%description
gnome-documents is a document manager application for GNOME,
aiming to be a simple and elegant replacement for using Files to show
the Documents directory.

%package data
Summary: Arch independent files for %name
Group: Office
BuildArch: noarch
Requires: %name-gir = %version-%release

%description data
This package provides noarch data needed for %name to work.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package gir
Summary: GObject introspection data for %name
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the %name library.

%package gir-devel
Summary: GObject introspection devel data for %name
Group: Development/Other
BuildArch: noarch
Requires: %name-devel = %version-%release
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the %name library.


%prep
%setup

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std
%find_lang --with-gnome %name

%files
%_bindir/%name
%dir %pkglibdir
%pkglibdir/*.so
%exclude %pkglibdir/*.la
%_man1dir/%name.1.*
%doc README AUTHORS NEWS TODO

%files gir
%dir %pkglibdir/girepository-1.0
%pkglibdir/girepository-1.0/Gd-%api_ver.typelib
%pkglibdir/girepository-1.0/GdPrivate-1.0.typelib

%files data -f %name.lang
%pkgdatadir/
%exclude %pkgdatadir/gir-1.0
%_datadir/applications/%name.desktop
%_datadir/dbus-1/services/org.gnome.Documents.SearchProvider.service
%_datadir/glib-2.0/schemas/org.gnome.Documents.enums.xml
%_datadir/glib-2.0/schemas/org.gnome.documents.gschema.xml
%_datadir/gnome-shell/search-providers/gnome-documents-search-provider.ini
%_iconsdir/hicolor/*/apps/%name.png
%_datadir/appdata/%name.appdata.xml


%changelog
* Wed Nov 13 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Fri Aug 30 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.4-alt1
- 3.8.4

* Fri Jun 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.3.1-alt1
- 3.8.3.1

* Mon Jun 10 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.3-alt1
- 3.8.3

* Tue May 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2.1-alt1
- 3.8.2.1

* Tue Apr 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Mon Mar 25 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0
- arch independent data moved to separate subpackage

* Tue Nov 13 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1
- 3.6.2

* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Thu Sep 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Tue May 15 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.2-alt1
- 0.4.2

* Tue Apr 17 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- 0.4.1

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.0.1-alt1
- 0.4.0.1

* Mon Nov 07 2011 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt1
- first build for Sisyphus

