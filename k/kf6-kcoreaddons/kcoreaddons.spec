%define rname kcoreaddons
%def_disable python
%if_enabled python
%define sipver3 %(rpm -q --qf '%%{VERSION}' python3-module-sip)
%endif

Name: kf6-%rname
Version: 6.27.0
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6 Tier 1 addon with various classes on top of QtCore
Url: http://www.kde.org
License: LGPL-2.1-or-later

Source: %rname-%version.tar
Patch1: alt-kreslimit-integration.patch
Patch2: alt-smb-share.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: libudev-devel libmount-devel
%if_enabled python
BuildRequires(pre): python3-module-sip-devel
BuildRequires: python3-module-PyQt6-devel
%endif
BuildRequires: gcc-c++ extra-cmake-modules qt6-base-devel qt6-tools-devel qt6-declarative-devel
BuildRequires: shared-mime-info

%description
KCoreAddons provides classes built on top of QtCore to perform various tasks
such as manipulating mime types, autosaving files, creating backup files,
generating random sequences, performing text manipulations such as macro
replacement, accessing user information and many more.

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
Requires: qt6-base-devel
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf6coreaddons
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6coreaddons
KF6 library

%if_enabled python
%package -n python-module-%rname-devel
Summary: Sip files for python-module-%rname
Group: Development/Python
BuildArch: noarch
%description -n python-module-%rname-devel
Sip files for python-module-%rname

%package -n python3-module-pykf6
Summary: common package for KF6 python3 bindings
License: GPLv2+ / LGPLv2+
Group: Development/Python3
Requires: %name-common = %version-%release
%description -n python3-module-pykf6
common package for KF6 python3 bindings

%package -n python3-module-%rname
Summary: Python3 bindings for KCoreAddons
License: GPLv2+ / LGPLv2+
Group: Development/Python3
Requires: %name-common = %version-%release
Requires: python3-module-sip = %sipver3
%description -n python3-module-%rname
Python3 bindings for KCoreAddons

%package -n python3-module-%rname-devel
Summary: Sip files for python3-module-%rname
Group: Development/Python3
BuildArch: noarch
%description -n python3-module-%rname-devel
Sip files for python3-module-%rname
%endif

%prep
%setup -n %rname-%version
%patch1 -p1 -b .kreslimit
%patch2 -p1
%ifarch %e2k
sed -i -E 's/(if \()(static const auto.*; )(force ==)/\2\1\3/' src/lib/io/kurlmimedata.cpp
%endif

%build
%K6build \
    -DBUILD_PYTHON_BINDINGS:BOOL=OFF \
    -DKDE4_DEFAULT_HOME=".kde4" \
    -D_KDE4_DEFAULT_HOME_POSTFIX=4 \
    #

%install
%K6install
%find_lang %name --all-name
%K6find_qtlang %name --all-name


%files common -f %name.lang
%doc LICENSES/* README.md
%_datadir/qlogging-categories6/*.*categories
%_xdgmimedir/packages/kde6.xml

%files devel
%_K6inc/KCoreAddons/
%_K6link/lib*.so
%_pkgconfigdir/*CoreAddons*.pc
%_K6lib/cmake/KF6CoreAddons
%_K6data/jsonschema/*.json
%_K6archdata/metatypes/*.json

%files -n libkf6coreaddons
%_K6lib/libKF6CoreAddons.so.*
%_K6qml/org/kde/coreaddons/

%if_enabled python
%files -n python3-module-pykf6
%dir %python3_sitelibdir/PyKF6/
%python3_sitelibdir/PyKF6/__init__.py
%python3_sitelibdir/PyKF6/__pycache__/
%dir %_datadir/sip3/PyKF6/
%files -n python3-module-%rname
%python3_sitelibdir/PyKF6/*.so
%files -n python3-module-%rname-devel
%_datadir/sip3/PyKF6/KCoreAddons/
%endif


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

* Mon Nov 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.8.0-alt2
- E2K: lcc 1.29 ICE workaround (mcst#9171; ilyakurdyukov@)

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

