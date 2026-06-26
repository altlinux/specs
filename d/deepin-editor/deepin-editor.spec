%def_disable clang

Name: deepin-editor
Version: 6.5.55
Release: alt1

Summary: Simple editor for Linux Deepin

License: GPL-3.0+
Group: Editors
Url: https://github.com/linuxdeepin/deepin-editor
VCS: https://github.com/linuxdeepin/deepin-editor

# Source-url: %url/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar
Patch0: deepin-editor-%version-%release.patch
Patch1: deepin-editor-6.0.16-armh-ppc64le.patch

BuildRequires(pre): rpm-build-ninja rpm-macros-dqt6
# Automatically added by buildreq on Wed Apr 09 2025
# optimized out: at-spi2-atk cmake cmake-modules dqt6-base-common dqt6-base-devel gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 icon-naming-utils icu-utils libEGL-mesa libGLX-mesa libX11-devel libat-spi2-core libcairo-gobject libcap-ng libclang-cpp19 libcrypt-devel libctf-nobfd0 libdouble-conversion3 libdqt6-concurrent libdqt6-core libdqt6-core5compat libdqt6-dbus libdqt6-gui libdqt6-network libdqt6-printsupport libdqt6-svg libdqt6-waylandclient libdqt6-widgets libdqt6-xml libdtk6core-devel libdtk6gui-devel libdtk6log-devel libgdk-pixbuf libglvnd-devel libgpg-error libjson-glib libp11-kit libqt6-core libqt6-dbus libqt6-eglfsdeviceintegration libqt6-eglfskmssupport libqt6-gui libqt6-network libqt6-opengl libqt6-qml libqt6-qmlmeta libqt6-qmlmodels libqt6-qmlworkerscript libqt6-quick libsasl2-3 libspirv-tools0 libssl-devel libstartup-notification libstdc++-devel libwayland-client libwayland-cursor libwayland-egl libwayland-server libxcb-devel libxcb-render-util libxcbutil-cursor libxcbutil-icccm libxcbutil-image libxcbutil-keysyms libxkbcommon-devel libxkbcommon-x11 llvm19.1-libs ninja-build pam0_userpass perl pkg-config python3 python3-base sh5 vulkan-headers
BuildRequires: deepin-qt-dbus-factory-devel dqt6-5compat-devel dqt6-svg-devel dqt6-tools dqt6-tools-devel dtk6-common-devel kf6-kcodecs-devel kf6-syntax-highlighting-devel libchardet-devel libcups-devel libdtk6widget-devel libicu-devel libuchardet-devel libwayland-client-devel
BuildRequires: libdqt6-concurrent vulkan-headers
%if_enabled clang
BuildRequires: clang-devel
BuildRequires: lld-devel
BuildRequires: libstdc++-devel
%else
BuildRequires: gcc-c++
%endif

# Requires: deepin-session-shell deepin-dqt5integration

%description
%summary.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%if_enabled clang
%define optflags_lto -flto=thin
export CC=clang
export CXX=clang++
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif
%DQ6build \
    -DCMAKE_INSTALL_LIBDIR=%_libdir \
#

%install
%DQ6install
%find_lang --with-qt %name

