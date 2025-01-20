%define soverlvp 0

%def_disable clang
%def_without library

Name: deepin-log-viewer
Version: 6.5.6
Release: alt1

Summary: System log viewer for Deepin

License: GPL-3.0-or-later
# 3rdparty/tmpfileplus/: MPL-2.0
# 3rdparty/minizip/: Zlib and Info-ZIP
# 3rdparty/md5/: Public-domain
# 3rdparty/libxlsxwriter/: GPL and MIT and BSD-2-Clause and BSD-3-Clause and Public-domain and Zlib and MPL-2.0
# 3rdparty/DocxFactory/: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-log-viewer

Source: %url/archive/%version/%name-%version.tar.gz
#Patch1: deepin-log-viewer-6.1.17-opensuse-use-system-xlsxwriter.patch
#Patch2: deepin-log-viewer-6.1.17-alt-use-system-minizip.patch
Patch3: deepin-log-viewer-6.1.17-alt-fix-pkgconfig.patch

BuildRequires(pre): rpm-build-ninja rpm-macros-dqt6
%if_enabled clang
BuildRequires(pre): clang-devel lld-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires: boost-devel-headers cmake deepin-gettext-tools dtk6-common-devel libdtk6widget-devel libminizip-devel libsystemd-devel libxerces-c-devel libxlsxwriter-devel python3-module-setuptools dqt6-svg-devel dqt6-tools-devel dqt6-5compat-devel rapidjson-devel libpolkitqt6-qt6-devel

%description
%summary.

%if_with library
%package -n liblogviewerplugin%soverlvp
Summary: logviewerplugin library for %name
Group: System/Libraries

%description -n liblogviewerplugin%soverlvp
This package provides logviewerplugin library for %name.

%package -n liblogviewerplugin-devel
Summary: development files for logviewerplugin
Group: Development/C++

%description -n liblogviewerplugin-devel
This package provides development files for logviewerplugin.
%endif

%prep
%setup
%autopatch -p1
sed -i 's|/lib/qt${QT_VERSION_MAJOR}/bin/lrelease|%_dqt6_bindir/lrelease|' \
  cmake/translation-generate.cmake

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif
export CPLUS_INCLUDE_PATH=$CPLUS_INCLUDE_PATH:%_includedir/qt6
export LC_ALL=C.UTF-8
%DQ6build \
  -DQT_LRELEASE=%_dqt6_bindir/lrelease \
  -DCMAKE_SAFETYTEST_ARG="CMAKE_SAFETYTEST_ARG_OFF" \
  -DAPP_VERSION=%version \
  -DVERSION=%version \
  -DLIB_INSTALL_DIR=%_libdir \
#

%install
%DQ6install
%find_lang --with-qt %name
chmod +x %buildroot%_bindir/deepin-logger

%if_without library
rm -rf %buildroot%_libdir/liblogviewerplugin.so*
rm -rf %buildroot%_includedir/liblogviewerplugin/
rm -rf %buildroot%_pkgconfigdir/liblogviewerplugin.pc
%endif

%files -f %name.lang
%doc README.md LICENSE.txt
%_bindir/*
%_userunitdir/coredump-reporter.service
%_userunitdir/coredump-reporter.timer
%_unitdir/deepin-log-viewer-daemon.service
%dir %_datadir/%name/
%dir %_datadir/%name/translations/
%_datadir/%name/translations/deepin_log_viewer.qm
%_datadir/%name/translations/deepin-log-viewer.qm
%_datadir/%name/translations/deepin-log-viewer_ky@Arab.qm
%dir %_datadir/%name/DocxTemplate/
%_datadir/%name/DocxTemplate/*.dfw
%_datadir/%name/auditRule.conf
%dir %_libexecdir/deepin-daemon/
%_libexecdir/deepin-daemon/log-view-service
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/dbus-1/system-services/com.deepin.logviewer.service
%_datadir/dbus-1/system.d/com.deepin.logviewer.conf
%_datadir/polkit-1/actions/com.deepin.pkexec.logViewer*.policy
%_datadir/glib-2.0/schemas/com.deepin.log.viewer.gschema.xml
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/org.deepin.log.viewer/
%_datadir/dsg/configs/org.deepin.log.viewer/org.deepin.log.viewer.json
%dir %_datadir/deepin-debug-config/
%dir %_datadir/deepin-debug-config/deepin-debug-config.d/
%_datadir/deepin-debug-config/deepin-debug-config.d/org.deepin.log.viewer.json
%dir %_datadir/%name/deepin-log.conf.d/
%_datadir/%name/deepin-log.conf.d/deepin-log-viewer.json
%dir %_datadir/deepin-manual/
%dir %_datadir/deepin-manual/manual-assets/
%dir %_datadir/deepin-manual/manual-assets/application/
%dir %_datadir/deepin-manual/manual-assets/application/%name/
%_datadir/deepin-manual/manual-assets/application/%name/log-viewer/

%if_with library
%files -n liblogviewerplugin%soverlvp
%_libdir/liblogviewerplugin.so.%{soverlvp}*

%files -n liblogviewerplugin-devel
%_includedir/liblogviewerplugin/
%_libdir/liblogviewerplugin.so
%_pkgconfigdir/liblogviewerplugin.pc
%endif

%changelog
* Mon Jan 20 2025 Leontiy Volodin <lvol@altlinux.org> 6.5.6-alt1
- New version 6.5.6.
- Switched to dqt6.

* Tue Sep 03 2024 Leontiy Volodin <lvol@altlinux.org> 6.1.17-alt1
- New version 6.1.17.
- Built via separate qt5 instead system (ALT #48138).

* Tue Sep 03 2024 Leontiy Volodin <lvol@altlinux.org> 6.1.11-alt2
- Applied usrmerge.

* Mon Jan 22 2024 Leontiy Volodin <lvol@altlinux.org> 6.1.11-alt1
- New version 6.1.11.

* Thu Oct 27 2022 Leontiy Volodin <lvol@altlinux.org> 5.9.13-alt1
- Initial build for ALT Sisyphus.
