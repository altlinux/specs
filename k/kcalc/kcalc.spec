%define rname kcalc

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Scientific Calculator
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: kde5-kcalc = %EVR
Obsoletes: kde5-kcalc < %EVR

Source: %rname-%version.tar
Source10: add-ru.po
Patch1: alt-i18n.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: libgmp-devel libmpfr-devel libmpc-devel
BuildRequires: kf6-kauth-devel kf6-kcodecs-devel kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel
BuildRequires: kf6-kguiaddons-devel kf6-ki18n-devel kf6-knotifications-devel kf6-kwidgetsaddons-devel kf6-kxmlgui-devel
BuildRequires: kf6-kcrash-devel kf6-kcolorscheme-devel kf6-kiconthemes-devel

%description
%summary.

%prep
%setup -n %rname-%version
%patch1 -p1

msgcat --use-first %SOURCE10 po/ru/kcalc.po > po/ru/kcalc.po.tmp
cat po/ru/kcalc.po.tmp > po/ru/kcalc.po
rm -f po/ru/kcalc.po.tmp

%build
%K6build

%install
%K6install
%K6install_move data kcalc kglobalaccel kconf_update
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/kcalc
%_K6data/kglobalaccel/*kcalc*
%_K6xdgapp/*kcalc*
%_K6conf_up/*kcalc*
%_K6cfg/*kcalc*
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

* Thu Apr 10 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.3-alt2
- fix i18n

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

