%define ver_major 0.14

%add_verify_elf_skiplist %_bindir/tracker-needle

%def_enable introspection
%def_disable hal
%def_enable upower
%def_enable libxml2
%def_enable gdkpixbuf
%def_enable gnome_keyring
%def_enable network_manager
%def_enable evolution
%def_disable rss
%def_enable flickr
%def_enable explorer
%def_enable search_bar
%def_enable preferences
%def_enable tracker_search_tool
%def_enable poppler
%def_enable libexif
%def_enable libiptcdata
%def_enable libgsf
%def_enable libjpeg
%def_enable libtiff
%def_enable libvorbis
%def_enable libflac
%def_enable exempi
%def_enable playlist
%def_enable nautilus_extension
%def_disable gtk_doc
%def_enable taglib
%def_enable needle
%def_disable qt
%def_enable libgif
%def_enable libcue
%def_enable libosinfo

# Unicode support library? (libunistring|libicu)
%define unicode_support libicu

%define _libexecdir %_prefix/libexec

Name: tracker
Version: %ver_major.1
Release: alt1

Summary: Tracker is a powerfull desktop-oriented search tool and indexer
License: GPLv2+
Group: Office
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>
Url: http://projects.gnome.org/tracker/

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar
Patch: %name-%version-%release.patch

Obsoletes: lib%name-client

%define dbus_ver 1.3.1
%define glib_ver 2.28.0
%define pango_ver 1.0.0
%define gtk_ver 3.0.0
%define libxml2_ver 2.6
%define hal_ver 0.5
%define upower_ver 0.9.0
%define gdkpixbuf_ver 2.12.0
%define qt_ver 4.7.1
%define poppler_ver 0.16.0
%define cairo_ver 1.0
%define gdk_ver 1.0
%define vorbis_ver 0.22
%define flac_ver 1.2.1
%define libexif_ver 0.6
%define libgfs_ver 1.13
%define exempi_ver 2.1.0
%define evo_ver 2.32.0
%define eds_ver 2.32.0
%define gee_ver 0.3
%define taglib_ver 1.6
%define gnome_keyring_ver 2.26
%define libgrss_ver 0.3
%define rest_ver 0.7
%define nm_ver 0.8
%define gst_ver 0.10.31
%define gupnp_ver 0.5
%define sqlite3_ver 3.7.0
%define libosinfo_ver 0.0.2

