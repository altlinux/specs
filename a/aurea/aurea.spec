%define xdg_name io.github.cleomenezesjr.aurea

Name: aurea
Version: 1.4
Release: alt1

Summary: Simple preview banner made to read metainfo files from Flatpak apps and represent them as they would on Flathub
License: GPL-3.0
Group: File tools

Url: https://github.com/CleoMenezesJr/Aurea
# Source-url: https://github.com/CleoMenezesJr/Aurea/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

%define gtk4_ver 4.5.0
%define adwaita_ver 1.2
%define soup3_ver 3.2.0

Requires: typelib(Gtk) = 4.0
Requires: typelib(Adw) = 1
Requires: typelib(Soup) = 3.0
Requires: python3(PIL)

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson blueprint-compiler libgio-devel

BuildRequires: libgtk4-gir-devel >= %gtk4_ver
BuildRequires: libadwaita-gir-devel >= %adwaita_ver

%description
%summary

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome  %name

%files -f %name.lang
%attr(755,root,root) %_bindir/%name
%_datadir/%name/
%_desktopdir/%xdg_name.desktop
%_iconsdir/hicolor/*/apps/*.svg
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/metainfo/%xdg_name.metainfo.xml

%changelog
* Mon Jun 03 2024 Boris Yumankulov <boria138@altlinux.org> 1.4-alt1
- initial build for ALT Sisyphus

