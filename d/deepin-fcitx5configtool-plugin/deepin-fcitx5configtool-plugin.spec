%define repo dde-fcitx5configtool-plugin
%define _libexecdir %_prefix/libexec

%def_disable clang

Name: deepin-fcitx5configtool-plugin
Version: 6.0.33
Release: alt1

Summary: The input method management plug-in of DDE control center

License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-fcitx5configtool-plugin
Vcs: https://github.com/linuxdeepin/deepin-fcitx5configtool-plugin

Provides: %repo = %EVR

# Source-url: %url/archive/%version/%repo-%version.tar.gz
Source: %repo-%version.tar
Patch: %name-%version-%release.patch

# deepin-control-center
ExcludeArch: i586

BuildRequires(pre): rpm-macros-dqt6 patchelf
%if_enabled clang
BuildRequires(pre): clang-devel lld-devel
%else
BuildRequires(pre): gcc-c++
%endif
# Automatically added by buildreq on Mon Apr 07 2025
# optimized out: at-spi2-atk cmake cmake-modules dqt6-base-common dqt6-base-devel dqt6-tools fcitx5-libs fcitx5-qt-libfcitx5qt5widgets fcitx5-qt-libfcitx5qt6widgets fcitx5-qt-libfcitx5qtdbus fcitx5-qt6 gcc-c++ git-core glibc-kernheaders-generic glibc-kernheaders-x86 icon-naming-utils libEGL-mesa libGLX-mesa libX11-devel libat-spi2-core libcairo-gobject libcap-ng libclang-cpp19 libcrypt-devel libctf-nobfd0 libdde-control-center6 libdouble-conversion3 libdqt6-core libdqt6-dbus libdqt6-gui libdqt6-network libdqt6-printsupport libdqt6-qml libdqt6-widgets libdqt6-xml libdtk6core-devel libdtk6gui-devel libdtk6log-devel libgdk-pixbuf libglvnd-devel libgpg-error libjson-glib libp11-kit libqt5-core libqt5-dbus libqt5-eglfsdeviceintegration libqt5-gui libqt5-network libqt5-widgets libqt5-xcbqpa libqt6-core libqt6-dbus libqt6-eglfsdeviceintegration libqt6-eglfskmssupport libqt6-gui libqt6-network libqt6-opengl libqt6-qml libqt6-qmlmeta libqt6-qmlmodels libqt6-qmlworkerscript libqt6-quick libqt6-waylandclient libqt6-widgets libsasl2-3 libspirv-tools0 libssl-devel libstartup-notification libstdc++-devel libwayland-client libwayland-client-devel libwayland-cursor libwayland-egl libwayland-server libxcb-devel libxcb-render-util libxcbutil-cursor libxcbutil-icccm libxcbutil-icccm-devel libxcbutil-image libxcbutil-keysyms libxkbcommon-devel libxkbcommon-x11 llvm19.1-libs ninja-build pam0_userpass perl pkg-config python3 python3-base sh5 vulkan-headers xorg-proto-devel
BuildRequires: appstream deepin-qt-dbus-factory-devel dqt6-declarative-devel dqt6-svg-devel dqt6-tools-devel libpolkitqt6-dqt6-devel dtk6-common-devel extra-cmake-modules fcitx5-devel fcitx5-qt-devel iso-codes kf6-kitemviews-devel kf6-kwidgetsaddons-devel libcups-devel libdde-control-center-devel libdtk6widget-devel libdqt6-eglfskmsgbmsupport libdqt6-labsqmlmodels libdqt6-xcbqpa libvulkan-devel libxkbfile-devel libicu-devel libdqt6-qmlcompiler
BuildRequires: iso-codes-devel xkeyboard-config-devel

%description
%summary.

%prep
%setup -n %repo-%version
%autopatch -p1

%build
export CPLUS_INCLUDE_PATH=%_includedir/KF6/KWidgetsAddons:%_includedir/Fcitx5Qt5/Fcitx5QtWidgetsAddons:$CPLUS_INCLUDE_PATH
%if_enabled clang
export CC="clang"
export CXX="clang++"
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif
%DQ6build \
#

%install
%DQ6install
# cleanup elfs
patchelf %buildroot%_libdir/dde-control-center/plugins_v1.0/fcitx5configtool/libfcitx5configtool_qml.so --remove-rpath
patchelf %buildroot%_libdir/dde-control-center/plugins_v1.0/fcitx5configtool/libfcitx5configtool_qml.so --add-rpath %_dqt6_libdir
# pack translations
%find_lang --with-qt --output=%name.lang dde-control-center deepin-fcitx5-configtool

%files -f %name.lang
%doc README*.md debian/changelog
%_bindir/kbd-layout-viewer6
%_bindir/fcitx5-helper
%_libexecdir/dcc-fcitx5configtool-exec
%_desktopdir/kbd-layout-viewer6.desktop
%_sysconfdir/xdg/autostart/fcitx5-helper.desktop
%dir %_libdir/dde-control-center/
%dir %_libdir/dde-control-center/plugins_v1.0/
%_libdir/dde-control-center/plugins_v1.0/fcitx5configtool/
# translations
%dir %_datadir/dde-control-center/
%dir %_datadir/dde-control-center/translations/
%dir %_datadir/dde-control-center/translations/v1.1/

%changelog
* Wed Jun 03 2026 Leontiy Volodin <lvol@altlinux.org> 6.0.33-alt1
- New version 6.0.33.

* Tue Apr 21 2026 Leontiy Volodin <lvol@altlinux.org> 6.0.31-alt1
- New version 6.0.31.
- Fixed build on dde-control-center 6.1.81.

* Tue Jan 20 2026 Leontiy Volodin <lvol@altlinux.org> 6.0.24-alt1
- New version 6.0.24.

* Thu Dec 18 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.22-alt1
- New version 6.0.22.

* Mon Oct 27 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.20-alt1
- New version 6.0.20.

* Mon Sep 22 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.17-alt1
- New version 6.0.17.

* Tue Aug 05 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.14-alt1
- New version 6.0.14.
- Updated position for dde-control-center plugins.

* Mon Apr 07 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.7-alt1
- New version 6.0.7.
- Added vcs tag.
- Switched to dqt6.

* Wed Sep 11 2024 Leontiy Volodin <lvol@altlinux.org> 5.0.23-alt1
- New version 5.0.23.
- Built via separate qt5 instead system (ALT #48138).

* Thu Dec 14 2023 Leontiy Volodin <lvol@altlinux.org> 5.0.17.0.4.7355-alt1
- Initial build for ALT Sisyphus.
