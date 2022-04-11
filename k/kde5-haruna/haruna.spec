%define rname haruna

%define sover 0
%define libharuna libharuna%sover

Name: kde5-%rname
Version: 0.7.3
Release: alt2
%K5init altplace

Group: Video
Summary: Video Player
Url: https://invent.kde.org/multimedia/haruna
License: GPL-3.0-or-later

Requires: youtube-dl

Source: %rname-%version.tar
Patch1: alt-dont-save-pos.patch

BuildRequires(pre): rpm-build-kf5
BuildRequires: cmake extra-cmake-modules
BuildRequires: qt5-declarative-devel qt5-quickcontrols2-devel
BuildRequires: libmpv-devel
BuildRequires: libavformat-devel libavcodec-devel libavutil-devel libavfilter-devel libswscale-devel
BuildRequires: kf5-kconfig-devel kf5-kcoreaddons-devel kf5-kdoctools-devel kf5-kfilemetadata-devel
BuildRequires: kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kirigami-devel kf5-kxmlgui-devel
BuildRequires: plasma5-breeze-devel

%description
Haruna is an open source video player built with Qt/QML and libmpv.

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

%package -n %libharuna
Group: System/Libraries
Summary: KF5 library
#Requires: %name-common = %version-%release
%description -n %libharuna
KF5 library


%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K5build \
    -DBUILD_SHARED_LIBS=ON \
    -DBUILD_TESTS:BOOL=OFF \
    -DBUILD_EXAMPLE:BOOL=OFF \
    #

%install
%K5install
%K5install_move data locale
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/* README.md
%_K5bin/haruna
%_K5xdgapp/*haruna*.desktop
%_K5icon/hicolor/*/apps/*haruna*.*

#%files -n %libharuna
#%doc LICENSE* README.md
#%_K5lib/libharuna.so.%sover
#%_K5lib/libharuna.so.*

%changelog
* Mon Apr 11 2022 Sergey V Turchin <zerg@altlinux.org> 0.7.3-alt2
- don't save playback position by default

* Thu Dec 23 2021 Sergey V Turchin <zerg@altlinux.org> 0.7.3-alt1
- initial build
