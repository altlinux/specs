%define rname tokodon

Name: kde5-%rname
Version: 23.08.5
Release: alt2
%K5init no_appdata

Group: Networking/Chat
Summary: Mastodon client
Url: http://www.kde.org
License:  GPL-3.0-only

Requires: libkf5sonnetui libkf5itemmodels

Source: %rname-%version.tar
Patch: alt-fix-logout.patch

# Automatically added by buildreq on Tue May 02 2023 (-bi)
# optimized out: cmake cmake-modules debugedit elfutils fontconfig-devel gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdbusaddons-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel libICE-devel libSM-devel libX11-devel libXau-devel libXext-devel libXfixes-devel libXi-devel libXmu-devel libXrender-devel libXt-devel libctf-nobfd0 libdbusmenu-qt52 libfreetype-devel libglvnd-devel libgpg-error libp11-kit libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-multimedia libqt5-network libqt5-qml libqt5-qmlmodels libqt5-quick libqt5-quickcontrols2 libqt5-quicktemplates2 libqt5-svg libqt5-test libqt5-texttospeech libqt5-waylandclient libqt5-websockets libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libssl-devel libstdc++-devel libwayland-client libwayland-cursor libxcb-devel libxcbutil-keysyms libxkbcommon-devel pkg-config python-modules python2-base python3 python3-base python3-dev python3-module-paste qt5-base-common qt5-base-devel qt5-declarative-devel rpm-build-file rpm-build-python3 sh4 tzdata xorg-proto-devel xorg-xf86miscproto-devel
#BuildRequires: appstream clang-tools extra-cmake-modules kf5-ki18n-devel kf5-kio-devel kf5-kirigami-addons-devel kf5-kirigami-devel kf5-knotifications-devel kf5-qqc2-desktop-style-devel libXScrnSaver-devel libXaw-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXft-devel libXinerama-devel libXpm-devel libXrandr-devel libXres-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libkf5itemmodels libkf5sonnetcore libqtkeychain-qt5-devel libxcbutil-devel libxcbutil-icccm-devel libxkbcommon-x11-devel libxkbfile-devel python3-module-mpl_toolkits python3-module-setuptools python3-module-zope qt5-imageformats qt5-multimedia-devel qt5-quickcontrols2-devel qt5-svg-devel qt5-wayland-devel qt5-webengine-devel qt5-websockets-devel tbb-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules
BuildRequires: libqtkeychain-qt5-devel
BuildRequires: libmpv-devel
BuildRequires: qt5-multimedia-devel qt5-quickcontrols2-devel qt5-svg-devel qt5-websockets-devel
BuildRequires: kf5-ki18n-devel kf5-kio-devel kf5-kirigami-addons-devel kf5-kirigami-devel
BuildRequires: kf5-knotifications-devel kf5-qqc2-desktop-style-devel kf5-kirigami-addons-devel

%description
A modern Mastodon client.

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

%package -n libkf5imagemapeditor
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n libkf5imagemapeditor
%name library


%prep
%setup -n %rname-%version
%patch -p1

%build
%K5build

%install
%K5install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K5bin/tokodon
%_K5xdgapp/*tokodon*.desktop
%_K5icon/*/*/apps/*tokodon*
%_K5notif/*tokodon*.notifyrc
%_datadir/qlogging-categories5/*.*categories

%changelog
* Thu Jun 06 2024 Daniil-Viktor Ratkin <krf10@altlinux.org> 23.08.5-alt2
- fix segfault at logout (closes: 47155)

* Mon Feb 19 2024 Sergey V Turchin <zerg@altlinux.org> 23.08.5-alt1
- new version

* Tue Dec 12 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.4-alt1
- new version

* Fri Nov 10 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.3-alt1
- new version

* Mon Oct 16 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.2-alt1
- new version

* Fri Jul 14 2023 Sergey V Turchin <zerg@altlinux.org> 23.04.3-alt1
- new version

* Fri Jun 09 2023 Sergey V Turchin <zerg@altlinux.org> 23.04.2-alt1
- new version

* Wed Jun 07 2023 Sergey V Turchin <zerg@altlinux.org> 23.04.1-alt1
- new version

* Tue May 02 2023 Sergey V Turchin <zerg@altlinux.org> 23.04.0-alt1
- initial build
