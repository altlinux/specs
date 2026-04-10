%define repo dde-clipboard
%def_disable clang

Name: deepin-clipboard
Version: 6.1.27
Release: alt1

Summary: Clipboard for DDE

License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-clipboard
Vcs: https://github.com/linuxdeepin/dde-clipboard

# Source-url: https://github.com/linuxdeepin/dde-clipboard/archive/%version/%repo-%version.tar.gz
Source: %repo-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-dqt6
# Automatically added by buildreq on Wed Mar 26 2025
# optimized out: cmake cmake-modules dqt6-base-devel dqt6-tools dtk6core gcc-c++ glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libdde-shell0 libdouble-conversion3 libdqt6-concurrent libdqt6-core libdqt6-dbus libdqt6-gui libdqt6-network libdqt6-opengl libdqt6-printsupport libdqt6-qml libdqt6-qmlmeta libdqt6-qmlmodels libdqt6-qmlworkerscript libdqt6-quick libdqt6-test libdqt6-waylandclient libdqt6-widgets libdqt6-xml libdtk6core-devel libdtk6gui-devel libdtk6log-devel libgio-qt6_0 libglibmm-devel libglvnd-devel libgpg-error libp11-kit libsasl2-3 libsigc++2-devel libssl-devel libstartup-notification libstdc++-devel libwayland-client libwayland-client-devel libwayland-cursor libwayland-cursor-devel libxcbutil-icccm libxkbcommon-devel ninja-build pkg-config python3 python3-base sh5 vulkan-headers wayland-devel
BuildRequires: dde-dock-devel deepin-shell deepin-tray-loader-devel dqt6-declarative-devel dqt6-tools-devel dqt6-wayland-devel dtk6-common-devel extra-cmake-modules libcups-devel libdde-shell-devel libdtk6widget-devel libgio-qt6-devel libgtest-devel libwayland-egl-devel libwayland-server-devel
BuildRequires: vulkan-headers libdqt6-test libdqt6-concurrent
BuildRequires: libsystemd-devel
%if_enabled clang
BuildRequires: clang-devel
%else
BuildRequires: gcc-c++
%endif

Requires: libdqt6-waylandclient = %_dqt6_version

%description
%summary.

%prep
%setup -n %repo-%version
%patch -p1
sed '/DESTINATION/s|lib/dde-dock/plugins|%_lib/dde-dock/plugins|' \
  -i CMakeLists.txt

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
%doc LICENSE README.md debian/changelog
%_bindir/%{repo}*
%_datadir/dbus-1/services/org.deepin.dde.Clipboard1.service
%_datadir/dbus-1/services/org.deepin.dde.ClipboardLoader1.service
%_datadir/dbus-1/services/org.deepin.dde.daemon.Clipboard1.service
%_userunitdir/%repo-daemon.service
%_userunitdir/%repo.service
%dir %_userunitdir/dde-session-initialized.target.wants/
%_userunitdir/dde-session-initialized.target.wants/dde-clipboard.service
%dir %_datadir/dde-dock/
%dir %_datadir/dde-dock/icons/
%dir %_datadir/dde-dock/icons/dcc-setting/
%_datadir/dde-dock/icons/dcc-setting/clipboard.svg
%_datadir/dde-dock/icons/dcc-setting/dcc-clipboard.dci
%dir %_libdir/dde-dock/
%dir %_libdir/dde-dock/plugins/
%_libdir/dde-dock/plugins/libdock-clipboard-plugin.so
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/org.deepin.dde.clipboard/
%_datadir/dsg/configs/org.deepin.dde.clipboard/org.deepin.dde.clipboard.json
# translations
%dir %_datadir/%repo/
%dir %_datadir/%repo/translations/
%_datadir/%repo/translations/dde-clipboard.qm
%_datadir/%repo/translations/dde-clipboard_es_419.qm
%_datadir/%repo/translations/dde-clipboard_ky@Arab.qm

%changelog
* Fri Apr 10 2026 Leontiy Volodin <lvol@altlinux.org> 6.1.27-alt1
- New version 6.1.27.

* Wed Apr 01 2026 Leontiy Volodin <lvol@altlinux.org> 6.1.26-alt1
- New version 6.1.26.

* Fri Feb 27 2026 Leontiy Volodin <lvol@altlinux.org> 6.1.22-alt1
- New version 6.1.22.

* Thu Jan 22 2026 Leontiy Volodin <lvol@altlinux.org> 6.1.20-alt1
- New version 6.1.20.

* Thu Dec 25 2025 Leontiy Volodin <lvol@altlinux.org> 6.1.18-alt1
- New version 6.1.18.

* Thu Nov 13 2025 Leontiy Volodin <lvol@altlinux.org> 6.1.16-alt1
- New version 6.1.16.

* Fri Oct 31 2025 Leontiy Volodin <lvol@altlinux.org> 6.1.15-alt1
- New version 6.1.15.

* Mon Oct 27 2025 Leontiy Volodin <lvol@altlinux.org> 6.1.13-alt1
- New version 6.1.13.

* Fri Aug 29 2025 Leontiy Volodin <lvol@altlinux.org> 6.1.11-alt1
- New version 6.1.11.

* Thu Jul 17 2025 Leontiy Volodin <lvol@altlinux.org> 6.1.10-alt1
- New version 6.1.10.

* Wed Mar 26 2025 Leontiy Volodin <lvol@altlinux.org> 6.1.6-alt1
- New version 6.1.6.
- Added vcs tag.
- Switched to dqt6.

* Wed May 29 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.9-alt1
- New version 6.0.9.
- Built via separate qt5 instead system (ALT #48138).

* Fri Dec 15 2023 Leontiy Volodin <lvol@altlinux.org> 6.0.7-alt1
- New version 6.0.7.
- Cleanup BRs.

* Fri Jan 20 2023 Leontiy Volodin <lvol@altlinux.org> 5.4.25-alt1
- New version (5.4.25).

* Tue Nov 08 2022 Leontiy Volodin <lvol@altlinux.org> 5.4.24-alt1
- New version (5.4.24).

* Fri Oct 07 2022 Leontiy Volodin <lvol@altlinux.org> 5.4.23-alt1
- New version (5.4.23).

* Mon Sep 12 2022 Leontiy Volodin <lvol@altlinux.org> 5.4.20-alt1
- New version (5.4.20).
- Built via cmake instead qmake.

* Tue May 18 2021 Leontiy Volodin <lvol@altlinux.org> 5.3.16-alt1
- New version (5.3.16) with rpmgs script.

* Tue Apr 13 2021 Leontiy Volodin <lvol@altlinux.org> 5.3.15-alt1
- New version (5.3.15) with rpmgs script.

* Fri Mar 19 2021 Leontiy Volodin <lvol@altlinux.org> 5.3.11-alt1
- Initial build for ALT Sisyphus.
