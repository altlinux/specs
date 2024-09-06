%define qdoc_found %{expand:%%(if [ -e %_qt6_bindir/qdoc ]; then echo 1; else echo 0; fi)}
%global qt_module qtwebview

Name: qt6-webview
Version: 6.7.2
Release: alt1

Group: System/Libraries
Summary: Qt Web View
Url: http://qt.io/
License:  LGPL-2.1 with Qt-LGPL-exception-1.1 or LGPL-3.0-only

Requires: qt6-webengine

ExcludeArch: %not_qt6_qtwebengine_arches

Source: %qt_module-everywhere-src-%version.tar

BuildRequires(pre): rpm-macros-qt6 rpm-macros-qt6-webengine
BuildRequires: cmake glibc-devel
BuildRequires: qt6-base-devel qt6-webengine-devel qt6-tools

%description
%summary

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
Requires: qt6-base-devel rpm-build-qml
%description devel
%summary.

%package doc
Summary: Document for developing apps which will use Qt5 %qt_module
Group: Development/KDE and QT
Requires: %name-common
%description doc
This package contains documentation for Qt5 %qt_module

%package -n libqt6-webview
Group: System/Libraries
Summary: Qt5 - library
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-webview
%summary

%package -n libqt6-webviewquick
Group: System/Libraries
Summary: Qt5 - library
Requires: %name-common
Requires: libqt6-core = %_qt6_version
Provides: %name = %EVR
Obsoletes: %name < %EVR
%description -n libqt6-webviewquick
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

%files -n libqt6-webview
%_qt6_libdir/libQt?WebView.so.*
%files -n libqt6-webviewquick
%_qt6_libdir/libQt?WebViewQuick.so.*
%_qt6_plugindir/webview/
%_qt6_qmldir/QtWebView/

%files devel
%_qt6_libdir/libQt*.so
%_qt6_libdatadir/libQt*.so
%_qt6_libdir/libQt*.prl
%_qt6_libdatadir/libQt*.prl
%_qt6_headerdir/Qt*/
%_qt6_archdatadir/mkspecs/modules/*.pr*
%_qt6_archdatadir/metatypes/qt*.json
%_qt6_archdatadir/modules/*.json
%_libdir/cmake/Qt*/
%_pkgconfigdir/Qt?WebView*.pc

%files doc
%if %qdoc_found
%_qt6_docdir/*
%endif
%_qt6_examplesdir/*

%changelog
* Tue Aug 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.7.2-alt1
- new version

* Wed Jul 10 2024 Sergey V Turchin <zerg@altlinux.org> 6.6.2-alt1
- initial build
