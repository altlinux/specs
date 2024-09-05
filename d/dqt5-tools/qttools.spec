%define optflags_lto %nil

%global qt_module dqttools
%def_disable qtconfig

%define dkf5_bindir %prefix/lib/dkf5/bin

Name: dqt5-tools
Version: 5.15.13
Release: alt0.dde.1
%define major %{expand:%(X='%version'; echo ${X%%%%.*})}
%define minor %{expand:%(X=%version; X=${X%%.*}; echo ${X#*.})}
%define bugfix %{expand:%(X='%version'; echo ${X##*.})}
# %%if "%%version" == "%%{get_version dqt5-tools-common}"
# %%def_disable bootstrap
# %%else
%def_enable bootstrap
# %%endif

Group: System/Libraries
Summary: Qt5 - QtTool components
Url: http://qt.io/
License: LGPL-2.1 with Qt-LGPL-exception-1.1 or LGPL-3.0-only

Requires: %name-common

# find librares
%add_findprov_lib_path %_dqt5_libdir

Source: %qt_module-everywhere-src-%version.tar

Source20: assistant.desktop
Source21: designer.desktop
Source22: linguist.desktop
Source23: qdbusviewer.desktop
Source24: qtconfig.desktop

# ALT
Patch10: alt-build-qtconfig.patch
Patch11: alt-runqttools-with-qt5-suffix.patch

# Automatically added by buildreq on Tue Oct 01 2013 (-bi)
# optimized out: elfutils libGL-devel libgst-plugins libdqt5-core libdqt5-dbus libdqt5-gui libdqt5-network libdqt5-opengl libdqt5-printsupport libdqt5-qml libdqt5-quick libdqt5-sql libdqt5-v8 libdqt5-webkit libdqt5-webkitwidgets libdqt5-widgets libdqt5-xml libstdc++-devel pkg-config python-base python3 python3-base dqt5-base-devel dqt5-declarative-devel ruby ruby-stdlibs
#BuildRequires: desktop-file-utils gcc-c++ glibc-devel-static python-module-distribute dqt5-webkit-devel rpm-build-python3 rpm-build-ruby
BuildRequires(pre): rpm-macros-dqt5
# BuildRequires(pre): dqt5-tools-common
#ifnarch %e2k
BuildRequires: clang-devel llvm-devel
#endif
BuildRequires: desktop-file-utils gcc-c++ glibc-devel libicu-devel
%if_enabled qtconfig
BuildRequires: /usr/bin/convert
%endif
BuildRequires: dqt5-base-devel dqt5-declarative-devel-static dqt5-xmlpatterns-devel
#BuildRequires: dqt5-webkit-devel
BuildRequires: libXext-devel libX11-devel
#BuildRequires: gstreamer-devel gst-plugins-devel
BuildRequires: libxslt-devel libudev-devel libgio-devel libsqlite3-devel
BuildRequires: rpm-macros-alternatives
%if_disabled bootstrap
BuildRequires: dqt5-tools
%endif

%description
%summary.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
Requires: dqt5-base-common
BuildArch: noarch
%description common
Common package for %name

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common
Requires: dqt5-base-devel
Requires: %name
Provides: %name-devel-static = %EVR
Obsoletes: %name-devel-static < %EVR
%description devel
%summary.

%package devel-static
Group: Development/KDE and QT
Summary: Development files for %name
BuildArch: noarch
Requires: %name-common
Requires: %name-devel
%description devel-static
%summary.

%package doc
Summary: Document for developing apps which will use Qt5 %qt_module
Group: Development/KDE and QT
Requires: %name-common
%description doc
This package contains documentation for Qt5 %qt_module

%package -n dqt5-assistant
Group: Text tools
Summary: Documentation browser for Qt5
Requires: %name-common
Requires: %name
%description -n dqt5-assistant
%summary.

%package -n dqt5-designer
Group: Development/KDE and QT
Summary: Designer for the Qt5
Requires: %name-common
Requires: %name
Requires: dqt5-base-devel
Provides: dqt5-linguist = %EVR
%description -n dqt5-designer
%summary.

%package -n dqt5-dbus
Group: System/Configuration/Other
Summary: This package contains D-Bus utilities for Qt5
Requires: %name-common
%description -n dqt5-dbus
This package contains D-Bus utilities for Qt5.

%package -n dqt5-qtconfig
Group: System/Configuration/Other
Summary: A configuration tool for Qt5
Requires: %name-common
%description -n dqt5-qtconfig
This package contains a configuration tool for Qt5.

%package -n libdqt5-uitools
Group: System/Libraries
Summary: Qt5 library
Requires: %name-common
%description -n libdqt5-uitools
%summary

%package -n libdqt5-clucene
Group: System/Libraries
Summary: Qt5 library
Requires: %name-common
%description -n libdqt5-clucene
%summary

%package -n libdqt5-designer
Group: System/Libraries
Summary: Qt5 library
Requires: %name-common
Requires: libdqt5-core = %_dqt5_version
%description -n libdqt5-designer
%summary

%package -n libdqt5-designercomponents
Group: System/Libraries
Summary: Qt5 library
Requires: %name-common
Requires: libdqt5-core = %_dqt5_version
%description -n libdqt5-designercomponents
%summary

%package -n libdqt5-help
Group: System/Libraries
Summary: Qt5 library
Requires: %name-common
Requires: libdqt5-core = %_dqt5_version
%description -n libdqt5-help
%summary

%prep
%setup -n %qt_module-everywhere-src-%version
%if_enabled qtconfig
%patch10 -p1
%endif
%patch11 -p1
syncqt.pl-dqt5 -version %version

# don't add rpath
sed -i '/QMAKE_RPATHDIR/d' src/qdoc/qdoc.pro

%build
%define qdoc_found %{expand:%%(if [ -e %_dqt5_bindir/qdoc ]; then echo 1; else echo 0; fi)}

# needed for documentation generation
# when some Qt header include paths
# are specified using '-isystem $path' arguments
%add_optflags -DQDOC_PASS_ISYSTEM

%qmake_dqt5
%make_build
%if %qdoc_found
export QT_HASH_SEED=0
%make docs
%endif

%install
>main.filelist
%install_dqt5
%if %qdoc_found
%make INSTALL_ROOT=%buildroot install_docs ||:
%endif

# fix pc-files
sed -i -e '/^Requires:/s/Qt5UiPlugin//' %buildroot/%_dqt5_libdir/pkgconfig/*.pc

# Add desktop files
desktop-file-install \
  --dir=%buildroot/%_desktopdir \
  --vendor="dqt5" \
  %SOURCE20 %SOURCE21 %SOURCE22 %SOURCE23 \
%if_enabled qtconfig
  %SOURCE24 \
%endif
  #

# install qdbus alternative
QDBUS_ALTPRIO=`printf '%%.2d%%.2d%%.2d%%.2d\n' 0 %major %minor %bugfix`
mkdir -p %buildroot/%_altdir/
cat > %buildroot/%_altdir/qdbus-%_dqt5 <<__EOF__
%_bindir/qdbus %_dqt5_bindir/qdbus $QDBUS_ALTPRIO
__EOF__
cat > %buildroot/%_altdir/qdbusviewer-%_dqt5 <<__EOF__
%_bindir/qdbusviewer %_dqt5_bindir/qdbusviewer $QDBUS_ALTPRIO
__EOF__
mkdir -p %buildroot%dkf5_bindir/
#ln -s `relative %_bindir/qdbus-%_dqt5 %dkf5_bindir/qdbus` %buildroot%dkf5_bindir/qdbus
#ln -s `relative %_bindir/qtpaths-%_dqt5 %dkf5_bindir/qtpaths` %buildroot%dkf5_bindir/qtpaths
for qt_tool in qdbus qtpaths
do
    ln -s `relative %_bindir/${qt_tool}-%_dqt5 %dkf5_bindir/${qt_tool}` %buildroot%dkf5_bindir/${qt_tool}
done

# icons
install -m644 -p -D src/assistant/assistant/images/assistant.png %buildroot/%_iconsdir/hicolor/32x32/apps/assistant-dqt5.png
install -m644 -p -D src/assistant/assistant/images/assistant-128.png %buildroot/%_iconsdir/hicolor/128x128/apps/assistant-dqt5.png
install -m644 -p -D src/designer/src/designer/images/designer.png %buildroot/%_iconsdir/hicolor/128x128/apps/designer-dqt5.png
install -m644 -p -D src/qdbus/qdbusviewer/images/qdbusviewer.png %buildroot/%_iconsdir/hicolor/32x32/apps/qdbusviewer-dqt5.png
install -m644 -p -D src/qdbus/qdbusviewer/images/qdbusviewer-128.png %buildroot/%_iconsdir/hicolor/128x128/apps/qdbusviewer-dqt5.png
%if_enabled qtconfig
convert -resize 32x32 src/qtconfig/images/appicon.png %buildroot/%_iconsdir/hicolor/32x32/apps/qtconfig-dqt5.png
%endif
# linguist icons
for icon in src/linguist/linguist/images/icons/linguist-*-32.png ; do
  size=$(echo $(basename ${icon}) | cut -d- -f2)
  install -p -m644 -D ${icon} %buildroot/%_iconsdir/hicolor/${size}x${size}/apps/linguist-dqt5.png
done

if [ -e %buildroot/%_dqt5_bindir/qdoc ] ; then
cat >>main.filelist <<__EOF__
%_bindir/qdoc*
%_dqt5_bindir/qdoc*
__EOF__
fi

%files common
%_dqt5_datadir/phrasebooks/

%files -f main.filelist
%_bindir/lconvert*
%_bindir/lrelease*
%_bindir/lupdate*
%_bindir/pixeltool*
%_bindir/qcollectiongenerator*
%_bindir/qhelpgenerator*
%_bindir/qtpaths*
%_bindir/qtdiag*
%_bindir/qtplugininfo*
%_bindir/qtattributionsscanner*
%_bindir/qdistancefieldgenerator*
%_bindir/lprodump*
%_dqt5_bindir/lconvert*
%_dqt5_bindir/lrelease*
%_dqt5_bindir/lupdate*
%_dqt5_bindir/pixeltool*
%_dqt5_bindir/qcollectiongenerator*
%_dqt5_bindir/qhelpgenerator*
%_dqt5_bindir/qtpaths*
%_dqt5_bindir/qtdiag*
%_dqt5_bindir/qtplugininfo*
%_dqt5_bindir/qtattributionsscanner*
%_dqt5_bindir/qdistancefieldgenerator*
%_dqt5_bindir/lprodump*
%dkf5_bindir/qtpaths

%if_enabled qtconfig
%files -n dqt5-qtconfig
%_bindir/qtconfig-dqt5
%_dqt5_bindir/qtconfig
%_desktopdir/*qtconfig.desktop
%_iconsdir/hicolor/*/apps/qtconfig*.*
%endif

%files -n dqt5-assistant
%_bindir/assistant-dqt5
%_dqt5_bindir/assistant
%_desktopdir/*assistant.desktop
%_iconsdir/hicolor/*/apps/assistant*.*
%if %qdoc_found
%_dqt5_docdir/qtassistant/
%_dqt5_docdir/qtassistant.qch
%endif

%files -n dqt5-dbus
%exclude %_altdir/qdbus-%_dqt5
%_bindir/qdbus-dqt5
%_dqt5_bindir/qdbus
%dkf5_bindir/qdbus
%exclude %_altdir/qdbusviewer-%_dqt5
%_bindir/qdbusviewer*
%_dqt5_bindir/qdbusviewer*
%_desktopdir/*qdbusviewer.desktop
%_iconsdir/hicolor/*/apps/qdbusviewer*.*

%files -n dqt5-designer
%_bindir/designer*
%_bindir/linguist*
%_dqt5_bindir/linguist*
%_dqt5_bindir/designer*
%_dqt5_plugindir/designer/lib*.so
%_desktopdir/*designer.desktop
%_desktopdir/*linguist.desktop
%_iconsdir/hicolor/*/apps/designer*.*
%_iconsdir/hicolor/*/apps/linguist*.*

%files devel
#%_dqt5_headerdir/QtCLucene/
%_dqt5_headerdir/QtDesigner/
%_dqt5_headerdir/QtDesignerComponents/
%_dqt5_headerdir/QtHelp/
%_dqt5_headerdir/QtUiTools/
%_dqt5_headerdir/QtUiPlugin/
%_dqt5_libdir/libQt*.prl
%_dqt5_libdatadir/libQt*.prl
%_dqt5_libdir/libQt*.so
%_dqt5_libdatadir/libQt*.so
#%_dqt5_libdir/pkgconfig/Qt*CLucene.pc
#%_dqt5_libdir/pkgconfig/Qt*DesignerComponents.pc
%_dqt5_libdir/pkgconfig/Qt*Designer.pc
%_dqt5_libdir/pkgconfig/Qt*Help.pc
%_dqt5_libdir/pkgconfig/Qt*UiPlugin.pc
%_dqt5_archdatadir/mkspecs/modules/*.pri
%_dqt5_libdir/cmake/Qt*/
# devel-static
%_dqt5_libdir/libQt?*.a
%_dqt5_libdatadir/libQt?*.a
%_dqt5_libdir/pkgconfig/Qt?UiTools.pc

%files  devel-static

%files doc
%if %qdoc_found
%_dqt5_docdir/*
%exclude %_dqt5_docdir/qtassistant/
%exclude %_dqt5_docdir/qtassistant.qch
%endif
%_dqt5_examplesdir/*

#%files -n libdqt5-uitools
#%_dqt5_libdir/libQt5UiTools.so.*
#%files -n libdqt5-clucene
#%_dqt5_libdir/libQt5CLucene.so.*
%files -n libdqt5-designer
%_dqt5_libdir/libQt5Designer.so.*
%files -n libdqt5-designercomponents
%_dqt5_libdir/libQt5DesignerComponents.so.*
%files -n libdqt5-help
%_dqt5_libdir/libQt5Help.so.*

%changelog
* Thu Jul 25 2024 Leontiy Volodin <lvol@altlinux.org> 5.15.13-alt0.dde.1
- fork qtbase for separate deepin buildings (ALT #48138)

* Thu Apr 04 2024 Sergey V Turchin <zerg@altlinux.org> 5.15.13-alt1
- new version

* Wed Jan 10 2024 Sergey V Turchin <zerg@altlinux.org> 5.15.12-alt1
- new version

* Wed Nov 22 2023 Sergey V Turchin <zerg@altlinux.org> 5.15.11-alt1
- new version

* Tue Aug 01 2023 Sergey V Turchin <zerg@altlinux.org> 5.15.10-alt2
- update requires (closes: 47087)

* Mon Jul 10 2023 Sergey V Turchin <zerg@altlinux.org> 5.15.10-alt1
- new version

* Wed Apr 26 2023 Sergey V Turchin <zerg@altlinux.org> 5.15.9-alt1
- new version

* Wed Jan 18 2023 Sergey V Turchin <zerg@altlinux.org> 5.15.8-alt1
- new version

* Thu Nov 17 2022 Sergey V Turchin <zerg@altlinux.org> 5.15.7-alt2
- automate bootstrap mode

* Tue Nov 15 2022 Sergey V Turchin <zerg@altlinux.org> 5.15.7-alt1
- new version

* Fri Oct 07 2022 Sergey V Turchin <zerg@altlinux.org> 5.15.6-alt1
- new version

* Tue Aug 16 2022 Sergey V Turchin <zerg@altlinux.org> 5.15.4-alt2
- build docs

* Mon Jul 04 2022 Sergey V Turchin <zerg@altlinux.org> 5.15.4-alt1
- new version

* Tue Sep 21 2021 Sergey V Turchin <zerg@altlinux.org> 5.15.2-alt5
- package empty devel-static package to solve autorebuild tests

* Fri Sep 10 2021 Sergey V Turchin <zerg@altlinux.org> 5.15.2-alt4
- move static libs to devel subpackage (closes: 40884)
- disable LTO

* Mon Sep 06 2021 Sergey V Turchin <zerg@altlinux.org> 5.15.2-alt3
- fix to build with LTO

* Mon Apr 26 2021 Sergey V Turchin <zerg@altlinux.org> 5.15.2-alt2
- build docs

* Mon Jan 11 2021 Sergey V Turchin <zerg@altlinux.org> 5.15.2-alt1
- new version

* Thu Sep 10 2020 Sergey V Turchin <zerg@altlinux.org> 5.15.1-alt1
- new version

* Fri Aug 14 2020 Sergey V Turchin <zerg@altlinux.org> 5.15.0-alt2
- fix run Qt tools

* Wed Jul 08 2020 Sergey V Turchin <zerg@altlinux.org> 5.15.0-alt1
- new version

* Fri Jul 03 2020 Sergey V Turchin <zerg@altlinux.org> 5.12.9-alt2
- build docs

* Mon Jun 22 2020 Sergey V Turchin <zerg@altlinux.org> 5.12.9-alt1
- new version

* Thu Apr 16 2020 Sergey V Turchin <zerg@altlinux.org> 5.12.8-alt2
- build docs

* Thu Apr 09 2020 Sergey V Turchin <zerg@altlinux.org> 5.12.8-alt1
- new version

* Mon Mar 16 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 5.12.7-alt3
- Fixed docs generation

* Wed Mar 11 2020 Sergey V Turchin <zerg@altlinux.org> 5.12.7-alt2
- build docs

* Thu Feb 13 2020 Sergey V Turchin <zerg@altlinux.org> 5.12.7-alt1
- new version

* Mon Dec 16 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.6-alt1
- new version

* Fri Oct 18 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.5-alt2
- build docs

* Mon Oct 07 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.5-alt1
- new version

* Wed Aug 07 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.4-alt2
- fix build requires for e2k

* Mon Jun 24 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.4-alt1
- new version

* Thu Apr 25 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.3-alt1
- new version

* Wed Mar 06 2019 Sergey V Turchin <zerg@altlinux.org> 5.12.2-alt1
- new version

* Thu Dec 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.3-alt1
- new version

* Mon Sep 24 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.2-alt1
- new version

* Thu Aug 16 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.1-alt2
- build docs

* Fri Aug 03 2018 Sergey V Turchin <zerg@altlinux.org> 5.11.1-alt1
- new version

* Thu Jul 12 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.6-alt2
- fix menu items russian translation, icons

* Wed Jun 13 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.6-alt1
- new version

* Tue Apr 17 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.5-alt1
- new version

* Wed Mar 07 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt1.2
- build docs

* Mon Feb 12 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt1.1
- don't build docs

* Thu Jan 25 2018 Sergey V Turchin <zerg@altlinux.org> 5.9.4-alt1
- new version

* Tue Dec 05 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.3-alt1
- new version

* Mon Oct 23 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.2-alt2
- build docs

* Fri Oct 06 2017 Sergey V Turchin <zerg@altlinux.org> 5.9.2-alt1
- new version

* Thu Dec 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.7.1-alt1
- new version

* Fri Oct 21 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.2-alt1.M80P.1
- build for M80P

* Fri Oct 21 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.2-alt2
- add qtpaths to KDE5 PATH

* Sun Oct 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.2-alt0.M80P.1
- build for M80P

* Wed Oct 12 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.2-alt1
- new version

* Mon Jun 27 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.1-alt1
- new version

* Tue May 31 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt3
- hide qdbusviewer from menu

* Thu Mar 31 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt2
- build docs

* Thu Mar 24 2016 Sergey V Turchin <zerg@altlinux.org> 5.6.0-alt1
- new version

* Tue Nov 17 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt2
- fix find qmake

* Thu Oct 15 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.1-alt1
- new version

* Fri Sep 25 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt2
- add alternavices for qdbus and qdbusviewer

* Mon Jul 06 2015 Sergey V Turchin <zerg@altlinux.org> 5.5.0-alt1
- new version

* Tue Jun 09 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.2-alt1
- new version

* Wed Feb 25 2015 Sergey V Turchin <zerg@altlinux.org> 5.4.1-alt1
- new version

* Tue Dec 16 2014 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- new version

* Wed Sep 17 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.2-alt1
- new version

* Fri Jun 27 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt0.M70P.1
- build for M70P

* Wed Jun 25 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.1-alt1
- new version

* Tue Jun 03 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- new version

* Thu Feb 27 2014 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt0.M70P.1
- built for M70P

* Thu Feb 13 2014 Sergey V Turchin <zerg@altlinux.org> 5.2.1-alt1
- new version

* Wed Jan 29 2014 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt5.M70P.1
- built for M70P

* Wed Jan 29 2014 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt6
- fix cmake config file (ALT#29761)

* Tue Jan 28 2014 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt4.M70P.1
- built for M70P

* Tue Jan 28 2014 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt5
- fix paths in cmake config (ALT#29761)

* Tue Nov 26 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt3.M70P.2
- build docs

* Mon Nov 25 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt3.M70P.1
- built for M70P

* Thu Oct 31 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt4
- built qtconfig

* Fri Oct 25 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt3
- built docs

* Wed Oct 23 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt2
- move static libs to separate package

* Mon Sep 30 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt1
- initial build

