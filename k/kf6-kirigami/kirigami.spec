%define rname kirigami

%define sover 6
%define libkirigami libkirigami%sover
%define libkirigamidelegates libkirigamidelegates%sover
%define libkirigamiplatform libkirigamiplatform%sover
%define libkirigamidialogs libkirigamidialogs%sover
%define libkirigamilayouts libkirigamilayouts%sover
%define libkirigamiprimitives libkirigamiprimitives%sover
%define libkirigamiprivate libkirigamiprivate%sover
%define libkirigamilayoutsprivate libkirigamilayoutsprivate%sover
%define libkirigamipolyfill libkirigamipolyfill%sover
%define libkirigamitemplates libkirigamitemplates%sover
%define libkirigamicontrols libkirigamicontrols%sover
%define libkirigamiforms libkirigamiforms%sover
%define libkirigamiformsprivatecards libkirigamiformsprivatecards%sover
%define libkirigamiformsprivateflat libkirigamiformsprivateflat%sover
%define libkirigamiformsprivatetemplates libkirigamiformsprivatetemplates%sover

Name: kf6-kirigami
Version: 6.27.0
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: A QtQuick based components set
Url: https://techbase.kde.org/Kirigami
License: LGPL-2.1-or-later

Requires: %name-common >= %EVR
Requires: qt6-declarative

Source0: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: libgomp-devel
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: qt6-svg-devel qt6-tools-devel qt6-shadertools-devel
#BuildRequires: kf6-kservice-devel kf6-kwindowsystem-devel
#BuildRequires: kf6-kpackage-devel
#BuildRequires: kf6-plasma-framework-devel

%description
Kirigami is a set of QtQuick components at the moment targeted for mobile use
(in the future desktop as well) targeting both Plasma Mobile and Android. It's
not a whole set of components, all the "Primitive" ones like buttons and
textboxes are a job for QtQuickControls (soon QtQuickControls2) but it's a set
of high level components to make the creation of applications that look and feel
great on mobile as well as desktop devices and follow the
https://community.kde.org/KDE_Visual_Design_Group/KirigamiHIG . The target of
those components is anybody that wants to do an application using QtQuick as its
main UI, especially if targeting a mobile platform, without adding many
dependencies. They work on a variety of platforms, such as Plasma Mobile,
Desktop Linux, Android and Windows. It will eventually become a Tier-1 KDE
Framework.

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
Requires: %name-common >= %EVR
Requires: libgomp-devel
%description devel
The %name-devel package contains libraries and header files for developing
applications that use %name

%package -n %libkirigami
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkirigami
%name library
%package -n %libkirigamidelegates
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkirigamidelegates
%name library

%package -n %libkirigamiplatform
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkirigamiplatform
%name library

%package -n %libkirigamidialogs
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkirigamidialogs
%name library

%package -n %libkirigamilayouts
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkirigamilayouts
%name library

%package -n %libkirigamiprimitives
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkirigamiprimitives
%name library

%package -n %libkirigamiprivate
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkirigamiprivate
%name library

%package -n %libkirigamilayoutsprivate
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkirigamilayoutsprivate
%name library

%package -n %libkirigamipolyfill
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkirigamipolyfill
%name library

%package -n %libkirigamitemplates
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkirigamitemplates
%name library

%package -n %libkirigamicontrols
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkirigamicontrols
%name library

%package -n %libkirigamiformsprivatetemplates
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkirigamiformsprivatetemplates
%name library

%package -n %libkirigamiforms
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkirigamiforms
%name library

%package -n %libkirigamiformsprivatecards
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkirigamiformsprivatecards
%name library

%package -n %libkirigamiformsprivateflat
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libkirigamiformsprivateflat
%name library

%prep
%setup -n %rname-%version
%ifarch %e2k
# same problem as with MSVC
sed -i "s/_MSC_VER/__e2k__/" src/imagecolors.cpp
%endif

%build
%K6build

%install
%K6install
%K6install_move data kdevappwizard
%find_lang %name --all-name
%K6find_qtlang %name --all-name

