%define rname kconfigwidgets
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
Summary: KDE Frameworks 6 widgets for configuration dialogs

Url: http://www.kde.org
License: LGPL-2.0-or-later

Source: %rname-%version.tar
Patch1: alt-klanguagebutton-dups.patch

BuildRequires(pre): rpm-build-kf6
%if_enabled python
BuildRequires(pre): python3-module-sip-devel
BuildRequires: python3-module-kcodecs-devel python3-module-kwidgetsaddons-devel python3-module-kconfig-devel python3-module-kauth-devel python3-module-kcoreaddons-devel
BuildRequires: python3-module-PyQt6-devel
%endif
BuildRequires: extra-cmake-modules
BuildRequires: qt6-base-devel qt6-declarative-devel qt6-tools-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kcodecs-devel kf6-kconfig-devel
BuildRequires: kf6-kwidgetsaddons-devel kf6-kcoreaddons-devel kf6-kguiaddons-devel kf6-ki18n-devel
BuildRequires: kf6-kdoctools-devel kf6-kcolorscheme-devel

%description
KConfigWidgets provides easy-to-use classes to create configuration dialogs, as
well as a set of widgets which uses KConfig to store their settings.

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
Requires: kf6-kauth-devel kf6-kcodecs-devel kf6-kconfig-devel kf6-kwidgetsaddons-devel kf6-kguiaddons-devel
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n libkf6configwidgets
Group: System/Libraries
Summary: KF6 library
Requires: %name-common = %version-%release
%description -n libkf6configwidgets
KF6 library

%if_enabled python
%package -n python-module-%rname
Summary: Python bindings for KConfigWidgets
License: GPLv2+ / LGPLv2+
Group: Development/Python
Requires: %name-common = %version-%release
Requires: python-module-pykf6
Requires: python-module-sip = %sipver2
%description -n python-module-%rname
Python bindings for KConfigWidgets

%package -n python-module-%rname-devel
Summary: Sip files for python-module-%rname
Group: Development/Python
BuildArch: noarch
%description -n python-module-%rname-devel
Sip files for python-module-%rname

%package -n python3-module-%rname
Summary: Python3 bindings for KConfigWidgets
License: GPLv2+ / LGPLv2+
Group: Development/Python3
Requires: %name-common = %version-%release
Requires: python3-module-pykf6
Requires: python3-module-sip = %sipver3
%description -n python3-module-%rname
Python3 bindings for KConfigWidgets

%package -n python3-module-%rname-devel
Summary: Sip files for python3-module-%rname
Group: Development/Python3
BuildArch: noarch
%description -n python3-module-%rname-devel
Sip files for python3-module-%rname
%endif

%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K6build

%install
%K6install
%K6install_move data locale
%find_lang %name --all-name --with-kde
%K6find_qtlang %name --all-name
rm -rf %buildroot%_libdir/*/*/*/__*


mkdir -p %buildroot/%_K6data/kconfigwidgets/


%files common -f %name.lang
%doc LICENSES/* README.md
%dir %_K6data/kconfigwidgets/
%_datadir/qlogging-categories6/*.*categories
%_K6i18n/*/kf6_entry.desktop

%files devel
%_K6inc/KConfigWidgets/
%_K6link/lib*.so
%_K6lib/cmake/KF6ConfigWidgets
%_K6plug/designer/*.so

%files -n libkf6configwidgets
%_K6lib/libKF6ConfigWidgets.so.*

%if_enabled python
#%files -n python-module-%rname
#%python_sitelibdir/PyKF6/*.so
#%files -n python-module-%rname-devel
#%_datadir/sip/PyKF6/KConfigWidgets/
%files -n python3-module-%rname
%python3_sitelibdir/PyKF6/*.so
%files -n python3-module-%rname-devel
%_datadir/sip3/PyKF6/KConfigWidgets/
%endif


%changelog
* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

