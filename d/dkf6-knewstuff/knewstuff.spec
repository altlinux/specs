%define rname knewstuff

Name: dkf6-%rname
Version: 6.28.0
Release: alt0.dde.1
%DK6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6 downloading and sharing additional application data
Url: http://www.kde.org
License: LGPL-2.0-or-later

Requires: dkf6-kirigami

Source: %name-%version.tar
Patch1: alt-check-ghns-auth.patch
Patch2: alt-warning.patch

# prevent hasher-privd limits
BuildRequires(pre): rpm-build-dkf6
BuildRequires: deepin-extra-cmake-modules dqt6-declarative-devel dqt6-tools-devel
BuildRequires: vulkan-headers libdqt6-quickwidgets libdqt6-qmlcompiler
BuildRequires: dkf6-attica-devel dkf6-karchive-devel dkf6-kauth-devel dkf6-kbookmarks-devel
BuildRequires: dkf6-kcodecs-devel dkf6-kcompletion-devel dkf6-kconfig-devel dkf6-kconfigwidgets-devel
BuildRequires: dkf6-kcoreaddons-devel dkf6-kdbusaddons-devel dkf6-kglobalaccel-devel dkf6-kguiaddons-devel
# BuildRequires: dkf6-kiconthemes-devel dkf6-kio-devel dkf6-kitemviews-devel
BuildRequires: dkf6-ki18n-devel
# BuildRequires: dkf6-kjobwidgets-devel dkf6-kservice-devel dkf6-ktextwidgets-devel dkf6-kwidgetsaddons-devel
# BuildRequires: dkf6-kwindowsystem-devel dkf6-kxmlgui-devel dkf6-solid-devel dkf6-sonnet-devel
BuildRequires: dkf6-kpackage-devel dkf6-syndication-devel dkf6-kirigami-devel

# find libraries
%add_findprov_lib_path %_DK6lib

%description
The KNewStuff library implements collaborative data sharing for
applications. It uses libattica to support the Open Collaboration Services
specification.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
# Requires: kde-common
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libdkf6newstuff
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n libdkf6newstuff
KF6 library

%package -n libdkf6newstuffcore
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n libdkf6newstuffcore
KF6 library

%package -n libdkf6newstuffwidgets
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n libdkf6newstuffwidgets
KF6 library


%prep
%setup -n %name-%version
%patch1 -p1
%patch2 -p1

%build
%DK6build

%install
%DK6install
%find_lang %name --all-name
%DK6find_qtlang %name --all-name

%files common -f %name.lang
%doc LICENSES/* README.md
%_DK6data/qlogging-categories6/*.*categories
#%_dkf6_data/kmoretools/

%files
%exclude %_bindir/knewstuff*
%_DK6bin/knewstuff*
%_DK6xdgapp/*knewstuff*.desktop

%files devel
%_DK6plug/designer/*newstuff*.so
%_DK6inc/KNewStuff*/
%_DK6link/lib*.so
%_DK6lib/cmake/*NewStuff*/

%files -n libdkf6newstuffcore
%_DK6lib/libKF6NewStuffCore.so.*

%files -n libdkf6newstuffwidgets
%_DK6lib/libKF6NewStuffWidgets.so.*
%_DK6qml/org/kde/newstuff/


%changelog
* Wed Oct 07 2026 Leontiy Volodin <lvol@altlinux.org> 6.28.0-alt0.dde.1
- fork for independent deepin buildings

* Tue Jul 14 2026 Sergey V Turchin <zerg@altlinux.org> 6.28.0-alt1
- new version

* Tue Jun 16 2026 Sergey V Turchin <zerg@altlinux.org> 6.27.0-alt1
- new version

* Mon May 11 2026 Sergey V Turchin <zerg@altlinux.org> 6.26.0-alt1
- new version

* Mon Apr 13 2026 Sergey V Turchin <zerg@altlinux.org> 6.25.0-alt1
- new version

* Fri Mar 20 2026 Sergey V Turchin <zerg@altlinux.org> 6.24.0-alt1
- new version

* Mon Feb 16 2026 Sergey V Turchin <zerg@altlinux.org> 6.23.0-alt1
- new version

* Wed Jan 14 2026 Sergey V Turchin <zerg@altlinux.org> 6.22.0-alt1
- new version

* Mon Dec 22 2025 Sergey V Turchin <zerg@altlinux.org> 6.21.0-alt1
- new version

* Thu Nov 20 2025 Sergey V Turchin <zerg@altlinux.org> 6.20.0-alt1
- new version

* Fri Oct 17 2025 Sergey V Turchin <zerg@altlinux.org> 6.19.0-alt1
- new version

* Mon Sep 15 2025 Sergey V Turchin <zerg@altlinux.org> 6.18.0-alt1
- new version

* Mon Aug 25 2025 Sergey V Turchin <zerg@altlinux.org> 6.17.0-alt1
- new version

* Mon Aug 04 2025 Sergey V Turchin <zerg@altlinux.org> 6.16.0-alt1
- new version

* Mon Jul 07 2025 Sergey V Turchin <zerg@altlinux.org> 6.15.0-alt1
- new version

* Wed May 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.14.0-alt1
- new version

* Mon Apr 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.13.0-alt1
- new version

* Fri Mar 28 2025 Sergey V Turchin <zerg@altlinux.org> 6.12.0-alt2
- more serious warning about downloadable content

* Mon Mar 17 2025 Sergey V Turchin <zerg@altlinux.org> 6.12.0-alt1
- new version

* Fri Feb 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.11.0-alt1
- new version

* Mon Jan 13 2025 Sergey V Turchin <zerg@altlinux.org> 6.10.0-alt1
- new version

* Mon Dec 16 2024 Sergey V Turchin <zerg@altlinux.org> 6.9.0-alt1
- new version

* Mon Nov 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.8.0-alt1
- new version

* Fri Oct 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.7.0-alt1
- new version

* Fri Oct 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.6.0-alt1
- new version

* Wed Sep 04 2024 Sergey V Turchin <zerg@altlinux.org> 6.5.0-alt1
- new version

* Tue Aug 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.4.0-alt1
- new version

* Thu Jul 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt2
- move qml into library packge

* Tue Jun 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

