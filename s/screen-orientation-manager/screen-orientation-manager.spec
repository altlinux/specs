%define _unpackaged_files_terminate_build 1

Name: screen-orientation-manager
Version: 1.5.4
Release: alt1

Summary: Touchscreen Orientation Manager for touchscreen tablets (e.g. Surface RT/Touch screen ARM Chromebooks) running GNU/Linux with X11
License: GPL-3.0-or-later
Group: Graphical desktop/Other
URL: https://github.com/archisman-panigrahi/screen-orientation-manager

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-meson

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: meson

Requires: python3(gi)
Requires: libayatana-appindicator3-gir

BuildArch: noarch

Source: %name-%version.tar

%description
Screen Orientation Manager for touchscreen tablets and convertible
laptops running GNU/Linux with X11

You can use this app to easily rotate the touchscreen input,
display orientation, touchpad and stylus input in one go.

While automatic rotation of input devices works seamlessly in GNOME
and KDE on Wayland, many entry-level devices use lightweight desktop
environments like XFCE, MATE, or LXDE, which rely on X11 and lack
support for automatic touchscreen input rotation. As a result, when
the screen is rotated, touch inputs can become misaligned (e.g.,
after rotating the screen, touching the top-left corner might register
as a tap in the bottom-right). This app resolves that issue. It also
runs in the system tray, making it easy to access when using the device
in tablet mode.

%prep
%setup
sed -i "s|io.github.archisman_panigrahi.screen-orientation-manager.svg|%_iconsdir/hicolor/scalable/apps/io.github.archisman_panigrahi.screen-orientation-manager.svg|" README.md
sed -i "s|Screenshots/||" README.md
sed -i "s|Categories=.*|Categories=GTK;Settings;HardwareSettings;|" io.github.archisman_panigrahi.screen-orientation-manager.desktop

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc LICENSE README.md Screenshots/*{1,2}.png
%_bindir/screen-orientation-manager
%_desktopdir/io.github.archisman_panigrahi.screen-orientation-manager.desktop
%_iconsdir/hicolor/scalable/apps/io.github.archisman_panigrahi.screen-orientation-manager.svg
%_datadir/metainfo/io.github.archisman_panigrahi.screen-orientation-manager.metainfo.xml
%dir %_datadir/screen-orientation-manager
%_datadir/screen-orientation-manager/ScreenOrientationManager.py
%_datadir/screen-orientation-manager/known-configs.txt
%dir %_datadir/screen-orientation-manager/rotation-scripts
%_datadir/screen-orientation-manager/rotation-scripts/i.sh
%_datadir/screen-orientation-manager/rotation-scripts/l.sh
%_datadir/screen-orientation-manager/rotation-scripts/n.sh
%_datadir/screen-orientation-manager/rotation-scripts/r.sh

%changelog
* Tue May 05 2026 Nikolay Strelkov <snk@altlinux.org> 1.5.4-alt1
- New version 1.5.4.

* Tue Feb 17 2026 Nikolay Strelkov <snk@altlinux.org> 1.5.3-alt1
- New version 1.5.3.

* Sun Feb 15 2026 Nikolay Strelkov <snk@altlinux.org> 1.5.1-alt1
- New version 1.5.1.

* Sat Feb 14 2026 Nikolay Strelkov <snk@altlinux.org> 1.5.0-alt1
- New version 1.5.0.

* Sun Nov 09 2025 Nikolay Strelkov <snk@altlinux.org> 1.4.2-alt1
- Initial build for Sisyphus
