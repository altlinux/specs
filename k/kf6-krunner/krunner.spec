%define rname krunner

Name: kf6-%rname
Version: 6.2.0
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6 plasma runners
Url: http://www.kde.org
License: LGPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kdbusaddons-devel kf6-kglobalaccel-devel
BuildRequires: kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel kf6-kio-devel kf6-kitemviews-devel
BuildRequires: kf6-kjobwidgets-devel kf6-kpackage-devel kf6-kservice-devel kf6-ktextwidgets-devel
BuildRequires: kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel
BuildRequires: kf6-solid-devel kf6-sonnet-devel kf6-threadweaver-devel kf6-kitemmodels-devel

%description
The Plasma workspace provides an application called KRunner which, among other
things, allows one to type into a text area which causes various actions and
information that match the text appear as the text is being typed.

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

%package -n libkf6runner
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6runner
KF6 library


%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6install_move data kdevappwizard
%find_lang %name --all-name
%K6find_qtlang %name --all-name

%files common -f %name.lang
%doc README.md
%_datadir/qlogging-categories6/*.*categories

%files devel
%_K6inc/KRunner/
%_K6link/lib*.so
%_K6lib/cmake/KF6Runner
%_K6dbus_iface/*.xml
%_K6data/kdevappwizard/templates/*runner*

%files -n libkf6runner
%_K6lib/libKF6Runner.so.*


%changelog
* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

