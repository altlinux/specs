%define ver_major 2.0
%define api_ver 2.0

# since 1.0.3 (see https://bugzilla.gnome.org/show_bug.cgi?id=733857)
%set_verify_elf_method unresolved=relaxed

%def_without bootstrap
%def_enable introspection
%def_enable upower
%def_enable network_manager
%def_enable gtk_doc

# Unicode support library? (libunistring|libicu)
%define unicode_support libicu

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
Obsoletes: %name-search-tool < 1.99.0
Obsoletes: nautilus-%name < 1.99.0

Requires: lib%name = %version-%release
%{?_without_bootstrap:Requires: %name-miners >= %ver_major}

%define dbus_ver 1.3.1
%define glib_ver 2.44.0
%define pango_ver 1.0.0
%define gtk_ver 3.0.0
%define upower_ver 0.9.0
%define nm_ver 0.8
%define gst_ver 1.0
%define sqlite_ver 3.20.1-alt2
%define soup_ver 2.40.0
%define gupnp_dlna_ver 0.9.4

Requires: libsqlite3 >= %sqlite_ver

BuildPreReq: gcc-c++ gnome-common rpm-build-gnome
BuildPreReq: gtk-doc docbook-utils python3
BuildPreReq: libxml2-devel
BuildPreReq: libdbus-devel >= %dbus_ver
BuildPreReq: libgio-devel >= %glib_ver
BuildPreReq: libicu-devel libunistring-devel
BuildPreReq: libpango-devel >= %pango_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildRequires: libsoup-devel >= %soup_ver libjson-glib-devel
%{?_enable_introspection:BuildPreReq: gobject-introspection-devel >= 0.9.5}
%{?_enable_upower:BuildPreReq: libupower-devel >= %upower_ver}
%{?_enable_network_manager:BuildPreReq: NetworkManager-glib-devel >= %nm_ver libnm-devel}
BuildRequires: libstemmer-devel

BuildPreReq: libuuid-devel
BuildPreReq: vala >= 0.18.0
BuildPreReq: intltool >= 0.35.0
BuildPreReq: sqlite3 libsqlite3-devel >= %sqlite_ver
BuildRequires: gstreamer1.0-devel >= %gst_ver gst-plugins1.0-devel >= %gst_ver
BuildRequires: libgupnp-dlna-devel >= %gupnp_dlna_ver
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
Provides: gir(Tracker) = 2.0

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

%prep
%setup

%build
%autoreconf
%configure \
	--disable-static \
	%{subst_enable introspection} \
	%{subst_enable upower} \
	--with-unicode-support=%unicode_support \
	%{?_enable_network_manager:--enable-network-manager} \
	%{subst_enable unac} \
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
%dir %_libdir/%name-%api_ver
%_libexecdir/tracker-store
%_datadir/dbus-1/services/*.service
%dir %_datadir/%name
%_datadir/%name/*.xml
%_datadir/%name/stop-words/
%_datadir/%name/ontologies/
%_datadir/%name/domain-ontologies/
%_prefix/lib/systemd/user/tracker-store.service
%_man1dir/tracker-store.*

%exclude %_datadir/bash-completion/completions/%name

%files -n lib%name
%_libdir/*.so.*
%_libdir/%name-%api_ver/*.so.*

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

%files devel
%_libdir/%name-%api_ver/*.so
%_includedir/%name-%api_ver/
%_pkgconfigdir/*.pc
%_libdir/*.so
%_datadir/vala/vapi/*

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/*
%endif

%if_enabled introspection
%files -n lib%name-gir
%_typelibdir/Tracker-%api_ver.typelib
%_typelibdir/TrackerControl-%api_ver.typelib
%_typelibdir/TrackerMiner-%api_ver.typelib

%files -n lib%name-gir-devel
%_girdir/Tracker-%api_ver.gir
%_girdir/TrackerControl-%api_ver.gir
%_girdir/TrackerMiner-%api_ver.gir
%endif


%changelog
* Wed Feb 07 2018 Yuri N. Sedunov <aris@altlinux.org> 2.0.3-alt1
- 2.0.3

* Thu Jan 04 2018 Yuri N. Sedunov <aris@altlinux.org> 2.0.2-alt2
- rebuilt against libicu*.so.60

* Wed Nov 15 2017 Yuri N. Sedunov <aris@altlinux.org> 2.0.2-alt1
- 2.0.2

* Wed Oct 04 2017 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt1
- 2.0.1

* Sun Sep 17 2017 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt2
- requires tracker-miners

* Tue Sep 12 2017 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1
- 2.0.0

* Tue Aug 22 2017 Yuri N. Sedunov <aris@altlinux.org> 1.99.3-alt1
- 1.99.3

* Tue Aug 22 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.3-alt1
- 1.12.3

* Mon Aug 07 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.2-alt1
- 1.12.2

* Thu Jun 29 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.1-alt1
- 1.12.1

* Mon Mar 20 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.0-alt1
- 1.12.0

* Thu Feb 23 2017 Yuri N. Sedunov <aris@altlinux.org> 1.10.5-alt1
- 1.10.5

* Thu Jan 19 2017 Yuri N. Sedunov <aris@altlinux.org> 1.10.4-alt1
- 1.10.4

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

