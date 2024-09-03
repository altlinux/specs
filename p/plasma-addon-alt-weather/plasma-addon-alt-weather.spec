%define _unpackaged_files_terminate_build 1
%global __find_debuginfo_files %nil

Name: plasma-addon-alt-weather
Version: 2.0.0
Release: alt3

Group: Graphical desktop/KDE
Summary: KDE Workspace 6 Plasma weather addon
License: GPLv2+

Provides: kde5-plasma-addon-alt-weather = %EVR
Obsoletes: kde5-plasma-addon-alt-weather < %EVR

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules gcc-c++
BuildRequires: kf6-kdeclarative-devel
BuildRequires: plasma-workspace-devel
BuildRequires: libplasma6
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kpackage-devel
BuildRequires: plasma6-plasma5support-devel
BuildRequires: plasma6-lib-devel

Requires: alt-identify-client

ExclusiveArch: x86_64 aarch64 %e2k

%description
The weather forecast addon for KDE Workspace 6 Plasma

%prep
%setup

%build
%K6build

%install
%K6install
%find_lang %name --all-name

%files -f %name.lang
%_K6plug/plasma5support/dataengine/*.so
%_K6qml/org/kde/plasma/alt/private/weather/
%_datadir/icons/hicolor/scalable/status/*
%_datadir/icons/breeze/status/64/*
%_datadir/icons/breeze-dark/status/64/*
%_datadir/plasma-addon-alt-weather/ya_logo/*
%_datadir/plasma/plasmoids/org.kde.plasma.alt.weather/
%_datadir/metainfo/*

%changelog
* Tue Sep 03 2024 Daniil-Viktor Ratkin <krf10@altlinux.org> 2.0.0-alt3
- fix manual location setting (closes: 51300)

* Thu Aug 15 2024 Daniil-Viktor Ratkin <krf10@altlinux.org> 2.0.0-alt2
- fix text shadows in tray

* Tue Aug 13 2024 Daniil-Viktor Ratkin <krf10@altlinux.org> 2.0.0-alt1
- full port to KF6

* Tue Jul 30 2024 Daniil-Viktor Ratkin <krf10@altlinux.org> 2.0.0-alt0.1
- port to KF6

* Tue Jul 30 2024 Daniil-Viktor Ratkin <krf10@altlinux.org> 1.0.25-alt2
- Update version (closes: #49309)

* Tue Jul 16 2024 Daniil-Viktor Ratkin <krf10@altlinux.org> 1.0.25-alt1
- slightly refactor and fix segfault after widget deletion (closes: #49632)

* Fri Mar 15 2024 Slava Aseev <ptrnine@altlinux.org> 1.0.24-alt1
- Fix:
  + error tooltip
  + BusyIndicator size in tray view
  + typo in russian translation (closes: #49701)
- Use shorter form for errors in badge
- Allow to configure badge only if applet is in system tray
- Validate location search input (closes: #49700)
- Update version (closes: #49309)

* Tue Mar 05 2024 Slava Aseev <ptrnine@altlinux.org> 1.0.23-alt1
- Fix wind icon direction (closes: #49614)
- Make temperature badge configurable
- Introduce applet tooltip

* Tue Mar 05 2024 Slava Aseev <ptrnine@altlinux.org> 1.0.22-alt1
- Fix text size in BadgeOverlay

* Fri Mar 01 2024 Slava Aseev <ptrnine@altlinux.org> 1.0.21-alt1
- Fix getting weather with en_* locales

* Thu Feb 29 2024 Slava Aseev <ptrnine@altlinux.org> 1.0.20-alt1
- Handle "calm" wind direction properly (closes: #49570)
- Fix weather url when auto location enabled (closes: #49569)

* Wed Feb 28 2024 Slava Aseev <ptrnine@altlinux.org> 1.0.19-alt1
- Bump version (closes: #49309)
- Fix BusyIndicator size in tray view (closes: #49542)
- Remove floating update interval (due to bugs)
- Enable by default

* Mon Feb 26 2024 Slava Aseev <ptrnine@altlinux.org> 1.0.18-alt1
- Use IP geolocation by default
- Show wind direction
- Make errors more informative
- Show old data if some error occurred
- Disable widget resize workaround
- Fix widget description

* Mon Feb 19 2024 Michael Shigorin <mike@altlinux.org> 1.0.17-alt1.1
- EA: += %%e2k

* Mon Jan 22 2024 Slava Aseev <ptrnine@altlinux.org> 1.0.17-alt1
- Enable build for aarch64
- Fix compact view in vertical panel and system tray
- Fix DetailsView when displayed via system tray

* Tue Jan 16 2024 Slava Aseev <ptrnine@altlinux.org> 1.0.16-alt1
- Refactor, add license headers, fix some potential bugs
  (thx @golubevan for the review)

* Tue Dec 26 2023 Slava Aseev <ptrnine@altlinux.org> 1.0.15-alt1
- Use floating update interval in weather source
- Fix widget resize bug

* Tue Dec 05 2023 Slava Aseev <ptrnine@altlinux.org> 1.0.14-alt1
- Update weather engine backend

* Fri Nov 17 2023 Slava Aseev <ptrnine@altlinux.org> 1.0.13-alt1
- Remove validation server, weather resource, and update delay
  settings

* Tue Nov 07 2023 Slava Aseev <ptrnine@altlinux.org> 1.0.12-alt1
- Fix:
  + widget resize bugs
  + wrong yandex logo colors with some themes

* Tue Nov 07 2023 Slava Aseev <ptrnine@altlinux.org> 1.0.11-alt1
- Fix bug with hours in hourly forecast

* Tue Nov 07 2023 Slava Aseev <ptrnine@altlinux.org> 1.0.10-alt1
- Fix "Today" label

* Thu Nov 02 2023 Slava Aseev <ptrnine@altlinux.org> 1.0.9-alt1
- Change icon installation directories
- Bring forecast's values into line with yandex.ru/pogoda

* Tue Oct 31 2023 Slava Aseev <ptrnine@altlinux.org> 1.0.8-alt1
- Fix incorrect yandex logo: use PNG instead of SVG

* Tue Oct 31 2023 Slava Aseev <ptrnine@altlinux.org> 1.0.7-alt1
- Fix start widged size on Education

* Mon Oct 23 2023 Slava Aseev <ptrnine@altlinux.org> 1.0.6-alt1
- Change default validation server and weather resource

* Mon Oct 23 2023 Slava Aseev <ptrnine@altlinux.org> 1.0.5-alt1
- Show the date relative to the timezone of the current location
- Some layouting fixes for Education

* Thu Oct 12 2023 Slava Aseev <ptrnine@altlinux.org> 1.0.4-alt1
- Rename package

* Wed Oct 11 2023 Slava Aseev <ptrnine@altlinux.org> 1.0.3-alt1
- Fix start widget size on p10

* Wed Oct 11 2023 Slava Aseev <ptrnine@altlinux.org> 1.0.2-alt1
- Visual improvements:
  + make settlement heading resizable
  + adjust start widget size
  + relayout fact view

* Mon Oct 09 2023 Slava Aseev <ptrnine@altlinux.org> 1.0.1-alt1
- Fix:
  + frozen current date
  + crash after closing the settings window
  + bug with same geocodes on the different widget instances
  + start widget size
  + invalid geocoder request when coordinates are not set

* Tue Oct 03 2023 Slava Aseev <ptrnine@altlinux.org> 1.0.0-alt1
- Initial build for ALT

