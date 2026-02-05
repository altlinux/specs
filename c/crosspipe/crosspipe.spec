%define _unpackaged_files_terminate_build 1

Name: crosspipe
Version: 0.1.1
Release: alt1

Summary: Graphical PipeWire connections manager
License: GPL-3.0-only
Group: Sound
Url: https://github.com/dp0sk/Crosspipe

Source: %name-%version.tar

BuildRequires(pre): rpm-build-vala
BuildRequires(pre): rpm-macros-meson

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(libpipewire-0.3)
BuildRequires: pkgconfig(libxml-2.0)

Requires: pipewire

%description
Crosspipe is a visual graph manager for PipeWire, built with
GTK4/Libadwaita and Vala, following the GNOME HIG.

Features:

* Visual graph of PipeWire nodes and connections
* Drag-and-drop connection management
* Native GTK4/Libadwaita interface, following GNOME HIG

%prep
%setup
sed -i "s|https://raw.githubusercontent.com/dp0sk/Crosspipe/refs/heads/main/data/icons|%_iconsdir|" README.md
sed -i "s|https://raw.githubusercontent.com/dp0sk/Crosspipe/refs/heads/main/data/||g" README.md

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md data/screenshot-light.png data/screenshot-dark.png
%_bindir/crosspipe
%_desktopdir/io.github.dp0sk.Crosspipe.desktop
%_datadir/glib-2.0/schemas/io.github.dp0sk.Crosspipe.gschema.xml
%_iconsdir/hicolor/scalable/apps/io.github.dp0sk.Crosspipe.svg
%_datadir/metainfo/io.github.dp0sk.Crosspipe.metainfo.xml

%changelog
* Thu Feb 05 2026 Nikolay Strelkov <snk@altlinux.org> 0.1.1-alt1
- Initial build for Sisyphus
