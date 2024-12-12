Name: alt-panelmoded
Version: 0.3.3
Release: alt1

Summary: Used for panelmode on operating systems of the Alt family with GNOME desktop enviroment
License: GPL-3.0-later
Group: Graphical desktop/GNOME

Url: https://gitlab.gnome.org/Armatik/alt-panelmoded
Vcs: https://gitlab.gnome.org/Armatik/alt-panelmoded
Source: %name-%version.tar

Requires: dconf
Requires: gnome-shell-extension-dash-to-panel

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-systemd
BuildRequires: meson
BuildRequires: vala
BuildRequires: pkgconfig(gio-2.0)

%description
Used for panelmode on operating systems of the Alt family with GNOME desktop
enviroment.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%post
%systemd_user_post %name.service

%preun
%systemd_user_preun %name.service

%files -f %name.lang
%_bindir/%name
%_user_unitdir/%name.service
%_datadir/%name
%_datadir/glib-2.0/schemas/org.altlinux.%name.gschema.xml
%_user_presetdir/20-%name.preset
%_desktopdir/org.altlinux.panelmoded.desktop

%changelog
* Thu Dec 12 2024 Oleg Shchavelev <oleg@altlinux.org> 0.3.3-alt1
- Initial build
