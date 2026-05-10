%define rname kirigami-gallery

Name: %rname
Version: 26.04.1
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Widget Browser for Kirigami
Url: http://www.kde.org
License: LGPL-2.0-or-later

Provides: kde5-kirigami-gallery = %EVR
Obsoletes: kde5-kirigami-gallery < %EVR

#Requires: qml6(org.kde.kitemmodels)
Requires: libkf6itemmodels

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-svg-devel qt6-tools-devel
BuildRequires: libvulkan-devel
BuildRequires: kf6-kitemmodels-devel
BuildRequires: kf6-kirigami-devel


%description
Application which uses all features from kirigami,
including links to the sourcecode, tips on how to use
the components and links to the corresponding
HIG pages and code examples on invent.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data locale
%find_lang %name --with-kde --all-name
%K6find_qtlang %name --all-name

%files -f %name.lang
%doc LICENSE*
%_K6bin/*
%_K6xdgapp/*.desktop
%_datadir/metainfo/*gallery*.xml

%changelog
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

