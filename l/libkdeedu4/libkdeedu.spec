%add_findpackage_path %_kde4_bindir

%define rname libkdeedu
Name: libkdeedu4
Version: 15.12.1
Release: alt1

Group: System/Libraries
Summary: Base KDEEDU library
Url: http://projects.kde.org/projects/kde/kdeedu/libkdeedu
License: GPLv2+

Provides: libkeduvocdocument4 = %version-%release
Obsoletes: libkeduvocdocument4 < %version-%release
Provides: kde4edu-core = %version-%release
Obsoletes: kde4edu-core < %version-%release

Source: %rname-%version.tar

# Automatically added by buildreq on Fri Sep 16 2011 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-test libqt4-xml libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base ruby xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4libs-devel libqt3-devel rpm-build-ruby zlib-devel-static
BuildRequires: gcc-c++ glib2-devel kde4libs-devel zlib-devel kde-common-devel

%description
Base KDEEDU library

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
License: LGPLv2 or GPLv3
Requires: %name = %version-%release
%description devel
Development files for %name

%prep
%setup -qn %rname-%version


%build
%K4build


%install
%K4install


%files
%doc README AUTHORS
%_K4libdir/libkeduvocdocument.so.*
%if 0
%_K4apps/kvtml/
%_K4iconsdir/hicolor/*/actions/coords.*
%_K4iconsdir/hicolor/*/actions/deriv_func.*
%_K4iconsdir/hicolor/*/actions/editconstants.*
%_K4iconsdir/hicolor/*/actions/editplots.*
%_K4iconsdir/hicolor/*/actions/func.*
%_K4iconsdir/hicolor/*/actions/functionhelp.*
%_K4iconsdir/hicolor/*/actions/integral_func.*
%_K4iconsdir/hicolor/*/actions/lessen.*
%_K4iconsdir/hicolor/*/actions/magnify.*
%_K4iconsdir/hicolor/*/actions/maximum.*
%_K4iconsdir/hicolor/*/actions/minimum.*
%_K4iconsdir/hicolor/*/actions/newdifferential.*
%_K4iconsdir/hicolor/*/actions/newfunction.*
%_K4iconsdir/hicolor/*/actions/newimplicit.*
%_K4iconsdir/hicolor/*/actions/newparametric.*
%_K4iconsdir/hicolor/*/actions/newpolar.*
%_K4iconsdir/hicolor/*/actions/resetview.*
%endif

%files devel
%_K4libdir/libqtmmlwidget.a
%_K4libdir/cmake/libkdeedu/
%_K4includedir/libkdeedu/
%_K4link/lib*.so
#%_pkgconfigdir/libkdeedu.pc



%changelog
* Tue Feb 02 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.1-alt1
- new version

* Wed Apr 22 2015 Sergey V Turchin <zerg@altlinux.org> 15.4.0-alt1
- new version

* Thu Jan 29 2015 Sergey V Turchin <zerg@altlinux.org> 14.12.1-alt1
- new version

* Mon Nov 17 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.3-alt1
- new version

* Thu Sep 18 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.1-alt1
- new version

* Thu Aug 14 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.0-alt1
- new version

* Fri Oct 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt0.M70P.1
- built for M70P

* Fri Sep 06 2013 Sergey V Turchin <zerg@altlinux.org> 4.11.1-alt1
- new version

* Fri Jul 05 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.5-alt1
- new version

* Tue Jun 04 2013 Sergey V Turchin <zerg@altlinux.org> 4.10.4-alt1
- new version

* Mon Dec 17 2012 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.1
- new beta version

* Wed Oct 03 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.1-alt1
- new version

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt0.M60P.1
- built for M60P

* Wed Jan 25 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60P.1
- built for M60P

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt0.M60T.1
- built for M60T

* Fri Sep 09 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- initial build
