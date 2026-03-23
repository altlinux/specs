%define app_id org.altlinux.gnome-legacy-theme-switcher
%define _unpackaged_files_terminate_build 1

Name: gnome-legacy-theme-switcher
Version: 0.1.3
Release: alt2

Summary: A service that applies dark gnome theme to "legacy" applications
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://altlinux.space/alt-gnome/gnome-legacy-theme-switcher
Vcs: https://altlinux.space/alt-gnome/gnome-legacy-theme-switcher
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: libgio

BuildArch: noarch

%description
%name allows to select light and dark gtk-theme variants
to sync with dark/light mode in gnome.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%post
%systemd_user_post %name.service

%preun
%systemd_user_preun %name.service

%files
%_bindir/%name
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%_user_unitdir/%name.service
%_user_unitdir/gnome-session@gnome.target.d/%name.conf

%changelog
* Mon Mar 23 2026 Michael Shigorin <mike@altlinux.org> 0.1.3-alt2
- Fix build --without check.
- Drop useless %%def_enable check.
- Minor spec cleanup.

* Tue Mar 10 2026 Vladislav Petrukhin <vladp@altlinux.org> 0.1.3-alt1
- New version 0.1.3.

* Fri Jun 06 2025 Semen Fomchenkov <armatik@altlinux.org> 0.1.2-alt1
- Initial build. (thx parovoz@alt)

