# If you want to suggest changes, please send PR on
# https://altlinux.space/alt-gnome/ReadySet to altlinux branch 

%define _unpackaged_files_terminate_build 1

%define app_id org.altlinux.ReadySet
%define _libexecdir %_prefix/libexec

Name: ready-set
Version: 0.2.8
Release: alt1

Summary: The utility for configuring the system at the first start
License: GPL-3.0-or-later
Group: Other
Url: https://altlinux.space/alt-gnome/ReadySet
Vcs: https://altlinux.space/alt-gnome/ReadySet.git

Source: %name-%version.tar

Requires: accountsservice

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-systemd
BuildRequires: blueprint-compiler
BuildRequires: meson
BuildRequires: pkgconfig(accountsservice)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(gnome-desktop-4)
BuildRequires: pkgconfig(gtk4) >= 4.18
BuildRequires: pkgconfig(ibus-1.0)
BuildRequires: pkgconfig(libadwaita-1) >= 1.7
BuildRequires: pkgconfig(polkit-gobject-1)
BuildRequires: pkgconfig(pwquality)
BuildRequires: pkgconfig(systemd)
BuildRequires: vala

%description
%summary.

%prep
%setup

%build
%meson -Dusername=_greeter
%meson_build

%install
%meson_install

%find_lang %name

%check
%meson_test

%files -f %name.lang
%_libexecdir/%name
%_libexecdir/%name-set-root-password
%_datadir/polkit-1/rules.d/%app_id.rules
%_iconsdir/hicolor/*/apps/%app_id.svg
%_iconsdir/hicolor/*/apps/%app_id-symbolic.svg
%doc README.md

%changelog
* Thu Dec 11 2025 Anton Midyukov <antohami@altlinux.org> 0.2.8-alt1
- Initial build.
