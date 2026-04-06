%define _unpackaged_files_terminate_build 1

Name: alt-workstation-gnome-main-menu
Version: 1.0.0
Release: alt1

Summary: Default GNOME Shell main menu layout for ALT Workstation
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://altlinux.space/alt-gnome/alt-workstation-gnome-main-menu
Vcs: https://altlinux.space/alt-gnome/alt-workstation-gnome-main-menu.git
Source: %name-%version.tar

BuildArch: noarch

Requires: foldy
Requires: gnome-shell
Requires: bash

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson

%description
Default GNOME Shell main menu layout configuration for ALT Workstation.
On first login the package automatically sets up application categories
and positions in the GNOME Shell app picker using Foldy.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%_bindir/%name-setup
%_datadir/%name/
%_sysconfdir/xdg/autostart/%name.desktop
%doc README.md COPYING

%changelog
* Sun Apr 06 2026 Semen Fomchenkov <armatik@altlinux.org> 1.0.0-alt1
- Initial build.
