%define rname libksane

%define sover 6
%define libksanewidgets libksanewidgets6_%sover

Name: kde6-%rname
Version: 24.08.1
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: SANE Library interface
Url: http://www.kde.org
License: LGPL-2.1-only OR LGPL-3.0-only

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: ksanecore-devel
BuildRequires: kf6-kconfig-devel kf6-ki18n-devel kf6-ktextwidgets-devel kf6-kwallet-devel
BuildRequires: kf6-kwidgetsaddons-devel kf6-sonnet-devel

%description
Libksane is a KDE interface for SANE library to control flat scanners.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Provides: kde5-libksane-common = %EVR
Obsoletes: kde5-libksane-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: ksanecore-devel
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libksanewidgets
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libksanewidgets
%name library


%prep
%setup -n %rname-%version

find -type f -name \*.h -or -name \*.cpp | \
while read f ; do
    sed -i '/^#include/s|<KSaneCore/|<KSaneCore6/|' $f
done

%build
%add_optflags -I%_K6inc
%K6build \
    -DBUILD_WITH_QT6:BOOL=ON \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    #

%install
%K6install
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*
%_K6icon/hicolor/*/actions/*.*

%files devel
%_K6inc/KSane*/
%_K6link/lib*.so
%_K6lib/cmake/KSane*/

%files -n %libksanewidgets
%_K6lib/libKSaneWidgets6.so.*


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- initial build

