%define rname koko
%define sover 0.0.1
%define libkokocommon libkokocommon%sover

Name: kde5-%rname
Version: 23.08.4
Release: alt1
%K5init

Group: Graphical desktop/KDE
Summary: Image Viewer
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: qt5-svg qt5-graphicaleffects kde5-kquickimageeditor

Source: %rname-%version.tar
# https://download.geonames.org/export/dump/admin1CodesASCII.txt
Source101: admin1CodesASCII.txt
# https://download.geonames.org/export/dump/admin2Codes.txt
Source102: admin2Codes.txt
# https://download.geonames.org/export/dump/cities1000.zip
Source103: cities1000.txt

# Automatically added by buildreq on Wed Dec 06 2023 (-bi)
# optimized out: cmake cmake-modules debugedit elfutils fontconfig-devel gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 gtk4-update-icon-cache kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-kguiaddons-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXmu-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libctf-nobfd0 libdbusmenu-qt52 libdouble-conversion3 libfreetype-devel libglvnd-devel libgpg-error libp11-kit libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-positioning libqt5-qml libqt5-qmlmodels libqt5-quick libqt5-quickcontrols2 libqt5-sql libqt5-svg libqt5-test libqt5-texttospeech libqt5-waylandclient libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libssl-devel libstdc++-devel libwayland-client libwayland-cursor libxcb-devel libxcbutil-keysyms libxcbutil-keysyms-devel libxkbcommon-devel libxkbfile-devel perl pkg-config python-modules python2-base python3 python3-base python3-dev python3-module-paste python3-module-setuptools qt5-base-common qt5-base-devel qt5-declarative-devel qt5-location-devel rpm-build-file rpm-build-python3 rpm-build-qml rpm-macros-python sh5 tzdata xorg-proto-devel xorg-xf86miscproto-devel
#BuildRequires: appstream clang-tools extra-cmake-modules kde5-kquickimageeditor-devel kf5-kdeclarative-devel kf5-kfilemetadata-devel kf5-ki18n-devel kf5-kirigami-devel kf5-knotifications-devel kf5-kpackage-devel libXaw-devel libXres-devel libexiv2-devel libnss-myhostname libxcb-render-util-devel libxcbutil-cursor-devel libxcbutil-devel libxcbutil-icccm-devel libxcbutil-image-devel libxkbcommon-x11-devel python-modules-compiler python3-module-zope qt5-graphicaleffects qt5-imageformats qt5-quickcontrols2-devel qt5-svg-devel qt5-wayland-devel qt5-webengine-devel qt5-x11extras-devel tbb-devel zip
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules
BuildRequires: qt5-base-devel qt5-quickcontrols2-devel qt5-location-devel qt5-svg-devel qt5-x11extras-devel
BuildRequires: zip
BuildRequires: kde5-kquickimageeditor-devel kf5-kdeclarative-devel kf5-kfilemetadata-devel kf5-ki18n-devel
BuildRequires: kf5-kirigami-devel kf5-knotifications-devel kf5-kpackage-devel
BuildRequires: libexiv2-devel
BuildRequires: libxcbutil-devel

%description
Koko is an image viewer designed for desktop and touch devices.

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

%package -n %libkokocommon
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libkokocommon
%name library


%prep
%setup -n %rname-%version
install -m 0644 %SOURCE101 src/
install -m 0644 %SOURCE102 src/
install -m 0644 %SOURCE103 ./
zip -0 src/cities1000.zip cities1000.txt
rm -f cities1000.txt

%build
%K5build

%install
%K5install
%K5install_move data koko
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*

%files
%_K5bin/koko
%_K5data/koko/
%_K5qml/org/kde/koko/
%_K5xdgapp/*koko*.desktop
%_K5icon/*/*/apps/*koko*.*
%_K5notif/*koko*.notifyrc
%_datadir/metainfo/*koko*.xml

#%files devel
#%_K5inc/koko_version.h
#%_K5inc/koko/
#%_K5link/lib*.so
#%_K5lib/cmake/koko
#%_K5archdata/mkspecs/modules/qt_koko.pri

%files -n %libkokocommon
%_K5lib/libkokocommon.so.*
%_K5lib/libkokocommon.so.%sover

%changelog
* Tue Dec 12 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.4-alt1
- new version

* Wed Dec 06 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.3-alt1
- new version

* Thu Oct 27 2022 Sergey V Turchin <zerg@altlinux.org> 22.09-alt1
- new version

* Wed Aug 18 2021 Sergey V Turchin <zerg@altlinux.org> 21.07-alt1
- initial build
