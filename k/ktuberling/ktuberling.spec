%define rname ktuberling

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Games/Educational
Summary: "Potato editor" game
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides:  kde5-ktuberling = %EVR
Obsoletes: kde5-ktuberling < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-base-devel qt6-declarative-devel qt6-svg-devel qt6-multimedia-devel
BuildRequires: qt6-phonon-devel
BuildRequires: /usr/bin/7zz
BuildRequires: libvulkan-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdbusaddons-devel 
BuildRequires: kf6-kdoctools-devel kf6-kguiaddons-devel kf6-ki18n-devel
BuildRequires: kf6-kiconthemes-devel kf6-kio-devel kf6-kitemmodels-devel kf6-kitemviews-devel kf6-kjobwidgets-devel
BuildRequires: kf6-knewstuff-devel kf6-knotifications-devel kf6-knotifyconfig-devel kf6-kparts-devel kf6-kservice-devel
BuildRequires: kf6-ktextwidgets-devel kf6-kunitconversion-devel kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel
BuildRequires: kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel
BuildRequires: kde6-libkdegames-devel

%description
KTuberling is a "potato editor" game intended for small
children and adults who remain young at heart. The game
has no winner; the only purpose is to make the funniest
faces you can.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data ktuberling
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories
%_K6bin/ktuberling
%_K6data/ktuberling/
%_K6xdgapp/org.kde.ktuberling.desktop
%_K6icon/*/*/apps/ktuberling.*
%_K6icon/*/*/mimetypes/application-x-tuberling.*
%_datadir/metainfo/*.xml


%changelog
* Tue Jun 09 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.2-alt1
- new version

* Mon May 11 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.1-alt1
- new version

* Sat Feb 07 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.2-alt1
- new version

* Tue Jan 20 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.1-alt1
- new version

* Thu Oct 23 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.2-alt1
- new version

* Tue Jul 22 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.3-alt1
- new version

* Fri May 30 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.1-alt1
- new version

* Tue Feb 25 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.2-alt1
- new version

* Mon Nov 11 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt1
- initial build

