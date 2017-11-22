%def_disable snapshot

%define _name httpseverywhere
%define ver_major 0.6
%define api_ver 0.6

%def_enable introspection
%def_enable valadoc

Name: lib%_name
Version: %ver_major.4
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
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgee0.8-gir-devel libjson-glib-gir-devel}
%{?_enable_valadoc:BuildRequires: valadoc}

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
%meson %{?_enable_valadoc:-Denable_valadoc=true}
%meson_build

%install
%meson_install

#! src/update.vala
#...

%check
%meson_test

%files
%_libdir/%name-%api_ver.so.*
%dir %_datadir/%name
%_datadir/%name/default.rulesets
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

%if_enabled valadoc
%files devel-doc
%_datadir/devhelp/books/%_name-%api_ver/
%endif

%changelog
* Wed Nov 22 2017 Yuri N. Sedunov <aris@altlinux.org> 0.6.4-alt1
- 0.6.4

* Tue Oct 31 2017 Yuri N. Sedunov <aris@altlinux.org> 0.6.3-alt1
- 0.6.3

* Wed Oct 25 2017 Yuri N. Sedunov <aris@altlinux.org> 0.6.2-alt1
- 0.6.2

* Mon Oct 09 2017 Yuri N. Sedunov <aris@altlinux.org> 0.6.1-alt1
- 0.6.1

* Sat Sep 23 2017 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- 0.6.0

* Thu Jul 27 2017 Yuri N. Sedunov <aris@altlinux.org> 0.4.8-alt1
- 0.4.8

* Fri Jul 14 2017 Yuri N. Sedunov <aris@altlinux.org> 0.4.7-alt1
- 0.4.7

* Wed Jun 21 2017 Yuri N. Sedunov <aris@altlinux.org> 0.4.6-alt1
- 0.4.6

* Fri Jun 09 2017 Yuri N. Sedunov <aris@altlinux.org> 0.4.5-alt1
- 0.4.5

* Tue Jun 06 2017 Yuri N. Sedunov <aris@altlinux.org> 0.4.4-alt1
- 0.4.4

* Thu May 11 2017 Yuri N. Sedunov <aris@altlinux.org> 0.4.3-alt1
- 0.4.3

* Thu Apr 20 2017 Yuri N. Sedunov <aris@altlinux.org> 0.4.2-alt1
- 0.4.2

* Thu Apr 06 2017 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- 0.4.1

* Sun Mar 19 2017 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- 0.4.0

* Wed Dec 21 2016 Yuri N. Sedunov <aris@altlinux.org> 0.2.10-alt1
- first build for Sisyphus




