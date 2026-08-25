%define oname org.kde.plasma.advanced-weather-widget
%define onameLC plasma_applet_%oname 

Name: plasma-applet-advanced-weather-widget
Version: 1.7.2
Release: alt1

Summary: Modern weather widget for KDE
License: GPL-2.0-or-later
Group: Graphical desktop/KDE

Url: https://store.kde.org/p/2349879
Vcs: https://github.com/pnedyalkov91/advanced-weather-widget

Source: %name-%version.tar

BuildArch: noarch

%description
Advanced Weather Widget for KDE Plasma 6 provides accurate forecasts
with multi-provider support (Open-Meteo, MET Norway, OpenWeatherMap,
WeatherAPI, Pirate Weather, Tomorrow.io, Visual Crossing, StormGlass,
Weatherbit, and QWeather), automatic location detection, reverse geocoding,
timezone, and altitude detection.

%prep
%setup

%build
rm -r -v contents/locale

%install
install -d %buildroot%_datadir/plasma/plasmoids/%oname
mv contents %buildroot%_datadir/plasma/plasmoids/%oname/
mv metadata.json %buildroot%_datadir/plasma/plasmoids/%oname/

for locale in translate/*.po; do
 dirname=$(basename "$locale" .po)
 mkdir -p %buildroot%_datadir/locale/${dirname}/LC_MESSAGES
 msgfmt -o "%buildroot%_datadir/locale/${dirname}/LC_MESSAGES/%onameLC.mo" "$locale"
done

%find_lang %onameLC --with-kde --all-name

%files -f %onameLC.lang
%_datadir/plasma/plasmoids/%oname

%changelog
* Wed Aug 26 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.7.2-alt1
- Initial build.
