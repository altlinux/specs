%define _unpackaged_files_terminate_build 1
%define oname net.armatik.Kitsune
%define nameS kitsune

%def_without check

Name: kitsune-adw
Version: 1.0.0
Release: alt1

Summary: Kitsune is an unofficial client for watching AniLiberty anime
License: GPL-3.0-or-later
Group: Video

Url: https://altlinux.space/armatik/Kitsune
Vcs: https://altlinux.space/armatik/Kitsune

BuildArch: noarch
AutoProv: nopython3

Source: %name-%version.tar

Requires: libwebp-pixbuf-loader
Requires: gst-plugin-gtk4
%add_python3_path %_datadir/%nameS

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-gir
BuildRequires: meson
BuildRequires: python3(gi)
BuildRequires: typelib(Adw)
BuildRequires: python3(cairo)
BuildRequires: pkgconfig(gtk4)
BuildRequires: python3(keyring)
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(libadwaita-1) 
BuildRequires: /usr/bin/glib-compile-schemas
BuildRequires: /usr/bin/gtk4-update-icon-cache
BuildRequires: /usr/bin/update-desktop-database

%if_with check
BuildRequires: xvfb-run
BuildRequires: typelib(Soup)
BuildRequires: python3-module-pytest
%endif

%description
%summary.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name --all-name

%check
%meson_test

%files -f %name.lang
%_bindir/%nameS
%_desktopdir/%oname.desktop
%_datadir/glib-2.0/schemas/%oname.*
%_iconsdir/hicolor/*/*/*.svg
%_datadir/%nameS
%_datadir/metainfo/%oname.*
%doc *.md

%changelog
* Sun Aug 09 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.0.0-alt1
- 0.8.5 -> 1.0.0

* Fri Mar 27 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.8.5-alt1
- 0.8.4 -> 0.8.5

* Sun Mar 22 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.8.4-alt1
- 0.8.3 -> 0.8.4

* Thu Mar 19 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.8.3-alt1
- 0.8.2 -> 0.8.3

* Wed Mar 18 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.8.2-alt1
- 0.7.1 -> 0.8.2

* Sat Mar 14 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.7.1-alt2
- added gst-plugin-gtk4 dependency

* Fri Mar 13 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.7.1-alt1
- 0.6.1 -> 0.7.1

* Wed Mar 11 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.6.1-alt1
- 0.6.0 -> 0.6.1

* Wed Mar 11 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.6.0-alt1
- 0.5.0 -> 0.6.0

* Tue Mar 10 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.5.0-alt1
- Initial build for ALT Linux.

