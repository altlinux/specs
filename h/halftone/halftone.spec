%def_disable snapshot

%define _name halftone
%define __name Halftone
%define ver_major 0.6
%define rdn_name io.github.tfuxu.%__name

%def_enable check

Name: %_name
Version: %ver_major.1
Release: alt1

Summary: Dither your images
License: GPL-3.0-or-later
Group: Graphics
Url: https://github.com/tfuxu/halftone

Vcs: https://github.com/tfuxu/halftone.git

%if_disabled snapshot
Source: https://github.com/tfuxu/halftone/archive/%version/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif

BuildArch: noarch

%define bp_ver 0.14
%define pygobject_ver 3.48
%define adw_ver 1.5

Requires: python3-module-pygobject3
Requires: typelib(Adw) = 1
Requires: libadwaita-gir >= %adw_ver
Requires: dconf

%add_python3_path %_datadir/%_name

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson blueprint-compiler >= %bp_ver
BuildRequires: pkgconfig(pygobject-3.0) >= %pygobject_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver typelib(Adw)
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils /usr/bin/glib-compile-schemas}

%description
A simple Libadwaita app for lossy image compression using dithering
technique.

%prep
%setup -n %__name-%version

%build
%meson -Dbuildtype=release
%nil
%meson_build

%install
%meson_install
%find_lang --with-gnome %_name

%check
%__meson_test

%files -f %_name.lang
%_bindir/%_name
%_desktopdir/%rdn_name.desktop
%_datadir/%_name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.*
%_datadir/metainfo/%rdn_name.*.xml
%doc README* CHANGELOG*

%changelog
* Thu Apr 03 2025 Yuri N. Sedunov <aris@altlinux.org> 0.6.1-alt1
- first build for Sisyphus


