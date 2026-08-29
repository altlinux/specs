%define rname kconfig
%def_disable notify
%def_disable python
%if_enabled python
%define sipver3 %(rpm -q --qf '%%{VERSION}' python3-module-sip)
%endif

Name: dkf6-%rname
Version: 6.28.0
Release: alt0.dde.1
%DK6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6 advanced configuration system
Url: http://www.kde.org
License: LGPL-2.1-or-later AND GPL-2.0-or-later

Source: %name-%version.tar
Patch2: alt-kconfig-notify-via-dbus.patch
Patch3: alt-small-not-authorize-donate.patch

# Automatically added by buildreq on Wed Dec 24 2014 (-bi)
# optimized out: cmake cmake-modules elfutils libEGL-devel libGL-devel libcloog-isl4 libqt6-core libqt6-gui libqt6-test libqt6-widgets libqt6-xml libstdc++-devel python-base qt6-base-devel qt6-tools ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules gcc-c++ python-module-google qt6-tools-devel rpm-build-ruby
BuildRequires(pre): rpm-build-dkf6
%if_enabled python
BuildRequires(pre): python3-module-sip-devel
BuildRequires: python3-module-PyQt6-devel
%endif
BuildRequires: gcc-c++ deepin-extra-cmake-modules dqt6-base-devel dqt6-declarative-devel dqt6-tools-devel
BuildRequires: vulkan-headers libdqt6-dbus libdqt6-gui libdqt6-quick libdqt6-xml

# find libraries
%add_findprov_lib_path %_DK6lib

%description
KConfig provides an advanced configuration system.

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

%package -n libdkf6configgui
Group: System/Libraries
Summary: DKF6 library
Requires: %name-common = %version-%release
%description -n libdkf6configgui
DKF6 library

%package -n libdkf6configcore
Group: System/Libraries
Summary: DKF6 library
Requires: %name-common = %version-%release
%description -n libdkf6configcore
DKF6 library

%package -n libdkf6configqml
Group: System/Libraries
Summary: DKF6 library
Requires: %name-common = %version-%release
%description -n libdkf6configqml
DKF6 library

%if_enabled python
%package -n python3-module-%rname
Summary: Python3 bindings for KConfig
License: GPLv2+ / LGPLv2+
Group: Development/Python3
Requires: %name-common = %version-%release
Requires: python3-module-pydkf6
Requires: python3-module-sip = %sipver3
%description -n python3-module-%rname
Python3 bindings for KConfig

%package -n python3-module-%rname-devel
Summary: Sip files for python3-module-%rname
Group: Development/Python3
BuildArch: noarch
%description -n python3-module-%rname-devel
Sip files for python3-module-%rname
%endif

%prep
%setup -n %name-%version
%if_enabled notify
%patch2 -p2
%endif
%patch3 -p1

%build
%DK6build

%install
%DK6install
%find_lang %name --all-name
%DK6find_qtlang %name --all-name


%files common -f %name.lang
%doc LICENSES/* README.md
%_DK6data/qlogging-categories6/*.*categories

%files
%exclude %_bindir/kreadconfig6
%_DK6bin/kreadconfig6
%exclude %_bindir/kwriteconfig6
%_DK6bin/kwriteconfig6
%if_enabled notify
%_DK6bin/kconf_watcher
%_DK6bin/kconf_apply
%endif
%_DK6qml/org/kde/config/

%files devel
%_DK6exec/kconfig_compiler_kf6
# %_DK6inc/kconfig_version.h
%_DK6inc/KConfig/kconfig_version.h
%_DK6inc/KConfigCore/
%_DK6inc/KConfigGui/
%_DK6inc/KConfigQml/
%_DK6link/lib*.so
%_DK6lib/cmake/KF6Config/
%_DK6archdata/metatypes/*.json

%files -n libdkf6configcore
%_DK6lib/libKF6ConfigCore.so.*
%_DK6exec/kconf_update
%files -n libdkf6configgui
%_DK6lib/libKF6ConfigGui.so.*
%files -n libdkf6configqml
%_DK6lib/libKF6ConfigQml.so.*

%if_enabled python
%files -n python3-module-%rname
%python3_sitelibdir/PyKF6/*.so
%files -n python3-module-%rname-devel
%_datadir/sip3/PyKF6/KConfigGui/
%_datadir/sip3/PyKF6/KConfigCore/
%endif


%changelog
* Thu Aug 13 2026 Leontiy Volodin <lvol@altlinux.org> 6.28.0-alt0.dde.1
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

