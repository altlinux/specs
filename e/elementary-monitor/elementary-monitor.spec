%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname io.elementary.monitor

%def_with check

Name: elementary-monitor
Version: 8.0.1
Release: alt1

Summary: Manage processes and monitor system resources.
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/monitor

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: /usr/bin/sassc
BuildRequires: pkgconfig(granite-7)
BuildRequires: pkgconfig(libgtop-2.0)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(udisks2)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(flatpak)
BuildRequires: pkgconfig(livechart-2)
BuildRequires: pkgconfig(libpci)
BuildRequires: libxnvctrl-devel

%if_with check
BuildRequires: /usr/bin/xvfb-run
%endif

%description
Manage processes and monitor system resources on the Pantheon/Elementary.

%prep
%setup
%patch -p1
sed -i 's|^Categories=.*|Categories=GTK;System;Monitor;|' data/monitor.desktop.in

%build
%meson \
       -Dindicator-wingpanel=disabled # TODO
%meson_build

%install
%meson_install

%find_lang %name --all-name

%check
xvfb-run %meson_test

%files -f %{name}.lang
%doc AUTHORS LICENSE README.md
%_bindir/%appname
%_desktopdir/%{appname}.desktop
%_iconsdir/hicolor/*/apps/%{appname}.svg
%_datadir/glib-2.0/schemas/%{appname}.gschema.xml
%_datadir/metainfo/%{appname}.metainfo.xml
%exclude %_datadir/locale/zh_HANS/LC_MESSAGES/%{appname}.mo
%exclude %_datadir/locale/zh_HANT/LC_MESSAGES/%{appname}.mo
%dir %_datadir/%{appname}/
%dir %_datadir/%{appname}/database/
%_datadir/%{appname}/database/cpu_bugs.csv
%_datadir/%{appname}/database/cpu_features.csv

%changelog
* Fri Nov 28 2025 Nikolay Strelkov <snk@altlinux.org> 8.0.1-alt1
- New version 8.0.1.

* Sun Oct 26 2025 Nikolay Strelkov <snk@altlinux.org> 8.0.0-alt1
- Initial build for Sisyphus
