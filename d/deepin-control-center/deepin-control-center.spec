%define _libexecdir %_prefix/libexec
%define sover 6

%def_disable clang

%define _cmake__builddir BUILD
%define repo dde-control-center

Name: deepin-control-center
Version: 6.1.96
Release: alt1

Summary: New control center for Linux Deepin

License: GPL-3.0-or-later and MIT
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-control-center
Vcs: https://github.com/linuxdeepin/dde-control-center

# Source-url: https://github.com/linuxdeepin/dde-control-center/archive/%version/%repo-%version.tar.gz
Source: %repo-%version.tar
Patch0: %name-%version-%release.patch
Patch1: deepin-control-center-6.1.4-alt-qch.patch
Patch2: deepin-control-center-6.1.40-alt-fixes-underlinked-libs.patch

#FAILED: src/plugin-mouse/CMakeFiles/mouse.dir/mouse_autogen/OYYSJO5W5K/qrc_mouse.cpp.o
#virtual memory exhausted: Cannot allocate memory
ExcludeArch: i586

BuildRequires(pre): rpm-macros-dqt6 patchelf
BuildRequires: cmake deepin-gettext-tools doxygen libdeepin-pw-check-devel dtk6-common-devel libdtk6widget-devel libpolkitqt6-dqt6-devel dqt6-declarative-devel dqt6-tools-devel dqt6-multimedia-devel dqt6-svg-devel dqt6-wayland-devel libdqt6-qmlcompiler libgtest-devel libsystemd-devel treeland-protocols libwayland-egl-devel libwayland-server-devel libdareader-devel libdde-shell-devel deepin-shell libicu-devel wlr-protocols libffmpegthumbnailer-devel
BuildRequires: vulkan-headers libdqt6-concurrent libdqt6-test libdqt6-wlshellintegration
%if_enabled clang
BuildRequires: clang-devel lld-devel
%else
BuildRequires: gcc-c++
%endif

Requires: libdqt6-gui = %_dqt6_version libdqt6-waylandclient = %_dqt6_version

%description
New control center for Linux Deepin.

%package -n lib%repo%sover
Summary: Library for %name
Group: System/Libraries
Requires: libdqt6-qmlmodels = %_dqt6_version

%description -n lib%repo%sover
This package provides library for %name.

%package -n lib%repo-devel
Summary: %summary
Group: Development/C++
Provides: %name-devel
Obsoletes: %name-devel

%description -n lib%repo-devel
This package provides development files for %name.

%prep
%setup -n %repo-%version
%autopatch -p1
# We do not use dpkg and deepinid.
sed -e '/add_subdirectory(src\/plugin-privacy)/d;' \
    -e '/add_subdirectory(src\/plugin-deepinid)/d;' \
    -i CMakeLists.txt

%build
export CPLUS_INCLUDE_PATH=%_dqt6_headerdir/QtXkbCommonSupport/%{_dqt6_version}:$CPLUS_INCLUDE_PATH
export SYSTYPE=Desktop
%if_enabled clang
export CC="clang"
export CXX="clang++"
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif
%DQ6build \
  -DCMAKE_INSTALL_LIBDIR=%_libdir \
  -DDCC_PLUGINS_INSTALL_DIR=%_lib/dde-control-center/plugins_v1.0 \
  -DDISABLE_AUTHENTICATION=ON \
  -DDISABLE_UPDATE=ON \
  -DDISABLE_SOUND_ADVANCED=ON \
#

%install
%DQ6install

