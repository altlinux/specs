%define rname knotifyconfig

Name: kf6-%rname
Version: 6.5.0
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6 configuration dialog for desktop notifications
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules
BuildRequires: qt6-declarative-devel
BuildRequires: qt6-phonon-devel qt6-speech-devel
#BuildRequires: libcanberra-devel # not good
BuildRequires: kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kdbusaddons-devel kf6-kglobalaccel-devel
BuildRequires: kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel kf6-kio-devel kf6-kitemviews-devel
BuildRequires: kf6-kjobwidgets-devel kf6-kservice-devel kf6-ktextwidgets-devel kf6-kwidgetsaddons-devel
BuildRequires: kf6-kwindowsystem-devel kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel

%description
KNotifyConfig provides a configuration dialog for desktop notifications which
can be embedded in your application.

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

%package -n libkf6notifyconfig
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6notifyconfig
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
#%_K6inc/knotifyconfig_version.h
%_K6inc/KNotifyConfig/
%_K6link/lib*.so
%_K6lib/cmake/KF6NotifyConfig

%files -n libkf6notifyconfig
%_K6lib/libKF6NotifyConfig.so.*


%changelog
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

