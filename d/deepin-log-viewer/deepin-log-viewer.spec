%def_disable clang

Name: deepin-log-viewer
Version: 5.9.13
Release: alt1
Summary: System log viewer for Deepin
License: GPL-3.0+
# 3rdparty/tmpfileplus/: MPL-2.0
# 3rdparty/minizip/: Zlib and Info-ZIP
# 3rdparty/md5/: Public-domain
# 3rdparty/libxlsxwriter/: GPL and MIT and BSD-2-Clause and BSD-3-Clause and Public-domain and Zlib and MPL-2.0
# 3rdparty/DocxFactory/: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-log-viewer

Source: %url/archive/%version/deepin-log-viewer-%version.tar.gz

BuildRequires(pre): rpm-build-ninja
%if_enabled clang
BuildRequires(pre): clang-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires: cmake cmake-modules qt5-base-devel dtk5-widget-devel dtk5-common qt5-tools-devel deepin-qt-dbus-factory-devel rapidjson boost-devel zlib-devel libgtest-devel libxerces-c-devel libpolkitqt5-qt5-devel
BuildRequires: libsystemd-devel libminizip-devel

%description
%summary.

%prep
%setup
# Don't build tests.
sed -i '/add_subdirectory(tests)/d' CMakeLists.txt

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
    -DCMAKE_SAFETYTEST_ARG="CMAKE_SAFETYTEST_ARG_OFF" \
    -DAPP_VERSION=%version \
    -DVERSION=%version \
    -DLIB_INSTALL_DIR=%_libdir \
#
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install

%files
%doc README.md LICENSE.txt
%_bindir/*
%_datadir/%name/
%_libexecdir/deepin-daemon/log-view-service
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/dbus-1/system-services/com.deepin.logviewer.service
%_datadir/dbus-1/system.d/com.deepin.logviewer.conf
%_datadir/polkit-1/actions/com.deepin.pkexec.logViewer*.policy
%dir %_datadir/deepin-manual/
%dir %_datadir/deepin-manual/manual-assets/
%dir %_datadir/deepin-manual/manual-assets/application/
%dir %_datadir/deepin-manual/manual-assets/application/%name/
%_datadir/deepin-manual/manual-assets/application/%name/log-viewer/

%changelog
* Thu Oct 27 2022 Leontiy Volodin <lvol@altlinux.org> 5.9.13-alt1
- Initial build for ALT Sisyphus.
