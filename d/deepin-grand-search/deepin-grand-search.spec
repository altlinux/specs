%define repo dde-grand-search

%def_disable clang

Name: deepin-grand-search
Version: 6.0.39
Release: alt1

Summary: Basic search tool for DDE

License: GPL-3.0-or-later
Group: File tools
Url: https://github.com/linuxdeepin/dde-grand-search
Vcs: https://github.com/linuxdeepin/dde-grand-search

# Source-url: https://github.com/linuxdeepin/dde-grand-search/archive/%version/%repo-%version.tar.gz
Source: %repo-%version.tar
Patch: %name-%version-%release.patch

%if_enabled clang
BuildRequires(pre): clang-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires(pre): rpm-build-ninja rpm-macros-dqt6
# Automatically added by buildreq on Thu Apr 03 2025
# optimized out: bash5 bashrc boost-asio-devel boost-devel-headers boost-filesystem-devel cmake cmake-modules dqt6-base-devel gcc-c++ glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libavcodec-devel libavformat-devel libavutil-devel libdeepin-pdfium1 libdeepin-qdbus-service0 libdouble-conversion3 libdqt5-core libdqt5-dbus libdqt6-concurrent libdqt6-core libdqt6-core5compat libdqt6-dbus libdqt6-gui libdqt6-network libdqt6-printsupport libdqt6-waylandclient libdqt6-widgets libdqt6-xml libdtk6core-devel libdtk6gui-devel libdtk6log-devel libglvnd-devel libgpg-error libp11-kit libsasl2-3 libssl-devel libstartup-notification libstdc++-devel libwayland-client libwayland-cursor libxkbcommon-devel ninja-build pkg-config python3 python3-base sh5 vulkan-headers zlib-devel
BuildRequires: dde-dock-devel dqt6-5compat-devel dqt6-tools-devel dqt6-declarative-devel dtk6-common-devel libcups-devel libdeepin-pdfium-devel libdeepin-qdbus-service-devel libdtk6widget-devel libdfm6-search-devel libffmpegthumbnailer-devel libgio-devel libicu-devel libjpeg-devel liblucene++-devel libtag-devel libuuid-devel deepin-desktop-base libantlr4-devel libdde-shell-devel deepin-shell deepin-desktop-base
BuildRequires: libdqt6-concurrent
# aarch64
BuildRequires: libpcre-devel

%description
Deepin Grand Search is a basic search tool developed
by Deepin Technology, featured with searching including
a series of files,applications or documents, etc.

%prep
%setup -n %repo-%version
%autopatch -p1

%build
export CPLUS_INCLUDE_PATH=%_includedir/antlr4-runtime:$CPLUS_INCLUDE_PATH
%define optflags_lto %nil
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export READELF="llvm-readelf"
%endif
%DQ6build \
  -DCMAKE_INSTALL_PREFIX=%_prefix \
  -DLIB_DESTINATION=%_lib \
#

%install
%DQ6install
%find_lang --with-qt --output=%repo.lang %repo dde-shell

