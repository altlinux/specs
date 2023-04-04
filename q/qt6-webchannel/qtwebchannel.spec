%define qdoc_found %{expand:%%(if [ -e %_qt6_bindir/qdoc ]; then echo 1; else echo 0; fi)}

%global qt_module qtwebchannel
%def_disable bootstrap

%add_findreq_skiplist %_qt6_examplesdir/*

Name: qt6-webchannel
Version: 6.4.2
Release: alt1

Group: System/Libraries
Summary: Qt6 - WebChannel component
Url: http://qt.io/
License: LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)

Source: %qt_module-everywhere-src-%version.tar

BuildRequires(pre): rpm-macros-qt6
BuildRequires: cmake glibc-devel qt6-base-devel
BuildRequires: qt6-websockets-devel qt6-declarative-devel
%if_disabled bootstrap
BuildRequires(pre): qt6-tools
%endif

%description
The Qt WebChannel module provides a library for seamless integration of C++
and QML applications with HTML/JavaScript clients. Any QObject can be
published to remote clients, where its public API becomes available.

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
Requires: %name-common = %EVR
Requires: qt6-base-devel
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
Summary: Document for developing apps which will use Qt6 %qt_module
Group: Development/KDE and QT
Requires: %name-common = %EVR
%description doc
This package contains documentation for Qt6 %qt_module

%package -n libqt6-webchannel
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-webchannel
%summary

%prep
%setup -n %qt_module-everywhere-src-%version

%build
%Q6build
%if_disabled bootstrap
%if %qdoc_found
export QT_HASH_SEED=0
%make -C BUILD docs
%endif
%endif

%install
%Q6install_qt
%if_disabled bootstrap
%if %qdoc_found
%make -C BUILD DESTDIR=%buildroot install_docs ||:
%endif
%endif

%files common
%doc LICENSES/*

%files -n libqt6-webchannel
%_qt6_libdir/libQt?WebChannel.so.*
%_qt6_qmldir/QtWebChannel/

%files devel
%_qt6_headerdir/Qt*/
%_qt6_libdir/libQt*.so
%_qt6_libdatadir/libQt*.so
%_qt6_libdir/libQt*.prl
%_qt6_libdatadir/libQt*.prl
%_qt6_libdir/cmake/Qt*/
#%_qt6_libdir/pkgconfig/Qt*.pc
%_qt6_archdatadir/mkspecs/modules/*.pri
%_qt6_libdir/metatypes/qt6*.json
%_qt6_datadir/modules/*.json
%_pkgconfigdir/Qt?*.pc

%files doc
%if_disabled bootstrap
%if %qdoc_found
%_qt6_docdir/*
%endif
%endif
#%_qt6_examplesdir/*

%changelog
* Wed Feb 15 2023 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt1
- new version

* Tue May 31 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt1
- initial build

