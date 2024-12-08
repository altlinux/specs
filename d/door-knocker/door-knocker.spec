%define APP_ID xyz.tytanium.DoorKnocker
%def_enable check

Name: door-knocker
Version: 0.6.0
Release: alt2

Summary: Check the availability of portals
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://codeberg.org/tytan652/door-knocker
Vcs: https://codeberg.org/tytan652/door-knocker
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson >= 0.62.0
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(glib-2.0) >= 2.76
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gtk4) >= 4.16
BuildRequires: pkgconfig(libadwaita-1) >= 1.6
%if_enabled check
BuildRequires: desktop-file-utils
%endif

%description
Door Knocker allows you to check availability of all portals provided
by xdg-desktop-portal.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%_desktopdir/%APP_ID.desktop
%_iconsdir/hicolor/*/apps/%{APP_ID}*.svg
%_datadir/metainfo/%APP_ID.metainfo.xml

%changelog
* Sun Dec 08 2024 Oleg Shchavelev <oleg@altlinux.org> 0.6.0-alt2
- Fix url and vcs values (ALT #52371)

* Tue Nov 19 2024 Oleg Shchavelev <oleg@altlinux.org> 0.6.0-alt1
- Initial build
