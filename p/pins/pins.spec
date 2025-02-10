%def_enable snapshot
%define _libexecdir %_prefix/libexec

%define _name Pins
%define binary_name pinapp
%define ver_major 2.0
%define rdn_name io.github.fabrialberio.%binary_name

%def_enable check

Name: pins
Version: %ver_major.0
Release: alt1

Summary: Create and edit app shortcuts
Group: Graphical desktop/GNOME
License: GPL-3.0-or-later
Url: https://github.com/fabrialberio/Pins

Vcs: https://github.com/fabrialberio/Pins.git

%if_enabled snapshot
Source: %_name-%version.tar
%else
Source: %url/archive/v%version/%_name-%version.tar.gz
%endif

%define adw_ver 1.4

Requires: dconf

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils}

%description
Pins allows to customize app menu by editing .desktop files.
Some of the things you can do are:
changing an app icon that doesn't fit in with your theme,
creating custom shortcuts to websites,
hiding apps you don't want to see,
editing properties in .desktop files.

%prep
%setup -n %_name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang --output=%name.lang %binary_name

%check
%__meson_test -v

%files -f %name.lang
%_bindir/%binary_name
%_desktopdir/%rdn_name.desktop
%_datadir/dbus-1/services/%rdn_name.service
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/*/*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*

%changelog
* Mon Feb 10 2025 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1
- first build for Sisyphus (v2.0.0-1-gaebb981)

