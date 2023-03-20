%def_disable snapshot
%define _name tracker
%define ver_major 3.5
%define beta %nil
%define api_ver_major 3
%define api_ver %{api_ver_major}.0
%define gst_api_ver 1.0

# since 1.0.3 (see https://bugzilla.gnome.org/show_bug.cgi?id=733857)
%set_verify_elf_method unresolved=relaxed

%def_with bootstrap
%def_enable introspection
%def_enable upower
%def_enable stemmer
%def_enable soup2
%def_enable soup3
%def_enable docs
%def_enable man
%def_enable test_utils

# Unicode support library? (unistring|icu)
%define unicode_support icu

%define _libexecdir %_prefix/libexec

Name: %_name%api_ver_major
Version: %ver_major.0
Release: alt1%beta

Summary: Tracker is a powerfull desktop-oriented search tool and indexer
License: GPL-2.0 and LGPL-2.1-or-later
Group: Office
Url: http://wiki.gnome.org/Projects/Tracker

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version%beta.tar.xz
%else
Source: %_name-%version%beta.tar
%endif

Requires: lib%name = %EVR
Requires: dconf
%{?_without_bootstrap:Requires: %_name-miners%api_ver_major >= %ver_major}

%define dbus_ver 1.3.1
%define glib_ver 2.52.0
%define pango_ver 1.0.0
%define gtk_ver 3.0.0
%define upower_ver 0.9.0
%define gst_ver 1.0
%define sqlite_ver 3.20.1-alt2
%define soup_ver 2.40.0
%define soup3_ver 2.99.2
%define gupnp_dlna_ver 0.9.4

Requires: libsqlite3 >= %sqlite_ver

BuildRequires(pre): rpm-macros-meson rpm-build-vala rpm-build-gnome rpm-build-gir rpm-build-systemd
%{?_enable_test_utils:
BuildRequires(pre): rpm-build-python3 python3-module-pygobject3
%add_python3_path %_libdir/%_name-%api_ver/trackertestutils
}
BuildRequires: /proc meson gcc-c++
BuildRequires: libxml2-devel libicu-devel libuuid-devel
BuildRequires: libdbus-devel >= %dbus_ver
BuildRequires: libgio-devel >= %glib_ver libpango-devel >= %pango_ver libgtk+3-devel >= %gtk_ver
%{?_enable_soup2:BuildRequires: libsoup-devel >= %soup_ver}
%{?_enable_soup3:BuildRequires: libsoup3.0-devel >= %soup3_ver}
BuildRequires: libjson-glib-devel
BuildRequires: gobject-introspection-devel
%{?_enable_upower:BuildRequires: libupower-devel >= %upower_ver}
%{?_enable_stemmer:BuildRequires: libstemmer-devel}
%{?_enable_docs:BuildRequires: gi-docgen}
%{?_enable_man:BuildRequires: asciidoc-a2x xsltproc}
BuildRequires: vala-tools
BuildRequires: sqlite3 libsqlite3-devel >= %sqlite_ver
BuildRequires: gstreamer%gst_api_ver-devel >= %gst_ver gst-plugins%gst_api_ver-devel >= %gst_ver
BuildRequires: libgupnp-dlna-devel >= %gupnp_dlna_ver
BuildRequires: pkgconfig(systemd) libseccomp-devel
BuildRequires: bash-completion

%description
Tracker is a powerful desktop-neutral first class object
database, tag/metadata database, search tool and indexer.

%package devel
Summary: Headers for developing programs that will use %name-miner
Group: Development/Other
Requires: lib%name = %EVR
Requires: %name = %EVR
Obsoletes: lib%name-client-devel
License: LGPL-2.1

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
Requires: lib%name = %EVR

%description -n lib%name-gir
GObject introspection data for the Tracker library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the Tracker library
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %EVR
Provides: gir(Tracker) = %api_ver

