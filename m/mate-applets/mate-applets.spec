%define _libexecdir %_prefix/libexec

Name: mate-applets
Version: 1.20.0
Release: alt1
Epoch: 1
Summary: MATE Desktop panel applets
License: GPLv2+ and LGPLv2+
Group: Graphical desktop/MATE
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: mate-netspeed = %version-%release
Obsoletes: mate-netspeed

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: mate-common intltool itstool libSM-devel libapm-devel libdbus-glib-devel libgtksourceview3-devel
BuildRequires: libgtop-devel libgucharmap-devel libmateweather-devel libnotify-devel libpolkit-devel libupower-devel
BuildRequires: libwireless-devel libwnck3-devel libxml2-devel mate-panel-devel yelp-tools

%description
MATE Desktop panel applets

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--disable-schemas-compile \
	--disable-static \
	--enable-polkit \
	--enable-ipv6 \
	--enable-stickynotes \
	--libexecdir=%_libexecdir/%name \
	--disable-cpufreq \
	--enable-frequency-selector=no

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %name --with-gnome --all-name

%files -f %name.lang
%doc AUTHORS COPYING README
%_sysconfdir/sound/events/mate-battstat_applet.soundlist
%_libexecdir/%name
%_datadir/%name
%_datadir/mate/ui/*.xml
%_datadir/mate-panel/applets/*
%_datadir/pixmaps/mate-accessx-status-applet
%_datadir/glib-2.0/schemas/*.xml
%_datadir/dbus-1/services/*.service
%_iconsdir/hicolor/*/*/*
%_man1dir/*.1*

%changelog
* Mon Mar 19 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.0-alt1
- initial build from git.mate-desktop.org
- disabled cpufreq

* Wed Feb 21 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release

