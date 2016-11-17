Name: conky-manager
Version: 2.3.4
Release: alt1
Summary: A simple GUI for managing Conky config files
Group: Monitoring
License: GPLv3+
Url: https://launchpad.net/conky-manager

Source0: %name-%version.tar.gz

Patch0: %name-desktopentry-fixer-and-arabizer.patch

Requires: conky
Requires: lm_sensors3
Requires: hddtemp
Requires: p7zip p7zip-standalone

# Automatically added by buildreq on Thu Nov 17 2016 (-bi)
# optimized out: at-spi2-atk elfutils fontconfig glib2-devel libX11-devel libat-spi2-core libatk-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgpg-error libjson-glib libpango-devel libwayland-client libwayland-cursor libwayland-egl libwayland-server pkg-config python-base python-modules
BuildRequires: libgee0.8-devel libgtk+3-devel libjson-glib-devel vala

%description
A simple GUI for managing Conky config files. Options for changing themes and
running Conky at startup build and packaged for fedora, more info
about the code, licence and credits at https://launchpad.net/conky-manager.

%prep
%setup
%patch0 -p0

%build
subst 's|/usr/share/${app_name}/libs|%_libdir/${app_name}/libs|g' src/makefile
%make_build

%install
make DESTDIR=%buildroot install
mkdir -p %buildroot%_libdir/%name/libs

%find_lang %name

%files -f %name.lang
%doc COPYING README THANKS TODO
%dir %_libdir/%name
%dir %_libdir/%name/libs
%_bindir/conky-manager
%_desktopdir/conky-manager.desktop
%_datadir/conky-manager
%_datadir/appdata/*.xml
%_pixmapsdir/conky-manager.png

%changelog
* Thu Nov 17 2016 Motsyo Gennadi <drool@altlinux.ru> 2.3.4-alt1
- 2.3.4

* Sun May 03 2015 Motsyo Gennadi <drool@altlinux.ru> 2.3.1-alt1
- 2.3.1 (altbug #30984)

* Sat May 31 2014 Motsyo Gennadi <drool@altlinux.ru> 1.2-alt1
- initial build for ALT Linux
