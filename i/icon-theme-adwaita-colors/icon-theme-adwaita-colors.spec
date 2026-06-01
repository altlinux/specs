%def_disable snapshot
%define _name Adwaita-Colors
%define __name adwaita-colors

%define ver_major 2.6
%define beta %nil

%def_disable check

Name: icon-theme-%__name
Version: %ver_major
Release: alt1%beta

Summary: Adwaita Colors Icon Theme
License: GPL-3.0
Group: Graphical desktop/GNOME
Url: https://github.com/dpejoh/Adwaita-colors

Vcs: https://github.com/dpejoh/Adwaita-colors.git

BuildArch: noarch

Provides: %_name = %EVR

%if_disabled snapshot
Source: %url/archive/v%version/%_name-%version%beta.tar.gz
%else
Source: %_name-%version%beta.tar
%endif

Requires(pre): icon-theme-adwaita icon-theme-adwaita-legacy

BuildRequires: icon-theme-adwaita /usr/bin/gio

%description
Adwaita Colors enhances the Adwaita icon theme by integrating GNOME's
accent color feature, introduced in GNOME 47. This project ensures that
your Adwaita icons reflect the same accent color as your GNOME theme,
instead of the default blue, for a more cohesive and customized look.

%prep
%setup -n %_name-%version

%install
mkdir -p %buildroot/%_iconsdir
./setup -i -p %buildroot/%_iconsdir
ln -sf ../../../Adwaita/scalable/places/folder.svg %buildroot/%_iconsdir/Adwaita-blue/scalable/status/folder-open.svg

%files
%_iconsdir/Adwaita-*/
%doc README*

%changelog
* Tue May 19 2026 Yuri N. Sedunov <aris@altlinux.org> 2.6-alt1
- 2.6

* Sun Aug 31 2025 Yuri N. Sedunov <aris@altlinux.org> 2.5-alt1
- 2.5

* Wed Jun 25 2025 Yuri N. Sedunov <aris@altlinux.org> 2.4.2-alt1
- 2.4.2

* Mon Feb 10 2025 Yuri N. Sedunov <aris@altlinux.org> 2.4.1-alt1
- first build for Sisyphus (v2.4.1-8-gf153417)


