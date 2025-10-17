%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname io.elementary.settings.useraccounts

Name: switchboard-plug-useraccounts
Version: 8.0.1
Release: alt1

Summary: Switchboard User Accounts Plug
License: LGPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/settings-useraccounts

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(switchboard-3)
BuildRequires: pkgconfig(polkit-gobject-1)
BuildRequires: pkgconfig(accountsservice)
BuildRequires: pkgconfig(gnome-desktop-4)
BuildRequires: pkgconfig(pwquality)

%description
Manage local user accounts.
elementary Settings plugin for managing local user accounts

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
%doc COPYING COPYRIGHT README.md
%_libdir/switchboard-3/system/libuseraccounts.so
%_libdir/switchboard-3/system/useraccounts/guest-session-toggle
%_datadir/metainfo/%{appname}.metainfo.xml
%_datadir/polkit-1/actions/%{appname}.policy

%changelog
* Sun Sep 21 2025 Nikolay Strelkov <snk@altlinux.org> 8.0.1-alt1
- Initial build for Sisyphus
