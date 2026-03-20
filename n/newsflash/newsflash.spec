%def_enable snapshot
%define optflags_lto %nil

%define _name news_flash_gtk
%define ver_major 5.0
%define rdn_name io.gitlab.news_flash.NewsFlash

%def_disable bootstrap
%def_enable check

Name: newsflash
Version: %ver_major.0
Release: alt1

Summary: NewsFlash is a RSS reader
License: GPL-3.0
Group: Networking/News
Url: https://apps.gnome.org/NewsFlash

Vcs: https://gitlab.com/news-flash/news_flash_gtk.git

%if_disabled snapshot
Source: https://gitlab.com/news-flash/-/archive/v%version/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif
Source1: %_name-%version-cargo.tar

%define gtk_ver 4.12
%define adwaita_ver 1.4
%define webkit_ver 2.42

Requires: xdg-utils

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: pkgconfig(gtksourceview-5) >= 5.18
BuildRequires: pkgconfig(webkitgtk-6.0) >= %webkit_ver
BuildRequires: gir(Adw) = 1 gir(WebKit) = 6.0
BuildRequires: pkgconfig(dbus-1)
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils}

BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(sqlite3)
# since 3.3.0 for video player based on libclapper
BuildRequires: pkgconfig(clapper-gtk-0.0)
# for libxml
BuildRequires: clang-devel

%description
%summary

%prep
%setup -n %_name-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%_name-%version-cargo.tar .cargo/ vendor/}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%rdn_name
%_desktopdir/%rdn_name.desktop
%_datadir/dbus-1/services/%rdn_name.service
%_iconsdir/hicolor/*/*/*.svg
%_datadir/metainfo/%rdn_name.appdata.xml
%doc README*


%changelog
* Fri Mar 20 2026 Yuri N. Sedunov <aris@altlinux.org> 5.0.0-alt1
- 5.0.0

* Wed Nov 19 2025 Yuri N. Sedunov <aris@altlinux.org> 4.2.1-alt1
- 4.2.1

* Tue Aug 26 2025 Yuri N. Sedunov <aris@altlinux.org> 4.1.4-alt1
- 4.1.4

* Mon Aug 04 2025 Yuri N. Sedunov <aris@altlinux.org> 4.1.3-alt1
- 4.1.3

* Wed Jul 23 2025 Yuri N. Sedunov <aris@altlinux.org> 4.1.2-alt1
- 4.1.2

* Mon Jul 14 2025 Yuri N. Sedunov <aris@altlinux.org> 4.0.3-alt1
- 4.0.3

* Wed Sep 25 2024 Yuri N. Sedunov <aris@altlinux.org> 3.3.5-alt1
- 3.3.5

* Wed Jul 31 2024 Yuri N. Sedunov <aris@altlinux.org> 3.3.4-alt1
- 3.3.4

* Sun Jul 14 2024 Yuri N. Sedunov <aris@altlinux.org> 3.3.2-alt1
- 3.3.2

* Thu Jun 06 2024 Yuri N. Sedunov <aris@altlinux.org> 3.3.0-alt1
- 3.3.0

* Sat Apr 06 2024 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Fri Mar 08 2024 Yuri N. Sedunov <aris@altlinux.org> 3.1.6-alt1
- 3.1.6

* Sat Mar 02 2024 Yuri N. Sedunov <aris@altlinux.org> 3.1.5-alt1
- 3.1.5

* Sat Feb 17 2024 Yuri N. Sedunov <aris@altlinux.org> 3.1.3-alt1
- 3.1.3

* Tue Feb 13 2024 Yuri N. Sedunov <aris@altlinux.org> 3.1.1-alt1
- 3.1.1

* Mon Sep 25 2023 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- first build for Sisyphus


