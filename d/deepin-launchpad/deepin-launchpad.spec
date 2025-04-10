%define repo dde-launchpad

%def_disable clang

Name: deepin-launchpad
Version: 1.0.11
Release: alt1

Summary: Launcher for DDE - next generation

License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-launchpad
Vcs: https://github.com/linuxdeepin/dde-launchpad.git

Provides: %repo = %EVR
Conflicts: deepin-launcher
Obsoletes: deepin-launcher

Source: %url/archive/%version/%repo-%version.tar.gz

BuildRequires(pre): rpm-build-ninja rpm-macros-dqt6
%if_enabled clang
BuildRequires(pre): clang-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires: cmake dtk6-common-devel libappstream-qt6-devel libdtk6gui-devel libgio-devel dqt6-declarative-devel dqt6-svg-devel dqt6-tools-devel libsystemd-devel dqt6-wayland-devel libwayland-egl-devel libwayland-server-devel libdde-shell-devel deepin-shell
BuildRequires: libdqt6-qmlcompiler libdqt6-quickcontrols2

Requires: libdqt6-core = %_dqt6_version libdqt6-waylandclient = %_dqt6_version

%description
%summary.

%prep
%setup -n %repo-%version
sed -i 's|AppStreamQt|AppStreamQt6|' \
  CMakeLists.txt \
  desktopintegration.cpp

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif
%DQ6build

%install
%DQ6install
%find_lang --with-qt %repo

%files -f %repo.lang
%doc README.md
%_bindir/%repo
# package outside find_lang
%dir %_datadir/%repo/
%dir %_datadir/%repo/translations/
%_datadir/%repo/translations/dde-launchpad.qm
# ---
%dir %_datadir/dde-shell/
%_datadir/dde-shell/org.deepin.ds.launchpad/
%_datadir/metainfo/org.deepin.dde.shell.launchpad.appdata.xml
%_userunitdir/org.deepin.dde.Launcher1.service
%_datadir/dbus-1/services/org.deepin.dde.Launcher1.service
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/dde-launchpad/
%_datadir/dsg/configs/dde-launchpad/org.deepin.dde.launchpad.appsmodel.json
%dir %_datadir/dsg/configs/org.deepin.dde.shell/
%_datadir/dsg/configs/org.deepin.dde.shell/org.deepin.ds.launchpad.json
%dir %_libdir/dde-shell/
%_libdir/dde-shell/org.deepin.ds.launchpad.so

%changelog
* Thu Apr 10 2025 Leontiy Volodin <lvol@altlinux.org> 1.0.11-alt1
- New version 1.0.11.
- Added vcs tag and fixed url tag.
- Enabled deepin-shell integration.

* Thu Mar 06 2025 Leontiy Volodin <lvol@altlinux.org> 0.6.12-alt2.1
- Simplified build macros.
- Fixed BuildRequires.

* Wed Oct 02 2024 Leontiy Volodin <lvol@altlinux.org> 0.6.12-alt2
- Built with separate qt6 (ALT #48138).

* Fri May 17 2024 Leontiy Volodin <lvol@altlinux.org> 0.6.12-alt1
- New version 0.6.12.

* Wed May 08 2024 Leontiy Volodin <lvol@altlinux.org> 0.6.9-alt1
- New version 0.6.9.

* Wed May 08 2024 Leontiy Volodin <lvol@altlinux.org> 0.5.0-alt1
- New version 0.5.0.
- Switched to qt6 and dtk6 by upstream.
- No more needed for qt hardlock requires.
- Built with appstream v1.

* Mon Mar 11 2024 Leontiy Volodin <lvol@altlinux.org> 0.4.6-alt2
- Applied improvements for easy rebuilding with appstream v1.

* Fri Mar 01 2024 Leontiy Volodin <lvol@altlinux.org> 0.4.6-alt1
- New version 0.4.6.

* Fri Jan 19 2024 Leontiy Volodin <lvol@altlinux.org> 0.4.3-alt2
- Requires: libqt5-core = %%_qt5_version.

* Wed Jan 17 2024 Leontiy Volodin <lvol@altlinux.org> 0.4.3-alt1
- New version 0.4.3.

* Tue Dec 26 2023 Leontiy Volodin <lvol@altlinux.org> 0.3.0.0.18.caf2-alt1
- Initial build for ALT Sisyphus.
