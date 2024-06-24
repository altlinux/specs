%define rname baloo

%ifndef _unitdir_user
%define _unitdir_user %prefix/lib/systemd/user
%endif

Name: kf6-%rname
Version: 6.3.0
Release: alt1
%K6init no_altplace

Group: Graphical desktop/KDE
Summary: KDE Frameworks 6 framework for searching and managing metadata
Url: http://www.kde.org
License: GPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only

#Requires: polkit-kde-baloo

Source: %rname-%version.tar
Patch1: alt-disable-indexing.patch
Patch2: alt-paths.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: liblmdb-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel
BuildRequires: kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdbusaddons-devel
BuildRequires: kf6-kdoctools kf6-kdoctools-devel
BuildRequires: kf6-kfilemetadata-devel kf6-kglobalaccel-devel
BuildRequires: kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel kf6-kidletime-devel 
BuildRequires: kf6-kio-devel kf6-kitemmodels-devel kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-knotifications-devel
BuildRequires: kf6-kparts-devel kf6-kservice-devel kf6-ktextwidgets-devel kf6-kunitconversion-devel
BuildRequires: kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel

%description
%summary.

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
Requires: kf6-kfilemetadata-devel
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n polkit-kde-baloo
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: %name-common = %version-%release
%description -n polkit-kde-baloo
Common polkit files for %name

%package -n libkf6baloo
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6baloo
KF6 library

%package -n libkf6balooengine
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6balooengine
KF6 library


%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p1

%build
%K6build

%install
%K6install
%find_lang %name --all-name

%files common -f %name.lang
%doc LICENSES/* README.md
%_datadir/qlogging-categories6/*.*categories

%files
%_K6bin/baloo*
%_K6exec/baloo*
%_K6plug/kf6/kded/baloosearchmodule.so
%_K6plug/kf6/kio/*.so
%_K6qml/org/kde/baloo/
%_K6start/*baloo*.desktop
%_unitdir_user/*.service

#%files -n polkit-kde-baloo
#%_datadir/polkit-1/actions/*baloo*filewatch*.policy

%files devel
%_K6inc/Baloo/
%_K6link/lib*.so
%_K6lib/cmake/KF6Baloo
%_K6dbus_iface/*aloo*.xml
%_pkgconfigdir/*aloo*.pc

%files -n libkf6baloo
%_K6lib/libKF6Baloo.so.*
%files -n libkf6balooengine
%_K6lib/libKF6BalooEngine.so.*


%changelog
* Tue Jun 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

