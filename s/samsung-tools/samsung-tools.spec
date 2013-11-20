Name: samsung-tools
Version: 2.3
Release: alt1

Summary: Tools for Samsung netbooks
License: GPLv3+
Group: System/Configuration/Hardware
URL: https://launchpad.net/samsung-tools
Source0: https://launchpad.net/samsung-tools/trunk/2.1/+download/%name-%version.tar.gz

Patch0: samsung-tools-2.2-alt-systemd-path.patch

BuildArch: noarch

# Automatically added by buildreq on Tue May 08 2012 (-bb)
# optimized out: python-base
BuildRequires: dbus-tools python-module-distribute rpm-build-gir

Requires: xbindkeys rfkill vbetool pm-utils

%description
'Samsung Tools' is the successor of 'Samsung Scripts' provided by the 'Linux
On My Samsung' project.

It allows the complete configuration and the control in a friendly way of the
devices found on Samsung netbooks (bluetooth, wireless, webcam, backlight, CPU
fan, special keys) and the control of various aspects related to power
management, like the undervolting of the CPU (when a PHC-enabled kernel is
available).

%prep
%setup -q
%patch0 -p1

%build

%install
%make_install DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%doc README TODO debian/changelog debian/upstart
%_unitdir/samsung-tools.service
%_sysconfdir/%name
%_sysconfdir/dbus-1
%_sysconfdir/xdg/autostart/*.desktop
%_bindir/*
%_libexecdir/pm-utils/power.d/samsung-tools_devices-power-management
%_libexecdir/pm-utils/power.d/samsung-tools_usb-autosuspend
%_libexecdir/pm-utils/power.d/samsung-tools_vm-writeback-time
%_libexecdir/pm-utils/sleep.d/20_samsung-tools
%_datadir/applications/%name-preferences.desktop
%_datadir/dbus-1/*/*
%_datadir/%name

%changelog
* Wed Nov 20 2013 Igor Zubkov <icesik@altlinux.org> 2.3-alt1
- 2.3

* Mon Sep 02 2013 Igor Zubkov <icesik@altlinux.org> 2.2-alt1
- 2.1 -> 2.2
- Add pm-utils to package requires
- Add systemd service file
- Change BuildArch to noarch

* Fri May 11 2012 Igor Zubkov <icesik@altlinux.org> 2.1-alt4
- Add vbetool to package requires

* Tue May 08 2012 Igor Zubkov <icesik@altlinux.org> 2.1-alt3
- Add rfkill to package requires

* Tue May 08 2012 Igor Zubkov <icesik@altlinux.org> 2.1-alt2
- Add xbindkeys to package requires

* Tue May 08 2012 Igor Zubkov <icesik@altlinux.org> 2.1-alt1
- build for Sisyphus

