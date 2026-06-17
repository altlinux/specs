%define rname purpose

%def_disable bootstrap

%define sover 6
%define libphabricatorhelpers libphabricatorhelpers%sover
%define libreviewboardhelpers libreviewboardhelpers%sover

Name: kf6-%rname
Version: 6.27.0
Release: alt1
%K6init no_altplace

Group: Graphical desktop/KDE
Summary: Abstraction to provide and leverage actions of a specific kind
Url: http://www.kde.org
License: LGPL-2.1-or-later

Requires: libkf6prison libkf6itemmodels kf6-kirigami kf6-kdeclarative
%if_disabled bootstrap
#Requires: connect
%endif

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-tools-devel qt6-declarative-devel
#BuildRequires: connect
%if_disabled bootstrap
BuildRequires: kaccounts-integration-devel
BuildRequires: accounts-qt6-devel signon-devel
%endif
BuildRequires: intltool
BuildRequires: libkf6prison libkf6itemmodels
BuildRequires: kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel kf6-kdeclarative-devel kf6-ki18n-devel kf6-kio-devel kf6-kitemviews-devel kf6-kjobwidgets-devel
BuildRequires: kf6-kpackage-devel kf6-kservice-devel kf6-kwidgetsaddons-devel kf6-kxmlgui-devel kf6-solid-devel
BuildRequires: kf6-knotifications-devel kf6-kwindowsystem-devel
BuildRequires: libgomp-devel kf6-kirigami-devel

%description
Purpose offers the possibility to create integrate services and actions on
any application without having to implement them specifically. Purpose will
offer them mechanisms to list the different alternatives to execute given the
requested action type and will facilitate components so that all the plugins
can receive all the information they need.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf6purposewidgets
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n libkf6purposewidgets
KF6 library

%package -n libkf6purpose
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n libkf6purpose
KF6 library

%package -n %libphabricatorhelpers
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n %libphabricatorhelpers
KF6 library

%package -n %libreviewboardhelpers
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n %libreviewboardhelpers
KF6 library

%prep
%setup -n %rname-%version

%if_enabled bootstrap
sed -i 's|KAccounts|KAccounts_BUILD_DEPS_LOOP_WITH_APPS|' CMakeLists.txt
%endif

%build
%K6build -DBUILD_TESTING:BOOL=TRUE

%install
%K6install
#K6install_move data purpose kpackage locale

mkdir -p %buildroot/%_datadir/accounts/services/kde/

%find_lang %name --all-name
%K6find_qtlang %name --append --all-name

%files common -f %name.lang
%doc LICENSES/* README.md
%_datadir/qlogging-categories6/*.*categories

%files
%_K6exec/purpose*
%_K6plug/kf6/purpose/
%_K6plug/kf6/kfileitemaction/*.so
%_K6qml/org/kde/purpose/
%_kf6_data/purpose/
%_K6icon/*/*/apps/*purpose*.*
%_datadir/accounts/services/kde/

%files devel
%_K6inc/Purpose/
%_K6inc/PurposeWidgets/
%_K6link/lib*.so
%_K6lib/cmake/KF6Purpose/

%files -n libkf6purpose
%_K6lib/libKF6Purpose.so.*
%files -n libkf6purposewidgets
%_K6lib/libKF6PurposeWidgets.so.*


%changelog
* Tue Jun 16 2026 Sergey V Turchin <zerg@altlinux.org> 6.27.0-alt1
- new version

* Mon May 11 2026 Sergey V Turchin <zerg@altlinux.org> 6.26.0-alt1
- new version

* Mon Apr 13 2026 Sergey V Turchin <zerg@altlinux.org> 6.25.0-alt1
- new version

* Fri Mar 20 2026 Sergey V Turchin <zerg@altlinux.org> 6.24.0-alt1
- new version

* Mon Feb 16 2026 Sergey V Turchin <zerg@altlinux.org> 6.23.0-alt1
- new version

* Wed Jan 14 2026 Sergey V Turchin <zerg@altlinux.org> 6.22.0-alt1
- new version

* Mon Dec 22 2025 Sergey V Turchin <zerg@altlinux.org> 6.21.0-alt1
- new version

* Thu Nov 20 2025 Sergey V Turchin <zerg@altlinux.org> 6.20.0-alt1
- new version

* Fri Oct 17 2025 Sergey V Turchin <zerg@altlinux.org> 6.19.0-alt1
- new version

* Mon Sep 15 2025 Sergey V Turchin <zerg@altlinux.org> 6.18.0-alt1
- new version

* Mon Aug 25 2025 Sergey V Turchin <zerg@altlinux.org> 6.17.0-alt1
- new version

* Mon Aug 04 2025 Sergey V Turchin <zerg@altlinux.org> 6.16.0-alt1
- new version

* Mon Jul 07 2025 Sergey V Turchin <zerg@altlinux.org> 6.15.0-alt1
- new version

* Wed May 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.14.0-alt1
- new version

* Mon Apr 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.13.0-alt1
- new version

* Mon Mar 17 2025 Sergey V Turchin <zerg@altlinux.org> 6.12.0-alt1
- new version

* Fri Feb 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.11.0-alt1
- new version

* Mon Jan 13 2025 Sergey V Turchin <zerg@altlinux.org> 6.10.0-alt1
- new version

* Mon Dec 16 2024 Sergey V Turchin <zerg@altlinux.org> 6.9.0-alt1
- new version

* Fri Dec 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.8.0-alt2
- build with kaccounts-integration

* Mon Nov 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.8.0-alt1
- new version

* Fri Oct 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.7.0-alt1
- new version

* Fri Oct 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.6.0-alt1
- new version

* Wed Sep 04 2024 Sergey V Turchin <zerg@altlinux.org> 6.5.0-alt1
- new version

* Tue Aug 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.4.0-alt1
- new version

* Tue Jun 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

