%def_disable snapshot
%define ver_major 1.2
%define beta %nil
%define api_ver 1
%define xdg_name org.gnome.Adwaita%api_ver

%def_enable introspection
%def_enable vala
%def_enable gtk_doc
%def_enable examples
%def_disable check

Name: libadwaita
Version: %ver_major.3
Release: alt1%beta
Epoch: 1

Summary: Library with GTK4 widgets for mobile devices
Group: System/Libraries
License: LGPL-2.1-or-later
Url: https://gitlab.gnome.org/GNOME/libadwaita

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version%beta.tar.xz
#Source: %url/-/archive/%version/%name-%version.tar.bz2
%else
Vcs: https://gitlab.gnome.org/GNOME/libadwaita.git
Source: %name-%version.tar
%endif

%define meson_ver 0.59
%define glib_ver 2.66
%define gtk_ver 4.5.0

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson >= %meson_ver sassc
BuildRequires: pkgconfig(gio-2.0) >= %glib_ver
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: libfribidi-devel
%{?_enable_introspection:BuildRequires(pre): rpm-build-gir
BuildRequires: pkgconfig(gobject-introspection-1.0) gir(Gtk) = 4.0}
%{?_enable_vala:BuildRequires(pre): rpm-build-vala
BuildRequires: vala-tools}
%{?_enable_gtk_doc:BuildRequires: gi-docgen}
%{?_enable_check:BuildRequires: xvfb-run librsvg}

%description
libadwaita is a collection of GTK4 widgets for adaptive applications
targeting form-factors from mobile to desktop. It also offers innovative
widgets following the GNOME design guidelines.

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
GObject introspection data for the %name library.

%package gir-devel
Summary: GObject introspection devel data for %name
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %EVR
Requires: %name-devel = %EVR

%description gir-devel
GObject introspection devel data for the %name library.

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %EVR

%description devel-doc
This package contains development documentation for %name library.

%package demo
Summary: %name widgets demonstration programs
Group: Development/GNOME and GTK+
Requires: %name = %EVR

%description demo
This package contains a program, along with its source code, that
demonstrates %name variety of all its widgets.

%prep
%setup -n %name-%version%beta

%build
%meson \
    %{?_enable_gtk_doc:-Dgtk_doc=true} \
    %{?_disable_examples:-Dexamples=false}
%nil
%meson_build

%install
%meson_install
%find_lang %name

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
xvfb-run -s -noreset %meson_test

%files -f %name.lang
%_libdir/%name-%api_ver.so.*
%doc README.md NEWS

%files devel
%_includedir/%name-%api_ver/
%_libdir/%name-%api_ver.so
%_pkgconfigdir/%name-%api_ver.pc
%{?_enable_vala:%_vapidir/%name-%api_ver.*}

%if_enabled introspection
%files gir
%_typelibdir/Adw-%api_ver.typelib

%files gir-devel
%_girdir/Adw-%api_ver.gir
%endif

%if_enabled gtk_doc
%files devel-doc
%_datadir/doc/%name-%api_ver/
%endif

%if_enabled examples
%files demo
%_bindir/adwaita-%api_ver-demo
%_desktopdir/%{xdg_name}.Demo.desktop
%_iconsdir/hicolor/*/apps/%{xdg_name}.Demo*.svg
%_datadir/metainfo/%{xdg_name}.Demo.metainfo.xml
%endif

%changelog
* Sat Mar 04 2023 Yuri N. Sedunov <aris@altlinux.org> 1:1.2.3-alt1
- 1.2.3

* Sun Feb 12 2023 Yuri N. Sedunov <aris@altlinux.org> 1:1.2.2-alt1
- 1.2.2

* Sat Jan 07 2023 Yuri N. Sedunov <aris@altlinux.org> 1:1.2.1-alt1
- 1.2.1

* Tue Sep 20 2022 Yuri N. Sedunov <aris@altlinux.org> 1:1.2.0-alt1
- 1.2.0

* Sat Sep 03 2022 Yuri N. Sedunov <aris@altlinux.org> 1:1.1.5-alt1
- 1.1.5

* Fri Aug 05 2022 Yuri N. Sedunov <aris@altlinux.org> 1:1.1.4-alt1
- 1.1.4

* Sat Jul 09 2022 Yuri N. Sedunov <aris@altlinux.org> 1:1.1.3-alt1
- 1.1.3

* Wed Jun 01 2022 Yuri N. Sedunov <aris@altlinux.org> 1:1.1.2-alt1
- 1.1.2

* Sat Apr 23 2022 Yuri N. Sedunov <aris@altlinux.org> 1:1.1.1-alt1
- 1.1.1

* Fri Mar 18 2022 Yuri N. Sedunov <aris@altlinux.org> 1:1.1.0-alt1
- 1.1.0

* Fri Mar 18 2022 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.3-alt1
- 1.0.3

* Fri Mar 04 2022 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.2-alt1
- 1.0.2

* Sun Jan 02 2022 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.1-alt1
- 1.0.1

* Fri Dec 31 2021 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.0-alt1
- 1.0.0
- new -demo subpackage

* Tue Nov 02 2021 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.0-alt0.3.alpha.4
- 1.0.0

* Tue Sep 28 2021 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.0-alt0.2.alpha.3
- 1.0.0.alpha3

* Thu Sep 16 2021 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.0-alt0.1alpha.2
- 1.0.0-alpha.2-164-g03f15948

* Tue May 04 2021 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt0.1
- first build for sisyphus

