%define repo dde-file-manager
%define soname 1

%def_without clang

Name: deepin-file-manager
Version: 6.0.44
Release: alt2

Summary: Deepin File Manager

License: GPL-3.0-or-later
Group: File tools
Url: https://github.com/linuxdeepin/dde-file-manager

Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz

Provides: %repo = %EVR

BuildRequires(pre): rpm-build-ninja rpm-macros-qt5
# Automatically added by buildreq on Thu Oct 26 2023
# optimized out: alt-os-release bash5 bashrc boost-asio-devel boost-devel-headers boost-filesystem-devel cmake cmake-modules gcc-c++ glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 gsettings-qt-devel icu-utils libX11-devel libdeepin-pdfium1 libdfm-burn1 libdfm-io1 libdfm-mount1 libdouble-conversion3 libdtkcore-devel libdtkgui-devel libdtkwidget-devel libffmpegthumbnailer-devel libgio-devel libglvnd-devel libgpg-error libgsettings-qt libicu-devel libisoburn-devel libp11-kit libpolkit-qt5-agent libpolkit-qt5-core libpolkit-qt5-gui libpoppler0-cpp libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-multimedia libqt5-network libqt5-printsupport libqt5-sql libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libsecret-devel libssl-devel libstartup-notification libstdc++-devel libudisks2-devel libxcb-devel pkg-config python3 python3-base python3-dev python3-module-setuptools qt5-base-common qt5-base-devel qt5-x11extras-devel sh5 xorg-proto-devel zlib-devel
BuildRequires: cmake deepin-dock-devel deepin-qt-dbus-factory-devel dtk6-common-devel dtkcore kf5-kcodecs-devel libcryptsetup-devel libdeepin-pdfium-devel libdfm-burn-devel libdfm-io-devel libdfm-mount-devel libdmr-devel libdocparser-devel liblucene++-devel libmount-devel libpcre-devel libpolkit-devel libpolkitqt5-qt5-devel libpoppler-cpp-devel libtag-devel qt5-multimedia-devel qt5-svg-devel qt5-tools qt5-x11extras-devel gsettings-qt-devel libffmpegthumbnailer-devel
BuildRequires: deepin-gettext-tools deepin-desktop-base

%if_with clang
BuildRequires: clang-devel lld-devel libstdc++-devel
%else
BuildRequires: gcc-c++
%endif

Requires: libqt5-gui = %_qt5_version libqt5-widgets = %_qt5_version

%description
File manager front end of Deepin OS.

%package -n lib%repo%soname
Summary: Library for %name
Group: System/Libraries

%description -n lib%repo%soname
Library for %name.

%package -n lib%repo-devel
Summary: Development files for %name
Group: Development/Other

%description -n lib%repo-devel
Development files for %name.

%package -n libdfm-extension%soname
Summary: Library for %name extensions
Group: System/Libraries

%description -n libdfm-extension%soname
Library for %name extensions.

%package -n libdfm-extension-devel
Summary: Development files for %name extensions
Group: Development/Other

%description -n libdfm-extension-devel
Development files for %name extensions.

%package -n libdfm-base%soname
Summary: Library for %name extensions
Group: System/Libraries

%description -n libdfm-base%soname
Library for %name extensions.

%package -n libdfm-base-devel
Summary: Development files for %name extensions
Group: Development/Other

%description -n libdfm-base-devel
Development files for %name extensions.

%package -n libdfm-framework%soname
Summary: Library for %name extensions
Group: System/Libraries

%description -n libdfm-framework%soname
Library for %name extensions.

%package -n libdfm-framework-devel
Summary: Development files for %name extensions
Group: Development/Other

%description -n libdfm-framework-devel
Development files for %name extensions.

%package -n deepin-desktop
Summary: Deepin desktop environment - desktop module
Group: Graphical desktop/Other

%description -n deepin-desktop
Deepin desktop environment - desktop module.

%prep
%setup -n %repo-%version
sed -i 's|lib/dde-dock/plugins/system-trays|${LIB_DESTINATION}/dde-dock/plugins/system-trays|' \
  src/external/dde-dock-plugins/disk-mount/CMakeLists.txt
sed -i 's|include <pcre.h>|include <pcre/pcre.h>|' \
  src/plugins/filemanager/dfmplugin-search/3rdparty/fsearch/database_search.c
sed -i 's|/usr/bin/python|%__python3|' \
  tests/report-daily-check.py

%build
%define optflags_lto %nil
%if_with clang
export CC=clang
export CXX=clang++
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%else
export CC=gcc
export CXX=g++
%endif
export PATH=%_qt5_bindir:$PATH
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_INSTALL_PREFIX=%_prefix \
    -DCMAKE_INSTALL_SYSCONFDIR=%_sysconfdir \
    -DSYSTEMD_USER_UNIT_DIR=%_userunitdir \
    -DVERSION=%version \
    -DLIB_INSTALL_DIR=%_lib \
    -DDFM_PLUGIN_DIR=%_libdir/%repo/plugins \
