%def_without check

%define xdg_name com.vysp3r.ProtonPlus

Name: protonplus
Version: 0.4.11
Release: alt1

Summary: Simple and powerful manager for Wine, Proton, DXVK and VKD3D
License: GPL-3.0
Group: Games/Other

Url: https://github.com/Vysp3r/ProtonPlus
# Source-url: https://github.com/Vysp3r/ProtonPlus/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson vala
BuildRequires: /proc

BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libadwaita-1) >= 1.4
BuildRequires: pkgconfig(libarchive)
BuildRequires: pkgconfig(libsoup-3.0)

%{?!_without_check:%{?!_disable_check:BuildRequires: %_bindir/appstream-util %_bindir/desktop-file-validate}}

%description
ProtonPlus is a simple and powerful manager for:
 - Wine
 - Proton
 - DXVK
 - VKD3D
 - Several other runners

Supports Steam, Lutris, Heroic and Bottles.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %xdg_name

ln -s %xdg_name %buildroot%_bindir/%name

%check
%__meson_test

%files -f %xdg_name.lang
%doc LICENSE.md
%doc README.md CONTRIBUTING.md CODE_OF_CONDUCT.md SECURITY.md
%_bindir/%name
%_bindir/%xdg_name
%_datadir/appdata/%xdg_name.appdata.xml
%_desktopdir/%xdg_name.desktop
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_iconsdir/hicolor/*/apps/%xdg_name.svg

%changelog
* Thu Jul 18 2024 Boris Yumankulov <boria138@altlinux.org> 0.4.11-alt1
- new version 0.4.11

* Sat May 25 2024 Boris Yumankulov <boria138@altlinux.org> 0.4.10-alt1
- Initial build for Sisyphus