BuildPreReq: gcc-c++ gnome-common rpm-build-gnome gtk-doc docbook-utils
BuildPreReq: glibc-devel
BuildPreReq: libdbus-devel >= %dbus_ver
BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: libgio-devel >= %glib_ver
BuildPreReq: libicu-devel libunistring-devel
BuildPreReq: libpango-devel >= %pango_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
%{?_enable_introspection:BuildPreReq: gobject-introspection-devel >= 0.9.5}
%{?_enable_hal:BuildPreReq: libhal-devel >= %hal_ver}
%{?_enable_upower:BuildPreReq: libupower-devel >= %upower_ver}
%{?_enable_network_manager:BuildPreReq: NetworkManager-glib-devel >= %nm_ver}
%{?_enable_libxml2:BuildPreReq: libxml2-devel >= %libxml2_ver}
BuildPreReq: libpng-devel >= 1.2
BuildPreReq: libuuid-devel
BuildPreReq: libenca-devel >= 1.9
BuildPreReq: vala >= 0.12.0
BuildPreReq: intltool >= 0.35.0
BuildPreReq: sqlite3 libsqlite3-devel >= %sqlite3_ver
BuildRequires: gstreamer-devel >= %gst_ver gst-plugins-devel >= %gst_ver
BuildRequires: libgupnp-dlna-devel >= %gupnp_ver
%{?_enable_gnome_keyring:BuildPreReq: libgnome-keyring-devel >= %gnome_keyring_ver}
%{?_enable_rss:BuildPreReq: libgrss-devel >= %libgrss_ver}
%{?_enable_tracker_search_tool:BuildPreReq: libgee-devel >= %gee_ver}
%{?_enable_flickr:BuildPreReq: librest-devel >= %rest_ver}
%{?_enable_explorer:BuildPreReq: libgee-devel >= %gee_ver}
%{?_enable_search_bar:BuildPreReq: libgnome-panel-devel}
%{?_enable_poppler:BuildPreReq: libpoppler-glib-devel >= %poppler_ver}
%{?_enable_libexif:BuildPreReq: libexif-devel >= %libexif_ver}
%{?_enable_libiptcdata:BuildPreReq: libiptcdata-devel}
%{?_enable_libgsf:BuildPreReq: libgsf-devel >= %libgfs_ver}
%{?_enable_libjpeg:BuildPreReq: libjpeg-devel}
%{?_enable_libtiff:BuildPreReq: libtiff-devel}
%{?_enable_libvorbis:BuildPreReq: libvorbis-devel >= %vorbis_ver}
%{?_enable_libvorbis:BuildPreReq: libflac-devel >= %flac_ver}
%{?_enable_exempi:BuildPreReq: libexempi-devel >= %exempi_ver}
%{?_enable_playlist:BuildPreReq: libtotem-pl-parser-devel}
%{?_enable_evolution:BuildPreReq: evolution-devel >= %evo_ver evolution-data-server-devel >= %eds_ver}
%{?_enable_nautilus_extension:BuildPreReq: libnautilus-devel}
%{?_enable_taglib:BuildPreReq: libtag-devel >= %taglib_ver}
%{?_enable_gtk_doc:BuildPreReq: gtk-doc docbook-utils graphviz dia}
%{?_enable_qt:BuildPreReq: libqt4-devel}
%{?_enable_libgif:BuildPreReq: libgif-devel}
%{?_enable_libcue:BuildPreReq: libcue-devel}
%{?_enable_libosinfo:BuildPreReq: libosinfo-devel >= %libosinfo_ver}

%description
Tracker is a powerful desktop-neutral first class object
database, tag/metadata database, search tool and indexer.

%package devel
Summary: Headers for developing programs that will use %name-miner
Group: Development/Other
Requires: %name = %version-%release
Obsoletes: lib%name-client-devel
License: LGPLv2.1+

%description devel
Tracker is a powerfull desktop-oriented search tool and indexer.
This package contains header files for development  and link applications with libtracker-miner.

%package devel-doc
Summary: Development documentation for %name
Group: Development/GNOME and GTK+
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
This package provides development documentation for %name.

%package -n lib%name-gir
Summary: GObject introspection data for the Tracker library
Group: System/Libraries
Requires: %name = %version-%release
Provides: typelib(Tracker) = %ver_major

%description -n lib%name-gir
GObject introspection data for the Tracker library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the Tracker library
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the Tracker library

%package -n gnome-applets-extra-%name
Summary: Tracker GNOME search applet
Group: Graphical desktop/GNOME
Requires: %name = %version-%release
Provides: %name-search-bar

%description -n gnome-applets-extra-%name
Tracker is a powerfull desktop-oriented search tool and indexer.
This package contains tracker GNOME search applet.

%package search-tool
Summary: Tracker search tool(s)
Group: Graphical desktop/GNOME
Requires: %name = %version-%release

%description search-tool
Graphical frontend to tracker search facilities.

%package explorer
Summary: Tracker explorer
Group: Graphical desktop/GNOME
Requires: %name = %version-%release

%description explorer
Graphical frontend for explorer to tracker search facilities.

%package utils
Summary: Commandline tools for Tracker
Group: Office
Requires: %name = %version-%release

