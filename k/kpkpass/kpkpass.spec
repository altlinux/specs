%define rname kpkpass

%define sover 6
%define libkpimpkpass libkpimpkpass%sover

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Apple Wallet pass files library
Url: http://www.kde.org
License: LGPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6 rpm-build-ubt
BuildRequires: extra-cmake-modules qt6-base-devel
BuildRequires: shared-mime-info
BuildRequires: kf6-karchive-devel

%description
Library to deal with Apple Wallet pass files.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf6-filesystem
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkpimpkpass
Group: System/Libraries
Summary: %name library
Requires: %name-common
Provides: libkpimpkpass = %EVR
Obsoletes: libkpimpkpass < %EVR
%description -n %libkpimpkpass
%name library


%prep
%setup -n %rname-%version

%build
%K6build \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    #

%install
%K6install
#mv %buildroot/%_K6xdgmime/application-vnd-apple-pkpass.xml \
#    %buildroot/%_K6xdgmime/application-vnd-apple-pkpass.xml
%find_lang %name --all-name

%files common -f %name.lang
%doc LICENSES/* README.md
%_datadir/qlogging-categories6/*.*categories
#%_K6xdgmime/*.xml

%files devel
%_K6inc/KPim6/KPkPass/
%_K6link/lib*.so
%_K6lib/cmake/KPim*PkPass/

%files -n %libkpimpkpass
%_K6lib/libKPim6PkPass.so.%sover
%_K6lib/libKPim6PkPass.so.*


%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build

