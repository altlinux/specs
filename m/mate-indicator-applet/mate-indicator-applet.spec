%define _unpackaged_files_terminate_build 1

Name: mate-indicator-applet
Version: 1.26.0
Release: alt2

Summary: MATE panel indicator applet
License: GPLv3 AND LGPLv3
Group: Graphical desktop/MATE
Url: https://github.com/mate-desktop/mate-indicator-applet

Packager: Nikolay Strelkov <snk@altlinux.org>

Source: %name-%version.tar

BuildRequires: libaccounts-glib-devel libayatana-indicator3-devel mate-common mate-panel-devel
BuildRequires: hicolor-icon-theme
BuildRequires: libdbus-glib-devel mate-settings-daemon-devel

%description
The indicator applet exposes Ayatana Indicators in the MATE Panel.
Ayatana Indicators are an initiative by Canonical to provide crisp
and clean system and application status indication. They take the
form of an icon and associated menu, displayed (usually) in the
desktop panel. Existing indicators include the Message Menu,
Battery Menu and Sound menu.

%prep
%setup

%build
NOCONFIGURE=1 mate-autogen
%configure \
  --disable-static                    \
  --disable-scrollkeeper              \
  --with-ayatana-indicators           \
  --libexecdir=%_libexecdir/%name
%make_build

%install
%makeinstall_std

%files
%doc COPYING COPYING.LGPL AUTHORS NEWS README
%_libexecdir/%name/
%_datadir/dbus-1/services/org.mate.panel.applet.IndicatorApplet*.service
%dir %_iconsdir/hicolor/scalable
%dir %_iconsdir/hicolor/scalable/apps
%_iconsdir/hicolor/scalable/apps/%name.*
%dir %_datadir/mate-panel
%dir %_datadir/mate-panel/applets
%_datadir/mate-panel/applets/org.mate.applets.Indicator.mate-panel-applet
%_datadir/mate-panel/applets/org.mate.applets.IndicatorAppmenu.mate-panel-applet
%_datadir/mate-panel/applets/org.mate.applets.IndicatorComplete.mate-panel-applet
%_datadir/locale/*/LC_MESSAGES/*.mo

%changelog
* Fri Feb 17 2023 Nikolay Strelkov <snk@altlinux.org> 1.26.0-alt2
- bump release to override autoimports package

* Sun Nov 06 2022 Nikolay Strelkov <snk@altlinux.org> 1.26.0-alt1
- Initial build for Sisyphus
