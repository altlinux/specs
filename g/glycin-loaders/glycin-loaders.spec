%def_disable snapshot
%define _libexecdir %_prefix/libexec

%define ver_major 0.1
%define beta %nil
%define api_ver 0+

%def_disable bootstrap

Name: glycin-loaders
Version: %ver_major.0
Release: alt1%beta

Summary: Glycin loaders for several formats
License: MPL-2.0 OR LGPL-2.1-or-later
Group: Graphics
Url: https://gitlab.gnome.org/Incubator/loupe

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version%beta.tar.xz
%else
Vcs: https://gitlab.gnome.org/Incubator/loupe.git
Source: %name-%version%beta.tar
%endif
Source1: %name-%version-cargo.tar

%define gtk_ver 4.11.3
%define heif_ver 1.14.2

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson git rust-cargo
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libheif) >= %heif_ver
BuildRequires: pkgconfig(libxml-2.0)

%description
Glycin image library allows to decode images into gdk::Texture
(https://gtk-rs.org/gtk4-rs/stable/latest/docs/gdk4/struct.Texture.html)
and to extract image metadata.

This package provides modular image loaders for Glycin.

%prep
%setup -n %name-%version%beta %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
[ ! -d .cargo ] && mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

%build
%meson
%meson_build

%install
%meson_install

%files
%_libexecdir/%name/%api_ver/glycin-heif
%_libexecdir/%name/%api_ver/glycin-jxl
%_libexecdir/%name/%api_ver/glycin-svg
%_libexecdir/%name/%api_ver/glycin-image-rs
%_datadir/%name/%api_ver/conf.d/glycin-heif.conf
%_datadir/%name/%api_ver/conf.d/glycin-jxl.conf
%_datadir/%name/%api_ver/conf.d/glycin-svg.conf
%_datadir/%name/%api_ver/conf.d/glycin-image-rs.conf
%doc README*


%changelog
* Thu Sep 14 2023 Yuri N. Sedunov <aris@altlinux.org> 0.1.0-alt1
- 0.1.0

* Sun Jul 02 2023 Yuri N. Sedunov <aris@altlinux.org> 0.1-alt0.1.alpha
- first build for Sisyphus


