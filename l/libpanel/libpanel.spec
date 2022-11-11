%def_disable snapshot
%define ver_major 1.0
%define beta %nil
%define api_ver 1
%define xdg_name org.gnome.Panel%api_ver

%def_enable introspection
%def_enable vala
%def_enable docs
%def_enable examples
%def_disable check

Name: libpanel
Version: %ver_major.2
Release: alt1%beta

Summary: Library with GTK4 widgets for IDE-like applications
Group: System/Libraries
License: LGPL-3.0
Url: https://gitlab.gnome.org/GNOME/%name

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version%beta.tar.xz
#Source: %url/-/archive/%version/%name-%version.tar.bz2
%else
Vcs: https://gitlab.gnome.org/GNOME/libpanel.git
Source: %name-%version.tar
%endif

%define meson_ver 0.60
%define glib_ver 2.72
%define gtk_ver 4.6.0
%define adwaita_ver 1.0

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson >= %meson_ver
BuildRequires: pkgconfig(gio-2.0) >= %glib_ver
BuildRequires: pkgconfig(gtk4) >= %gtk_ver  pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: libfribidi-devel
%{?_enable_introspection:BuildRequires(pre): rpm-build-gir
BuildRequires: pkgconfig(gobject-introspection-1.0) gir(Gtk) = 4.0 gir(Adw) = 1}
%{?_enable_vala:BuildRequires(pre): rpm-build-vala
BuildRequires: vala-tools}
%{?_enable_docs:BuildRequires: gi-docgen}
%{?_enable_check:BuildRequires: xvfb-run librsvg}

%description
%name is a collection of GTK widgets for IDE-like applications targeting
GNOME using GTK4 and libadwaita.

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
    %{?_disable_docs:-Ddocs=disabled} \
    %{?_enable_examples:-Dinstall-examples=true}
%nil
%meson_build

%install
%meson_install
%find_lang %name

%check
xvfb-run -s -noreset %__meson_test

%files -f %name.lang
%_libdir/%name-%api_ver.so.*
%_iconsdir/hicolor/*/actions/panel-*.svg
%doc README* NEWS

%files devel
%_includedir/%name-%api_ver/
%_libdir/%name-%api_ver.so
%_pkgconfigdir/%name-%api_ver.pc
%{?_enable_vala:%_vapidir/%name-%api_ver.*}

%if_enabled introspection
%files gir
%_typelibdir/Panel-%api_ver.typelib

%files gir-devel
%_girdir/Panel-%api_ver.gir
%endif

%if_enabled docs
%files devel-doc
%_datadir/doc/panel-1.0/
%endif

%if_enabled examples
%files demo
%_bindir/%name-example
%endif

%changelog
* Fri Nov 11 2022 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Tue Sep 27 2022 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Thu Sep 22 2022 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- first build for Sisyphus

