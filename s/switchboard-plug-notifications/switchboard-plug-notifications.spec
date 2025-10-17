%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname io.elementary.settings.notifications

Name: switchboard-plug-notifications
Version: 8.0.0
Release: alt1

Summary: Switchboard Notifications Plug
License: GPL-2.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/settings-notifications

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(switchboard-3)

%description
Change notification settings.
Switchboard plug for controlling Pantheon's notifications.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%find_lang %appname

%check
%meson_test

%files -f %{appname}.lang
%doc COPYING README.md
%_libdir/switchboard-3/personal/libnotifications.so
%_datadir/metainfo/io.elementary.settings.notifications.metainfo.xml

%changelog
* Sun Sep 21 2025 Nikolay Strelkov <snk@altlinux.org> 8.0.0-alt1
- Initial build for Sisyphus
