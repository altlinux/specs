%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: lomiri-weather-app
Version: 6.2.0
Release: alt1

Summary: Weather App for Lomiri Operating Environment
License: GPL-3.0-only
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/apps/lomiri-weather-app

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-qt5
BuildRequires(pre): rpm-build-qml

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(flatbuffers)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5QuickControls2)
BuildRequires: pkgconfig(Qt5Location)
BuildRequires: pkgconfig(Qt5WebEngine)

Requires: libqt5-qml
Requires: libqt5-quick
Requires: qml(Lomiri.Components)
Requires: qml(Lomiri.Layouts)
Requires: qml(QtLocation)

%description
This app is a core app for Ubuntu Touch's shell Lomiri. Ubuntu Touch is
a mobile OS developed by the UBports Foundation. Lomiri is its operating
environment optimized for touch based human-machine interaction, but
also supports convergence (i.e. switching between tablet/phone and
desktop mode).

This package provides Lomiri's Weather App.

%prep
%setup
%patch -p1

%build
%cmake \
       -DCLICK_MODE=OFF \
       -DINSTALL_TESTS=OFF
%cmake_build

%install
%cmake_install

%find_lang %name --all-name

%files -f %{name}.lang
%doc AUTHORS ChangeLog LICENSE.md NEWS README.md RELEASING.md TROUBLESHOOTING.md
%_bindir/lomiri-weather-app
%dir %_qt5_qmldir/LomiriWeather
%_qt5_qmldir/LomiriWeather/libLomiriWeather.so
%_qt5_qmldir/LomiriWeather/qmldir
%_desktopdir/lomiri-weather-app.desktop
%dir %_datadir/lomiri-weather-app
%_datadir/lomiri-weather-app/weather-app-splash.svg
%_datadir/lomiri-weather-app/weather-app.svg
%_datadir/lomiri-url-dispatcher/urls/lomiri-weather-app.url-dispatcher

%exclude %_datadir/locale/it_CARES/LC_MESSAGES/lomiri-weather-app.mo
%exclude %_datadir/locale/zh_LATN@pinyin/LC_MESSAGES/lomiri-weather-app.mo

%changelog
* Fri Jul 25 2025 Nikolay Strelkov <snk@altlinux.org> 6.2.0-alt1
- Initial build for Sisyphus
