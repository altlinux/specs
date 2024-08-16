%ifndef _userunitdir
%define _userunitdir %prefix/lib/systemd/user
%endif

%define rname powerdevil

%define powerdevilconfigcommonprivate_sover 6
%define libpowerdevilconfigcommonprivate libpowerdevilconfigcommonprivate%powerdevilconfigcommonprivate_sover
%define powerdevilui_sover 6
%define libpowerdevilui libpowerdevilui%powerdevilui_sover
%define powerdevilcore_sover 2
%define libpowerdevilcore libpowerdevilcore%powerdevilcore_sover

Name: %rname
Version: 6.1.4
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
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: libudev-devel libddcutil-devel
BuildRequires: libvulkan-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel
BuildRequires: kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel
BuildRequires: kf6-kdbusaddons-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel kf6-kglobalaccel-devel
BuildRequires: kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel kf6-kidletime-devel 
BuildRequires: kf6-kio-devel kf6-kitemmodels-devel kf6-kitemviews-devel kf6-kjobwidgets-devel
BuildRequires: kf6-knotifications-devel kf6-knotifyconfig-devel kf6-kparts-devel kf6-kservice-devel
BuildRequires: kf6-ktextwidgets-devel kf6-kunitconversion-devel kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel
BuildRequires: kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel
BuildRequires: kf6-kirigami-devel
BuildRequires: kf6-networkmanager-qt-devel kf6-bluez-qt-devel kf6-kcmutils-devel
BuildRequires: plasma6-libkscreen-devel plasma-workspace-devel plasma6-kwayland-devel plasma6-activities-devel
BuildRequires: plasma6-layer-shell-qt-devel
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

%package -n %libpowerdevilconfigcommonprivate
Group: System/Libraries
Summary: KF6 library
Requires: %name-common >= %EVR
%description -n %libpowerdevilconfigcommonprivate
KF6 library

%package -n %libpowerdevilui
Group: System/Libraries
Summary: KF6 library
Requires: %name-common >= %EVR
%description -n %libpowerdevilui
KF6 library

%package -n %libpowerdevilcore
Group: System/Libraries
Summary: KF6 library
Requires: %name-common >= %EVR
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
/sbin/setcap CAP_WAKE_ALARM=+ep %_K6libexecdir/org_kde_powerdevil ||:


%files common -f %name.lang
%doc COPYING*
%_datadir/qlogging-categories6/*.*categories

%files
%_K6dbus/system.d/*.conf
%_K6exec/kauth/*helper*
%_K6libexecdir/*power*
%_K6plug/powerdevil/
%_K6plug/plasma/kcms/systemsettings/*powerdevil*.so
%_K6start/powerdevil.desktop
%_K6xdgapp/*powerdevil*.desktop
%_K6notif/*.notifyrc
%_K6dbus_srv/*.service
%_K6dbus_sys_srv/*.service
%_datadir/polkit-1/actions/*.policy
%_userunitdir/*.service

#%files devel
#%_K6link/lib*.so
#%_K6dbus_iface/*powerdevil*

%files -n %libpowerdevilconfigcommonprivate
%_K6lib/libpowerdevilconfigcommonprivate.so.*
%_K6lib/libpowerdevilconfigcommonprivate.so.%powerdevilconfigcommonprivate_sover
%files -n %libpowerdevilcore
%_K6lib/libpowerdevilcore.so.*
%_K6lib/libpowerdevilcore.so.%powerdevilcore_sover
#%files -n %libpowerdevilui
#%_K6lib/libpowerdevilui.so.*
#%_K6lib/libpowerdevilui.so.%powerdevilui_sover


%changelog
* Thu Aug 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.4-alt1
- new version

* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build

