%define rname qqc2-breeze-style

Name: %rname
Version: 6.7.2
Release: alt1

Summary: Breeze inspired QQC2 Style
License: LGPL-2.0-or-later
Group: Graphical desktop/KDE
Url: https://invent.kde.org/plasma/qqc2-breeze-style

Provides: kf6-qqc2-breeze-style = %EVR
Obsoletes: kf6-qqc2-breeze-style < %EVR

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6

BuildRequires: cmake
BuildRequires: extra-cmake-modules

BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Qml)

BuildRequires: kf6-kguiaddons-devel
BuildRequires: kf6-kconfig-devel
BuildRequires: kf6-kirigami-devel
BuildRequires: kf6-kcolorscheme-devel
BuildRequires: kf6-kiconthemes-devel

%description
This is a style for Qt Quick Controls (also known as QQC2 in Qt)
which implements the KDE Visual Design Group's vision for Breeze
in pure Qt Quick and Kirigami.

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: kf6-filesystem
%description devel
The %name-devel package contains CMake files for
developing applications that use %name.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install

%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc README.md
%dir %_K6qml/org/kde/breeze/
%_K6qml/org/kde/breeze/*
%_K6plug/kf6/kirigami/platform/org.kde.breeze.so

%files devel
%_libdir/cmake/QQC2BreezeStyle/

%changelog
* Wed Jul 01 2026 Sergey V Turchin <zerg@altlinux.org> 6.7.2-alt1
- new version

* Mon Jun 29 2026 Sergey V Turchin <zerg@altlinux.org> 6.7.1-alt1
- new version

* Tue May 12 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.5-alt1
- new version

* Fri Apr 10 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.4-alt2
- fix obsoletes

* Thu Apr 09 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.4-alt1
- new version

* Thu Apr 09 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.3-alt2
- fix provides

* Thu Apr 09 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.3-alt1
- new version
- rename package

* Sat Feb 07 2026 Nikolay Strelkov <snk@altlinux.org> 6.5.91-alt1
- Initial build for Sisyphus
