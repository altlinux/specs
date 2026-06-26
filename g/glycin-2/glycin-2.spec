%def_disable snapshot
%define _libexecdir %_prefix/libexec

%define _name glycin
%define ver_major 2.1
%define beta %nil
%define namespace Gly
%define api_ver_major 2
%define api_ver %{api_ver_major}+

%def_enable thumbnailer

%def_disable bootstrap
%def_disable check

Name: %_name-%api_ver_major
Version: %ver_major.5
Release: alt1%beta

Summary: Glycin image library
License: MPL-2.0 OR LGPL-2.1-or-later
Group: Graphics
Url: https://gitlab.gnome.org/GNOME/glycin

Vcs: https://gitlab.gnome.org/GNOME/glycin.git

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version%beta.tar.xz
%else
Source: %_name-%version%beta.tar
%endif
Source1: %_name-%version%beta-cargo.tar

%define gtk_ver 4.16
%define cairo_ver 1.17
%define rsvg_ver 2.52.0
%define heif_ver 1.17.0
%define jxl_ver 0.11.1
%define lcms_ver 2.14
%define seccomp_ver 2.5.0

BuildRequires(pre): rpm-macros-meson rpm-build-gir rpm-build-vala
BuildRequires: meson git rust-cargo
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(cairo) >= %cairo_ver
BuildRequires: pkgconfig(librsvg-2.0) >= %rsvg_ver
BuildRequires: pkgconfig(libheif) >= %heif_ver
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(libjxl) >= %jxl_ver
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
%setup -n %_name-%version%beta %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
[ ! -d .cargo ] && mkdir .cargo
cargo vendor -s glycin-dev-tools/Cargo.toml | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%_name-%version%beta-cargo.tar .cargo/ vendor/}

%build
%meson \
    %{subst_enable_meson_bool thumbnailer %_name-thumbnailer}
%nil
%meson_build

%install
%meson_install

%check
%__meson_test

%files loaders
%{?_enable_thumbnailer:%_bindir/%_name-thumbnailer}
%_libexecdir/%_name-loaders/%api_ver/glycin-heif
%_libexecdir/%_name-loaders/%api_ver/glycin-jxl
%_libexecdir/%_name-loaders/%api_ver/glycin-svg
%_libexecdir/%_name-loaders/%api_ver/glycin-image-rs
%_datadir/%_name-loaders/%api_ver/conf.d/glycin-heif.conf
%_datadir/%_name-loaders/%api_ver/conf.d/glycin-jxl.conf
%_datadir/%_name-loaders/%api_ver/conf.d/glycin-svg.conf
%_datadir/%_name-loaders/%api_ver/conf.d/glycin-image-rs.conf
%{?_enable_thumbnailer:
%_datadir/thumbnailers/%_name-heif.thumbnailer
%_datadir/thumbnailers/%_name-image-rs.thumbnailer
%_datadir/thumbnailers/%_name-jxl.thumbnailer
%_datadir/thumbnailers/%_name-svg.thumbnailer}
%doc README* NEWS

%files -n lib%name
%_libdir/lib%_name-%api_ver_major.so.*

%files -n lib%name-devel
%_includedir/%_name-%api_ver_major/%_name.h
%_libdir/lib%_name-%api_ver_major.so
%_pkgconfigdir/%_name-%api_ver_major.pc
%_vapidir/%_name-%api_ver_major.deps
%_vapidir/%_name-%api_ver_major.vapi

%files -n lib%name-gir
%_typelibdir/%namespace-%api_ver_major.typelib

%files -n lib%name-gir-devel
%_girdir/%namespace-%api_ver_major.gir

%files -n lib%name-gtk4
%_libdir/lib%_name-gtk4-%api_ver_major.so.*

%files -n lib%name-gtk4-devel
%_includedir/%_name-gtk4-%api_ver_major/%_name-gtk4.h
%_libdir/lib%_name-gtk4-%api_ver_major.so
%_pkgconfigdir/%_name-gtk4-%api_ver_major.pc
%_vapidir/%_name-gtk4-%api_ver_major.deps
%_vapidir/%_name-gtk4-%api_ver_major.vapi

%files -n lib%name-gtk4-gir
%_typelibdir/%{namespace}Gtk4-%api_ver_major.typelib

%files -n lib%name-gtk4-gir-devel
%_girdir/%{namespace}Gtk4-%api_ver_major.gir

%changelog
* Fri Jun 26 2026 Yuri N. Sedunov <aris@altlinux.org> 2.1.5-alt1
- 2.1.5

* Tue Mar 24 2026 Yuri N. Sedunov <aris@altlinux.org> 2.1.1-alt1
- 2.1.1

* Fri Mar 13 2026 Yuri N. Sedunov <aris@altlinux.org> 2.1.0-alt1
- 2.1.0

* Wed Feb 11 2026 Yuri N. Sedunov <aris@altlinux.org> 2.0.8-alt1
- 2.0.8

* Wed Nov 12 2025 Yuri N. Sedunov <aris@altlinux.org> 2.0.7-alt1
- 2.0.7

* Wed Nov 05 2025 Yuri N. Sedunov <aris@altlinux.org> 2.0.5-alt1
- 2.0.5

* Tue Oct 21 2025 Yuri N. Sedunov <aris@altlinux.org> 2.0.4-alt1
- 2.0.4

* Mon Oct 13 2025 Yuri N. Sedunov <aris@altlinux.org> 2.0.3-alt1
- 2.0.3

* Sun Sep 28 2025 Yuri N. Sedunov <aris@altlinux.org> 2.0.2-alt1
- 2.0.2

* Fri Sep 12 2025 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1
- 2.0.0

* Sat Aug 02 2025 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt1
- 1.2.3

* Sat Jun 28 2025 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt1
- 1.2.2

* Fri Apr 11 2025 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- 1.2.1

* Sat Mar 15 2025 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Fri Feb 28 2025 Yuri N. Sedunov <aris@altlinux.org> 1.1.6-alt1
- 1.1.6

* Tue Feb 25 2025 Yuri N. Sedunov <aris@altlinux.org> 1.1.5-alt1
- 1.1.5

* Sat Jan 04 2025 Yuri N. Sedunov <aris@altlinux.org> 1.1.4-alt1
- 1.1.4

* Sat Nov 23 2024 Yuri N. Sedunov <aris@altlinux.org> 1.1.2-alt1
- 1.1.2

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


