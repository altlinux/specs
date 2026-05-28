%define _unpackaged_files_terminate_build 1
%define app_id studio.planetpeanut.Bobby

Name: bobby
Version: 50.0.2
Release: alt1
Summary: Browse SQLite files.
Group: Other
License: GPL-3.0-or-later
Url: https://github.com/hbons/Bobby
Vcs: https://github.com/hbons/Bobby

Source0: %name-%version.tar
Source1: vendor.tar
Source2: config.toml

Patch0: %name-%version.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: rust-cargo
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(sqlite3)

%description
Bobby lets you open SQLite database files (.db, .sqlite) and browse the 
tables inside. Handy for app development or inspecting downloaded databases.

%prep
%setup -a1 -q
%autopatch -p1
install -vpD %SOURCE2 .cargo/config.toml

%build
%meson
%meson_build

%install
%meson_install

%files
%_bindir/%name
%_desktopdir/%app_id.desktop
%_datadir/metainfo/%app_id.metainfo.xml
%_iconsdir/hicolor/*/apps/%{app_id}*.svg
%_datadir/glib-2.0/schemas/%app_id.gschema.xml

%changelog
* Wed May 27 2026 Vladislav Petrukhin <vladp@altlinux.org> 50.0.2-alt1
- Initial build.

