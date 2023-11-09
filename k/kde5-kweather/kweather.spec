%define rname kweather

Name: kde5-%rname
Version: 23.08.2
Release: alt2
%K5init

Group: Graphical desktop/KDE
Summary: Weather application
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: kf5-kirigami-addons

Source: %rname-%version.tar
Patch1: alt-clear-country-names.patch

# Automatically added by buildreq on Tue Apr 25 2023 (-bi)
# optimized out: cmake cmake-modules debugedit elfutils fontconfig-devel gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 kf5-kconfig-devel kf5-kcoreaddons-common kf5-kcoreaddons-devel kf5-kwindowsystem-devel libICE-devel libSM-devel libX11-devel libXau-devel libXext-devel libXfixes-devel libXi-devel libXmu-devel libXrender-devel libXt-devel libctf-nobfd0 libdbusmenu-qt52 libfreetype-devel libglvnd-devel libgpg-error libp11-kit libqt5-charts libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-positioning libqt5-printsupport libqt5-qml libqt5-qmlmodels libqt5-quick libqt5-quickcontrols2 libqt5-quicktemplates2 libqt5-sql libqt5-svg libqt5-test libqt5-texttospeech libqt5-waylandclient libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libssl-devel libstdc++-devel libwayland-client libwayland-cursor libxcb-devel libxcbutil-keysyms libxkbcommon-devel pkg-config python-modules python2-base python3 python3-base python3-dev python3-module-paste python3-module-pkg_resources qt5-base-common qt5-base-devel qt5-declarative-devel rpm-build-file rpm-build-python3 rpm-build-qml rpm-macros-python sh4 tzdata xorg-proto-devel xorg-xf86miscproto-devel
#BuildRequires: appstream clang-tools extra-cmake-modules kde5-kweathercore-devel kf5-ki18n-devel kf5-kirigami-addons-devel kf5-kirigami-devel kf5-knotifications-devel kf5-kpackage-devel kf5-kservice-devel kf5-plasma-framework-devel libXScrnSaver-devel libXaw-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXft-devel libXinerama-devel libXpm-devel libXrandr-devel libXres-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libxcbutil-devel libxcbutil-icccm-devel libxkbcommon-x11-devel libxkbfile-devel python-modules-compiler python3-module-mpl_toolkits python3-module-setuptools python3-module-zope qt5-charts-devel qt5-imageformats qt5-quickcontrols2-devel qt5-svg-devel qt5-translations qt5-wayland-devel qt5-webengine-devel rpm-build-qml6 tbb-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-charts-devel qt5-svg-devel qt5-quickcontrols2-devel
BuildRequires: kde5-kweathercore-devel
BuildRequires: kf5-ki18n-devel kf5-kirigami-devel kf5-kirigami-addons-devel kf5-plasma-framework-devel
BuildRequires: kf5-knotifications-devel kf5-kpackage-devel kf5-kservice-devel

%description
A convergent weather application for Plasma.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf5weather
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n libkf5weather
%name library


%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K5build

%install
%K5install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K5bin/kweather
%_K5plug/plasma/applets/*kweather*.so
%_K5xdgapp/*kweather*.desktop
%_K5dbus_srv/*kweather*.service
%_K5icon/hicolor/*/apps/*kweather*
%_kf5_data/plasma/plasmoids/*kweather*/
%_datadir/metainfo/*.xml

%changelog
* Thu Nov 09 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.2-alt2
- package metainfo

* Mon Oct 16 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.2-alt1
- new version

* Mon Jul 17 2023 Sergey V Turchin <zerg@altlinux.org> 23.04.3-alt2
- when search show subdivision if possible (closes: 46940)

* Fri Jul 14 2023 Sergey V Turchin <zerg@altlinux.org> 23.04.3-alt1
- new version

* Wed Jun 14 2023 Sergey V Turchin <zerg@altlinux.org> 23.04.2-alt1
- new version

* Thu May 11 2023 Sergey V Turchin <zerg@altlinux.org> 23.04.0-alt2
- clear country names

* Tue Apr 25 2023 Sergey V Turchin <zerg@altlinux.org> 23.04.0-alt1
- new version

* Wed Aug 18 2021 Sergey V Turchin <zerg@altlinux.org> 21.07-alt1
- initial build
