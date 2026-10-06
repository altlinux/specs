%define rname syndication

Name: dkf6-%rname
Version: 6.28.0
Release: alt0.dde.1
%DK6init altplace

Group: Graphical desktop/KDE
Summary: RSS/Atom parser library
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %name-%version.tar

# Automatically added by buildreq on Wed Aug 12 2015 (-bi)
# optimized out: cmake cmake-modules elfutils libEGL-devel libGL-devel libqt6-core libqt6-dbus libqt6-gui libqt6-network libqt6-widgets libqt6-x11extras libqt6-xml libstdc++-devel python-base python3 python3-base ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules gcc-c++ kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kio-devel kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-kservice-devel kf6-kwidgetsaddons-devel kf6-kxmlgui-devel kf6-solid-devel libdb4-devel python-module-google qt6-base-devel rpm-build-python3 rpm-build-ruby
BuildRequires(pre): rpm-build-dkf6 rpm-build-ubt
BuildRequires: deepin-extra-cmake-modules dqt6-tools-devel
BuildRequires: dkf6-kauth-devel dkf6-kbookmarks-devel dkf6-kcodecs-devel dkf6-kcompletion-devel dkf6-kconfig-devel
BuildRequires: dkf6-kconfigwidgets-devel dkf6-kcoreaddons-devel dkf6-kio-devel dkf6-kitemviews-devel dkf6-kjobwidgets-devel
BuildRequires: dkf6-kservice-devel dkf6-kwidgetsaddons-devel dkf6-kxmlgui-devel dkf6-solid-devel

# find libraries
%add_findprov_lib_path %_DK6lib

%description
%summary.

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

%package -n libdkf6syndication
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libdkf6syndication
KF6 library


%prep
%setup -n %name-%version

%build
%DK6build

%install
%DK6install
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/* README.md
%_DK6data/qlogging-categories6/*.*categories

%files devel
%_DK6inc/Syndication/
%_DK6link/lib*.so
%_DK6lib/cmake/KF6Syndication/

%files -n libdkf6syndication
%_DK6lib/libKF6Syndication.so.*


%changelog
* Tue Oct 06 2026 Leontiy Volodin <lvol@altlinux.org> 6.28.0-alt0.dde.1
- fork for independent deepin build

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

* Tue Jun 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

