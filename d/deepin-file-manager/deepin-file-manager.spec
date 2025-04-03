%define repo dde-file-manager
%define _libexecdir %_prefix/libexec
%define soname 1
%define __builddir BUILD

%def_without clang

Name: deepin-file-manager
Version: 6.5.44
Release: alt2

Summary: Deepin File Manager

License: GPL-3.0-or-later
Group: File tools
Url: https://github.com/linuxdeepin/dde-file-manager
Vcs: git://github.com/linuxdeepin/dde-file-manager.git

Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz
Patch0: deepin-file-manager-6.5.42-alt-fixes-paths.patch
Patch1: deepin-file-manager-6.5.42-alt-fixes-underlinked-elfs.patch
Patch2: deepin-file-manager-6.5.44-alt-options-uos.patch

# /usr/include/dqt6/QtCore/qhash.h:65:33:
# error: static assertion failed:
# The key type must have a qHash overload or a std::hash specialization
ExcludeArch: i586

Provides: %repo = %EVR

BuildRequires(pre): rpm-build-ninja rpm-macros-dqt6
# Automatically added by buildreq on Tue Apr 01 2025
# optimized out: boost-asio-devel boost-devel-headers boost-filesystem-devel cmake cmake-modules dqt6-base-devel dqt6-tools gcc-c++ glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 icu-utils libX11-devel libdde-shell0 libdeepin-pdfium1 libdeepin-qdbus-service0 libdfm6-burn1 libdfm6-io1 libdfm6-mount1 libdouble-conversion3 libdqt5-core libdqt5-dbus libdqt6-concurrent libdqt6-core libdqt6-dbus libdqt6-gui libdqt6-multimedia libdqt6-network libdqt6-opengl libdqt6-printsupport libdqt6-qml libdqt6-qmlmeta libdqt6-qmlmodels libdqt6-qmlworkerscript libdqt6-quick libdqt6-sql libdqt6-svg libdqt6-svgwidgets libdqt6-waylandclient libdqt6-widgets libdqt6-xml libdtk6core-devel libdtk6gui-devel libdtk6log-devel libdtk6widget-devel libfreetype-devel libgio-devel libglvnd-devel libgpg-error libicu-devel libjson-c5 libp11-kit libpng-devel libpolkit-qt6-agent libpolkit-qt6-core libpolkit-qt6-gui libpoppler2-cpp libqt6-core libqt6-gui libsasl2-3 libsecret-devel libssl-devel libstartup-notification libstdc++-devel libwayland-client libwayland-cursor libxcb-devel libxkbcommon-devel pkg-config python3 python3-base qt6-base-devel sh5 vulkan-headers xorg-proto-devel zlib-devel
BuildRequires: dde-dock-devel deepin-shell dqt6-declarative-devel dqt6-multimedia-devel dqt6-svg-devel dqt6-tools-devel dtk6-common-devel libcryptsetup-devel libcups-devel libdde-shell-devel libdeepin-pdfium-devel libdeepin-qdbus-service-devel libdevmapper-devel libdfm6-burn-devel libdfm6-io-devel libdfm6-mount-devel libdmr-devel libdocparser-devel libffmpegthumbnailer-devel libjpeg-devel liblcms2-devel liblucene++-devel libmount-devel libopenjpeg2.0-devel libpcre-devel libpolkit-devel libpolkitqt6-qt6-devel libpoppler-cpp-devel libtag-devel libxcbutil-icccm-devel
BuildRequires: deepin-gettext-tools deepin-desktop-base libfreetype-devel libpng-devel

%if_with clang
BuildRequires: clang-devel lld-devel libstdc++-devel
%else
BuildRequires: gcc-c++
%endif

Requires: libdqt6-gui = %_dqt6_version libdqt6-widgets = %_dqt6_version

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

%package -n libdfm6-base%soname
Summary: Library for %name extensions
Group: System/Libraries

%description -n libdfm6-base%soname
Library for %name extensions.

%package -n libdfm6-base-devel
Summary: Development files for %name extensions
Group: Development/Other

%description -n libdfm6-base-devel
Development files for %name extensions.

%package -n libdfm6-framework%soname
Summary: Library for %name extensions
Group: System/Libraries

%description -n libdfm6-framework%soname
Library for %name extensions.

%package -n libdfm6-framework-devel
Summary: Development files for %name extensions
Group: Development/Other

