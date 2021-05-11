%def_enable snapshot
%define ver_major 1.1
%define api_ver 1

%def_enable introspection
%def_enable vala
%def_enable gtk_doc
%def_enable check

Name: libadwaita
Version: %ver_major.0
Release: alt0.1

Summary: Library with GTK4 widgets for mobile devices
Group: System/Libraries
License: LGPL-2.1-or-later
Url: https://gitlab.gnome.org/GNOME/libadwaita

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
#Source: %url/-/archive/%version/%name-%version.tar.bz2
%else
Vcs: https://gitlab.gnome.org/GNOME/libadwaita.git
# 3b8fce9 (no tags)
Source: %name-%version.tar
%endif

%define glib_ver 2.44
%define gtk_ver 4.2.1

BuildRequires(pre): meson rpm-build-gir
BuildRequires: sassc
BuildRequires: pkgconfig(gio-2.0) >= %glib_ver
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
%{?_enable_introspection:BuildRequires: pkgconfig(gobject-introspection-1.0) gir(Gtk) = 4.0}
%{?_enable_vala:BuildRequires: vala-tools}
%{?_enable_gtk_doc:BuildRequires: gtk-doc}
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

%prep
%setup -n %name-%version

%build
%meson \
	-Dgtk_doc=true \
	-Dexamples=false
%meson_build

%install
%meson_install
%find_lang %name

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
xvfb-run -s -noreset %meson_test

%files -f %name.lang
%_libdir/%name-%api_ver.so.*
%doc README.md

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
%_datadir/gtk-doc/html/%name-%api_ver/
%endif

%changelog
* Tue May 04 2021 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt0.1
- first build for sisyphus

