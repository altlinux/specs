%define rname zanshin

%define sover 5
%define libzanshin libzanshin%sover

Name: kde5-%rname
Version: 23.08.5
Release: alt1
%K5init

Group: Office
Summary: TODO Manager
Url: http://www.kde.org
License: LGPL-2.0-or-later and GPL-2.0-or-later

ExcludeArch: %not_qt5_qtwebengine_arches

Provides: %{name}-common = %EVR
Obsoletes: %{name}-common < %EVR
Requires: kde5-akonadi

Source: %rname-%version.tar
Patch1: alt-migrator-segfault.patch

# Automatically added by buildreq on Tue Feb 15 2022 (-bi)
# optimized out: boost-devel boost-devel-headers cmake cmake-modules debugedit elfutils fontconfig fontconfig-devel gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 gtk-update-icon-cache kde5-kontactinterface-common kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-ki18n-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-plasma-framework-devel kf5-solid-devel kf5-sonnet-devel libICE-devel libSM-devel libX11-devel libXau-devel libXext-devel libXfixes-devel libXi-devel libXmu-devel libXrender-devel libXt-devel libctf-nobfd0 libdb4-devel libdbusmenu-qt52 libfreetype-devel libglvnd-devel libgpg-error libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-qmlmodels libqt5-quick libqt5-sql libqt5-svg libqt5-test libqt5-texttospeech libqt5-waylandclient libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libssl-devel libstdc++-devel libwayland-client libwayland-cursor libxcb-devel libxcbutil-keysyms libxkbcommon-devel pkg-config python-modules python2-base python3 python3-base python3-dev python3-module-paste qt5-base-common qt5-base-devel rpm-build-file rpm-build-python3 rpm-macros-python sh4 tzdata xorg-proto-devel xorg-xf86miscproto-devel
#BuildRequires: appstream extra-cmake-modules kde5-akonadi-calendar-devel kde5-akonadi-devel kde5-kontactinterface-devel kf5-kcalcore-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kpackage-devel kf5-kparts-devel kf5-krunner-devel kf5-ktextwidgets-devel libXScrnSaver-devel libXaw-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXft-devel libXinerama-devel libXpm-devel libXrandr-devel libXres-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libxcbutil-devel libxcbutil-icccm-devel libxkbcommon-x11-devel libxkbfile-devel python-modules-compiler python3-module-setuptools python3-module-zope qt5-imageformats qt5-svg-devel qt5-wayland-devel qt5-webengine-devel
BuildRequires(pre): rpm-build-kf5 rpm-macros-qt5-webengine
BuildRequires: extra-cmake-modules qt5-base-devel
BuildRequires: kf5-kcalcore-devel kf5-kio-devel kf5-kitemmodels-devel kf5-kpackage-devel kf5-kparts-devel
BuildRequires: kf5-krunner-devel kf5-ktextwidgets-devel
BuildRequires: kde5-akonadi-calendar-devel kde5-akonadi-devel kde5-kontactinterface-devel
BuildRequires: kde5-kidentitymanagement-devel kde5-kpimtextedit-devel

%description
A Getting Things Done application which aims at getting your mind like water.

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
%_K5bin/zanshin*
%_K5plug/kf5/krunner/*zanshin*.so
%_K5plug/pim5/kontact/*zanshin*.so
%_K5plug/*zanshin*.so
%_K5xdgapp/*zanshin*.desktop
%_K5xmlgui/zanshin/
%_K5icon/hicolor/*/apps/*zanshin*.*
%_datadir/metainfo/*.xml

%changelog
* Fri Feb 16 2024 Sergey V Turchin <zerg@altlinux.org> 23.08.5-alt1
- new version

* Mon Feb 05 2024 Dmitrii Fomchenkov <sirius@altlinux.org> 23.08.4-alt3
- fix language switching (closes: 48928)

* Wed Dec 20 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.4-alt2
- add fix against migrator segfault (closes: 44720) (thanks sirius@alt)

* Fri Dec 08 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.4-alt1
- new version

* Fri Nov 10 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.3-alt1
- new version

* Fri Oct 13 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.2-alt1
- new version

* Thu Sep 21 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.1-alt1
- new version

* Fri Jul 14 2023 Sergey V Turchin <zerg@altlinux.org> 23.04.3-alt1
- new version

* Fri Jun 09 2023 Sergey V Turchin <zerg@altlinux.org> 23.04.2-alt1
- new version

* Fri May 12 2023 Sergey V Turchin <zerg@altlinux.org> 23.04.1-alt1
- new version

* Mon Mar 06 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.3-alt1
- new version

* Fri Feb 03 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.2-alt1
- new version

* Wed Jan 11 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.1-alt1
- new version

* Mon Nov 07 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.3-alt1
- new version

* Tue Oct 18 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.2-alt1
- new version

* Thu Sep 08 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.1-alt1
- new version

* Mon Jul 11 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.3-alt1
- new version

* Fri Jun 10 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.2-alt1
- new version

* Fri May 13 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.1-alt1
- new version

* Fri Mar 04 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.3-alt1
- new version

* Mon Feb 28 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.2-alt2
- fix package translations

* Mon Feb 21 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.2-alt1
- new version

* Tue Feb 15 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.1-alt1
- initial build
