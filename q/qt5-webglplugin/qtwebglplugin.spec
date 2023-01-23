
%global qt_module qtwebglplugin
%define major 5

Name: qt5-webglplugin
Version: 5.15.8
Release: alt1

Group: System/Libraries
Summary: Qt5 - WebGL streaming plugin
Url: http://qt.io/
License: LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)

Requires: libqt5-core = %_qt5_version
Requires: %name-common

Source: %qt_module-everywhere-src-%version.tar

BuildRequires(pre): rpm-macros-qt5
BuildRequires: gcc-c++ glibc-devel
BuildRequires: qt5-base-devel
BuildRequires: qt5-base-devel-static
BuildRequires: qt5-websockets-devel
# following is the list of missing dependencies of qt5-base-devel-static
BuildRequires: glib2-devel
BuildRequires: fontconfig-devel
BuildRequires: libfreetype-devel
BuildRequires: zlib-devel

%description
Qt5 QPA plugin for running an application via a browser using streamed WebGL commands.

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
Requires: %name-common
Requires: qt5-base-devel
%description devel
%summary.

%package devel-static
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common
Requires: %name-devel
%description devel-static
%summary.

%package doc
Summary: Document for developing apps which will use Qt5 %qt_module
Group: Development/KDE and QT
Requires: %name-common
%description doc
This package contains documentation for Qt5 %qt_module

%package -n libqt5-webglplugin
Summary: Qt5 library
Group: System/Libraries
Requires: %name-common
Requires: libqt5-core = %_qt5_version
%description -n libqt5-webglplugin
%summary

%prep
%setup -qn %qt_module-everywhere-src-%version
syncqt.pl-qt5 -version %version

%build
%qmake_qt5
%make_build

%install
%install_qt5

%files common
%files
%doc LICENSE*
%_qt5_plugindir/platforms/*webgl*.so

%files devel
%_qt5_libdir/cmake/Qt%{major}Gui/*WebGL*.cmake

%changelog
* Wed Jan 18 2023 Sergey V Turchin <zerg@altlinux.org> 5.15.8-alt1
- new version

* Tue Nov 15 2022 Sergey V Turchin <zerg@altlinux.org> 5.15.7-alt1
- new version

* Fri Oct 07 2022 Sergey V Turchin <zerg@altlinux.org> 5.15.6-alt1
- new version

* Mon Jul 04 2022 Sergey V Turchin <zerg@altlinux.org> 5.15.4-alt1
- new version

* Mon Jan 11 2021 Sergey V Turchin <zerg@altlinux.org> 5.15.2-alt1
- new version

* Thu Sep 10 2020 Sergey V Turchin <zerg@altlinux.org> 5.15.1-alt1
- new version

* Thu Aug 13 2020 Sergey V Turchin <zerg@altlinux.org> 5.15.0-alt1
- new version

* Wed Aug 05 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 5.12.9-alt1
- Initial build for ALT.
