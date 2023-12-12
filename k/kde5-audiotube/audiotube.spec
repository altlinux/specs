%define rname audiotube

%define sover 5
%define libaudiotubecore libaudiotubecore%sover

Name: kde5-%rname
Version: 23.08.4
Release: alt1
%K5init

Group: Sound
Summary: YouTube Music client
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: qt5-imageformats
Requires: python3(ytmusicapi) python3(yt_dlp)
Requires: kf5-kirigami-addons
Source: %rname-%version.tar

# Automatically added by buildreq on Mon Apr 24 2023 (-bi)
# optimized out: cmake cmake-modules debugedit elfutils fontconfig-devel gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libICE-devel libSM-devel libX11-devel libXau-devel libXext-devel libXfixes-devel libXi-devel libXmu-devel libXrender-devel libXt-devel libctf-nobfd0 libfreetype-devel libglvnd-devel libgpg-error libp11-kit libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-qml libqt5-qmlmodels libqt5-quick libqt5-quickcontrols2 libqt5-quicktemplates2 libqt5-sql libqt5-svg libqt5-widgets libqt5-x11extras libsasl2-3 libssl-devel libstdc++-devel libxcb-devel libxcbutil-keysyms libxkbcommon-devel pkg-config python-modules python2-base python3 python3-base python3-dev python3-module-cffi python3-module-charset-normalizer python3-module-idna python3-module-paste python3-module-pkg_resources python3-module-pycparser python3-module-requests python3-module-urllib3 qt5-base-devel qt5-declarative-devel rpm-build-file rpm-build-python3 sh4 tzdata xorg-proto-devel xorg-xf86miscproto-devel
#BuildRequires: appstream extra-cmake-modules kf5-kcoreaddons-devel kf5-kcrash-devel kf5-ki18n-devel kf5-kirigami-addons-devel kf5-kirigami-devel kf5-kwindowsystem-devel libXScrnSaver-devel libXaw-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXft-devel libXinerama-devel libXpm-devel libXrandr-devel libXres-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libxcbutil-devel libxcbutil-icccm-devel libxkbcommon-x11-devel libxkbfile-devel pybind11-devel python3-module-certifi python3-module-chardet python3-module-mpl_toolkits python3-module-pycryptodome python3-module-setuptools python3-module-yt_dlp python3-module-ytmusicapi python3-module-zope python3-modules-sqlite3 qt5-imageformats qt5-quickcontrols2-devel qt5-svg-devel qt5-wayland-devel qt5-webengine-devel tbb-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: pybind11-devel python3-devel python3(ytmusicapi) python3(yt_dlp)
BuildRequires: qt5-quickcontrols2-devel qt5-svg-devel
BuildRequires: futuresql-qt5-devel qcoro5-devel
BuildRequires: kf5-kirigami-addons-devel
BuildRequires: extra-cmake-modules
BuildRequires: kf5-kcoreaddons-devel kf5-kcrash-devel kf5-ki18n-devel kf5-kirigami-addons-devel
BuildRequires: kf5-kirigami-devel kf5-kwindowsystem-devel
#libXScrnSaver-devel libXaw-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXft-devel
#libXinerama-devel libXpm-devel libXrandr-devel libXres-devel libXtst-devel libXv-devel libXxf86misc-devel
#libXxf86vm-devel libxcbutil-devel libxcbutil-icccm-devel libxkbcommon-x11-devel libxkbfile-devel
# python3-module-certifi python3-module-chardet python3-module-mpl_toolkits python3-module-pycryptodome
#python3-module-setuptools python3-module-yt_dlp python3-module-ytmusicapi python3-module-zope
#python3-modules-sqlite3 qt5-imageformats

%description
Convergent YouTube Music client.

%prep
%setup -n %rname-%version

%build
%K5build \
    #

%install
%K5install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K5bin/*
%_K5xdgapp/*audiotube.desktop
%_K5icon/*/*/apps/*%{rname}*
%_datadir/metainfo/*.xml

%changelog
* Mon Dec 11 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.4-alt1
- new version

* Fri Nov 10 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.3-alt1
- new version

* Thu Nov 09 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.2-alt2
- package metadata

* Wed Oct 25 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.2-alt1
- new version

* Thu Jun 29 2023 Sergey V Turchin <zerg@altlinux.org> 23.04.2-alt1
- new version

* Tue Apr 25 2023 Sergey V Turchin <zerg@altlinux.org> 23.04.0-alt1
- initial build
