%define rname krecorder

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Audio Recorder
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: kf6-kirigami-addons
Provides:  kde5-krecorder = %EVR
Obsoletes: kde5-krecorder < %EVR

Source: %rname-%version.tar
Patch0: fix-incorrect-recording-saving.patch
Patch1: fix-text-overlay.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-base-devel
BuildRequires: qt6-multimedia-devel qt6-declarative-devel qt6-svg-devel qt6-wayland-devel
BuildRequires: kf6-kirigami-addons-devel
BuildRequires: kf6-kconfig-devel kf6-ki18n-devel kf6-kirigami-devel kf6-kcoreaddons-devel
BuildRequires: kf6-kwindowsystem-devel

%description
A convergent audio recording application for Plasma.
Features:
* Record audio with a visualizer, and pausing functionality
* Ability to select audio sources
* Ability to select encoding and container formats
* Audio playback with a visualizer

%prep
%setup -n %rname-%version
#%patch0 -p2
#%patch1 -p2

%build
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/krecorder
%_K6xdgapp/*krecorder*.desktop
%_K6icon/hicolor/*/apps/*krecorder*.*
%_datadir/metainfo/*.xml

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

