%define xdg_name com.raggesilver.BlackBox
%define _name blackbox

Name: blackbox-terminal
Version: 0.13.2
Release: alt1

Summary: A beautiful GTK 4 terminal.
License: GPL-3.0
Group: Terminals

Url: https://gitlab.gnome.org/raggesilver/blackbox
Source: %name-%version.tar
Packager: Vladimir Didenko <cow@altlinux.org>

Provides: xvt
# Executable file name conflict
Conflicts: blackbox

%define vte_ver 0.69.0

Requires(pre): libvte3 >= %vte_ver
Requires: dconf

BuildRequires(pre): rpm-macros-meson rpm-build-gnome rpm-macros-alternatives
BuildRequires: meson
BuildRequires: vala
BuildRequires: libgio-devel
BuildRequires: libgtk4-devel
BuildRequires: libvte3-devel >= %vte_ver
BuildRequires: libadwaita-devel
BuildRequires: libmarble-vala
BuildRequires: libpcre2-devel libxml2-devel
BuildRequires: librsvg-devel
BuildRequires: libjson-glib-devel
BuildRequires: libgraphene-devel
BuildRequires: libgee0.8-devel

%description
A beautiful GTK 4 terminal.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%find_lang %_name

%files -f %_name.lang
%doc COPYING README.md
%_bindir/%_name
%_datadir/%_name
%_datadir/appdata/%xdg_name.appdata.xml
%_desktopdir/%xdg_name.desktop
%_datadir/glib-2.0/schemas/*
%_iconsdir/hicolor/*/actions/*.svg
%_iconsdir/hicolor/*/apps/*.svg

%changelog
* Thu Mar 9 2023 Vladimir Didenko <cow@altlinux.org> 0.13.2-alt1
- New version

* Thu Jan 19 2023 Vladimir Didenko <cow@altlinux.org> 0.13.1-alt1
- New version

* Tue Dec 6 2022 Vladimir Didenko <cow@altlinux.org> 0.12.2-alt1
- New version

* Mon Oct 24 2022 Vladimir Didenko <cow@altlinux.org> 0.12.1-alt2
- Fix text selection

* Wed Oct 5 2022 Vladimir Didenko <cow@altlinux.org> 0.12.1-alt1
- New version

* Mon Sep 19 2022 Vladimir Didenko <cow@altlinux.org> 0.12.0-alt1
- Initial build for Sisyphus