%description utils
Included utilities for Tracker:
  * tracker-import: imports turtle file data into the database.
  * tracker-info: retrieve all information available for a certain file.
  * tracker-control: manage Tracker processes and data.
  * tracker-search: this perfoms a google like search using SEARCHTERM to
    retrieve all matching files where SEARCHTERM appears in any searchable
    metadata.
  * tracker-stats: retreive some statistics.
  * tracker-sparql: allows  the caller to run an RDF query on the database.
  * tracker-tag: tool to manage tags on files.

%package -n evolution-%name
Summary: Tracker plugin for Evolution
Group: Office
Requires: %name = %version-%release
Provides: %name-plugin-evolution = %version-%release
Obsoletes: %name-plugin-evolution

%description -n evolution-%name
Tracker is a powerfull desktop-oriented search tool and indexer.
This package contains plugin for Evolution.

%package -n nautilus-%name
Summary: Nautilus extension for managing tags
Group: Graphical desktop/GNOME
Requires: %name = %version-%release
Provides: %name-nautilus = %version-%release
Obsoletes: %name-nautilus

%description -n nautilus-%name
Nautilus extension for managing tags

%prep
%setup -q
%patch -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
	--disable-static \
	%{subst_enable introspection} \
	%{subst_enable hal} \
	%{subst_enable upower} \
	--with-unicode-support=%unicode_support \
	%{?_enable_network_manager:--enable-network-manager} \
	%{subst_enable libxml2} \
	%{subst_enable gdkpixbuf} \
	%{subst_enable qt} \
	%{subst_enable unac} \
	%{?_enable_gnome_keyring:--enable-gnome-keyring} \
	%{?_enable_flickr:--enable-miner-flickr} \
	%{?_enable_rss:--enable-miner-rss} \
	%{?_enable_evolition:--enable-miner-evolution} \
	%{?_enable_nautilus_extension:--enable-nautilus-extension} \
	%{subst_enable taglib} \
	%{?_enable_search_bar:--enable-tracker-search-bar} \
	%{?_enable_needle:--enable-tracker-needle} \
	%{?_enable_explorer:--enable-tracker-explorer} \
	%{?_enable_tracker_search_tool:--enable-tracker-search-tool} \
	%{?_enable_preferences:--enable-tracker-preferences} \
	%{subst_enable poppler} \
	%{subst_enable libexif} \
	%{subst_enable libiptcdata} \
	%{subst_enable libgsf} \
	%{subst_enable libjpeg} \
	%{subst_enable libtiff} \
	%{subst_enable libgif} \
	%{subst_enable libvorbis} \
	%{subst_enable libflac} \
	%{subst_enable exempi} \
	%{subst_enable playlist} \
	%{subst_enable libcue} \
	%{subst_enable libosinfo} \
	%{?_enable_gtk_doc:--enable-gtk-doc}

#	--enable-guarantee-metadata \

%make_build

%install
%make DESTDIR=%buildroot install

