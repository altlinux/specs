%define qdoc_found %{expand:%%(if [ -e %_qt6_bindir/qdoc ]; then echo 1; else echo 0; fi)}
%global qt_module qtremoteobjects

Name:    qt6-remoteobjects
Summary: Qt6 - Qt Remote Objects
Group: System/Libraries
Version: 6.1.1
Release: alt1

# See LGPL_EXCEPTIONS.txt, LICENSE.GPL3, respectively, for exception details
License: LGPLv2 with exceptions or GPLv3 with exceptions
Url:     http://www.qt.io

Source: %qt_module-everywhere-src-%version.tar

BuildRequires(pre): rpm-macros-qt6 qt6-tools
BuildRequires: cmake qt6-base-devel qt6-declarative-devel

%description
Qt Remote Objects (QtRO) is an inter-process communication (IPC)
module developed for Qt.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
Requires: qt6-base-common
BuildArch: noarch
%description common
Common package for %name

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
Requires: %name = %EVR
Requires: qt6-base-devel

%description devel
%summary.

%package doc
Summary: Document for developing apps which will use Qt6 %qt_module
Group: Development/KDE and QT
Requires: %name-common
%description doc
This package contains documentation for Qt6 %qt_module

%package -n libqt6-remoteobjects
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-remoteobjects
%summary

%package -n libqt6-remoteobjectsqml
Group: System/Libraries
Summary: Qt6 - library
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-remoteobjectsqml
%summary

%prep
%setup -n %qt_module-everywhere-src-%version
#syncqt.pl-qt6 -version %version

%build
%Q6build
%if %qdoc_found
%make -C BUILD docs
%endif

%install
%Q6install_qt
%if %qdoc_found
%make -C BUILD DESTDIR=%buildroot install_docs ||:
%endif


%files common

%files
%doc LICENSES/*
%_qt6_libexecdir/repc
%_qt6_qmldir/QtRemoteObjects/

%files -n libqt6-remoteobjects
%_qt6_libdir/libQt6RemoteObjects.so.*
%files -n libqt6-remoteobjectsqml
%_qt6_libdir/libQt6RemoteObjectsQml.so.*

%files devel
%_qt6_headerdir/QtRemoteObjects*/
%_qt6_headerdir/QtRepParser/
%_qt6_libdir/libQt?R*.prl
%_qt6_libdatadir/libQt?R*.prl
%_qt6_libdir/cmake/Qt?RemoteObjects*/
%_qt6_libdir/cmake/Qt?RepParser/
%_qt6_libdir/cmake/Qt?Qml/QmlPlugins/Qt?declarative*
%_qt6_libdir/cmake/Qt?BuildInternals/StandaloneTests/QtRemoteObjects*.cmake
%_qt6_libdir/pkgconfig/Qt?R*.pc
%_qt6_archdatadir/mkspecs/features/*.pr*
%_qt6_archdatadir/mkspecs/modules/qt_lib_r*.pr*
%_qt6_libdir/libQt*.so
%_qt6_libdatadir/libQt*.so
%_qt6_archdatadir/metatypes/qt*.json
%_qt6_archdatadir/modules/*.json

%files doc
%if %qdoc_found
%_qt6_docdir/*
%endif
%_qt6_examplesdir/*

%changelog
* Tue Dec 05 2023 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- initial build
