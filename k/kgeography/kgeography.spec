%define rname kgeography

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Education
Summary: Geography learning program
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides:  kde5-kgeography = %EVR
Obsoletes: kde5-kgeography < %EVR

Source: %rname-%version.tar
Source2: data.tar
Patch: alt-fix-borders.patch
Patch2: alt-remove-flags.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: libvulkan-devel
BuildRequires: kf6-kauth-devel kf6-kcodecs-devel kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel
BuildRequires: kf6-kdoctools-devel kf6-ki18n-devel kf6-kiconthemes-devel kf6-kitemviews-devel
BuildRequires: kf6-kservice-devel kf6-kwidgetsaddons-devel kf6-kxmlgui-devel kf6-kcrash-devel
BuildRequires: kf6-kcolorscheme-devel

%description
%summary.

%prep
%setup -n %rname-%version
tar -xvf %SOURCE2 data/
%patch -p2
%patch2 -p2

mv data/flags/{ukraine/Crimea,russia/crimea}.png
mv data/flags/{ukraine/Donetsk,russia/donetsk}.png
mv data/flags/{ukraine/Lugansk,russia/lugansk}.png
mv data/flags/{ukraine/Zaporizhya,russia/zaporozhye}.png
mv data/flags/{ukraine/Kherson,russia/kherson}.png
mv data/flags/{ukraine/Sevastopol-city,russia/sevastopol}.png

%build
%K6build

%install
%K6install
%K6install_move data kgeography
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%_datadir/locale/*/LC_SCRIPTS/kgeography/
%_K6bin/kgeography
%_K6data/kgeography/
%_K6icon/*/*/apps/kgeography.*
%_K6xdgapp/org.kde.kgeography.desktop
%_K6cfg/kgeography.kcfg
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

* Thu Jul 31 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.3-alt2
- don't overclean flags

* Tue Jul 22 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.3-alt1
- new version

* Mon Jul 21 2025 Oleg Solovyov <mcpain@altlinux.org> 25.04.1-alt2
- remove flags

* Wed May 28 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.1-alt1
- new version

* Mon Feb 24 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.2-alt1
- new version

* Thu Nov 07 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

