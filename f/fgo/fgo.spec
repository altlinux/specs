Name: fgo
Version: 1.5.1
Release: alt1

Summary: A simple launcher for FlightGear flight simulator
License: distributable
Group: Games/Other

Url: http://sites.google.com/site/erobosprojects/flightgear/add-ons/fgo
Source0: %url/download/%name-%version.tar.gz
Source1: %name.desktop
Source2: %name.6
Source3: %name.watch
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch
Requires: FlightGear >= 2.0.0
Requires: python-module-imaging

%define fgodir %_gamesdatadir/%name

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
install -pDm644 data/pics/icons/48x48/fgo.png %buildroot%_liconsdir/%name.png

%files
%_gamesbindir/%name
%fgodir/
%_desktopdir/%name.desktop
%_liconsdir/%name.png
%_man6dir/%name.6*
%doc docs/*

%changelog
* Tue Mar 11 2014 Michael Shigorin <mike@altlinux.org> 1.5.1-alt1
- new version (watch file uupdate)

* Thu Mar 06 2014 Michael Shigorin <mike@altlinux.org> 1.5.0-alt1
- new version (watch file uupdate)

* Tue Feb 11 2014 Michael Shigorin <mike@altlinux.org> 1.4.5-alt1
- new version (watch file uupdate)

* Wed Mar 28 2012 Michael Shigorin <mike@altlinux.org> 1.3.1-alt1
- built for ALT Linux
  + packaging stuff heavily derived from Debian