%description -n lib%name-gir-devel
GObject introspection devel data for the Tracker library

%package tests
Summary: Tests for Tracker search tool
Group: Development/Other
Requires: %name = %EVR
Provides: tracker-sandbox %name-sandbox

%description tests
This package provides tests programs that can be used to verify
the functionality of the installed Tracker.

%prep
%setup -n %_name-%version%beta
#fixed install_rpath for tracker, tracker-store binaries
sed -i 's/tracker_install_rpath/tracker_internal_libs_dir/' src/*/meson.build

%build
%meson \
	%{?_disable_soup3:-Dsoup='soup2'} \
	-Dunicode_support=%unicode_support \
	%{?_enable_stemmer:-Dstemmer=enabled} \
	%{?_disable_docs:-Ddocs=false} \
	%{?_disable_man:-Dman=false} \
	%{?_disable_test_utils:-Dtest_utils=false} \
	-Dtest_utils_dir='%_libdir/%_name-%api_ver'
%nil
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%_bindir/%name
%dir %_libdir/%_name-%api_ver
%_libexecdir/*
%dir %_datadir/%name
%_datadir/%name/stop-words/
%_datadir/%name/ontologies/
%_datadir/bash-completion/completions/%name
%_userunitdir/%_name-xdg-portal-%api_ver_major.service
%_datadir/dbus-1/services/org.freedesktop.portal.Tracker.service
%if_enabled man
%_man1dir/%_name-xdg-portal*
%_man1dir/%name-endpoint.*
%_man1dir/%name-export.*
%_man1dir/%name-import.*
%_man1dir/%name-sparql.*
%_man1dir/%name-sql.*
%endif
%doc AUTHORS NEWS README*

%files -n lib%name
%_libdir/*.so.*
%_libdir/%_name-%api_ver/lib%_name-parser-libicu.so
%{?_enable_soup2:%_libdir/%_name-%api_ver/lib%_name-http-soup2.so}
%{?_enable_soup3:%_libdir/%_name-%api_ver/lib%_name-http-soup3.so}

%files devel
%_includedir/%_name-%api_ver/
%_pkgconfigdir/*.pc
%_libdir/*.so
%_vapidir/*

%if_enabled docs
%files devel-doc
%_datadir/doc/Tracker-%api_ver
%endif

%if_enabled introspection
%files -n lib%name-gir
%_typelibdir/Tracker-%api_ver.typelib

%files -n lib%name-gir-devel
%_girdir/Tracker-%api_ver.gir
%endif

%if_enabled test_utils
%files tests
%_libdir/%_name-%api_ver/trackertestutils/
%endif

%changelog
* Mon Mar 20 2023 Yuri N. Sedunov <aris@altlinux.org> 3.5.0-alt1
- 3.5.0

* Mon Dec 05 2022 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Wed Oct 26 2022 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Wed Sep 21 2022 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon Sep 05 2022 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt0.9.rc
- 3.4.0.rc
- enabled libsoup-3.0 support

* Tue Aug 09 2022 Yuri N. Sedunov <aris@altlinux.org> 3.3.3-alt1
- 3.3.3

* Wed Jul 06 2022 Yuri N. Sedunov <aris@altlinux.org> 3.3.2-alt1
- 3.3.2

* Thu Jun 30 2022 Yuri N. Sedunov <aris@altlinux.org> 3.3.1-alt1.1
- temporarily disabled libsoup-3.0 support

* Wed Jun 01 2022 Yuri N. Sedunov <aris@altlinux.org> 3.3.1-alt1
- 3.3.1

* Sun Mar 20 2022 Yuri N. Sedunov <aris@altlinux.org> 3.3.0-alt1
- 3.3.0

* Sun Oct 31 2021 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Sat Sep 18 2021 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Sat Jun 12 2021 Yuri N. Sedunov <aris@altlinux.org> 3.1.2-alt1
- 3.1.2

* Fri Apr 09 2021 Yuri N. Sedunov <aris@altlinux.org> 3.1.1-alt1
- 3.1.1

* Sun Mar 21 2021 Yuri N. Sedunov <aris@altlinux.org> 3.1.0-alt1
- 3.1.0

* Mon Mar 15 2021 Yuri N. Sedunov <aris@altlinux.org> 3.1.0-alt0.8.rc
- 3.1.0.rc

* Mon Jan 11 2021 Yuri N. Sedunov <aris@altlinux.org> 3.0.3-alt1
- 3.0.3

* Wed Dec 09 2020 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Fri Oct 02 2020 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Mon Sep 14 2020 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Mon Sep 07 2020 Yuri N. Sedunov <aris@altlinux.org> 2.99.5-alt1
- 2.99.5

* Sat Jun 27 2020 Yuri N. Sedunov <aris@altlinux.org> 2.99.2-alt1
- 2.99.2

* Sun May 03 2020 Yuri N. Sedunov <aris@altlinux.org> 2.99.1-alt1
- 2.99.1

* Tue Mar 10 2020 Yuri N. Sedunov <aris@altlinux.org> 2.3.4-alt1
- 2.3.4

* Tue Mar 03 2020 Yuri N. Sedunov <aris@altlinux.org> 2.3.2-alt1
- 2.3.2

* Sat Oct 12 2019 Yuri N. Sedunov <aris@altlinux.org> 2.3.1-alt1
- 2.3.1

* Mon Sep 23 2019 Yuri N. Sedunov <aris@altlinux.org> 2.3.0-alt2
- rebuilt without bootstrap

* Tue Sep 10 2019 Yuri N. Sedunov <aris@altlinux.org> 2.3.0-alt1
- 2.3.0

* Fri May 03 2019 Yuri N. Sedunov <aris@altlinux.org> 2.2.2-alt1
- 2.2.2

* Sat Mar 16 2019 Yuri N. Sedunov <aris@altlinux.org> 2.2.1-alt1.1
- rebuilt without bootstrap

* Wed Mar 06 2019 Yuri N. Sedunov <aris@altlinux.org> 2.2.1-alt1
- 2.2.1

* Thu Feb 21 2019 Yuri N. Sedunov <aris@altlinux.org> 2.1.8-alt1
- 2.1.8

* Wed Feb 06 2019 Yuri N. Sedunov <aris@altlinux.org> 2.1.7-alt1
- 2.1.7

* Thu Jan 24 2019 Yuri N. Sedunov <aris@altlinux.org> 2.1.6-alt2.2
- disabled bootstrap again after rebuild tracker-miners against libexempi.so.8

* Thu Jan 24 2019 Yuri N. Sedunov <aris@altlinux.org> 2.1.6-alt2.1
- enabled bootstrap to rebuild tracker-miners against libexempi.so.8

* Thu Dec 20 2018 Yuri N. Sedunov <aris@altlinux.org> 2.1.6-alt2
- fixed buildreqs for network-manager support

* Fri Nov 09 2018 Yuri N. Sedunov <aris@altlinux.org> 2.1.6-alt1
- updated to 2.1.6-3-gb44919518

* Wed Sep 26 2018 Yuri N. Sedunov <aris@altlinux.org> 2.1.5-alt1
- 2.1.5

* Tue Sep 18 2018 Yuri N. Sedunov <aris@altlinux.org> 2.1.4-alt2
- rebuilt without bootstrap (ALT #35408)

* Tue Sep 04 2018 Yuri N. Sedunov <aris@altlinux.org> 2.1.4-alt1
- 2.1.4

* Wed Jul 25 2018 Yuri N. Sedunov <aris@altlinux.org> 2.0.4-alt2
- rebuilt against libicu*.so.62

* Mon Jun 25 2018 Yuri N. Sedunov <aris@altlinux.org> 2.0.4-alt1
- 2.0.4

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

