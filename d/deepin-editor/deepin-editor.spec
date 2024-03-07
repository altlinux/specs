%def_disable clang

Name: deepin-editor
Version: 6.0.16
Release: alt1

Summary: Simple editor for Linux Deepin

License: GPL-3.0+
Group: Editors
Url: https://github.com/linuxdeepin/deepin-editor

Source: %url/archive/%version/%name-%version.tar.gz
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-ninja rpm-macros-qt5
# Automatically added by buildreq on Mon Jan 29 2024
# optimized out: bash5 bashrc cmake-modules gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 icu-utils libdouble-conversion3 libdtkcore-devel libdtkgui-devel libglvnd-devel libgpg-error libgsettings-qt libicu-devel libp11-kit libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libssl-devel libstartup-notification libstdc++-devel pkg-config python3 python3-base python3-dev qt5-base-devel sh5
BuildRequires: cmake deepin-qt-dbus-factory-devel kf5-kcodecs-devel kf5-syntax-highlighting-devel libchardet-devel libdtkwidget-devel libuchardet-devel qt5-svg-devel qt5-tools
%if_enabled clang
BuildRequires: clang-devel
BuildRequires: lld-devel
BuildRequires: libstdc++-devel
%else
BuildRequires: gcc-c++
%endif

# Requires: deepin-session-shell deepin-qt5integration
Requires: libqt5-gui = %_qt5_version

%description
%summary.

%prep
%setup
%autopatch -p1

%build
export PATH=%_qt5_bindir:$PATH
%if_enabled clang
%define optflags_lto -flto=thin
export CC=clang
export CXX=clang++
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_INSTALL_LIBDIR=%_libdir \
#
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install
%find_lang --with-qt %name

%files -f %name.lang
%doc README.md LICENSE.txt
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
