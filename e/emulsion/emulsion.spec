%def_enable snapshot

%define _name emulsion
%define ver_major 3.3
%define rdn_name io.github.lainsce.Emulsion

%def_enable check

Name: %_name
Version: %ver_major.9
Release: alt1

Summary: Stock up on colors
License: GPL-3.0-or-later
Group: Graphics
Url: https://github.com/lainsce/emulsion

Vcs: https://github.com/lainsce/emulsion.git

%if_disabled snapshot
Source: %url/archive/%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson vala-tools
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(gmodule-2.0)
BuildRequires: pkgconfig(json-glib-1.0)
%{?_enable_check:BuildRequires: /usr/bin/appstream-util desktop-file-utils /usr/bin/glib-compile-schemas}

%description
Store your palettes in an easy way, and edit them if needed.

%prep
%setup -n %_name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang %rdn_name

%check
%__meson_test

%files -f %rdn_name.lang
%_bindir/%rdn_name
%_desktopdir/%rdn_name.desktop
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/*/*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc AUTHORS* README*

%changelog
* Fri May 10 2024 Yuri N. Sedunov <aris@altlinux.org> 3.3.9-alt1
- first build for Sisyphus (3.3.9-14-gefc64b2)


