%define qdoc_found %{expand:%%(if [ -e %_qt6_bindir/qdoc ]; then echo 1; else echo 0; fi)}

%global qt_module qtgrpc

Name: qt6-grpc
Version: 6.10.3
Release: alt3

Group: System/Libraries
Summary: Qt6 - Grpc component
Url: http://qt.io/
License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0

Source: %qt_module-everywhere-src-%version.tar

BuildRequires(pre): rpm-macros-qt6 qt6-tools
BuildRequires: cmake qt6-declarative-devel
BuildRequires: libgrpc-devel libgrpc++-devel /usr/bin/grpc_cpp_plugin
BuildRequires: libprotobuf-devel libprotobuf-c-devel libcares-devel libre2-devel

%description
Support for CAN and potentially other serial buses.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
BuildArch: noarch
Requires: qt6-base-common
%description common
Common package for %name

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common
Requires: qt6-base-devel
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
Summary: Document for developing apps which will use Qt6 %qt_module
Group: Development/KDE and QT
Requires: %name-common
%description doc
This package contains documentation for Qt6 %qt_module

%package -n libqt6-grpc
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-grpc
%summary

%package -n libqt6-grpcquick
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-grpcquick
%summary

%package -n libqt6-protobuf
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-protobuf
%summary

%package -n libqt6-protobufqtcoretypes
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-protobufqtcoretypes
%summary

%package -n libqt6-protobufqtfuitypes
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-protobufqtfuitypes
%summary

%package -n libqt6-protobufquick
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-protobufquick
%summary

%package -n libqt6-protobufwellknowntypes
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-protobufwellknowntypes
%summary

%prep
%setup -n %qt_module-everywhere-src-%version

%build
%Q6build \
    -DQT_GENERATE_SBOM:BOOL=OFF \
    -DQT_BUILD_EXAMPLES:BOOL=OFF \
    #
%if %qdoc_found
%Q6make --target docs
%endif

%install
%Q6install_qt
%if %qdoc_found
#%make -C BUILD DESTDIR=%buildroot install_docs ||:
mkdir -p %buildroot/%_docdir/qt6/
cp -ar BUILD/share/doc/qt6/* %buildroot/%_docdir/qt6/
%endif

%files common
%doc LICENSES/*

%files -n libqt6-grpc
%_qt6_libdir/libQt?Grpc.so.*
%files -n libqt6-grpcquick
%_qt6_libdir/libQt?GrpcQuick.so.*
%_qt6_qmldir/QtGrpc/
%files -n libqt6-protobuf
%_qt6_libdir/libQt?Protobuf.so.*
%files -n libqt6-protobufqtcoretypes
%_qt6_libdir/libQt?ProtobufQtCoreTypes.so.*
%files -n libqt6-protobufqtfuitypes
%_qt6_libdir/libQt?ProtobufQtGuiTypes.so.*
%files -n libqt6-protobufquick
%_qt6_libdir/libQt?ProtobufQuick.so.*
%_qt6_qmldir/QtProtobuf/
%files -n libqt6-protobufwellknowntypes
%_qt6_libdir/libQt?ProtobufWellKnownTypes.so.*

%files devel
%_qt6_libexecdir/qt*gen
%_qt6_headerdir/Qt*/
%_qt6_libdatadir/libQt*.so
%_qt6_libdatadir/libQt*.prl
%_qt6_libdir/libQt*.so
%_qt6_libdir/libQt*.prl
%_qt6_libdir/cmake/Qt*/
%_qt6_archdatadir/mkspecs/modules/qt_lib_*.pri
%_qt6_archdatadir/metatypes/qt6*.json
%_qt6_archdatadir/modules/*.json
%_pkgconfigdir/Qt?*.pc

%files doc
%if %qdoc_found
%_qt6_docdir/*
%endif
#%_qt6_examplesdir/*

%changelog
* Mon Jun 01 2026 Sergey V Turchin <zerg@altlinux.org> 6.10.3-alt3
- don't build examples

* Mon Apr 13 2026 Sergey V Turchin <zerg@altlinux.org> 6.10.3-alt2
- fix build requires

* Tue Apr 07 2026 Sergey V Turchin <zerg@altlinux.org> 6.10.3-alt1
- new version

* Tue Mar 24 2026 Sergey V Turchin <zerg@altlinux.org> 6.10.2-alt1
- initial build
