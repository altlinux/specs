%define origver 1-3-1

Name: fgo
Version: 1.3.1
Release: alt1

Summary: A simple launcher for FlightGear flight simulator
License: distributable
Group: Games/Other

Url: http://sites.google.com/site/erobosprojects/flightgear/add-ons/fgo
Source0: %url/download/%name-%origver.tar.gz
Source1: %name.desktop
Source2: %name.6
Source3: %name.watch
Patch0:  %name-config.patch
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch
Requires: FlightGear >= 2.0.0

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
%patch0 -p1

%build

%install
install -pDm755 %name %buildroot%fgodir/%name
cp -a src/ %buildroot%fgodir

install -d %buildroot%_gamesbindir
ln -s `relative %fgodir/%name %_gamesbindir/%name` \
	%buildroot%_gamesbindir/%name

install -pDm644 %SOURCE1 %buildroot%_desktopdir/%name.desktop
install -pDm644 %SOURCE2 %buildroot%_man6dir/%name.6
install -pDm644 src/pics/icon.png %buildroot%_liconsdir/%name.png

%files
%_gamesbindir/%name
%fgodir/
%_desktopdir/%name.desktop
%_liconsdir/%name.png
%_man6dir/%name.6*
%doc docs/

%changelog
* Wed Mar 28 2012 Michael Shigorin <mike@altlinux.org> 1.3.1-alt1
- built for ALT Linux
  + packaging stuff heavily derived from Debian
