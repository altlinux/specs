%define _unpackaged_files_terminate_build 1

Name: qgroundcontrol
Version: 5.1.4
Release: alt1

Summary: Ground Control Station (GCS) designed for UAVs
License: Apache-2.0
Group: Engineering
URL: https://qgroundcontrol.com
VCS: https://github.com/mavlink/qgroundcontrol.git

Source: %name-%version.tar
Source1: %name-%version-vendor-mavlink.tar
Source2: %name-%version-vendor-c_library_v2.tar
Source3: %name-%version-vendor-PX4-GPSDrivers.tar
Source4: %name-%version-vendor-ParameterRepository.tar
Source5: %name-%version-vendor-earcut.hpp.tar

Patch1: alt-build-with-system-libs.patch
Patch2: alt-general-build.patch
Patch3: alt-esri-stadia-maptiler.patch
Patch4: alt-libcurl-tile-download.patch

Requires: qt6-charts
Requires: libOpenGL
Requires: libqt6-quickvectorimage

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc gcc-c++
%ifarch %e2k
BuildRequires: clang
%endif
BuildRequires: packagekit-qt6-devel
BuildRequires: qt6-charts-devel
BuildRequires: qt6-5compat-devel
BuildRequires: qt6-base-devel
BuildRequires: qt6-tools-devel
BuildRequires: qt6-location-devel
BuildRequires: qt6-multimedia-devel
BuildRequires: qt6-sensors-devel
BuildRequires: qt6-svg-devel
BuildRequires: qt6-speech-devel
BuildRequires: qt6-serialport-devel
BuildRequires: qt6-wayland-devel
BuildRequires: qt6-connectivity-devel
BuildRequires: qt6-quick3d-devel
BuildRequires: qt6-positioning-devel
BuildRequires: qt6-shadertools-devel
BuildRequires: qt6-httpserver-devel
BuildRequires: qt6-scxml-devel
BuildRequires: libqtgraphs-qt6-devel
BuildRequires: gstreamer1.0-devel
BuildRequires: gst-plugins1.0-devel
BuildRequires: gst-plugins-good1.0-qt6
BuildRequires: zlib-devel
BuildRequires: libSDL3-devel
BuildRequires: libshape-devel
BuildRequires: libgeographiclib-devel geographiclib
BuildRequires: libulog_cpp-devel
BuildRequires: libevents-devel
BuildRequires: libxz-embedded-devel
BuildRequires: gamecontrollerdb
BuildRequires: libcurl-devel
BuildRequires: libffi-devel
BuildRequires: liblzma-devel
BuildRequires: libzstd-devel
BuildRequires: libarchive-devel
BuildRequires: libexif-devel
BuildRequires: valijson-devel
BuildRequires: libexpat-devel
BuildRequires: libosmium-devel
BuildRequires: protozero-devel
BuildRequires: python3-dev
BuildRequires: python3-module-jinja2
BuildRequires: python3-module-defusedxml
BuildRequires: /proc

%description
QGroundControl (QGC) is a highly intuitive and powerful Ground Control Station
(GCS) designed for UAVs. Whether you're a first-time pilot or an experienced
professional, QGC provides a seamless user experience for flight control and
mission planning, making it the go-to solution for any MAVLink-enabled drone.

%prep
%setup -a 1 -a 2 -a 3 -a 4 -a 5
%autopatch -p1
# disable QML plugins deploy
sed -i '/install(SCRIPT ${deploy_script})/d' cmake/install/Install.cmake

%build
export LC_ALL=C.UTF-8
export QTDIR=%_qt6_prefix
export PATH="%{_qt6_bindir}:$PATH"
%cmake \
%ifarch %e2k
	-DCMAKE_C{_COMPILER=clang,XX_COMPILER=clang++} \
	-DCMAKE_C{,XX}_FLAGS_RELEASE="-O2 -g -DNDEBUG" \
	-DCMAKE_INSTALL_RPATH="%_libdir/gstreamer-1.0" \
	-DCMAKE_SKIP_INSTALL_RPATH=OFF \
%endif
	-DQGC_STABLE_BUILD=ON \
	-DCMAKE_AUTOGEN_PARALLEL=%__nprocs \
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_PREFIX_PATH=%_libdir/cmake/ \
	-DBUILD_SHARED_LIBS=ON \
	-DLIB_PREFIX=%_libdir \
	-DLIB_DIR_NAME=%_lib \
	-DUSE_SYSTEM_ULOG_CPP=ON \
	-DUSE_SYSTEM_QMDNSENGINE=ON \
	-DUSE_SYSTEM_PX4-GPSDRIVERS=ON \
	-DUSE_SYSTEM_SDL_GAMECONTROLLERDB=ON \
	-DUSE_SYSTEM_SDL2=ON \
	-DUSE_SYSTEM_MAVLINK=ON \
	-DUSE_SYSTEM_LIBEVENTS=ON \
	-DUSE_SYSTEM_ZLIB=ON \
	-DUSE_SYSTEM_XZ-EMBEDDED=ON \
	-DUSE_SYSTEM_GEOGRAPHICLIB=ON \
	-DUSE_SYSTEM_SHAPE=ON \
	-DUSE_SYSTEM_GSTQML6=ON \
    -DQGC_SYSTEM_LIBS_ONLY=ON \
    -DQGC_AUTO_PYTHON_VENV=OFF \
    -DQGC_CREATE_APPIMAGE=OFF \
    -DQGC_CPACK_GENERATOR= \
	#

%cmake_build

%install
%cmake_install

%find_lang --without-mo --with-qt qgc

%files -f qgc.lang
%_bindir/QGroundControl
%_desktopdir/org.mavlink.qgroundcontrol.desktop
%_iconsdir/hicolor/*/apps/QGroundControl.png
%_iconsdir/hicolor/scalable/apps/QGroundControl.svg
%exclude %_datadir/metainfo/org.mavlink.qgroundcontrol.appdata.xml

%changelog
* Tue Sep 22 2026 Ilya Mukhamadeev <nicourced@altlinux.org> 5.1.4-alt1
- Vendor mavlink, c_library_v2, PX4-GPSDrivers, ParameterRepository and
  earcut.hpp.
- New version.

* Fri Sep 11 2026 Sergey V Turchin <zerg@altlinux.org> 5.0.8-alt7
- NMU: disable Qt version restriction

* Wed May 13 2026 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 5.0.8-alt6
- e2k build fix (use clang)
- use proper cmake macros (enables parallel build)
- parallel Qt meta-object compiler (moc/autogen)
- remove unused BR
- spec cleanup

* Thu Apr 23 2026 Ilya Muhamadeev <nicourced@altlinux.org> 5.0.8-alt5
- Replace Yandex Tiles with Esri, MapTiler, Stadia providers;
- Add libcurl tile downloader.

* Sat Apr 4 2026 Ilya Muhamadeev <nicourced@altlinux.org> 5.0.8-alt4
- Use Yandex Maps as online maps provider.

* Tue Mar 24 2026 Ilya Muhamadeev <nicourced@altlinux.org> 5.0.8-alt3
- Remove SDL version hardening, update QGC hardcoded version.

* Thu Feb 26 2026 Ilya Muhamadeev <nicourced@altlinux.org> 5.0.8-alt2
- Remove useless BuildRequires (closes: 57928).

* Tue Feb 17 2026 Ilya Muhamadeev <nicourced@altlinux.org> 5.0.8-alt1
- Update version.

* Tue Jan 13 2026 Ilya Muhamadeev <nicourced@altlinux.org> 5.0.7-alt1
- Initial build.
