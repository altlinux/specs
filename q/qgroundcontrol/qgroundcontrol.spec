%define _unpackaged_files_terminate_build 1

Name: qgroundcontrol
Version: 5.0.8
Release: alt5

Summary: Ground Control Station (GCS) designed for UAVs
License: Apache-2.0
Group: Engineering
URL: https://qgroundcontrol.com
VCS: https://github.com/mavlink/qgroundcontrol.git

Source: %name-%version.tar
Source1: fix-qml-plugins.cmake

Patch1: alt-build-with-system-libs.patch
Patch2: alt-general-build.patch
Patch3: alt-source.patch
Patch4: alt-add-find-locationprivate.patch
Patch5: alt-add-elapsedtimer.patch
Patch6: alt-add-types-workaround.patch
Patch7: alt-esri-stadia-maptiler.patch
Patch8: alt-libcurl-tile-download.patch

Requires: qt6-charts
Requires: libOpenGL

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc gcc-c++
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
BuildRequires: qt6-quick3d
BuildRequires: qt6-positioning-devel
BuildRequires: qt6-shadertools-devel
BuildRequires: qt6-sql-interbase
BuildRequires: qt6-sql-postgresql
BuildRequires: qt6-sql-odbc
BuildRequires: qt6-sql-mysql
BuildRequires: gstreamer1.0-devel
BuildRequires: gst-plugins1.0-devel
BuildRequires: gst-plugins-good1.0-qt6
BuildRequires: libpcre2-devel
BuildRequires: libffi-devel
BuildRequires: libwayland-egl-devel
BuildRequires: liborc-devel
BuildRequires: libXau-devel
BuildRequires: libXdmcp-devel
BuildRequires: libgudev-devel
BuildRequires: libudev-devel
BuildRequires: libcap-devel
BuildRequires: libgbm-devel
BuildRequires: zlib-devel
BuildRequires: libmount-devel
BuildRequires: libblkid-devel
BuildRequires: libselinux-devel
BuildRequires: libunwind-devel
BuildRequires: libSDL2-devel
BuildRequires: libSDL3-devel
BuildRequires: libsystemd-devel
BuildRequires: patchelf
BuildRequires: libsoundio-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libwayland-client-devel
BuildRequires: libX11-devel
BuildRequires: libXrandr-devel
BuildRequires: libvulkan-devel
BuildRequires: libgbm-devel
BuildRequires: libdrm-devel
BuildRequires: libibus-devel
BuildRequires: libibus-gir-devel
BuildRequires: libsamplerate-devel
BuildRequires: libsndio7-devel
BuildRequires: libqmdnsengine-devel
BuildRequires: libshape-devel
BuildRequires: libgeographiclib-devel geographiclib
BuildRequires: libulog_cpp-devel
BuildRequires: libevents-devel
BuildRequires: libxz-embedded-devel
BuildRequires: parameterrepository
BuildRequires: gamecontrollerdb
BuildRequires: gpsdrivers
BuildRequires: c_library_v2
BuildRequires: libcurl-devel
BuildRequires: /proc

%description
QGroundControl (QGC) is a highly intuitive and powerful Ground Control Station
(GCS) designed for UAVs. Whether you're a first-time pilot or an experienced
professional, QGC provides a seamless user experience for flight control and
mission planning, making it the go-to solution for any MAVLink-enabled drone.

%prep
%setup
%autopatch -p1

# Copy prebuilt parameters where QGC expects them to be.
cp -r %_datadir/ParameterRepository/* src/FirmwarePlugin/APM/ArduPilot-Parameter-Repository/

%build
export LC_ALL=ru_RU.UTF-8
qt-cmake-qt6 -B build -G Ninja \
            -DCMAKE_BUILD_TYPE=Release \
            -DCMAKE_PROJECT_INCLUDE=%SOURCE1 \
            -DCMAKE_SKIP_INSTALL_RPATH=ON \
            -DCMAKE_INSTALL_RPATH="%_libdir" \
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
            #

cmake --build build --config Release
patchelf --set-rpath '' build/Release/QGroundControl # Clear wrong paths in rpath.

%install
mkdir -pv %buildroot
mkdir -pv %buildroot%_bindir
install -Dm 755 build/Release/QGroundControl %buildroot%_bindir/QGroundControl

mkdir -pv %buildroot%_datadir/applications
install -Dm 644 build/org.mavlink.qgroundcontrol.desktop %buildroot%_datadir/applications/org.mavlink.qgroundcontrol.desktop

install -Dm 644 resources/icons/qgroundcontrol.png %buildroot/%_datadir/icons/hicolor/128x128/apps/QGroundControl.png

%find_lang --without-mo --with-qt qgc

%files -f qgc.lang
%_bindir/QGroundControl
%_datadir/applications/org.mavlink.qgroundcontrol.desktop
%_datadir/icons/hicolor/128x128/apps/QGroundControl.png

%changelog
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
