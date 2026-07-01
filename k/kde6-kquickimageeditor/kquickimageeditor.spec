%define rname kquickimageeditor

%define sover 1
%define libkquickimageeditor libkquickimageeditor%sover

Name: kde6-%rname
Version: 0.6.2
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: KQuickImageEditor QtQuick components
Url: https://invent.kde.org/libraries/kquickimageeditor
License: GPL-2.0-or-later

Requires: kf6-kirigami

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-base-devel qt6-declarative-devel
BuildRequires: kf6-kconfig-devel

%description
KQuickImageEditor is a set of QtQuick components providing basic image editing capabilities.

%package common
BuildArch: noarch
Summary: Common %name files
Group: System/Configuration/Other
Provides:  kde5-kquickimageeditor-common = %EVR
Obsoletes: kde5-kquickimageeditor-common < %EVR
%description common
Common %name files

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
Conflicts: kde5-kquickimageeditor-devel
%description devel
This package contains the development files for %name.

%package -n %libkquickimageeditor
Group: System/Libraries
Summary: %name library
#Requires: %name-common >= %EVR
Provides: %name = %EVR
Obsoletes: %name < %EVR
%description -n %libkquickimageeditor
%name library

%prep
%setup -n %rname-%version

%build
%K6build \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    #

%install
%K6install
%find_lang --with-kde --all-name %name

%files -n %libkquickimageeditor -f %name.lang
%doc LICENSES/*
%_K6lib/libKQuickImageEditor.so.%sover
%_K6lib/libKQuickImageEditor.so.*
%_K6qml/org/kde/kquickimageeditor/

%files devel
%_K6inc/??uick?mage?ditor/
%_K6link/lib*.so
%_K6lib/cmake/KQuickImageEditor/
%_K6archdata/mkspecs/modules/*KQuickImageEditor*.pri

%changelog
* Wed Jul 01 2026 Sergey V Turchin <zerg@altlinux.org> 0.6.2-alt1
- new version

* Wed Mar 18 2026 Sergey V Turchin <zerg@altlinux.org> 0.6.1-alt1
- new version

* Tue Jan 20 2026 Sergey V Turchin <zerg@altlinux.org> 0.6.0-alt1
- new version

* Thu Mar 06 2025 Sergey V Turchin <zerg@altlinux.org> 0.5.1-alt1
- new version

* Wed Nov 27 2024 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt3
- obsolete kde5-kquickimageeditor-common

* Wed Oct 23 2024 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt2
- fix conflicts

* Fri Oct 18 2024 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt1
- initial build
