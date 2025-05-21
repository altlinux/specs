%define _unpackaged_files_terminate_build 1
%define app_id io.github.zaedus.spider
%def_enable check

Name: spider
Version: 0.0.6
Release: alt1

Summary: Install web apps
License: GPL-3.0-only
Group: Graphical desktop/GNOME

Url: https://github.com/Zaedus/spider
Vcs: https://github.com/Zaedus/spider
Source0: %name-%version.tar
Source1: %name-vendor.tar
Source2: config.toml

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: rust-cargo
BuildRequires: blueprint-compiler
BuildRequires: xmllint
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(cairo-gobject)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(javascriptcoregtk-6.0)
BuildRequires: pkgconfig(libsoup-3.0)
BuildRequires: pkgconfig(webkitgtk-6.0)
BuildRequires: pkgconfig(libadwaita-1)
%if_enabled check
BuildRequires: appstream
BuildRequires: desktop-file-utils
%endif

%description
Spider is a program designed to make installing and using web apps simple and
powerful while integrating with the GNOME desktop.

- Sandboxed: Each web app is completely isolated
- Adaptive Window Styling: Each app's titlebar adapts to it's theme color
- High quality icons: Scrapes websites for a high quality icons to use

%prep
%setup -a 1
install -vD %SOURCE2 .cargo/config.toml

%build
%meson -Dbuildtype=release

%install
%meson_install
%find_lang --with-gnome %name

%check
%meson_test

%files -f %name.lang
%_bindir/%name
%_datadir/%name
%_desktopdir/%app_id.desktop
%_datadir/metainfo/%app_id.metainfo.xml
%_iconsdir/hicolor/*/apps/%{app_id}*.svg
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%doc README.md

%changelog
* Mon May 19 2025 David Sultaniiazov <x1z53@altlinux.org> 0.0.6-alt1
- Initial build
