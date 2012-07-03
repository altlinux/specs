%define _name alarm-clock
%define ver_major 0.3

Name: %_name-applet
Version: %ver_major.2
Release: alt1

Summary: GNOME Alarm Clock Applet
Group: Graphical desktop/GNOME
License: GPL
Url: http://%_name.pseudoberries.com

Source: http://launchpad.net/%_name/trunk/%version/+download/%_name-applet-%version.tar.gz

BuildRequires: intltool gnome-common rpm-build-gnome
BuildRequires: libgtk+2-devel GConf libGConf-devel gstreamer-devel
BuildRequires: libunique-devel libnotify-devel gnome-icon-theme

%description
Alarm Clock is a fully-featured alarm clock for notification area of
GNOME panel or equivalent. It's easy to use yet powerful with support
for multiple repeatable alarms, as well as snoozing and a flexible
notification system.

%prep
%setup

%build
%autoreconf
%configure \
	--disable-schemas-install

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang --with-gnome %name

%post
%gconf2_install %_name

%preun
if [ $1 = 0 ]; then
%gconf2_uninstall %_name
fi

%files -f %_name-applet.lang
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/%name
%_iconsdir/hicolor/*/*/*
%config %gconf_schemasdir/%_name.schemas
%doc AUTHORS README NEWS

%changelog
* Sat Apr 07 2012 Yuri N. Sedunov <aris@altlinux.org> 0.3.2-alt1
- first build for Sisyphus



