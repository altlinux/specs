%define rname kglobalaccel
%ifndef _userunitdir
%define _userunitdir %prefix/lib/systemd/user
%endif
%define service_name plasma-kglobalaccel

Name: dkf6-%rname
Version: 6.28.0
Release: alt0.dde.1
%DK6init

Group: System/Libraries
Summary: KDE Frameworks 6 global desktop keyboard shortcuts
Url: http://www.kde.org
License: LGPL-2.0-or-later

Source: %name-%version.tar

BuildRequires(pre): rpm-build-dkf6
BuildRequires: deepin-extra-cmake-modules dqt6-tools-devel
BuildRequires: vulkan-headers libdqt6-widgets
BuildRequires: libXScrnSaver-devel libXcomposite-devel libXcursor-devel libXdamage-devel
BuildRequires: libXdmcp-devel libXft-devel libXinerama-devel libXmu-devel libXpm-devel
BuildRequires: libXrandr-devel libXtst-devel libXv-devel libXxf86misc-devel
BuildRequires: libXxf86vm-devel libxcbutil-keysyms-devel libxkbfile-devel
#BuildRequires: dkf6-kconfig-devel dkf6-kcoreaddons-devel dkf6-kcrash-devel dkf6-kdbusaddons-devel
#BuildRequires: dkf6-ki18n-devel dkf6-kwindowsystem-devel dkf6-kservice-devel

# find libraries
%add_findprov_lib_path %_DK6lib

%description
KGlobalAccel allows you to have global accelerators that are independent of
the focused window.  Unlike regular shortcuts, the application's window does not
need focus for them to be activated.

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

%package -n libdkf6globalaccel
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n libdkf6globalaccel
KF6 library

%package -n libdkf6globalaccelprivate
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n libdkf6globalaccelprivate
KF6 library


%prep
%setup -n %name-%version

%build
%DK6build

%install
%DK6install
%DK6install_move data locale
mkdir -p %buildroot/%_DK6data/kglobalaccel/
%find_lang %name --all-name
%DK6find_qtlang %name --all-name

%files common -f %name.lang
%doc LICENSES/* README.md
%_DK6data/qlogging-categories6/*.*categories
%dir %_DK6data/kglobalaccel/

#%files
#%exclude %_bindir/*6
#%_DK6bin/kglobalaccel6
#%_DK6srv/kglobalaccel6.desktop
#%_DK6dbus_srv/org.kde.kglobalaccel.service
#%_DK6plug/org.kde.kglobalaccel6*/
#exclude %_userunitdir/%service_name.service

%files devel
%_DK6inc/KGlobalAccel/
%_DK6link/lib*.so
%_DK6lib/cmake/KF6GlobalAccel/
%_DK6dbus_iface/kf6_org.kde.??lobal?ccel*

%files -n libdkf6globalaccel
%_DK6lib/libKF6GlobalAccel.so.*
#%files -n libdkf6globalaccelprivate
#%_DK6lib/libKF6GlobalAccelPrivate.so.*


%changelog
* Thu Oct 01 2026 Leontiy Volodin <lvol@altlinux.org> 6.28.0-alt0.dde.1
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

