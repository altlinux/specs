%def_disable snapshot
%define ver_major 1.5
%define beta %nil
%define namespace Adap
%define api_ver 1
%define xdg_name org.gnome.Adapta%api_ver

%def_enable introspection
%def_enable vala
%def_enable gtk_doc
%def_enable examples
%def_disable check

Name: libadapta
Version: %ver_major.0
Release: alt1%beta

Summary: libAdapta is libAdwaita with theme support and a few extra
Group: System/Libraries
License: LGPL-2.1-or-later
Url: https://github.com/xapp-project/libadapta

Vcs: https://github.com/xapp-project/libadapta.git

%if_disabled snapshot
Source: https://github.com/xapp-project/libadapta/archive/%version/%name-%version%beta.tar.gz
%else
Source: %name-%version%beta.tar
%endif

%define meson_ver 0.59
%define glib_ver 2.76.0
%define gtk_ver 4.13.4
%define gi_ver 1.76

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson >= %meson_ver sassc
BuildRequires: pkgconfig(gio-2.0) >= %glib_ver
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: libfribidi-devel
BuildRequires: libappstream-devel
%{?_enable_introspection:BuildRequires(pre): rpm-build-gir
BuildRequires: gobject-introspection-devel >= %gi_ver gir(Gtk) = 4.0}
%{?_enable_vala:BuildRequires(pre): rpm-build-vala
BuildRequires: vala-tools}
%{?_enable_gtk_doc:BuildRequires: gi-docgen}
%{?_enable_check:BuildRequires: xvfb-run librsvg xdg-desktop-portal}

%description
%{summary}.
It provides the same features and the same look as libAdwaita by
default.

In desktop environments which provide theme selection, libAdapta apps
follow the theme and use the proper window controls.

libAdapta also provides a compatibility header which makes it easy for
developers to switch between libAdwaita and libAdapta without requiring
code changes.

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
    %{subst_enable_meson_bool gtk_doc gtk_doc} \
    %{subst_enable_meson_bool examples examples}
%nil
%meson_build

%install
%meson_install
%find_lang %name

%check
xvfb-run -s -noreset %__meson_test

%files -f %name.lang
%_libdir/%name-%api_ver.so.*
#%_libdir/%name-%api_ver-internal.so.*
%doc README.md NEWS

%files devel
%_includedir/%name-%api_ver/
%_libdir/%name-%api_ver.so
#%_libdir/%name-%api_ver-internal.so
%_pkgconfigdir/%name-%api_ver.pc
%{?_enable_vala:%_vapidir/%name-%api_ver.*}

%if_enabled introspection
%files gir
%_typelibdir/%namespace-%api_ver.typelib

%files gir-devel
%_girdir/%namespace-%api_ver.gir
%endif

%if_enabled gtk_doc
%files devel-doc
%_datadir/doc/%name-%api_ver/
%endif

%if_enabled examples
%files demo
%_bindir/adapta-%api_ver-demo
%_desktopdir/%{xdg_name}.Demo.desktop
%_iconsdir/hicolor/*/apps/%{xdg_name}.Demo*.svg
%_datadir/metainfo/%{xdg_name}.Demo.metainfo.xml
%_datadir/themes/LibAdapta-Example/
%endif

%changelog
* Fri May 23 2025 Yuri N. Sedunov <aris@altlinux.org> 1.5.0-alt1
- first build for sisyphus

