%define rname analitza

%define sover 9
%define libanalitzaplot libanalitzaplot%sover
%define libanalitzagui libanalitzagui%sover
%define libanalitzawidgets libanalitzawidgets%sover
%define libanalitza libanalitza%sover

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: System/Libraries
Summary: Mathematical features
Url: http://www.kde.org
License: GPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: eigen3 extra-cmake-modules qt6-declarative-devel qt6-svg-devel qt6-tools-devel
BuildRequires: libvulkan-devel libGLU-devel
BuildRequires: kf6-ki18n-devel

%description
The analitza library will let you add mathematical features to your program.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Provides:  kde5-analitza-common = %EVR
Obsoletes: kde5-analitza-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Conflicts: kde5-analitza-devel
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libanalitzaplot
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libanalitzaplot
%name library

%package -n %libanalitzagui
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libanalitzagui
%name library

%package -n %libanalitzawidgets
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libanalitzawidgets
%name library

%package -n %libanalitza
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libanalitza
%name library

%prep
%setup -n %rname-%version

%build
%K6build \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    #

%install
%K6install
%K6install_move data libanalitza
%find_lang %name --with-kde --all-name
%K6find_qtlang %name --all-name

%files common -f %name.lang
%doc COPYING*

%files devel
%_K6inc/Analitza?/
%_K6link/lib*.so
%_K6lib/cmake/Analitza?/

%files -n %libanalitzaplot
%_K6lib/libAnalitzaPlot.so.%sover
%_K6lib/libAnalitzaPlot.so.*
%_K6qml/org/kde/analitza/
%_K6data/libanalitza/
%files -n %libanalitzagui
%_K6lib/libAnalitzaGui.so.%sover
%_K6lib/libAnalitzaGui.so.*
%files -n %libanalitzawidgets
%_K6lib/libAnalitzaWidgets.so.%sover
%_K6lib/libAnalitzaWidgets.so.*
%files -n %libanalitza
%_K6lib/libAnalitza.so.%sover
%_K6lib/libAnalitza.so.*


%changelog
* Tue Jun 09 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.2-alt1
- new version

* Mon May 11 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.1-alt1
- new version

* Tue Mar 10 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.3-alt1
- new version

* Sat Feb 07 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.2-alt1
- new version

* Tue Jan 20 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.1-alt1
- new version

* Wed Oct 22 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.2-alt1
- new version

* Tue Jul 22 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.3-alt1
- new version

* Wed May 28 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.1-alt1
- new version

* Mon Feb 24 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.2-alt1
- new version

* Thu Nov 07 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- initial build

