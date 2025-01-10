%define rname plasma5support

%define sover 6
%define libplasma5support libplasma5support%sover

Name: plasma6-%rname
Version: 6.2.5
Release: alt1
%K6init

Group: Graphical desktop/KDE
Summary: Migration aids for KF5 -> KF6 migration
Url: http://www.kde.org
License: LGPL-2.0-or-later

Source: %rname-%version.tar
Patch1: alt-freespace-thread-timer.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: libvulkan-devel
BuildRequires: extra-cmake-modules qt6-declarative-devel
BuildRequires: kf6-kconfig-devel kf6-kcoreaddons-devel kf6-kguiaddons-devel kf6-ki18n-devel
BuildRequires: kf6-knotifications-devel kf6-solid-devel kf6-kio-devel
BuildRequires: plasma6-libksysguard-devel

%description
%summary.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
#Conflicts: plasma5-workspace-common < 1:5
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
#Conflicts: plasma5-workspace-devel
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libplasma5support
Group: System/Libraries
Summary: KF6 library
Requires: %name-common >= %EVR
%description -n %libplasma5support
KF6 library


%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K6build \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    #

%install
%K6install
%find_lang %name --all-name

%files common -f %name.lang
%doc LICENSES/*
%_datadir/qlogging-categories6/*.*categories

%files
%_K6plug/plasma5support/
%_K6qml/org/kde/plasma/plasma5support/
%_K6data/plasma5support/

%files devel
%_K6inc/Plasma5Support/
%_K6link/lib*.so
%_K6lib/cmake/Plasma5Support/

%files -n %libplasma5support
%_K6lib/libPlasma5Support.so.*
%_K6lib/libPlasma5Support.so.%sover


%changelog
* Thu Jan 09 2025 Sergey V Turchin <zerg@altlinux.org> 6.2.5-alt1
- new version

* Tue Nov 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt1
- new version

* Wed Nov 06 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.3-alt1
- new version

* Mon Oct 28 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.2-alt1
- new version

* Tue Sep 10 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.5-alt1
- new version

* Thu Aug 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.4-alt1
- new version

* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jul 03 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- initial build