%files -f %repo.lang
%doc README.md LICENSE.txt debian/changelog
%_bindir/dde-grand-search*
%_desktopdir/%repo.desktop
%dir %_libdir/dde-dock/
%dir %_libdir/dde-dock/plugins/
%_libdir/dde-dock/plugins/libddegrandsearch_dockplugin.so
%dir %_datadir/dde-dock/
%dir %_datadir/dde-dock/icons/
%dir %_datadir/dde-dock/icons/dcc-setting/
%_datadir/dde-dock/icons/dcc-setting/dcc-search.dci
%dir %_libdir/dde-grand-search-daemon/
%dir %_libdir/dde-grand-search-daemon/plugins/
%dir %_libdir/dde-grand-search-daemon/plugins/searcher/
%_libdir/dde-grand-search-daemon/plugins/searcher/.readme
%dir %_libdir/dde-grand-search/
%dir %_libdir/dde-grand-search/plugins/
%dir %_libdir/dde-grand-search/plugins/preview/
%_libdir/dde-grand-search/plugins/preview/*.conf
%_libdir/dde-grand-search/plugins/preview/*.so
%dir %_libdir/dde-shell/
%_libdir/dde-shell/org.deepin.ds.dock.searchitem.so
%dir %_datadir/dde-shell/
%dir %_datadir/dde-shell/org.deepin.ds.dock.searchitem/
%_datadir/dde-shell/org.deepin.ds.dock.searchitem/metadata.json
%_datadir/dde-shell/org.deepin.ds.dock.searchitem/searchitem.qml
%dir %_datadir/dde-shell/org.deepin.ds.dock.searchitem/icons/
%_datadir/dde-shell/org.deepin.ds.dock.searchitem/icons/dde-grand-search.dci
%_datadir/dde-shell/org.deepin.ds.dock.searchitem/icons/search.dci
%dir %_datadir/deepin-service-manager/
%dir %_datadir/deepin-service-manager/other/
%_datadir/deepin-service-manager/other/grand-search-daemon.json
# package outside find_lang
%dir %_datadir/dde-grand-search/
%dir %_datadir/dde-grand-search/translations/
%_datadir/dde-grand-search/translations/dde-grand-search.qm
%dir %_datadir/dde-shell/org.deepin.ds.dock.searchitem/translations/
%_datadir/dde-shell/org.deepin.ds.dock.searchitem/translations/org.deepin.ds.dock.searchitem.qm
# ---
%_datadir/dbus-1/interfaces/com.deepin.dde.GrandSearch.xml
%_datadir/dbus-1/interfaces/com.deepin.dde.GrandSearchSetting.xml
%_datadir/dbus-1/services/com.deepin.dde.GrandSearch.service
%_datadir/dbus-1/services/org.deepin.dde.GrandSearchDaemon.service
%_datadir/dbus-1/services/com.deepin.dde.GrandSearchSetting.service
%_datadir/glib-2.0/schemas/com.deepin.dde.dock.module.grand-search.gschema.xml
# manual
%dir %_datadir/deepin-manual/
%dir %_datadir/deepin-manual/manual-assets/
%dir %_datadir/deepin-manual/manual-assets/application/
%_datadir/deepin-manual/manual-assets/application/%repo/
# ---

%changelog
* Tue Jun 30 2026 Leontiy Volodin <lvol@altlinux.org> 6.0.39-alt1
- New version 6.0.39.

* Thu May 14 2026 Leontiy Volodin <lvol@altlinux.org> 6.0.32-alt1
- New version 6.0.32.

* Wed Apr 29 2026 Leontiy Volodin <lvol@altlinux.org> 6.0.31-alt1
- New version 6.0.31.

* Thu Apr 02 2026 Leontiy Volodin <lvol@altlinux.org> 6.0.30-alt1
- New version 6.0.30.

* Tue Mar 03 2026 Leontiy Volodin <lvol@altlinux.org> 6.0.29-alt1
- New version 6.0.29.
- Fixed build on shrinked dqt6.

* Thu Jan 29 2026 Leontiy Volodin <lvol@altlinux.org> 6.0.28-alt2
- Fixed build on dde-shell 2.0.27.

* Mon Dec 29 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.28-alt1
- New version 6.0.28.

* Mon Dec 22 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.26-alt1
- New version 6.0.26.

* Wed Oct 22 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.25-alt1
- New version 6.0.25.

* Mon Sep 15 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.24-alt1
- New version 6.0.24.

* Mon Jul 28 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.20-alt1
- New version 6.0.20.

* Wed Apr 30 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.9.1-alt2
- Fixed build with deepin-desktop-base 2025.03.06.

* Wed Apr 23 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.9.1-alt1
- New version 6.0.9.1.

* Thu Apr 03 2025 Leontiy Volodin <lvol@altlinux.org> 6.0.7-alt1
- New version 6.0.7.
- Switched to dqt6.

* Tue Jan 14 2025 Leontiy Volodin <lvol@altlinux.org> 5.5.11-alt1
- New version 5.5.11.
- Added vcs tag.

* Fri May 31 2024 Leontiy Volodin <lvol@altlinux.org> 5.4.9-alt1
- New version 5.4.9.
- Built via separate qt5 instead system (ALT #48138).

* Tue Jan 09 2024 Leontiy Volodin <lvol@altlinux.org> 5.4.5-alt1
- New version 5.4.5.
- Cleanup BRs.

* Thu Apr 06 2023 Leontiy Volodin <lvol@altlinux.org> 5.4.2-alt1
- New version 5.4.2.

* Fri Dec 02 2022 Leontiy Volodin <lvol@altlinux.org> 5.3.2-alt1
- Initial build for ALT Sisyphus.
