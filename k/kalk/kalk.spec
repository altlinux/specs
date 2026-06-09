%define rname kalk

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Convergent calculator
Url: http://www.kde.org
License: GPL-3.0-or-later

#Requires: qt6-feedback
Provides:  kde5-kalk = %EVR
Obsoletes: kde5-kalk < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules
#BuildRequires: qt6-feedback-devel
BuildRequires: qt6-declarative-devel qt6-svg-devel
BuildRequires: flex bison
BuildRequires: libvulkan-devel
BuildRequires: libqalculate-devel
BuildRequires: libmpfr-devel libgmp-devel
BuildRequires: kf6-kconfig-devel kf6-kcoreaddons-devel kf6-ki18n-devel kf6-kirigami-devel kf6-kunitconversion-devel

%description
Kalk is a convergent calculator application.
Although it is mainly targeted for mobile platforms.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/kalk
%_K6xdgapp/*kalk*desktop
%_K6icon/*/*/apps/*kalk*
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

