%define _libexecdir %_prefix/libexec

Name: mate-applets
Version: 1.20.1
Release: alt2
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

BuildRequires: mate-common intltool itstool libSM-devel libdbus-glib-devel libgtksourceview3-devel
BuildRequires: libgtop-devel libgucharmap-devel libmateweather-devel libnotify-devel libpolkit-devel libupower-devel
BuildRequires: libwireless-devel libwnck3-devel libxml2-devel mate-panel-devel yelp-tools
%ifnarch s390 s390x sparc64 %e2k
# no cpupower as well if it's ever needed here
BuildRequires: libapm-devel
%endif

%description
MATE Desktop panel applets

%prep
%setup
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
%makeinstall_std

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
* Sat May 05 2018 Michael Shigorin <mike@altlinux.org> 1:1.20.1-alt2
- avoid apm on platforms without it

* Tue Mar 27 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.1-alt1
- 1.20.1

* Mon Mar 19 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.0-alt1
- initial build from git.mate-desktop.org
- disabled cpufreq

* Wed Feb 21 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release

