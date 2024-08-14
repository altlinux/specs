
%define sover 6
%define libplasma libplasma%sover
%define libplasmaquick libplasmaquick%sover

%define rname libplasma
Name: plasma6-lib
Version: 6.1.2
Release: alt1
%K6init

Group: System/Libraries
Summary: Plasma foundational libraries
Url: http://www.kde.org
License: LGPL-2.0-or-later

Provides: %libplasma-devel = %version-%release

Source: %rname-%version.tar

# Automatically added by buildreq on Wed Jun 26 2024 (-bi)
# optimized out: cmake cmake-modules debugedit elfutils fontconfig-devel gcc-c++ git-core glibc-kernheaders-generic glibc-kernheaders-x86 kf6-karchive-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcolorscheme-devel kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kglobalaccel-devel kf6-kguiaddons-devel kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-kservice-devel kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-solid-devel libICE-devel libSM-devel libX11-devel libXau-devel libXext-devel libXfixes-devel libXi-devel libXmu-devel libXrender-devel libXt-devel libctf-nobfd0 libdouble-conversion3 libfreetype-devel libglvnd-devel libgpg-error libp11-kit libqt6-core libqt6-dbus libqt6-gui libqt6-network libqt6-opengl libqt6-qml libqt6-qmlcompiler libqt6-qmlmodels libqt6-quick libqt6-quickcontrols2 libqt6-quicktemplates2 libqt6-svg libqt6-waylandclient libqt6-widgets libqt6-xml libsasl2-3 libssl-devel libstdc++-devel libvulkan-devel libwayland-client libwayland-client-devel libwayland-cursor libwayland-cursor-devel libwayland-server-devel libxcb-devel libxcbutil-keysyms libxkbcommon-devel perl pkg-config python-modules python2-base python3 python3-base python3-dev python3-module-setuptools qt6-base-common qt6-base-devel qt6-declarative-devel qt6-svg-devel rpm-build-file rpm-build-python3 rpm-build-qml rpm-build-qml6 rpm-macros-python sh5 tzdata vulkan-headers wayland-devel xorg-proto-devel xorg-xf86miscproto-devel
#BuildRequires: appstream clang-tools extra-cmake-modules glslang kde5-plasma-wayland-protocols kf6-kcmutils-devel kf6-ki18n-devel kf6-kiconthemes-devel kf6-kio-devel kf6-kirigami-devel kf6-knotifications-devel kf6-kpackage-devel kf6-ksvg-devel libGLU-devel libXScrnSaver-devel libXaw-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXft-devel libXinerama-devel libXpm-devel libXrandr-devel libXres-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libwayland-egl-devel libxcb-render-util-devel libxcbutil-cursor-devel libxcbutil-devel libxcbutil-icccm-devel libxcbutil-image-devel libxcbutil-keysyms-devel libxkbcommon-x11-devel libxkbfile-devel plasma6-activities-devel python-modules-compiler qt6-wayland-devel rpm-build-kf6 tbb-devel
BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules
BuildRequires: qt6-base-devel qt6-declarative-devel
BuildRequires: qt6-wayland-devel libwayland-egl-devel plasma-wayland-protocols
BuildRequires: kf6-kcmutils-devel kf6-ki18n-devel kf6-kiconthemes-devel kf6-kio-devel kf6-kirigami-devel
BuildRequires: kf6-knotifications-devel kf6-kpackage-devel kf6-ksvg-devel
BuildRequires: plasma6-activities-devel

%description
Foundational libraries, components, and tools of the Plasma workspaces.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libplasma
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libplasma
%name library

%package -n %libplasmaquick
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libplasmaquick
%name library

%prep
%setup -n %rname-%version

%build
%K6build \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    #

%install
%K6install
%K6install_move data locale
%find_lang %name --all-name
%K6find_qtlang %name --append --all-name

%files common -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories
%_K6data/plasma/desktoptheme/*

%files devel
%_K6data/kdevappwizard/templates/*.tar.bz2
%_K6inc/Plasma/
%_K6inc/PlasmaQuick/
%_K6link/lib*.so
%_K6lib/cmake/Plasma/
%_K6lib/cmake/PlasmaQuick/
#%_pkgconfigdir/Plasma.pc

%files -n %libplasma
%_K6lib/libPlasma.so.%sover
%_K6lib/libPlasma.so.*
%_K6plug/kf6/kirigami/platform/KirigamiPlasmaStyle.so
%_K6plug/kf6/packagestructure/plasma_*.so

%files -n %libplasmaquick
%_K6lib/libPlasmaQuick.so.%sover
%_K6lib/libPlasmaQuick.so.*
%_K6qml/org/kde/kirigami/*/
%_K6qml/org/kde/plasma/*/


%changelog
* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- initial build
