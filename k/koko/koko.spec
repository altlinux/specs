%define rname koko
%define sover 0.0.1
%define libkokocommon libkokocommon%sover

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Image Viewer
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: %name-common >= %EVR
Requires: qt6-svg kf6-purpose kf6-kirigami-addons kde6-kquickimageeditor
Provides:  kde5-koko = %EVR
Obsoletes: kde5-koko < %EVR

Source: %rname-%version.tar
# https://download.geonames.org/export/dump/admin1CodesASCII.txt
Source101: admin1CodesASCII.txt
# https://download.geonames.org/export/dump/admin2Codes.txt
Source102: admin2Codes.txt
# https://download.geonames.org/export/dump/cities1000.zip
Source103: cities1000.txt

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules
BuildRequires: qt6-declarative-devel qt6-positioning-devel qt6-svg-devel 
BuildRequires: zip
BuildRequires: kde6-kquickimageeditor-devel kf6-kdeclarative-devel kf6-kfilemetadata-devel kf6-ki18n-devel
BuildRequires: kf6-kirigami-devel kf6-knotifications-devel kf6-kpackage-devel
BuildRequires: kf6-kirigami-addons kf6-kirigami-addons-devel
BuildRequires: kf6-purpose-devel
BuildRequires: libexiv2-devel
BuildRequires: libxcbutil-devel

%description
Koko is an image viewer designed for desktop and touch devices.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Provides:  kde5-koko-common = %EVR
Obsoletes: kde5-koko-common < %EVR
%description common
%name common package

%package -n %libkokocommon
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkokocommon
%name library


%prep
%setup -n %rname-%version
install -m 0644 %SOURCE101 src/
install -m 0644 %SOURCE102 src/
install -m 0644 %SOURCE103 ./
zip -0 src/cities1000.zip cities1000.txt
rm -f cities1000.txt

%build
%K6build

%install
%K6install
%K6install_move data koko
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*

%files
%_K6bin/koko
%_K6data/koko/
#%_K6qml/org/kde/koko/
%_K6xdgapp/*koko*.desktop
%_K6icon/*/*/apps/*koko*.*
%_K6notif/*koko*.notifyrc
%_datadir/metainfo/*koko*.xml

#%files -n %libkokocommon
#%_K6lib/libkokocommon.so.*
#%_K6lib/libkokocommon.so.%sover


%changelog
* Mon Jun 08 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.2-alt1
- new version

* Sun May 10 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.1-alt1
- new version

* Tue Mar 10 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.3-alt1
- new version

* Sat Feb 07 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.2-alt1
- new version

* Tue Jan 20 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.1-alt1
- new version

* Wed Nov 19 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.3-alt1
- new version

* Wed Sep 24 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.1-alt1
- new version

* Mon Jun 23 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.2-alt1
- new version

* Thu May 22 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.1-alt1
- new version

* Wed Mar 19 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.3-alt1
- new version

* Wed Feb 19 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.2-alt1
- new version

* Mon Feb 03 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.1-alt1
- new version

* Thu Oct 24 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

