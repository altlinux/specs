%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define _libexecdir %_prefix/libexec

%define appname io.elementary.settings-daemon

Name: elementary-settings-daemon
Version: 8.4.0
Release: alt1

Summary: Keep session settings in sync
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/settings-daemon

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala
BuildRequires(pre): rpm-macros-systemd

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(fwupd)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gexiv2)
BuildRequires: pkgconfig(packagekit-glib2)
BuildRequires: pkgconfig(libgeoclue-2.0)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(accountsservice)
BuildRequires: pkgconfig(systemd)
BuildRequires: vapi(granite)

%description
elementary Settings Daemon keeps settings in sync between session
components

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
%doc LICENSE README.md
%_sysconfdir/xdg/autostart/%{appname}.desktop
%_bindir/%appname
%_libexecdir/%{appname}.xdg-desktop-portal
%_unitdir/%{appname}.check-for-firmware-updates.service
%_unitdir/%{appname}.check-for-firmware-updates.timer
%_userunitdir/%{appname}.xdg-desktop-portal.service
%_userunitdir/%{appname}.system-update.service
%_userunitdir/%{appname}.system-update.timer
%_datadir/accountsservice/interfaces/io.elementary.SettingsDaemon.AccountsService.xml
%_desktopdir/%{appname}.desktop
%_datadir/dbus-1/interfaces/io.elementary.SettingsDaemon.AccountsService.xml
%_datadir/dbus-1/services/org.freedesktop.impl.portal.desktop.elementary.settings-daemon.service
%_datadir/glib-2.0/schemas/%{appname}.gschema.xml
%_datadir/metainfo/%{appname}.metainfo.xml
%_datadir/xdg-desktop-portal/portals/%{appname}.portal
%exclude %_datadir/locale/zh_HANS/LC_MESSAGES/io.elementary.settings-daemon.mo
%exclude %_datadir/locale/zh_HANT/LC_MESSAGES/io.elementary.settings-daemon.mo

%changelog
* Fri Nov 28 2025 Nikolay Strelkov <snk@altlinux.org> 8.4.0-alt1
- New version 8.4.0.

* Sun Sep 21 2025 Nikolay Strelkov <snk@altlinux.org> 8.3.1-alt1
- Initial build for Sisyphus
