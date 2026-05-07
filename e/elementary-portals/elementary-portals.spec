%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname io.elementary.portals

%define _libexecdir %_prefix/libexec

Name: elementary-portals
Version: 8.2.0
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
BuildRequires: pkgconfig(accountsservice)
BuildRequires: pkgconfig(libadwaita-1)

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
%_datadir/glib-2.0/schemas/xdg-desktop-portal-pantheon.gschema.xml
%_datadir/xdg-desktop-portal/portals/pantheon.portal
%_datadir/metainfo/%{appname}.metainfo.xml
%exclude %_datadir/locale/zh_HANS/LC_MESSAGES/xdg-desktop-portal-pantheon.mo
%exclude %_datadir/locale/zh_HANT/LC_MESSAGES/xdg-desktop-portal-pantheon.mo

%changelog
* Thu May 07 2026 Nikolay Strelkov <snk@altlinux.org> 8.2.0-alt1
- New version 8.2.0.

* Sat Jan 24 2026 Nikolay Strelkov <snk@altlinux.org> 8.1.0-alt1
- New version 8.1.0.

* Sat Sep 20 2025 Nikolay Strelkov <snk@altlinux.org> 8.0.4-alt1
- Initial build for Sisyphus
