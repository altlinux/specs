%define repo dde-grand-search

%def_disable clang

Name: deepin-grand-search
Version: 5.3.2
Release: alt1
Summary: Basic search tool for DDE
License: GPL-3.0+
Group: File tools
Url: https://github.com/linuxdeepin/dde-grand-search

Source: %url/archive/%version/%repo-%version.tar.gz

%if_enabled clang
BuildRequires(pre): clang-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires(pre): rpm-build-ninja
BuildRequires: cmake libgio-devel glib2-devel libtag-devel libavformat-devel libffmpegthumbnailer-devel libpcre-devel
BuildRequires: qt5-base-devel qt5-tools libpoppler-qt5-devel gsettings-qt-devel
BuildRequires: dtk5-widget-devel dtk5-common deepin-qt-dbus-factory-devel deepin-dock-devel

%description
Deepin Grand Search is a basic search tool developed
by Deepin Technology, featured with searching including
a series of files,applications or documents, etc.

%prep
%setup -n %repo-%version
sed -i 's|lib/dde-dock/plugins/|%_lib/dde-dock/plugins/|' \
  src/grand-search-dock-plugin/CMakeLists.txt
sed -i 's|lib/${CMAKE_LIBRARY_ARCHITECTURE}|%_lib|' \
  CMakeLists.txt

%build
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
%doc README.md LICENSE
%_bindir/dde-grand-search*
%_sysconfdir/xdg/autostart/dde-grand-search-daemon.desktop
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
%_datadir/dde-grand-search/translations/dde-grand-search.qm
%_datadir/dbus-1/interfaces/com.deepin.dde.GrandSearch.xml
%_datadir/dbus-1/services/com.deepin.dde.GrandSearch.service
%_datadir/dbus-1/services/com.deepin.dde.daemon.GrandSearch.service
%_datadir/glib-2.0/schemas/com.deepin.dde.dock.module.grand-search.gschema.xml

%changelog
* Fri Dec 02 2022 Leontiy Volodin <lvol@altlinux.org> 5.3.2-alt1
- Initial build for ALT Sisyphus.
