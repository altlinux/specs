%define _name libchamplain
%define ver_major 0.12
%define api_ver 0.12
%def_enable introspection
%def_enable vala
%def_disable gtk_doc

Name: %_name
Version: %ver_major.3
Release: alt1

Summary: Map view library for Clutter
License: LGPLv2+
Group: System/Libraries
Url: http://projects.gnome.org/%name/
Source: http://ftp.gnome.org/pub/GNOME/sources/%name/%ver_major/%_name-%version.tar.xz

%define glib_ver 2.16
%define cairo_ver 1.4
%define gtk_ver 3.0.1
%define clutter_ver 1.7.10
%define soup_ver 2.33.90
%define gir_ver 0.10.3

BuildPreReq: libgio-devel >= %glib_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libcairo-devel >= %cairo_ver
BuildPreReq: libclutter-devel >= %clutter_ver
BuildPreReq: libsoup-gnome-devel >= %soup_ver
BuildRequires: libclutter-gtk3-devel libsoup-devel libsqlite3-devel gtk-doc
%{?_enable_vala:BuildRequires: vala-tools}
%{?_enable_introspection:BuildRequires: gobject-introspection-devel >= 0.9.5 libgtk+3-gir-devel libclutter-gir-devel}

%description
Libchamplain is a C library aimed to provide a ClutterActor to display
rasterized maps.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains development files for %name.

%package devel-doc
Summary: Development documentation for %name
Group: Development/C
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
This package contains development documentation for %name.

%package gtk3
Summary: Gtk+ widget wrapper for %name
Group: System/Libraries
Requires: %name = %version-%release

%description gtk3
Libchamplain-gtk is a library providing a GtkWidget to embed %name
into Gtk+ applications.

%package gtk3-devel
Summary: Development files for %name-gtk
Group: Development/C
Requires: %name-gtk3 = %version-%release
Requires: %name-devel = %version-%release

%description gtk3-devel
This package contains development files for %name-gtk.

%package gtk3-devel-doc
Summary: Development documentation for %name-gtk
Group: Development/C
BuildArch: noarch
Conflicts: %name-gtk3 < %version

%description gtk3-devel-doc
This package contains development documentation for %name-gtk.

%package gir
Summary: GObject introspection data for the Libchamplain library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the Libchamplain library

%package gir-devel
Summary: GObject introspection devel data for the Libchamplain library
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the Libchamplain library

%package gtk3-gir
Summary: GObject introspection data for the Libchamplain library
Group: System/Libraries
Requires: %name-gtk3 = %version-%release
Requires: %name-gir = %version-%release

%description gtk3-gir
GObject introspection data for the Libchamplain library

%package gtk3-gir-devel
Summary: GObject introspection devel data for the Libchamplain library
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-gtk3-gir = %version-%release
Requires: %name-gir-devel = %version-%release

%description gtk3-gir-devel
GObject introspection devel data for the Libchamplain library

%package vala
Summary: Vala bindings for the Libchamplain library
Group: System/Libraries
BuildArch: noarch
Requires: %name = %version-%release

%description vala
This package provides Vala language bindings for the Libchamplain library


%prep
%setup -q -n %_name-%version

%build
%autoreconf
%configure --disable-static \
	%{?_enable_gtk_doc:--enable-gtk} \
	%{?_disable_vala:--disable-vala-demos} \
	--enable-introspection=auto

%make_build

%install
%make DESTDIR=%buildroot install

%files
%_libdir/%_name-%api_ver.so.*
%doc AUTHORS ChangeLog NEWS

%files devel
%_libdir/%_name-%api_ver.so
%dir %_includedir/%_name-%api_ver
%_includedir/%_name-%api_ver/champlain
%_libdir/pkgconfig/champlain-%api_ver.pc
%doc demos/animated-marker.c
%doc demos/launcher.c
%doc demos/polygons.c

#%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/%_name
#%endif

%files gtk3
%_libdir/%_name-gtk-%api_ver.so.*

%files gtk3-devel
%_libdir/%_name-gtk-%api_ver.so
%dir %_includedir/%_name-gtk-%api_ver
%_includedir/%_name-gtk-%api_ver/champlain-gtk
%_libdir/pkgconfig/champlain-gtk-%api_ver.pc
%doc demos/launcher-gtk.c
%doc demos/markers.c