%files common -f %name.lang
%_datadir/qlogging-categories6/*.*categories

%files
%_K6qml/org/kde/kirigami/

%files devel
%_K6link/lib*.so
%_K6inc/Kirigami/
%_libdir/cmake/KF6Kirigami*/
%_K6data/kdevappwizard/templates/*kirigami*
%_K6archdata/metatypes/*.json

%files -n %libkirigami
%_K6lib/libKirigami.so.*
%_K6lib/libKirigami.so.%sover
%files -n %libkirigamicontrols
%_K6lib/libKirigamiControls.so.%sover
%_K6lib/libKirigamiControls.so.*
%files -n %libkirigamidelegates
%_K6lib/libKirigamiDelegates.so.%sover
%_K6lib/libKirigamiDelegates.so.*
%files -n %libkirigamiplatform
%_K6lib/libKirigamiPlatform.so.%sover
%_K6lib/libKirigamiPlatform.so.*
%files -n %libkirigamidialogs
%_K6lib/libKirigamiDialogs.so.%sover
%_K6lib/libKirigamiDialogs.so.*
%files -n %libkirigamilayouts
%_K6lib/libKirigamiLayouts.so.%sover
%_K6lib/libKirigamiLayouts.so.*
%files -n %libkirigamiprimitives
%_K6lib/libKirigamiPrimitives.so.%sover
%_K6lib/libKirigamiPrimitives.so.*
%files -n %libkirigamiprivate
%_K6lib/libKirigamiPrivate.so.%sover
%_K6lib/libKirigamiPrivate.so.*
%files -n %libkirigamilayoutsprivate
%_K6lib/libKirigamiLayoutsPrivate.so.%sover
%_K6lib/libKirigamiLayoutsPrivate.so.*
%files -n %libkirigamipolyfill
%_K6lib/libKirigamiPolyfill.so.%sover
%_K6lib/libKirigamiPolyfill.so.*
%files -n %libkirigamitemplates
%_K6lib/libKirigamiTemplates.so.%sover
%_K6lib/libKirigamiTemplates.so.*
%files -n %libkirigamiforms
%_K6lib/libKirigamiForms.so.%sover
%_K6lib/libKirigamiForms.so.*
%files -n %libkirigamiformsprivatecards
%_K6lib/libKirigamiFormsPrivateCards.so.%sover
%_K6lib/libKirigamiFormsPrivateCards.so.*
%files -n %libkirigamiformsprivateflat
%_K6lib/libKirigamiFormsPrivateFlat.so.%sover
%_K6lib/libKirigamiFormsPrivateFlat.so.*
%files -n %libkirigamiformsprivatetemplates
%_K6lib/libKirigamiFormsPrivateTemplates.so.%sover
%_K6lib/libKirigamiFormsPrivateTemplates.so.*

%changelog
* Tue Jun 16 2026 Sergey V Turchin <zerg@altlinux.org> 6.27.0-alt1
- new version

* Mon May 11 2026 Sergey V Turchin <zerg@altlinux.org> 6.26.0-alt1
- new version

* Mon Apr 13 2026 Sergey V Turchin <zerg@altlinux.org> 6.25.0-alt1
- new version

* Fri Mar 20 2026 Sergey V Turchin <zerg@altlinux.org> 6.24.0-alt1
- new version

* Tue Mar 03 2026 Sergey V Turchin <zerg@altlinux.org> 6.23.1-alt1
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

* Thu May 22 2025 Sergey V Turchin <zerg@altlinux.org> 6.14.1-alt1
- new version

* Wed May 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.14.0-alt1
- new version

* Mon Apr 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.13.0-alt1
- new version

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

* Wed Oct 16 2024 Sergey V Turchin <zerg@altlinux.org> 6.7.0-alt3
- fix requires

* Wed Oct 16 2024 Sergey V Turchin <zerg@altlinux.org> 6.7.0-alt2
- fix requires

* Fri Oct 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.7.0-alt1
- new version

* Fri Oct 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.6.0-alt1
- new version

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

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 5.115.0-alt1
- initial build
