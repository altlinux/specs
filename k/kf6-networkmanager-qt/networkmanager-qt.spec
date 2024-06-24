%define rname networkmanager-qt

Name: kf6-%rname
Version: 6.3.0
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6 Qt wrapper for NetworkManager DBus API
Url: http://www.kde.org
License: LGPL-2.1-only OR LGPL-3.0-only

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-base-devel qt6-declarative-devel
BuildRequires: libnm-devel

%description
NetworkManagerQt provides access to all NetworkManager features
exposed on DBus. It allows you to manage your connections and control
your network devices and also provides a library for parsing connection
settings which are used in DBus communication.

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
Requires: libnm-devel
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf6networkmanagerqt
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6networkmanagerqt
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
%_K6inc/NetworkManagerQt/
%_K6link/lib*.so
%_K6lib/cmake/KF6NetworkManagerQt

%files -n libkf6networkmanagerqt
%_K6lib/libKF6NetworkManagerQt.so.*
%_K6qml/org/kde/networkmanager/

%changelog
* Tue Jun 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

