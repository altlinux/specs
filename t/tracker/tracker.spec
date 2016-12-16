%define ver_major 1.10
%define ver_api 1.0

# since 1.0.3 (see https://bugzilla.gnome.org/show_bug.cgi?id=733857)
%set_verify_elf_method unresolved=relaxed

%def_enable introspection
%def_disable hal
%def_enable upower
%def_enable libxml2
%def_enable network_manager
%def_enable libmediaart
%def_disable evolution
%def_enable rss
%def_enable preferences
%def_enable poppler
%def_enable libgxps
%def_enable libexif
%def_enable libiptcdata
%def_enable libgsf
%def_enable libjpeg
%def_enable libtiff
%def_enable libpng
%def_enable libvorbis
%def_enable libflac
%def_enable exempi
%def_enable nautilus_extension
%def_enable gtk_doc
%def_enable taglib
%def_enable needle
%def_enable libgif
%def_enable libcue
%def_enable abiword
%def_enable dvi
%def_enable mp3
%def_enable ps
%def_enable text
%def_enable icon
%def_enable artwork
%def_enable libosinfo
%def_enable playlist

# Unicode support library? (libunistring|libicu)
%define unicode_support libicu

# mediaextractor (gstreamer|libav|mplayer|external)
%define generic_media_extractor gstreamer

%define _libexecdir %_prefix/libexec

Name: tracker
Version: %ver_major.3
Release: alt1

Summary: Tracker is a powerfull desktop-oriented search tool and indexer
License: GPLv2+
Group: Office
Url: http://wiki.gnome.org/Projects/Tracker

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

Obsoletes: lib%name-client
Requires: lib%name = %version-%release

%define dbus_ver 1.3.1
%define glib_ver 2.40.0
%define pango_ver 1.0.0
%define gtk_ver 3.0.0
%define libxml2_ver 2.6
%define hal_ver 0.5
%define upower_ver 0.9.0
%define poppler_ver 0.16.0
%define cairo_ver 1.0
%define gdk_ver 1.0
%define vorbis_ver 0.22
%define flac_ver 1.2.1
%define libexif_ver 0.6
%define libgsf_ver 1.14.24
%define exempi_ver 2.1.0
%define evo_ver 2.32.0
%define eds_ver 2.32.0
%define gee_ver 0.3
%define taglib_ver 1.6
%define libgrss_ver 0.7
%define rest_ver 0.7
%define nm_ver 0.8
%define gst_ver 0.10.31
%define gupnp_dlna_ver 0.9.4
%define libosinfo_ver 0.2.9
%define libpng_ver 0.89
%define libmediaart_ver 1.9
%define sqlite_ver 3.11.0

