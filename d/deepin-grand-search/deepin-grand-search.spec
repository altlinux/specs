%define repo dde-grand-search

%def_disable clang

Name: deepin-grand-search
Version: 5.4.5
Release: alt1

Summary: Basic search tool for DDE

License: GPL-3.0-or-later
Group: File tools
Url: https://github.com/linuxdeepin/dde-grand-search

Source: %url/archive/%version/%repo-%version.tar.gz
Patch: %name-%version-%release.patch

%if_enabled clang
BuildRequires(pre): clang-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires(pre): rpm-build-ninja
# Automatically added by buildreq on Tue Jan 09 2024
# optimized out: alt-os-release bash5 bashrc cmake cmake-modules dtkcore gcc-c++ glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libavcodec-devel libavformat-devel libavutil-devel libdeepin-pdfium1 libdouble-conversion3 libdtkcore-devel libdtkgui-devel libglvnd-devel libgpg-error libgsettings-qt libicu-devel libp11-kit libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libssl-devel libstartup-notification libstdc++-devel pkg-config python3 python3-base python3-dev python3-module-setuptools qt5-base-common qt5-base-devel sh5 zlib-devel
BuildRequires: deepin-dock-devel deepin-qt-dbus-factory-devel gsettings-qt-devel libdeepin-pdfium-devel libdtkwidget-devel libffmpegthumbnailer-devel libgio-devel libjpeg-devel libtag-devel qt5-tools
# aarch64
BuildRequires: libpcre-devel

%description
Deepin Grand Search is a basic search tool developed
by Deepin Technology, featured with searching including
a series of files,applications or documents, etc.

%prep
%setup -n %repo-%version
%patch -p1

%build
%define optflags_lto %nil
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export READELF="llvm-readelf"
%endif
export PATH=%_qt5_bindir:$PATH
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_INSTALL_PREFIX=%_prefix \
  -DARCHITECTURE=%_arch \
#
cmake --build %_cmake__builddir -j%__nprocs

%install
%cmake_install
%find_lang --with-qt %repo

%files -f %repo.lang
%doc README.md LICENSE.txt
%_bindir/dde-grand-search*
%_desktopdir/dde-grand-search-daemon.desktop
%dir %_libdir/dde-dock/
%dir %_libdir/dde-dock/plugins/
%_libdir/dde-dock/plugins/libddegrandsearch_dockplugin.so
%dir %_libdir/dde-grand-search-daemon/
%_libdir/dde-grand-search-daemon/libdde-grand-search-daemon.so
%dir %_libdir/dde-grand-search-daemon/plugins/
%dir %_libdir/dde-grand-search-daemon/plugins/searcher/
%_libdir/dde-grand-search-daemon/plugins/searcher/.readme
%dir %_libdir/dde-grand-search/
%dir %_libdir/dde-grand-search/plugins/
%dir %_libdir/dde-grand-search/plugins/preview/
%_libdir/dde-grand-search/plugins/preview/*.conf
%_libdir/dde-grand-search/plugins/preview/*.so
%_datadir/dde-grand-search/translations/dde-grand-search.qm
%_datadir/dbus-1/interfaces/com.deepin.dde.GrandSearch.xml
%_datadir/dbus-1/services/com.deepin.dde.GrandSearch.service
%_datadir/dbus-1/services/com.deepin.dde.daemon.GrandSearch.service
%_datadir/glib-2.0/schemas/com.deepin.dde.dock.module.grand-search.gschema.xml

%changelog
* Tue Jan 09 2024 Leontiy Volodin <lvol@altlinux.org> 5.4.5-alt1
- New version 5.4.5.
- Cleanup BRs.

* Thu Apr 06 2023 Leontiy Volodin <lvol@altlinux.org> 5.4.2-alt1
- New version 5.4.2.

* Fri Dec 02 2022 Leontiy Volodin <lvol@altlinux.org> 5.3.2-alt1
- Initial build for ALT Sisyphus.
