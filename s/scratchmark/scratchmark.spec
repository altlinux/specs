%define _unpackaged_files_terminate_build 1
%define app_id org.scratchmark.Scratchmark

Name: scratchmark
Version: 1.8.0
Release: alt1
Summary: Organized markdown editor.
Group: Editors
License: GPL-3.0-or-later
Url: https://github.com/sevonj/scratchmark
Vcs: https://github.com/sevonj/scratchmark

Source0: %name-%version.tar
Source1: vendor.tar
Source2: config.toml

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: rust-cargo
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: libgtksourceview5-devel

%description
Scratchmark lets you focus on the text without distractions. It's designed both
for keeping notes and writing longer texts, and makes organizing files easy.

%prep
%setup -a1
mkdir -p .cargo
install -vpD %SOURCE2 .cargo/config.toml

%build
%meson -Doffline=true -Dbuildtype=release
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%check
%meson_test

%files -f %name.lang
%_bindir/%name
%_desktopdir/%app_id.desktop
%_datadir/metainfo/%app_id.metainfo.xml
%_datadir/%name/%name.gresource
%_datadir/%name/editor_schemes/*
%_iconsdir/hicolor/symbolic/apps/%app_id-symbolic.svg
%_iconsdir/hicolor/scalable/apps/%app_id.svg
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%_datadir/%name/language_specs/markdown.lang

%changelog
* Wed Apr 15 2026 Vladislav Petrukhin <vladp@altlinux.org> 1.8.0-alt1
- New version 1.8.0.

* Tue Feb 10 2026 Vladislav Petrukhin <vladp@altlinux.org> 1.7.1-alt1
- New version 1.7.1. 

* Tue Dec 02 2025 Vladislav Petrukhin <vladp@altlinux.org> 1.5.0-alt1
- Initial build.
