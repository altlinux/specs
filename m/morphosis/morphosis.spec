%define _name Morphosis
%define ver_major 1
%define rdn_name garden.jamie.%_name

%def_enable check

Name: morphosis
Version: %ver_major.1
Release: alt1

Summary: Documents converter for the Gnome Desktop
License: GPL-3.0-or-later
Group: Text tools
Url: https://gitlab.gnome.org/Monster/morphosis

BuildArch: noarch

Vcs: https://gitlab.gnome.org/Monster/morphosis.git
Source: %name-%version.tar

%add_python3_path %_datadir/%name

Requires: /usr/bin/pandoc dconf
Requires: typelib(Adw) = 1 typelib(WebKit) = 6.0

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson
BuildRequires: blueprint-compiler typelib(Adw) = 1 /usr/bin/glib-compile-resources
%{?_enable_check:BuildRequires: /usr/bin/desktop-file-validate /usr/bin/appstreamcli /usr/bin/glib-compile-schemas}

%description
Morphosis is a document conversion app written in Python, using GTK4 and
Libadwaita. Conversions are done with Pandoc.

%prep
%setup

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
%doc README.*

%changelog
* Tue May 28 2024 Yuri N. Sedunov <aris@altlinux.org> 1.1-alt1
- first build for Sisyphus (7ff7a6f)



