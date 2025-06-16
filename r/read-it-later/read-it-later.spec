%define _unpackaged_files_terminate_build 1
%def_enable check
%define app_id com.belmoussaoui.ReadItLater
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

Name: read-it-later
Version: 0.6.2
Release: alt1

Summary: Save and read web articles
License: GPL-3.0-or-later
Group: Office
Url: https://gitlab.gnome.org/World/read-it-later
Vcs: https://gitlab.gnome.org/World/read-it-later

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: config.toml

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: rust-cargo
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(javascriptcoregtk-6.0)
BuildRequires: pkgconfig(webkitgtk-6.0)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(libcurl)
BuildRequires: /proc
%if_enabled check
BuildRequires: desktop-file-utils
BuildRequires: /usr/bin/appstreamcli
BuildRequires: /usr/bin/glib-compile-schemas
%endif

%description
Read It Later, is a simple Wallabag client.
It has the basic features to manage your articles.
* Add new articles;
* Archive an article;
* Delete an article;
* Favorite an article.

It also comes with a nice on eyes reader mode
that supports code syntax highlighting and a dark mode.

%prep
%setup -a1
%autopatch -p1
install -vD %SOURCE2 .cargo/config.toml

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%check
%meson_test

%files -f %name.lang
%_bindir/%name
%_desktopdir/%app_id.desktop
%_iconsdir/hicolor/*/apps/%{app_id}*.svg
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%_datadir/metainfo/%app_id.metainfo.xml
%_datadir/%name/*.gresource
%doc README.md

%changelog
* Tue Jun 10 2025 Semen Fomchenkov <armatik@altlinux.org> 0.6.2-alt1
- Initial build.