BuildPreReq: gcc-c++ gnome-common rpm-build-gnome gtk-doc docbook-utils
BuildPreReq: glibc-devel
BuildPreReq: libdbus-devel >= %dbus_ver
BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: libgio-devel >= %glib_ver
%{?_enable_libmediaart:BuildPreReq: libmediaart2.0-devel >= %libmediaart_ver}
BuildPreReq: libicu-devel libunistring-devel
BuildPreReq: libpango-devel >= %pango_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
%{?_enable_introspection:BuildPreReq: gobject-introspection-devel >= 0.9.5}
%{?_enable_hal:BuildPreReq: libhal-devel >= %hal_ver}
%{?_enable_upower:BuildPreReq: libupower-devel >= %upower_ver}
%{?_enable_network_manager:BuildPreReq: NetworkManager-glib-devel >= %nm_ver}
%{?_enable_libxml2:BuildPreReq: libxml2-devel >= %libxml2_ver}
%{?_enable_libpng:BuildPreReq: libpng-devel >= %libpng_ver}
BuildPreReq: libuuid-devel
BuildPreReq: libenca-devel >= 1.9
BuildPreReq: vala >= 0.18.0
BuildPreReq: intltool >= 0.35.0
BuildPreReq: sqlite3 libsqlite3-devel >= %sqlite_ver
BuildRequires: gstreamer1.0-devel >= %gst_ver gst-plugins1.0-devel >= %gst_ver
BuildRequires: libgupnp-dlna-devel >= %gupnp_dlna_ver
BuildRequires: libavformat-devel >= 0.8.4 libavcodec-devel >= 0.8.4  libavutil-devel >= 0.8.4
%{?_enable_rss:BuildPreReq: libgrss-devel >= %libgrss_ver}
BuildPreReq: libgee0.8-devel >= %gee_ver
%{?_enable_poppler:BuildPreReq: libpoppler-glib-devel >= %poppler_ver}
%{?_enable_libgxps:BuildPreReq: libgxps-devel}
%{?_enable_libexif:BuildPreReq: libexif-devel >= %libexif_ver}
%{?_enable_libiptcdata:BuildPreReq: libiptcdata-devel}
%{?_enable_libgsf:BuildPreReq: libgsf-devel >= %libgsf_ver}
%{?_enable_libjpeg:BuildPreReq: libjpeg-devel}
%{?_enable_libtiff:BuildPreReq: libtiff-devel}
%{?_enable_libvorbis:BuildPreReq: libvorbis-devel >= %vorbis_ver}
%{?_enable_libvorbis:BuildPreReq: libflac-devel >= %flac_ver}
%{?_enable_exempi:BuildPreReq: libexempi-devel >= %exempi_ver}
%{?_enable_evolution:BuildPreReq: evolution-devel >= %evo_ver evolution-data-server-devel >= %eds_ver}
%{?_enable_nautilus_extension:BuildPreReq: libnautilus-devel}
%{?_enable_taglib:BuildPreReq: libtag-devel >= %taglib_ver}
%{?_enable_gtk_doc:BuildPreReq: gtk-doc docbook-utils graphviz}
%{?_enable_libgif:BuildPreReq: libgif-devel}
%{?_enable_libcue:BuildPreReq: libcue-devel}
%{?_enable_libosinfo:BuildPreReq: libosinfo-devel >= %libosinfo_ver}
%{?_enable_playlist:BuildPreReq: libtotem-pl-parser-devel}
BuildRequires: systemd-devel libseccomp-devel

%description
Tracker is a powerful desktop-neutral first class object
database, tag/metadata database, search tool and indexer.

%package devel
Summary: Headers for developing programs that will use %name-miner
Group: Development/Other
Requires: lib%name = %version-%release
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

%package -n lib%name
Summary: Tracker shared libraries
Group: System/Libraries
Conflicts: %name < %version-%release

%description -n lib%name
This package contains shred Tracker libraries for applications.

%package -n lib%name-gir
Summary: GObject introspection data for the Tracker library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the Tracker library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the Tracker library
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the Tracker library

%package search-tool
Summary: Tracker search tool(s)
Group: Graphical desktop/GNOME
Requires: %name = %version-%release

%description search-tool
Graphical frontend to tracker search facilities.

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
%setup

%build
%autoreconf
%configure \
	--disable-static \
	%{subst_enable introspection} \
	%{subst_enable hal} \
	%{subst_enable upower} \
	--with-unicode-support=%unicode_support \
	--enable-generic-media-extractor=%generic_media_extractor \
	%{?_enable_network_manager:--enable-network-manager} \
	%{subst_enable libxml2} \
	%{subst_enable unac} \
	%{?_enable_rss:--enable-miner-rss} \
	%{?_enable_evolition:--enable-miner-evolution} \
	%{?_enable_nautilus_extension:--enable-nautilus-extension} \
	%{subst_enable taglib} \
	%{?_enable_needle:--enable-tracker-needle} \
	%{?_enable_preferences:--enable-tracker-preferences} \
	%{subst_enable poppler} \
	%{subst_enable libgxps} \
	%{subst_enable libexif} \
	%{subst_enable libiptcdata} \
	%{subst_enable libgsf} \
	%{subst_enable libjpeg} \
	%{subst_enable libtiff} \
	%{subst_enable libgif} \
	%{subst_enable libpng} \
	%{subst_enable libvorbis} \
	%{subst_enable libflac} \
	%{subst_enable exempi} \
	%{subst_enable libcue} \
	%{subst_enable abiword} \
	%{subst_enable dvi} \
	%{subst_enable mp3} \
	%{subst_enable ps} \
	%{subst_enable text} \
	%{subst_enable icon} \
	%{subst_enable artwork} \
	%{subst_enable libosinfo} \
	%{subst_enable playlist} \
	%{?_enable_gtk_doc:--enable-gtk-doc}

