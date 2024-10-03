%global qt_module dqttools
#define optflags_lto %nil

%define dkf6_bindir %prefix/lib/dkf6/bin

Name: dqt6-tools
Version: 6.7.2
Release: alt0.dde.1
%define major %{expand:%(X='%version'; echo ${X%%%%.*})}
%define minor %{expand:%(X=%version; X=${X%%.*}; echo ${X#*.})}
%define bugfix %{expand:%(X='%version'; echo ${X##*.})}
# %%if "%%version" == "%%{get_version dqt6-tools-common}"
# %%def_disable bootstrap
# %%else
%def_enable bootstrap
# %%endif

Group: System/Libraries
Summary: Qt6 - QtTool components
Url: http://qt.io/
License:  GPL-3.0-only or LGPL-3.0-only

Requires: %name-common = %EVR

Source: %qt_module-everywhere-src-%version.tar
Patch1: alt-run-qttools-with-dqt6-suffix.patch

Source20: assistant.desktop
Source21: designer.desktop
Source22: linguist.desktop
Source23: qdbusviewer.desktop

# find librares
%add_findprov_lib_path %_dqt6_libdir

BuildRequires(pre): rpm-macros-dqt6 rpm-build-ninja
# BuildRequires(pre): dqt6-tools-common
#ifnarch %e2k
BuildRequires: clang-devel-static llvm-devel-static
BuildRequires: clang-devel llvm-devel
BuildRequires: /usr/bin/clang-format /usr/bin/clangd
#endif
BuildRequires: cmake desktop-file-utils gcc-c++ glibc-devel zlib-devel libzstd-devel libicu-devel
BuildRequires: dqt6-base-devel dqt6-declarative-devel
BuildRequires: libXext-devel libX11-devel libxkbcommon-x11-devel
BuildRequires: libxslt-devel libudev-devel libgio-devel libsqlite3-devel
BuildRequires: rpm-macros-alternatives
%if_disabled bootstrap
BuildRequires: dqt6-tools
%endif

%description
%summary.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
Requires: dqt6-base-common
BuildArch: noarch
%description common
Common package for %name

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %EVR
Requires: dqt6-base-devel
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

%package -n dqt6-assistant
Group: Text tools
Summary: Documentation browser for Qt6
Requires: %name-common = %EVR
Requires: %name
%description -n dqt6-assistant
%summary.

%package -n dqt6-designer
Group: Development/KDE and QT
Summary: Designer for the Qt6
Requires: %name-common = %EVR
Requires: %name
Requires: dqt6-base-devel
Provides: dqt6-linguist = %EVR
%description -n dqt6-designer
%summary.

%package -n dqt6-dbus
Group: System/Configuration/Other
Summary: This package contains D-Bus utilities for Qt6
Requires: %name-common = %EVR
%description -n dqt6-dbus
This package contains D-Bus utilities for Qt6.

%package -n libdqt6-uitools
Group: System/Libraries
Summary: Qt6 library
Requires: %name-common = %EVR
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-uitools
%summary

%package -n libdqt6-clucene
Group: System/Libraries
Summary: Qt6 library
Requires: %name-common = %EVR
%description -n libdqt6-clucene
%summary

%package -n libdqt6-designer
Group: System/Libraries
Summary: Qt6 library
Requires: %name-common = %EVR
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-designer
%summary

%package -n libdqt6-designercomponents
Group: System/Libraries
Summary: Qt6 library
Requires: %name-common = %EVR
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-designercomponents
%summary

%package -n libdqt6-help
Group: System/Libraries
Summary: Qt6 library
Requires: %name-common = %EVR
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-help
%summary

%prep
%setup -n %qt_module-everywhere-src-%version
#%patch1 -p1

%build
%if_disabled bootstrap
%define qdoc_found %{expand:%%(if [ -e %_dqt6_bindir/qdoc ]; then echo 1; else echo 0; fi)}
%else
%define qdoc_found 0
%endif
# needed for documentation generation
# when some Qt header include paths
# are specified using '-isystem $path' arguments
%add_optflags -DQDOC_PASS_ISYSTEM
%DQ6build \
    -DCMAKE_SKIP_RPATH:BOOL=OFF \
    -DCMAKE_MAKE_PROGRAM=ninja \
    #
%if %qdoc_found
%DQ6make --target docs
%endif

%install
>main.filelist
%DQ6install_qt
%if %qdoc_found
%make -C BUILD DESTDIR=%buildroot VERBOSE=1 install_docs ||:
%endif

# Add desktop files
desktop-file-install \
  --dir=%buildroot/%_desktopdir \
  --vendor="dqt6" \
  %SOURCE20 %SOURCE21 %SOURCE22 %SOURCE23 \
  #

# install qdbus alternative
QDBUS_ALTPRIO=`printf '%%.2d%%.2d%%.2d%%.2d\n' 0 %major %minor %bugfix`
mkdir -p %buildroot/%_altdir/
cat > %buildroot/%_altdir/qdbus-%_dqt6 <<__EOF__
%_bindir/qdbus %_dqt6_bindir/qdbus $QDBUS_ALTPRIO
__EOF__
cat > %buildroot/%_altdir/qdbusviewer-%_dqt6 <<__EOF__
%_bindir/qdbusviewer %_dqt6_bindir/qdbusviewer $QDBUS_ALTPRIO
__EOF__
mkdir -p %buildroot%dkf6_bindir/
for qt_tool in qdbus
do
    ln -s `relative %_bindir/${qt_tool}-%_dqt6 %dkf6_bindir/${qt_tool}` %buildroot/%dkf6_bindir/${qt_tool}
done

# icons
install -m644 -p -D src/assistant/assistant/images/assistant.png %buildroot/%_iconsdir/hicolor/32x32/apps/assistant-dqt6.png
install -m644 -p -D src/assistant/assistant/images/assistant-128.png %buildroot/%_iconsdir/hicolor/128x128/apps/assistant-dqt6.png
install -m644 -p -D src/designer/src/designer/images/designer.png %buildroot/%_iconsdir/hicolor/128x128/apps/designer-dqt6.png
install -m644 -p -D src/qdbus/qdbusviewer/images/qdbusviewer.png %buildroot/%_iconsdir/hicolor/32x32/apps/qdbusviewer-dqt6.png
install -m644 -p -D src/qdbus/qdbusviewer/images/qdbusviewer-128.png %buildroot/%_iconsdir/hicolor/128x128/apps/qdbusviewer-dqt6.png
# linguist icons
for icon in src/linguist/linguist/images/icons/linguist-*-32.png ; do
  size=$(echo $(basename ${icon}) | cut -d- -f2)
  install -p -m644 -D ${icon} %buildroot/%_iconsdir/hicolor/${size}x${size}/apps/linguist-dqt6.png
done
# add qdoc if compiled
if [ -e %buildroot/%_dqt6_bindir/qdoc ] ; then
cat >>main.filelist <<__EOF__
%_bindir/qdoc*
%_dqt6_bindir/qdoc*
__EOF__
fi

if [ -z "`ls -1 %buildroot/%_dqt6_examplesdir/`" ] ; then
    mkdir -p %buildroot/%_dqt6_examplesdir/
    >%buildroot/%_dqt6_examplesdir/%name
fi

# relax depends on plugins files
for f in %buildroot/%_dqt6_libdir/cmake/Qt?*/Qt*luginTargets.cmake ; do
    sed -i '/message.*FATAL_ERROR.*target.* references the file/s|FATAL_ERROR|WARNING|' $f
done

%files common
%doc LICENSES/*
%_dqt6_datadir/phrasebooks/

%files -f main.filelist
%_bindir/lconvert*
%_bindir/lrelease*
%_bindir/lupdate*
%_bindir/pixeltool*
%_bindir/qtdiag*
%_bindir/qtplugininfo*
%_bindir/qdistancefieldgenerator*
%_dqt6_bindir/lconvert*
%_dqt6_bindir/lrelease*
%_dqt6_bindir/lupdate*
%_dqt6_bindir/pixeltool*
%_dqt6_bindir/qtdiag*
%_dqt6_bindir/qtplugininfo*
%_dqt6_bindir/qdistancefieldgenerator*
%_dqt6_libexecdir/qtattributionsscanner
%_dqt6_libexecdir/lprodump
%_dqt6_libexecdir/lrelease-pro
%_dqt6_libexecdir/lupdate-pro
%_dqt6_libexecdir/qhelpgenerator

%files -n dqt6-assistant
%_bindir/assistant-dqt6
%_dqt6_bindir/assistant
%_desktopdir/*assistant.desktop
%_iconsdir/hicolor/*/apps/assistant*.*
%if %qdoc_found
%_dqt6_docdir/qtassistant/
%_dqt6_docdir/qtassistant.qch
%endif

%files -n dqt6-dbus
%exclude %_altdir/qdbus-%_dqt6
%_bindir/qdbus-dqt6
%_dqt6_bindir/qdbus
%dkf6_bindir/qdbus
%exclude %_altdir/qdbusviewer-%_dqt6
%_bindir/qdbusviewer*
%_dqt6_bindir/qdbusviewer*
%_desktopdir/*qdbusviewer.desktop
%_iconsdir/hicolor/*/apps/qdbusviewer*.*

%files -n dqt6-designer
%_bindir/designer*
%_bindir/linguist*
%_dqt6_bindir/linguist*
%_dqt6_bindir/designer*
%_desktopdir/*designer.desktop
%_desktopdir/*linguist.desktop
%_iconsdir/hicolor/*/apps/designer*.*
%_iconsdir/hicolor/*/apps/linguist*.*

%files devel
%_dqt6_headerdir/Qt*/
%_dqt6_libdir/libQt*.prl
%_dqt6_libdatadir/libQt*.prl
%_dqt6_libdir/libQt*.so
%_dqt6_libdatadir/libQt*.so
%_dqt6_plugindir/designer/lib*.so
%_dqt6_archdatadir/mkspecs/modules/*.pri
%_dqt6_libdir/cmake/Qt*/
%_dqt6_archdatadir/metatypes/qt6*.json
%_dqt6_archdatadir/modules/*.json
%_dqt6_libdir/pkgconfig/Qt?*.pc
# devel-static
#%_dqt6_libdir/libQt?*.a
#%_dqt6_libdatadir/libQt?*.a

#%files  devel-static

%files doc
%if %qdoc_found
%_dqt6_docdir/*
%exclude %_dqt6_docdir/qtassistant/
%exclude %_dqt6_docdir/qtassistant.qch
%endif
%_dqt6_examplesdir/*

%files -n libdqt6-designer
%_dqt6_libdir/libQt6Designer.so.*
%files -n libdqt6-designercomponents
%_dqt6_libdir/libQt6DesignerComponents.so.*
%files -n libdqt6-help
%_dqt6_libdir/libQt6Help.so.*
%files -n libdqt6-uitools
%_dqt6_libdir/libQt6UiTools.so.*

%changelog
* Wed Oct 02 2024 Leontiy Volodin <lvol@altlinux.org> 6.7.2-alt0.dde.1
- fork qt6 for separate deepin packaging (ALT #48138)

* Tue Aug 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.7.2-alt1
- new version

* Mon Feb 19 2024 Sergey V Turchin <zerg@altlinux.org> 6.6.2-alt1
- new version

* Tue Jan 09 2024 Sergey V Turchin <zerg@altlinux.org> 6.6.1-alt2
- fix build docs

* Tue Dec 05 2023 Sergey V Turchin <zerg@altlinux.org> 6.6.1-alt1
- new version

* Tue Oct 31 2023 Sergey V Turchin <zerg@altlinux.org> 6.6.0-alt1
- new version

* Tue Jun 13 2023 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt2
- fixed compilation error with clang 16 (thanks asheplyakov@alt) (closes: 46478)

* Wed Feb 15 2023 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt1
- new version

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
