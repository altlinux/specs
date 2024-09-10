%define rname qqc2-desktop-style

Name: kf6-%rname
Version: 6.5.0
Release: alt1
%K6init altplace

Group: Graphical desktop/KDE
Summary: KDE Frameworks 6 visual style
Url: http://www.kde.org
License: LGPL-2.1-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-base-devel qt6-declarative-devel qt6-tools-devel
BuildRequires: libvulkan-devel
BuildRequires: kf6-kauth-devel kf6-kcoreaddons-devel kf6-kconfigwidgets-devel kf6-kiconthemes-devel kf6-kirigami-devel
BuildRequires: kf6-kcolorscheme-devel

%description
QtQuickControls 2 style that uses QWidget's QStyle for painting

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -n %rname-%version

%build
%K6build

%install
%K6install
%K6find_qtlang --all-name %name

%files -f %name.lang
%_K6qml/org/kde/desktop/
%_K6qml/org/kde/qqc2desktopstyle/
%_K6plug/kf6/kirigami/platform/*.so

%files devel
%_libdir/cmake/KF6QQC2*Style/


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

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