#	--enable-guarantee-metadata \

%make_build

%install
%makeinstall_std

find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%find_lang %name
rm -rf %buildroot%_datadir/tracker-tests

%files -f %name.lang
%doc AUTHORS ChangeLog COPYING NEWS README
%doc src/libtracker-common/COPYING.LIB
%config(noreplace) %_sysconfdir/xdg/autostart/*
%_datadir/glib-2.0/schemas/*
%dir %_libdir/%name-%ver_api
%_libdir/%name-%ver_api/extract-modules
%_libdir/%name-%ver_api/writeback-modules

%_libexecdir/tracker-extract
%_libexecdir/tracker-miner-fs
%_libexecdir/tracker-store
%_libexecdir/tracker-writeback
%_libexecdir/tracker-miner-apps
%_libexecdir/tracker-miner-user-guides
%{?_enable_rss:%_libexecdir/%name-miner-rss}

%_datadir/dbus-1/services/*.service
%_man1dir/tracker-miner-fs.*
%{?_enable_rss:%_man1dir/%name-miner-rss.1.*}

%dir %_datadir/%name
%_datadir/%name/*.xml
%_datadir/%name/stop-words/
%_datadir/%name/miners/
%_datadir/%name/ontologies/
%_datadir/%name/extract-rules/
%_prefix/lib/systemd/user/tracker-extract.service
%_prefix/lib/systemd/user/tracker-miner-apps.service
%_prefix/lib/systemd/user/tracker-miner-fs.service
%_prefix/lib/systemd/user/tracker-miner-rss.service
%_prefix/lib/systemd/user/tracker-miner-user-guides.service
%_prefix/lib/systemd/user/tracker-store.service
%_prefix/lib/systemd/user/tracker-writeback.service

%_man1dir/tracker-extract.*
%_man1dir/tracker-store.*
%_man1dir/tracker-writeback.*

%exclude %_datadir/bash-completion/completions/%name

%files -n lib%name
%_libdir/*.so.*
%_libdir/%name-%ver_api/*.so.*

%files utils
%_bindir/%name
%_man1dir/tracker-info.*
%_man1dir/tracker-search.*
%_man1dir/tracker-sparql.*
%_man1dir/tracker-tag.*
%_man1dir/tracker-daemon.*
%_man1dir/tracker-index.*
%_man1dir/tracker-reset.*
%_man1dir/tracker-sql.*
%_man1dir/tracker-status.*

%files search-tool
%_bindir/tracker-preferences
%_bindir/tracker-needle
%_datadir/applications/*.desktop
%_datadir/icons/*/*/apps/tracker.*
%_datadir/%name/tracker-preferences.ui
%_datadir/%name/tracker-needle.ui
%_datadir/appdata/tracker-needle.appdata.xml
%_datadir/appdata/tracker-preferences.appdata.xml
%_man1dir/tracker-preferences.*
%_man1dir/tracker-needle.*

