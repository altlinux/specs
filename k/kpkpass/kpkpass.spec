%define rname kpkpass

%define sover 6
%define libkpimpkpass libkpimpkpass%sover

Name: %rname
Version: 26.04.1
Release: alt2
%K6init

Group: Graphical desktop/KDE
Summary: Apple Wallet pass files library
Url: http://www.kde.org
License: LGPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
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
#%_K6xdgmime/*pkpass*.xml

%files devel
%_K6inc/KPim6/KPkPass/
%_K6link/lib*.so
%_K6lib/cmake/KPim*PkPass/

%files -n %libkpimpkpass
%_K6lib/libKPim6PkPass.so.%sover
%_K6lib/libKPim6PkPass.so.*
%_K6qml/org/kde/pkpass/

%changelog
* Mon Jul 06 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.1-alt2
- don't package mime data

* Fri May 08 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.1-alt1
- new version

* Thu Mar 05 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.3-alt1
- new version

* Fri Feb 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.2-alt1
- new version

* Fri Jan 16 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.1-alt1
- new version

* Tue Nov 18 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.3-alt1
- new version

* Fri Oct 10 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.2-alt1
- new version

* Tue Sep 16 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.1-alt1
- new version

* Thu Jul 24 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.3-alt1
- new version

* Fri Jun 06 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.2-alt1
- new version

* Mon May 12 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.1-alt1
- new version

* Thu Apr 17 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.0-alt1
- new version

* Fri Mar 07 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.3-alt1
- new version

* Wed Feb 12 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.2-alt1
- new version

* Thu Jan 09 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.1-alt1
- new version

* Thu Nov 14 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt1
- new version

* Fri Oct 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- new version

* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- new version

* Mon Sep 09 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.0-alt1
- new version

* Wed Aug 21 2024 Sergey V Turchin <zerg@altlinux.org> 24.05.2-alt1
- initial build

