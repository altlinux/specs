%def_disable snapshot
%define _libexecdir %_prefix/libexec

%define ver_major 1.1
%define beta %nil
%define api_ver_major 1
%define api_ver %{api_ver_major}+

%def_disable bootstrap
%def_disable check

Name: glycin
Version: %ver_major.1
Release: alt1%beta

Summary: Glycin image library
License: MPL-2.0 OR LGPL-2.1-or-later
Group: Graphics
Url: https://gitlab.gnome.org/GNOME/glycin

Vcs: https://gitlab.gnome.org/GNOME/glycin.git

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version%beta.tar.xz
%else
Source: %name-%version%beta.tar
%endif
%{?_enable_snapshot:Source1: %name-%version-cargo.tar}

%define gtk_ver 4.12
%define cairo_ver 1.17
%define rsvg_ver 2.52.0
%define heif_ver 1.14.2
%define lcms_ver 2.14
%define seccomp_ver 2.5.0

BuildRequires(pre): rpm-macros-meson rpm-build-gir rpm-build-vala
BuildRequires: meson git rust-cargo
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(cairo) >= %cairo_ver
BuildRequires: pkgconfig(librsvg-2.0) >= %rsvg_ver
BuildRequires: pkgconfig(libheif) >= %heif_ver
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(libjxl)
BuildRequires: pkgconfig(lcms2) >= %lcms_ver
BuildRequires: pkgconfig(libseccomp) >= %seccomp_ver
BuildRequires: gobject-introspection-devel gir(Gtk) = 4.0
BuildRequires: vala-tools
BuildRequires: clang-devel

%description
Glycin image library allows to decode images into gdk::Texture
(https://gtk-rs.org/gtk4-rs/stable/latest/docs/gdk4/struct.Texture.html)
and to extract image metadata.

%package loaders
Summary: Glycin loaders for several formats
Group: Graphics

%description loaders
Glycin image library allows to decode images into gdk::Texture
(https://gtk-rs.org/gtk4-rs/stable/latest/docs/gdk4/struct.Texture.html)
and to extract image metadata.

This package provides modular image loaders for Glycin.

%package -n lib%name
Summary: Glycin shared library
Group: System/Libraries

%description -n lib%name
This package contains shared Glycin library.

%package -n lib%name-devel
Summary: Development files for Glycin library
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
This package contains development files for the Glycin library.

%package -n lib%name-gir
Summary: GObject introspection data for the Glycin library
Group: System/Libraries
Requires: lib%name = %EVR

%description -n lib%name-gir
GObject introspection data for the Glycin library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the Glycin library
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-devel = %EVR
Requires: lib%name-gir = %EVR

%description -n lib%name-gir-devel
GObject introspection devel data for the Glycin library.

%package -n lib%name-gtk4
Summary: Glycin-Gtk4 shared library
Group: System/Libraries
Requires: lib%name = %EVR

%description -n lib%name-gtk4
This package contains shared Glycin-Gtk4 library.

%package -n lib%name-gtk4-devel
Summary: Development files for Glycin-Gtk4 library
Group: Development/C
Requires: lib%name-gtk4 = %EVR
Requires: lib%name-devel = %EVR

%description -n lib%name-gtk4-devel
This package contains development files for the Glycin-Gtk4 library.

%package -n lib%name-gtk4-gir
Summary: GObject introspection data for the Glycin-Gtk4 library
Group: System/Libraries
Requires: lib%name-gtk4 = %EVR
Requires: lib%name-gir = %EVR

%description -n lib%name-gtk4-gir
GObject introspection data for the Glycin-Gtk4 library

%package -n lib%name-gtk4-gir-devel
Summary: GObject introspection devel data for the Glycin-Gtk4 library
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gtk4-devel = %EVR
Requires: lib%name-gtk4-gir = %EVR
Requires: lib%name-gir-devel = %EVR

%description -n lib%name-gtk4-gir-devel
GObject introspection devel data for the Glycin-Gtk4 library.

%prep
%setup -n %name-%version%beta %{?_enable_snapshot:%{?_disable_bootstrap:-a1}}
%{?_enable_bootstrap:
[ ! -d .cargo ] && mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

%build
%meson
%meson_build

%install
%meson_install

%check
%__meson_test

%files loaders
%_libexecdir/%name-loaders/%api_ver/glycin-heif
%_libexecdir/%name-loaders/%api_ver/glycin-jxl
%_libexecdir/%name-loaders/%api_ver/glycin-svg
%_libexecdir/%name-loaders/%api_ver/glycin-image-rs
%_datadir/%name-loaders/%api_ver/conf.d/glycin-heif.conf
%_datadir/%name-loaders/%api_ver/conf.d/glycin-jxl.conf
%_datadir/%name-loaders/%api_ver/conf.d/glycin-svg.conf
%_datadir/%name-loaders/%api_ver/conf.d/glycin-image-rs.conf
%doc README* NEWS

%files -n lib%name
%_libdir/lib%name-%api_ver_major.so.*

%files -n lib%name-devel
%_includedir/%name-%api_ver_major/%name.h
%_libdir/lib%name-%api_ver_major.so
%_pkgconfigdir/%name-%api_ver_major.pc
%_vapidir/lib%name-%api_ver_major.deps
%_vapidir/lib%name-%api_ver_major.vapi

%files -n lib%name-gir
%_typelibdir/Gly-%api_ver_major.typelib

%files -n lib%name-gir-devel
%_girdir/Gly-%api_ver_major.gir

%files -n lib%name-gtk4
%_libdir/lib%name-gtk4-%api_ver_major.so.*

%files -n lib%name-gtk4-devel
%_includedir/%name-gtk4-%api_ver_major/%name-gtk4.h
%_libdir/lib%name-gtk4-%api_ver_major.so
%_pkgconfigdir/%name-gtk4-%api_ver_major.pc
%_vapidir/lib%name-gtk4-%api_ver_major.deps
%_vapidir/lib%name-gtk4-%api_ver_major.vapi

%files -n lib%name-gtk4-gir
%_typelibdir/GlyGtk4-%api_ver_major.typelib

%files -n lib%name-gtk4-gir-devel
%_girdir/GlyGtk4-%api_ver_major.gir

%changelog
* Mon Sep 16 2024 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt1
- 1.1.1

* Sun Mar 31 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Sun Mar 17 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Tue Nov 14 2023 Yuri N. Sedunov <aris@altlinux.org> 0.1.2-alt1
- 0.1.2

* Thu Sep 14 2023 Yuri N. Sedunov <aris@altlinux.org> 0.1.0-alt1
- 0.1.0

* Sun Jul 02 2023 Yuri N. Sedunov <aris@altlinux.org> 0.1-alt0.1.alpha
- first build for Sisyphus


