Name: blueberry
Version: 1.1.8
Release: alt1
Summary: A Bluetooth configuration tool
License: GPLv3
Group: System/Configuration/Hardware
Url: https://github.com/linuxmint/blueberry

Obsoletes: blueman
Provides: blueman

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
Requires: libgtk+3-gir libgnome-bluetooth-gir rfkill wmctrl gnome-bluetooth

%description
Utility for Bluetooth devices graphical configuration

%prep
%setup -q
%patch0 -p1

%build
%make

%install
%make DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%_sysconfdir/xdg/autostart/%name-tray.desktop
%_bindir/*
%_datadir/%name
%_desktopdir/%name.desktop
%_datadir/glib-2.0/schemas/*.xml
%_iconsdir/hicolor/*/status/*

%changelog
* Thu Nov 24 2016 Vladimir Didenko <cow@altlinux.org> 1.1.8-alt1
- 1.1.8
- add gnome-bluetooth to requires

* Tue Jul 12 2016 Valery Inozemtsev <shrek@altlinux.ru> 1.1.5-alt1
- 1.1.5
- obsoletes blueman
- updates tray icons

* Fri Dec 18 2015 Vladimir Didenko <cow@altlinux.org> 1.1.0-alt1
- 1.1.0

* Sat Jun 27 2015 Vladimir Didenko <cow@altlinux.org> 1.0.9-alt2
- add wmctrl to deps

* Sat Jun 27 2015 Vladimir Didenko <cow@altlinux.org> 1.0.9-alt1
- 1.0.9
- added missed deps (closes: #31108)

* Fri Mar 27 2015 Vladimir Didenko <cow@altlinux.org> 1.0.3-alt1
- initial release
