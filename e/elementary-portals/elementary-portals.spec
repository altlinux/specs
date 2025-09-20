%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname io.elementary.portals

%define _libexecdir %_prefix/libexec

Name: elementary-portals
Version: 8.0.4
Release: alt1

Summary: Flatpak portals for Pantheon
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/portals

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(granite-7)
BuildRequires: pkgconfig(pantheon-wayland-1)

%description
An implementation of XDG Flatpak portals for elementary OS and
Pantheon

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name --all-name

%check
%meson_test

%files -f %name.lang
%doc COPYING README.md
%_userunitdir/xdg-desktop-portal-pantheon.service
%_libexecdir/xdg-desktop-portal-pantheon
%_datadir/dbus-1/services/org.freedesktop.impl.portal.desktop.pantheon.service
%_datadir/xdg-desktop-portal/portals/pantheon.portal
%_datadir/metainfo/%{appname}.metainfo.xml

%changelog
* Sat Sep 20 2025 Nikolay Strelkov <snk@altlinux.org> 8.0.4-alt1
- Initial build for Sisyphus
