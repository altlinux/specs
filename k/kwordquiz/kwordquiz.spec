%define rname kwordquiz

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Education
Summary: A general purpose flash card program
Url: http://www.kde.org
License: LGPL-2.0-or-later

Requires: kdeedu-data kf6-kirigami-addons
Provides:  kde5-kwordquiz = %EVR
Obsoletes: kde5-kwordquiz < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-multimedia-devel qt6-declarative-devel qt6-declarative-devel qt6-phonon-devel
BuildRequires: libvulkan-devel
BuildRequires: kf6-kirigami-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel
BuildRequires: kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdbusaddons-devel
BuildRequires: kf6-kdeclarative-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel  kf6-kguiaddons-devel kf6-ki18n-devel
BuildRequires: kf6-kiconthemes-devel  kf6-kio-devel kf6-kitemmodels-devel kf6-kitemviews-devel
BuildRequires: kf6-kjobwidgets-devel kf6-knewstuff-devel kf6-knotifications-devel kf6-knotifyconfig-devel
BuildRequires: kf6-kpackage-devel kf6-kparts-devel kf6-kservice-devel kf6-ktextwidgets-devel kf6-kunitconversion-devel
BuildRequires: kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel
BuildRequires: kf6-kirigami-addons-devel
BuildRequires: kde6-libkeduvocdocument-devel

%description
KWordQuiz is a general purpose flash card program. It can be used for
vocabulary learning and many other subjects. If you need more advanced
language learning features, please try KVocTrain.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data kwordquiz knsrcfiles
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6bin/kwordquiz
%_K6data/kwordquiz/
%_K6icon/*/*/apps/*kwordquiz*
%_K6icon/*/*/mimetypes/application-x-kwordquiz.*
%_K6xdgapp/org.kde.kwordquiz.desktop
%_K6cfg/kwordquiz.kcfg
%_K6data/knsrcfiles/*kwordquiz*.knsrc
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

