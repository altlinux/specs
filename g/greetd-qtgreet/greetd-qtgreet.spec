%define _unpackaged_files_terminate_build 1

Name: greetd-qtgreet
Version: 2.0.4
Release: alt2

Summary: Qt based greeter for greetd
License: GPL-3.0-only
Group: Graphical desktop/Other
Url: https://gitlab.com/marcusbritanicus/QtGreet

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson

BuildRequires: meson
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(wayqt-qt6)
BuildRequires: pkgconfig(df6application)
BuildRequires: pkgconfig(df6utils)
BuildRequires: pkgconfig(df6login1)
BuildRequires: pkgconfig(mpv)
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: rpm-build-python3

Requires: mpv
Requires: greetd
Requires: sway
Requires: greetd-qtgreet-data

Provides: greetd-greeter

%description
%summary, to be run under wayfire or similar wlr-based compositors.

%package data
Summary: Qt based greeter for greetd - data files
Group: Graphical desktop/Other
BuildArch: noarch

%description data
%summary, to be run under wayfire or similar wlr-based compositors.

This package contains the architecture independent data files.

%prep
%setup

%build
%meson \
       -Ddynpath=%_localstatedir/qtgreet
%meson_build

%install
%meson_install
install -d 755 %buildroot%_localstatedir/qtgreet

%check
%meson_test

%files
%doc Changelog LICENSE README.md ReleaseNotes screenshots
%dir %_sysconfdir/qtgreet
%config(noreplace) %_sysconfdir/qtgreet/config.ini
%config(noreplace) %_sysconfdir/qtgreet/sway.cfg
%config(noreplace) %_sysconfdir/qtgreet/users.conf
%config(noreplace) %_sysconfdir/qtgreet/wayfire.ini
%_bindir/qtgreet
%_iconsdir/hicolor/512x512/apps/QtGreet.png
%_iconsdir/hicolor/scalable/apps/QtGreet.svg
%dir %_localstatedir/qtgreet

%files data
%dir %_datadir/qtgreet
%exclude %_datadir/qtgreet/Changelog
%exclude %_datadir/qtgreet/README.md
%exclude %_datadir/qtgreet/ReleaseNotes
%dir %_datadir/qtgreet/backgrounds
%_datadir/qtgreet/backgrounds/*
%dir %_datadir/qtgreet/themes
%_datadir/qtgreet/themes/LytMgr.py
%dir %_datadir/qtgreet/themes/aerial
%_datadir/qtgreet/themes/aerial/4k.m3u
%_datadir/qtgreet/themes/aerial/all_sd.m3u
%_datadir/qtgreet/themes/aerial/day.m3u
%_datadir/qtgreet/themes/aerial/index.theme
%_datadir/qtgreet/themes/aerial/layout.hjson
%_datadir/qtgreet/themes/aerial/night.m3u
%_datadir/qtgreet/themes/aerial/style.qss
%dir %_datadir/qtgreet/themes/compact
%_datadir/qtgreet/themes/compact/index.theme
%_datadir/qtgreet/themes/compact/layout.hjson
%_datadir/qtgreet/themes/compact/style.qss
%dir %_datadir/qtgreet/themes/default
%_datadir/qtgreet/themes/default/index.theme
%_datadir/qtgreet/themes/default/layout.hjson
%_datadir/qtgreet/themes/default/style.qss
%dir %_datadir/qtgreet/themes/sidebar
%_datadir/qtgreet/themes/sidebar/index.theme
%_datadir/qtgreet/themes/sidebar/layout.hjson
%_datadir/qtgreet/themes/sidebar/style.qss

%changelog
* Sat Jan 24 2026 Nikolay Strelkov <snk@altlinux.org> 2.0.4-alt2
- Added missed greetd-greeter provider (closes: #57626).

* Fri Jan 09 2026 Nikolay Strelkov <snk@altlinux.org> 2.0.4-alt1
- Initial build for Sisyphus
