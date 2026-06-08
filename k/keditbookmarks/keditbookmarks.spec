%define rname keditbookmarks

%define kbookmarkmodel_private_sover 6
%define libkbookmarkmodel_private libkbookmarkmodel_private%kbookmarkmodel_private_sover

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Utility to edit KDE bookmarks
Url: http://www.kde.org
License: LGPL-2.0-or-later

Provides: kde5-keditbookmarks = %EVR
Obsoletes: kde5-keditbookmarks < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: kf6-kdoctools-devel kf6-kiconthemes-devel kf6-kio-devel
BuildRequires: kf6-kparts-devel kf6-ktextwidgets-devel kf6-kwindowsystem-devel
BuildRequires: kf6-kconfigwidgets-devel

%description
Utility to edit KDE bookmarks.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Provides: kde5-keditbookmarks-common = %EVR
Obsoletes: kde5-keditbookmarks-common < %EVR
%description common
%name common package

%package -n %libkbookmarkmodel_private
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkbookmarkmodel_private
%name library.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc COPYING*
%_datadir/qlogging-categories6/*.*categories

%files
%_K6bin/kbookmarkmerger
%_K6bin/keditbookmarks
%_K6xdgapp/org.kde.keditbookmarks.desktop
%_K6cfg/keditbookmarks.kcfg

%files -n %libkbookmarkmodel_private
%_K6lib/libkbookmarkmodel_private.so.%kbookmarkmodel_private_sover
%_K6lib/libkbookmarkmodel_private.so.*


%changelog
* Fri Jun 05 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.2-alt1
- new version

* Sun May 10 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.1-alt1
- new version

* Fri Mar 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.3-alt1
- new version

* Fri Feb 06 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.2-alt1
- new version

* Mon Jan 19 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.1-alt1
- new version

* Wed Nov 19 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.3-alt1
- new version

* Mon Oct 13 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.2-alt1
- new version

* Tue Sep 23 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.1-alt1
- new version

* Fri Jul 25 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.3-alt1
- new version

* Wed Jun 11 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.2-alt1
- new version

* Wed May 14 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.1-alt1
- new version

* Tue Mar 11 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.3-alt1
- new version

* Thu Mar 06 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.2-alt1
- new version

* Wed Jan 29 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.1-alt1
- new version

* Mon Nov 18 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.3-alt1
- new version

* Thu Oct 17 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

