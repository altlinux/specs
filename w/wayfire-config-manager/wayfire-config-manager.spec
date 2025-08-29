# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: wayfire-config-manager
Version: 0.10.0
Release: alt1
Summary: Wayfire Config Manager
License: MIT
Group: Graphical desktop/Other
Url: https://github.com/WayfireWM/wcm
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: meson
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: libglm-devel
BuildRequires: libevdev-devel
BuildRequires: libxkbcommon-devel
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gtkmm-3.0)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(wayfire)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wf-config) >= 0.10.0
BuildRequires: pkgconfig(wf-shell) >= 0.10.0

Requires: hicolor-icon-theme

%description
%summary.

%prep
%setup
%patch -p1

%build
%meson
%meson_build

%install
%meson_install

%check
desktop-file-validate %buildroot%_desktopdir/*.desktop

%files
%doc LICENSE
%_bindir/wcm
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*.svg
%_datadir/wcm/

%changelog
* Fri Aug 29 2025 Anton Midyukov <antohami@altlinux.org> 0.10.0-alt1
- New version 0.10.0.

* Fri Nov 29 2024 Anton Midyukov <antohami@altlinux.org> 0.9.0-alt2
- fix mistake with new line escaping before %%meson_build macro

* Sat Oct 12 2024 Anton Midyukov <antohami@altlinux.org> 0.9.0-alt1
- initial build
