%def_disable snapshot

%define xdg_name org.gnome.Documents
%define xdg_name1 org.gnome.Books
%define ver_major 3.26
%define api_ver 1.0
%define _libexecdir %_prefix/libexec

Name: gnome-documents
Version: %ver_major.2
Release: alt1

Summary: A document manager application for GNOME
Group: Office
License: GPLv2+
Url: https://wiki.gnome.org/Apps/Documents

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

%define lok_ver 5.2-alt2

Requires: %name-data = %version-%release
Requires: gnome-online-miners
Requires: libreofficekit >= %lok_ver

# find ./ -name "*.js" |/usr/lib/rpm/gir-js.req |sort|uniq|sed -e 's/^/Requires: /'
Requires: typelib(cairo)
Requires: typelib(EvinceDocument)
Requires: typelib(EvinceView)
Requires: typelib(Gd)
Requires: typelib(GData)
Requires: typelib(Gdk)
Requires: typelib(GdkPixbuf)
Requires: typelib(GdPrivate)
Requires: typelib(Gepub)
Requires: typelib(Gio)
Requires: typelib(GLib)
Requires: typelib(GnomeDesktop)
Requires: typelib(Goa)
Requires: typelib(GObject)
Requires: typelib(Gtk)
Requires: typelib(LOKDocView)
Requires: typelib(Pango)
Requires: typelib(Tracker) = 2.0
Requires: typelib(TrackerControl)
Requires: typelib(WebKit2)
Requires: typelib(Zpj)

%define pkglibdir %_libdir/%name
%define pkgdatadir %_datadir/%name
%set_typelibdir %pkglibdir
%set_girdir %pkgdatadir

%define glib_ver 2.40.0
%define gtk_ver 3.20.0
%define evince_ver 3.13.3
%define tracker_ver 1.99
%define goa_ver 3.2.0
%define gdata_ver 0.17.2
%define soup_ver 2.41.3
%define gi_ver 1.31.6
%define gepub_ver 0.5

BuildRequires: autoconf-archive yelp-tools desktop-file-utils docbook-style-xsl
BuildRequires: libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver
BuildRequires: libgnome-desktop3-devel libgdata-devel >= %gdata_ver
BuildRequires: liboauth-devel libgnome-online-accounts-devel >= %goa_ver
BuildRequires: pkgconfig(tracker-control-2.0) pkgconfig(tracker-sparql-2.0)
BuildRequires: libevince-devel >= %evince_ver
BuildRequires: libsoup-devel >= %soup_ver
BuildRequires: libwebkit2gtk-devel
BuildRequires: libzapojit-devel
BuildRequires: gobject-introspection-devel >= %gi_ver
BuildRequires: libgtk+3-gir-devel libgjs-devel libevince-gir-devel libgnome-desktop3-gir-devel
BuildRequires: libgdata-gir-devel libgnome-online-accounts-gir-devel libtracker-gir-devel >= %tracker_ver
BuildRequires: libzapojit-gir-devel libgepub-gir-devel >= %gepub_ver
BuildRequires: librsvg

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
%_bindir/gnome-books
%dir %pkglibdir
%pkglibdir/*.so
%exclude %pkglibdir/*.la
%_man1dir/%name.1.*
%_man1dir/gnome-books.1.*
# contains arch dependent scripts
%pkgdatadir/
%exclude %pkgdatadir/gir-1.0
%doc README AUTHORS NEWS TODO

%files gir
%dir %pkglibdir/girepository-1.0
%pkglibdir/girepository-1.0/Gd-%api_ver.typelib
%pkglibdir/girepository-1.0/GdPrivate-1.0.typelib

%files data -f %name.lang
%_desktopdir/%xdg_name.desktop
%_desktopdir/%xdg_name1.desktop
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/dbus-1/services/%xdg_name1.service
%_datadir/glib-2.0/schemas/%xdg_name.enums.xml
%_datadir/glib-2.0/schemas/org.gnome.documents.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.books.gschema.xml
%_datadir/gnome-shell/search-providers/%xdg_name.search-provider.ini
%_iconsdir/hicolor/*/apps/*.png
%_iconsdir/hicolor/scalable/apps/*.svg
%_datadir/appdata/%xdg_name.appdata.xml
%_datadir/appdata/%xdg_name1.appdata.xml

%changelog
* Thu Feb 01 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt1
- 3.26.2

* Tue Oct 03 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Thu Sep 14 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Fri Jul 21 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.3-alt1
- 3.24.3

* Thu May 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.2-alt1
- 3.24.2

* Wed Apr 12 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt1
- 3.24.1

* Mon Mar 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Sun Mar 12 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Wed Aug 17 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Tue Jul 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt2
- updated to 3.20.0-11-gb2c58e7
- updated reqs

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.3-alt1
- 3.18.3

* Wed Nov 11 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Wed Oct 14 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1.2
- fixed files section

* Wed Oct 14 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1.1
- %%pkgdatadir/ moved to main package

* Tue Oct 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Tue Sep 22 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0.1-alt1
- 3.18.0.1

* Fri Sep 11 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.4-alt1
- 3.16.4

* Sun Aug 09 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.3-alt2
- rebuilt against libgdata.so.22

* Mon Aug 03 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.3-alt1
- 3.16.3

* Mon May 11 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Fri Nov 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Fri Oct 17 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Wed Sep 24 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Fri Aug 22 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt2
- rebuilt against libgdata.so.19

* Fri May 02 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Tue Mar 11 2014 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

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

