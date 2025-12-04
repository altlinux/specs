%define _unpackaged_files_terminate_build 1
%define app_id io.github.tobagin.scramble
%define __name scramble

Name: scramble-adw
Version: 1.2.2
Release: alt1
Summary: Privacy-focused image metadata removal tool
Group: Graphics
License: GPL-3.0-or-later
Url: https://github.com/tobagin/scramble
Vcs: https://github.com/tobagin/scramble

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: vala
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: libgexiv2-0.16-devel

%description
Scramble is a modern, privacy-focused utility for viewing and removing
metadata from images. Built with GTK4 and LibAdwaita, it provides a clean,
intuitive interface with a responsive 50/50 layout for
efficient metadata inspection and removal.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %__name

%check
%meson_test

%files -f %__name.lang
%_bindir/%__name
%_desktopdir/%app_id.desktop
%_datadir/metainfo/%app_id.metainfo.xml
%_iconsdir/hicolor/scalable/apps/%app_id.svg
%_datadir/glib-2.0/schemas/%app_id.gschema.xml


%changelog
* Mon Dec 01 2025 Vladislav Petrukhin <vladp@altlinux.org> 1.2.2-alt1
- Initial build.

