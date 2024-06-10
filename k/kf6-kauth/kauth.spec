%define rname kauth
%def_disable python
%if_enabled python
%define sipver2 %(rpm -q --qf '%%{VERSION}' python-module-sip)
%define sipver3 %(rpm -q --qf '%%{VERSION}' python3-module-sip)
%endif

Name: kf6-%rname
Version: 6.2.0
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6 executing actions as privileged user
Url: http://www.kde.org
License: LGPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
%if_enabled python
BuildRequires(pre): python3-module-sip-devel python3-module-PyQt6-devel
BuildRequires: python3-module-kcoreaddons-devel
%endif
BuildRequires: extra-cmake-modules gcc-c++ kf6-kcoreaddons-devel kf6-kwindowsystem-devel libpolkitqt6-qt6-devel qt6-tools-devel

%description
KAuth provides a convenient, system-integrated way to offload actions that need
to be performed as a privileged user (root, for example) to small (hopefully
secure) helper utilities.

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

%package -n libkf6auth
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6auth
KF6 library

%package -n libkf6authcore
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6authcore
KF6 library

%if_enabled python
%package -n python-module-%rname
Summary: Python bindings for KAuth
License: GPLv2+ / LGPLv2+
Group: Development/Python
Requires: %name-common = %version-%release
Requires: python-module-pykf6
Requires: python-module-sip = %sipver2
%description -n python-module-%rname
Python bindings for KAuth

%package -n python-module-%rname-devel
Summary: Sip files for python-module-%rname
Group: Development/Python
BuildArch: noarch
%description -n python-module-%rname-devel
Sip files for python-module-%rname

%package -n python3-module-%rname
Summary: Python3 bindings for KAuth
License: GPLv2+ / LGPLv2+
Group: Development/Python3
Requires: %name-common = %version-%release
Requires: python3-module-pykf6
Requires: python3-module-sip = %sipver3
%description -n python3-module-%rname
Python3 bindings for KAuth

%package -n python3-module-%rname-devel
Summary: Sip files for python3-module-%rname
Group: Development/Python3
BuildArch: noarch
%description -n python3-module-%rname-devel
Sip files for python3-module-%rname
%endif

%prep
%setup -n %rname-%version

%if_disabled python
sed -i 's|PythonModuleGeneration|PythonModuleGeneration_DISABLED|' src/CMakeLists.txt
%endif

%build
%K6build \
    -DKAUTH_BACKEND_NAME=PolkitQt6-1 \
    #

%install
%K6install
%find_lang %name --all-name
%K6find_qtlang %name --all-name
rm -rf %buildroot%_libdir/*/*/*/__*


%files common -f %name.lang
%doc LICENSES/* README.md
%_datadir/qlogging-categories6/*.*categories
%dir %_K6exec/kauth/
%_K6dbus/system.d/*auth*.conf

%files devel
%_K6inc/KAuth*/
%_K6link/lib*.so
%_K6lib/cmake/KF6Auth/
%_K6data/kauth/

%files -n libkf6authcore
%_K6lib/libKF6AuthCore.so.*
%_K6exec/kauth/*
%_K6plug/kf6/kauth/

#%files -n libkf6auth
#%_K6lib/libKF6Auth.so.*

%if_enabled python
%files -n python3-module-%rname
%python3_sitelibdir/PyKF6/*.so
%files -n python3-module-%rname-devel
%_datadir/sip3/PyKF6/KAuth/
%endif


%changelog
* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