%description -n libdfm6-framework-devel
Development files for %name extensions.

%package -n deepin-desktop
Summary: Deepin desktop environment - desktop module
Group: Graphical desktop/Other
BuildArch: noarch

%description -n deepin-desktop
Deepin desktop environment - desktop module.

%prep
%setup -n %repo-%version
%autopatch -p1
# fix bad_elf_symbols
sed -e '/stopSpinner/d;' \
    -e '/startSpinner/d;' \
    -i src/plugins/filemanager/dfmplugin-titlebar/views/private/addressbar_p.h
sed -e '/removeCachedMnts/d;' \
    -i src/plugins/filemanager/dfmplugin-workspace/utils/filedatamanager.h

%build
# ninja generates dependency cycle
# [0/2] /usr/bin/cmake -P /usr/src/RPM/BUILD/dde-file-manager-6.5.42/BUILD/CMakeFiles/VerifyGlobs.cmake
# ninja: error: dependency cycle:
# src/dfm-base/libdfm6-base.so ->
# src/dfm-base/libdfm6-base.so.6.5.42 ->
# src/dfm-base/CMakeFiles/dfm6-base.dir/dfm6-base_autogen/mocs_compilation.cpp.o ->
# cmake_object_order_depends_target_dfm6-base ->
# src/dfm-base/devicemanager_interface_qt6.cpp ->
# /usr/src/RPM/BUILD/dde-file-manager-6.5.42/assets/dbus/org.deepin.Filemanager.Daemon.DeviceManager.xml ->
# src/dfm-base/libdfm6-base.so

%define optflags_lto %nil
%if_with clang
export CC=clang
export CXX=clang++
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%else
export CC=gcc
export CXX=g++
%endif
export CPLUS_INCLUDE_PATH=%_includedir/qt6:$CPLUS_INCLUDE_PATH
%DQ6cmake \
    -G "Unix Makefiles" \
    -DCMAKE_MAKE_PROGRAM=make \
    -DLIB_DESTINATION=%_lib \
    -DCMAKE_INSTALL_PREFIX=%_prefix \
    -DCMAKE_INSTALL_SYSCONFDIR=%_sysconfdir \
    -DSYSTEMD_USER_UNIT_DIR=%_userunitdir \
    -DVERSION=%version \
    -DLIB_INSTALL_DIR=%_lib \
    -DDFM_PLUGIN_DIR=%_libdir/%repo/plugins \
#
%make_build -C %__builddir

%install
%makeinstall_std -C %__builddir
chmod +x %buildroot%_sysconfdir/deepin/dde-file-manager/dfm-dlnfs-automount
chmod +x %buildroot%_bindir/dfm-open.sh
chmod +x %buildroot%_bindir/dde-property-dialog

