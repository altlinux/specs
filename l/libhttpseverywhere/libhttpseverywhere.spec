%def_disable snapshot

%define _name httpseverywhere
%define ver_major 0.2
%define api_ver 0.2

%def_enable introspection
%def_disable doc

Name: lib%_name
Version: %ver_major.10
Release: alt1

Summary: Library to use HTTPSEverywhere in desktop applications
Group: System/Libraries
License: LGPLv3
Url: https://github.com/grindhold/%name

%if_disabled snapshot
#Source: %url/archive/%name-%version.tar.gz
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

BuildRequires: meson >= 0.36.0 vala-tools valadoc
BuildRequires: libgio-devel libsoup-devel libarchive-devel libxml2-devel
BuildRequires: libjson-glib-devel libgee0.8-devel
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgee0.8-gir-devel}

%description
%name is a GObject based library enables to leverage the power of
[HTTPSEverywhere](https://www.eff.org/https-everywhere) to any
desktop-application.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
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

%package devel-doc
Summary: Development documentation for %name
Group: Development/C
BuildArch: noarch
Conflicts: %name < %version-%release

%description devel-doc
This package contains development documentation for %name

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

#! src/update.vala
#...

%check
#ninja-build -C mesonbuild test
%meson_test

%files
%_libdir/%name-%api_ver.so.*
%dir %_datadir/%name
%_datadir/%name/rulesets.json
%doc README.md

%files devel
%_includedir/%_name-%api_ver/
%_libdir/%name-%api_ver.so
%_pkgconfigdir/%_name-%api_ver.pc
%_vapidir/%_name-%api_ver.deps
%_vapidir/%_name-%api_ver.vapi

%if_enabled introspection
%files gir
%_typelibdir/HTTPSEverywhere-%api_ver.typelib

#%files gir-devel
#%_girdir/HTTPSEverywhere-%api_ver.gir
%endif

%if_enabled doc
%files devel-doc
%_datadir/devhelp/books/%_name-%api_ver/
%endif

%changelog
* Wed Dec 21 2016 Yuri N. Sedunov <aris@altlinux.org> 0.2.10-alt1
- first build for Sisyphus




