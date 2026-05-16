%def_disable snapshot

%define _name bella
%define __name Bella
%define ver_major 0.1
%define rdn_name io.github.josephmawa.%__name

# broken appdata as usual
%def_disable check

Name: %_name
Version: %ver_major.10
Release: alt1

Summary: Yet Another Eye Dropper
License: GPL-3.0-or-later
Group: Graphics
Url: https://github.com/josephmawa/Bella

Vcs: https://github.com/josephmawa/Bella.git

%if_disabled snapshot
Source: https://github.com/josephmawa/Bella/archive/v%version/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif

BuildArch: noarch

%define adw_ver 1.5

Requires: typelib(Adw) = 1
Requires: typelib(Xdp)
Requires: libadwaita-gir >= %adw_ver
Requires: dconf

%add_python3_path %_datadir/%_name

BuildRequires(pre): rpm-macros-meson rpm-build-gir
BuildRequires: meson /usr/bin/gjs
BuildRequires: /usr/bin/glib-compile-resources /usr/bin/gtk4-update-icon-cache
%{?_enable_check:BuildRequires: /usr/bin/appstream-util desktop-file-utils /usr/bin/glib-compile-schemas}

%description
Pick a color from anywhere on your screen and save it in one of the
common color formats.

Pipettes do not happen much!

%prep
%setup -n %__name-%version

%build
%meson -Dbuildtype=release
%nil
%meson_build

%install
%meson_install
%find_lang --with-gnome %__name

%check
%__meson_test

%files -f %__name.lang
%_bindir/%rdn_name
%_desktopdir/%rdn_name.desktop
%_datadir/%__name
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.*
%_datadir/metainfo/%rdn_name.*.xml
%doc README*

%changelog
* Sat May 16 2026 Yuri N. Sedunov <aris@altlinux.org> 0.1.10-alt1
- 0.1.10

* Wed May 06 2026 Yuri N. Sedunov <aris@altlinux.org> 0.1.9-alt1
- 0.1.9

* Mon Mar 23 2026 Yuri N. Sedunov <aris@altlinux.org> 0.1.8-alt1
- 0.1.8

* Sat Nov 22 2025 Yuri N. Sedunov <aris@altlinux.org> 0.1.7-alt1
- 0.1.7

* Wed Jul 16 2025 Yuri N. Sedunov <aris@altlinux.org> 0.1.6-alt1
- 0.1.6

* Fri May 16 2025 Yuri N. Sedunov <aris@altlinux.org> 0.1.5-alt1
- 0.1.5

* Thu Apr 03 2025 Yuri N. Sedunov <aris@altlinux.org> 0.1.4-alt1
- first build for Sisyphus


