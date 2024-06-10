%define rname kdav

%define sover 6
%define libkpimkdav libkpimkdav%sover

Name: kf6-%rname
Version: 6.2.0
Release: alt1
%K6init altplace

Group: Graphical desktop/KDE
Summary: DAV protocol implemention
Url: http://www.kde.org
License: LGPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: kf6-kconfig-devel kf6-kio-devel kf6-ki18n-devel

%description
DAV protocol implemention with KJobs.

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

%package -n libkf6dav
Group: System/Libraries
Summary: %name library
Requires: %name-common
%description -n libkf6dav
%name library


%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/* README.md
%_datadir/qlogging-categories6/*.*categories

%files devel
#%_K6inc/kdav_version.h
%_K6inc/KDAV/
%_K6link/lib*.so
%_K6lib/cmake/KF6DAV/

%files -n libkf6dav
%_K6lib/libKF6DAV.so.%sover
%_K6lib/libKF6DAV.so.*


%changelog
* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

