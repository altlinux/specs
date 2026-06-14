%define _unpackaged_files_terminate_build 1

Name: typhoon
Version: 1.7.3
Release: alt1

Summary: Stylish weather app based on Stormcloud
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://archisman-panigrahi.github.io/typhoon
VCS: https://github.com/archisman-panigrahi/typhoon

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-qt6-webengine

BuildRequires: meson
BuildRequires: /usr/bin/appstreamcli
BuildRequires: /usr/bin/gtk-update-icon-cache
BuildRequires: rpm-build-python3

Requires: libportal-gir
Requires: libwebkit2gtk-gir
Requires: /usr/bin/convert
Requires: /usr/bin/gsettings
Requires: python3(dbus)
Requires: python3(cairosvg)

# see https://bugzilla.altlinux.org/show_bug.cgi?id=45638
%def_disable girar_repacks_srpm
%if_enabled  girar_repacks_srpm
BuildArch: noarch
%endif

ExcludeArch: %not_qt6_qtwebengine_arches

Requires: python3-module-PyQt6
Requires: python3-module-PyQt6-WebEngine

%description
Typhoon is a beautiful weather application that provides real-time weather
updates and forecasts in a highly configurable and colorful widget
inspired by the Metro interface in Windows 8.

Originally based on Stormcloud by Jono Cooper, Typhoon is powered by
Open-Meteo, OpenStreetMap and ipapi.

Features:

* Real-time weather updates and forecasts for up to four days
* Customizable units of measurement
* Displays current temperature as launcher count
* Displays precipitation warning within app
* Displays system notifications for rain, snow or thunderstorm
* Configurable widget opacity and color
* Chameleonic background color based on wallpaper or accent color
* Temperature based background color
* Supports customizable background color
* Powered by Open-Meteo, OpenStreetMap and ipapi
* Supports IP address-based location detection
* Supports multiple locations via multiple windows

%prep
%setup
sed -i "s|Categories=.*|Categories=GTK;Utility;Clock;Maps;|" io.github.archisman_panigrahi.typhoon.desktop
sed -i "s|typhoon/io.github.archisman_panigrahi.typhoon.svg|%_iconsdir/hicolor/scalable/apps/io.github.archisman_panigrahi.typhoon.svg|" README.md
sed -i "s|https://archisman-panigrahi.github.io/typhoon/assets/img/||" README.md

%build
%meson
%meson_build

%install
%meson_install

%if_disabled  girar_repacks_srpm
# something fake arch-like to bypass girar checks
mkdir -p %buildroot%perl_vendor_autolib/%name
%endif

%check
%meson_test

%files
%doc README.md assets/screenshots/typhoon.png
%_bindir/typhoon
%_desktopdir/io.github.archisman_panigrahi.typhoon.desktop
%_iconsdir/hicolor/scalable/apps/io.github.archisman_panigrahi.typhoon.svg
%_datadir/metainfo/io.github.archisman_panigrahi.typhoon.metainfo.xml
%dir %_datadir/typhoon
%_datadir/typhoon/*
%if_disabled  girar_repacks_srpm
%perl_vendor_autolib/%name
%endif

%changelog
* Sun Jun 14 2026 Nikolay Strelkov <snk@altlinux.org> 1.7.3-alt1
- New version 1.7.3.

* Sun Mar 01 2026 Nikolay Strelkov <snk@altlinux.org> 1.7.2-alt1
- New version 1.7.2.

* Wed Feb 26 2026 Nikolay Strelkov <snk@altlinux.org> 1.7.1-alt2
- Corrected license, require PyQt6 and PyQt6-WebEngine python3 modules.

* Wed Feb 25 2026 Nikolay Strelkov <snk@altlinux.org> 1.7.1-alt1
- New version 1.7.1.

* Sun Feb 22 2026 Nikolay Strelkov <snk@altlinux.org> 1.7.0-alt1
- New version 1.7.0.

* Fri Feb 20 2026 Nikolay Strelkov <snk@altlinux.org> 1.6.0-alt1
- New version 1.6.0.

* Fri Feb 13 2026 Nikolay Strelkov <snk@altlinux.org> 1.5.2-alt1
- New version 1.5.2.

* Thu Feb 05 2026 Nikolay Strelkov <snk@altlinux.org> 1.5.1-alt1
- New version 1.5.1.

* Fri Jan 30 2026 Nikolay Strelkov <snk@altlinux.org> 1.5.0-alt1
- New version 1.5.0.

* Sun Jan 25 2026 Nikolay Strelkov <snk@altlinux.org> 1.4.5-alt1
- New version 1.4.5.

* Thu Jan 22 2026 Nikolay Strelkov <snk@altlinux.org> 1.4.4-alt1
- New version 1.4.4.

* Sat Jan 17 2026 Nikolay Strelkov <snk@altlinux.org> 1.3.3-alt1
- Initial build for Sisyphus
