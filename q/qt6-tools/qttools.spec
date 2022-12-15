%global qt_module qttools
#define optflags_lto %nil

%define kf6_bindir %prefix/lib/kf6/bin

Name: qt6-tools
Version: 6.2.4
Release: alt4
%define major %{expand:%(X='%version'; echo ${X%%%%.*})}
%define minor %{expand:%(X=%version; X=${X%%.*}; echo ${X#*.})}
%define bugfix %{expand:%(X='%version'; echo ${X##*.})}
%if "%version" == "%{get_version qt6-tools-common}"
%def_disable bootstrap
%else
%def_enable bootstrap
%endif

Group: System/Libraries
Summary: Qt6 - QtTool components
Url: http://qt.io/
License:  GPL-3.0-only or LGPL-3.0-only

Requires: %name-common = %EVR

Source: %qt_module-everywhere-src-%version.tar
Patch1: alt-run-qttools-with-qt6-suffix.patch

Source20: assistant.desktop
Source21: designer.desktop
Source22: linguist.desktop
Source23: qdbusviewer.desktop

BuildRequires(pre): rpm-macros-qt6 qt6-tools-common
#ifnarch %e2k
BuildRequires: clang-devel-static llvm-devel-static
BuildRequires: clang-devel llvm-devel
BuildRequires: /usr/bin/clang-format /usr/bin/clangd
#endif
BuildRequires: cmake desktop-file-utils gcc-c++ glibc-devel zlib-devel libicu-devel
BuildRequires: qt6-base-devel qt6-declarative-devel
BuildRequires: libXext-devel libX11-devel libxkbcommon-x11-devel
BuildRequires: libxslt-devel libudev-devel libgio-devel libsqlite3-devel
BuildRequires: rpm-macros-alternatives
%if_disabled bootstrap
BuildRequires: qt6-tools
%endif

%description
%summary.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
Requires: qt6-base-common
BuildArch: noarch
%description common
Common package for %name

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %EVR
Requires: qt6-base-devel
Requires: %name
Provides: %name-devel-static = %EVR
Obsoletes: %name-devel-static < %EVR
%description devel
%summary.

%package devel-static
Group: Development/KDE and QT
Summary: Development files for %name
BuildArch: noarch
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

%package -n qt6-assistant
Group: Text tools
Summary: Documentation browser for Qt6
Requires: %name-common = %EVR
Requires: %name = %EVR
%description -n qt6-assistant
%summary.

%package -n qt6-designer
Group: Development/KDE and QT
Summary: Designer for the Qt6
Requires: %name-common = %EVR
Requires: %name = %EVR
Provides: qt6-linguist = %EVR
%description -n qt6-designer
%summary.

%package -n qt6-dbus
Group: System/Configuration/Other
Summary: This package contains D-Bus utilities for Qt6
Requires: %name-common = %EVR
%description -n qt6-dbus
This package contains D-Bus utilities for Qt6.

%package -n libqt6-uitools
Group: System/Libraries
Summary: Qt6 library
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-uitools
%summary

%package -n libqt6-clucene
Group: System/Libraries
Summary: Qt6 library
Requires: %name-common = %EVR
%description -n libqt6-clucene
%summary

%package -n libqt6-designer
Group: System/Libraries
Summary: Qt6 library
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-designer
%summary

%package -n libqt6-designercomponents
Group: System/Libraries
Summary: Qt6 library
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-designercomponents
%summary

%package -n libqt6-help
Group: System/Libraries
Summary: Qt6 library
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-help
%summary

%prep
%setup -n %qt_module-everywhere-src-%version
#%patch1 -p1

%build
%define qdoc_found %{expand:%%(if [ -e %_qt6_bindir/qdoc ]; then echo 1; else echo 0; fi)}
# needed for documentation generation
# when some Qt header include paths
# are specified using '-isystem $path' arguments
%add_optflags -DQDOC_PASS_ISYSTEM
%Q6build \
    -DCMAKE_SKIP_RPATH:BOOL=ON \
    #
%if_disabled bootstrap
%make -C BUILD docs
%endif

%install
>main.filelist
%Q6install_qt
%if_disabled bootstrap
%if %qdoc_found
%make -C BUILD DESTDIR=%buildroot install_docs ||:
%endif
%endif

# Add desktop files
desktop-file-install \
  --dir=%buildroot/%_desktopdir \
  --vendor="qt6" \
  %SOURCE20 %SOURCE21 %SOURCE22 %SOURCE23 \
  #

# install qdbus alternative
QDBUS_ALTPRIO=`printf '%%.2d%%.2d%%.2d%%.2d\n' 0 %major %minor %bugfix`
mkdir -p %buildroot/%_altdir/
cat > %buildroot/%_altdir/qdbus-%_qt6 <<__EOF__
%_bindir/qdbus %_qt6_bindir/qdbus $QDBUS_ALTPRIO
__EOF__
cat > %buildroot/%_altdir/qdbusviewer-%_qt6 <<__EOF__
%_bindir/qdbusviewer %_qt6_bindir/qdbusviewer $QDBUS_ALTPRIO
__EOF__
mkdir -p %buildroot%kf6_bindir/
for qt_tool in qdbus
do
    ln -s `relative %_bindir/${qt_tool}-%_qt6 %kf6_bindir/${qt_tool}` %buildroot/%kf6_bindir/${qt_tool}
done

# icons
install -m644 -p -D src/assistant/assistant/images/assistant.png %buildroot/%_iconsdir/hicolor/32x32/apps/assistant-qt6.png
install -m644 -p -D src/assistant/assistant/images/assistant-128.png %buildroot/%_iconsdir/hicolor/128x128/apps/assistant-qt6.png
install -m644 -p -D src/designer/src/designer/images/designer.png %buildroot/%_iconsdir/hicolor/128x128/apps/designer-qt6.png
install -m644 -p -D src/qdbus/qdbusviewer/images/qdbusviewer.png %buildroot/%_iconsdir/hicolor/32x32/apps/qdbusviewer-qt6.png
install -m644 -p -D src/qdbus/qdbusviewer/images/qdbusviewer-128.png %buildroot/%_iconsdir/hicolor/128x128/apps/qdbusviewer-qt6.png
# linguist icons
for icon in src/linguist/linguist/images/icons/linguist-*-32.png ; do
  size=$(echo $(basename ${icon}) | cut -d- -f2)
  install -p -m644 -D ${icon} %buildroot/%_iconsdir/hicolor/${size}x${size}/apps/linguist-qt6.png
done
# add qdoc if compiled
if [ -e %buildroot/%_qt6_bindir/qdoc ] ; then
cat >>main.filelist <<__EOF__
%_bindir/qdoc*
%_qt6_bindir/qdoc*
__EOF__
fi

if [ -z "`ls -1 %buildroot/%_qt6_examplesdir/`" ] ; then
    mkdir -p %buildroot/%_qt6_examplesdir/
    >%buildroot/%_qt6_examplesdir/%name
fi

%files common
%_qt6_datadir/phrasebooks/

%files -f main.filelist
%_bindir/lconvert*
%_bindir/lrelease*
%_bindir/lupdate*
%_bindir/pixeltool*
%_bindir/qhelpgenerator*
%_bindir/qtdiag*
%_bindir/qtplugininfo*
%_bindir/qdistancefieldgenerator*
%_qt6_bindir/lconvert*
%_qt6_bindir/lrelease*
%_qt6_bindir/lupdate*
%_qt6_bindir/pixeltool*
%_qt6_bindir/qhelpgenerator*
%_qt6_bindir/qtdiag*
%_qt6_bindir/qtplugininfo*
%_qt6_bindir/qdistancefieldgenerator*
%_qt6_libexecdir/qtattributionsscanner
%_qt6_libexecdir/lprodump
%_qt6_libexecdir/lrelease-pro
%_qt6_libexecdir/lupdate-pro

%files -n qt6-assistant
%_bindir/assistant-qt6
%_qt6_bindir/assistant
%_desktopdir/*assistant.desktop
%_iconsdir/hicolor/*/apps/assistant*.*
%if_disabled bootstrap
%_qt6_docdir/qtassistant/
%_qt6_docdir/qtassistant.qch
%endif

%files -n qt6-dbus
%_altdir/qdbus-%_qt6
%_bindir/qdbus-qt6
%_qt6_bindir/qdbus
%kf6_bindir/qdbus
%_altdir/qdbusviewer-%_qt6
%_bindir/qdbusviewer*
%_qt6_bindir/qdbusviewer*
%_desktopdir/*qdbusviewer.desktop
%_iconsdir/hicolor/*/apps/qdbusviewer*.*

%files -n qt6-designer
%_bindir/designer*
%_bindir/linguist*
%_qt6_bindir/linguist*
%_qt6_bindir/designer*
%_qt6_plugindir/designer/lib*.so
%_desktopdir/*designer.desktop
%_desktopdir/*linguist.desktop
%_iconsdir/hicolor/*/apps/designer*.*
%_iconsdir/hicolor/*/apps/linguist*.*

%files devel
#%_qt6_libexecdir/*
%_qt6_headerdir/QtDesigner/
%_qt6_headerdir/QtDesignerComponents/
%_qt6_headerdir/QtHelp/
%_qt6_headerdir/QtUiTools/
%_qt6_headerdir/QtUiPlugin/
%_qt6_headerdir/QtTools/
%_qt6_libdir/libQt*.prl
%_qt6_libdatadir/libQt*.prl
%_qt6_libdir/libQt*.so
%_qt6_libdatadir/libQt*.so
%_qt6_archdatadir/mkspecs/modules/*.pri
%_libdir/cmake/Qt*/
%_qt6_libdir/metatypes/qt6*.json
%_qt6_datadir/modules/*.json
# devel-static
#%_qt6_libdir/libQt?*.a
#%_qt6_libdatadir/libQt?*.a

#%files  devel-static

%files doc
%if_disabled bootstrap
%_qt6_docdir/*
%exclude %_qt6_docdir/qtassistant/
%exclude %_qt6_docdir/qtassistant.qch
%endif
%_qt6_examplesdir/*

%files -n libqt6-designer
%_qt6_libdir/libQt6Designer.so.*
%files -n libqt6-designercomponents
%_qt6_libdir/libQt6DesignerComponents.so.*
%files -n libqt6-help
%_qt6_libdir/libQt6Help.so.*
%files -n libqt6-uitools
%_qt6_libdir/libQt6UiTools.so.*

%changelog
* Thu Dec 15 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt4
- automate bootstrap mode

* Fri Jun 10 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt3
- fix run lupdate

* Thu Jun 09 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt2
- fix run lprodump

* Wed May 25 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt1
- new version

* Tue Dec 07 2021 Sergey V Turchin <zerg@altlinux.org> 6.2.2-alt1
- new version

* Mon Dec 06 2021 Sergey V Turchin <zerg@altlinux.org> 6.2.1-alt1
- initial build
