%define rname colord-kde

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Colord support for KDE
Url: https://invent.kde.org/graphics/colord-kde/
License: GPL-2.0-or-later

Requires: colord icc-profiles
Requires: kf6-kirigami-addons
Provides:  kde5-colord = %EVR
Obsoletes: kde5-colord < %EVR

Source: %rname-%version.tar
Source10: po-add-ru.po
Patch1: fix_icc_profile_delete.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules
BuildRequires: qt6-declarative-devel
BuildRequires: liblcms2-devel
BuildRequires: libvulkan-devel
BuildRequires: libXrandr-devel libXaw-devel libXres-devel libXext-devel libxcb-devel
BuildRequires: kf6-kcmutils-devel kf6-kconfigwidgets-devel kf6-kdbusaddons-devel kf6-ki18n-devel
BuildRequires: kf6-kservice-devel kf6-kwindowsystem-devel kf6-kpackage-devel
BuildRequires: kf6-kdeclarative-devel kf6-kitemmodels-devel

%description
KDE support for colord including KDE Daemon module and System Settings module.

%prep
%setup -n %rname-%version
%patch1 -p1

mv po/ru/colord-kde.po{,.old}
msgcat --use-first po/ru/colord-kde.po.old %SOURCE10 > po/ru/colord-kde.po
rm -f po/ru/colord-kde.po.old
cp -ar po/ru/colord-kde.po po/ru/kcm_colord.po

%build
%K6build

%install
%K6install
%K6install_move data locale kpackage
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc MAINTAINERS TODO
%_K6bin/*colord*
%_K6xdgapp/*colord*.desktop
%_K6plug/kf6/kded/*colord*.so
%_K6plug/plasma/kcms/systemsettings/*colord*.so


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

* Tue Feb 04 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.1-alt2
- fix russian translation

* Wed Jan 29 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.1-alt1
- new version

* Mon Nov 18 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt1
- new version

* Thu Oct 17 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

