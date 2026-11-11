%define _unpackaged_files_terminate_build 1
%define app_id io.github.Replexo.Glance
%def_enable check

Name: glance
Version: 1.0
Release: alt1
Summary: View and edit images on GNOME
Group: Graphics
License: GPL-3.0-or-later
Url: https://github.com/Replexo/Glance
Vcs: https://github.com/Replexo/Glance

Source0: %name-%version.tar
Source1: vendor.tar
Source2: config.toml

Requires: glycin-2-loaders

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: rust-cargo
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(gweather4)
BuildRequires: pkgconfig(libseccomp)
BuildRequires: itstool
%if_enabled check
BuildRequires: desktop-file-utils
BuildRequires: appstream
BuildRequires: fonts-ttf-liberation
%endif

%description
Glance is an image viewer with an editor built in. Open a picture, mark it up,
adjust its colours or crop it, and save, all in the same window. It is a fork 
of Loupe, the GNOME image viewer, so browsing stays fast, sandboxed 
and touch-friendly.

%prep
%setup -a1
mkdir -p .cargo
install -vpD %SOURCE2 .cargo/config.toml

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
%_datadir/metainfo/%app_id.metainfo.xml
%_datadir/dbus-1/services/%app_id.service
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%_iconsdir/hicolor/*/apps/%{app_id}*.svg
%_datadir/licenses/%name/COPYING.*

%changelog
* Mon Nov 09 2026 Vladislav Petrukhin <vladp@altlinux.org> 1.0-alt1
- Initial build.

