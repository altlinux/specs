
%global qt_module qtdoc

Name: qt5-doc
Version: 5.4.0
Release: alt1

Group: Development/KDE and QT
Summary: Main Qt5 Reference Documentation
Url: http://qt-project.org/
License: LGPLv2 / GPLv3

BuildArch: noarch

Source: %qt_module-opensource-src-%version.tar

BuildRequires: gcc-c++ qt5-base-devel qt5-tools

%description
QtDoc contains the main Qt Reference Documentation, which includes
overviews, Qt topics, and examples not specific to any Qt module.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
BuildArch: noarch
Requires: qt5-base-common
%description common
Common package for %name

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %EVR
Requires: qt5-base-devel
%description devel
%summary.

%package devel-static
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %EVR
Requires: %name-devel
%description devel-static
%summary.

%package doc
BuildArch: noarch
Summary: Document for developing apps which will use Qt5 %qt_module
Group: Development/KDE and QT
Requires: %name-common = %EVR
%description doc
This package contains documentation for Qt5 %qt_module

%package -n libqt5-doc
Summary: Qt5 library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n libqt5-doc
%summary

%prep
%setup -qn %qt_module-opensource-src-%version

%build
%qmake_qt5
%make_build
%make docs

%install
%install_qt5
%make INSTALL_ROOT=%buildroot install_docs ||:

%files
%_qt5_docdir/*

%changelog
* Tue Dec 16 2014 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- new version

* Wed Sep 17 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt1
- new version

* Fri Jun 27 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt0.M70P.1
- build for M70P

* Thu Jun 26 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- new version

* Thu Jun 05 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- initial build
