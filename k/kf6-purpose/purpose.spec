%define rname purpose

%def_enable bootstrap

%define sover 6
%define libphabricatorhelpers libphabricatorhelpers%sover
%define libreviewboardhelpers libreviewboardhelpers%sover

Name: kf6-%rname
Version: 6.2.0
Release: alt1
%K6init no_altplace

Group: Graphical desktop/KDE
Summary: Abstraction to provide and leverage actions of a specific kind
Url: http://www.kde.org
License: LGPL-2.1-or-later

Requires: kf6-kirigami
%if_disabled bootstrap
#Requires: connect
%endif

Source: %rname-%version.tar
Patch1: alt-i18n.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-base-devel qt6-declarative-devel
#BuildRequires: connect
%if_disabled bootstrap
BuildRequires: kaccounts-integration-devel
BuildRequires: accounts-qt6-devel signon-devel
%endif
BuildRequires: intltool
BuildRequires: kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel kf6-kdeclarative-devel kf6-ki18n-devel kf6-kio-devel kf6-kitemviews-devel kf6-kjobwidgets-devel
BuildRequires: kf6-kpackage-devel kf6-kservice-devel kf6-kwidgetsaddons-devel kf6-kxmlgui-devel kf6-solid-devel
BuildRequires: kf6-knotifications-devel kf6-kirigami-devel kf6-kwindowsystem-devel

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
%patch1 -p1

%if_enabled bootstrap
sed -i 's|KAccounts|KAccounts_BUILD_DEPS_LOOP_WITH_APPS|' CMakeLists.txt
%endif

%build
%K6build

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
%if_disabled bootstrap
%_K6icon/*/*/actions/kipiplugin_youtube.*
%endif
%_kf6_data/purpose/
%_K6icon/*/*/apps/*purpose*.*
%_datadir/accounts/services/kde/

%files devel
%if_disabled bootstrap
%_K6lib/cmake/KDEExperimentalPurpose/
%endif
%_K6inc/Purpose/
%_K6inc/PurposeWidgets/
%_K6link/lib*.so
%_K6lib/cmake/KF6Purpose/

%if_disabled bootstrap
%files -n %libphabricatorhelpers
%_K6lib/libPhabricatorHelpers.so.*
%_K6lib/libPhabricatorHelpers.so.%sover
%files -n %libreviewboardhelpers
%_K6lib/libReviewboardHelpers.so.*
%_K6lib/libReviewboardHelpers.so.%sover
%endif
%files -n libkf6purpose
%_K6lib/libKF6Purpose.so.*
%files -n libkf6purposewidgets
%_K6lib/libKF6PurposeWidgets.so.*


%changelog
* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

