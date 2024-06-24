%define rname knewstuff

Name: kf6-%rname
Version: 6.3.0
Release: alt1
%K6init no_altplace

Group: System/Libraries
Summary: KDE Frameworks 6 downloading and sharing additional application data
Url: http://www.kde.org
License: LGPL-2.0-or-later

Requires: kf6-kirigami

Source: %rname-%version.tar
Patch1: alt-check-ghns-auth.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules gcc-c++ qt6-base-devel qt6-declarative-devel qt6-tools-devel
BuildRequires: kf6-attica-devel kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel
BuildRequires: kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel kf6-kdbusaddons-devel kf6-kglobalaccel-devel kf6-kguiaddons-devel
BuildRequires: kf6-ki18n-devel kf6-kiconthemes-devel kf6-kio-devel kf6-kitemviews-devel
BuildRequires: kf6-kjobwidgets-devel kf6-kservice-devel kf6-ktextwidgets-devel kf6-kwidgetsaddons-devel
BuildRequires: kf6-kwindowsystem-devel kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel
BuildRequires: kf6-kpackage-devel kf6-syndication-devel kf6-kirigami-devel

%description
The KNewStuff library implements collaborative data sharing for
applications. It uses libattica to support the Open Collaboration Services
specification.

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

%package -n libkf6newstuff
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6newstuff
KF6 library

%package -n libkf6newstuffcore
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6newstuffcore
KF6 library

%package -n libkf6newstuffwidgets
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6newstuffwidgets
KF6 library


%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K6build

%install
%K6install
%find_lang %name --all-name
%K6find_qtlang %name --all-name

%files common -f %name.lang
%doc LICENSES/* README.md
%_datadir/qlogging-categories6/*.*categories
#%_kf6_data/kmoretools/

%files
%_K6bin/knewstuff*
%_K6xdgapp/*knewstuff*.desktop
%_K6qml/org/kde/newstuff/

%files devel
%_K6plug/designer/*newstuff*.so
%_K6inc/KNewStuff*/
%_K6link/lib*.so
%_K6lib/cmake/*NewStuff*/

%files -n libkf6newstuffcore
%_K6lib/libKF6NewStuffCore.so.*

%files -n libkf6newstuffwidgets
%_K6lib/libKF6NewStuffWidgets.so.*


%changelog
* Tue Jun 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

