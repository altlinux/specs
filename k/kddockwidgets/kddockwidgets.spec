%define sover 3

Name: kddockwidgets
Version: 2.4.0
Release: alt1

Summary: Qt dock widget library, suitable for replacing QDockWidget
License: GPL-2.0-only OR GPL-3.0-only
Group: System/Libraries

Url: https://www.kdab.com/development-resources/qt-tools/%name
Vcs: https://github.com/KDAB/KDDockWidgets
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/KDAB/KDDockWidgets/archive/v%version/KDDockWidgets-%version.tar.gz
Source: KDDockWidgets-%version.tar

BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: libkdbindings-devel
BuildRequires: libspdlog-devel
BuildRequires: libvulkan-devel
BuildRequires: nlohmann-json-devel
BuildRequires: python3-dev
BuildRequires: qt5-quickcontrols2-devel
BuildRequires: qt5-tools
BuildRequires: qt5-x11extras-devel
BuildRequires: qt6-declarative-devel
BuildRequires: qt6-tools

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
%cmake \
	-DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
	-DKDDockWidgets_QT6:BOOL=OFF \
	-DKDDockWidgets_TESTS:BOOL=ON \
	-DKDDockWidgets_DOCS:BOOL=ON \
	-DECM_MKSPECS_INSTALL_DIR:PATH=%_qt5_archdatadir/mkspecs/modules \
	%nil
%cmake_build

# Qt 6 version
export PATH=%_qt6_libexecdir:$PATH
%define _cmake__builddir %_target_platform-qt6
%cmake \
	-DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
	-DKDDockWidgets_TESTS:BOOL=ON \
	-DKDDockWidgets_DOCS:BOOL=ON \
	-DKDDockWidgets_QML_MODULE:BOOL=ON \
	%nil
%cmake_build

%install
# Qt 5 version
%define _cmake__builddir %_target_platform
%cmake_install
%__rm -rf %buildroot%_defaultdocdir/KDDockWidgets/{LICENSES,LICENSE.txt,README.md}

# Qt 6 version
%define _cmake__builddir %_target_platform-qt6
%cmake_install
%__rm -rf %buildroot%_defaultdocdir/KDDockWidgets-qt6/{LICENSES,LICENSE.txt,README.md}

%files -n lib%name%sover
%doc LICENSE.txt README.md
%_libdir/lib%name.so.%sover
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_libdir/lib%name.so
%_includedir/%name
%_cmakedir/KDDockWidgets
%_qt5_archdatadir/mkspecs/modules/qt_KDDockWidgets.pri
%_defaultdocdir/KDDockWidgets

%files -n lib%name-qt6_%sover
%doc LICENSE.txt README.md
%_libdir/lib%name-qt6.so.%sover
%_libdir/lib%name-qt6.so.*

%files -n lib%name-qt6-devel
%_libdir/lib%name-qt6.so
%_includedir/%name-qt6
%_cmakedir/KDDockWidgets-qt6
%_qt6_mkspecsdir/modules/qt_KDDockWidgets.pri
%_defaultdocdir/KDDockWidgets-qt6

%changelog
* Wed Nov 05 2025 Nazarov Denis <nenderus@altlinux.org> 2.4.0-alt1
- New version 2.4.0.

* Sun Sep 28 2025 Nazarov Denis <nenderus@altlinux.org> 2.3.0-alt1
- New version 2.3.0.

* Mon Jun 30 2025 Nazarov Denis <nenderus@altlinux.org> 2.2.5-alt1
- Initial build for ALT Linux


