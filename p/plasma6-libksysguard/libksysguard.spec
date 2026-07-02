
%define rname libksysguard

%ifarch %not_qt6_qtwebengine_arches
%def_disable qtwebengine
%else
%def_enable qtwebengine
%endif

%define sover 11
%define libksgrd libksgrd%sover
%define libksignalplotter libksignalplotter%sover
%define liblsofui liblsofui%sover
%define libprocesscore libprocesscore%sover
%define libprocessui libprocessui%sover
%define sover2 2
%define libksysguardformatter libksysguardformatter%sover2
%define libksysguardfaces libksysguardfaces%sover2
%define libksysguardsensors libksysguardsensors%sover2
%define libksysguardsystemstats libksysguardsystemstats%sover2

Name: plasma6-%rname
Version: 6.7.2
Release: alt1
#Epoch: 1
%K6init

Group: System/Libraries
Summary: KDE Frameworks 6 performance monitor library
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires(post): /sbin/setcap
Provides: plasma5-libksysguard = 1:%version-%release
Obsoletes: plasma5-libksysguard < 1:%version-%release

Source: %rname-%version.tar
Patch: alt-killbtn.patch

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6-webengine
BuildRequires: libvulkan-devel
BuildRequires: extra-cmake-modules
BuildRequires: libsensors3-devel libdrm-devel
BuildRequires: zlib-devel libnl-devel libcap-devel libpcap-devel
BuildRequires: qt6-declarative-devel  qt6-tools-devel
%if_enabled qtwebengine
BuildRequires: qt6-webengine-devel qt6-webchannel-devel
%endif
BuildRequires: kf6-kauth-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kdbusaddons-devel kf6-kguiaddons-devel
BuildRequires: kf6-ki18n-devel kf6-kiconthemes-devel kf6-kitemviews-devel kf6-kpackage-devel kf6-kservice-devel
BuildRequires: kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel 
BuildRequires: kf6-kglobalaccel-devel kf6-kio-devel kf6-kdeclarative-devel kf6-knewstuff-devel

%description
Performance monitor library

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Provides: plasma5-libksysguard-common = 1:%version-%release
Obsoletes: plasma5-libksysguard-common < 1:%version-%release
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

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
Requires: polkit-kde-ksysguard >= %EVR
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

%package -n polkit-kde-ksysguard
Summary: %name common package
Group: System/Configuration/Other
Epoch: 1
BuildArch: noarch
Requires: kde-common
Provides: %name-polkit = %EVR
Obsoletes: %name-polkit < %EVR
%description -n polkit-kde-ksysguard
Common polkit files for %name

%prep
%setup -n %rname-%version
#%patch -p2

%build
%K6build \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    #

%install
%K6install
%K6install_move data ksysguard knsrcfiles
%find_lang %name --all-name

%post
/sbin/setcap CAP_NET_RAW=+ep %_K6libexecdir/ksysguard/ksgrd_network_helper ||:

%files common -f %name.lang
%doc LICENSES/*
%dir %_K6data/ksysguard/
%_datadir/qlogging-categories6/*.*categories

%files
%dir %_K6plug/ksysguard/
%dir %_K6plug/ksysguard/process/
%_K6bin/ksysguard-*
%_K6exec/kauth/*ksysguard*
%_K6libexecdir/ksysguard/ksgrd_network_helper
%_K6dbus/system.d/org.kde.ksysguard.processlisthelper.conf
%_K6dbus_sys_srv/org.kde.ksysguard.processlisthelper.service
%_K6plug/ksysguard/process/*ksysguard*.so
%_K6plug/kf6/packagestructure/*ksysguard*.so
%_K6qml/org/kde/ksysguard/
%_K6data/ksysguard/
%_K6data/knsrcfiles/*

%files devel
#%_K6plug/designer/*.so
%_K6inc/ksysguard/
%_K6link/lib*.so
%_K6lib/cmake/K*SysGuard/
%_K6dbus_iface/*.xml

%files -n polkit-kde-ksysguard
%_datadir/polkit-1/actions/org.kde.ksysguard.processlisthelper.policy

%files -n %libprocesscore
%_K6lib/libprocesscore.so.%sover
%_K6lib/libprocesscore.so.*
%if 0
%files -n %libprocessui
%_K6lib/libprocessui.so.%sover
%_K6lib/libprocessui.so.*
%files -n %libksgrd
%_K6lib/libksgrd.so.%sover
%_K6lib/libksgrd.so.*
%files -n %libksignalplotter
%_K6lib/libksignalplotter.so.%sover
%_K6lib/libksignalplotter.so.*
%files -n %liblsofui
%_K6lib/liblsofui.so.%sover
%_K6lib/liblsofui.so.*
%endif
%files -n %libksysguardformatter
%_K6lib/libKSysGuardFormatter.so.%sover2
%_K6lib/libKSysGuardFormatter.so.*
%files -n %libksysguardfaces
%_K6lib/libKSysGuardSensorFaces.so.%sover2
%_K6lib/libKSysGuardSensorFaces.so.*
%files -n %libksysguardsensors
%_K6lib/libKSysGuardSensors.so.%sover2
%_K6lib/libKSysGuardSensors.so.*
%files -n %libksysguardsystemstats
%_K6lib/libKSysGuardSystemStats.so.%sover2
%_K6lib/libKSysGuardSystemStats.so.*



%changelog
* Wed Jul 01 2026 Sergey V Turchin <zerg@altlinux.org> 6.7.2-alt1
- new version

* Mon Jun 29 2026 Sergey V Turchin <zerg@altlinux.org> 6.7.1-alt1
- new version

* Tue May 12 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.5-alt1
- new version

* Thu Apr 09 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.4-alt1
- new version

* Mon Mar 30 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.3-alt1
- new version

* Wed Mar 11 2026 Sergey V Turchin <zerg@altlinux.org> 6.5.6-alt1
- new version

* Thu Jan 15 2026 Sergey V Turchin <zerg@altlinux.org> 6.5.5-alt1
- new version

* Wed Dec 10 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.4-alt1
- new version

* Tue Nov 18 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.3-alt1
- new version

* Thu Nov 13 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.2-alt1
- new version

* Wed Nov 12 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.6-alt1
- new version

* Tue Sep 16 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.5-alt1
- new version

* Fri Aug 22 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.4-alt1
- new version

* Tue Jul 15 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.3-alt1
- new version

* Tue Jul 08 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt1
- new version

* Wed May 07 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.5-alt1
- new version

* Wed Apr 02 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.4-alt1
- new version

* Wed Mar 12 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.3-alt1
- new version

* Wed Feb 26 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.2-alt1
- new version

* Wed Feb 19 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.1-alt1
- new version

* Fri Feb 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Thu Jan 09 2025 Sergey V Turchin <zerg@altlinux.org> 6.2.5-alt1
- new version

* Tue Nov 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt1
- new version

* Wed Nov 06 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.3-alt1
- new version

* Mon Oct 28 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.2-alt1
- new version

* Tue Sep 10 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.5-alt1
- new version

* Thu Aug 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.4-alt1
- new version

* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build

