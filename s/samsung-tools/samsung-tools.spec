Name: samsung-tools
Version: 2.1
Release: alt4

Summary: Tools for Samsung netbooks
License: GPLv3+
Group: System/Configuration/Hardware
URL: https://launchpad.net/samsung-tools
Source0: https://launchpad.net/samsung-tools/trunk/2.1/+download/%name-%version.tar.gz

# Automatically added by buildreq on Tue May 08 2012 (-bb)
# optimized out: python-base
BuildRequires: dbus-tools python-module-distribute rpm-build-gir

Requires: xbindkeys rfkill vbetool

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

%build

%install
%make_install DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%doc debian/README.Debian debian/changelog debian/upstart
%_bindir/*
%_sysconfdir/%name
%_sysconfdir/dbus-1
%_sysconfdir/pm/
%_sysconfdir/xdg/autostart/*.desktop
%_datadir/applications/%name-preferences.desktop
%_datadir/dbus-1/*/*
%_prefix/lib/%name

%changelog
* Fri May 11 2012 Igor Zubkov <icesik@altlinux.org> 2.1-alt4
- Add vbetool to package requires

* Tue May 08 2012 Igor Zubkov <icesik@altlinux.org> 2.1-alt3
- Add rfkill to package requires

* Tue May 08 2012 Igor Zubkov <icesik@altlinux.org> 2.1-alt2
- Add xbindkeys to package requires

* Tue May 08 2012 Igor Zubkov <icesik@altlinux.org> 2.1-alt1
- build for Sisyphus

