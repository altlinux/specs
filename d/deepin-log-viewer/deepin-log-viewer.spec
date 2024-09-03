%define soverlvp 0

%def_disable clang
%def_without library

Name: deepin-log-viewer
Version: 6.1.11
Release: alt2

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
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-ninja
%if_enabled clang
BuildRequires(pre): clang-devel lld-devel
%else
BuildRequires(pre): gcc-c++
%endif
# Automatically added by buildreq on Wed Jan 10 2024
# optimized out: bash5 bashrc boost-devel cmake-modules gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libdouble-conversion3 libdtkcore-devel libdtkgui-devel libglvnd-devel libgpg-error libgsettings-qt libicu-devel libp11-kit libpolkit-qt5-agent libpolkit-qt5-core libpolkit-qt5-gui libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libssl-devel libstartup-notification libstdc++-devel libxerces-c perl perl-Config-Tiny perl-Encode perl-XML-LibXML perl-parent pkg-config python3 python3-base python3-dev qt5-base-devel qt5-tools sh5 zlib-devel
BuildRequires: boost-devel-headers cmake deepin-gettext-tools gsettings-qt-devel libdtkwidget-devel libminizip-devel libpolkitqt5-qt5-devel libsystemd-devel libxerces-c-devel libxlsxwriter-devel python3-module-setuptools qt5-svg-devel qt5-tools-devel rapidjson-devel libgio-qt-devel

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
%patch -p1

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif
export PATH=%_qt5_bindir:$PATH
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_SAFETYTEST_ARG="CMAKE_SAFETYTEST_ARG_OFF" \
    -DAPP_VERSION=%version \
    -DVERSION=%version \
    -DLIB_INSTALL_DIR=%_libdir \
#
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install
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
%_unitdir/timers.target.wants/coredump-reporter.timer
%_unitdir/coredump-reporter.service
%_unitdir/coredump-reporter.timer
%_unitdir/deepin-log-viewer-daemon.service
%dir %_datadir/%name/
%dir %_datadir/%name/translations/
%_datadir/%name/translations/deepin_log_viewer.qm
%_datadir/%name/translations/deepin-log-viewer.qm
%_datadir/%name/translations/deepin-log-viewer_ky@Arab.qm
%dir %_datadir/%name/DocxTemplate/
%_datadir/%name/DocxTemplate/*.dfw
%_datadir/%name/auditRule.conf
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
* Tue Sep 03 2024 Leontiy Volodin <lvol@altlinux.org> 6.1.11-alt2
- Applied usrmerge.

* Mon Jan 22 2024 Leontiy Volodin <lvol@altlinux.org> 6.1.11-alt1
- New version 6.1.11.

* Thu Oct 27 2022 Leontiy Volodin <lvol@altlinux.org> 5.9.13-alt1
- Initial build for ALT Sisyphus.
