%define rname kompare

%define sover 6
%define libkomparedialogpages libkomparedialogpages%sover
%define libkompareinterface libkompareinterface%sover

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Graphical File Differences Tool
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides:  kde5-kompare = %EVR
Obsoletes: kde5-kompare < %EVR

Source: %rname-%version.tar
Patch1: alt-hide-settings-help-btn.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kdoctools kf6-kdoctools-devel
BuildRequires: kf6-ki18n-devel kf6-kiconthemes-devel kf6-kio-devel kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-kparts-devel
BuildRequires: kf6-kservice-devel kf6-ktexteditor-devel kf6-ktextwidgets-devel kf6-kwidgetsaddons-devel
BuildRequires: kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel kf6-syntax-highlighting-devel
BuildRequires: kde6-libkomparediff2-devel

%description
Kompare is a GUI front-end program that enables differences between source files to be viewed and merged.
Kompare can be used to compare differences on files or the contents of folders. Kompare supports a variety
of diff formats and provide many options to customize the information level displayed.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Provides:  kde5-kompare-common = %EVR
Obsoletes: kde5-kompare-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkomparedialogpages
Group: System/Libraries
Summary: KF6 library
Requires: %name-common >= %EVR
Obsoletes: libkomparedialogpages5 < %EVR
%description -n %libkomparedialogpages
KF6 library

%package -n %libkompareinterface
Group: System/Libraries
Summary: KF6 library
Requires: %name-common >= %EVR
Obsoletes: libkompareinterface5 < %EVR
%description -n %libkompareinterface
KF6 library


%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K6build \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    #

%install
%K6install
%K6install_move data kio
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*

%files
%_K6bin/kompare
%_K6plug/kf6/parts/kompare*.so
%_K6xdgapp/org.kde.kompare.desktop
%_K6icon/hicolor/*/apps/*kompare*.*
%_K6data/kio/servicemenus/*kompare*.desktop
%_datadir/qlogging-categories6/*.*categories
%_datadir/metainfo/*.xml

%files devel
#%_K6inc/kompare_version.h
%_K6inc/kompare/
%_K6link/lib*.so
#%_K6lib/cmake/kompare

%files -n %libkompareinterface
%_K6lib/libkompareinterface.so.%sover
%_K6lib/libkompareinterface.so.*
%files -n %libkomparedialogpages
%_K6lib/libkomparedialogpages.so.%sover
%_K6lib/libkomparedialogpages.so.*


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

