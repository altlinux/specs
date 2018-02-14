%define qt_module qtgamepad

Name: qt5-gamepad
Version: 5.9.4
Release: alt1%ubt

Group: System/Libraries
Summary: A Qt 5 module that adds support for getting events from gamepad devices on multiple platforms.
Url: http://qt.io/
License: LGPLv2 / GPLv3

Source: %qt_module-opensource-src-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires: gcc-c++ glibc-devel 
BuildRequires: libudev-devel libSDL2-devel
BuildRequires: qt5-base-devel qt5-base-devel-static

%description
%summary

%package common
Summary: Common package for %name
Group: System/Configuration/Other
Requires: qt5-base-common
%description common
Common package for %name

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %EVR
Requires: qt5-base-devel rpm-build-qml
%description devel
%summary.

%package -n libqt5-gamepad
Group: System/Libraries
Summary: Qt5 - library
Requires: %name-common = %EVR
%description -n libqt5-gamepad
%summary

%prep
%setup -n %qt_module-opensource-src-%version
syncqt.pl-qt5 -version %version -private

%build
%qmake_qt5
%make_build

%install
%install_qt5

%files common
%dir %_qt5_plugindir/gamepads/

%files -n libqt5-gamepad
%_qt5_libdir/libQt5Gamepad.so.*
%_qt5_plugindir/gamepads/*

%files devel
%_qt5_libdir/libQt*.so
%_qt5_libdatadir/libQt*.so
%_qt5_libdir/libQt*.prl
%_qt5_libdatadir/libQt*.prl
%_qt5_headerdir/Qt*/
%_qt5_archdatadir/mkspecs/modules/*.pr*
%_libdir/cmake/Qt*/
%_pkgconfigdir/Qt?Gamepad.pc

%changelog
* Wed Feb 14 2018 Oleg Solovyov <mcpain@altlinux.org> 5.9.4-alt1%ubt
- initial build
