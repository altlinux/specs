%define rname kirigami

%define sover 6
%define libkirigami libkirigami%sover
%define libkirigamidelegates libkirigamidelegates%sover
%define libkirigamiplatform libkirigamiplatform%sover
%define libkirigamidialogs libkirigamidialogs%sover
%define libkirigamilayouts libkirigamilayouts%sover
%define libkirigamiprimitives libkirigamiprimitives%sover
%define libkirigamiprivate libkirigamiprivate%sover

Name: kf6-kirigami
Version: 6.5.0
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: A QtQuick based components set
Url: https://techbase.kde.org/Kirigami
License: LGPL-2.1-or-later

Requires: %name-common
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
Requires: %name-common
%description devel
The %name-devel package contains libraries and header files for developing
applications that use %name

%package -n %libkirigami
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n %libkirigami
KF6 library
%package -n %libkirigamidelegates
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n %libkirigamidelegates
KF6 library

%package -n %libkirigamiplatform
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n %libkirigamiplatform
KF6 library

%package -n %libkirigamidialogs
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n %libkirigamidialogs
KF6 library

%package -n %libkirigamilayouts
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n %libkirigamilayouts
KF6 library

%package -n %libkirigamiprimitives
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n %libkirigamiprimitives
KF6 library

%package -n %libkirigamiprivate
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n %libkirigamiprivate
KF6 library

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

%files -n %libkirigami
%_K6lib/libKirigami.so.*
%_K6lib/libKirigami.so.%sover
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

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 5.115.0-alt1
- initial build
