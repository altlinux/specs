%define qdoc_found %{expand:%%(if [ -e %_qt6_bindir/qdoc ]; then echo 1; else echo 0; fi)}
%global qt_module qtvirtualkeyboard

Name: qt6-virtualkeyboard
Version: 6.4.2
Release: alt1

Group: System/Libraries
Summary: Qt6 - QtQuick virtual keyboard component
Url: http://qt.io/
License: GPL-3.0-only

Requires: %name-common
Provides: qml6(QtQuick.VirtualKeyboard)

Source: %qt_module-everywhere-src-%version.tar

BuildRequires(pre): rpm-macros-qt6 qt6-tools
BuildRequires: cmake qt6-declarative-devel qt6-connectivity-devel qt6-multimedia-devel qt6-svg-devel
BuildRequires: libhunspell-devel
BuildRequires: libxcb-devel libxkbcommon-devel

%description
Qt Virtual Keyboard is a virtual keyboard framework that consists of a C++
backend supporting custom input methods as well as a UI frontend implemented
in QML.

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

%package -n libqt6-virtualkeyboard
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-virtualkeyboard
%summary

%package -n libqt6-hunspellinputmethod
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-hunspellinputmethod
%summary

%prep
%setup -n %qt_module-everywhere-src-%version
rm -rf src/virtualkeyboard/3rdparty/hunspell


%build
%Q6build \
    -DFEATURE_vkb_desktop:BOOL=ON \
    -DFEATURE_vkb_xcb:BOOL=ON \
    -DFEATURE_vkb_arrow_keynavigation:BOOL=ON \
    -DFEATURE_vkb_default_style:BOOL=ON \
    -DFEATURE_pinyin:BOOL=OFF \
    -DFEATURE_openwnn:BOOL=OFF \
    -DFEATURE_tcime:BOOL=OFF \
    -DFEATURE_cangjie:BOOL=OFF \
    -DFEATURE_zhuyin:BOOL=OFF \
    $(for d in src/virtualkeyboard/content/layouts/*_* ; do LNG=`basename $d`; echo -n " -DFEATURE_vkb_lang_${LNG}:BOOL=OFF"; done) \
    -DFEATURE_vkb_lang_en_US:BOOL=ON \
    -DFEATURE_vkb_lang_ru_RU:BOOL=ON \
    #
%if %qdoc_found
%make -C BUILD docs
%endif

%install
%Q6install_qt
%if %qdoc_found
%make -C BUILD DESTDIR=%buildroot install_docs ||:
%endif

%files common
%doc LICENSES/*

%files
%_qt6_plugindir/platforminputcontexts/*virtualkeyboard*.so
%_qt6_qmldir/QtQuick/VirtualKeyboard/

%files devel
%_qt6_libdatadir/libQt*.so
%_qt6_libdatadir/libQt*.prl
%_qt6_libdir/libQt*.so
%_qt6_libdir/libQt*.prl
%_libdir/cmake/Qt?/Find*.cmake
%_libdir/cmake/Qt?Gui/*VirtualKeyboard*
%_libdir/cmake/Qt?VirtualKeyboard/
%_libdir/cmake/Qt*InputMethod*/
%_libdir/cmake/Qt?BuildInternals/StandaloneTests/*VirtualKeyboard*.cmake
%_libdir/cmake/Qt?Qml/QmlPlugins/Qt?qtvkb*plugin*.cmake
%_qt6_headerdir/Qt*/
%_qt6_archdatadir/mkspecs/modules/qt_lib_*.pri
%_qt6_libdir/metatypes/qt6*.json
%_qt6_datadir/modules/*.json
%_pkgconfigdir/Qt?*.pc

%files doc
%if %qdoc_found
%_qt6_docdir/*
%endif
#%_qt6_examplesdir/*

%files -n libqt6-virtualkeyboard
%_qt6_libdir/libQt?VirtualKeyboard.so.*
%files -n libqt6-hunspellinputmethod
%_qt6_libdir/libQt?HunspellInputMethod.so.*

%changelog
* Wed Feb 15 2023 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt1
- new version

* Thu Oct 13 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt2
- fix requires

* Tue Jun 07 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt1
- initial build
