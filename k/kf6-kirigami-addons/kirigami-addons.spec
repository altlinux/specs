%define rname kirigami-addons

Name: kf6-%rname
Version: 1.3.0
Release: alt1
%K6init

Group: System/Libraries
Summary: Set of widgets for Kirigami-based applications
Url:  https://invent.kde.org/libraries/kirigami-addons
License: GPL-2.0-or-later or LGPL-2.0-or-later

Requires: kde-common
# all
Requires: kf6-kirigami
# qmlmodels
Requires: libqt6-qmlmodels
# treeview
Requires: libkf6itemmodels
# kiconthemes
Requires: libkf6iconthemes

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-base-devel qt6-declarative-devel
BuildRequires: kf6-ki18n-devel kf6-kconfig-devel kf6-kirigami-devel

%description
Set of "widgets" i.e visual end user components along with a code to support them.
Components are usable by both touch and desktop experiences providing a native experience on both,
and look native with any QQC2 style (qqc2-desktop-theme, Material or Plasma)

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
Requires: kf6-filesystem
%description devel
This package contains the development files for %name.

%prep
%setup -n %rname-%version

%build
%K6build \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    #

%install
%K6install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6qml/org/kde/kirigamiaddons/

%files devel
%_libdir/cmake/KF6KirigamiAddons/

%changelog
* Thu Jun 27 2024 Sergey V Turchin <zerg@altlinux.org> 1.3.0-alt1
- initial build
