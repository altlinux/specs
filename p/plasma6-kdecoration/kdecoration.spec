%define rname kdecoration
%define sover 6
%define sover_private 2
%define libkdecorations libkdecorations3_%sover
%define libkdecorationsprivate libkdecorations3private%sover_private

Name: plasma6-%rname
Version: 6.7.2
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
%_K6inc/kdecoration?_version.h
%_includedir/KDecoration?/
%_K6link/lib*.so
%_K6lib/cmake/KDecoration?/

%files -n %libkdecorations
%_K6lib/libkdecorations3.so.%sover
%_K6lib/libkdecorations3.so.*
%files -n %libkdecorationsprivate
%_K6lib/libkdecorations3private.so.%sover_private
%_K6lib/libkdecorations3private.so.*



%changelog
* Wed Jul 01 2026 Sergey V Turchin <zerg@altlinux.org> 6.7.2-alt1
- new version

* Mon Jun 29 2026 Sergey V Turchin <zerg@altlinux.org> 6.7.1-alt1
- new version

* Tue May 12 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.5-alt1
- new version

* Thu Apr 09 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.4-alt1
- new version

* Mon Mar 30 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.3-alt1
- new version

* Wed Mar 11 2026 Sergey V Turchin <zerg@altlinux.org> 6.5.6-alt1
- new version

* Thu Jan 15 2026 Sergey V Turchin <zerg@altlinux.org> 6.5.5-alt1
- new version

* Wed Dec 10 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.4-alt1
- new version

* Tue Nov 18 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.3-alt1
- new version

* Thu Nov 13 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.2-alt1
- new version

* Wed Nov 12 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.6-alt1
- new version

* Tue Sep 16 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.5-alt1
- new version

* Fri Aug 22 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.4-alt1
- new version

* Tue Jul 15 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.3-alt1
- new version

* Tue Jul 08 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt1
- new version

* Wed May 07 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.5-alt1
- new version

* Wed Apr 02 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.4-alt1
- new version

* Wed Mar 12 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.3-alt1
- new version

* Wed Feb 26 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.2-alt1
- new version

* Wed Feb 19 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.1-alt1
- new version

* Fri Feb 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

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

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build

