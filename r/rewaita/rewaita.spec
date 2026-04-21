%def_disable snapshot

%define _name rewaita
%define __name Rewaita
%define ver_major 1.1
%define rdn_name io.github.swordpuffin.%_name

%def_enable check

Name: %_name
Version: %ver_major.2
Release: alt1

Summary: GNOME colors customizer
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://github.com/SwordPuffin/Rewaita

BuildArch: noarch

Vcs: https://github.com/SwordPuffin/Rewaita.git

%if_disabled snapshot
Source: https://github.com/SwordPuffin/Rewaita/archive/v%version/%_name-%version.tar.gz
%else
Source: %__name-%version.tar
%endif

%add_python3_path %_datadir/%_name

Requires: python3-module-pygobject3
Requires: typelib(Adw) = 1
Requires: typelib(GtkSource) = 5
Requires: typelib(Xdp) = 1.0
Requires: dconf

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson /usr/bin/glib-compile-resources
BuildRequires: gtk4-update-icon-cache
%{?_enable_check:BuildRequires: /usr/bin/desktop-file-validate /usr/bin/appstreamcli
BuildRequires: /usr/bin/glib-compile-schemas}

%description
Rewaita gives your Adwaita apps a fresh look by tinting them with
popular color schemes.

%prep
%setup -n %__name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%check
%__meson_test

%files -f %name.lang
%attr(0755,root,root) %_bindir/%name
%_datadir/%name/
%_desktopdir/%rdn_name.desktop
%_datadir/icons/hicolor/*/*/*.svg
%_datadir/dbus-1/services/%rdn_name.service
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README.*

%changelog
* Tue Apr 21 2026 Yuri N. Sedunov <aris@altlinux.org> 1.1.2-alt1
- 1.1.2

* Mon Jan 12 2026 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt1
- 1.1.1

* Tue Dec 23 2025 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0

* Wed Sep 17 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.8-alt1
- 1.0.8

* Wed Sep 03 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.7-alt1
- 1.0.7

* Mon Sep 01 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.6-alt1
- 1.0.6

* Sun Aug 24 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.5-alt1
- first build for Sisyphus (v1.0.5-8-gd1f06f3)
