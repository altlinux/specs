%define rname frameworkintegration

%def_enable packagekit

Name: kf6-%rname
Version: 6.27.0
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6 integration
Url: http://www.kde.org
License: LGPL-2.0-or-later

Source: %rname-%version.tar
Patch1: alt-def-font.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-tools-devel qt6-declarative-devel
%if_enabled packagekit
BuildRequires: libappstream-qt6-devel packagekit-qt6-devel
%endif
BuildRequires: kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kdbusaddons-devel kf6-kglobalaccel-devel
BuildRequires: kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel kf6-kio-devel kf6-kitemviews-devel
BuildRequires: kf6-kjobwidgets-devel kf6-knotifications-devel kf6-kservice-devel kf6-ktextwidgets-devel
BuildRequires: kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel kf6-solid-devel
BuildRequires: kf6-sonnet-devel kf6-kpackage-devel kf6-knewstuff-devel

%description
Framework Integration is a set of plugins responsible for better integration of
Qt applications when running on a KDE Plasma workspace.

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
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf6style
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6style
KF6 library


%prep
%setup -n %rname-%version
#%patch1 -p1

if [ -d %_libdir/cmake/AppStreamQt6 -a ! -d %_libdir/cmake/AppStreamQt ] ; then
    mkdir -p cmake/AppStreamQt/
    for f in %_libdir/cmake/AppStreamQt6/*.cmake ; do
	ln -s $f cmake/AppStreamQt/`basename "$f" | sed 's|6||'`
    done
    ln -s %_includedir/AppStreamQt6 src/kpackage-install-handlers/appstream/AppStreamQt
fi

%build
%K6build \
    -DAppStreamQt_DIR:PATH=$PWD/cmake/AppStreamQt \
    #

%install
%K6install
%K6install_move data kconf_update
%find_lang %name --all-name
%K6find_qtlang %name --all-name
mkdir -p %buildroot/%_K6exec/kpackagehandlers/

%files common -f %name.lang
%doc LICENSES/* README.md
%dir %_K6exec/kpackagehandlers/

%files devel
%_K6inc/FrameworkIntegration/
%_K6inc/KStyle/
%_K6link/lib*.so
%_K6lib/cmake/KF6FrameworkIntegration

%files -n libkf6style
%_K6exec/kpackagehandlers/knshandler
%if_enabled packagekit
%_K6exec/kpackagehandlers/appstreamhandler
%endif
%_K6lib/libKF6Style.so.*
%_K6plug/kf6/*.so
%_K6notif/*.notifyrc


%changelog
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

