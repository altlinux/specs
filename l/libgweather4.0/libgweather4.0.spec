%def_disable snapshot

%define _libexecdir %_prefix/libexec
%define _name libgweather
%define ver_major 4.0
%define beta %nil
%define api_ver_major 4
%define api_ver 4.0
%define xdg_name org.gnome.GWeather%api_ver_major

# while geocode-glib depends on soup-2.4
%def_enable soup2
%def_enable introspection
%def_enable vala
%def_enable gtk_doc
# fails offline
%def_disable check

Name: %_name%api_ver
Version: %ver_major.0
Release: alt1%beta

Summary: A library for weather information
Group: System/Libraries
License: GPLv3
Url: https://wiki.gnome.org/Projects/LibGWeather

%if_disabled snapshot
Source: %gnome_ftp/%_name/%ver_major/%_name-%version%beta.tar.xz
%else
Source: %_name-%version%beta.tar
%endif

%define glib_ver 2.68
%define soup2_ver 2.44
%define soup_api_ver 3.0
%define soup3_ver 2.99.2
%define gir_ver 0.9.5
%define vala_ver 0.21.1
%define geocode_ver 3.26.1

Requires: %name-data = %EVR

BuildRequires(pre): rpm-build-gnome rpm-macros-meson
BuildRequires: meson
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libgeocode-glib-devel >= %geocode_ver libxml2-devel
BuildRequires: xsltproc perl-XML-Parser xml-utils gzip
BuildRequires: python3-module-pygobject3 python3-module-pylint
%{?_disable_soup2:BuildRequires: libsoup%soup_api_ver-devel >= %soup3_ver}
%{?_enable_soup2:BuildRequires: libsoup-devel >= %soup2_ver}
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

This package contains locations data for %name

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

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

sed -i "s|'\(pylint\)'|'\1.py3'|" meson.build

%build
# for tm.tm_gmtoff
%add_optflags -D_GNU_SOURCE
%meson \
    %{?_enable_gtk_doc:-Dgtk_doc=true} \
    %{?_disable_vala:-Denable_vala=false} \
    %{?_disable_soup2:-Dsoup2=false}
%nil
%meson_build

%install
%meson_install
%find_lang --output=%name.lang %_name-%api_ver
%find_lang --output=%name-locations.lang %_name-%api_ver-locations

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%meson_test

%files -f %name.lang
%dir %_libdir/%_name-%api_ver_major
%_libdir/%_name-%api_ver_major/Locations.bin
%_libdir/*.so.*
%_datadir/glib-2.0/schemas/%xdg_name.enums.xml
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%doc NEWS README*

%files data -f %name-locations.lang
%dir %_datadir/%_name-%api_ver_major
%_datadir/%_name-%api_ver_major/Locations.xml
%_datadir/%_name-%api_ver_major/locations.dtd

%files devel
%_includedir/%_name-%api_ver
%_libdir/*.so
%_pkgconfigdir/*

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
* Fri Mar 18 2022 Yuri N. Sedunov <aris@altlinux.org> 4.0.0-alt1
- 4.0.0

* Sat Nov 20 2021 Yuri N. Sedunov <aris@altlinux.org> 3.90.0-alt1
- first build for Sisyphus

