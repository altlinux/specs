# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1
%define uuid xwayland-indicator@swsnr.de

Name: gnome-shell-extension-xwayland-indicator
Version: 50.1
Release: alt1
Summary: Determine whether a window in GNOME uses xwayland
License: EUPL-1.2
Group: Graphical desktop/GNOME
URL: https://codeberg.org/swsnr/gnome-shell-extension-xwayland-indicator
VCS: https://codeberg.org/swsnr/gnome-shell-extension-xwayland-indicator.git
Source0: %name-%version.tar
Source1: node-modules.tar

BuildArch: noarch

BuildRequires: just
BuildRequires: node

Requires: gnome-shell >= 50

%description
This small GNOME extension shows the X11 logo in the panel if the current session
uses X11 instead of wayland or if the currently focused window used xwayland.

%prep
%setup -a1
%autopatch -p1

%build
just tsc='node_modules/.bin/tsc' build

%install
mkdir -p %buildroot%_datadir/gnome-shell/extensions/%uuid
cp -a build/. %buildroot%_datadir/gnome-shell/extensions/%uuid/
cp -a icons %buildroot%_datadir/gnome-shell/extensions/%uuid/

%files
%_datadir/gnome-shell/extensions/%uuid
%doc README.md LICENSE

%changelog
* Sun Jul 26 2026 Dmitry Udalov <udalov@altlinux.org> 50.1-alt1
- Update to 50.1
- License changed to EUPL-1.2

* Wed May 07 2025 Anton Midyukov <antohami@altlinux.org> 48.5-alt1
- initial build
