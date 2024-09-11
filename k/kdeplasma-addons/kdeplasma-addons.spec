%define rname kdeplasma-addons

%ifarch %not_qt6_qtwebengine_arches
%def_disable qtwebengine
%else
%def_enable qtwebengine
%endif

%define plasmacomicprovidercore_sover 6
%define libplasmacomicprovidercore libplasmacomicprovidercore%plasmacomicprovidercore_sover
%define plasmaweatherprivate_sover 6
%define libplasmaweatherprivate libplasmaweatherprivate%plasmaweatherprivate_sover
%define plasmapotdprovidercore_sover 6
%define libplasmapotdprovidercore libplasmapotdprovidercore%plasmapotdprovidercore_sover

Name: %rname
Version: 6.1.5
Release: alt1
#Epoch: 1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Frameworks 6 Plasma addons
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: %name-common = %version-%release
# desktop cube
Requires: qt6-quick3d
# plasma.quickshare
Requires: kf6-purpose
# plasma.diskquota
Requires: quota
#
Requires: libkf6itemmodels kf6-purpose kf6-kirigami-addons 
#
Provides: plasma5-addons = 1:%version-%release
Obsoletes: plasma5-addons < 1:%version-%release

Source: %rname-%version.tar
Patch1: alt-sover.patch
Patch2: alt-def-dict.patch

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6-webengine
BuildRequires: extra-cmake-modules gcc-c++ qt6-declarative-devel  qt6-declarative-devel qt6-5compat-devel
%if_enabled qtwebengine
BuildRequires: qt6-webengine-devel
%endif
BuildRequires: libxcbutil-image-devel libxcb-devel
BuildRequires: libvulkan-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcmutils-devel kf6-kcodecs-devel kf6-kcompletion-devel
BuildRequires: kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdbusaddons-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel
BuildRequires: kf6-kglobalaccel-devel kf6-kguiaddons-devel kf6-ki18n-devel
BuildRequires: kf6-kiconthemes-devel  kf6-kio-devel kf6-kitemmodels-devel kf6-kitemviews-devel kf6-kjobwidgets-devel
BuildRequires: kf6-knotifications-devel kf6-kpackage-devel kf6-kparts-devel kf6-krunner-devel kf6-kservice-devel kf6-ktextwidgets-devel
BuildRequires: kf6-kunitconversion-devel kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel 
BuildRequires: kf6-solid-devel kf6-sonnet-devel kf6-knewstuff-devel
BuildRequires: kf6-kdeclarative-devel kf6-kholidays-devel kf6-networkmanager-qt-devel
BuildRequires: plasma6-lib-devel plasma6-activities-devel plasma6-plasma5support-devel
BuildRequires: plasma-workspace-devel plasma6-libksysguard-devel

%description
Plasma addons.

%package common
Summary: %name common package
Group: System/Configuration/Other
Requires: kde-common
Provides: plasma5-addons-common = 1:%version-%release
Obsoletes: plasma5-addons-common < 1:%version-%release
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %EVR
Conflicts: plasma5-addons-devel < 1:%version-%release
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libplasmacomicprovidercore
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %EVR
%description -n %libplasmacomicprovidercore
KF6 library

%package -n %libplasmaweatherprivate
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %EVR
%description -n %libplasmaweatherprivate
KF6 library

%package -n %libplasmapotdprovidercore
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %EVR
%description -n %libplasmapotdprovidercore
KF6 library

%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1

# exclude applet
sed -i '/^add_subdirectory(comic)/d' applets/CMakeLists.txt

# disable krunners by default
for d in runners/*/*.json ; do
    sed -i '/EnabledByDefault/s|true|false|' $d
done

%build
%K6build \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    #

%install
%K6install
%K6install_move data kwin kdevappwizard kdevfiletemplates locale knsrcfiles
%K6install_move icon all
%find_lang %name --all-name
# ensure arch-dependence
touch touch-%_arch

%files common -f %name.lang
%doc touch-%_arch LICENSES/*
%_K6icon/*/*/*/*.*
%_datadir/qlogging-categories6/*.*categories

%files
%_K6exec/kauth/*
%_K6plug/kf6/krunner/kcms/*.so
%_K6plug/plasma/applets/*.so
%_K6plug/plasmacalendarplugins/*
%_K6plug/potd/
%_K6plug/kf6/krunner/*.so
%_K6plug/kf6/kded/*.so
%_K6plug/kwin/effects/configs/*.so
%_K6qml/org/kde/plasma/private/*/
%_K6qml/org/kde/plasmacalendar/*/
%_K6qml/org/kde/plasma/wallpapers/potd/
%_K6data/plasma/*
%_K6data/kwin/*
%_K6notif/*
%_datadir/metainfo/*.xml
%_K6dbus_sys_srv/*.service
%_K6dbus/system.d/*.conf
%_datadir/polkit-1/actions/*.policy

# comic
#%_K6data/knsrcfiles/*.knsrc
#%_K6plug/kpackage/packagestructure/*.so
#%_K6srvtyp/*

%files devel
%_K6inc/plasma/potdprovider/
%_K6link/lib*.so
%_libdir/cmake/PlasmaPotdProvider/
%_K6data/kdev*/templates/*.tar.*

#%files -n %libplasmacomicprovidercore
#%_K6lib/libplasmacomicprovidercore.so.*
#%_K6lib/libplasmacomicprovidercore.so.%plasmacomicprovidercore_sover
%files -n %libplasmapotdprovidercore
%_K6lib/libplasmapotdprovidercore.so.*
%_K6lib/libplasmapotdprovidercore.so.%plasmapotdprovidercore_sover



%changelog
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

