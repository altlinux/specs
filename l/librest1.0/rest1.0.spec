%def_disable snapshot

%define _name rest
%define ver_major 0.9
%define api_ver 1.0

%def_disable soup2
%def_enable introspection
%def_enable gtk_doc
%def_enable tests
%def_enable demo

Name: lib%_name%api_ver
Version: %ver_major.1
Release: alt1

Summary: A library for access to RESTful web services
Group: System/Libraries
License: LGPL-2.1-or-later
Url: http://www.gnome.org

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
%else
Source: %_name-%version.tar
%endif

Requires: ca-certificates

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson glib2-devel libxml2-devel pkgconfig(json-glib-1.0)
%if_enabled soup2
BuildRequires: pkgconfig(libsoup-2.4)
%else
BuildRequires: pkgconfig(libsoup-3.0)
%endif
%{?_enable_introspection:BuildRequires(pre): rpm-build-gir
%if_enabled soup2
BuildRequires: gir(Soup) = 2.4
%else
BuildRequires: gir(Soup) = 3.0
%endif
}
%{?_enable_gtk_doc:BuildRequires: gi-docgen}
%{?_enable_demo:BuildRequires: pkgconfig(libadwaita-1) pkgconfig(gtksourceview-5)}

%description
This library was designed to make it easier to access web services that
claim to be "RESTful". A RESTful service should have urls that represent
remote objects, which methods can then be called on. The majority of services
don't actually adhere to this strict definition. Instead, their RESTful end
point usually has an API that is just simpler to use compared to other types
of APIs they may support (XML-RPC, for instance). It is this kind of API that
this library is attempting to support.

%package devel
Summary: Development package for %name
Group: Development/C
Requires: %name = %EVR

%description devel
Files for development with %name.

%package gir
Summary: GObject introspection data for the %_name library
Group: System/Libraries
Requires: %name = %EVR

%description gir
GObject introspection data for the %_name library

%package gir-devel
Summary: GObject introspection devel data for the %_name library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %EVR
Requires: %name-devel = %EVR

%description gir-devel
GObject introspection devel data for the %_name library

%package devel-doc
Summary: Development documentation for %_name
Group: Development/C
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
This package contains development documentation for the %_name library.

%package demo
Summary: %name demonstration program
Group: Development/C
Requires: %name = %EVR

%description demo
This package provides demonstration program for the %_name library.

%prep
%setup -n %_name-%version

%build
%meson \
    %{?_enable_soup2:-Dsoup2=true} \
    %{?_disable_gtk_doc:-Dgtk-doc=false} \
    %{?_disable_tests:-Dtests=false} \
    -Dca_certificates_path="%_datadir/ca-certificates/ca-bundle.crt"
%nil
%meson_build

%install
%meson_install

%check
# network required for extras (flickr, lastfm) tests
%__meson_test --no-suite rest-extras

%files
%_libdir/lib%_name-%api_ver.so.*
%_libdir/lib%_name-extras-%api_ver.so.*
%doc AUTHORS README* NEWS

%files devel
%_includedir/%_name-%api_ver/
%_libdir/lib%_name-%api_ver.so
%_libdir/lib%_name-extras-%api_ver.so
%_pkgconfigdir/%{_name}*%api_ver.pc

%if_enabled introspection
%files gir
%_typelibdir/Rest-%api_ver.typelib
%_typelibdir/RestExtras-%api_ver.typelib

%files gir-devel
%_girdir/Rest-%api_ver.gir
%_girdir/RestExtras-%api_ver.gir
%endif

%if_enabled gtk_doc
%files devel-doc
%_datadir/doc/lib%_name-%api_ver/
%endif

%if_enabled demo
%files demo
%_bindir/lib%_name-demo
%_desktopdir/org.gnome.RestDemo.desktop
%endif

%changelog
* Mon Jun 20 2022 Yuri N. Sedunov <aris@altlinux.org> 0.9.1-alt1
- 0.9.1 (1.0 API, ported to Meson build system)

* Tue Oct 17 2017 Yuri N. Sedunov <aris@altlinux.org> 0.8.1-alt1
- 0.8.1

* Mon Apr 18 2016 Yuri N. Sedunov <aris@altlinux.org> 0.8.0-alt1
- 0.8.0

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 0.7.93-alt1
- 0.7.93

* Wed Sep 03 2014 Yuri N. Sedunov <aris@altlinux.org> 0.7.92-alt1
- 0.7.92

* Mon Mar 10 2014 Yuri N. Sedunov <aris@altlinux.org> 0.7.91-alt1
- 0.7.91

* Thu Sep 06 2012 Yuri N. Sedunov <aris@altlinux.org> 0.7.90-alt1
- 0.7.90

* Thu Nov 10 2011 Yuri N. Sedunov <aris@altlinux.org> 0.7.12-alt1
- 0.7.12

* Mon Oct 31 2011 Yuri N. Sedunov <aris@altlinux.org> 0.7.11-alt1
- 0.7.11

* Sat Jul 16 2011 Yuri N. Sedunov <aris@altlinux.org> 0.7.10-alt2
- build without tests.

* Thu Jun 30 2011 Yuri N. Sedunov <aris@altlinux.org> 0.7.10-alt1
- first build for Sisyphus

