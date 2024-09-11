%define rname kdecoration
%define sover 6
%define sover_private 11
%define libkdecorations libkdecorations2_%sover
%define libkdecorationsprivate libkdecorations2private%sover_private

Name: plasma6-%rname
Version: 6.1.5
Release: alt1
%K6init

Group: System/Libraries
Summary: KDE Frameworks 6 Plugin based library to create window decorations
Url: http://www.kde.org
License: GPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: libvulkan-devel
BuildRequires: extra-cmake-modules qt6-base-devel
BuildRequires: kf6-ki18n-devel kf6-kcoreaddons-devel

%description
KDecoration2 is a library to create window decorations. These window decorations can be used by
for example an X11 based window manager which re-parents a Client window to a window decoration
frame.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
Provides: plasma5-kdecoration-common = %EVR
Obsoletes: plasma5-kdecoration-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Conflicts: plasma5-kdecoration-devel
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n %libkdecorations
Group: System/Libraries
Summary: KF6 library
Requires: %name-common >= %EVR
%description -n %libkdecorations
KF6 library

%package -n %libkdecorationsprivate
Group: System/Libraries
Summary: KF6 library
Requires: %name-common >= %EVR
%description -n %libkdecorationsprivate
KF6 library


%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%find_lang %name --all-name

%files common -f %name.lang
%doc LICENSES/* README.md

%files devel
%_K6inc/kdecoration2_version.h
%_includedir/KDecoration2/
%_K6link/lib*.so
%_K6lib/cmake/KDecoration2

%files -n %libkdecorations
%_K6lib/libkdecorations2.so.%sover
%_K6lib/libkdecorations2.so.*
%files -n %libkdecorationsprivate
%_K6lib/libkdecorations2private.so.%sover_private
%_K6lib/libkdecorations2private.so.*



%changelog
* Tue Sep 10 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.5-alt1
- new version

* Thu Aug 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.4-alt1
- new version

* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build

