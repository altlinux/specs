%def_disable clang
%def_disable tests
%define repo dde-printer

Name: deepin-printer
Version: 1.0.20
Release: alt1

Summary: Printing utility for DDE

License: GPL-3.0+
# src/cppcups/snmp.{c,h}: Apache-2.0
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-printer
Vcs: https://github.com/linuxdeepin/dde-printer.git

Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz
Patch: %name-%version-%release.patch

%if_enabled clang
BuildRequires: clang-devel lld-devel
%else
BuildRequires: gcc-c++
%endif
BuildRequires: dqt5-base-devel
BuildRequires: libcups-devel
BuildRequires: dqt5-tools
BuildRequires: dtk5-widget-devel
BuildRequires: libsmbclient-devel
BuildRequires: libusb-devel
BuildRequires: libgtest-devel
#Requires: icon-theme-hicolor

%description
Graphical interface to configure the printing system for DDE.

%prep
%setup -n %repo-%version
%autopatch -p1

%build
export PATH=%_dqt5_bindir:$PATH
%if_enabled clang
export CC=clang
export CXX=clang++
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif
%qmake_dqt5 \
%if_enabled clang
  QMAKE_STRIP= -spec linux-clang \
%endif
  DEFINES+="VERSION=%version" \
  CONFIG+=nostrip \
  QMAKE_RPATHDIR=%_dqt5_libdir \
  LIB_INSTALL_DIR=%_libdir \
#
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot
%find_lang %repo

%files -f %repo.lang
%doc README.md LICENSE
%_bindir/%repo
%_bindir/%repo-helper
%_datadir/%repo/
%_datadir/%repo-helper/
%_desktopdir/%repo.desktop
%dir %_libdir/deepin-service-manager/
%_libdir/deepin-service-manager/libddeprinter.so*
%dir %_libexecdir/deepin-daemon/
%_libexecdir/deepin-daemon/dde-printer-manager
%dir %_libexecdir/deepin/
%dir %_libexecdir/deepin/dde-printer/
%dir %_libexecdir/deepin/dde-printer/printer-drivers/
%dir %_libexecdir/deepin/dde-printer/printer-drivers/cndrvcups-capt/
%_libexecdir/deepin/dde-printer/printer-drivers/cndrvcups-capt/canon*
%_sysconfdir/dbus-1/system.d/com.deepin.printer.manager.conf
%_datadir/dbus-1/services/com.deepin.print.helper.service
%_datadir/dbus-1/system-services/com.deepin.printer.manager.service
%_iconsdir/hicolor/48x48/apps/%repo.svg
%_datadir/polkit-1/actions/com.deepin.pkexec.devPrinter.policy
%_unitdir/dde-printer-manager.service
%dir %_datadir/deepin-debug-config/
%dir %_datadir/deepin-debug-config/deepin-debug-config.d/
%_datadir/deepin-debug-config/deepin-debug-config.d/dde-printer_debug.json
%dir %_datadir/deepin-log-viewer/
%dir %_datadir/deepin-log-viewer/deepin-log.conf.d/
%_datadir/deepin-log-viewer/deepin-log.conf.d/dde-printer.json
%dir %_datadir/deepin-service-manager/
%dir %_datadir/deepin-service-manager/user/
%_datadir/deepin-service-manager/user/dde-printer.json
%dir %_datadir/deepin-manual/
%dir %_datadir/deepin-manual/manual-assets/
%dir %_datadir/deepin-manual/manual-assets/application/
%dir %_datadir/deepin-manual/manual-assets/application/%repo/
%_datadir/deepin-manual/manual-assets/application/%repo/*.pdf
%_datadir/deepin-manual/manual-assets/application/%repo/print-manager/
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/dde-printer/
%_datadir/dsg/configs/dde-printer/org.deepin.dde.printer.json

%changelog
* Thu Apr 24 2025 Leontiy Volodin <lvol@altlinux.org> 1.0.20-alt1
- New version 1.0.20.
- Added vcs tag.

* Wed May 29 2024 Leontiy Volodin <lvol@altlinux.org> 0.9.21-alt1
- New version 0.9.21.
- Built via separate qt5 instead system (ALT #48138).

* Tue Mar 05 2024 Leontiy Volodin <lvol@altlinux.org> 0.9.20-alt1
- New version 0.9.20.
- Used default compiler versions for easy backporting.
- Applied fixes from master branch.

* Thu Jan 26 2023 Leontiy Volodin <lvol@altlinux.org> 0.9.16-alt2
- Fixed build with googletest 1.13.0.

* Tue Nov 22 2022 Leontiy Volodin <lvol@altlinux.org> 0.9.16-alt1
- New version (0.9.16).

* Thu May 19 2022 Leontiy Volodin <lvol@altlinux.org> 0.9.13-alt1
- New version (0.9.13).

* Wed Jun 30 2021 Leontiy Volodin <lvol@altlinux.org> 0.8.7-alt1
- New version (0.8.7).

* Thu Mar 18 2021 Leontiy Volodin <lvol@altlinux.org> 0.8.5-alt1
- Initial build for ALT Sisyphus.
