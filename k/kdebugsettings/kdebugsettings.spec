%define rname kdebugsettings

%define sover 6
%define libkdebugsettings libkdebugsettings%sover
%define libkdebugsettingscore libkdebugsettingscore%sover

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: KDE KDebug Settings
Url: http://www.kde.org
License: LGPL-2.0-or-later

Provides:  kde5-kdebugsettings = %EVR
Obsoletes: kde5-kdebugsettings < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel kf6-kdbusaddons-devel kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel kf6-kio-devel
BuildRequires: kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-kservice-devel kf6-kwidgetsaddons-devel kf6-kxmlgui-devel kf6-solid-devel

%description
%summary.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Provides:  kde5-kdebugsettings-common = %EVR
Obsoletes: kde5-kdebugsettings-common < %EVR
%description common
%name common package.

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkdebugsettings
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libkdebugsettings5 < %EVR
%description -n %libkdebugsettings
%name library.

%package -n %libkdebugsettingscore
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libkdebugsettingscore5 < %EVR
%description -n %libkdebugsettingscore
%name library.


%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data kdebugsettings
%find_lang %name --with-kde --all-name


%files common -f %name.lang
%_K6data/kdebugsettings/
%_datadir/qlogging-categories6/*.*categories

%files
%_K6bin/*
%_K6xdgapp/*
%_datadir/metainfo/*.xml

%files -n %libkdebugsettings
%_K6lib/libkdebugsettings.so.*
%_K6lib/libkdebugsettings.so.%sover
%files -n %libkdebugsettingscore
%_K6lib/libkdebugsettingscore.so.*
%_K6lib/libkdebugsettingscore.so.%sover


%changelog
* Fri Jun 05 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.2-alt1
- new version

* Sun May 10 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.1-alt1
- new version

* Fri Mar 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.3-alt1
- new version

* Fri Feb 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.2-alt1
- new version

* Mon Jan 19 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.1-alt1
- new version

* Wed Nov 19 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.3-alt1
- new version

* Mon Oct 13 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.2-alt1
- new version

* Tue Sep 23 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.1-alt1
- new version

* Fri Jul 25 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.3-alt1
- new version

* Wed Jun 11 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.2-alt1
- new version

* Wed May 14 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.1-alt1
- new version

* Tue Mar 11 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.3-alt1
- new version

* Thu Mar 06 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.2-alt1
- new version

* Wed Jan 29 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.1-alt1
- new version

* Mon Nov 18 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt1
- new version

* Thu Oct 17 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

