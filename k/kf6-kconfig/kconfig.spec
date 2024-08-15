%define rname kconfig
%def_disable notify
%def_disable python
%if_enabled python
%define sipver3 %(rpm -q --qf '%%{VERSION}' python3-module-sip)
%endif

Name: kf6-%rname
Version: 6.4.0
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6 advanced configuration system
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar
Patch2: alt-kconfig-notify-via-dbus.patch
Patch3: alt-small-not-authorize-donate.patch

# Automatically added by buildreq on Wed Dec 24 2014 (-bi)
# optimized out: cmake cmake-modules elfutils libEGL-devel libGL-devel libcloog-isl4 libqt6-core libqt6-gui libqt6-test libqt6-widgets libqt6-xml libstdc++-devel python-base qt6-base-devel qt6-tools ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules gcc-c++ python-module-google qt6-tools-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf6 rpm-build-ubt
%if_enabled python
BuildRequires(pre): python3-module-sip-devel
BuildRequires: python3-module-PyQt6-devel
%endif
BuildRequires: gcc-c++ extra-cmake-modules qt6-base-devel qt6-declarative-devel qt6-tools-devel

%description
KConfig provides an advanced configuration system.

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

%package -n libkf6configgui
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6configgui
KF6 library

%package -n libkf6configcore
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6configcore
KF6 library

%package -n libkf6configqml
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6configqml
KF6 library

%if_enabled python
%package -n python3-module-%rname
Summary: Python3 bindings for KConfig
License: GPLv2+ / LGPLv2+
Group: Development/Python3
Requires: %name-common = %version-%release
Requires: python3-module-pykf6
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
%setup -n %rname-%version
%if_enabled notify
%patch2 -p2
%endif
%patch3 -p1

%build
%K6build

%install
%K6install
%find_lang %name --all-name
%K6find_qtlang %name --all-name


%files common -f %name.lang
%doc LICENSES/* README.md
%_datadir/qlogging-categories6/*.*categories

%files
%_bindir/kreadconfig6
%_K6bin/kreadconfig6
%_bindir/kwriteconfig6
%_K6bin/kwriteconfig6
%if_enabled notify
%_K6bin/kconf_watcher
%_K6bin/kconf_apply
%endif
%_K6qml/org/kde/config/

%files devel
%_K6exec/kconfig_compiler_kf6
#%_K6inc/kconfig_version.h
%_K6inc/KConfig/kconfig_version.h
%_K6inc/KConfigCore/
%_K6inc/KConfigGui/
%_K6inc/KConfigQml/
%_K6link/lib*.so
%_K6lib/cmake/KF6Config

%files -n libkf6configcore
%_K6lib/libKF6ConfigCore.so.*
%_K6exec/kconf_update
%files -n libkf6configgui
%_K6lib/libKF6ConfigGui.so.*
%files -n libkf6configqml
%_K6lib/libKF6ConfigQml.so.*

%if_enabled python
%files -n python3-module-%rname
%python3_sitelibdir/PyKF6/*.so
%files -n python3-module-%rname-devel
%_datadir/sip3/PyKF6/KConfigGui/
%_datadir/sip3/PyKF6/KConfigCore/
%endif


%changelog
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