find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog COPYING NEWS README
%doc src/libtracker-common/COPYING.LIB
%config(noreplace) %_sysconfdir/xdg/autostart/*
%_datadir/glib-2.0/schemas/*
%dir %_libdir/%name-%ver_major
%_libdir/%name-%ver_major/*.so.*
%_libdir/%name-%ver_major/extract-modules
%_libdir/%name-%ver_major/writeback-modules

%_libexecdir/*

%_datadir/dbus-1/services/*.service
%_man1dir/tracker-miner-fs.1.gz

%dir %_datadir/%name
%_datadir/%name/*.xml
%_datadir/%name/languages
%_datadir/%name/miners
%_datadir/%name/ontologies
%_datadir/%name/extract-rules

%if_enabled flickr
%dir %_datadir/%name/icons
%_datadir/%name/icons/tracker-miner-flickr.svg
%endif

%_libdir/libtracker-extract*.so.*
%_libdir/libtracker-miner*.so.*
%_libdir/libtracker-sparql*.so.*

%_man1dir/tracker-extract.1.gz
%_man1dir/tracker-writeback.1.gz
%_man1dir/tracker-store.1.gz

%if_enabled search_bar
%exclude %_libexecdir/tracker-search-bar
%exclude %_datadir/%name/tracker-search-bar-menu.xml
%endif

%files utils
%_bindir/tracker-import
%_bindir/tracker-info
%_bindir/tracker-control
%_bindir/tracker-search
%_bindir/tracker-sparql
%_bindir/tracker-stats
%_bindir/tracker-tag
%_man1dir/tracker-import.1.gz
%_man1dir/tracker-info.1.gz
%_man1dir/tracker-control.1.gz
%_man1dir/tracker-search.1.gz
%_man1dir/tracker-sparql.1.gz
%_man1dir/tracker-stats.1.gz
%_man1dir/tracker-tag.1.gz

%files search-tool
%_bindir/tracker-preferences
%_bindir/tracker-needle
%_datadir/applications/*.desktop
%_datadir/icons/*/*/apps/tracker.*
%_datadir/%name/tracker-preferences.ui
%_datadir/%name/tracker-needle.ui
%_man1dir/tracker-preferences.1.gz
%_man1dir/tracker-needle.1.gz

%files explorer
%_bindir/tracker-explorer
%_datadir/%name/tracker-explorer.ui

