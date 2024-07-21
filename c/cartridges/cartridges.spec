%def_disable snapshot
%define _libexecdir %_prefix/libexec

%define _name cartridges
%define ver_major 2.9
%define rdn_name page.kramo.Cartridges

%def_enable check

Name: %_name
Version: %ver_major.3
Release: alt1

Summary: Cartridges
License: GPL-3.0-or-later
Group: Games/Other
Url: https://apps.gnome.org/Cartridges

%if_disabled snapshot
Source: https://github.com/kra-mo/cartridges/archive/v%version/%_name-%version.tar.gz
%else
Vcs: https://github.com/kra-mo/cartridges.git
Source: %_name-%version.tar
%endif

BuildArch: noarch

%define bp_ver 0.10
%define adw_ver 1.5

Requires: typelib(Adw) = 1
Requires: libadwaita-gir >= %adw_ver
Requires: dconf

# macOS specific
%add_python3_req_skip AppKit Foundation

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson blueprint-compiler >= %bp_ver typelib(Adw)
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils /usr/bin/glib-compile-schemas}

%description
Cartridges is a simple game launcher for all of your games. It has
support for importing games from Steam, Lutris, Heroic and more with no
login necessary. You can sort and hide games or download cover art from
SteamGridDB.

%prep
%setup -n %_name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %_name

%check
%__meson_test

%files -f %_name.lang
%_bindir/%_name
%_libexecdir/%_name-search-provider
%python3_sitelibdir_noarch/%name
%_desktopdir/%rdn_name.desktop
%_datadir/%_name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/dbus-1/services/%rdn_name.SearchProvider.service
%_datadir/gnome-shell/search-providers/%rdn_name.SearchProvider.ini
%_iconsdir/hicolor/*/apps/%{rdn_name}*.*
%_datadir/metainfo/%rdn_name.*.xml
%doc README*


%changelog
* Sun Jul 21 2024 Yuri N. Sedunov <aris@altlinux.org> 2.9.3-alt1
- 2.9.3

* Sun May 26 2024 Yuri N. Sedunov <aris@altlinux.org> 2.8.5-alt1
- 2.8.5

* Mon Apr 29 2024 Yuri N. Sedunov <aris@altlinux.org> 2.8.4-alt1
- 2.8.4

* Tue Apr 09 2024 Yuri N. Sedunov <aris@altlinux.org> 2.8.3-alt1
- 2.8.3

* Wed Apr 03 2024 Yuri N. Sedunov <aris@altlinux.org> 2.8.2-alt1
- 2.8.2
- enabled %%check

* Thu Mar 28 2024 Yuri N. Sedunov <aris@altlinux.org> 2.8.1-alt1
- 2.8.1

* Sun Mar 10 2024 Yuri N. Sedunov <aris@altlinux.org> 2.7.4-alt1
- 2.7.4

* Tue Feb 20 2024 Yuri N. Sedunov <aris@altlinux.org> 2.7.3-alt1
- 2.7.3

* Mon Jan 01 2024 Yuri N. Sedunov <aris@altlinux.org> 2.7.2-alt1
- updated to v2.7.2-2-g06e4dad

* Sat Dec 23 2023 Yuri N. Sedunov <aris@altlinux.org> 2.7.1-alt1
- 2.7.1

* Sat Nov 04 2023 Yuri N. Sedunov <aris@altlinux.org> 2.6.2-alt1
- 2.6.2

* Mon Oct 30 2023 Yuri N. Sedunov <aris@altlinux.org> 2.6.1-alt1
- first preview for Sisyphus


