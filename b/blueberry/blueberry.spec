Name: blueberry
Version: 1.1.0
Release: alt1

Summary: A Bluetooth configuration tool
License: %gpl3only
Group: System/Configuration/Hardware
Url: https://github.com/linuxmint/blueberry

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-licenses
Requires: rfkill wmctrl
Requires: libgtk+3-gir, libgnome-bluetooth-gir

%description
The Blueberry is a front-end to gnome-bluetooth. Supposed to be
used for bluetooth configuration in Cinnamon, MATE, Xfce, GNOME
and Unity.

%prep
%setup -q
%patch0 -p1

%build
make all

%install
make install DESTDIR=%{buildroot}
%find_lang %name

%files -f %name.lang
%doc README.md
%_sysconfdir/xdg/autostart/%name-tray.desktop
%_bindir/*
%_datadir/%name
%_datadir/applications/*.desktop
%_datadir/glib-2.0/schemas/*.xml
%_datadir/icons/hicolor/*/status/*


%changelog
* Fri Dec 18 2015 Vladimir Didenko <cow@altlinux.org> 1.1.0-alt1
- 1.1.0

* Sat Jun 27 2015 Vladimir Didenko <cow@altlinux.org> 1.0.9-alt2
- add wmctrl to deps

* Sat Jun 27 2015 Vladimir Didenko <cow@altlinux.org> 1.0.9-alt1
- 1.0.9
- added missed deps (closes: #31108)

* Fri Mar 27 2015 Vladimir Didenko <cow@altlinux.org> 1.0.3-alt1
- initial release
