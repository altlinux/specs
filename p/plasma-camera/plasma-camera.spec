%define rname plasma-camera

%define sover 0
%define libplasma_camera libplasma-camera%sover

Name: %rname
Version: 2.1.0
Release: alt1
%K6init

Group:  Video
Summary: Simple camera application for mobile devices
License: GPL-3.0-only
Url: https://anongit.kde.org/plasma-camera.git

Provides: kde5-plasma-camera = %EVR
Obsoletes: kde5-plasma-camera < %EVR

Requires: qt6-multimedia kf6-kirigami

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: qt6-declarative-devel qt6-svg-devel qt6-wayland-devel qt6-multimedia-devel qt6-sensors-devel
BuildRequires: extra-cmake-modules
BuildRequires: kf6-kcoreaddons-devel kf6-ki18n-devel kf6-kconfig-devel kf6-kirigami-devel
BuildRequires: libcamera-devel libexiv2-devel

%description
Simple camera application for mobile devices.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install

%find_lang --all-name --with-qt %name

%files -f %name.lang
%_K6bin/*camera*
%_K6xdgapp/*camera*.desktop
%_datadir/metainfo/*.xml

%changelog
* Thu Nov 13 2025 Sergey V Turchin <zerg@altlinux.org> 2.1.0-alt1
- new version

* Thu Jul 31 2025 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt1
- new version
- rename package

* Tue Nov 14 2023 Sergey V Turchin <zerg@altlinux.org> 1.0-alt2
- package metadata

* Fri Mar 20 2020 Sergey V Turchin <zerg@altlinux.org> 1.0-alt1
- initial build
