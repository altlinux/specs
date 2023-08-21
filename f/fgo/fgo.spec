%define fgodir %_gamesdatadir/%name

%filter_from_requires '/python2.*/d'

Name: fgo
Version: 1.5.5
Release: alt2.1

Summary: A simple launcher for FlightGear flight simulator
License: distributable
Group: Games/Other
Url: http://sites.google.com/site/erobosprojects/flightgear/add-ons/fgo
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch

Source0: %url/download/%name-%version.tar.gz
Source1: %name.desktop
Source2: %name.6
Source3: %name.watch

Patch0: port-to-python3.patch

BuildRequires(pre): rpm-build-python3
Requires: FlightGear >= 2.0.0

%description
FGo! is a fast and simple way to start FlightGear session in
GNU/Linux operating system. Like other such applications (e.g.
FGRun) FGo! allows you to easily select an aircraft, airport,
scenario, etc. It's also provides a convenient way to run
TerraSync.

What distinguishes it from other such applications is the text
window allowing you to write any other, more advanced command
line options that will be passed to FlightGear. This is similar
to editing the .fgfsrc configuration file.

You can actually think about FGo! as the configuration file
editor with some useful gadgets :)

%prep
%setup -n %name
%patch0 -p2

cat >> data/config/presets << __EOF__

--airport=KSFO
--fg-root=/usr/share/flightgear/
--fg-scenery=/usr/share/flightgear/Scenery
AI_SCENARIOS=
APT_DATA_SOURCE=0
FG_BIN=/usr/bin/fgfs
FG_WORKING_DIR=
FILTER_APT_LIST=0
TERRASYNC=0
TERRASYNC_BIN=/usr/bin/terrasync
TERRASYNC_PORT=5501
TERRASYNC_SCENERY=
__EOF__

%build

%install
install -pDm755 %name %buildroot%fgodir/%name
cp -a data/ src/ %buildroot%fgodir

install -d %buildroot%_gamesbindir
ln -s `relative %fgodir/%name %_gamesbindir/%name` \
	%buildroot%_gamesbindir/%name

install -pDm644 %SOURCE1 %buildroot%_desktopdir/%name.desktop
install -pDm644 %SOURCE2 %buildroot%_man6dir/%name.6
install -pDm644 share/icons/48x48/fgo.png %buildroot%_liconsdir/%name.png

# adding shebang to make them visible for python3.req.py
find %buildroot%fgodir/src/ -name \*.py -exec sed -i '1 i#!/usr/bin/env python3' {} +
find %buildroot%fgodir/src/ -name \*.py -exec chmod +x {} +

%files
%_gamesbindir/%name
%fgodir/
%_desktopdir/%name.desktop
%_liconsdir/%name.png
%_man6dir/%name.6*
%doc docs/*

%changelog
* Sat Aug 12 2023 Daniel Zagaynov <kotopesutility@altlinux.org> 1.5.5-alt2.1
- NMU: added shebang to %%fgodir/src python3-modules and made them executable
       to make them visible to python3.req.py

* Wed Mar 25 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.5.5-alt2
- Porting to python3.

* Fri Dec 26 2014 Michael Shigorin <mike@altlinux.org> 1.5.5-alt1
- new version (watch file uupdate)

* Tue Jun 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt1.1
- NMU: fixed watch file

* Thu Mar 27 2014 Michael Shigorin <mike@altlinux.org> 1.5.2-alt1
- new version (watch file uupdate)

* Tue Mar 11 2014 Michael Shigorin <mike@altlinux.org> 1.5.1-alt1
- new version (watch file uupdate)

* Thu Mar 06 2014 Michael Shigorin <mike@altlinux.org> 1.5.0-alt1
- new version (watch file uupdate)

* Tue Feb 11 2014 Michael Shigorin <mike@altlinux.org> 1.4.5-alt1
- new version (watch file uupdate)

* Wed Mar 28 2012 Michael Shigorin <mike@altlinux.org> 1.3.1-alt1
- built for ALT Linux
  + packaging stuff heavily derived from Debian
