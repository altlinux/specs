%define _name gxml
%define ver_major 0.16
%define api_ver 0.16
%def_enable docs

Name: lib%_name
Version: %ver_major.0
Release: alt1

Summary: GXml provides a GObject API for manipulating XML
Group: System/Libraries
License: LGPLv2.1+
Url: http://live.gnome.org/XML

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
#Source: %_name-%version.tar

%define glib_ver 2.32
%define vala_ver 0.34.6
%define gee_ver 0.10.5
%define xml2_ver 2.7

BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libgee0.8-devel >= %gee_ver
BuildRequires: libxml2-devel >= %xml2_ver
BuildRequires: libvala-devel >= %vala_ver vala-tools
BuildRequires: gobject-introspection-devel libgee0.8-gir-devel
BuildRequires: intltool gtk-doc
%{?_enable_docs:BuildRequires: valadoc yelp-tools graphviz}

%description
GXml provides a GObject API for manipulating XML. Most functionality
is provided through libxml2. Currently, GXml provides the DOM Level 1
Core API.

%package devel
Summary: Development files for GXml
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains libraries and header files needed for
development using GXml.

%package gir
Summary: GObject introspection data for the GXml library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the GXml library

%package gir-devel
Summary: GObject introspection devel data for the GXml library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

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
%autoreconf
%configure --disable-static \
	%{subst_enable docs}
%make_build

%install
%makeinstall_std

%check
%make check

%find_lang --output=%_name.lang %_name GXml

%files -f %_name.lang
%_libdir/%name-%api_ver.so.*
%doc AUTHORS NEWS README

%files devel
%_includedir/%_name-%api_ver/
%_libdir/%name-%api_ver.so
%_pkgconfigdir/%_name-%api_ver.pc
%_vapidir/%_name-%api_ver.deps
%_vapidir/%_name-%api_ver.vapi

%files gir
%_typelibdir/GXml-%api_ver.typelib

%files gir-devel
%_girdir/GXml-%api_ver.gir

%if_enabled docs
%files devel-doc
#%_datadir/gtk-doc/html/%_name/
%_datadir/devhelp/books/GXml-%api_ver/
%endif

%changelog
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



