%define rname kirigami-addons

%define kchart_sover 2
%define libkchart libkchart%kchart_sover
%define kgantt_sover 2
%define libkgantt libkgantt%kgantt_sover


Name: kf5-%rname
Version: 0.6.1
Release: alt1
%K5init

Group: System/Libraries
Summary: Set of widgets for Kirigami-based applications
Url:  https://invent.kde.org/libraries/kirigami-addons
License: GPL-2.0-or-later or LGPL-2.0-or-later

Provides: %name-dateandtime = %EVR
Obsoletes: %name-dateandtime < %EVR
Provides: %name-treeview = %EVR
Obsoletes: %name-treeview < %EVR
Requires: %name-common
# all
Requires: kf5-kirigami
# treeview
Requires: libkf5itemmodels kf5-qqc2-desktop-style

Source: %rname-%version.tar

# Automatically added by buildreq on Mon Sep 06 2021 (-bi)
# optimized out: cmake cmake-modules debugedit elfutils fontconfig gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libctf-nobfd0 libglvnd-devel libqt5-core libqt5-gui libqt5-network libqt5-qml libqt5-qmlmodels libqt5-quick libqt5-quickcontrols2 libqt5-quicktemplates2 libsasl2-3 libssl-devel libstdc++-devel perl python-modules python2-base python3 python3-base python3-module-paste qt5-base-common qt5-base-devel qt5-declarative-devel rpm-build-file rpm-build-python3 rpm-build-qml rpm-macros-python sh4 tzdata
#BuildRequires: appstream extra-cmake-modules git-core kf5-ki18n-devel kf5-kirigami-devel python-modules-compiler python3-dev qt5-quickcontrols2-devel qt5-svg-devel qt5-wayland-devel qt5-webengine-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-base-devel qt5-quickcontrols2-devel
BuildRequires: kf5-ki18n-devel kf5-kirigami-devel

%description
Set of "widgets" i.e visual end user components along with a code to support them.
Components are usable by both touch and desktop experiences providing a native experience on both,
and look native with any QQC2 style (qqc2-desktop-theme, Material or Plasma)

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description common
%name common package

%package dateandtime
Group: System/Libraries
Summary: Date and time add-on for the Kirigami framework
Requires: %name-common
Requires: kf5-kirigami
%description dateandtime
Date and time Kirigami addons, which complements other
software like Kclock.

%package treeview
Group: System/Libraries
Summary: Tree view add-on for the Kirigami framework
Requires: %name-common
Requires: libkf5itemmodels kf5-kirigami kf5-qqc2-desktop-style
%description treeview
Tree view Kirigami addon, which is useful for listing files.

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
Requires: %name-common
%description devel
This package contains the development files for %name.

%prep
%setup -n %rname-%version

%build
%K5build \
    -DKDE_INSTALL_INCLUDEDIR=%_K5inc \
    #

%install
%K5install
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*

%files
%_K5qml/org/kde/kirigamiaddons/

%files devel
%_libdir/cmake/KF5KirigamiAddons/

%changelog
* Mon Dec 05 2022 Sergey V Turchin <zerg@altlinux.org> 0.6.1-alt1
- new version

* Tue Oct 18 2022 Sergey V Turchin <zerg@altlinux.org> 0.4-alt1
- new version

* Fri Jul 01 2022 Sergey V Turchin <zerg@altlinux.org> 0.3-alt1
- new version

* Mon Sep 06 2021 Sergey V Turchin <zerg@altlinux.org> 0.2-alt1
- initial build
