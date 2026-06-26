%define _unpackaged_files_terminate_build 1

%define appname org.easycoding.TunedSwitcher

%def_with check

Name: tuned-switcher
Version: 1.1.2
Release: alt1

Summary: Simple utility to manipulate the Tuned service
License: GPL-3.0-or-later
Group: System/Configuration/Hardware
Url: https://github.com/xvitaly/tuned-switcher

Source: %name-%version.tar

BuildRequires(pre): cmake

BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Svg)
BuildRequires: qt6-tools-devel
BuildRequires: pandoc

%if_with check
BuildRequires: ctest
BuildRequires: /usr/bin/appstream-util
%endif

Requires: hicolor-icon-theme
Requires: tuned

%description
Tuned Switcher is a simple utility for managing performance profiles
using the Tuned service.

Tuned is a daemon for monitoring and adaptive tuning of system devices.
In order to use this program, a daemon must be installed on your system.

Currently supported features:

* shows the active profile;
* easy and simple switching of performance profiles;
* automatic mode support;
* profile switch notifications;
* service control functions;
* optional widget-only mode support;
* optional systemd integration.

%prep
%setup
sed -i "s/^Categories=.*/Categories=System;Monitor;/" assets/desktop/tuned-switcher.desktop.in \
                                                      assets/desktop/autorun.desktop.in
sed -i "s/ validate / validate --nonet /" CMakeLists.txt

%build
%cmake \
       -DBUILD_MANPAGE=ON \
%if_with check
       -DBUILD_TESTS=ON
%else
       -DBUILD_TESTS=OFF
%endif
%cmake_build

%install
%cmake_install

%find_lang %name --all-name --with-qt

%check
%ctest -j1 -VV

%files -f %{name}.lang
%doc COPYING README.md docs
%_bindir/%name
%_desktopdir/%{appname}.desktop
%_iconsdir/hicolor/*/apps/%{appname}.png
%_iconsdir/hicolor/scalable/apps/%{appname}.svg
%_man1dir/%{name}.1.*
%_datadir/metainfo/%{appname}.metainfo.xml

%changelog
* Fri Jun 26 2026 Nikolay Strelkov <snk@altlinux.org> 1.1.2-alt1
- New version 1.1.2.

* Sat Jun 06 2026 Nikolay Strelkov <snk@altlinux.org> 1.1.1-alt1
- New version 1.1.1.

* Thu May 21 2026 Nikolay Strelkov <snk@altlinux.org> 1.1.0-alt1
- New version 1.1.0.

* Tue Apr 14 2026 Nikolay Strelkov <snk@altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus
