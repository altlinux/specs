%define rname libksysguard

%ifarch %e2k ppc64le
%def_disable qtwebengine
%else
%def_enable qtwebengine
%endif

%define sover 9
%define libksgrd libksgrd%sover
%define libksignalplotter libksignalplotter%sover
%define liblsofui liblsofui%sover
%define libprocesscore libprocesscore%sover
%define libprocessui libprocessui%sover
%define sover2 1
%define libksysguardformatter libksysguardformatter%sover2
%define libksysguardfaces libksysguardfaces%sover2
%define libksysguardsensors libksysguardsensors%sover2
%define libksysguardsystemstats libksysguardsystemstats%sover2

Name: plasma5-%rname
Version: 5.26.4
Release: alt1
Epoch: 1
%K5init altplace

Group: System/Libraries
Summary: KDE Workspace 5 performance monitor library
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: kf5-libksysguard = %EVR
Obsoletes: kf5-libksysguard < %EVR
Conflicts: plasma5-ksysguard < 5.22
Requires(post): /sbin/setcap

Source: %rname-%version.tar
Patch: alt-killbtn.patch

# Automatically added by buildreq on Wed Feb 25 2015 (-bi)
# optimized out: cmake cmake-modules elfutils libEGL-devel libGL-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libcloog-isl4 libgst-plugins1.0 libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-opengl libqt5-positioning libqt5-printsupport libqt5-qml libqt5-quick libqt5-script libqt5-sensors libqt5-sql libqt5-webkit libqt5-webkitwidgets libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcb-devel libxcbutil-keysyms libxkbfile-devel python-base qt5-base-devel ruby ruby-stdlibs xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: extra-cmake-modules gcc-c++ kf5-kauth-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kitemviews-devel kf5-kpackage-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-plasma-framework-devel python-module-google qt5-script-devel qt5-webkit-devel qt5-x11extras-devel rpm-build-gir rpm-build-ruby zlib-devel-static
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules gcc-c++
BuildRequires: libsensors3-devel
BuildRequires: zlib-devel libnl-devel libcap-devel libpcap-devel
BuildRequires: qt5-script-devel qt5-x11extras-devel qt5-tools-devel
%if_enabled qtwebengine
BuildRequires: qt5-webengine-devel
%endif
BuildRequires: kf5-kauth-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-kguiaddons-devel
BuildRequires: kf5-ki18n-devel kf5-kiconthemes-devel kf5-kitemviews-devel kf5-kpackage-devel kf5-kservice-devel
BuildRequires: kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-plasma-framework-devel
BuildRequires: kf5-kglobalaccel-devel kf5-kio-devel kf5-kdeclarative-devel kf5-knewstuff-devel

%description
Performance monitor library

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
Provides: kf5-libksysguard-common = %EVR
Obsoletes: kf5-libksysguard-common < %EVR
Conflicts: plasma5-ksysguard-common < 5.22
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Provides: kf5-libksysguard-devel = %EVR
Obsoletes: kf5-libksysguard-devel < %EVR
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n polkit-kde-ksysguard
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: %name-common
%description -n polkit-kde-ksysguard
Common polkit files for %name

%package -n %libksgrd
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libksgrd
%name library

%package -n %libksignalplotter
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libksignalplotter
%name library

%package -n %libprocesscore
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Requires: polkit-kde-ksysguard
%description -n %libprocesscore
%name library

%package -n %liblsofui
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Requires: lsof
%description -n %liblsofui
%name library

%package -n %libprocessui
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libprocessui
%name library

%package -n %libksysguardformatter
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libksysguardformatter
%name library

%package -n %libksysguardfaces
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libksysguardfaces
%name library

%package -n %libksysguardsensors
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libksysguardsensors
%name library

%package -n %libksysguardsystemstats
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libksysguardsystemstats
%name library

%prep
%setup -n %rname-%version
#%patch -p2

%build
%K5build \
    -DKDE_INSTALL_INCLUDEDIR=%_K5inc \
    #

%install
%K5install
%K5install_move data ksysguard knsrcfiles
%find_lang %name --all-name

%post
/sbin/setcap CAP_NET_RAW=+ep %_K5libexecdir/ksysguard/ksgrd_network_helper ||:

%files common -f %name.lang
%doc LICENSES/*
%dir %_K5data/ksysguard/
%_datadir/qlogging-categories5/*.*categories

%files
%dir %_K5plug/ksysguard/
%dir %_K5plug/ksysguard/process/
%_K5libexecdir/kauth/*ksysguard*
%_K5libexecdir/ksysguard/ksgrd_network_helper
%_K5dbus/system.d/org.kde.ksysguard.processlisthelper.conf
%_K5dbus_sys_srv/org.kde.ksysguard.processlisthelper.service
%_K5plug/kpackage/packagestructure/sensor*.so
%_K5plug/ksysguard/process/ksysguard_*.so
%_K5qml/org/kde/ksysguard/
%_K5data/ksysguard/
%_K5data/knsrcfiles/*

%files devel
%_K5plug/designer/*.so
#%_K5inc/libksysguard_version.h
%_K5inc/ksysguard/
%_K5link/lib*.so
%_K5lib/cmake/K*SysGuard/
#%_K5archdata/mkspecs/modules/qt_libKSysGuard.pri
%_K5dbus_iface/*.xml

%files -n polkit-kde-ksysguard
%_datadir/polkit-1/actions/org.kde.ksysguard.processlisthelper.policy

%files -n %libprocesscore
%_K5lib/libprocesscore.so.%sover
%_K5lib/libprocesscore.so.*
%files -n %libprocessui
%_K5lib/libprocessui.so.%sover
%_K5lib/libprocessui.so.*
%files -n %libksgrd
%_K5lib/libksgrd.so.%sover
%_K5lib/libksgrd.so.*
%files -n %libksignalplotter
%_K5lib/libksignalplotter.so.%sover
%_K5lib/libksignalplotter.so.*
%files -n %liblsofui
%_K5lib/liblsofui.so.%sover
%_K5lib/liblsofui.so.*
%files -n %libksysguardformatter
%_K5lib/libKSysGuardFormatter.so.%sover2
%_K5lib/libKSysGuardFormatter.so.*
%files -n %libksysguardfaces
%_K5lib/libKSysGuardSensorFaces.so.%sover2
%_K5lib/libKSysGuardSensorFaces.so.*
%files -n %libksysguardsensors
%_K5lib/libKSysGuardSensors.so.%sover2
%_K5lib/libKSysGuardSensors.so.*
%files -n %libksysguardsystemstats
%_K5lib/libKSysGuardSystemStats.so.%sover2
%_K5lib/libKSysGuardSystemStats.so.*

%changelog
* Tue Nov 29 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.26.4-alt1
- new version

* Tue Nov 08 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.26.3-alt1
- new version

* Thu Oct 27 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.26.2-alt1
- new version

* Wed Sep 07 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.25.5-alt1
- new version

* Wed Aug 17 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.25.4-alt1
- new version

* Mon Jul 11 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.24.6-alt1
- new version

* Wed May 04 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.24.5-alt1
- new version

* Wed Mar 30 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.24.4-alt1
- new version

* Mon Jan 31 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.23.5-alt3
- build without qtwebengine on e2k

* Wed Jan 26 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.23.5-alt2
- build without qtwebengine on ppc64le

* Mon Jan 10 2022 Sergey V Turchin <zerg@altlinux.org> 1:5.23.5-alt1
- new version

* Wed Dec 01 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.23.4-alt1
- new version

* Wed Nov 10 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.23.3-alt1
- new version

* Mon Nov 01 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.23.2-alt1
- new version

* Wed Sep 01 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.22.5-alt1
- new version

* Tue Jul 27 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.22.4-alt1
- new version

* Wed Jul 07 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.22.3-alt1
- new version

* Thu Jul 01 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.22.2-alt1
- new version

* Thu May 13 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.21.5-alt1
- new version

* Tue Apr 06 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.21.4-alt1
- new version

* Fri Mar 19 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.21.3-alt1
- new version

* Mon Jan 11 2021 Sergey V Turchin <zerg@altlinux.org> 1:5.20.5-alt1
- new version

* Wed Dec 02 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.20.4-alt1
- new version

* Wed Oct 28 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.20.2-alt1
- new version

* Thu Sep 17 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.19.5-alt1
- new version

* Tue Jul 28 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.19.4-alt1
- new version

* Tue Jul 07 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.19.3-alt1
- new version

* Tue Jul 07 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.19.2-alt1
- new version

* Thu May 07 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.18.5-alt1
- new version

* Thu Apr 02 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.18.4-alt1
- new version

* Wed Mar 11 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.18.3-alt1
- new version

* Tue Feb 25 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.18.1-alt2
- fix requires

* Wed Feb 19 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.18.1-alt1
- new version

* Wed Feb 12 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.17.5-alt2
- update requires

* Thu Jan 09 2020 Sergey V Turchin <zerg@altlinux.org> 1:5.17.5-alt1
- new version

* Thu Dec 05 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.17.4-alt1
- new version

* Wed Nov 13 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.17.3-alt1
- new version

* Fri Nov 01 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.17.2-alt1
- new version

* Mon Oct 28 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.17.1-alt1
- new version

* Thu Oct 17 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.17.0-alt1
- new version

* Mon Sep 09 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.16.5-alt1
- new version

* Thu Aug 01 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.16.4-alt1
- new version

* Thu Jul 11 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.16.3-alt1
- new version

* Wed Jun 26 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.16.2-alt1
- new version

* Tue Jun 18 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.16.1-alt1
- new version

* Thu Jun 06 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.15.5-alt2
- new version

* Tue Jun 04 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.15.5-alt1
- new version

* Wed Apr 24 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.15.4-alt1
- new version

* Tue Mar 05 2019 Sergey V Turchin <zerg@altlinux.org> 1:5.12.8-alt1
- new version

* Wed Nov 28 2018 Oleg Solovyov <mcpain@altlinux.org> 1:5.12.7-alt2
- added killBtn column

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1:5.12.7-alt1.qa1
- NMU: applied repocop patch

* Thu Sep 27 2018 Sergey V Turchin <zerg@altlinux.org> 1:5.12.7-alt1
- new version

* Wed Jul 04 2018 Sergey V Turchin <zerg@altlinux.org> 1:5.12.6-alt2
- fix version

* Tue Jul 03 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt2
- update russian translation

* Wed Jun 27 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.6-alt1
- new version

* Thu May 03 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.5-alt1
- new version

* Wed Mar 28 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.4-alt1
- new version

* Tue Mar 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.3-alt1
- new version

* Thu Mar 01 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.2-alt1
- new version

* Wed Feb 14 2018 Maxim Voronov <mvoronov@altlinux.org> 5.12.0-alt2
- renamed kf5-libksysguard -> plasma5-libksysguard

* Wed Feb 07 2018 Sergey V Turchin <zerg@altlinux.org> 5.12.0-alt1
- new version

* Wed Jan 10 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.5-alt1
- new version

* Mon Dec 11 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.4-alt1
- new version

* Thu Nov 09 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.3-alt1
- new version

* Tue Nov 07 2017 Sergey V Turchin <zerg@altlinux.org> 5.11.2-alt1
- new version

* Fri Sep 29 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.5-alt2
- build without qtwebkit

* Mon Sep 25 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.5-alt1
- new version

* Wed Jul 19 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.4-alt1
- new version

* Fri Jul 14 2017 Sergey V Turchin <zerg@altlinux.org> 5.10.3-alt1
- new version

* Wed Apr 26 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.5-alt1
- new version

* Mon Apr 10 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt1
- new version

* Thu Mar 09 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.3-alt1
- new version

* Mon Feb 20 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.2-alt1
- new version

* Mon Feb 20 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.1-alt1
- new version

* Fri Dec 09 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.4-alt1
- new version

* Wed Nov 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.3-alt0.M80P.1
- build for M80P

* Tue Nov 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.3-alt1
- new version

* Tue Oct 25 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt1
- new version

* Tue Oct 18 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.1-alt0.M80P.1
- build for M80P

* Fri Oct 14 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.1-alt1
- new version

* Tue Oct 04 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt1
- new version

* Tue Aug 30 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.4-alt1
- new version

* Mon Aug 08 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.3-alt1
- new version

* Tue Jul 26 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.2-alt1
- new version

* Wed Jul 13 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt1
- new version

* Wed Jul 06 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.0-alt1
- new version

* Wed Jun 29 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.5-alt1
- new version

* Wed May 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.4-alt1
- new version

* Thu Apr 21 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.3-alt1
- new version

* Wed Mar 30 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.1-alt1
- new version

* Mon Mar 21 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt1
- new version

* Wed Mar 09 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.5-alt1
- new version

* Mon Feb 29 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.4-alt2
- fix to compile with new gcc

* Thu Jan 28 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.4-alt1
- new version

* Thu Jan 14 2016 Sergey V Turchin <zerg@altlinux.org> 5.5.3-alt1
- new version

* Tue Dec 29 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.2-alt1
- new version

* Thu Dec 17 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt1
- new version

* Wed Dec 09 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- new version

* Thu Nov 19 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.3-alt3
- rebuild

* Wed Nov 11 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.3-alt1
- new version

* Wed Oct 07 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt1
- new version

* Thu Sep 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt1
- new version

* Wed Aug 26 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- new version

* Sat Aug 22 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.95-alt1
- new version

* Wed Jul 01 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt1
- new version

* Fri May 29 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- new version

* Thu Apr 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- new version

* Tue Apr 28 2015 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt0.1
- test

* Thu Apr 16 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.2-alt1
- new version

* Mon Mar 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.2-alt0.1
- test

* Wed Feb 25 2015 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt0.1
- initial build
