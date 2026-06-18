%define _libexecdir %_prefix/libexec

Name: deepin-update-ui
Version: 1.0.56
Release: alt1

Summary: DDE UI collection for updating functions

License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-update-ui
VCS: https://github.com/linuxdeepin/deepin-update-ui

# Source-url: %url/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar
Patch0: %name-%version-%release.patch
Patch1: deepin-update-ui-1.0.22-alt-fix-underlinked-libraries.patch
Patch2: deepin-update-ui-1.0.22-alt-fix-unmets.patch

# deepin-control-center is missing on i586
ExcludeArch: i586

# prevent hasher_priv error
%filter_from_requires /\/usr\/bin\/kwin_wayland/d

BuildRequires: cmake dqt6-base-devel libcups-devel dqt6-tools-devel dqt6-declarative-devel dtk6-common-devel libdtk6widget-devel libdde-control-center-devel dde-dock-devel libwayland-client-devel libdqt6-qmlcompiler
BuildRequires: libdqt6-concurrent vulkan-headers

%description
%summary.

%prep
%setup
%patch0 -p1
%patch1 -p2
%patch2 -p2
sed \
 -e '/LIBRARY DESTINATION/s|lib/|${LIB_DESTINATION}/|' \
 -i src/dock-update-plugin/CMakeLists.txt \
 -i src/private-lastore-tray/CMakeLists.txt


%build
%DQ6build \
  -DCMAKE_INSTALL_PREFIX=%_prefix \
  -DCMAKE_INSTALL_SYSCONFDIR=%_sysconfdir \
  -DCMAKE_INSTALL_LIBDIR=%_lib \
  -DLIB_DESTINATION=%_lib \
#

%install
%DQ6install
%find_lang --with-qt --output=%name.lang %name dde-control-center dock-update-plugin private-lastore-tray

%files -f %name.lang
%doc README*.md LICENSE debian/changelog
%_sysconfdir/X11/Xsession.d/98deepin-upgrade-check
%_sysconfdir/xdg/autostart/dde-update-autostart.desktop
%_bindir/dde-rollback
%_bindir/dde-update
%_bindir/rollback_check.sh
%_bindir/run-kwayland-check-wrapper.sh
%_bindir/run-kwayland-check.sh
%_bindir/system_upgrade_check.sh
%dir %_libexecdir/deepin-update-ui/
%_libexecdir/deepin-update-ui/copy-update-log.sh
%_libexecdir/deepin-update-ui/dde-update-env.sh
%dir %_libdir/dde-control-center/
%dir %_libdir/dde-control-center/plugins_v1.0/
%dir %_libdir/dde-control-center/plugins_v1.0/update/
%_libdir/dde-control-center/plugins_v1.0/update/*
%dir %_libdir/dde-dock/
%dir %_libdir/dde-dock/plugins/
%_libdir/dde-dock/plugins/libdock-update-plugin.so
%_libdir/dde-dock/plugins/libprivate-lastore-tray.so
%dir %_datadir/dde-dock/
%dir %_datadir/dde-dock/icons/
%dir %_datadir/dde-dock/icons/dcc-setting/
%_datadir/dde-dock/icons/dcc-setting/dcc-plugin-update.dci
%_datadir/dde-dock/icons/dcc-setting/private-lastore*.svg
%_unitdir/deepin-update-log-copy@.service
%_userunitdir/dde-update-env.service
%_datadir/polkit-1/rules.d/52-deepin-update-ui.rules
%dir %_datadir/dde-session-shell/
%dir %_datadir/dde-session-shell/greeters.d/
%dir %_datadir/dde-session-shell/greeters.d/launch.conf.d/
%_datadir/dde-session-shell/greeters.d/launch.conf.d/98_rollback_conf.json
%_datadir/dde-session-shell/greeters.d/launch.conf.d/99_system_upgrade_conf.json
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/org.deepin.dde.control-center/
%_datadir/dsg/configs/org.deepin.dde.control-center/org.deepin.dde.control-center.update.json
# package outside find_lang
%dir %_datadir/deepin-update-ui/
%dir %_datadir/deepin-update-ui/translations/
%_datadir/deepin-update-ui/translations/dde-rollback_ky@Arab.qm
%_datadir/deepin-update-ui/translations/dde-update_ky@Arab.qm
%dir %_datadir/dde-control-center/
%dir %_datadir/dde-control-center/translations/
%dir %_datadir/dde-control-center/translations/v1.1/
%dir %_datadir/dde-control-center/permission-interfaces/
%_datadir/dde-control-center/permission-interfaces/org.deepin.dcc-update-ui.json
%dir %_datadir/private-lastore-tray/
%dir %_datadir/private-lastore-tray/translations/
%dir %_datadir/dock-update-plugin/
%dir %_datadir/dock-update-plugin/translations/
%_datadir/dock-update-plugin/translations/dock-update-plugin_ky@Arab.qm

%changelog
* Thu Jun 18 2026 Leontiy Volodin <lvol@altlinux.org> 1.0.56-alt1
- New version 1.0.56.

* Wed May 13 2026 Leontiy Volodin <lvol@altlinux.org> 1.0.52-alt1
- New version 1.0.52.

* Tue Apr 21 2026 Leontiy Volodin <lvol@altlinux.org> 1.0.49-alt2
- Fixed build on dde-control-center 6.1.81.

* Tue Apr 14 2026 Leontiy Volodin <lvol@altlinux.org> 1.0.49-alt1
- New version 1.0.49.

* Tue Mar 17 2026 Leontiy Volodin <lvol@altlinux.org> 1.0.46-alt1
- New version 1.0.46.

* Thu Mar 05 2026 Leontiy Volodin <lvol@altlinux.org> 1.0.44-alt1
- New version 1.0.44.
- Fixed build on shrinked dqt6.

* Wed Jan 28 2026 Leontiy Volodin <lvol@altlinux.org> 1.0.41-alt1
- New version 1.0.41.
- Fixed build on dtk 6.7.31.

* Thu Dec 25 2025 Leontiy Volodin <lvol@altlinux.org> 1.0.37-alt1
- New version 1.0.37.

* Thu Nov 20 2025 Leontiy Volodin <lvol@altlinux.org> 1.0.34-alt1
- New version 1.0.34.

* Fri Oct 31 2025 Leontiy Volodin <lvol@altlinux.org> 1.0.32-alt1
- New version 1.0.32.

* Wed Oct 29 2025 Leontiy Volodin <lvol@altlinux.org> 1.0.31-alt1
- New version 1.0.31.

* Wed Sep 24 2025 Leontiy Volodin <lvol@altlinux.org> 1.0.29-alt1
- New version 1.0.29.

* Fri Sep 05 2025 Leontiy Volodin <lvol@altlinux.org> 1.0.27-alt1
- New version 1.0.27.

* Mon Aug 04 2025 Leontiy Volodin <lvol@altlinux.org> 1.0.22-alt1
- Initial build for ALT Sisyphus.
