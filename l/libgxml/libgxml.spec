%def_enable snapshot

%define _name gxml
%define namespace GXml
%define ver_major 0.20
%define api_ver 0.20

%def_enable introspection
%def_enable docs
%def_enable check

Name: lib%_name
Version: %ver_major.4
Release: alt1

Summary: GXml provides a GObject API for manipulating XML
Group: System/Libraries
License: LGPL-2.1-or-later
Url: https://wiki.gnome.org/GXml

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
%else
Source: %_name-%version.tar
%endif

%define glib_ver 2.72
%define vala_ver 0.34.6
%define gee_ver 0.20.5
%define xml2_ver 2.9.13

BuildRequires(pre): rpm-macros-meson rpm-build-vala
BuildRequires: meson vala-tools
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libgee0.8-devel >= %gee_ver
BuildRequires: libxml2-devel >= %xml2_ver
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgee0.8-gir-devel}
%{?_enable_docs:BuildRequires: valadoc yelp-tools graphviz gtk-doc
BuildRequires: fonts-ttf-roboto fonts-ttf-google-noto-sans-vf}

%description
GXml provides a GObject API for manipulating XML. Most functionality
is provided through libxml2. Currently, GXml provides the DOM Level 1
Core API.

%package devel
Summary: Development files for GXml
Group: Development/C
Requires: %name = %EVR

%description devel
This package contains libraries and header files needed for
development using GXml.

%package gir
Summary: GObject introspection data for the GXml library
Group: System/Libraries
Requires: %name = %EVR

%description gir
GObject introspection data for the GXml library

%package gir-devel
Summary: GObject introspection devel data for the GXml library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %EVR
Requires: %name-devel = %EVR

%description gir-devel
GObject introspection devel data for the GXml library.

%package devel-doc
Summary: Development documentation for GXml
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version-%release

%description devel-doc
This package contains development documentation for GXml library.

%prep
%setup -n %_name-%version
# to avoid "/usr/lib/rpm/debugedit: canonicalization unexpectedly shrank by one character" bug
find ./ -type f -print0| xargs -r0 subst 's|gxml//xlibxml.h|gxml/xlibxml.h|' --

%build
%meson \
    %{?_enable_docs:-Ddocs=true} \
    %{?_enable_introspection:-Dintrospection=true}
%nil
%meson_build

%install
%meson_install
%find_lang --output=%_name.lang %_name GXml-%api_ver

%check
%__meson_test

%files -f %_name.lang
%_libdir/%name-%api_ver.so.*
%doc AUTHORS NEWS README

%files devel
%_includedir/%_name-%api_ver/
%_libdir/%name-%api_ver.so
%_pkgconfigdir/%_name-%api_ver.pc
%_vapidir/%_name-%api_ver.vapi

%if_enabled introspection
%files gir
%_typelibdir/%namespace-%api_ver.typelib

%files gir-devel
%_girdir/%namespace-%api_ver.gir
%endif

%if_enabled docs
%files devel-doc
#%_datadir/gtk-doc/html/%_name/
%_datadir/devhelp/books/%namespace-%api_ver/
%endif

%changelog
* Tue May 07 2024 Yuri N. Sedunov <aris@altlinux.org> 0.20.4-alt1
- updated to 0.20.4-19-g54a9251

* Wed Mar 09 2022 Yuri N. Sedunov <aris@altlinux.org> 0.20.3-alt1.1
- added some fonts to BR to fix docs build

* Sat Mar 05 2022 Yuri N. Sedunov <aris@altlinux.org> 0.20.3-alt1
- updated to 0.20.3-7-g3eac3ac

* Sun Dec 19 2021 Yuri N. Sedunov <aris@altlinux.org> 0.20.1-alt1
- updated to 0.20.1-10-gf02031e

* Fri Oct 30 2020 Yuri N. Sedunov <aris@altlinux.org> 0.20.0-alt1
- 0.20.0

* Thu Aug 20 2020 Yuri N. Sedunov <aris@altlinux.org> 0.18.2-alt1
- 0.18.2

* Mon Jul 08 2019 Yuri N. Sedunov <aris@altlinux.org> 0.18.1-alt1
- 0.18.1 (ported to Meson build system)

* Thu Jul 04 2019 Yuri N. Sedunov <aris@altlinux.org> 0.18.0-alt1
- 0.18.0

* Sat Jan 05 2019 Yuri N. Sedunov <aris@altlinux.org> 0.16.3-alt2
- updated to 0.16.3-3-ge51ce7b

* Mon Mar 05 2018 Yuri N. Sedunov <aris@altlinux.org> 0.16.3-alt1
- 0.16.3

* Wed Feb 07 2018 Yuri N. Sedunov <aris@altlinux.org> 0.16.1-alt1
- 0.16.1

* Wed Jan 10 2018 Yuri N. Sedunov <aris@altlinux.org> 0.16.0-alt1
- 0.16.0

* Sat Apr 08 2017 Yuri N. Sedunov <aris@altlinux.org> 0.14.3-alt1
- 0.14.3

* Thu Apr 06 2017 Yuri N. Sedunov <aris@altlinux.org> 0.14.2-alt1
- 0.14.2

* Fri Mar 10 2017 Yuri N. Sedunov <aris@altlinux.org> 0.14.0-alt1
- 0.14.0

* Tue Sep 27 2016 Yuri N. Sedunov <aris@altlinux.org> 0.12.0-alt1
- 0.12.0

* Fri Jan 15 2016 Yuri N. Sedunov <aris@altlinux.org> 0.8.2-alt1
- 0.8.2

* Wed Jan 13 2016 Yuri N. Sedunov <aris@altlinux.org> 0.8.1-alt1
- 0.8.1

* Thu Jul 09 2015 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- first build for Sisyphus



