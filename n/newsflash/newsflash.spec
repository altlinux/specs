%def_enable snapshot
%define optflags_lto %nil

%define _name news_flash_gtk
%define ver_major 3.3
%define rdn_name io.gitlab.news_flash.NewsFlash

%def_disable bootstrap
%def_enable check

Name: newsflash
Version: %ver_major.2
Release: alt1

Summary: NewsFlash is a RSS reader
License: GPL-3.0
Group: Networking/News
Url: https://apps.gnome.org/NewsFlash

%if_disabled snapshot
Source: https://gitlab.com/news-flash/-/archive/v%version/%_name-%version.tar.gz
%else
Vcs: https://gitlab.com/news-flash/news_flash_gtk.git
Source: %_name-%version.tar
%endif
Source1: %name-%version-cargo.tar

%define gtk_ver 4.12
%define adwaita_ver 1.4
%define webkit_ver 2.42

Requires: xdg-utils

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver gir(Adw)
BuildRequires: pkgconfig(webkitgtk-6.0) >= %webkit_ver
BuildRequires: pkgconfig(dbus-1)
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils}

BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(sqlite3)
# since 3.3.0 for video player based on libclapper
BuildRequires: pkgconfig(clapper-gtk-0.0)

%description
%summary

%prep
%setup -n %_name-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

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
%_iconsdir/hicolor/*/*/*.svg
%_datadir/metainfo/%rdn_name.appdata.xml
%doc README*


%changelog
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


