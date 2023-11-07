%define rname flatpak-kcm

Name: plasma5-%rname
Version: 5.27.9
Release: alt2
%K5init

Group: System/Configuration/Packaging
Summary: KDE Flatpak Permissions Management
Url: http://www.kde.org
License: BSD-2-Clause and BSD-3-Clause and CC0-1.0 and GPL-2.0-or-later

#Requires: flatpak

Source: %rname-%version.tar

# Automatically added by buildreq on Tue Apr 18 2023 (-bi)
# optimized out: cmake cmake-modules debugedit elfutils gcc-c++ glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 kf5-kauth-devel kf5-kcodecs-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kservice-devel kf5-kwidgetsaddons-devel libctf-nobfd0 libgio-devel libglvnd-devel libgpg-error libjson-glib libostree-devel libp11-kit libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-qml libqt5-qmlmodels libqt5-quick libqt5-svg libqt5-waylandclient libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libssl-devel libstdc++-devel libwayland-client libwayland-cursor libxcbutil-keysyms pkg-config python-modules python2-base python3 python3-base python3-dev python3-module-paste qt5-base-devel qt5-declarative-devel rpm-build-file rpm-build-python3 rpm-build-qml rpm-macros-python sh4 tzdata
#BuildRequires: appstream clang-tools extra-cmake-modules kf5-kcmutils-devel kf5-kdeclarative-devel kf5-ki18n-devel kf5-kpackage-devel libflatpak-devel python-modules-compiler python3-module-mpl_toolkits python3-module-setuptools python3-module-zope qt5-imageformats qt5-svg-devel qt5-wayland-devel qt5-webengine-devel rpm-build-qml6 tbb-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules
BuildRequires: qt5-svg-devel qt5-declarative-devel
BuildRequires: libflatpak-devel
BuildRequires: kf5-kitemmodels-devel kf5-kcmutils-devel kf5-kdeclarative-devel kf5-ki18n-devel kf5-kpackage-devel

%description
The KCM allows changing what permissions have been granted to installed Flatpak applications.

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

%package -n libkf5flatpak-kcm
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n libkf5flatpak-kcm
%name library


%prep
%setup -n %rname-%version

%build
%K5build \
    #

%install
%K5install
%K5install_move data kpackage
%find_lang %name --all-name

%files -f %name.lang
%doc LICENSES/*
%_K5plug/plasma/kcms/systemsettings/*flatpak*.so
%_K5xdgapp/*flatpak*.desktop
%_K5data/kpackage/kcms/kcm_flatpak/

%changelog
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

* Wed May 10 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.5-alt1
- new version

* Tue Apr 18 2023 Sergey V Turchin <zerg@altlinux.org> 5.27.4-alt1
- initial build
