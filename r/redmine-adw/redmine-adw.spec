%define _unpackaged_files_terminate_build 1
%define app_id ru.toxblh.RedmineAdw

Name: redmine-adw
Version: 1.0.1
Release: alt1
Summary: A GTK4/libadwaita client for Redmine
License: GPL-3.0
Group: Communications
Url: https://altlinux.space/toxblh/redmine-adw
VCS: https://altlinux.space/toxblh/redmine-adw.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: /usr/bin/glib-compile-schemas
BuildRequires: /usr/bin/gtk4-update-icon-cache
BuildRequires: /usr/bin/update-desktop-database
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(libsoup-3.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(webkitgtk-6.0)
BuildRequires: pkgconfig(libsecret-1)

%description
%summary.

%prep
%setup
%autopatch -p 1

%build
%meson
%meson_build -v

%install
%meson_install
%find_lang %name --all-name

%files -f %name.lang
%_bindir/%name
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*
%_datadir/metainfo/*.xml
%_datadir/glib-2.0/schemas/%app_id.*

%changelog
* Fri Oct 23 2026 Vasiliy Doylov <neko@altlinux.org> 1.0.1-alt1
- Initial build for ALT.
