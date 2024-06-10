%define rname kcompletion
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
Summary: KDE Frameworks 6 completion-ready widgets
Url: http://www.kde.org
License: LGPL-2.0-or-later

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
%if_enabled python
BuildRequires(pre): python3-module-sip-devel
BuildRequires: python3-module-PyQt6-devel
%endif
BuildRequires: extra-cmake-modules kf6-kconfig-devel kf6-kwidgetsaddons-devel kf6-kcodecs-devel
BuildRequires: qt6-declarative-devel qt6-tools-devel

%description
KCompletion provides the completion-ready widgets framework.

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

%package -n libkf6completion
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6completion
KF6 library

%if_enabled python
%package -n python-module-%rname
Summary: Python bindings for KCompletion
License: GPLv2+ / LGPLv2+
Group: Development/Python
Requires: %name-common = %version-%release
Requires: python-module-pykf6
Requires: python-module-sip = %sipver2
%description -n python-module-%rname
Python bindings for KCompletion

%package -n python-module-%rname-devel
Summary: Sip files for python-module-%rname
Group: Development/Python
BuildArch: noarch
%description -n python-module-%rname-devel
Sip files for python-module-%rname

%package -n python3-module-%rname
Summary: Python3 bindings for KCompletion
License: GPLv2+ / LGPLv2+
Group: Development/Python3
Requires: %name-common = %version-%release
Requires: python3-module-pykf6
Requires: python3-module-sip = %sipver3
%description -n python3-module-%rname
Python3 bindings for KCompletion

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
%K6build

%install
%K6install
%find_lang %name --all-name
%K6find_qtlang %name --all-name
rm -rf %buildroot%_libdir/*/*/*/__*


%files common -f %name.lang
%doc LICENSES/* README.md
%_datadir/qlogging-categories6/*.*categories

%files devel
%_K6plug/designer/*.so
#%_K6inc/kcompletion_version.h
%_K6inc/KCompletion/
%_K6link/lib*.so
%_K6lib/cmake/KF6Completion

%files -n libkf6completion
%_K6lib/libKF6Completion.so.*

%if_enabled python
#%files -n python-module-%rname
#%python_sitelibdir/PyKF6/*.so
#%files -n python-module-%rname-devel
#%_datadir/sip/PyKF6/KCompletion/
%files -n python3-module-%rname
%python3_sitelibdir/PyKF6/*.so
%files -n python3-module-%rname-devel
%_datadir/sip3/PyKF6/KCompletion/
%endif


%changelog
* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

