%define rname parley
%add_findreq_skiplist %_K6data/parley/plugins/*.py

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Education
Summary: Vocabulary training application
Url: http://www.kde.org
License: GPL-2.0-or-later or GPL-3.0-only

Requires: kdeedu-data
Requires: translate-shell
Provides:  kde5-parley = %EVR
Obsoletes: kde5-parley < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6-webengine
BuildRequires: extra-cmake-modules qt6-multimedia-devel qt6-declarative-devel qt6-svg-devel
%ifarch %qt6_qtwebengine_arches
BuildRequires: qt6-webengine-devel
%endif
BuildRequires: libvulkan-devel
BuildRequires: libxslt-devel xsltproc
BuildRequires: kf6-kauth-devel kf6-kbookmarks-devel kf6-kcmutils-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel 
BuildRequires: kf6-kdoctools kf6-kdoctools-devel kf6-ki18n-devel kf6-kiconthemes-devel kf6-kio-devel
BuildRequires: kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-knewstuff-devel kf6-knotifications-devel
BuildRequires: kf6-kparts-devel kf6-kservice-devel kf6-ktextwidgets-devel kf6-kwidgetsaddons-devel
BuildRequires: kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel
BuildRequires: kde6-libkeduvocdocument-devel

%description
Parley is a program to help you memorize things.

Parley supports many language specific features but can be used for other
learning tasks just as well. It uses the spaced repetition learning method,
also known as flash cards.

%prep
%setup -n %rname-%version

%build
%K6build \
%ifarch %qt6_qtwebengine_arches
    -DBUILD_BROWSERINTEGRATION:BOOL=ON \
%else
    -DBUILD_BROWSERINTEGRATION:BOOL=OFF \
%endif
    #

%install
%K6install
%K6install_move data parley knsrcfiles
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/parley
%_K6data/parley/
%_K6xdgapp/org.kde.parley.desktop
%_K6icon/*/*/apps/parley.*
%_K6icon/*/*/apps/parley-*.*
%_K6icon/oxygen/*/actions/*.*
%_K6cfg/documentsettings.kcfg
%_K6cfg/languagesettings.kcfg
%_K6cfg/parley.kcfg
%_K6data/knsrcfiles/*parley*.knsrc
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

* Mon Nov 11 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt2
- build on all arches

* Thu Nov 07 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

