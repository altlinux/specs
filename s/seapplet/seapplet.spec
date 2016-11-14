Name: seapplet
Version: 0.3.5
Release: alt1

Summary: Applet for selinux
License: GPL
Group: System/Configuration/Packaging
Packager: Andrey Kolotov <qwest@altlinux.org>

Source: %name-%version.tar

BuildRequires: gcc-c++ libqt4-devel librtmp libselinux-devel

%description
Applet for selinux.


%prep
%setup -q -n %name-%version
%qmake_qt4

%build
%make
lrelease-qt4 security.pro

%install
%make INSTALL_ROOT=%buildroot install

mkdir -p %buildroot/%_datadir/%name/translations/
install -m644 translations/seapplet_*.qm %buildroot/%_datadir/%name/translations/
mkdir -p %buildroot/%_datadir/applications/
install -m644 %name.desktop %buildroot/%_datadir/applications/%name.desktop

mkdir -p %buildroot/%_sysconfdir/xdg/autostart/
install -m644 %name.desktop %buildroot/%_sysconfdir/xdg/autostart/%name.desktop

%files
#%doc README
%_bindir/*
%_datadir/%name
%_datadir/applications/%name.desktop
%_sysconfdir/xdg/autostart/%name.desktop


%changelog
* Mon Nov 14 2016 Sergey V Turchin <zerg at altlinux dot org> 0.3.5-alt1
- fix autostart in MATE

* Fri Apr 08 2016 Sergey V Turchin <zerg at altlinux dot org> 0.3.4-alt0.M70C.1
- build for M70C

* Fri Apr 08 2016 Sergey V Turchin <zerg at altlinux dot org> 0.3.4-alt1
- fix show initial state of categories
- fix autostart in MATE
- code cleanup

* Wed Dec 18 2013 Timur Aitov <timonbl4@altlinux.org> 0.3.3-alt1.1
- send to build

* Fri Sep 20 2013 Andrey Kolotov <qwest@altlinux.org> 0.3.3-alt1
- lowlevel category print and check in tray by default

* Tue Sep 18 2013 Andrey Kolotov <qwest@altlinux.org> 0.3.2-alt1
- by default lowlevel range instead of s0

* Fri Sep 13 2013 Andrey Kolotov <qwest@altlinux.org> 0.3.1-alt1
- fix bug number in pid file

* Thu Sep 12 2013 Andrey Kolotov <qwest@altlinux.org> 0.3.0-alt1
- new algorithm based on shmget().
- not used files in /dev/shm/
- used pid files in /tmp/secure/
- rewritten function:
  * Tray::SaveTip()
  * Tray::SaveTip_destroy()
  * SaveTip_destroy()
  * Policity_read()
- new function:
  * Pidfile_create()
  * Pidfile_get()

* Wed Jun 19 2013 Timur Aitov <timonbl4@altlinux.org> 0.2.0-alt1
- print color code

* Tue Jun 18 2013 Andrey Kolotov <qwest@altlinux.org> 0.1.1-alt1
- Changed the colors of the indicator (closes: #29083).
- Fixed selecting the last level (closes: #29084).

* Mon Apr 29 2013 Andriy Stepanov <stanv@altlinux.ru> 0.1.0-alt1
- Initial release
