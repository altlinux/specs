%define _unpackaged_files_terminate_build 1

Name: elementary-session-settings
Version: 8.1.0
Release: alt1.git.0a69481

Summary: Session settings for elementary OS
License: GPL-2.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/session-settings

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-systemd

BuildRequires: meson
BuildRequires: cmake
BuildRequires: pkgconfig(gnome-settings-daemon)
BuildRequires: pkgconfig(systemd)
BuildRequires: /usr/bin/gnome-keyring-daemon
BuildRequires: /usr/bin/onboard
BuildRequires: /usr/bin/orca

Requires: gala
Requires: /usr/bin/gnome-session
Requires: wingpanel
Requires: gnome-settings-daemon
Requires: gnome-keyring
Requires: gcr4
Requires: orca
Requires: elementary-settings-daemon

BuildArch: noarch

%description
%summary

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc LICENSE README.md
%_userunitdir/gnome-session@pantheon-wayland.target.d/session.conf
%_userunitdir/gnome-session@pantheon.target.d/session.conf
%_desktopdir/pantheon-mimeapps.list
%_datadir/gnome-session/sessions/pantheon-wayland.session
%_datadir/wayland-sessions/pantheon-wayland.desktop

%changelog
* Mon Apr 07 2026 Nikolay Strelkov <snk@altlinux.org> 8.1.0-alt1.git.0a69481
- Initial build for Sisyphus