%files
%doc README.md LICENSE
%_bindir/%repo
%_bindir/%repo-daemon
%_bindir/%repo-pkexec
%_bindir/dde-property-dialog
%_bindir/dde-select-dialog-x11
%_bindir/dde-select-dialog-wayland
%_bindir/dde-file-dialog
%_bindir/deepin-diskencrypt-service
%_bindir/file-manager.sh
%_bindir/dfm-open.sh
%_libexecdir/%repo
%_libexecdir/%repo-preview
%_datadir/%repo/
%_desktopdir/%repo.desktop
%_sysconfdir/X11/Xsession.d/99dfm-dlnfs-automount
%dir %_sysconfdir/deepin/
%dir %_sysconfdir/deepin/dde-file-manager/
%_sysconfdir/deepin/dde-file-manager/dfm-dlnfs-automount
%_sysconfdir/polkit-1/localauthority/10-vendor.d/99-dde-file-manager-encrypt.pkla
%_datadir/dbus-1/interfaces/com.deepin.filemanager.filedialog.xml
%_datadir/dbus-1/interfaces/com.deepin.filemanager.filedialogmanager.xml
%_datadir/glib-2.0/schemas/com.deepin.dde.filemanager.gschema.xml
%_datadir/dbus-1/services/com.deepin.filemanager.filedialog.service
%_datadir/dbus-1/services/org.freedesktop.FileManager.service
%_datadir/dbus-1/services/com.deepin.filemanager.filedialog_x11.service
%_datadir/dbus-1/services/com.deepin.filemanager.filedialog_wayland.service
%_datadir/dbus-1/services/org.deepin.Filemanager.Daemon.service
%_datadir/dbus-1/system-services/org.deepin.Filemanager.DiskEncrypt.service
%_datadir/dbus-1/system-services/org.deepin.Filemanager.MountControl.service
%_datadir/dbus-1/system-services/org.deepin.Filemanager.UserShareManager.service
%_datadir/dbus-1/system.d/org.deepin.filemanager.accesscontrol.conf
%_datadir/dbus-1/system.d/org.deepin.filemanager.diskencrypt.conf
%_datadir/dbus-1/system.d/org.deepin.filemanager.mountcontrol.conf
%_datadir/dbus-1/system.d/org.deepin.filemanager.usersharemanager.conf
%_userunitdir/dde-file-manager.service
%dir %_userunitdir/dde-session-initialized.target.wants/
%_userunitdir/dde-session-initialized.target.wants/dde-file-manager.service
%dir %_sysconfdir/systemd/system/deepin-service-group@.service.d/
%_sysconfdir/systemd/system/deepin-service-group@.service.d/dde-file-manage-service-override.conf
%dir %_datadir/deepin/
%_datadir/deepin/%repo/
%_datadir/mime/packages/dtk-dci.xml
%_datadir/polkit-1/actions/com.deepin.pkexec.dde-file-manager.policy
%_datadir/polkit-1/actions/org.deepin.filemanager.accesscontrol.policy
%_datadir/polkit-1/actions/org.deepin.filemanager.diskencrypt.policy
%_datadir/polkit-1/actions/org.deepin.filemanager.usersharemanager.policy
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
%_libdir/%repo/tools/libdfm-upgrade-qt6.so
%_libdir/%repo/plugins/
%dir %_libdir/dde-shell/
%_libdir/dde-shell/org.deepin.ds.desktop.so
%dir %_datadir/dde-shell/
%dir %_datadir/dde-shell/org.deepin.ds.desktop/
%_datadir/dde-shell/org.deepin.ds.desktop/metadata.json
%dir %_libdir/deepin-service-manager/
%_libdir/deepin-service-manager/libdde-filemanager*.so
%dir %_datadir/deepin-service-manager/
%dir %_datadir/deepin-service-manager/other/
%dir %_datadir/deepin-service-manager/system/
%dir %_datadir/deepin-service-manager/user/
%_datadir/deepin-service-manager/other/deepin-diskencrypt-service.json
%_datadir/deepin-service-manager/system/dde-filemanager-accesscontrol.json
%_datadir/deepin-service-manager/system/dde-filemanager-mountcontrol.json
%_datadir/deepin-service-manager/system/dde-filemanager-sharecontrol.json
%_datadir/deepin-service-manager/user/dde-filemanager-textindex.json
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
%_udev_rulesdir/99-dfm-encrypt.rules

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

%files -n libdfm6-base%soname
%_libdir/libdfm6-base.so.%version
%_libdir/libdfm6-base.so.%soname

%files -n libdfm6-base-devel
%_libdir/libdfm6-base.so
%exclude %_pkgconfigdir/dfm6-base.pc
%_includedir/dfm-base/
%_libdir/cmake/dfm6-base/

%files -n libdfm6-framework%soname
%_libdir/libdfm6-framework.so.%version
%_libdir/libdfm6-framework.so.%soname

%files -n libdfm6-framework-devel
%_libdir/libdfm6-framework.so
%exclude %_pkgconfigdir/dfm6-framework.pc
%_includedir/dfm-framework/
%_libdir/cmake/dfm6-framework/

%files -n deepin-desktop
%_desktopdir/dde-computer.desktop
%_desktopdir/dde-trash.desktop
%_desktopdir/dde-home.desktop
%_desktopdir/dde-open.desktop
%_datadir/dbus-1/services/com.deepin.dde.desktop.service

%changelog
* Thu Apr 03 2025 Leontiy Volodin <lvol@altlinux.org> 6.5.44-alt2
- Always use xdg-open (ALT #53701).

* Wed Apr 02 2025 Leontiy Volodin <lvol@altlinux.org> 6.5.44-alt1
- New version 6.5.44.
- Added vcs tag.
- Switched to dqt6.

* Mon Sep 02 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.50-alt1
- New version 6.0.50.
- Built via separate qt5 instead system (ALT #48138).

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
