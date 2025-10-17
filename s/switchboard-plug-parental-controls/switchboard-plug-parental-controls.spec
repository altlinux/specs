%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname io.elementary.settings.screentime-limits

%define _libexecdir %_prefix/libexec

Name: switchboard-plug-parental-controls
Version: 8.0.1
Release: alt1

Summary: Switchboard Screen Time & Limits Plug
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/switchboard-plug-parental-controls

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala
BuildRequires(pre): rpm-macros-systemd

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(polkit-gobject-1)
BuildRequires: pkgconfig(granite-7)
BuildRequires: pkgconfig(flatpak)
BuildRequires: pkgconfig(malcontent-0)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(accountsservice)
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(switchboard-3)

%description
Manage Screen Time & Limits.
Settings plugin for managing Screen Time & Limits.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

mkdir -pv %buildroot/%_sysconfdir/xdg/autostart/
cp -v %buildroot%_desktopdir/pantheon-parental-controls-client.desktop %buildroot/%_sysconfdir/xdg/autostart/pantheon-parental-controls-client.desktop

%find_lang %appname

%check
%meson_test

%files -f %{appname}.lang
%doc COPYING README.md
%dir %_sysconfdir/pantheon-parental-controls
%_sysconfdir/pantheon-parental-controls/daemon.conf
%_sysconfdir/xdg/autostart/pantheon-parental-controls-client.desktop
%_bindir/pantheon-parental-controls-daemon
%_unitdir/pantheon-parental-controls.service
%_libdir/switchboard-3/system/libscreentime-limits.so
%_libexecdir/pantheon-parental-controls-client
%_desktopdir/pantheon-parental-controls-client.desktop
%_datadir/dbus-1/system-services/org.pantheon.ParentalControls.service
%_datadir/dbus-1/system.d/org.pantheon.ParentalControls.conf
%_iconsdir/hicolor/*/apps/%{appname}.svg
%_datadir/metainfo/%{appname}.metainfo.xml
%_datadir/polkit-1/actions/%{appname}.policy

%changelog
* Sun Sep 21 2025 Nikolay Strelkov <snk@altlinux.org> 8.0.1-alt1
- Initial build for Sisyphus
