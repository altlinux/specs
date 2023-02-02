%def_disable snapshot
%define _name libhandy
%define ver_major 1.8
%define api_ver 1

%def_enable introspection
%def_enable vala
%def_enable gtk_doc
%def_enable glade_catalog
%def_enable check

Name: %_name%api_ver
Version: %ver_major.1
Release: alt1

Summary: Library with GTK+3 widgets for mobile devices (API version 1)
Group: System/Libraries
License: LGPL-2.1-or-later
Url: https://gitlab.gnome.org/GNOME/libhandy

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
#Source: %url/-/archive/%version/%name-%version.tar.bz2
%else
Vcs: https://gitlab.gnome.org/GNOME/libhandy.git
Source: %_name-%version.tar
%endif

%define gtk_ver 3.24.1
%define glade_ver 3.36

BuildRequires(pre): rpm-macros-meson rpm-build-gir
BuildRequires: meson pkgconfig(gio-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gmodule-2.0)
BuildRequires: pkgconfig(gtk+-3.0) >= %gtk_ver
BuildRequires: pkgconfig(fribidi)
%{?_enable_introspection:BuildRequires: pkgconfig(gobject-introspection-1.0) gir(Gtk) = 3.0}
%{?_enable_vala:BuildRequires(pre): rpm-build-vala
BuildRequires: vala-tools}
%{?_enable_gtk_doc:BuildRequires: gi-docgen}
%{?_enable_glade_catalog:BuildRequires: pkgconfig(gladeui-2.0) >= %glade_ver}
%{?_enable_check:BuildRequires: xvfb-run librsvg fonts-ttf-liberation}

%description
libhandy provides GTK+3 widgets and GObjects to ease developing
applications for mobile devices.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package gir
Summary: GObject introspection data for %name
Group: System/Libraries
Requires: %name = %EVR

%description gir
GObject introspection data for the handy library.

%package gir-devel
Summary: GObject introspection devel data for %name
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %EVR
Requires: %name-devel = %EVR

%description gir-devel
GObject introspection devel data for the handy library.

%package devel-doc
Summary: Development documentation for %_name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %EVR

%description devel-doc
This package contains development documentation for handy library.

%prep
%setup -n %_name-%version

%build
%meson \
	-Dgtk_doc=true \
	-Dexamples=false
%meson_build

%install
%meson_install
%find_lang %_name

%check
xvfb-run -s -noreset %__meson_test

%files -f %_name.lang
%_libdir/%_name-%api_ver.so.*
%doc README.md

%files devel
%_includedir/%_name-%api_ver/
%_libdir/%_name-%api_ver.so
%_pkgconfigdir/%_name-%api_ver.pc
%{?_enable_glade_catalog:%_libdir/glade/modules/libglade-handy-%api_ver.so
%_datadir/glade/catalogs/%_name-%api_ver.xml}
%{?_enable_vala:%_vapidir/%_name-%api_ver.*}

%if_enabled introspection
%files gir
%_typelibdir/Handy-%api_ver.typelib

%files gir-devel
%_girdir/Handy-%api_ver.gir
%endif

%if_enabled gtk_doc
%files devel-doc
%_datadir/doc/%_name-%api_ver/
%endif

%changelog
* Thu Feb 02 2023 Yuri N. Sedunov <aris@altlinux.org> 1.8.1-alt1
- 1.8.1

* Mon Sep 26 2022 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- 1.8.0

* Sat Jul 09 2022 Yuri N. Sedunov <aris@altlinux.org> 1.6.3-alt1
- 1.6.3

* Sat Apr 23 2022 Yuri N. Sedunov <aris@altlinux.org> 1.6.2-alt1
- 1.6.2

* Sat Mar 19 2022 Yuri N. Sedunov <aris@altlinux.org> 1.6.1-alt1
- 1.6.1

* Fri Mar 11 2022 Yuri N. Sedunov <aris@altlinux.org> 1.5.0-alt1.1
- fixed %%check

* Fri Nov 12 2021 Yuri N. Sedunov <aris@altlinux.org> 1.5.0-alt1
- 1.5.0

* Sun Sep 05 2021 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Mon Jun 21 2021 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt1
- 1.2.3

* Tue Apr 27 2021 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt1
- 1.2.2

* Mon Apr 19 2021 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- updated to 1.2.1-2-gf2ec0b3

* Fri Mar 12 2021 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Thu Dec 24 2020 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt1
- 1.0.3

* Thu Nov 12 2020 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Mon Nov 02 2020 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- updated to 1.0.1-1-ga7cfd93

* Tue Sep 08 2020 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Fri Aug 28 2020 Yuri N. Sedunov <aris@altlinux.org> 0.90.0-alt1
- 0.90.0

* Fri Jun 19 2020 Yuri N. Sedunov <aris@altlinux.org> 0.0.13-alt1.1
- disabled glade catalog incompatible with glade-3.36

* Thu Jan 09 2020 Yuri N. Sedunov <aris@altlinux.org> 0.0.13-alt1
- 0.0.13

* Fri Dec 13 2019 Yuri N. Sedunov <aris@altlinux.org> 0.0.12-alt1
- 0.0.12

* Fri Aug 30 2019 Yuri N. Sedunov <aris@altlinux.org> 0.0.11-alt1
- 0.0.11

* Wed Jun 19 2019 Yuri N. Sedunov <aris@altlinux.org> 0.0.10-alt1
- 0.0.10

* Fri Mar 08 2019 Yuri N. Sedunov <aris@altlinux.org> 0.0.9-alt1
- 0.0.9

* Sat Feb 16 2019 Yuri N. Sedunov <aris@altlinux.org> 0.0.8-alt1
- 0.0.8

* Thu Feb 07 2019 Yuri N. Sedunov <aris@altlinux.org> 0.0.7-alt1
- first build for sisyphus

