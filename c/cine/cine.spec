%def_disable snapshot

%define __name Cine
%define _name cine
%define ver_major 1.0
%define rdn_name io.github.diegopvlk.%__name

%def_enable check

Name: %_name
Version: %ver_major.5
Release: alt1

Summary: MPV-based Video Player for Linux
License: GPL-3.0-or-later
Group: Video
Url: https://github.com/diegopvlk/Cine

Vcs: https://github.com/diegopvlk/Cine.git

BuildArch: noarch

%if_disabled snapshot
Source: https://github.com/diegopvlk/%__name/archive/v%version/%__name-%version.tar.gz
%else
Source: %__name-%version.tar
%endif

BuildArch: noarch

%add_python3_path %_datadir/%_name

%define adw_ver 1.8

Requires: python3-module-pygobject3
Requires: dconf
Requires: typelib(Adw) = 1
Requires: libadwaita-gir >= %adw_ver
#Requires: mpv

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson blueprint-compiler
BuildRequires: /usr/bin/glib-compile-resources /usr/bin/gtk4-update-icon-cache
%{?_enable_check:BuildRequires: /usr/bin/desktop-file-validate /usr/bin/appstreamcli /usr/bin/glib-compile-schemas}

%description
Cine combines a clean interface with a high-performance engine to
deliver a seamless viewing experience.

%prep
%setup -n %__name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%_datadir/%name/
%_desktopdir/%rdn_name.desktop
%_datadir/icons/hicolor/*/apps/*
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/metainfo/%rdn_name.metainfo.xml
%_datadir/dbus-1/services/%rdn_name.service
%doc README.*

%changelog
* Thu Feb 05 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.5-alt1
- 1.0.5

* Wed Feb 04 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.4-alt1
- first build for Sisyphus


