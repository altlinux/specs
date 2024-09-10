%define rname kitemviews
%if_enabled python
%define sipver3 %(rpm -q --qf '%%{VERSION}' python3-module-sip)
%endif

Name: kf6-%rname
Version: 6.5.0
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6 set of item views extending the Qt model-view framework
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Wed Dec 24 2014 (-bi)
# optimized out: cmake cmake-modules elfutils libEGL-devel libGL-devel libcloog-isl4 libqt6-core libqt6-gui libqt6-test libqt6-widgets libqt6-xml libstdc++-devel python-base qt6-base-devel qt6-tools ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules gcc-c++ python-module-google qt6-tools-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf6 rpm-build-ubt
%if_enabled python
BuildRequires(pre): python3-module-sip-devel
BuildRequires: python3-module-PyQt6-devel
%endif
BuildRequires: gcc-c++ extra-cmake-modules qt6-base-devel qt6-tools-devel

%description
KItemViews includes a set of views, which can be used with item models. It
includes views for categorizing lists and to add search filters to flat and
hierarchical lists.

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

%package -n libkf6itemviews
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6itemviews
KF6 library

%if_enabled python
%package -n python3-module-%rname
Summary: Python3 bindings for KItemViews
License: GPLv2+ / LGPLv2+
Group: Development/Python3
Requires: %name-common = %version-%release
Requires: python3-module-pykf6
Requires: python3-module-sip = %sipver3
%description -n python3-module-%rname
Python3 bindings for KItemViews

%package -n python3-module-%rname-devel
Summary: Sip files for python3-module-%rname
Group: Development/Python3
BuildArch: noarch
%description -n python3-module-%rname-devel
Sip files for python3-module-%rname
%endif

%prep
%setup -n %rname-%version

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
#%_K6inc/kitemviews_version.h
%_K6inc/KItemViews/
%_K6link/lib*.so
%_K6lib/cmake/KF6ItemViews

%files -n libkf6itemviews
%_K6lib/libKF6ItemViews.so.*

%if_enabled python
%files -n python3-module-%rname
%python3_sitelibdir/PyKF6/*.so
%files -n python3-module-%rname-devel
%_datadir/sip3/PyKF6/KItemViews/
%endif


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

