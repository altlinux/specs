%define sover 2.2

Name: kddockwidgets
Version: 2.2.5
Release: alt1

Summary: Qt dock widget library, suitable for replacing QDockWidget
License: GPL-2.0-only OR GPL-3.0-only
Group: System/Libraries

Url: https://www.kdab.com/development-resources/qt-tools/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/KDAB/KDDockWidgets/archive/v%version/KDDockWidgets-%version.tar.gz
Source: KDDockWidgets-%version.tar

BuildRequires: libkdbindings-devel
BuildRequires: libspdlog-devel
BuildRequires: libvulkan-devel
BuildRequires: nlohmann-json-devel
BuildRequires: qt5-quickcontrols2-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: qt6-declarative-devel

%description
KDDockWidgets is a Qt dock widget library written by KDAB, suitable for
replacing QDockWidget and implementing advanced functionalities missing in Qt.

Although KDDockWidgets is ready to be used out of the box, it can also be seen
as a framework to allow building very tailored custom docking systems. It tries
to expose every internal widget and every knob for the app developer to tune.

%package -n lib%name%sover
Summary: Qt dock widget library, suitable for replacing QDockWidget
Group: System/Libraries

%description -n lib%name%sover
KDDockWidgets is a Qt dock widget library written by KDAB, suitable for
replacing QDockWidget and implementing advanced functionalities missing in Qt.

Although KDDockWidgets is ready to be used out of the box, it can also be seen
as a framework to allow building very tailored custom docking systems. It tries
to expose every internal widget and every knob for the app developer to tune.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C++

%description -n lib%name-devel
This package contains libraries and header files for
developing applications that use %name.

%package -n lib%name-qt6_%sover
Summary: Qt dock widget library, suitable for replacing QDockWidget
Group: System/Libraries

%description -n lib%name-qt6_%sover
KDDockWidgets is a Qt dock widget library written by KDAB, suitable for
replacing QDockWidget and implementing advanced functionalities missing in Qt.

Although KDDockWidgets is ready to be used out of the box, it can also be seen
as a framework to allow building very tailored custom docking systems. It tries
to expose every internal widget and every knob for the app developer to tune.

%package -n lib%name-qt6-devel
Summary: Development files for %name
Group: Development/C++

%description -n lib%name-qt6-devel
This package contains libraries and header files for
developing applications that use %name.

%prep
%setup -n KDDockWidgets-%version

%build
# Qt 5 version
%define _cmake__builddir %_target_platform
%cmake -DECM_MKSPECS_INSTALL_DIR:PATH=%_qt5_archdatadir/mkspecs/modules
%cmake_build

# Qt 6 version
%define _cmake__builddir %_target_platform-qt6
%cmake -DKDDockWidgets_QT6:BOOL=ON
%cmake_build

%install
# Qt 5 version
%define _cmake__builddir %_target_platform
%cmake_install
%__rm -rf %buildroot%_defaultdocdir/KDDockWidgets

# Qt 6 version
%define _cmake__builddir %_target_platform-qt6
%cmake_install
%__rm -rf %buildroot%_defaultdocdir/KDDockWidgets-qt6

%files -n lib%name%sover
%doc README.md
%_libdir/lib%name.so.%sover
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_libdir/lib%name.so
%_includedir/%name
%_cmakedir/KDDockWidgets
%_qt5_archdatadir/mkspecs/modules/qt_KDDockWidgets.pri

%files -n lib%name-qt6_%sover
%doc README.md
%_libdir/lib%name-qt6.so.%sover
%_libdir/lib%name-qt6.so.*

%files -n lib%name-qt6-devel
%_libdir/lib%name-qt6.so
%_includedir/%name-qt6
%_cmakedir/KDDockWidgets-qt6
%_qt6_mkspecsdir/modules/qt_KDDockWidgets.pri

%changelog
* Mon Jun 30 2025 Nazarov Denis <nenderus@altlinux.org> 2.2.5-alt1
- Initial build for ALT Linux


