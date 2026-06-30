%define _unpackaged_files_terminate_build 1
%define oname io.github.tanaybhomia.Whisp

Name: whisp
Version: 1.3.6
Release: alt1

Summary: The Anti-Note for GNOME
License: GPL-3.0-or-later
Group: Editors

Url: https://tanaybhomia.github.io/Whisp
Vcs: https://github.com/tanaybhomia/Whisp

BuildArch: noarch
AutoProv: nopython3

Source: %name-%version.tar

%add_python3_path %_datadir/%name/%name

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson pkgconfig(gtk4) pkgconfig(libadwaita-1) typelib(Adw)

%description
A fluid, gesture-driven scratchpad designed for absolute speed.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc *.md
%_bindir/%name
%_desktopdir/%oname.desktop
%_iconsdir/hicolor/*/apps/*.svg
%_datadir/metainfo/%oname.*
%_datadir/%name

%changelog
* Tue Jun 30 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.3.6-alt1
- Initial build for ALT Linux.

