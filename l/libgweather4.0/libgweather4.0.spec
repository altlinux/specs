%def_disable snapshot

%define _libexecdir %_prefix/libexec
%define _name libgweather
%define ver_major 4.2
%define beta %nil
%define api_ver_major 4
%define api_ver 4.0
%define xdg_name org.gnome.GWeather%api_ver_major

%def_enable new_russia

%def_disable soup2
%def_enable introspection
%def_enable vala
%def_enable gtk_doc
# libgweather test suite fails offline, required https://www.aviationweather.gov
%def_enable check

Name: %_name%api_ver
Version: %ver_major.0
Release: alt2%beta

Summary: A library for weather information
Group: System/Libraries
License: GPLv3
Url: https://wiki.gnome.org/Projects/LibGWeather

%if_disabled snapshot
Source: %gnome_ftp/%_name/%ver_major/%_name-%version%beta.tar.xz
%else
Source: %_name-%version%beta.tar
%endif
%{?_enable_new_russia:
Patch10: %_name-4.2.0-alt-Simferopol.patch
Patch11: %_name-4.2.0-alt-Donetsk.patch
Patch12: %_name-4.2.0-alt-Donetsk-po-locations.patch}

%define glib_ver 2.68
%define soup2_ver 2.44
%define soup_api_ver 3.0
%define soup3_ver 2.99.2
%define gir_ver 0.9.5
%define vala_ver 0.21.1
%define geocode_ver 3.26.3

BuildRequires(pre): rpm-build-gnome rpm-macros-meson
BuildRequires: meson
BuildRequires: libgio-devel >= %glib_ver libxml2-devel pkgconfig(json-glib-1.0)
BuildRequires: xsltproc perl-XML-Parser xml-utils gzip
BuildRequires: python3-module-pygobject3 python3-module-pylint
%{?_disable_soup2:BuildRequires: pkgconfig(libsoup-3.0) >= %soup3_ver pkgconfig(geocode-glib-2.0) >= %geocode_ver}
%{?_enable_soup2:BuildRequires: libsoup-devel >= %soup2_ver pkgconfig(geocode-glib-1.0)}
%{?_enable_introspection:BuildRequires(pre): rpm-build-gir
BuildRequires: gobject-introspection-devel >= %gir_ver libgtk+3-gir-devel}
%{?_enable_vala:BuildRequires(pre): rpm-build-vala
BuildRequires: vala-tools >= %vala_ver}
%{?_enable_gtk_doc:BuildRequires: gi-docgen}

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

This package contains locations development data for %name.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR
Requires: %name-data = %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name-devel < %EVR

%description devel-doc
The %name-devel-doc package contains documentation for
developing applications that use %name.

%package gir
Summary: GObject introspection data for the %name library
Group: System/Libraries
Requires: %name = %EVR

%description gir
GObject introspection data for the %name library

%package gir-devel
Summary: GObject introspection devel data for the %name library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %EVR
Requires: %name-devel = %EVR

%description gir-devel
GObject introspection devel data for the %name library

%package vala
Summary: Vala language bindings for the %name library
Group: Development/Other
BuildArch: noarch
Requires: %name-devel = %EVR

%description vala
This package provides Vala language bindings for the %name library.

%prep
%setup -n %_name-%version%beta
%{?_enable_new_russia:
%patch10 -b .Simferopol
%patch11 -b .Donetsk
%patch12 -b .Donetsk}

sed -i "s|'\(pylint\)'|'\1.py3'|" meson.build

%build
# for tm.tm_gmtoff
%add_optflags -D_GNU_SOURCE
%meson \
    %{?_enable_gtk_doc:-Dgtk_doc=true} \
    %{?_disable_vala:-Denable_vala=false} \
    %{?_enable_soup2:-Dsoup2=true}
%nil
%{?_enable_new_russia:%meson_build %_name-%api_ver-locations-pot %_name-%api_ver-update-po}
%meson_build

%install
%meson_install
%find_lang --output=%name.lang %_name-%api_ver %_name-%api_ver-locations

%check
%__meson_test -v --print-errorlogs --suite lint

%files -f %name.lang
%dir %_libdir/%_name-%api_ver_major
%_libdir/%_name-%api_ver_major/Locations.bin
%_libdir/%_name-%api_ver_major.so.*
%_datadir/glib-2.0/schemas/%xdg_name.enums.xml
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%doc NEWS README*

%files devel
%_includedir/%_name-%api_ver
%_libdir/%_name-%api_ver_major.so
%_pkgconfigdir/*

%files data
%dir %_datadir/%_name-%api_ver_major
%_datadir/%_name-%api_ver_major/Locations.xml
%_datadir/%_name-%api_ver_major/locations.dtd

%if_enabled gtk_doc
%files devel-doc
%_datadir/doc/libgweather-%api_ver/
%endif

%if_enabled introspection
%files gir
%_typelibdir/GWeather-%api_ver.typelib

%files gir-devel
%_girdir/GWeather-%api_ver.gir
%endif

%if_enabled vala
%files vala
%_vapidir/gweather%api_ver_major.vapi
%_vapidir/gweather%api_ver_major.deps
%endif


%changelog
* Sun Dec 18 2022 Yuri N. Sedunov <aris@altlinux.org> 4.2.0-alt2
- fixed Simferopol and Donetsk locations

* Tue Sep 20 2022 Yuri N. Sedunov <aris@altlinux.org> 4.2.0-alt1
- 4.2.0

* Sat Sep 03 2022 Yuri N. Sedunov <aris@altlinux.org> 4.1.1-alt1
- 4.1.1
- built with libsoup-3.0/geocode-glib-2.0

* Fri Mar 18 2022 Yuri N. Sedunov <aris@altlinux.org> 4.0.0-alt1
- 4.0.0

* Sat Nov 20 2021 Yuri N. Sedunov <aris@altlinux.org> 3.90.0-alt1
- first build for Sisyphus

