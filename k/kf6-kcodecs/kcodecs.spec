%define rname kcodecs
%def_disable python
%if_enabled python
%define sipver2 %(rpm -q --qf '%%{VERSION}' python-module-sip)
%define sipver3 %(rpm -q --qf '%%{VERSION}' python3-module-sip)
%endif

Name: kf6-%rname
Version: 6.4.0
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6 collection of methods to manipulate strings
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Fri Dec 26 2014 (-bi)
# optimized out: cmake cmake-modules elfutils libcloog-isl4 libqt6-core libqt6-test libqt6-xml libstdc++-devel python-base qt6-base-devel qt6-tools ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules gcc-c++ python-module-google qt6-tools-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf6
BuildRequires(pre): python3-module-sip-devel

BuildRequires: extra-cmake-modules gcc-c++ qt6-tools-devel
BuildRequires: /usr/bin/gperf
BuildRequires: python3-module-PyQt6-devel

%description
KCodecs provide a collection of methods to manipulate strings using various encodings.

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

%package -n libkf6codecs
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6codecs
KF6 library

%if_enabled python
%package -n python-module-%rname
Summary: Python bindings for KCodecs
License: GPLv2+ / LGPLv2+
Group: Development/Python
Requires: %name-common = %version-%release
Requires: python-module-pykf6
Requires: python-module-sip = %sipver2
%description -n python-module-%rname
Python bindings for KCodecs

%package -n python-module-%rname-devel
Summary: Sip files for python-module-%rname
Group: Development/Python
BuildArch: noarch
%description -n python-module-%rname-devel
Sip files for python-module-%rname

%package -n python3-module-%rname
Summary: Python3 bindings for KCodecs
License: GPLv2+ / LGPLv2+
Group: Development/Python3
Requires: %name-common = %version-%release
Requires: python3-module-pykf6
Requires: python3-module-sip = %sipver3
%description -n python3-module-%rname
Python3 bindings for KCodecs

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
%_K6inc/KCodecs/
%_K6link/lib*.so
%_K6lib/cmake/KF6Codecs

%files -n libkf6codecs
%_K6lib/libKF6Codecs.so.*

%if_enabled python
#%files -n python-module-%rname
#%python_sitelibdir/PyKF6/*.so
#%files -n python-module-%rname-devel
#%_datadir/sip/PyKF6/KCodecs/
%files -n python3-module-%rname
%python3_sitelibdir/PyKF6/*.so
%files -n python3-module-%rname-devel
%_datadir/sip3/PyKF6/KCodecs/
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

