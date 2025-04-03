%define repo dde-grand-search

%def_disable clang

Name: deepin-grand-search
Version: 6.0.7
Release: alt1

Summary: Basic search tool for DDE

License: GPL-3.0-or-later
Group: File tools
Url: https://github.com/linuxdeepin/dde-grand-search
Vcs: git://github.com/linuxdeepin/dde-grand-search.git

Source: %url/archive/%version/%repo-%version.tar.gz
Patch: deepin-grand-search-5.4.5-alt-fix-GNUInstallDirs.patch

%if_enabled clang
BuildRequires(pre): clang-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires(pre): rpm-build-ninja rpm-macros-dqt6
# Automatically added by buildreq on Thu Apr 03 2025
# optimized out: bash5 bashrc boost-asio-devel boost-devel-headers boost-filesystem-devel cmake cmake-modules dqt6-base-devel gcc-c++ glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libavcodec-devel libavformat-devel libavutil-devel libdeepin-pdfium1 libdeepin-qdbus-service0 libdouble-conversion3 libdqt5-core libdqt5-dbus libdqt6-concurrent libdqt6-core libdqt6-core5compat libdqt6-dbus libdqt6-gui libdqt6-network libdqt6-printsupport libdqt6-waylandclient libdqt6-widgets libdqt6-xml libdtk6core-devel libdtk6gui-devel libdtk6log-devel libglvnd-devel libgpg-error libp11-kit libsasl2-3 libssl-devel libstartup-notification libstdc++-devel libwayland-client libwayland-cursor libxkbcommon-devel ninja-build pkg-config python3 python3-base sh5 vulkan-headers zlib-devel
BuildRequires: dde-dock-devel dqt6-5compat-devel dqt6-tools dtk6-common-devel libcups-devel libdeepin-pdfium-devel libdeepin-qdbus-service-devel libdtk6widget-devel libffmpegthumbnailer-devel libgio-devel libicu-devel libjpeg-devel liblucene++-devel libtag-devel libuuid-devel
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
%find_lang --with-qt %repo

%files -f %repo.lang
%doc README.md LICENSE.txt
%_bindir/dde-grand-search*
%dir %_libdir/dde-dock/
%dir %_libdir/dde-dock/plugins/
%_libdir/dde-dock/plugins/libddegrandsearch_dockplugin.so
%dir %_libdir/dde-grand-search-daemon/
%dir %_libdir/dde-grand-search-daemon/plugins/
%dir %_libdir/dde-grand-search-daemon/plugins/searcher/
%_libdir/dde-grand-search-daemon/plugins/searcher/.readme
%dir %_libdir/dde-grand-search/
%dir %_libdir/dde-grand-search/plugins/
%dir %_libdir/dde-grand-search/plugins/preview/
%_libdir/dde-grand-search/plugins/preview/*.conf
%_libdir/dde-grand-search/plugins/preview/*.so
%dir %_datadir/deepin-service-manager/
%dir %_datadir/deepin-service-manager/other/
%_datadir/deepin-service-manager/other/grand-search-daemon.json
%dir %_datadir/dde-grand-search/
%dir %_datadir/dde-grand-search/translations/
%_datadir/dde-grand-search/translations/dde-grand-search.qm
%_datadir/dbus-1/interfaces/com.deepin.dde.GrandSearch.xml
%_datadir/dbus-1/interfaces/com.deepin.dde.GrandSearchSetting.xml
%_datadir/dbus-1/services/com.deepin.dde.GrandSearch.service
%_datadir/dbus-1/services/org.deepin.dde.GrandSearchDaemon.service
%_datadir/dbus-1/services/com.deepin.dde.GrandSearchSetting.service
%_datadir/glib-2.0/schemas/com.deepin.dde.dock.module.grand-search.gschema.xml

%changelog
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
