%define rname ki18n
%def_disable python
%if_enabled python
%define sipver2 %(rpm -q --qf '%%{VERSION}' python-module-sip)
%define sipver3 %(rpm -q --qf '%%{VERSION}' python3-module-sip)
%endif
%add_python3_path %_libdir/cmake

Name: kf6-%rname
Version: 6.3.0
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6 gettext-based UI text internationalization
Url: http://www.kde.org
License: LGPL-2.0-or-later

Source: %rname-%version.tar
Patch1: alt-fallback.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: rpm-build-python3
BuildRequires: extra-cmake-modules qt6-declarative-devel
%if_enabled python
BuildRequires(pre): python3-module-sip-devel
BuildRequires: python3-module-PyQt6-devel
%endif

%description
KI18n provides functionality for internationalizing user interface text
in applications, based on the GNU Gettext translation system.
It wraps the standard Gettext functionality, so that the programmers
and translators can use the familiar Gettext tools and workflows.

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

%package -n libkf6i18n
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
%description -n libkf6i18n
KF6 library

%package -n libkf6i18nlocaledata
Group: System/Libraries
Summary: KF6 library
Requires: %name-common
Requires: iso-codes
%description -n libkf6i18nlocaledata
KF6 library

%if_enabled python
%package -n python-module-%rname
Summary: Python bindings for KI18n
License: GPLv2+ / LGPLv2+
Group: Development/Python
Requires: %name-common
Requires: python-module-pykf6
Requires: python-module-sip = %sipver2
%description -n python-module-%rname
Python bindings for KI18n

%package -n python-module-%rname-devel
Summary: Sip files for python-module-%rname
Group: Development/Python
BuildArch: noarch
%description -n python-module-%rname-devel
Sip files for python-module-%rname

%package -n python3-module-%rname
Summary: Python3 bindings for KI18n
License: GPLv2+ / LGPLv2+
Group: Development/Python3
Requires: %name-common
Requires: python3-module-pykf6
Requires: python3-module-sip = %sipver3
%description -n python3-module-%rname
Python3 bindings for KI18n

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

%if_disabled python
sed -i 's|PythonModuleGeneration|PythonModuleGeneration_DISABLED|' src/CMakeLists.txt
%endif

%build
%K6build

%install
%K6install
%K6install_move data locale
%find_lang %name --all-name
%K6find_qtlang %name --all-name
rm -rf %buildroot%_libdir/*/*/*/__*


%files common -f %name.lang
%doc LICENSES/* README.md
%dir %_K6i18n/*/
%dir %_K6i18n/*/LC_MESSAGES/
%_K6i18n/*/LC_SCRIPTS/
%_datadir/qlogging-categories6/*.*categories

%files devel
#%_K6inc/ki18n_version.h
%_K6inc/KI18n/
%_K6inc/KI18nLocaleData/
%_K6link/lib*.so
%_K6lib/cmake/KF6I18n/

%files -n libkf6i18n
%_K6lib/libKF6I18n.so.*
%_K6plug/kf6/ktranscript.so
%files -n libkf6i18nlocaledata
%_K6lib/libKF6I18nLocaleData.so.*
%_K6qml/org/kde/i18n/localeData/

%if_enabled python
#%files -n python-module-%rname
#%python_sitelibdir/PyKF6/*.so
#%files -n python-module-%rname-devel
#%_datadir/sip/PyKF6/KI18n/
%files -n python3-module-%rname
%python3_sitelibdir/PyKF6/*.so
%files -n python3-module-%rname-devel
%_datadir/sip3/PyKF6/KI18n/
%endif


%changelog
* Tue Jun 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

