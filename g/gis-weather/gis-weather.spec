Name:		gis-weather
Version:	0.8.0
Release:	alt1.1
License:	GPLv3
Summary:	Customizable weather widget
Url:		http://sourceforge.net/projects/gis-weather
Group:		Accessibility
Source:		%name-%version.tar.gz
Source1:	gis-weather
Source2:	gis-weather.desktop

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-gir

# Automatically added by buildreq on Wed Jul 08 2015 (-bi)
# optimized out: python-base
BuildRequires: dos2unix python3 rpm-build-gir

Requires: python3-module-pygobject3 python3-module-pycairo

%add_python3_compile_include %_datadir/%name
# libaptindicator is not package in ALT Linux
%add_typelib_req_skiplist typelib(AppIndicator3)

%description
Customizable weather widget.
Features
  * View weather for several days
  * Detailed weather forecast for today and tomorrow
  * Fast switching between cities
  * Select the background and theme weather icons
  * "Compass" with the wind direction, with adjustable angle of rotation
  * Highlighting the high wind
  * Support weather services:
    * Gismeteo.com
    * AccuWeather.com
  * Support SVG and widget scale
  * Indicator to panel
  * Presets

%prep
%setup

%build
dos2unix ./dialogs/settings_dialog.py

%install
install -Dm 0755 %SOURCE1 %buildroot%_bindir/%name
install -Dm 0644 %SOURCE2 %buildroot%_datadir/applications/%name.desktop
install -dm 0755 %buildroot%_datadir/%name
echo rpm > %buildroot%_datadir/%name/package
cp -a {dialogs,gis-weather.py,icon.png,i18n,services,themes,utils} %buildroot%_datadir/%name/
grep -rl '^#!' %buildroot%_datadir/%name/ | xargs chmod 0755

%files
%doc README.md
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/%name

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Dec 04 2015 Motsyo Gennadi <drool@altlinux.ru> 0.8.0-alt1
- 0.8.0

* Fri Nov 06 2015 Motsyo Gennadi <drool@altlinux.ru> 0.7.9-alt1
- 0.7.9

* Sun Aug 23 2015 Motsyo Gennadi <drool@altlinux.ru> 0.7.8.7-alt1
- 0.7.8.7

* Mon Jul 06 2015 Motsyo Gennadi <drool@altlinux.ru> 0.7.8.5-alt1
- initial build for ALT Linux from OpenSUSE package
