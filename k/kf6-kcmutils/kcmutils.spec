%define rname kcmutils

Name: kf6-%rname
Version: 6.4.0
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6 classes to work with KCModules
Url: http://www.kde.org
License: LGPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6 rpm-build-ubt
BuildRequires: extra-cmake-modules gcc-c++ qt6-base-devel qt6-declarative-devel
BuildRequires: kf6-kauth-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kdbusaddons-devel
BuildRequires: kf6-kglobalaccel-devel kf6-kguiaddons-devel kf6-ki18n-devel
BuildRequires: kf6-kiconthemes-devel kf6-kitemviews-devel kf6-kservice-devel
BuildRequires: kf6-ktextwidgets-devel kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel
BuildRequires: kf6-kxmlgui-devel kf6-sonnet-devel kf6-attica-devel
BuildRequires: kf6-kpackage-devel kf6-kio-devel

%description
KCMUtils provides various classes to work with KCModules. KCModules can be
created with the KConfigWidgets framework.

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

%package -n libkf6kcmutils
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n libkf6kcmutils
KF6 library

%package -n libkf6kcmutilsquick
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n libkf6kcmutilsquick
KF6 library

%package -n libkf6kcmutilscore
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n libkf6kcmutilscore
KF6 library

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %name --all-name
%K6find_qtlang %name --all-name

%files common -f %name.lang
%doc LICENSES/* README.md
%_datadir/qlogging-categories6/*.*categories

%files devel
%_K6exec/kcmdesktopfilegenerator
%_K6inc/KCMUtils*/
%_K6link/lib*.so
%_K6lib/cmake/KF6KCMUtils

%files -n libkf6kcmutils
%_bindir/*kcm*
%_K6bin/*kcm*
%_K6lib/libKF6KCMUtils.so.*
%files -n libkf6kcmutilsquick
%_K6lib/libKF6KCMUtilsQuick.so.*
%_K6qml/org/kde/kcmutils/
%files -n libkf6kcmutilscore
%_K6lib/libKF6KCMUtilsCore.so.*


%changelog
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

