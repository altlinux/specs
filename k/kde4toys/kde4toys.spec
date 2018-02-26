
%add_findpackage_path %_kde4_bindir

%define rname kdetoys
Name: kde4toys
%define major 4
%define minor 8
%define bugfix 0
Version: %major.%minor.%bugfix
Release: alt1

Group: Graphical desktop/KDE
Summary: K Desktop Environment - Toys and Amusements
Url: http://www.kde.org/
License: GPL

#Requires: %name-kweather = %version-%release
Requires: %name-amor = %version-%release
Requires: %name-ktux = %version-%release
Requires: %name-kteatime = %version-%release

#Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%rname-%version.tar.bz2
Source: %rname-%version.tar

BuildRequires(pre): kde4base-runtime-devel kde4base-workspace-devel
BuildRequires: gcc-c++ libjpeg-devel
BuildRequires: kde4base-runtime-devel >= %version kde4base-workspace-devel >= %version

%description
Toys for the K Desktop Environment.

Software included in this package are:
	- amor: Amusing Misuse Of Resources put's comic figures above your windows
	- kteatime: system tray applet that makes sure your tea doesn't get too strong
	- ktux: Tux-in-a-Spaceship screen saver
	- kweather: plasma applet that will display the current weather outside

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common >= %major.%minor
Conflicts: kdetoys-common <= 3.5.12-alt1
%description common
%name common package

%package kweather
Group: Graphical desktop/KDE
Summary: Plasma applet that will display the current weather outside
Requires: %name-common = %version-%release
%description kweather
Plasma applet that will display the current weather outside

%package amor
Group: Graphical desktop/KDE
Summary: Amusing Misuse Of Resources put's comic figures above your windows
Requires: %name-common = %version-%release
%description amor
Amusing Misuse Of Resources put's comic figures above your windows

%package ktux
Group: Graphical desktop/KDE
Summary: Tux-in-a-Spaceship screen saver
Requires: %name-common = %version-%release
%description ktux
Tux-in-a-Spaceship screen saver

%package kteatime
Group: Graphical desktop/KDE
Summary: System tray applet that makes sure your tea doesn't get too strong
Requires: %name-common = %version-%release
%description kteatime
System tray applet that makes sure your tea doesn't get too strong

%package devel
Summary: Header files for %name
Group: Development/KDE and QT
Requires: kde4libs-devel
Requires: %name-common = %version-%release
%description devel
This package includes the header files you will need to compile
applications for %name


%prep
%setup -q -n %rname-%version


%build
%K4build


%install
%K4install

%files
%files common
%doc README

#%files kweather
#%_K4bindir/kweatherreport
#%_K4bindir/kweatherservice
#%_K4libdir/libkdeinit4_kweatherreport.so
#%_K4lib/kcm_weather.so
#%_K4lib/kcm_weatherservice.so
#%_K4apps/kweather
#%_K4apps/kweatherservice
#%_K4srv/kweatherservice.desktop
#%_K4srv/kcmweather.desktop
#%_K4srv/kcmweatherservice.desktop
#%_K4iconsdir/hicolor/*/apps/kweather.png
#%_K4doc/*/kweather

%files amor
%_K4bindir/amor
%_K4apps/amor
%_K4xdg_apps/amor.desktop
%_K4iconsdir/hicolor/*/apps/amor.png
%_K4doc/*/amor

%files ktux
%_K4bindir/ktux
%_K4apps/ktux
%_K4srv/ScreenSavers/ktux.desktop
%_K4iconsdir/hicolor/*/apps/ktux.png

%files kteatime
%_K4bindir/kteatime
%_K4apps/kteatime
%_K4xdg_apps/kteatime.desktop
%_K4iconsdir/hicolor/*/apps/kteatime.*
%_K4doc/*/kteatime

%files devel
#%_K4link/*
%_K4dbus_interfaces/*

%changelog
* Fri Jan 27 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60P.1
- built for M60P

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60T.1
- built for M60T

* Sun Sep 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- new version

* Fri Jun 10 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.4-alt1
- new version

* Tue May 10 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.3-alt1
- new version

* Tue Apr 12 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt1
- new version

* Fri Mar 04 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.1-alt1
- new version
- move to standart place

* Thu Feb 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt1
- new version

* Wed Jan 19 2011 Sergey V Turchin <zerg@altlinux.org> 4.5.5-alt1
- new version

* Wed Dec 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.4-alt1
- new version

* Wed Nov 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.3-alt1
- new version

* Thu Oct 07 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.2-alt1
- new version

* Wed Sep 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.1-alt1
- new version

* Mon Aug 09 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.0-alt1
- new version

* Thu Jul 08 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt0.M51.1
- built for M51

* Mon Jul 05 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt1
- new version

* Thu Jun 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt0.M51.1
- built for M51

* Wed Jun 02 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt1
- new version

* Thu May 13 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt0.M51.1
- built for M51

* Wed May 12 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt1
- new version

* Wed Apr 21 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt0.M51.1
- built for M51

* Wed Mar 31 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt1
- new version

* Tue Mar 02 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.1-alt1
- new version

* Fri Feb 12 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.0-alt1
- new version

* Thu Jan 28 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.95-alt1
- new version

* Mon Jan 25 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.90-alt1
- new version

* Tue Dec 15 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt0.M51.1
- built for M51

* Tue Dec 01 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt1
- new version

* Mon Nov 09 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt0.M51.1
- built for M51

* Thu Nov 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt1
- new version

* Mon Oct 12 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.2-alt1
- new version

* Tue Sep 01 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.1-alt1
- new version

* Wed Aug 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.0-alt1
- 4.3.0

* Thu Jul 23 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.98-alt1
- 4.2.98

* Mon Jul 20 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.96-alt1
- 4.2.96

* Mon Jun 22 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt0.M50.1
- built for M50

* Tue Jun 09 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt1
- new version

* Tue May 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.3-alt1
- new version

* Mon Apr 06 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.2-alt1
- new version

* Fri Mar 06 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.1-alt1
- new version

* Thu Jan 29 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.0-alt1
- new version

* Thu Jan 22 2009 Sergey V Turchin <zerg at altlinux dot org> 4.1.96-alt1
- new version

* Fri Nov 07 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.3-alt1
- new version

* Fri Oct 24 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.2-alt1
- initial specfile
