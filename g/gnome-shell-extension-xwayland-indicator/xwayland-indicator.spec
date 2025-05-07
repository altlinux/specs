# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: gnome-shell-extension-xwayland-indicator
Version: 48.5
Release: alt1
Summary: Determine whether a window in GNOME uses xwayland
License: MPL-2.0 OR GPL-2.0-or-later
Group: Graphical desktop/GNOME
URL: https://codeberg.org/swsnr/gnome-shell-extension-xwayland-indicator
VCS: https://codeberg.org/swsnr/gnome-shell-extension-xwayland-indicator.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

%description
This small GNOME extension shows the X11 logo in the panel if the current session
uses X11 instead of wayland or if the currently focused window used xwayland.

%prep
%setup
%autopatch -p1

%install
mkdir -p %buildroot%_datadir/gnome-shell/extensions/xwayland-indicator@swsnr.de
install -m644 extension.js %buildroot%_datadir/gnome-shell/extensions/xwayland-indicator@swsnr.de
install -m644 metadata.json %buildroot%_datadir/gnome-shell/extensions/xwayland-indicator@swsnr.de
cp -a icons %buildroot%_datadir/gnome-shell/extensions/xwayland-indicator@swsnr.de

%files
%_datadir/gnome-shell/extensions/xwayland-indicator@swsnr.de
%doc README.md LICENSE-GPL2 LICENSE-MPL2

%changelog
* Wed May 07 2025 Anton Midyukov <antohami@altlinux.org> 48.5-alt1
- initial build
