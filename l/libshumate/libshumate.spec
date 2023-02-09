%def_disable snapshot
%define _name shumate
%define ver_major 1.0
%define beta %nil
%define api_ver_major 1
%define api_ver 1.0
%define xdg_name org.gnome.Shumate

%def_enable introspection
%def_enable vala
%def_enable gtk_doc
%def_enable demos
%def_enable check

Name: lib%_name
Version: %ver_major.3
Release: alt1.1%beta

Summary: Library with GTK4 widget to display maps
Group: System/Libraries
License: LGPL-2.1-or-later
Url: https://gitlab.gnome.org/GNOME/libshumate

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version%beta.tar.xz
%else
Vcs: https://gitlab.gnome.org/GNOME/libshumate.git
Source: %name-%version.tar
%endif

%define meson_ver 0.53
%define glib_ver 2.66
%define gtk_ver 4.5.0
%define soup3_ver 3.0.0

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson >= %meson_ver
BuildRequires: pkgconfig(gio-2.0) >= %glib_ver
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(sqlite3)
%if_enabled soup3
BuildRequires: libsoup3.0-devel >= %soup3_ver
%else
BuildRequires: libsoup-devel
%endif
%{?_enable_soup3:BuildRequires: libsoup3-devel >= %soup3_ver}
%{?_enable_introspection:BuildRequires(pre): rpm-build-gir
BuildRequires: pkgconfig(gobject-introspection-1.0) gir(Gtk) = 4.0}
%{?_enable_vala:BuildRequires(pre): rpm-build-vala
BuildRequires: vala-tools}
%{?_enable_gtk_doc:BuildRequires: gtk-doc gi-docgen}
%{?_enable_check:BuildRequires: /proc xvfb-run librsvg /bin/dbus-launch at-spi2-core}

%description
libshumate is a GTK4 widget to display maps.

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
GObject introspection data for the %_name library.

%package gir-devel
Summary: GObject introspection devel data for %name
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %EVR
Requires: %name-devel = %EVR

%description gir-devel
GObject introspection devel data for the %_name library.

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %EVR

%description devel-doc
This package contains development documentation for %_name library.

%package demo
Summary: %name widgets demonstration programs
Group: Development/GNOME and GTK+
Requires: %name = %EVR

%description demo
This package contains a program, along with its source code, that
demonstrates %name.

%prep
%setup -n %name-%version%beta

%build
%meson \
    %{?_enable_soup3:-Dlibsoup3=true} \
    %{?_enable_gtk_doc:-Dgtk_doc=true} \
    %{?_enable_demos:-Ddemos=true}
%nil
%meson_build

%install
%meson_install
%find_lang --output=%name.lang  %name %_name%api_ver_major

%check
# set GTK_A11Y=none if at-spi2-core not available
xvfb-run -s -noreset %__meson_test -v

%files -f %name.lang
%_libdir/%name-%api_ver.so.*
%doc README* NEWS

%files devel
%_includedir/%_name-%api_ver/
%_libdir/%name-%api_ver.so
%_pkgconfigdir/%_name-%api_ver.pc
%{?_enable_vala:%_vapidir/%_name-%api_ver.*}

%if_enabled introspection
%files gir
%_typelibdir/Shumate-%api_ver.typelib

%files gir-devel
%_girdir/Shumate-%api_ver.gir
%endif

%if_enabled gtk_doc
%files devel-doc
%_datadir/doc/%name-%api_ver/
%endif

%if_enabled demos
%files demo
%_bindir/%_name-demo
%endif

%changelog
* Thu Feb 09 2023 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt1.1
- fixed %%check for dbus >= 1.14.4

* Fri Dec 02 2022 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt1
- 1.0.3

* Sat Oct 22 2022 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Wed Sep 28 2022 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- updated to 1.0.1-5-ge819592

* Tue Sep 20 2022 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Thu Sep 01 2022 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.5.beta
- 1.0.0.beta

* Fri Jan 14 2022 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.1.alpha.1
- first build for sisyphus (1.0.0.alpha.1)