# cleanup broken rpaths in elfs
patchelf %buildroot%_libdir/dde-control-center/plugins_v1.0/dock/dock.so --shrink-rpath --allowed-rpath-prefixes %_dqt6_libdir
patchelf %buildroot%_libdir/dde-control-center/plugins_v1.0/display/display.so --shrink-rpath --allowed-rpath-prefixes %_dqt6_libdir
patchelf %buildroot%_libdir/dde-control-center/plugins_v1.0/notification/notification.so --shrink-rpath --allowed-rpath-prefixes %_dqt6_libdir
patchelf %buildroot%_libdir/dde-control-center/plugins_v1.0/blueTooth/blueTooth.so --shrink-rpath --allowed-rpath-prefixes %_dqt6_libdir
patchelf %buildroot%_libdir/dde-control-center/plugins_v1.0/wacom/wacom.so --shrink-rpath --allowed-rpath-prefixes %_dqt6_libdir
patchelf %buildroot%_libdir/dde-control-center/plugins_v1.0/datetime/datetime.so --shrink-rpath --allowed-rpath-prefixes %_dqt6_libdir
patchelf %buildroot%_libdir/dde-control-center/plugins_v1.0/touchscreen/touchscreen.so --shrink-rpath --allowed-rpath-prefixes %_dqt6_libdir
patchelf %buildroot%_libdir/dde-control-center/plugins_v1.0/commonInfo/commonInfo.so --shrink-rpath --allowed-rpath-prefixes %_dqt6_libdir
patchelf %buildroot%_libdir/dde-control-center/plugins_v1.0/systemInfo/systemInfo.so --shrink-rpath --allowed-rpath-prefixes %_dqt6_libdir
patchelf %buildroot%_libdir/dde-control-center/plugins_v1.0/keyboard/keyboard.so --shrink-rpath --allowed-rpath-prefixes %_dqt6_libdir
patchelf %buildroot%_libdir/dde-control-center/plugins_v1.0/personalization/personalization.so --shrink-rpath --allowed-rpath-prefixes %_dqt6_libdir
patchelf %buildroot%_libdir/dde-control-center/plugins_v1.0/mouse/mouse.so --shrink-rpath --allowed-rpath-prefixes %_dqt6_libdir
patchelf %buildroot%_libdir/dde-control-center/plugins_v1.0/power/power.so --shrink-rpath --allowed-rpath-prefixes %_dqt6_libdir
patchelf %buildroot%_libdir/dde-control-center/plugins_v1.0/defaultapp/defaultapp.so --shrink-rpath --allowed-rpath-prefixes %_dqt6_libdir
patchelf %buildroot%_libdir/dde-control-center/plugins_v1.0/sound/sound.so --shrink-rpath --allowed-rpath-prefixes %_dqt6_libdir
patchelf %buildroot%_libdir/dde-control-center/plugins_v1.0/accounts/accounts.so --shrink-rpath --allowed-rpath-prefixes %_dqt6_libdir

# package translations
%find_lang --with-qt %repo

%files -f %repo.lang
%doc LICENSE README.md debian/changelog
%_bindir/%repo
%dir %_libexecdir/deepin/
%_libexecdir/deepin/%repo
%_desktopdir/org.deepin.dde.control-center.desktop
%_datadir/metainfo/org.deepin.dde.controlcenter.metainfo.xml
%_datadir/dbus-1/services/org.deepin.dde.ControlCenter1.service
%dir %_libdir/%repo/
%_libdir/%repo/plugins_v1.0/
%dir %_libdir/dde-grand-search-daemon/
%dir %_libdir/dde-grand-search-daemon/plugins/
%dir %_libdir/dde-grand-search-daemon/plugins/searcher/
%_libdir/dde-grand-search-daemon/plugins/searcher/org.deepin.dde-grand-search.dde-control-center-setting.conf
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/org.deepin.dde.control-center/
%_datadir/dsg/configs/org.deepin.dde.control-center/org.deepin.dde.control-center*.json
%_datadir/dsg/configs/org.deepin.region-format.json
%dir %_datadir/%repo/
%_userunitdir/org.deepin.dde.control-center.service
%dir %_datadir/deepin-debug-config/
%dir %_datadir/deepin-debug-config/deepin-debug-config.d/
%_datadir/deepin-debug-config/deepin-debug-config.d/org.deepin.dde.control-center.json
%dir %_datadir/deepin-log-viewer/
%dir %_datadir/deepin-log-viewer/deepin-log.conf.d/
%_datadir/deepin-log-viewer/deepin-log.conf.d/org.deepin.dde.control-center.json
# package outside find_lang
%dir %_datadir/%repo/translations/
%dir %_datadir/%repo/translations/v1.1/
%_datadir/%repo/translations/v1.1/dde-control-center_ky@Arab.qm

%files -n lib%repo%sover
%_libdir/lib%repo.so.%{sover}*

%files -n lib%repo-devel
%_libdir/lib%repo.so
%dir %_libdir/cmake/DdeControlCenter/
%_libdir/cmake/DdeControlCenter/DdeControlCenter*.cmake
%_includedir/%repo/

%changelog
* Fri Jun 26 2026 Leontiy Volodin <lvol@altlinux.org> 6.1.96-alt1
- New version 6.1.96.

* Mon Jun 22 2026 Leontiy Volodin <lvol@altlinux.org> 6.1.95-alt1
- New version 6.1.95.

* Fri Apr 17 2026 Leontiy Volodin <lvol@altlinux.org> 6.1.81-alt1
- New version 6.1.81.

* Thu Feb 26 2026 Leontiy Volodin <lvol@altlinux.org> 6.1.64-alt2
- Fixed build on shrinked dqt6.

