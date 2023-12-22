%define rname aura-browser

Name: plasma5-%rname
Version: 5.27.10
Release: alt1
%K5init

Group: Networking/WWW
Summary: Web-browser for TV
Url: http://www.kde.org
License: GPL-2.0-or-later

ExcludeArch: %not_qt5_qtwebengine_arches

Requires: qt5-qtdeclarative qt5-graphicaleffects qt5-virtualkeyboard qt5-svg qt5-imageformats qml(QtWebEngine) kf5-kirigami

Source: %rname-%version.tar

# Automatically added by buildreq on Fri Dec 22 2023 (-bi)
# optimized out: bash5 cmake cmake-modules debugedit elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 gtk4-update-icon-cache libctf-nobfd0 libdouble-conversion3 libglvnd-devel libgpg-error libp11-kit libqt5-core libqt5-gui libqt5-multimedia libqt5-network libqt5-positioning libqt5-qml libqt5-qmlmodels libqt5-quick libqt5-quickcontrols2 libqt5-test libqt5-webchannel libqt5-webengine libqt5-webenginecore libqt5-widgets libsasl2-3 libssl-devel libstdc++-devel python3 python3-base python3-dev python3-module-paste python3-module-setuptools qt5-base-devel qt5-declarative-devel qt5-location-devel qt5-webchannel-devel rpm-build-file rpm-build-python3 sh5 tzdata
#BuildRequires: appstream extra-cmake-modules kf5-ki18n-devel kf5-kirigami-devel python3-module-mpl_toolkits python3-module-zope qt5-imageformats qt5-multimedia-devel qt5-quickcontrols2-devel qt5-svg-devel qt5-wayland-devel qt5-webengine-devel
BuildRequires(pre): rpm-build-kf5 rpm-macros-qt5-webengine
BuildRequires: extra-cmake-modules
BuildRequires: qt5-multimedia-devel qt5-quickcontrols2-devel qt5-svg-devel qt5-wayland-devel qt5-webengine-devel
BuildRequires: kf5-ki18n-devel kf5-kirigami-devel

%description
Browser for a fully immersed Big Screen experience allowing you to navigate the world wide web using just your remote control.

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

%build
%K5build \
    #

%install
%K5install
%find_lang %name --all-name

%files -f %name.lang
%doc LICENSES/*
%_K5bin/aura-browser
%_K5xdgapp/*aura-browser*.desktop
%_K5icon/hicolor/*/apps/*aura-browser*.*
%_datadir/metainfo/*.xml

%changelog
* Fri Dec 22 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.10-alt1
- initial build