%files -f %name.lang
%doc README.md LICENSE.txt debian/changelog
%_bindir/%name
%dir %_datadir/%name/
%dir %_datadir/%name/themes/
%_datadir/%name/themes/*.theme
# package translations outside %%find_lang
%dir %_datadir/%name/translations/
%_datadir/%name/translations/%name.qm
# ---
%dir %_datadir/%name/org.kde.syntax-highlighing/
%dir %_datadir/%name/org.kde.syntax-highlighing/syntax/
%_datadir/%name/org.kde.syntax-highlighing/syntax/vbscript.xml
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%dir %_datadir/dsg/
%dir %_datadir/dsg/configs/
%dir %_datadir/dsg/configs/org.deepin.editor/
%_datadir/dsg/configs/org.deepin.editor/org.deepin.editor.json
%dir %_datadir/deepin-manual/
%dir %_datadir/deepin-manual/manual-assets/
%dir %_datadir/deepin-manual/manual-assets/application/
%dir %_datadir/deepin-manual/manual-assets/application/%name/
%_datadir/deepin-manual/manual-assets/application/%name/editor/

%changelog
* Fri Jun 26 2026 Leontiy Volodin <lvol@altlinux.org> 6.5.55-alt1
- New version 6.5.55.

* Wed Jun 03 2026 Leontiy Volodin <lvol@altlinux.org> 6.5.52-alt1
- New version 6.5.52.

* Thu Apr 30 2026 Leontiy Volodin <lvol@altlinux.org> 6.5.49-alt1
- New version 6.5.49.

* Fri Apr 17 2026 Leontiy Volodin <lvol@altlinux.org> 6.5.48-alt1
- New version 6.5.48.

* Thu Apr 02 2026 Leontiy Volodin <lvol@altlinux.org> 6.5.47-alt1
- New version 6.5.47.

* Mon Mar 02 2026 Leontiy Volodin <lvol@altlinux.org> 6.5.44-alt1
- New version 6.5.44.

* Mon Jan 26 2026 Leontiy Volodin <lvol@altlinux.org> 6.5.42-alt2
- Fixed build on dtk 6.7.31.

* Wed Dec 17 2025 Leontiy Volodin <lvol@altlinux.org> 6.5.42-alt1
- New version 6.5.42.

* Wed Nov 05 2025 Leontiy Volodin <lvol@altlinux.org> 6.5.40-alt1
- New version 6.5.40.

* Mon Oct 06 2025 Leontiy Volodin <lvol@altlinux.org> 6.5.38-alt1
- New version 6.5.38.

* Wed Apr 09 2025 Leontiy Volodin <lvol@altlinux.org> 6.5.21-alt1
- New version 6.5.21.

* Tue Mar 11 2025 Leontiy Volodin <lvol@altlinux.org> 6.5.16-alt1
- New version 6.5.16.
- Switched to dqt6.

* Wed Jan 15 2025 Leontiy Volodin <lvol@altlinux.org> 6.5.11-alt1
- New version 6.5.11.
- Added vcs tag.

* Thu Dec 12 2024 Leontiy Volodin <lvol@altlinux.org> 6.5.6.0.3.6d5f-alt1
- New version 6.5.6-3-g6d5f7a36.

* Thu Sep 26 2024 Leontiy Volodin <lvol@altlinux.org> 6.5.2-alt1
- New version 6.5.2.

* Wed May 22 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.17-alt2
- Built via separate qt5 instead system (ALT #48138).

* Wed Apr 10 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.17-alt1
- New version 6.0.17.

* Thu Mar 07 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.16-alt1
- New version 6.0.16.
- Requires: libqt5-gui = %%_qt5_version.

* Mon Jan 29 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.15.0.6.660b-alt1
- New version 6.0.15-6-g660b5ad1.

* Tue Jul 25 2023 Leontiy Volodin <lvol@altlinux.org> 6.0.11-alt1
- New version 6.0.11.

* Fri Jun 23 2023 Leontiy Volodin <lvol@altlinux.org> 6.0.10-alt1
- New version 6.0.10.

* Fri Apr 14 2023 Leontiy Volodin <lvol@altlinux.org> 6.0.6-alt1
- New version 6.0.6.

* Thu Mar 23 2023 Leontiy Volodin <lvol@altlinux.org> 6.0.5-alt1
- New version (6.0.5).

* Mon Feb 06 2023 Leontiy Volodin <lvol@altlinux.org> 6.0.0-alt1
- New version (6.0.0).
- Applied fixes from master branch.

* Tue Nov 22 2022 Leontiy Volodin <lvol@altlinux.org> 5.10.40-alt1
- New version (5.10.40).

* Thu May 19 2022 Leontiy Volodin <lvol@altlinux.org> 5.10.23-alt1
- New version (5.10.23).

* Thu Apr 28 2022 Leontiy Volodin <lvol@altlinux.org> 5.10.21-alt1
- New version (5.10.21).

* Fri Mar 18 2022 Leontiy Volodin <lvol@altlinux.org> 5.10.18-alt1
- New version (5.10.18).

* Mon Oct 04 2021 Leontiy Volodin <lvol@altlinux.org> 5.9.14-alt1
- New version (5.9.14).

* Fri Aug 27 2021 Leontiy Volodin <lvol@altlinux.org> 5.9.11-alt1
- New version (5.9.11).
- Checkout from euler into dev branch.

* Wed Jun 30 2021 Leontiy Volodin <lvol@altlinux.org> 5.9.7-alt1
- New version (5.9.7).

* Thu Apr 08 2021 Leontiy Volodin <lvol@altlinux.org> 5.9.0.49-alt1
- New version (5.9.0.49) with rpmgs script.

* Fri Mar 12 2021 Leontiy Volodin <lvol@altlinux.org> 5.9.0.32-alt1
- New version (5.9.0.32) with rpmgs script.

* Wed Dec 30 2020 Leontiy Volodin <lvol@altlinux.org> 5.9.0.16-alt1
- New version (5.9.0.16) with rpmgs script.

* Tue Dec 29 2020 Leontiy Volodin <lvol@altlinux.org> 5.9.0.12-alt1
- New version (5.9.0.12) with rpmgs script.

* Tue Nov 17 2020 Leontiy Volodin <lvol@altlinux.org> 5.9.0.11-alt1
- New version (5.9.0.11) with rpmgs script.

* Fri Oct 23 2020 Leontiy Volodin <lvol@altlinux.org> 5.9.0.6-alt1
- New version (5.9.0.6) with rpmgs script.

* Thu Oct 22 2020 Leontiy Volodin <lvol@altlinux.org> 5.6.37-alt1
- New version (5.6.37) with rpmgs script.

* Fri Oct 16 2020 Leontiy Volodin <lvol@altlinux.org> 5.6.36-alt1
- New version (5.6.36) with rpmgs script.
- Added new BR.

* Tue Aug 18 2020 Leontiy Volodin <lvol@altlinux.org> 5.6.28-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
