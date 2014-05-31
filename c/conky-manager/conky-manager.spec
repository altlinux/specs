Name: conky-manager
Version: 1.2
Release: alt1
Summary: A simple GUI for managing Conky config files
Group: Monitoring
License: GPLv3+
Url: https://launchpad.net/conky-manager

Source0: %name-%version.tar.gz

Requires: conky
Requires: lm_sensors
Requires: hddtemp
Requires: p7zip

BuildRequires: libgee-devel libgtk+3-devel vala

%description
A simple GUI for managing Conky config files. Options for changing themes and
running Conky at startup build and packaged for fedora, more info
about the code, licence and credits at https://launchpad.net/conky-manager.

%prep
%setup

%build
%make_build

%install
make DESTDIR=%buildroot install

%files
%doc COPYING README THANKS TODO

%_bindir/conky-manager
%_desktopdir/conky-manager.desktop
%_datadir/conky-manager
%_pixmapsdir/conky-manager.png

%changelog
* Sat May 31 2014 Motsyo Gennadi <drool@altlinux.ru> 1.2-alt1
- initial build for ALT Linux
