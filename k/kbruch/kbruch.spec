%define rname kbruch

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Education
Summary: Exercise Fractions
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides:  kde5-kbruch = %EVR
Obsoletes: kde5-kbruch < %EVR

Source: %rname-%version.tar
Patch: Fix-incorrect-display-of-user-interface-elements-alt.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: libvulkan-devel
BuildRequires: kf6-kauth-devel kf6-kcodecs-devel kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel
BuildRequires: kf6-kdoctools-devel kf6-ki18n-devel kf6-kwidgetsaddons-devel kf6-kxmlgui-devel kf6-kcolorscheme-devel

%description
KBruch is a small program to practice calculating with fractions and percentages.
Different exercises are provided for this purpose and you can use the learning mode
to practice with fractions. The program checks the user's input and gives feedback.

%prep
%setup -n %rname-%version
%patch -p1

%build
%K6build

%install
%K6install
%K6install_move data kbruch
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/kbruch
%_K6data/kbruch/
%_K6icon/*/*/apps/kbruch.*
%_K6xdgapp/org.kde.kbruch.desktop
%_K6cfg/kbruch.kcfg
%_datadir/metainfo/*.xml

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

