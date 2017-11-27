%define ver_major 3.26
%define api_ver 3.0
%def_disable static
%def_enable introspection
%def_enable vala

Name: libgweather
Version: %ver_major.1
Release: alt1

Summary: A library for weather information
Group: System/Libraries
License: GPLv3
Url: https://wiki.gnome.org/Projects/LibGWeather

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

# From configure.ac
%define gtk_ver 3.13.5
%define glib_ver 2.35.1
%define intltool_ver 0.40.0
%define soup_ver 2.44
%define gir_ver 0.9.5
%define vala_ver 0.21.1

Requires: %name-data = %version-%release

BuildPreReq: libgio-devel >= %glib_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libsoup-devel >= %soup_ver
BuildPreReq: intltool >= %intltool_ver
BuildPreReq: xsltproc
BuildPreReq: rpm-build-gnome gtk-doc
BuildRequires: libgeocode-glib-devel libxml2-devel perl-XML-Parser xml-utils gzip
%{?_enable_introspection:BuildPreReq: gobject-introspection-devel >= %gir_ver libgtk+3-gir-devel}
%{?_enable_vala:BuildPreReq: vala-tools >= %vala_ver}
BuildRequires: libgladeui2.0-devel

%description
libgweather is a library to access weather information from online
services for numerous locations.

%package data
Summary: Locations data for %name
Group: System/Libraries
BuildArch: noarch

%description data
libgweather is a library to access weather information from online
services for numerous locations.

This package contains locations data for %name

%package devel
Summary: Development files for %name
Group: Development/GNOME and GTK+
# libgweather used to be part of gnome-applets, and
# gnome-applets-devel only had the libgweather-devel parts in it
Obsoletes: gnome-applets-gweather-devel < %version
Provides: gnome-applets-gweather-devel = %version
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name-devel < %version-%release

%description devel-doc
The %name-devel-doc package contains documentation for
developing applications that use %name.

%package gir
Summary: GObject introspection data for the %name library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the %name library

%package gir-devel
Summary: GObject introspection devel data for the %name library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the %name library

%package vala
Summary: Vala language bindings for the %name library
Group: Development/Other
BuildArch: noarch
Requires: %name-devel = %version-%release

%description vala
This package provides Vala language bindings for the %name library.

%prep
%setup

%build
# for tm.tm_gmtoff
%add_optflags -D_GNU_SOURCE
%configure \
    %{subst_enable static} \
    %{subst_enable vala}
%make_build

%install
%makeinstall_std

%find_lang --output=%name.lang %name-%api_ver
%find_lang --output=%name-locations.lang %name-locations

%check
%make check

%files -f %name.lang
%_libdir/*.so.*
%_datadir/glib-2.0/schemas/org.gnome.GWeather.enums.xml
%_datadir/glib-2.0/schemas/org.gnome.GWeather.gschema.xml
%doc AUTHORS NEWS README

%files data -f %name-locations.lang
%dir %_datadir/libgweather
%_datadir/libgweather/Locations.xml
%_datadir/libgweather/locations.dtd

%files devel
%_includedir/%name-%api_ver
%_libdir/*.so
%_pkgconfigdir/*
%_datadir/glade/catalogs/%name.xml

%files devel-doc
%_datadir/gtk-doc/html/*

%if_enabled introspection
%files gir
%_typelibdir/GWeather-%api_ver.typelib

%files gir-devel
%_girdir/GWeather-%api_ver.gir
%endif

%if_enabled vala
%files vala
%_vapidir/gweather-%api_ver.vapi
%endif


%changelog
* Mon Nov 27 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Mon Jun 05 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt1
- 3.24.1

* Sun Mar 19 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Thu Dec 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.4-alt1
- 3.20.4

* Sun Oct 02 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.3-alt2
- changed Asia/Rangoon to Asia/Yangon according to tzdata-2016g

* Mon Aug 29 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.3-alt1
- 3.20.3

* Tue Aug 16 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Mon May 09 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Mon Oct 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Tue Apr 14 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Tue Jan 20 2015 Yuri N. Sedunov <aris@altlinux.org> 3.14.3-alt1
- 3.14.3

* Sun Dec 21 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Mon Oct 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Fri Sep 12 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt2
- Yr.no: update to version 1.9 of the online API (BGO #736334)

* Tue May 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Tue Apr 15 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Sun Feb 02 2014 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

* Tue Oct 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0
- optional -vala subpackage

* Tue May 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Tue Apr 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Tue Nov 13 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1
- 3.6.2

* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Wed Sep 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Fri Mar 09 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Wed Mar 07 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon Oct 24 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Mon Sep 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Wed Apr 06 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Wed Feb 02 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.6-alt1
- 2.91.6

* Fri Nov 05 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.3-alt2
- rebuild for update dependencies

* Sun Oct 03 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.3-alt1
- 2.30.3

* Tue Jun 22 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt1
- 2.30.2

* Tue Mar 30 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Tue Mar 09 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.92-alt1
- 2.29.92

* Tue Feb 23 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.91-alt1
- 2.29.91

* Tue Feb 09 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.90-alt1
- 2.29.90

* Mon Jan 11 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.5-alt1
- 2.29.5

* Fri Dec 25 2009 Yuri N. Sedunov <aris@altlinux.org> 2.29.4-alt1
- 2.29.4

* Tue Sep 22 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Wed Sep 09 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.92-alt1
- 2.27.92

* Tue Aug 25 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.91-alt1
- 2.27.91

* Tue Jun 30 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.2.1-alt1
- 2.26.2.1

* Tue Apr 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Tue Mar 17 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Wed Mar 04 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.92-alt1
- 2.25.92

* Wed Jan 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.5-alt1
- 2.25.5
- new devel-doc noarch package

* Tue Jan 13 2009 Yuri N. Sedunov <aris@altlinux.org> 2.24.3-alt1
- 2.24.3

* Tue Nov 25 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt1
- 2.24.2
- removed obsolete %%post* scripts
- move gziped .xml files (altbug # 17180) to separate noarch subpackage

* Wed Oct 22 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1
- apply %%lang tags to localized xml files (Fedora)

* Sun Sep 28 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt1
- 2.24.0

* Mon Jun 30 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.3-alt1
- new version 2.22.3

* Tue Apr 08 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.1.1-alt1
- new version 2.22.1.1

* Tue Mar 18 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1.1
- build for Sisyphus

* Fri Mar 14 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1
- 2.22.0

* Mon Mar 10 2008 Alexey Shabalin <shaba@altlinux.ru> 2.21.92-alt1
- initial build for ALTLinux

