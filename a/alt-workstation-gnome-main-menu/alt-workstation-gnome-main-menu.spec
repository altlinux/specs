%define _unpackaged_files_terminate_build 1

Name: alt-workstation-gnome-main-menu
Version: 1.1.0
Release: alt1

Summary: Default GNOME Shell main menu layout for ALT Workstation
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://altlinux.space/alt-gnome/alt-workstation-gnome-main-menu
Vcs: https://altlinux.space/alt-gnome/alt-workstation-gnome-main-menu.git
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson

%description
Default GNOME Shell main menu layout configuration for ALT Workstation.
Sets up application categories and folder layout in the GNOME Shell
app picker using dconf database and GSchema override.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%_sysconfdir/dconf/db/local.d/01-app-folders
%_datadir/glib-2.0/schemas/10_%name.gschema.override
%_datadir/desktop-directories/X-ALT-Communication.directory
%_datadir/desktop-directories/X-ALT-Containers.directory
%_datadir/desktop-directories/X-ALT-Creative.directory
%_datadir/desktop-directories/X-ALT-Development.directory
%_datadir/desktop-directories/X-ALT-Office.directory
%_datadir/desktop-directories/X-ALT-RemoteAccess.directory
%_datadir/desktop-directories/X-ALT-Wine.directory
%doc README.md COPYING

%changelog
* Tue Apr 07 2026 Semen Fomchenkov <armatik@altlinux.org> 1.1.0-alt1
- Update to v1.1.0.

* Mon Apr 06 2026 Semen Fomchenkov <armatik@altlinux.org> 1.0.0-alt1
- Initial build.
