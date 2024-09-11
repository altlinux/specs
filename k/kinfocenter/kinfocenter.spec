%define rname kinfocenter

%define kinfocenterinternal_sover 6
%define libkinfocenterinternal libkinfocenterinternal%kinfocenterinternal_sover

Name: %rname
Version: 6.1.5
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Plasma Info Center
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides:  plasma5-kinfocenter = %EVR
Obsoletes: plasma5-kinfocenter < %EVR
Requires: kf6-kirigami
Requires: systemsettings
# USB
Requires: usbids

Source: %rname-%version.tar
Source10: ansi2html.sh
Source20: add-ru.po
Patch2: alt-mark-usb-drives.patch
Patch3: alt-no-aha-tool.patch
Patch4: alt-use-pretty-name.patch
Patch5: alt-symlink.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-base-devel qt6-declarative-devel
BuildRequires: libpci-devel libraw1394-devel libusb-devel
BuildRequires: libGLU-devel libXScrnSaver-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXft-devel
BuildRequires: libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel
BuildRequires: libxkbfile-devel
BuildRequires: libvulkan-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcmutils-devel kf6-kcodecs-devel kf6-kcompletion-devel
BuildRequires: kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdbusaddons-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel
BuildRequires: kf6-kglobalaccel-devel kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel
BuildRequires: kf6-kio-devel kf6-kitemmodels-devel kf6-kitemviews-devel kf6-kjobwidgets-devel
BuildRequires: kf6-knotifications-devel kf6-kparts-devel kf6-kservice-devel kf6-ktextwidgets-devel kf6-kunitconversion-devel
BuildRequires: kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel
BuildRequires: kf6-kdeclarative-devel kf6-kpackage-devel
BuildRequires: plasma6-kwayland-devel
BuildRequires: systemsettings

%description
KDE Info Center.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Provides: plasma5-kinfocenter-common = %EVR
Obsoletes: plasma5-kinfocenter-common < %EVR
%description common
%name common package

%package maxi
Summary: %name maximum package
Group: System/Configuration/Packaging
Provides:  plasma5-kinfocenter-maxi = %EVR
Obsoletes: plasma5-kinfocenter-maxi < %EVR
Requires: %name
# Window Manager
Requires: /usr/share/qt6/bin/qdbus
# OpenCL
Requires: /usr/bin/clinfo
# OpenGL (EGL)
Requires: /usr/bin/eglinfo
# OpenGL (GLX)
Requires: /usr/bin/glxinfo
# X-Server
Requires: /usr/bin/xdpyinfo
# Wayland
Requires: /usr/bin/wayland-info
# PCI
Requires: /usr/bin/lspci
# CPU
Requires: /usr/bin/lscpu
# Vulkan
Requires: /usr/bin/vulkaninfo
# Firmware Security
#Requires: /usr/bin/fwupdmgr
# About
Requires: /usr/sbin/dmidecode
# Network
Requires: /usr/bin/ip
# Audio
Requires: /usr/bin/pactl
%description maxi
%name maximum package.

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Conflicts: plasma5-kinfocenter-devel < %EVR
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkinfocenterinternal
Group: System/Libraries
Summary: KF6 library
Requires: %name-common >= %EVR
%description -n %libkinfocenterinternal
KF6 library


%prep
%setup -n %rname-%version
#%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

grep -e 'add_library.*KInfoCenterInternal' src/CMakeLists.txt \
 && echo 'set_target_properties(KInfoCenterInternal PROPERTIES VERSION ${PROJECT_VERSION} SOVERSION 6)' >>src/CMakeLists.txt \
 ||:

for p in po/ru/*.po ; do
    mv ${p}{,.old}
    msgcat --use-first %SOURCE20 ${p}.old > ${p}
    rm -f ${p}.old
done


%build
%K6build

%install
%K6install
%K6install_move data desktop-directories kcmusb kcmview1394 kpackage kinfocenter
%K6install_move menu all
install -Dm 0755 %SOURCE10 %buildroot/%_K6bin/kinfocenter-ansi2html.sh

%find_lang %name --with-kde --all-name

%files common  -f %name.lang
%doc LICENSES/*

%files maxi

%files
%_K6bin/*
%_K6plug/plasma/kcms/*.so
%_K6plug/plasma/kcms/kinfocenter/*.so
%_K6qml/org/kde/kinfocenter/
%_K6xdgapp/*.desktop
%_K6xdgdir/*.directory
%_K6xdgmenu/*.menu
%_K6data/kinfocenter/
# kinfocenter/dmidecode-helper
%_K6exec/kauth/*dmidecode*
%_K6dbus_sys_srv/*dmidecode*
%_datadir/dbus-1/system.d/*dmidecode*
%_datadir/polkit-1/actions/*dmidecode*
%_datadir/metainfo/*.xml

%files -n %libkinfocenterinternal
%_K6lib/libKInfoCenterInternal.so.*
%_K6lib/libKInfoCenterInternal.so.%kinfocenterinternal_sover



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