* Thu Dec 25 2025 Leontiy Volodin <lvol@altlinux.org> 6.1.64-alt1
- New version 6.1.64.

* Thu Nov 13 2025 Leontiy Volodin <lvol@altlinux.org> 6.1.56-alt1
- New version 6.1.56.
- Built with polkit-qt6 for DDE instead system.

* Mon Sep 15 2025 Leontiy Volodin <lvol@altlinux.org> 6.1.47-alt1
- New version 6.1.47.

* Mon Aug 04 2025 Leontiy Volodin <lvol@altlinux.org> 6.1.40-alt1
- New version 6.1.40.
- Fixed plugin detection.

* Mon Jul 21 2025 Leontiy Volodin <lvol@altlinux.org> 6.1.38-alt1
- New version 6.1.38.

* Thu Jun 26 2025 Leontiy Volodin <lvol@altlinux.org> 6.1.32-alt2
- Fixed underlinked accounts plugin.

* Wed Jun 25 2025 Leontiy Volodin <lvol@altlinux.org> 6.1.32-alt1
- New version 6.1.32.

* Wed May 07 2025 Leontiy Volodin <lvol@altlinux.org> 6.1.23-alt1
- New version 6.1.23.

* Tue Apr 08 2025 Leontiy Volodin <lvol@altlinux.org> 6.1.19-alt1
- New version 6.1.19.
- Added vcs tag.
- Switched to dqt6.

* Mon Sep 02 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.54-alt1
- New version 6.0.54.
- Built via separate qt5 instead system (ALT #48138).

* Mon Sep 02 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.47-alt3
- NMU: fixed FTBFS.

* Mon Apr 01 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.47-alt2
- Fixed the path to the qt5 qch file.

* Mon Apr 01 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.47-alt1
- New version 6.0.47.

* Thu Feb 01 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.44-alt1
- New version 6.0.44.

* Thu Jan 25 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.43-alt1
- New version 6.0.43.
- Fixed license tag.

* Sat Dec 02 2023 Leontiy Volodin <lvol@altlinux.org> 6.0.35-alt1
- New version 6.0.35.
- Cleanup spec and BRs.
- Removed binding to KF5.

* Thu Nov 02 2023 Ivan A. Melnikov <iv@altlinux.org> 5.6.3-alt1.1
- NMU: Cleanup usage of %%K5* macros (fixes FTBFS).

* Wed Jan 11 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.3-alt1
- New version (5.6.3).
- Cleanup spec.

* Wed Dec 14 2022 Leontiy Volodin <lvol@altlinux.org> 5.6.1-alt1
- New version (5.6.1).

* Mon Oct 17 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.157-alt1
- New version (5.5.157).

* Tue Sep 13 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.149-alt1
- New version (5.5.149).

* Mon Aug 29 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.144-alt1
- New version (5.5.144).

* Fri Jun 03 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.34-alt2
- Fixed build with new dtkcommon.

* Wed Jun 01 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.34-alt1
- New version (5.5.34).

* Fri Apr 22 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.16.2-alt1
- New version (5.5.16.2).
- Built with deepin-pw-check again (without cracklib).

* Wed Aug 25 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.70-alt1
- New version (5.4.70).
- Remove deepin-pw-check from BuildRequires.

* Thu Jul 08 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.47-alt2.git1362dfe
- Fixed build with libgmock.so.1.11.0.

* Wed Jun 30 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.47-alt1.git1362dfe
- Fixed version tag.

* Fri Jun 25 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.23-alt3.git1362dfe
- Temporarily hidden the widget to set the lockscreen timeout.

* Thu Jun 24 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.23-alt2.git1362dfe
- Build git snapshot.
- Disabled General Settings.

* Tue May 18 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.23-alt1
- New version (5.4.23) with rpmgs script.

* Fri Apr 09 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.17-alt2
- Fixed build with dtk 5.4.13.

* Tue Apr 06 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.17-alt1
- New version (5.4.17) with rpmgs script (thanks archlinux for the patch).

* Wed Mar 24 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.9-alt1
- New version (5.4.9) with rpmgs script.

* Tue Jan 12 2021 Leontiy Volodin <lvol@altlinux.org> 5.3.0.82-alt1
- New version (5.3.0.82) with rpmgs script.

* Mon Nov 30 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.68-alt1
- New version (5.3.0.68) with rpmgs script.

* Fri Oct 09 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.44-alt1
- New version (5.3.0.44) with rpmgs script.

* Mon Aug 31 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.18-alt1
- Initial build for ALT Sisyphus (thanks fedora and archlinux for this spec).
