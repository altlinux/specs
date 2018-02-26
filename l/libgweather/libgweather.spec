%define ver_major 3.4
%define api_ver 3.0
%def_disable static
%def_enable introspection

Name: libgweather
Version: %ver_major.1
Release: alt1
Summary: A library for weather information

Group: System/Libraries
License: GPLv3
Url: http://live.gnome.org/LibGWeather
Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

# From configure.in
%define gtk_ver 2.91.7
%define glib_ver 2.27.4
%define gconf_ver 2.32.0
%define intltool_ver 0.40.0
%define soup_ver 2.33.1
%define gir_ver 0.9.5

Requires: %name-data = %version-%release

BuildPreReq: libGConf-devel >= %gconf_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libsoup-gnome-devel >= %soup_ver
BuildPreReq: intltool >= %intltool_ver
BuildPreReq: xsltproc
BuildPreReq: rpm-build-gnome
BuildRequires: libxml2-devel perl-XML-Parser xml-utils gzip
%{?_enable_introspection:BuildPreReq: gobject-introspection-devel >= %gir_ver libgtk+3-gir-devel}

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
Group: Development/C
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
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the %name library

%prep
%setup -q

%build
%configure \
    %{subst_enable static} \
    --enable-locations-compression

%make_build

#cd po
#make %name.pot
#for p in *.po; do
#  msgmerge -U $p %name.pot
#done
#make
#cd ..

%install
%make_install DESTDIR=%buildroot install

%find_lang --output=%name.lang %name-%api_ver

# do the %%lang tag for the localized xml files
find %buildroot -name Locations.*.xml.gz | sed 's:'"%buildroot"'::
s:\(.*\)/Locations\.\([^.]*\)\.xml.gz:%lang(\2) \1/Locations.\2.xml.gz:' > %name-data.lang

%post
%gconf2_install gweather

%preun
if [ $1 = 0 ]; then
%gconf2_uninstall gweather
fi

%files -f %name.lang
%_libdir/*.so.*
%gconf_schemasdir/*.schemas
%doc AUTHORS NEWS README

%files data -f %name-data.lang
%dir %_datadir/libgweather
%_datadir/libgweather/Locations.xml.gz
%_datadir/libgweather/locations.dtd
%_iconsdir/gnome/*/*/*

%files devel
%_includedir/%name-%api_ver
%_libdir/*.so
%_pkgconfigdir/*

%files devel-doc
%_datadir/gtk-doc/html/*

%if_enabled introspection
%files gir
%_libdir/girepository-1.0/GWeather-3.0.typelib

%files gir-devel
%_datadir/gir-1.0/GWeather-3.0.gir
%endif

%changelog
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

