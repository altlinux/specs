%def_disable snapshot
%define _libexecdir %_prefix/libexec

%define ver_major 0.8
%define rdn_name org.gnome.World.Iotas

%def_enable check

Name: iotas
Version: %ver_major.2
Release: alt1

Summary: Simple note taking with Nextcloud Notes
License: GPL-3.0
Group: Office
Url: https://gitlab.gnome.org/World/iotas

%if_disabled snapshot
Source: %url/-/archive/%version/%name-%version.tar.gz
%else
Vcs: https://gitlab.gnome.org/World/iotas.git
Source: %name-%version.tar
%endif

%define adw_ver 1.5

Requires: typelib(Adw) = 1
Requires: typelib(GtkSource) = 5
Requires: typelib(WebKit) = 6.0
Requires: dconf gnome-keyring

BuildArch: noarch

%add_python3_path %_datadir/%name

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson
BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(gtksourceview-5)
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils /usr/bin/glib-compile-schemas}

%description
Iotas is a simple note taking app with mobile-first design and a focus
on sync with Nextcloud Notes.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome --output=%name.lang %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%_libexecdir/%name-search-provider
%python3_sitelibdir_noarch/%name/
%python3_sitelibdir_noarch/markdown_it_img_lazyload_plugin/
%python3_sitelibdir_noarch/markdown_it_modified_tasklists_plugin/
%_datadir/%name/
%_datadir/gtksourceview-5/language-specs/%name-markdown.lang
%_datadir/gtksourceview-5/styles/%name-*.xml
%_desktopdir/%rdn_name.desktop
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/dbus-1/services/%rdn_name.SearchProvider.service
%_datadir/gnome-shell/search-providers/%rdn_name.SearchProvider.ini
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*

%changelog
* Fri Aug 09 2024 Yuri N. Sedunov <aris@altlinux.org> 0.8.2-alt1
- 0.8.2

* Wed Aug 07 2024 Yuri N. Sedunov <aris@altlinux.org> 0.8.1-alt1
- 0.8.1

* Thu Jun 06 2024 Yuri N. Sedunov <aris@altlinux.org> 0.8.0-alt1
- 0.8.0

* Fri May 03 2024 Yuri N. Sedunov <aris@altlinux.org> 0.2.14-alt1
- 0.2.14

* Fri Apr 19 2024 Yuri N. Sedunov <aris@altlinux.org> 0.2.13-alt1
- 0.2.13

* Tue Apr 02 2024 Yuri N. Sedunov <aris@altlinux.org> 0.2.12-alt1
- 0.2.12

* Wed Mar 13 2024 Yuri N. Sedunov <aris@altlinux.org> 0.2.10-alt1
- 0.2.10

* Sat Mar 09 2024 Yuri N. Sedunov <aris@altlinux.org> 0.2.9-alt1
- 0.2.9

* Sat Feb 24 2024 Yuri N. Sedunov <aris@altlinux.org> 0.2.8-alt1
- 0.2.8

* Sat Jan 20 2024 Yuri N. Sedunov <aris@altlinux.org> 0.2.7-alt1
- updated to 0.2.7-14-g3aa62e4

* Sun Nov 19 2023 Yuri N. Sedunov <aris@altlinux.org> 0.2.6-alt1
- first build for Sisyphus (0.2.6-13-gc7c221d)