#
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install
chmod +x %buildroot%_sysconfdir/deepin/dde-file-manager/dfm-dlnfs-automount
chmod +x %buildroot%_bindir/%repo-pkexec
chmod +x %buildroot%_bindir/dde-property-dialog

%files
%doc README.md LICENSE
%_bindir/%repo
%_bindir/%repo-daemon
%_bindir/%repo-pkexec
%_bindir/%repo-server
%_bindir/dde-property-dialog
%_bindir/dde-select-dialog-x11
%_bindir/dde-select-dialog-wayland
%_bindir/dde-file-dialog
%_datadir/%repo/
%_desktopdir/%repo.desktop
%_sysconfdir/X11/Xsession.d/99dfm-dlnfs-automount
%dir %_sysconfdir/deepin/
%dir %_sysconfdir/deepin/dde-file-manager/
%_sysconfdir/deepin/dde-file-manager/dfm-dlnfs-automount
%_datadir/dbus-1/interfaces/com.deepin.filemanager.filedialog.xml
%_datadir/dbus-1/interfaces/com.deepin.filemanager.filedialogmanager.xml
%_datadir/glib-2.0/schemas/com.deepin.dde.dock.module.disk-mount.gschema.xml
%_datadir/glib-2.0/schemas/com.deepin.dde.filemanager.gschema.xml
%_datadir/dbus-1/services/com.deepin.filemanager.filedialog.service
%_datadir/dbus-1/services/org.freedesktop.FileManager.service
%_datadir/dbus-1/system-services/com.deepin.filemanager.daemon.service
%_sysconfdir/dbus-1/system.d/com.deepin.filemanager.daemon.conf
%_unitdir/dde-filemanager-daemon.service
%_userunitdir/dde-filemanager-server.service
%dir %_userunitdir/dde-session-initialized.target.wants/
%_userunitdir/dde-session-initialized.target.wants/dde-filemanager-server.service
%_datadir/dbus-1/services/com.deepin.filemanager.filedialog_x11.service
%_datadir/dbus-1/services/com.deepin.filemanager.filedialog_wayland.service
%_datadir/dbus-1/services/org.deepin.filemanager.server.service
%dir %_datadir/deepin/
%_datadir/deepin/%repo/
%_datadir/mime/packages/dtk-dci.xml
%_datadir/polkit-1/actions/com.deepin.pkexec.dde-file-manager.policy
%_datadir/polkit-1/actions/com.deepin.filemanager.daemon.accesscontrol.policy
%_datadir/polkit-1/actions/com.deepin.filemanager.daemon.sharecontrol.policy
%_datadir/polkit-1/actions/com.deepin.filemanager.vault.policy
%_datadir/applications/context-menus/.readme
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/org.deepin.dde.file-manager/
%_datadir/dsg/configs/org.deepin.dde.file-manager/*.json
%dir %_libdir/dde-dock/
%dir %_libdir/dde-dock/plugins/
%dir %_libdir/dde-dock/plugins/system-trays/
%_libdir/dde-dock/plugins/system-trays/libdde-disk-mount-plugin.so
%dir %_libdir/%repo/
%dir %_libdir/%repo/tools/
%_libdir/%repo/tools/libdfm-upgrade.so
%_libdir/%repo/plugins/
%dir %_datadir/deepin-manual/
%dir %_datadir/deepin-manual/manual-assets/
%dir %_datadir/deepin-manual/manual-assets/application/
%dir %_datadir/deepin-manual/manual-assets/application/%repo/
%_datadir/deepin-manual/manual-assets/application/%repo/file-manager/
%dir %_datadir/deepin-log-viewer/
%dir %_datadir/deepin-log-viewer/deepin-log.conf.d/
%_datadir/deepin-log-viewer/deepin-log.conf.d/*.json
%dir %_datadir/deepin-debug-config/
%dir %_datadir/deepin-debug-config/deepin-debug-config.d/
%_datadir/deepin-debug-config/deepin-debug-config.d/org.deepin.file-manager.json

%files -n lib%repo%soname
%_libdir/lib%repo.so.%version
%_libdir/lib%repo.so.%soname

%files -n lib%repo-devel
%_libdir/lib%repo.so

%files -n libdfm-extension%soname
%_libdir/libdfm-extension.so.%version
%_libdir/libdfm-extension.so.%soname

%files -n libdfm-extension-devel
%_includedir/dfm-extension/
%_libdir/libdfm-extension.so
%exclude %_pkgconfigdir/dfm-extension.pc
%_libdir/cmake/dfm-extension/

%files -n libdfm-base%soname
%_libdir/libdfm-base.so.%version
%_libdir/libdfm-base.so.%soname

%files -n libdfm-base-devel
%_libdir/libdfm-base.so
%exclude %_pkgconfigdir/dfm-base.pc
%_includedir/dfm-base/
%_libdir/cmake/dfm-base/

%files -n libdfm-framework%soname
%_libdir/libdfm-framework.so.%version
%_libdir/libdfm-framework.so.%soname

%files -n libdfm-framework-devel
%_libdir/libdfm-framework.so
%exclude %_pkgconfigdir/dfm-framework.pc
%_includedir/dfm-framework/
%_libdir/cmake/dfm-framework/

%files -n deepin-desktop
%_bindir/dde-desktop
%_desktopdir/dde-computer.desktop
%_desktopdir/dde-trash.desktop
%_desktopdir/dde-home.desktop
%_desktopdir/dde-open.desktop
%_datadir/dbus-1/services/com.deepin.dde.desktop.service

%changelog
* Mon Sep 02 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.44-alt2
- NMU: fixed FTBFS.

* Wed Apr 03 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.44-alt1
- New version 6.0.44.

* Fri Mar 01 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.40-alt1
- New version 6.0.40.

* Fri Jan 19 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.39-alt2
- Requires: libqt5-core = %%_qt5_version.

* Thu Jan 18 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.39-alt1
- New version 6.0.39.

* Mon Dec 04 2023 Leontiy Volodin <lvol@altlinux.org> 6.0.37-alt1
- New version 6.0.37.
- Removed obsoleted patches.
- Cleanup BRs.

* Thu Nov 02 2023 Ivan A. Melnikov <iv@altlinux.org> 5.8.3-alt2.1
- NMU: fix build on riscv64 and loongarch64
  + build with gcc13;
  + no deepin-anything on these architectures.

* Tue Jan 31 2023 Leontiy Volodin <lvol@altlinux.org> 5.8.3-alt2
- Enabled deepin-anything on aarch64.
- Enabled build on armh and ppc64le.

* Fri Dec 30 2022 Leontiy Volodin <lvol@altlinux.org> 5.8.3-alt1.1
- Fixed build with deepin-anything 6.0.3.

* Wed Dec 28 2022 Leontiy Volodin <lvol@altlinux.org> 5.8.3-alt1
- New version (5.8.3).

* Tue Dec 06 2022 Leontiy Volodin <lvol@altlinux.org> 5.8.1-alt1
- New version (5.8.1).

* Wed Nov 09 2022 Leontiy Volodin <lvol@altlinux.org> 5.8.0-alt1
- New version (5.8.0).

* Mon Oct 03 2022 Leontiy Volodin <lvol@altlinux.org> 5.6.4-alt2
- Fixed build with pcre.

* Tue Aug 16 2022 Leontiy Volodin <lvol@altlinux.org> 5.6.4-alt1
- New version (5.6.4).

* Thu Jun 02 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.10-alt2
- Fixed gcc12 build.
- Returned desktop icons.

* Thu Apr 07 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.10-alt1
- New version (5.5.10).
- Changed group tag.

* Tue Mar 22 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.1-alt1
- New version (5.5.1).

* Thu Sep 09 2021 Leontiy Volodin <lvol@altlinux.org> 5.2.0.87-alt5
- Fixed dde-disk-mount-plugin for i586.

* Fri Jun 25 2021 Leontiy Volodin <lvol@altlinux.org> 5.2.0.87-alt4
- Hidden lockscreen checkbox more correctly.

* Thu Jun 24 2021 Leontiy Volodin <lvol@altlinux.org> 5.2.0.87-alt3
- Fixed startup on aarch64 architecture.

* Sat Jun 19 2021 Leontiy Volodin <lvol@altlinux.org> 5.2.0.87-alt2
- Hidden lockscreen checkbox.
- Fixed version tag.

* Mon Feb 15 2021 Leontiy Volodin <lvol@altlinux.org> 5.2.0.87-alt1.1
- Rebuilt with Qt 5.15.2.

* Mon Jan 25 2021 Leontiy Volodin <lvol@altlinux.org> 5.2.0.87-alt1
- New version (5.2.0.87) with rpmgs script.

* Mon Jan 11 2021 Leontiy Volodin <lvol@altlinux.org> 5.2.0.85-alt1
- New version (5.2.0.85) with rpmgs script.

* Sat Dec 26 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.0.82-alt3
- Built with gcc10.

* Tue Dec 22 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.0.82-alt2
- Removed non-working shortcuts from the desktop.

* Mon Dec 07 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.0.82-alt1
- New version (5.2.0.82) with rpmgs script.

* Mon Nov 30 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.0.76-alt2.git7ccae23
- Built from git.

* Tue Nov 10 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.0.76-alt1
- New version (5.2.0.76) with rpmgs script.

* Mon Nov 02 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.0.69-alt1
- New version (5.2.0.69) with rpmgs script.

* Mon Oct 12 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.0.61-alt1
- New version (5.2.0.61) with rpmgs script.
- Removed requires.

* Mon Oct 05 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.0.59-alt1
- New version (5.2.0.59) with rpmgs script.

* Mon Sep 14 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.0.45-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
