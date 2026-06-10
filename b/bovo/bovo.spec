%define rname bovo

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Games/Boards
Summary: Classic pen and paper game
Url: http://www.kde.org
License: BSD-3-Clause

Provides:  kde5-bovo = %EVR
Obsoletes: kde5-bovo < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-base-devel qt6-declarative-devel qt6-svg-devel
BuildRequires: /usr/bin/7zz
BuildRequires: libvulkan-devel
BuildRequires: kf6-kauth-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel
BuildRequires: kf6-kdbusaddons-devel  kf6-kdoctools-devel kf6-ki18n-devel kf6-kwidgetsaddons-devel
BuildRequires: kf6-kxmlgui-devel kf6-kcrash-devel kf6-kcolorscheme-devel kf6-kiconthemes-devel
BuildRequires: kde6-libkdegames-devel

%description
Bovo is a KDE game, modeled upon a classic pen and paper game,
where you try to connect five in a row prior to your opponent.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data bovo
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%_K6bin/bovo
%_K6data/bovo/
%_K6icon/*/*/apps/bovo.*
%_K6xdgapp/org.kde.bovo.desktop
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

