%define rname plasma-welcome

Name: plasma5-welcome
Version: 5.27.11
Release: alt2
%K5init

Group: Graphical desktop/KDE
Summary: First start wizard for Plasma
Url: http://www.kde.org
License: GPL-2.0-or-later

# PowerfulWhenNeeded
Requires: kf5-knewstuff

Source: %rname-%version.tar
Patch1: alt-disable-pages.patch
Patch2: alt-check-auth.patch
Patch3: alt-add-pre-distro-pages.patch
Patch4: alt-discover-apps.patch

# Automatically added by buildreq on Thu Apr 13 2023 (-bi)
# optimized out: cmake cmake-modules debugedit elfutils fontconfig-devel gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 kf5-attica-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel libICE-devel libSM-devel libX11-devel libXau-devel libXext-devel libXfixes-devel libXi-devel libXmu-devel libXrender-devel libXt-devel libctf-nobfd0 libdbusmenu-qt52 libfreetype-devel libglvnd-devel libgpg-error libp11-kit libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-qml libqt5-qmlmodels libqt5-quick libqt5-quickcontrols2 libqt5-svg libqt5-texttospeech libqt5-waylandclient libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libssl-devel libstdc++-devel libwayland-client libwayland-cursor libxcb-devel libxcbutil-keysyms libxkbcommon-devel perl pkg-config python-modules python2-base python3 python3-base python3-dev python3-module-paste qt5-base-devel qt5-declarative-devel rpm-build-file rpm-build-python3 rpm-build-qml sh4 tzdata xorg-proto-devel xorg-xf86miscproto-devel
#BuildRequires: accounts-qt5-devel appstream clang-tools extra-cmake-modules kde5-kaccounts-integration-devel kf5-kdeclarative-devel kf5-ki18n-devel kf5-kirigami-devel kf5-knewstuff-devel kf5-knotifications-devel kf5-kpackage-devel kf5-plasma-framework-devel libXScrnSaver-devel libXaw-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXft-devel libXinerama-devel libXpm-devel libXrandr-devel libXres-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libxcbutil-devel libxcbutil-icccm-devel libxkbcommon-x11-devel libxkbfile-devel python3-module-mpl_toolkits python3-module-setuptools python3-module-zope qt5-imageformats qt5-quickcontrols2-devel qt5-svg-devel qt5-wayland-devel qt5-webengine-devel rpm-build-qml6 signon-devel tbb-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules
BuildRequires: qt5-quickcontrols2-devel qt5-svg-devel qt5-wayland-devel
BuildRequires: kde5-kaccounts-integration-devel kf5-kdeclarative-devel kf5-ki18n-devel kf5-kirigami-devel
BuildRequires: kf5-knewstuff-devel kf5-knotifications-devel kf5-kpackage-devel kf5-plasma-framework-devel
BuildRequires: accounts-qt5-devel kde5-kaccounts-integration-devel signon-devel

%description
A Friendly onboarding wizard for Plasma.

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

%package -n libdrkonqi
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n libdrkonqi
%name library


%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%K5build

%install
%K5install
mkdir -p %buildroot/%_datadir/plasma-welcome-extra-pages{,-pre}
%find_lang %name --all-name

%files -f %name.lang
%doc LICENSES/*
%dir %_datadir/plasma-welcome-extra-pages/
%dir %_datadir/plasma-welcome-extra-pages-pre/
%_K5bin/plasma-welcome
%_K5qml/org/kde/plasma/welcome/
%_K5xdgapp/*plasma-welcome*.desktop
%_K5start/*plasma-welcome*.desktop
%_datadir/metainfo/*.xml

%changelog
* Wed May 29 2024 Sergey V Turchin <zerg@altlinux.org> 5.27.11-alt2
- fix russian translation

* Thu Mar 07 2024 Sergey V Turchin <zerg@altlinux.org> 5.27.11-alt1
- new version

* Wed Feb 14 2024 Sergey V Turchin <zerg@altlinux.org> 5.27.10-alt5
- fix Discover page proposed apps list (closes: 49412)

* Fri Feb 09 2024 Sergey V Turchin <zerg@altlinux.org> 5.27.10-alt4
- package extra pages dirs

* Wed Feb 07 2024 Sergey V Turchin <zerg@altlinux.org> 5.27.10-alt3
- add ability to add distro-specific pages first

* Wed Feb 07 2024 Sergey V Turchin <zerg@altlinux.org> 5.27.10-alt2
- fix russian translation (see bug#47320)

* Thu Dec 07 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.10-alt1
- new version

* Thu Nov 02 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.9-alt2
- dont force alternate placement

* Thu Oct 26 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.9-alt1
- new version

* Tue Sep 12 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.8-alt1
- new version

* Tue Aug 01 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.7-alt1
- new version

* Wed Jul 05 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.6-alt1
- new version

* Fri May 26 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.5-alt2
- hide unauthorized pages

* Wed May 10 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.5-alt1
- new version

* Thu Apr 13 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.4-alt1
- initial build
