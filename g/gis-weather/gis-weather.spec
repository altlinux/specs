Name:		gis-weather
Version:	0.8.4.17
Release:	alt2
License:	GPLv3
Summary:	Customizable weather widget

# 		https://github.com/RingOV/gis-weather
Url:		http://sourceforge.net/projects/gis-weather
Group:		Accessibility
Packager:       Motsyo Gennadi <drool@altlinux.ru>
Source:		%name-%version.tar
Source1:	gis-weather
Source2:	gis-weather.desktop

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-gir

BuildRequires: dos2unix libappindicator-gtk3

# BEGIN SourceDeps(oneline):
BuildRequires: python3(cairo) python3(changelog) python3(distro) python3(gi) python3(gi.repository) python3-base
# END SourceDeps(oneline)


Requires: python3-module-pygobject3 python3-module-pycairo libgtk+3-gir

%add_python3_path %_datadir/%name
# This is not realy needed here (when there are no subpackages), because
# all of the deps get self-satisfied internally in python3.req.py
# (but in future that feature may be turned off):
%allow_python3_import_path %_datadir/%name
# More precise deps:
%python3_req_hier
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
install -Dm 0644 %SOURCE2 %buildroot%_desktopdir/%name.desktop
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
* Tue Jul 16 2024 Hihin Ruslan <ruslandh@altlinux.ru> 0.8.4.17-alt2
- Add requires libgtk+3-gir

* Tue Oct 03 2023 Hihin Ruslan <ruslandh@altlinux.ru> 0.8.4.17-alt1
- Update from github (ALT #47590)

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 0.8.1-alt1.1
- Rebuild with python3.7.

* Thu Oct 12 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.1-alt1
- 0.8.1 (thx Motsyo Gennadi <drool@>)

* Tue Oct 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.0-alt1.2
- rebuild with rpm-build-python3-0.1.10.10-alt1 (more deps are found)
- %%python3_req_hier for more precise deps.

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
