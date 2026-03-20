%define _unpackaged_files_terminate_build 1
%define xdg_name com.vysp3r.ProtonPlus

%def_without check

Name: protonplus
Version: 0.5.17
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

%check
%__meson_test

%files -f %xdg_name.lang
%doc LICENSE.md
%doc README.md CONTRIBUTING.md CODE_OF_CONDUCT.md SECURITY.md
%_bindir/%name
%_datadir/metainfo/%xdg_name.metainfo.xml
%_desktopdir/%xdg_name.desktop
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_iconsdir/hicolor/*/apps/%xdg_name.png

%changelog
* Fri Mar 20 2026 Boris Yumankulov <boria138@altlinux.org> 0.5.17-alt1
- new version 0.5.17

* Wed Feb 11 2026 Boris Yumankulov <boria138@altlinux.org> 0.5.16-alt1
- new version 0.5.16

* Mon Jan 05 2026 Boris Yumankulov <boria138@altlinux.org> 0.5.15-alt1
- new version 0.5.15

* Mon Dec 22 2025 Boris Yumankulov <boria138@altlinux.org> 0.5.14-alt1
- new version 0.5.14

* Sun Oct 19 2025 Boris Yumankulov <boria138@altlinux.org> 0.5.13-alt1
- new version 0.5.13

* Tue Sep 09 2025 Boris Yumankulov <boria138@altlinux.org> 0.5.12-alt1
- new version 0.5.12

* Sun Jul 06 2025 Boris Yumankulov <boria138@altlinux.org> 0.5.8-alt1
- new version 0.5.8

* Thu Jun 19 2025 Boris Yumankulov <boria138@altlinux.org> 0.5.5-alt1
- new version 0.5.5

* Sat May 31 2025 Boris Yumankulov <boria138@altlinux.org> 0.4.31-alt1
- new version 0.4.31

* Fri May 23 2025 Boris Yumankulov <boria138@altlinux.org> 0.4.30-alt1
- new version 0.4.30

* Fri Mar 28 2025 Boris Yumankulov <boria138@altlinux.org> 0.4.27-alt1
- new version 0.4.27

* Sun Feb 16 2025 Boris Yumankulov <boria138@altlinux.org> 0.4.23-alt1
- new version 0.4.23

* Mon Oct 14 2024 Boris Yumankulov <boria138@altlinux.org> 0.4.20-alt1
- new version 0.4.20

* Thu Oct 03 2024 Boris Yumankulov <boria138@altlinux.org> 0.4.18-alt1
- new version 0.4.18

* Thu Jul 18 2024 Boris Yumankulov <boria138@altlinux.org> 0.4.11-alt1
- new version 0.4.11

* Sat May 25 2024 Boris Yumankulov <boria138@altlinux.org> 0.4.10-alt1
- Initial build for Sisyphus