%files devel
%_libdir/%name-%ver_major/*.so
%_includedir/%name-%ver_major
%_pkgconfigdir/*.pc
%_libdir/*.so
%_datadir/vala/vapi/*

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/*
# temporary delete radio-overview.png, dia have bug - generated image different size on i586 and x86_84
# %exclude %_datadir/gtk-doc/html/ontology/radio-overview.png
%endif

%if_enabled evolution
%files -n evolution-%name
%_libdir/evolution/*/plugins/*
%endif

%if_enabled search_bar
%files -n gnome-applets-extra-%name
%_libexecdir/tracker-search-bar
%_datadir/%name/tracker-search-bar-menu.xml
%_datadir/%name/tracker-search-bar.ui
%_datadir/gnome-panel/4.0/applets/org.gnome.panel.SearchBar.panel-applet
%_man1dir/tracker-search-bar.1.gz
%endif

%if_enabled nautilus_extension
%files -n nautilus-%name
%nautilus_extdir/libnautilus-tracker-tags.so
%endif

%if_enabled introspection
%files -n lib%name-gir
%_typelibdir/*.typelib

%files -n lib%name-gir-devel
%_girdir/*.gir
%endif

%changelog
* Wed May 23 2012 Alexey Shabalin <shaba@altlinux.ru> 0.14.1-alt1
- 0.14.1

* Thu Mar 15 2012 Alexey Shabalin <shaba@altlinux.ru> 0.14.0-alt1
- 0.14.0
- enable libosinfo support
- enable libcue support

* Wed Mar 07 2012 Alexey Shabalin <shaba@altlinux.ru> 0.12.10-alt1
- 0.12.10

* Wed Dec 21 2011 Alexey Shabalin <shaba@altlinux.ru> 0.12.9-alt1
- 0.12.9

* Mon Nov 28 2011 Alexey Shabalin <shaba@altlinux.ru> 0.12.8-alt1
- 0.12.8

* Thu Nov 10 2011 Alexey Shabalin <shaba@altlinux.ru> 0.12.7-alt2
- don't autostart services in KDE
- autostart services in LXDE

* Tue Nov 01 2011 Alexey Shabalin <shaba@altlinux.ru> 0.12.7-alt1
- 0.12.7

* Sun Oct 30 2011 Yuri N. Sedunov <aris@altlinux.org> 0.10.32-alt2
- rebuild against e-d-s-3.2.1

* Fri Oct 21 2011 Alexey Shabalin <shaba@altlinux.ru> 0.10.32-alt1
- 0.10.32

* Mon Oct 17 2011 Alexey Shabalin <shaba@altlinux.ru> 0.10.31-alt1
- 0.10.31

* Wed Oct 05 2011 Alexey Shabalin <shaba@altlinux.ru> 0.10.29-alt1
- 0.10.29
- disable build gtk-doc
- enable build search bar applet

* Mon Sep 19 2011 Alexey Shabalin <shaba@altlinux.ru> 0.10.27-alt1
- 0.10.27
- enable flickr support

* Tue Aug 30 2011 Alexey Shabalin <shaba@altlinux.ru> 0.10.23-alt1
- 0.10.23

* Tue Jul 12 2011 Alexey Shabalin <shaba@altlinux.ru> 0.10.19-alt1
- 0.10.19

* Fri May 27 2011 Alexey Shabalin <shaba@altlinux.ru> 0.10.15-alt1
- 0.10.15

* Tue May 24 2011 Alexey Shabalin <shaba@altlinux.ru> 0.10.14-alt1
- 0.10.14

* Fri Apr 29 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.18-alt1
- 0.8.18

* Wed Oct 06 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.17-alt1
- 0.8.17

* Sat Aug 21 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.16-alt1
- 0.8.16

* Wed Aug 11 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.15-alt2
- rebuild with poppler5

* Sun Jul 18 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.15-alt1
- 0.8.15

* Fri Jul 02 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.14-alt1
- 0.8.14

* Tue Jun 22 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.12-alt1
- 0.8.12

* Mon Jun 14 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.11-alt1
- 0.8.11

* Thu Jun 03 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.10-alt1
- 0.8.10

* Fri May 21 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.7-alt1
- 0.8.7

* Sat May 15 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.6-alt1
- 0.8.6

* Fri May 07 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.5-alt1
- 0.8.5

* Sat May 01 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.4-alt1
- 0.8.4

* Wed Apr 28 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.3-alt3
- rebuild with new evolution

* Mon Apr 26 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.3-alt2
- rebuild with new evolution
- rename tracker-plugin-evolution to  evolution-tracker
- rename tracker-nautilus to nautilus-tracker

* Sat Apr 24 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.3-alt1
- 0.8.3

* Fri Apr 16 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.2-alt1
- 0.8.2

* Fri Apr 02 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt1
- 0.8.0
- add vala files to devel package

* Fri Mar 26 2010 Alexey Shabalin <shaba@altlinux.ru> 0.7.28-alt1
- 0.7.28 + git snapshot  18b10a365e0fa736590dca83fccf4895ae7c8af5
- update buildreq and options for configure
- upstream drop deskbar-applet

* Fri Mar 12 2010 Alexey Shabalin <shaba@altlinux.ru> 0.7.25-alt1
- 0.7.25
- git snapshot f39f413f86c4c6ae155e2a5ba70c2ce143b337c9

* Fri Mar 05 2010 Alexey Shabalin <shaba@altlinux.ru> 0.7.24-alt1
- 0.7.24

* Sat Feb 27 2010 Alexey Shabalin <shaba@altlinux.ru> 0.7.23-alt1
- 0.7.23

* Wed Feb 24 2010 Alexey Shabalin <shaba@altlinux.ru> 0.7.21-alt2.git96052c
- git snapshot 96052c98be58df5e0c4f609953d42e15af6908d9

* Mon Feb 22 2010 Alexey Shabalin <shaba@altlinux.ru> 0.7.21-alt1
- 0.7.21

* Fri Feb 12 2010 Alexey Shabalin <shaba@altlinux.ru> 0.7.20-alt1
- 0.7.20
- upstream fixed *.pc files; drop alt fix-pkgconfig patch
- upstream drop libtracker-gtk

* Tue Feb 09 2010 Alexey Shabalin <shaba@altlinux.ru> 0.7.19-alt2
- split libtracker to libtracker-client. 
- move libtracker-extract,libtracker-miner to main tracker package.

* Mon Feb 08 2010 Alexey Shabalin <shaba@altlinux.ru> 0.7.19-alt1
- 0.7.19
- build with flac support
- move gtk-doc files to devel-doc package
- merge libtracker-client and other libs to libtracker package, exclude libtracker-gtk
- merge all devel files to tracker-devel package, exclude libtracker-gtk-devel

* Fri Jan 15 2010 Alexey Shabalin <shaba@altlinux.ru> 0.7.16-alt1
- 0.7.16

* Tue Jan 12 2010 Alexey Shabalin <shaba@altlinux.ru> 0.7.15-alt1
- 0.7.15

* Tue Dec 29 2009 Alexey Shabalin <shaba@altlinux.ru> 0.7.14-alt1
- 0.7.14

* Thu Dec 24 2009 Alexey Shabalin <shaba@altlinux.ru> 0.7.13-alt1
- 0.7.13

* Sat Dec 19 2009 Alexey Shabalin <shaba@altlinux.ru> 0.7.12-alt1
- 0.7.12
- build with wv2
- package nautilus extension

* Sun Dec 13 2009 Alexey Shabalin <shaba@altlinux.ru> 0.7.11-alt1
- 0.7.11
- disable HAL support for AC power detection (use DeviceKit-power)

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.8-alt1.1
- Rebuilt with python 2.6

* Sat Nov 21 2009 Alexey Shabalin <shaba@altlinux.ru> 0.7.8-alt1
- 0.7.8

* Sat Nov 14 2009 Alexey Shabalin <shaba@altlinux.ru> 0.7.7-alt1
- 0.7.7

* Fri Nov 06 2009 Alexey Shabalin <shaba@altlinux.ru> 0.7.6-alt1
- 0.7.6

* Thu Oct 29 2009 Alexey Shabalin <shaba@altlinux.ru> 0.7.4-alt1
- 0.7.4

* Fri Oct 09 2009 Alexey Shabalin <shaba@altlinux.ru> 0.7.2-alt1
- 0.7.2

* Fri Oct 02 2009 Alexey Shabalin <shaba@altlinux.ru> 0.7.1-alt1
- 0.7.1

* Tue Sep 29 2009 Alexey Shabalin <shaba@altlinux.ru> 0.7.0-alt1
- 0.7.0
- revoke from orphaned
- rewrite spec

* Tue Oct 07 2008 Alex Karpov <karpov@altlinux.ru> 0.6.6-alt1.3
- removed gnome-libs-devel from build requirements
    + spec cleanup

* Mon May 26 2008 Alex Karpov <karpov@altlinux.ru> 0.6.6-alt1.2
- rebuild with new gstreamer

* Mon Apr 07 2008 Alex Karpov <karpov@altlinux.ru> 0.6.6-alt1.1
- added update_menus

* Wed Mar 19 2008 Alex Karpov <karpov@altlinux.ru> 0.6.6-alt1
- 0.6.6 

* Tue Jan 29 2008 Alex Karpov <karpov@altlinux.ru> 0.6.4-alt1.1
- updated %files section for correct libtracker-devel content

* Tue Dec 11 2007 Alex Karpov <karpov@altlinux.ru> 0.6.4-alt1
- 0.6.4

* Sat Oct 13 2007 Alex Karpov <karpov@altlinux.ru> 0.6.3-alt1.1
- rebuild with poppler-0.6

* Wed Sep 26 2007 Alex Karpov <karpov@altlinux.ru> 0.6.3-alt1
- 0.6.3 

* Wed Sep 05 2007 Alex Karpov <karpov@altlinux.ru> 0.6.2-alt1
- 0.6.2

* Wed Sep 05 2007 Alex Karpov <karpov@altlinux.ru> 0.6.1-alt1
- new version

* Tue Jul 31 2007 Alex Karpov <karpov@altlinux.ru> 0.6.0-alt0.1
- initial build

