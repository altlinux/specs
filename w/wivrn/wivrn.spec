%define _unpackaged_files_terminate_build 1

%global commit1 1b526bb3a0ff326ecd05af4c2c541407f53c6d4b
%global monado_version 25.1.0

Name:    wivrn
Version: 26.6.1
Release: alt1

Summary: An OpenXR streaming application to a standalone headset
License: GPL-3.0-only
Group:   Games/Other
URL:     https://github.com/WiVRn/WiVRn
VCS:     https://github.com/WiVRn/WiVRn.git

Source:  %name-%version.tar
Source1: monado-src-%commit1.tar.bz2

Patch: 0001-c-multi-early-wake-of-compositor.patch
Patch1: 0002-Use-extern-socket-fd.patch
Patch2: 0003-change-environment-blend-mode-selection-logic.patch
Patch3: 0004-st-oxr-forward-0-refresh-rate.patch
Patch4: 0005-d-steamvr_lh-prevent-crash-on-vive-pro2-WiVRn.patch
Patch5: 0006-st-oxr-push-XrEventDataInteractionProfileChanged-whe.patch
Patch6: 0007-don-t-verify-GL-stuff.patch
Patch7: 0008-configure-u_git_tag-in-WiVRn.patch
Patch8: 0009-fix-csv_logger-boost-pfr-version.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ ninja-build extra-cmake-modules git-core
BuildRequires: libvulkan-devel glslc glslang-devel libssl-devel boost-devel
BuildRequires: boost-locale-devel libgeocode-glib2.0-devel libavcodec-devel
BuildRequires: libavutil-devel libswresample-devel libdrm-devel libx264-devel
BuildRequires: libsystemd-devel libcap-devel pipewire-libs-devel libpulseaudio-devel
BuildRequires: libavahi-devel libdbus-devel eigen3-devel libpcre2-devel
BuildRequires: nlohmann-json-devel cli11-devel libffi-devel libmount-devel
BuildRequires: libnotify-devel libblkid-devel librsvg-devel libselinux-devel
BuildRequires: libjpeg-devel libtiff-devel libwebp-devel libzstd-devel liblzma-devel
BuildRequires: libdeflate-devel shared-mime-info-devel bzlib-devel libbrotli-devel
BuildRequires: libexpat-devel libXdmcp-devel libpixman-devel libdav1d-devel
BuildRequires: libxml2-devel libfribidi-devel libthai-devel libdatrie-devel
BuildRequires: mylibrary-devel qt6-base-devel qt6-declarative-devel
BuildRequires: kf6-kirigami-devel kf6-ki18n-devel kf6-kcoreaddons-devel
BuildRequires: kf6-qqc2-desktop-style-devel kf6-kiconthemes-devel
BuildRequires: kf6-kirigami kf6-kirigami-addons kf6-kirigami-addons-devel qcoro6-devel
BuildRequires: libhidapi-devel libbluez-devel libopenhmd-devel libopencv-devel
BuildRequires: libusb-devel librealsense-devel libSDL2-devel libcjson-devel
BuildRequires: libuvc-devel libXrandr-devel gstreamer1.0-devel gst-plugins1.0-devel
BuildRequires: gst-plugins1.0-devel liborc-devel libsurvive-devel libopenvr-devel
BuildRequires: doxygen appstream spirv-tools

# Optional build-time dependencies missing in Sisyphus.
# CMake disables the corresponding drivers/features automatically.
# - depthai    : Intel DepthAI cameras (DRIVER_DEPTHAI)
# - LeapV2     : Leap Motion controller (legacy SDK)
# - LeapSDK    : Leap Motion controller (current SDK)
# - ONNXRuntime: hand tracking ML inference
# - Percetto   : performance tracing

ExclusiveArch: x86_64

%description
WiVRn wirelessly connects a standalone VR headset to a Linux computer.
You canthen play PCVR games on the headset while processing is done on
the computer.

Supports a wide range of headsets such as:

Meta Quest 1, 2, 3, 3S, Pro
Pico Neo 3, Pico 4
HTC Vive Focus 3, XR Elite
Samsung Galaxy XR
and most other Android based headsets


%package -n %name-dashboard
Summary: WiVRn dashboard
Group:   Games/Other
Requires: %name = %EVR
Requires: android-tools

%description -n %name-dashboard
WiVRn dashboard is a GUI for configuring and controlling WiVRn.

It is used to manage the server configuration, client installation,
and to assist in pairing the headset with the server.

%prep
%setup
%patch8 -p1

mkdir -p _deps/monado-src
tar -xvf %SOURCE1 --strip-components 1 -C _deps/monado-src
pushd _deps/monado-src
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
popd

%build

%cmake \
	-GNinja \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DCMAKE_INTERPROCEDURAL_OPTIMIZATION=ON \
	-DCMAKE_PROJECT_VERSION=%monado_version \
	-DENABLE_COLOURED_OUTPUT=OFF \
	-DFETCHCONTENT_BASE_DIR="_deps" \
	-DFETCHCONTENT_FULLY_DISCONNECTED=ON \
	-DGIT_DESC=v%version \
	-DGIT_COMMIT=v%version \
	-DOVR_COMPAT_SEARCH_PATH=%_libdir/opencomposite/runtime \
	-DWIVRN_BUILD_CLIENT=OFF \
	-DWIVRN_BUILD_DASHBOARD=ON \
	-DWIVRN_BUILD_DISSECTOR=OFF \
	-DWIVRN_BUILD_SERVER=ON \
	-DWIVRN_BUILD_WIVRNCTL=ON \
	-DCMAKE_INSTALL_PREFIX=%prefix \
	-DWIVRN_FEATURE_STEAMVR_LIGHTHOUSE=ON \
	-DWIVRN_USE_NVENC=ON \
	-DWIVRN_USE_PIPEWIRE=ON \
	-DWIVRN_USE_PULSEAUDIO=ON \
	-DWIVRN_USE_SYSTEMD=ON \
	-DWIVRN_USE_VAAPI=ON \
	-DWIVRN_USE_X264=ON \
	-DWIVRN_USE_VULKAN_ENCODE=ON \
	-Wno-dev

%cmake_build

%install
%cmake_install

%find_lang %name-dashboard

%files -f %name-dashboard.lang
%doc COPYING LICENSE* README*
%_bindir/wivrnctl
%_bindir/wivrn-server
%dir %_libdir/%name
%_libdir/%name/libopenxr_wivrn.so
%_libdir/%name/libmonado_wivrn.so
%_libdir/%name/libmonado_wivrn.so.25
%_libdir/%name/libmonado_wivrn.so.25.1.0
%_datadir/openxr/1/openxr_wivrn.json
%_userunitdir/wivrn.service
%_libexecdir/firewalld/services/wivrn.xml
%_datadir/metainfo/io.github.wivrn.wivrn.metainfo.xml

%files -n %name-dashboard
%_bindir/wivrn-dashboard
%_desktopdir/io.github.wivrn.wivrn.desktop
%_iconsdir/hicolor/scalable/apps/io.github.wivrn.wivrn.svg

%changelog
* Sat Jun 20 2026 Sergey Palcheh <minergenon@altlinux.org> 26.6.1-alt1
- new version 26.6.1

* Sat Jun 13 2026 Sergey Palcheh <minergenon@altlinux.org> 26.6-alt1
- initial build for ALT Sisyphus

