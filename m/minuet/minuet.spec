%define rname minuet

%define minuet_sover 0.3.0
%define libminuetinterfaces libminuetinterfaces%minuet_sover

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Education
Summary: Music Education Software
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides:  kde5-minuet = %EVR
Obsoletes: kde5-minuet < %EVR

Requires: kf6-kirigami

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-declarative-devel qt6-svg-devel
BuildRequires: libvulkan-devel
BuildRequires: drumstick-devel libalsa-devel libfluidsynth-devel
BuildRequires: kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel kf6-kcrash-devel  kf6-kdoctools-devel kf6-ki18n-devel kf6-kio-devel kf6-kirigami kf6-kirigami-devel
BuildRequires: kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-kservice-devel kf6-kwidgetsaddons-devel
BuildRequires: kf6-kxmlgui-devel kf6-solid-devel

%description
Minuet is an application for music education. It features a set of ear training exercises regarding intervals, chords, scales and more.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Provides:  kde5-minuet-common = %EVR
Obsoletes: kde5-minuet-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libminuetinterfaces
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n %libminuetinterfaces
%name library

%prep
%setup -n %rname-%version

#sed -i 's|^#set(FluidSynth_VERSION|set(FluidSynth_VERSION|' cmake/FindFluidSynth.cmake

%build
%K6build \
    -DQT_MAJOR_VERSION=6 \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    #

%install
%K6install
%K6install_move data minuet
%find_lang %name --with-kde --all-name

%files
%_K6bin/minuet
%_K6data/minuet/
%_K6icon/hicolor/*/apps/minuet.*
%_K6icon/hicolor/*/actions/minuet-*.*
%_K6xdgapp/org.kde.minuet.desktop
%_K6plug/minuet/
%_datadir/metainfo/*.xml

%files common -f %name.lang
%doc COPYING*

%files -n %libminuetinterfaces
%_K6lib/libminuetinterfaces.so.*
%_K6lib/libminuetinterfaces.so.%minuet_sover

%files devel
%_K6link/libminuetinterfaces.so
%_K6inc/minuet/


%changelog
* Tue Jun 09 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.2-alt1
- new version

* Mon May 11 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.1-alt1
- new version

* Tue Mar 10 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.3-alt1
- new version

* Sat Feb 07 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.2-alt1
- new version

* Tue Jan 20 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.1-alt1
- new version

* Wed Oct 22 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.2-alt1
- new version

* Tue Jul 22 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.3-alt1
- new version

* Wed May 28 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.1-alt1
- new version

* Mon Feb 24 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.2-alt1
- new version

* Thu Nov 07 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

