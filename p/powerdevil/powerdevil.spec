%ifndef _userunitdir
%define _userunitdir %prefix/lib/systemd/user
%endif

%define rname powerdevil

%define powerdevilcore_sover 2
%define libpowerdevilcore libpowerdevilcore%powerdevilcore_sover

Name: %rname
Version: 6.7.2
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Frameworks 6 advanced power management settings
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: upower
Requires(pre): /sbin/setcap

Provides: plasma5-powerdevil = %EVR
Obsoletes: plasma5-powerdevil < %EVR

Source: %rname-%version.tar

Patch1: alt-kidletime-crash.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-wayland-devel
BuildRequires: qcoro6-devel
BuildRequires: libudev-devel libddcutil-devel
BuildRequires: libvulkan-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel
BuildRequires: kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel
BuildRequires: kf6-kdbusaddons-devel kf6-krunner-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel kf6-kglobalaccel-devel
BuildRequires: kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel kf6-kidletime-devel 
BuildRequires: kf6-kio-devel kf6-kitemmodels-devel kf6-kitemviews-devel kf6-kjobwidgets-devel
BuildRequires: kf6-knotifications-devel kf6-knotifyconfig-devel kf6-kparts-devel kf6-kservice-devel
BuildRequires: kf6-ktextwidgets-devel kf6-kunitconversion-devel kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel
BuildRequires: kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel kf6-kpackage-devel
BuildRequires: kf6-kirigami-devel
BuildRequires: kf6-networkmanager-qt-devel kf6-bluez-qt-devel kf6-kcmutils-devel
BuildRequires: plasma-wayland-protocols
BuildRequires: plasma6-libkscreen-devel plasma-workspace-devel plasma6-kwayland-devel plasma6-activities-devel
BuildRequires: plasma6-layer-shell-qt-devel plasma6-lib-devel
# tmp
BuildRequires: libnm-devel

%description
Advanced power management settings.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Provides: plasma5-powerdevil-common = %EVR
Obsoletes: plasma5-powerdevil-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libpowerdevilcore
Group: System/Libraries
Summary: KF6 library
Requires: %name-common >= %EVR
Obsoletes: libpowerdevilconfigcommonprivate6 < %EVR
%description -n %libpowerdevilcore
KF6 library


%prep
%setup -n %rname-%version
%patch1 -p2

sed -i 's|Libcap|setcap_EXEC_ALREADY_IN_RPM_POST_SCRIPT|' CMakeLists.txt

%build
%K6build \
    -DHAVE_DDCUTIL=ON \
    #

%install
%K6install
%K6install_move exec org_kde_powerdevil
%find_lang %name --with-kde --all-name

%post
/usr/sbin/setcap CAP_WAKE_ALARM=+ep %_K6libexecdir/org_kde_powerdevil ||:

%files common -f %name.lang
%doc COPYING*
%_datadir/qlogging-categories6/*.*categories

%files
%_K6dbus/system.d/*.conf
%_K6exec/kauth/*helper*
%_K6libexecdir/*power*
%_K6plug/powerdevil/
%_K6plug/kf6/krunner/*powerdevil*.so
%_K6plug/plasma/kcms/systemsettings/*power*.so
%_K6plug/plasma/applets/org.kde.plasma.*.so
%_K6qml/org/kde/plasma/private/batterymonitor/
%_K6qml/org/kde/plasma/private/brightnesscontrolplugin/
%_K6start/powerdevil.desktop
%_K6xdgapp/*power*.desktop
%_K6notif/*.notifyrc
%_K6dbus_sys_srv/*.service
%_datadir/polkit-1/actions/*.policy
%_userunitdir/*.service
#%_datadir/metainfo/*.xml

#%files devel
#%_K6link/lib*.so
#%_K6dbus_iface/*powerdevil*

%files -n %libpowerdevilcore
%_K6lib/libpowerdevilcore.so.*
%_K6lib/libpowerdevilcore.so.%powerdevilcore_sover


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

* Mon Feb 24 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.1-alt2
- obsolete libpowerdevilconfigcommonprivate6

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