%files devel
%_libdir/%name-%ver_api/*.so
%_includedir/%name-%ver_api
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
* Fri Dec 16 2016 Yuri N. Sedunov <aris@altlinux.org> 1.10.3-alt1
- 1.10.3

* Thu Dec 08 2016 Yuri N. Sedunov <aris@altlinux.org> 1.10.2-alt1
- 1.10.2

* Fri Oct 14 2016 Yuri N. Sedunov <aris@altlinux.org> 1.10.1-alt1
- 1.10.1

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 1.10.0-alt1
- 1.10.0

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- 1.8.0

* Tue Mar 01 2016 Yuri N. Sedunov <aris@altlinux.org> 1.6.2-alt1
- 1.6.2

* Tue Feb 09 2016 Yuri N. Sedunov <aris@altlinux.org> 1.6.1-alt2
- rebuild against libicu*.so.56

* Thu Nov 26 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.1-alt1
- 1.6.1

* Tue Sep 22 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Fri Jul 31 2015 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt1
- 1.4.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Wed Dec 10 2014 Yuri N. Sedunov <aris@altlinux.org> 1.2.5-alt1
- 1.2.5

* Thu Nov 06 2014 Yuri N. Sedunov <aris@altlinux.org> 1.2.4-alt1
- 1.2.4

* Fri Oct 17 2014 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt1
- 1.2.3

* Wed Oct 15 2014 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt2
- rebuilt against libupower-glib.so.3

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt1
- 1.2.2

* Tue Sep 02 2014 Yuri N. Sedunov <aris@altlinux.org> 1.0.4-alt1
- 1.0.4

* Wed Aug 27 2014 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt1
- 1.0.3

* Mon Jul 28 2014 Alexey Shabalin <shaba@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Mon May 12 2014 Alexey Shabalin <shaba@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Tue Mar 25 2014 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Wed Feb 19 2014 Alexey Shabalin <shaba@altlinux.ru> 0.17.2-alt1
- 0.17.2

* Wed Dec 11 2013 Alexey Shabalin <shaba@altlinux.ru> 0.16.4-alt1
- 0.16.4

* Thu Nov 07 2013 Alexey Shabalin <shaba@altlinux.ru> 0.16.3-alt1
- 0.16.3
- enable playlist support

* Tue Oct 01 2013 Alexey Shabalin <shaba@altlinux.ru> 0.16.2-alt2
- upstream snapshot of branch tracker-0.16

* Wed Aug 07 2013 Alexey Shabalin <shaba@altlinux.ru> 0.16.2-alt1
- 0.16.2

* Tue May 28 2013 Alexey Shabalin <shaba@altlinux.ru> 0.16.1-alt4
- move libtracker-common.so.0 and libtracker-data.so.0 to libtracker too

* Tue May 28 2013 Alexey Shabalin <shaba@altlinux.ru> 0.16.1-alt3
- move shared libraries to libtracker

* Tue May 28 2013 Alexey Shabalin <shaba@altlinux.ru> 0.16.1-alt2
- update hu,ru,pl translations

* Mon May 06 2013 Alexey Shabalin <shaba@altlinux.ru> 0.16.1-alt1
- 0.16.1

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.16.0-alt1.qa1
- NMU: rebuilt with libarchive.so.13.

* Tue Mar 19 2013 Alexey Shabalin <shaba@altlinux.ru> 0.16.0-alt1
- 0.16.0
- upstream deleted search_bar, flickr, playlist support

* Wed Mar 13 2013 Alexey Shabalin <shaba@altlinux.ru> 0.15.4-alt1
- 0.15.4

* Mon Feb 25 2013 Alexey Shabalin <shaba@altlinux.ru> 0.15.2-alt1
- 0.15.2

* Mon Jan 28 2013 Alexey Shabalin <shaba@altlinux.ru> 0.15.1-alt1
- 0.15.1

* Thu Nov 15 2012 Alexey Shabalin <shaba@altlinux.ru> 0.14.4-alt1.1
- rebuild with libicu-5.1

* Fri Nov 02 2012 Alexey Shabalin <shaba@altlinux.ru> 0.14.4-alt1
- 0.14.4

* Wed Oct 31 2012 Alexey Shabalin <shaba@altlinux.ru> 0.14.3-alt1
- 0.14.3

* Tue Oct 02 2012 Alexey Shabalin <shaba@altlinux.ru> 0.14.2-alt2
- disable evolution plugin

* Mon Jul 30 2012 Alexey Shabalin <shaba@altlinux.ru> 0.14.2-alt1
- 0.14.2

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

