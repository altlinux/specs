%def_disable snapshot

%define _name color-code
%define __name ColorCode
%define ver_major 0.1
%define rdn_name com.oyajun.%__name

%def_enable check

Name: %_name
Version: %ver_major.5
Release: alt1

Summary: Resistor Color Code Calculator
License: GPL-3.0-or-later
Group: Sciences/Physics
Url: https://github.com/oyajun/color-code

Vcs: https://github.com/oyajun/color-code.git

%if_disabled snapshot
Source: %url/archive/v%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif

BuildArch: noarch

%add_python3_path %_datadir/%name

Requires: python3-module-pygobject3
Requires: typelib(Adw) = 1

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson blueprint-compiler
BuildRequires: pkgconfig(libadwaita-1)
%{?_enable_check:BuildRequires: desktop-file-utils /usr/bin/appstreamcli /usr/bin/glib-compile-schemas}

%description
"Color Code" is the app which converts to the resistance value from the
color code.

%prep
%setup %_name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome --output=%name.lang %name

%check
%__meson_test

%files -f %name.lang
%attr(0755,root,root) %_bindir/%name
%_datadir/%name/
%_desktopdir/%rdn_name.desktop
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*

%changelog
* Sat Apr 12 2025 Yuri N. Sedunov <aris@altlinux.org> 0.1.5-alt1
- first build for Sisyphus


