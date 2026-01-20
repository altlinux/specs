%define _unpackaged_files_terminate_build 1

%def_without check

Name: apx-gui
Version: 1.0.6
Release: alt1

Summary: GUI frontend for Apx in GTK 4 and Libadwaita
License: GPL-3.0-only
Group: System/Configuration/Packaging
URL: https://github.com/Vanilla-OS/apx-gui

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-meson

BuildRequires: meson
BuildRequires: cmake
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: /usr/bin/appstreamcli
BuildRequires: /usr/bin/desktop-file-validate
BuildRequires: /usr/bin/gtk-update-icon-cache

Requires: apx
Requires: python3(requests)
Requires: python3(urllib3)
Requires: python3(yaml)

BuildArch: noarch

Source: %name-%version.tar

Patch: %name-%version-%release.patch

%description
%summary.

%prep
%setup
%patch -p1
sed -i "s|data/icons|%_iconsdir|" README.md
sed -i "s|data/screenshot.png|screenshot.png|" README.md
sed -i "s|Categories=Utility;Development;GTK;|Categories=System;FileTools;TerminalEmulator;GTK;|" data/org.vanillaos.ApxGUI.desktop.in

%build
%meson
%meson_build

%install
%meson_install

%find_lang apx_gui

%check
%meson_test

%files -f apx_gui.lang
%doc README.md data/screenshot.png
%_bindir/apx-gui
%_datadir/appdata/org.vanillaos.ApxGUI.appdata.xml
%_desktopdir/org.vanillaos.ApxGUI.desktop
%dir %_datadir/apx_gui
%_datadir/apx_gui/*
%_datadir/glib-2.0/schemas/org.vanillaos.ApxGUI.gschema.xml
%_iconsdir/hicolor/scalable/actions/brush-symbolic.svg
%_iconsdir/hicolor/scalable/actions/recycling-bin-symbolic.svg
%_iconsdir/hicolor/scalable/apps/org.vanillaos.ApxGUI.svg
%_iconsdir/hicolor/symbolic/apps/org.vanillaos.ApxGUI-symbolic.svg
%exclude %_datadir/locale/zh_Hans/LC_MESSAGES/apx_gui.mo
%exclude %_datadir/locale/zh_Hant/LC_MESSAGES/apx_gui.mo

%changelog
* Tue Jan 20 2026 Nikolay Strelkov <snk@altlinux.org> 1.0.6-alt1
- Initial build for Sisyphus
