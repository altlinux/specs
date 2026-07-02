%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%define rname plasma-welcome

Name: %rname
Version: 6.7.2
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: First start wizard for Plasma
Url: http://www.kde.org
License: GPL-2.0-or-later

# PowerfulWhenNeeded
#Requires: kf6-knewstuff

Provides: plasma5-welcome = %EVR
Obsoletes: plasma5-welcome < %EVR

Source: %rname-%version.tar
Source10: po-add-ru.po
Patch2: alt-check-auth.patch
Patch3: alt-prepend-distro-pages.patch
Patch4: alt-icons.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules
BuildRequires: libvulkan-devel
BuildRequires: qt6-declarative-devel qt6-svg-devel qt6-wayland-devel
BuildRequires: kf6-kdeclarative-devel kf6-ki18n-devel kf6-kirigami-devel
BuildRequires: kf6-knewstuff-devel kf6-knotifications-devel kf6-kpackage-devel kf6-kcmutils-devel kf6-ksvg-devel
BuildRequires: kf6-kirigami-addons-devel
BuildRequires: accounts-qt6-devel
BuildRequires: plasma6-lib-devel
# kaccounts-integration-devel signon-devel

%description
A Friendly onboarding wizard for Plasma.

%prep
%setup -n %rname-%version
%patch2 -p1
%patch3 -p1
%patch4 -p1

msgcat --use-first %SOURCE10 po/ru/plasma-welcome.po > po/ru/plasma-welcome.po.tmp
cat po/ru/plasma-welcome.po.tmp > po/ru/plasma-welcome.po
rm -f po/ru/plasma-welcome.po.tmp

%build
%K6build

%install
%K6install
mkdir -p %buildroot/%_K6data/plasma/plasma-welcome/extra-pages/
mkdir -p %buildroot/%_datadir/plasma-welcome-extra-pages-pre/
%find_lang %name --all-name

%files -f %name.lang
%doc LICENSES/*
%dir %_datadir/plasma-welcome-extra-pages-pre/
%_K6bin/plasma-welcome
%_K6qml/org/kde/plasma/welcome/
%_K6plug/kf6/kded/*welcome*.so
%_K6data/plasma/plasma-welcome/
%_K6xdgapp/*plasma-welcome*.desktop
%_datadir/qlogging-categories6/*.*categories
%_datadir/metainfo/*.xml

%changelog
* Wed Jul 01 2026 Sergey V Turchin <zerg@altlinux.org> 6.7.2-alt1
- new version

* Mon Jun 29 2026 Sergey V Turchin <zerg@altlinux.org> 6.7.1-alt1
- new version

* Tue May 12 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.5-alt1
- new version

* Thu Apr 09 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.4-alt1
- new version

* Mon Mar 30 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.3-alt1
- new version

* Wed Mar 11 2026 Sergey V Turchin <zerg@altlinux.org> 6.5.6-alt1
- new version

* Thu Jan 15 2026 Sergey V Turchin <zerg@altlinux.org> 6.5.5-alt1
- new version

* Wed Dec 10 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.4-alt1
- new version

* Tue Nov 18 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.3-alt1
- new version

* Thu Nov 13 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.2-alt1
- new version

* Wed Nov 12 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.6-alt1
- new version

* Wed Oct 29 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.5-alt2
- don't change default Discover apps suggestions

* Tue Sep 16 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.5-alt1
- new version

* Fri Aug 22 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.4-alt1
- new version

* Mon Jul 21 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.3-alt2
- fix l10n

* Tue Jul 15 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.3-alt1
- new version

* Tue Jul 08 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt1
- new version

* Wed May 07 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.5-alt1
- new version

* Wed Apr 02 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.4-alt1
- new version

* Wed Mar 12 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.3-alt1
- new version

* Wed Mar 05 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.2-alt3
- fix panel mock main menu icon

* Wed Mar 05 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.2-alt2
- fix russian translation (closes: 47320)

* Wed Feb 26 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.2-alt1
- new version

* Wed Feb 19 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.1-alt1
- new version

* Fri Feb 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Thu Jan 09 2025 Sergey V Turchin <zerg@altlinux.org> 6.2.5-alt1
- new version

* Tue Nov 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt1
- new version

* Wed Nov 06 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.3-alt1
- new version

* Mon Oct 28 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.2-alt1
- new version

* Tue Sep 10 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.5-alt1
- new version

* Thu Aug 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.4-alt1
- new version

* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build

