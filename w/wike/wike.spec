%define _name wike
%define ver_major 3.1
%define rdn_name com.github.hugolabe.Wike

%def_enable check

Name: %_name
Version: %ver_major.0
Release: alt1

Summary: Wikipedia reader for the GNOME Desktop
License: GPL-3.0-or-later
Group: Education
Url: https://apps.gnome.org/Wike

BuildArch: noarch

Vcs: https://github.com/hugolabe/Wike.git
Source0: %name-%version.tar
Patch0: wike-3.0.1-alt-data_dynamic_default_language.patch

%add_python3_path %_datadir/%_name

Requires: dconf
Requires: typelib(Adw) = 1 typelib(WebKit) = 6.0

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson pkgconfig(gio-2.0)
BuildRequires: /usr/bin/glib-compile-resources /usr/bin/gtk4-update-icon-cache
%{?_enable_check:BuildRequires: /usr/bin/desktop-file-validate /usr/bin/appstreamcli /usr/bin/glib-compile-schemas}

%description
Wike is a Wikipedia reader for the GNOME Desktop.
Provides access to all the content of this online encyclopedia in a
native application, with a simpler and distraction-free view of
articles.

%prep
%setup
%patch0 -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%_datadir/%name/
%_desktopdir/%rdn_name.desktop
%_datadir/icons/hicolor/*/apps/*
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/metainfo/%rdn_name.metainfo.xml
%_datadir/dbus-1/services/%rdn_name.SearchProvider.service
%_datadir/gnome-shell/search-providers/%rdn_name.SearchProvider.ini
%doc README.*

%changelog
* Wed Aug 14 2024 Yuri N. Sedunov <aris@altlinux.org> 3.1.0-alt1
- 3.1.0

* Sat Apr 13 2024 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt2.1
- just rebuilt for Sisyphus with patch from proposed in previous release

* Sat Apr 13 2024 Semen Fomchenkov <armatik@altlinux.org> 3.0.1-alt2
- Added automatic language selection based on the user's locale.

* Sat Mar 30 2024 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1.1
- fixed build w/o %%check

* Sat Mar 23 2024 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Sat Mar 09 2024 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt3
- prepared for Sisyphus

* Sat Mar 09 2024 Semen Fomchenkov <armatik@altlinux.org> 3.0.0-alt2
- 3.0 update

* Sun Jan 28 2024 Semen Fomchenkov <armatik@altlinux.org> 2.1.0-alt1
- Init build for Sisyphus
