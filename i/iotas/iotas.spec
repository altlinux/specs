%def_disable snapshot
%define _libexecdir %_prefix/libexec

%define ver_major 2026
%define rdn_name org.gnome.World.Iotas

# failed with pypandoc-1.16
%def_disable check

Name: iotas
Version: %ver_major.4
Release: alt1

Summary: Simple note taking with Nextcloud Notes
License: GPL-3.0
Group: Office
Url: https://apps.gnome.org/Iotas

Vcs: https://gitlab.gnome.org/World/iotas.git

%if_disabled snapshot
Source: https://gitlab.gnome.org/World/iotas/-/archive/%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif

%define adw_ver 1.8
%define gtksource_ver 5.6
%define pandoc_ver 3.8.1
# https://bugzilla.altlinux.org/55825
Requires: python3-module-mdit-plugins >= 0.5.0
# https://bugzilla.altlinux.org/55824
Requires: python3-module-markdown-it >= 4.0.0
# https://bugzilla.altlinux.org/56289
Requires: python3-module-pypandoc >= 1.16.2

Requires: python3-module-pygobject3
Requires: typelib(Adw) = 1
Requires: typelib(GtkSource) = 5
Requires: typelib(WebKit) = 6.0
Requires: dconf gnome-keyring
Requires: pandoc >= %pandoc_ver

BuildArch: noarch

%add_python3_path %_datadir/%name

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson
BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(gtksourceview-5) >= %gtksource_ver
%{?_enable_check:BuildRequires: python3-module-pygobject3 python3(pytest)
BuildRequires: python3(markdown_it) python3(mdit_py_plugins)
BuildRequires: python3(pypandoc) python3(sqlite3) python3(requests)
BuildRequires: typelib(Adw) = 1 typelib(GtkSource) = 5 typelib(WebKit) = 6.0
BuildRequires: /usr/bin/appstreamcli desktop-file-utils /usr/bin/glib-compile-schemas}

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
export PYTHONPATH=%buildroot%python3_sitelibdir_noarch
%__meson_test

%files -f %name.lang
%_bindir/%name
%_libexecdir/%name-search-provider
%python3_sitelibdir_noarch/%name/
%python3_sitelibdir_noarch/markdown_it_img_figures_plugin/
%python3_sitelibdir_noarch/markdown_it_modified_tasklists_plugin/
%_datadir/%name/
%_desktopdir/%rdn_name.desktop
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/dbus-1/services/%rdn_name.service
%_datadir/dbus-1/services/%rdn_name.SearchProvider.service
%_datadir/gnome-shell/search-providers/%rdn_name.SearchProvider.ini
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README* CHANGELOG*

%changelog
* Mon Mar 30 2026 Yuri N. Sedunov <aris@altlinux.org> 2026.4-alt1
- 2026.4

* Sun Jan 25 2026 Yuri N. Sedunov <aris@altlinux.org> 0.12.7-alt1
- 0.12.7

* Fri Jan 16 2026 Yuri N. Sedunov <aris@altlinux.org> 0.12.6-alt1
- 0.12.6

* Thu Nov 20 2025 Yuri N. Sedunov <aris@altlinux.org> 0.12.5-alt1
- 0.12.5

* Sun Nov 09 2025 Yuri N. Sedunov <aris@altlinux.org> 0.12.4-alt1
- 0.12.4

* Wed Oct 08 2025 Yuri N. Sedunov <aris@altlinux.org> 0.12.1-alt1
- 0.12.1

* Mon Sep 01 2025 Yuri N. Sedunov <aris@altlinux.org> 0.11.4-alt1
- 0.11.4

* Sun Jul 27 2025 Yuri N. Sedunov <aris@altlinux.org> 0.11.2-alt1
- 0.11.2

* Wed Jul 09 2025 Yuri N. Sedunov <aris@altlinux.org> 0.11.1-alt1
- 0.11.1-30-gd357226

* Tue Mar 25 2025 Yuri N. Sedunov <aris@altlinux.org> 0.11.0-alt1
- 0.11.0

* Tue Mar 18 2025 Yuri N. Sedunov <aris@altlinux.org> 0.10.3-alt1
- 0.10.3

* Fri Feb 28 2025 Yuri N. Sedunov <aris@altlinux.org> 0.10.2-alt1
- 0.10.2

* Fri Feb 21 2025 Yuri N. Sedunov <aris@altlinux.org> 0.10.1-alt1
- 0.10.1

* Thu Jan 23 2025 Yuri N. Sedunov <aris@altlinux.org> 0.10.0-alt1
- 0.10.0

* Fri Nov 15 2024 Yuri N. Sedunov <aris@altlinux.org> 0.9.5-alt1
- 0.9.5

* Tue Oct 29 2024 Yuri N. Sedunov <aris@altlinux.org> 0.9.4-alt1
- 0.9.4

* Tue Oct 15 2024 Yuri N. Sedunov <aris@altlinux.org> 0.9.3-alt1
- 0.9.3

* Mon Oct 07 2024 Yuri N. Sedunov <aris@altlinux.org> 0.9.2-alt1
- 0.9.2

* Wed Sep 25 2024 Yuri N. Sedunov <aris@altlinux.org> 0.9.1-alt1
- 0.9.1

* Fri Sep 20 2024 Yuri N. Sedunov <aris@altlinux.org> 0.9.0-alt1
- 0.9.0

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


