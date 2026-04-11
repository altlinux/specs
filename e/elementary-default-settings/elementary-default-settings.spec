%define _unpackaged_files_terminate_build 1

Name: elementary-default-settings
Version: 8.1.1
Release: alt1

Summary: Default settings for elementary OS
License: GPL-2.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/default-settings

Source: %name-%version.tar

BuildRequires(pre): meson

BuildRequires: cmake
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(polkit-gobject-1)
BuildRequires: pkgconfig(accountsservice)

BuildArch: noarch

%description
This package contains various system defaults for elementary OS.
Installing this package won't affect existing users on your system.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc LICENSE README.md
%config(noreplace) %_sysconfdir/NetworkManager/conf.d/10-globally-managed-devices.conf
%config(noreplace) %_sysconfdir/geoclue/conf.d/99-beacondb.conf
%config(noreplace) %_sysconfdir/gtk-4.0/settings.ini
%config(noreplace) %_sysconfdir/netplan/01-network-manager-all.yml
%config(noreplace) %_sysconfdir/skel/.inputrc
%config(noreplace) %_sysconfdir/skel/.local/share/flatpak/repo/appcenter.trustedkeys.gpg
%config(noreplace) %_sysconfdir/skel/.local/share/flatpak/repo/config
%config(noreplace) %_sysconfdir/skel/.local/share/flatpak/repo/flathub.trustedkeys.gpg
%config(noreplace) %_sysconfdir/sudoers.d/pwfeedback
%_datadir/accountsservice/interfaces/io.elementary.pantheon.AccountsService.xml
%_datadir/apparmor/extra-profiles/bwrap-userns-restrict-patched
%exclude %_desktopdir/sessioninstaller.desktop
%exclude %_datadir/cups/data/default-testpage.pdf
%_datadir/dbus-1/interfaces/io.elementary.pantheon.AccountsService.xml
%_datadir/glib-2.0/schemas/default-settings.gschema.override
%_datadir/polkit-1/actions/io.elementary.pantheon.AccountsService.policy
%_datadir/xdg-desktop-portal/pantheon-portals.conf

%changelog
* Sat Apr 11 2026 Nikolay Strelkov <snk@altlinux.org> 8.1.1-alt1
- Initial build for Sisyphus
