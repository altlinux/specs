%define app_id org.altlinux.gnome-legacy-theme-switcher
%def_enable check
%define _unpackaged_files_terminate_build 1

Name: gnome-legacy-theme-switcher
Version: 0.1.2
Release: alt1

Summary: A service, that applies gnome dark theme to "legacy" applications
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://altlinux.space/alt-gnome/gnome-legacy-theme-switcher
Vcs: https://altlinux.space/alt-gnome/gnome-legacy-theme-switcher

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
%if_enabled check
BuildRequires: libgio
%endif

BuildArch: noarch

%description
%name allows you to select light and dark gtk-theme variants to sync with dark/light mode in gnome.

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
%_libexecdir/systemd/user/%name.service
%_libexecdir/systemd/user/gnome-session@gnome.target.d/%name.conf

%changelog
* Fri Jun 06 2025 Semen Fomchenkov <armatik@altlinux.org> 0.1.2-alt1
- Initial build. (thx parovoz@alt)

