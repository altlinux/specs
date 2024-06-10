%define rname kservice

Name: kf6-%rname
Version: 6.2.0
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6 plugin framework for desktop services
Url: http://www.kde.org
License: LGPL-2.0-or-later

Source: %rname-%version.tar
Patch1: alt-skip-antikde-mimeapps-list.patch

BuildRequires(pre): rpm-build-kf6 rpm-build-ubt
BuildRequires: extra-cmake-modules qt6-base-devel qt6-declarative-devel
BuildRequires: docbook-style-xsl flex bison
BuildRequires: kf6-karchive-devel kf6-kconfig-devel kf6-kcoreaddons-devel kf6-kcrash-devel
BuildRequires: kf6-kdbusaddons-devel kf6-kdoctools kf6-kdoctools-devel
BuildRequires: kf6-ki18n-devel kf6-kwindowsystem-devel

%description
KService provides a plugin framework for handling desktop services. Services can
be applications or libraries. They can be bound to MIME types or handled by
application specific code.

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
Requires: kf6-kconfig-devel
Requires: kf6-kcoreaddons-devel
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf6service
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
Requires: altlinux-freedesktop-menu-generic
%description -n libkf6service
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

%files devel
%_K6inc/KService/
%_K6link/lib*.so
%_K6lib/cmake/KF6Service

%files -n libkf6service
%_bindir/kbuildsycoca6
%_K6bin/kbuildsycoca6
%_K6lib/libKF6Service.so.*
#%_K6srvtyp/*.desktop


%changelog
* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

