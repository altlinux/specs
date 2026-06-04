%define rname ffmpegthumbs

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Video
Summary: Video thumbnail generator
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: kde5-ffmpegthumbs = %EVR
Obsoletes: kde5-ffmpegthumbs < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: libavcodec-devel libavutil-devel libavdevice-devel libavformat-devel libpostproc-devel libswscale-devel libavfilter-devel
#BuildRequires: taglib-devel
BuildRequires: kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kio-devel kf6-kitemviews-devel kf6-kjobwidgets-devel
BuildRequires: kf6-kservice-devel kf6-kwidgetsaddons-devel kf6-kxmlgui-devel kf6-solid-devel kf6-ki18n-devel

%description
Video thumbnail generator for KDE.

%prep
%setup -n %rname-%version

%build
%K6build \
    -DQT_MAJOR_VERSION=6 \
    #

%install
%K6install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories
%_K6cfg/ffmpegthumb*.kcfg
%_K6plug/kf6/thumbcreator/ffmpegthumbs.so
%_datadir/metainfo/*.xml


%changelog
* Thu Jun 04 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.2-alt1
- new version

* Fri May 08 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.1-alt1
- new version

* Fri Mar 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.3-alt1
- new version

* Fri Feb 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.2-alt1
- new version

* Mon Jan 19 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.1-alt1
- new version

* Tue Nov 18 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.3-alt1
- new version

* Mon Oct 13 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.2-alt1
- new version

* Mon Sep 22 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.1-alt1
- new version

* Thu Jul 24 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.3-alt1
- new version

* Tue Jun 10 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.2-alt1
- new version

* Mon May 12 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.1-alt1
- new version

* Mon Apr 21 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.0-alt1
- new version

* Tue Mar 11 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.3-alt1
- new version

* Tue Feb 18 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.2-alt1
- new version

* Mon Jan 20 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.1-alt1
- new version

* Wed Nov 13 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt1
- new version

* Fri Oct 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- new version

* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- initial build