#%if_enabled gtk_doc
%files gtk3-devel-doc
%_datadir/gtk-doc/html/%_name-gtk/
#%endif

%if_enabled introspection
%files gir
%_typelibdir/Champlain-%api_ver.typelib

%files gtk3-gir
%_typelibdir/GtkChamplain-%api_ver.typelib

%files gir-devel
%_girdir/Champlain-%api_ver.gir

%files gtk3-gir-devel
%_girdir/GtkChamplain-%api_ver.gir
%endif

%if_enabled vala
%files vala
%_datadir/vala/vapi/*
%endif

%changelog
* Mon Jul 16 2012 Yuri N. Sedunov <aris@altlinux.org> 0.12.3-alt1
- 0.12.3

* Mon Mar 12 2012 Yuri N. Sedunov <aris@altlinux.org> 0.12.2-alt1
- 0.12.2

* Wed Jan 04 2012 Yuri N. Sedunov <aris@altlinux.org> 0.12.1-alt1
- 0.12.1

* Sun Oct 30 2011 Yuri N. Sedunov <aris@altlinux.org> 0.12.0-alt1
- 0.12.0

* Thu Mar 31 2011 Yuri N. Sedunov <aris@altlinux.org> 0.8.3-alt1
- 0.8.3

* Tue Jan 18 2011 Yuri N. Sedunov <aris@altlinux.org> 0.8.1-alt1
- 0.8.1

* Sun Nov 07 2010 Yuri N. Sedunov <aris@altlinux.org> 0.8.0-alt2
- rebuild for update dependencies

* Tue Oct 05 2010 Yuri N. Sedunov <aris@altlinux.org> 0.8.0-alt1
- 0.8.0

* Thu Sep 09 2010 Yuri N. Sedunov <aris@altlinux.org> 0.7.1-alt1
- 0.7.1

* Sun Aug 22 2010 Yuri N. Sedunov <aris@altlinux.org> 0.4.7-alt1
- 0.4.7

* Wed Mar 31 2010 Yuri N. Sedunov <aris@altlinux.org> 0.4.5-alt2
- rebuild with new rpm-build-gir (0.2-alt1)

* Wed Mar 24 2010 Yuri N. Sedunov <aris@altlinux.org> 0.4.5-alt1
- 0.4.5

* Fri Jan 29 2010 Yuri N. Sedunov <aris@altlinux.org> 0.4.4-alt1
- 0.4.4
- python bindings

* Sun Jan 10 2010 Yuri N. Sedunov <aris@altlinux.org> 0.4.3-alt1
- 0.4.3
- new -gir{,-devel} subpackages
- prepared for build python-module-libchamplain (requires newer pyclutter{,-gtk})

* Sat Oct 31 2009 Yuri N. Sedunov <aris@altlinux.org> 0.4.2-alt1
- 0.4.2

* Mon Oct 19 2009 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- 0.4.1

* Mon Sep 14 2009 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- 0.4.0

* Mon Sep 14 2009 Yuri N. Sedunov <aris@altlinux.org> 0.3.92-alt1
- adapted for Sisyphus
- update to 0.3.92
- new devel-{,gtk-}doc noarch packages

* Mon Aug 24 2009 Matthias Clasen <mclasen@redhat.com> - 0.3.91-1
- Update to 0.3.91

* Tue Aug 11 2009 Matthias Clasen <mclasen@redhat.com> - 0.3.90-1
- Update to 0.3.90

* Mon Aug  3 2009 Matthias Clasen <mclasen@redhat.com> - 0.3.6-1
- Update to 0.3.6

* Sat Aug 02 2009 Debarshi Ray <rishi@fedoraproject.org> - 0.3.5-1
- Version bump to 0.3.5.
  * Marker selection API. (GNOME Bugzilla #577909)
  * http://ftp.gnome.org/pub/GNOME/sources/libchamplain/0.3/libchamplain-0.3.5.news
  * http://ftp.gnome.org/pub/GNOME/sources/libchamplain/0.3/libchamplain-0.3.4.news
  * http://ftp.gnome.org/pub/GNOME/sources/libchamplain/0.3/libchamplain-0.3.5.changes
  * http://ftp.gnome.org/pub/GNOME/sources/libchamplain/0.3/libchamplain-0.3.4.changes

* Fri Jul 24 2009 Release Engineering <rel-eng@fedoraproject.org> - 0.3.3-2
- Autorebuild for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Debarshi Ray <rishi@fedoraproject.org> - 0.3.3-1
- Version bump to 0.3.3.
  * Support for custom map sources and listing available map sources.
  * Smooth movement to a new position. (GNOME Bugzilla #557641)
  * Keep the center of the map in the center after a resize. (GNOME Bugzilla
    #557642)
  * Double click to zoom and center. (GNOME Bugzilla #557644)
  * Added a way to know the maximum and minimum zoom level. (GNOME Bugzilla
    #557965)
  * Fixed unwanted wrap effect when panning at zoom level >= 8. (GNOME
    Bugzilla #558020)
  * Fixed center on and zooming in behavior. (GNOME Bugzilla #558026)
  * Lack of user feedback during loading of tiles. (GNOME Bugzilla #559522)
  * Added missing zoom level to OpenStreetMap Mapnik. (GNOME Bugzilla
    #559446)
  * Fixed wrong elastic effect affecting Emapthy's map view. (GNOME Bugzilla
    #561700)
  * Added disk cache management. (GNOME Bugzillla #568931)
  * Host application should be able to limit the maximum and minimum zoom
    levels. (GNOME Bugzilla #571702)
  * Allow host applications to draw lines/routes on the map. (GNOME Bugzilla
    #572377)
  * Support proxies. (GNOME Bugzilla #573937)
  * Provide a way to make visible a bunch of markers. (GNOME Bugzilla #574809)
  * Do not allow negative zoom levels. (GNOME Bugzilla #575138)
  * Fixed corrupted map when double-clicking at maximum level. (GNOME Bugzilla
    #575139)
  * Prevent ChamplainNetworkMapSource from crashing when setting "proxy-uri".
    (GNOME Bugzilla #575902).
  * Implemented advanced markers. (GNOME Bugzilla #576055)
  * Various memory management fixes for ChamplainTile. (GNOME Bugzilla
    #576159)
  * Any go_to should stop a previous and not yet finished go_to. (GNOME
    Bugzilla #576832)
  * Prevent segmentation fault on 32 bit platforms. (GNOME Bugzilla #576698)
  * Introduced a new signal called ChamplainView::animation-completed. (GNOME
    Bugzilla #577169)
  * Set decel-rate correctly. (GNOME Bugzilla #580785)
  * champlain_network_map_source_fill_tile should be private. (GNOME Bugzilla
    #582786)
  * Fixed champlain_view_center_on. (GNOME Bugzilla #583502)
  * Fixed "longitude" and "latitude" properties, which were reversed. (GNOME
    Bugzilla #584365)
  * Make the cache work the first time. (GNOME Bugzilla #584390)
  * GNOME Goal: use accessor functions instead direct access. (GNOME Bugzilla
    #585698)
- Added 'BuildRequires: chrpath' for removing rpaths.

* Wed Mar 18 2009 Debarshi Ray <rishi@fedoraproject.org> - 0.2.9-1
- Version bump to 0.2.9.
  * Fixed elastic effect.
  * Reduced exported symbols.

* Wed Feb 25 2009 Release Engineering <rel-eng@fedoraproject.org> - 0.2.8-3
- Autorebuild for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 28 2009 Debarshi Ray <rishi@fedoraproject.org> - 0.2.8-2
- Removed 'Requires: clutter-devel >= 0.8 pkgconfig' from libchamplain-devel
  for all distributions, except Fedora 10.
- Fixed sample code to not use generic headers.

* Wed Jan 14 2009 Debarshi Ray <rishi@fedoraproject.org> - 0.2.8-1
- Initial build. Imported SPEC from openSUSE.
  * Added a new constructor for ChamplainMarkers made of an image.
  * Double clicking on the map will now zoom and recenter.
  * When resizing a ChamplainView, the centered content will still be
    centered after the resizing. Can be disabled.
  * The Map's license is displayed by default on the lower right corner.
  * Fixed map centering on startup.
  * Fixed missing zoom level in OpenStreetMap Mapnik.
  * Fixed zooming and centering behaviour. (GNOME Bugzilla #558026)
