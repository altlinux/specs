%define _unpackaged_files_terminate_build 1
%define soversion 10

Name: gz-sim
Version: 10.1.1
Release: alt2

Summary: Open source robotics simulator. The latest version of Gazebo.
License: Apache-2.0
Group: Other
Vcs: https://github.com/gazebosim/gz-sim
Url: https://gazebosim.org/libs/sim/

Source: %name-%version.tar

Patch0: gz-sim-10.0.0-altlinux-Qt6.9.2-compat.patch

# Same as for ogre-next
ExclusiveArch: x86_64 %e2k

Conflicts: libgz-sim

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: python3-dev
BuildRequires: libprotobuf-devel
BuildRequires: libfreeimage-devel
BuildRequires: libogre-next-devel
BuildRequires: libgperftools-devel
BuildRequires: libtinyxml2-devel
BuildRequires: tbb-devel
BuildRequires: libswscale-devel
BuildRequires: libavdevice-devel
BuildRequires: libavformat-devel
BuildRequires: libavfilter-devel
BuildRequires: libavcodec-devel
BuildRequires: libavutil-devel
BuildRequires: libgts-devel
BuildRequires: libbullet3-devel
BuildRequires: libusb-devel
BuildRequires: libopenal-devel
BuildRequires: libhdf5-devel
BuildRequires: libcurl-devel
BuildRequires: libswresample-devel
BuildRequires: libpcre2-devel
BuildRequires: protobuf-compiler
BuildRequires: tinyxml-devel
BuildRequires: libtar-devel

BuildRequires: gz-cmake
BuildRequires: libsdformat-devel
BuildRequires: gz-msgs
BuildRequires: libgz-msgs-devel
BuildRequires: gz-transport
BuildRequires: libgz-transport-devel
BuildRequires: libgz-common-devel
BuildRequires: libgz-fuel-tools-devel
BuildRequires: libgz-plugin-devel
BuildRequires: libgz-sensors-devel
BuildRequires: gz-gui
BuildRequires: libgz-gui-devel
BuildRequires: libgz-physics-devel
BuildRequires: gz-tools-devel
BuildRequires: libsimbody-devel
BuildRequires: qt6-base-devel
BuildRequires: qt6-declarative-devel
BuildRequires: boost-asio-devel
BuildRequires: boost-interprocess-devel
BuildRequires: boost-filesystem-devel
BuildRequires: boost-program_options-devel
BuildRequires: libgdal-devel
BuildRequires: libuuid-devel
BuildRequires: pybind11-devel
BuildRequires: libyaml-devel
BuildRequires: libstdc++-devel-static
BuildRequires: ronn
BuildRequires: xsltproc
BuildRequires: libgraphviz-devel
%ifnarch %e2k
BuildRequires: libdart-devel
%endif
BuildRequires: libfmt-devel

BuildRequires: ctest
BuildRequires: gz-common
BuildRequires: xvfb-run
BuildRequires: qt6-5compat-devel
BuildRequires: jsoncpp-devel
BuildRequires: libzip-devel

Requires: gz-common
Requires: gz-fuel-tools
Requires: gz-gui
Requires: gz-msgs
Requires: gz-physics
Requires: gz-plugin
Requires: gz-rendering
Requires: gz-transport
Requires: sdformat
Requires: gz-tools
Requires: qt6-5compat

%description
Gazebo simulates multiple robots in a 3D environment
with extensive dynamic interaction between objects.

%package -n libgz-sim%soversion
Summary: Library of gz-sim
Group: System/Libraries

%description -n libgz-sim%soversion
This package contains library libgz-sim of gz-sim.

%package -n libgz-sim-ackermann-steering-system%soversion
Summary: Library of gz-sim-ackermann-steering-system
Group: System/Libraries

%description -n libgz-sim-ackermann-steering-system%soversion
This package contains library libgz-sim-ackermann-steering-system of gz-sim.

%package -n libgz-sim-acoustic-comms-system%soversion
Summary: Library of gz-sim-acoustic-comms-system
Group: System/Libraries

%description -n libgz-sim-acoustic-comms-system%soversion
This package contains library libgz-sim-acoustic-comms-system of gz-sim.

%package -n libgz-sim-advanced-lift-drag-system%soversion
Summary: Library of gz-sim-advanced-lift-drag-system
Group: System/Libraries

%description -n libgz-sim-advanced-lift-drag-system%soversion
This package contains library libgz-sim-advanced-lift-drag-system of gz-sim.

%package -n libgz-sim-air-pressure-system%soversion
Summary: Library of gz-sim-air-pressure-system
Group: System/Libraries

%description -n libgz-sim-air-pressure-system%soversion
This package contains library libgz-sim-air-pressure-system of gz-sim.

%package -n libgz-sim-air-speed-system%soversion
Summary: Library of gz-sim-air-speed-system
Group: System/Libraries

%description -n libgz-sim-air-speed-system%soversion
This package contains library libgz-sim-air-speed-system of gz-sim.

%package -n libgz-sim-altimeter-system%soversion
Summary: Library of gz-sim-altimeter-system
Group: System/Libraries

%description -n libgz-sim-altimeter-system%soversion
This package contains library libgz-sim-altimeter-system of gz-sim.

%package -n libgz-sim-apply-joint-force-system%soversion
Summary: Library of gz-sim-apply-joint-force-system
Group: System/Libraries

%description -n libgz-sim-apply-joint-force-system%soversion
This package contains library libgz-sim-apply-joint-force-system of gz-sim.

%package -n libgz-sim-apply-link-wrench-system%soversion
Summary: Library of gz-sim-apply-link-wrench-system
Group: System/Libraries

%description -n libgz-sim-apply-link-wrench-system%soversion
This package contains library libgz-sim-apply-link-wrench-system of gz-sim.

%package -n libgz-sim-breadcrumbs-system%soversion
Summary: Library of gz-sim-breadcrumbs-system
Group: System/Libraries

%description -n libgz-sim-breadcrumbs-system%soversion
This package contains library libgz-sim-breadcrumbs-system of gz-sim.

%package -n libgz-sim-buoyancy-engine-system%soversion
Summary: Library of gz-sim-buoyancy-engine-system
Group: System/Libraries

%description -n libgz-sim-buoyancy-engine-system%soversion
This package contains library libgz-sim-buoyancy-engine-system of gz-sim.

%package -n libgz-sim-buoyancy-system%soversion
Summary: Library of gz-sim-buoyancy-system
Group: System/Libraries

%description -n libgz-sim-buoyancy-system%soversion
This package contains library libgz-sim-buoyancy-system of gz-sim.

%package -n libgz-sim-camera-video-recorder-system%soversion
Summary: Library of gz-sim-camera-video-recorder-system
Group: System/Libraries

%description -n libgz-sim-camera-video-recorder-system%soversion
This package contains library libgz-sim-camera-video-recorder-system of gz-sim.

%package -n libgz-sim-collada-world-exporter-system%soversion
Summary: Library of gz-sim-collada-world-exporter-system
Group: System/Libraries

%description -n libgz-sim-collada-world-exporter-system%soversion
This package contains library libgz-sim-collada-world-exporter-system of gz-sim.

%package -n libgz-sim-comms-endpoint-system%soversion
Summary: Library of gz-sim-comms-endpoint-system
Group: System/Libraries

%description -n libgz-sim-comms-endpoint-system%soversion
This package contains library libgz-sim-comms-endpoint-system of gz-sim.

%package -n libgz-sim-contact-system%soversion
Summary: Library of gz-sim-contact-system
Group: System/Libraries

%description -n libgz-sim-contact-system%soversion
This package contains library libgz-sim-contact-system of gz-sim.

%package -n libgz-sim-detachable-joint-system%soversion
Summary: Library of gz-sim-detachable-joint-system
Group: System/Libraries

%description -n libgz-sim-detachable-joint-system%soversion
This package contains library libgz-sim-detachable-joint-system of gz-sim.

%package -n libgz-sim-diff-drive-system%soversion
Summary: Library of gz-sim-diff-drive-system
Group: System/Libraries

%description -n libgz-sim-diff-drive-system%soversion
This package contains library libgz-sim-diff-drive-system of gz-sim.

%package -n libgz-sim-drive-to-pose-controller-system%soversion
Summary: Library of gz-sim-drive-to-pose-controller-system
Group: System/Libraries

%description -n libgz-sim-drive-to-pose-controller-system%soversion
This package contains library libgz-sim-drive-to-pose-controller-system of gz-sim.

%package -n libgz-sim-entity-semantics-system%soversion
Summary: Library of gz-sim-entity-semantics-system
Group: System/Libraries

%description -n libgz-sim-entity-semantics-system%soversion
This package contains library libgz-sim-entity-semantics-system of gz-sim.

%package -n libgz-sim-free-space-explorer-system%soversion
Summary: Library of gz-sim-free-space-explorer-system
Group: System/Libraries

%description -n libgz-sim-free-space-explorer-system%soversion
This package contains library libgz-sim-free-space-explorer-system of gz-sim.

%package -n libgz-sim-lookup-wheel-slip-system%soversion
Summary: Library of gz-sim-lookup-wheel-slip-system
Group: System/Libraries

%description -n libgz-sim-lookup-wheel-slip-system%soversion
This package contains library libgz-sim-lookup-wheel-slip-system of gz-sim.

%package -n libgz-sim-dvl-system%soversion
Summary: Library of gz-sim-dvl-system
Group: System/Libraries

%description -n libgz-sim-dvl-system%soversion
This package contains library libgz-sim-dvl-system of gz-sim.

%package -n libgz-sim-elevator-system%soversion
Summary: Library of gz-sim-elevator-system
Group: System/Libraries

%description -n libgz-sim-elevator-system%soversion
This package contains library libgz-sim-elevator-system of gz-sim.

%package -n libgz-sim-environment-preload-system%soversion
Summary: Library of gz-sim-environment-preload-system
Group: System/Libraries

%description -n libgz-sim-environment-preload-system%soversion
This package contains library libgz-sim-environment-preload-system of gz-sim.

%package -n libgz-sim-environmental-sensor-system%soversion
Summary: Library of gz-sim-environmental-sensor-system
Group: System/Libraries

%description -n libgz-sim-environmental-sensor-system%soversion
This package contains library libgz-sim-environmental-sensor-system of gz-sim.

%package -n libgz-sim-follow-actor-system%soversion
Summary: Library of gz-sim-follow-actor-system
Group: System/Libraries

%description -n libgz-sim-follow-actor-system%soversion
This package contains library libgz-sim-follow-actor-system of gz-sim.

%package -n libgz-sim-forcetorque-system%soversion
Summary: Library of gz-sim-forcetorque-system
Group: System/Libraries

%description -n libgz-sim-forcetorque-system%soversion
This package contains library libgz-sim-forcetorque-system of gz-sim.

%package -n libgz-sim-gui%soversion
Summary: Library of gz-sim-gui
Group: System/Libraries

%description -n libgz-sim-gui%soversion
This package contains library libgz-sim-gui of gz-sim.

%package -n libgz-sim-hydrodynamics-system%soversion
Summary: Library of gz-sim-hydrodynamics-system
Group: System/Libraries

%description -n libgz-sim-hydrodynamics-system%soversion
This package contains library libgz-sim-hydrodynamics-system of gz-sim.

%package -n libgz-sim-imu-system%soversion
Summary: Library of gz-sim-imu-system
Group: System/Libraries

%description -n libgz-sim-imu-system%soversion
This package contains library libgz-sim-imu-system of gz-sim.

%package -n libgz-sim-joint-controller-system%soversion
Summary: Library of gz-sim-joint-controller-system
Group: System/Libraries

%description -n libgz-sim-joint-controller-system%soversion
This package contains library libgz-sim-joint-controller-system of gz-sim.

%package -n libgz-sim-joint-position-controller-system%soversion
Summary: Library of gz-sim-joint-position-controller-system
Group: System/Libraries

%description -n libgz-sim-joint-position-controller-system%soversion
This package contains library libgz-sim-joint-position-controller-system of gz-sim.

%package -n libgz-sim-joint-state-publisher-system%soversion
Summary: Library of gz-sim-joint-state-publisher-system
Group: System/Libraries

%description -n libgz-sim-joint-state-publisher-system%soversion
This package contains library libgz-sim-joint-state-publisher-system of gz-sim.

%package -n libgz-sim-joint-trajectory-controller-system%soversion
Summary: Library of gz-sim-joint-trajectory-controller-system
Group: System/Libraries

%description -n libgz-sim-joint-trajectory-controller-system%soversion
This package contains library libgz-sim-joint-trajectory-controller-system of gz-sim.

%package -n libgz-sim-kinetic-energy-monitor-system%soversion
Summary: Library of gz-sim-kinetic-energy-monitor-system
Group: System/Libraries

%description -n libgz-sim-kinetic-energy-monitor-system%soversion
This package contains library libgz-sim-kinetic-energy-monitor-system of gz-sim.

%package -n libgz-sim-label-system%soversion
Summary: Library of gz-sim-label-system
Group: System/Libraries

%description -n libgz-sim-label-system%soversion
This package contains library libgz-sim-label-system of gz-sim.

%package -n libgz-sim-lens-flare-system%soversion
Summary: Library of gz-sim-lens-flare-system
Group: System/Libraries

%description -n libgz-sim-lens-flare-system%soversion
This package contains library libgz-sim-lens-flare-system of gz-sim.

%package -n libgz-sim-lift-drag-system%soversion
Summary: Library of gz-sim-lift-drag-system
Group: System/Libraries

%description -n libgz-sim-lift-drag-system%soversion
This package contains library libgz-sim-lift-drag-system of gz-sim.

%package -n libgz-sim-lighter_than_air_dynamics-system%soversion
Summary: Library of gz-sim-lighter_than_air_dynamics-system
Group: System/Libraries

%description -n libgz-sim-lighter_than_air_dynamics-system%soversion
This package contains library libgz-sim-lighter_than_air_dynamics-system of gz-sim.

%package -n libgz-sim-linearbatteryplugin-system%soversion
Summary: Library of gz-sim-linearbatteryplugin-system
Group: System/Libraries

%description -n libgz-sim-linearbatteryplugin-system%soversion
This package contains library libgz-sim-linearbatteryplugin-system of gz-sim.

%package -n libgz-sim-log-system%soversion
Summary: Library of gz-sim-log-system
Group: System/Libraries

%description -n libgz-sim-log-system%soversion
This package contains library libgz-sim-log-system of gz-sim.

%package -n libgz-sim-log-video-recorder-system%soversion
Summary: Library of gz-sim-log-video-recorder-system
Group: System/Libraries

%description -n libgz-sim-log-video-recorder-system%soversion
This package contains library libgz-sim-log-video-recorder-system of gz-sim.

%package -n libgz-sim-logical-camera-system%soversion
Summary: Library of gz-sim-logical-camera-system
Group: System/Libraries

%description -n libgz-sim-logical-camera-system%soversion
This package contains library libgz-sim-logical-camera-system of gz-sim.

%package -n libgz-sim-logicalaudiosensorplugin-system%soversion
Summary: Library of gz-sim-logicalaudiosensorplugin-system
Group: System/Libraries

%description -n libgz-sim-logicalaudiosensorplugin-system%soversion
This package contains library libgz-sim-logicalaudiosensorplugin-system of gz-sim.

%package -n libgz-sim-magnetometer-system%soversion
Summary: Library of gz-sim-magnetometer-system
Group: System/Libraries

%description -n libgz-sim-magnetometer-system%soversion
This package contains library libgz-sim-magnetometer-system of gz-sim.

%package -n libgz-sim-mecanum-drive-system%soversion
Summary: Library of gz-sim-mecanum-drive-system
Group: System/Libraries

%description -n libgz-sim-mecanum-drive-system%soversion
This package contains library libgz-sim-mecanum-drive-system of gz-sim.

%package -n libgz-sim-model-photo-shoot-system%soversion
Summary: Library of gz-sim-model-photo-shoot-system
Group: System/Libraries

%description -n libgz-sim-model-photo-shoot-system%soversion
This package contains library libgz-sim-model-photo-shoot-system of gz-sim.

%package -n libgz-sim-multicopter-control-system%soversion
Summary: Library of gz-sim-multicopter-control-system
Group: System/Libraries

%description -n libgz-sim-multicopter-control-system%soversion
This package contains library libgz-sim-multicopter-control-system of gz-sim.

%package -n libgz-sim-multicopter-motor-model-system%soversion
Summary: Library of gz-sim-multicopter-motor-model-system
Group: System/Libraries

%description -n libgz-sim-multicopter-motor-model-system%soversion
This package contains library libgz-sim-multicopter-motor-model-system of gz-sim.

%package -n libgz-sim-navsat-system%soversion
Summary: Library of gz-sim-navsat-system
Group: System/Libraries

%description -n libgz-sim-navsat-system%soversion
This package contains library libgz-sim-navsat-system of gz-sim.

%package -n libgz-sim-odometry-publisher-system%soversion
Summary: Library of gz-sim-odometry-publisher-system
Group: System/Libraries

%description -n libgz-sim-odometry-publisher-system%soversion
This package contains library libgz-sim-odometry-publisher-system of gz-sim.

%package -n libgz-sim-opticaltactileplugin-system%soversion
Summary: Library of gz-sim-opticaltactileplugin-system
Group: System/Libraries

%description -n libgz-sim-opticaltactileplugin-system%soversion
This package contains library libgz-sim-opticaltactileplugin-system of gz-sim.

%package -n libgz-sim-particle-emitter-system%soversion
Summary: Library of gz-sim-particle-emitter-system
Group: System/Libraries

%description -n libgz-sim-particle-emitter-system%soversion
This package contains library libgz-sim-particle-emitter-system of gz-sim.

%package -n libgz-sim-perfect-comms-system%soversion
Summary: Library of gz-sim-perfect-comms-system
Group: System/Libraries

%description -n libgz-sim-perfect-comms-system%soversion
This package contains library libgz-sim-perfect-comms-system of gz-sim.

%package -n libgz-sim-performer-detector-system%soversion
Summary: Library of gz-sim-performer-detector-system
Group: System/Libraries

%description -n libgz-sim-performer-detector-system%soversion
This package contains library libgz-sim-performer-detector-system of gz-sim.

%package -n libgz-sim-physics-system%soversion
Summary: Library of gz-sim-physics-system
Group: System/Libraries

%description -n libgz-sim-physics-system%soversion
This package contains library libgz-sim-physics-system of gz-sim.

%package -n libgz-sim-pose-publisher-system%soversion
Summary: Library of gz-sim-pose-publisher-system
Group: System/Libraries

%description -n libgz-sim-pose-publisher-system%soversion
This package contains library libgz-sim-pose-publisher-system of gz-sim.

%package -n libgz-sim-python-system-loader-system%soversion
Summary: Library of gz-sim-python-system-loader-system
Group: System/Libraries

%description -n libgz-sim-python-system-loader-system%soversion
This package contains library libgz-sim-python-system-loader-system of gz-sim.

%package -n libgz-sim-rendering%soversion
Summary: Library of gz-sim-rendering
Group: System/Libraries

%description -n libgz-sim-rendering%soversion
This package contains library libgz-sim-rendering of gz-sim.

%package -n libgz-sim-rf-comms-system%soversion
Summary: Library of gz-sim-rf-comms-system
Group: System/Libraries

%description -n libgz-sim-rf-comms-system%soversion
This package contains library libgz-sim-rf-comms-system of gz-sim.

%package -n libgz-sim-scene-broadcaster-system%soversion
Summary: Library of gz-sim-scene-broadcaster-system
Group: System/Libraries

%description -n libgz-sim-scene-broadcaster-system%soversion
This package contains library libgz-sim-scene-broadcaster-system of gz-sim.

%package -n libgz-sim-sensors-system%soversion
Summary: Library of gz-sim-sensors-system
Group: System/Libraries

%description -n libgz-sim-sensors-system%soversion
This package contains library libgz-sim-sensors-system of gz-sim.

%package -n libgz-sim-shader-param-system%soversion
Summary: Library of gz-sim-shader-param-system
Group: System/Libraries

%description -n libgz-sim-shader-param-system%soversion
This package contains library libgz-sim-shader-param-system of gz-sim.

%package -n libgz-sim-spacecraft-thruster-model-system%soversion
Summary: Library of gz-sim-spacecraft-thruster-model-system
Group: System/Libraries

%description -n libgz-sim-spacecraft-thruster-model-system%soversion
This package contains library libgz-sim-spacecraft-thruster-model-system of gz-sim.

%package -n libgz-sim-thermal-sensor-system%soversion
Summary: Library of gz-sim-thermal-sensor-system
Group: System/Libraries

%description -n libgz-sim-thermal-sensor-system%soversion
This package contains library libgz-sim-thermal-sensor-system of gz-sim.

%package -n libgz-sim-thermal-system%soversion
Summary: Library of gz-sim-thermal-system
Group: System/Libraries

%description -n libgz-sim-thermal-system%soversion
This package contains library libgz-sim-thermal-system of gz-sim.

%package -n libgz-sim-thruster-system%soversion
Summary: Library of gz-sim-thruster-system
Group: System/Libraries

%description -n libgz-sim-thruster-system%soversion
This package contains library libgz-sim-thruster-system of gz-sim.

%package -n libgz-sim-touchplugin-system%soversion
Summary: Library of gz-sim-touchplugin-system
Group: System/Libraries

%description -n libgz-sim-touchplugin-system%soversion
This package contains library libgz-sim-touchplugin-system of gz-sim.

%package -n libgz-sim-track-controller-system%soversion
Summary: Library of gz-sim-track-controller-system
Group: System/Libraries

%description -n libgz-sim-track-controller-system%soversion
This package contains library libgz-sim-track-controller-system of gz-sim.

%package -n libgz-sim-tracked-vehicle-system%soversion
Summary: Library of gz-sim-tracked-vehicle-system
Group: System/Libraries

%description -n libgz-sim-tracked-vehicle-system%soversion
This package contains library libgz-sim-tracked-vehicle-system of gz-sim.

%package -n libgz-sim-trajectory-follower-system%soversion
Summary: Library of gz-sim-trajectory-follower-system
Group: System/Libraries

%description -n libgz-sim-trajectory-follower-system%soversion
This package contains library libgz-sim-trajectory-follower-system of gz-sim.

%package -n libgz-sim-triggered-publisher-system%soversion
Summary: Library of gz-sim-triggered-publisher-system
Group: System/Libraries

%description -n libgz-sim-triggered-publisher-system%soversion
This package contains library libgz-sim-triggered-publisher-system of gz-sim.

%package -n libgz-sim-user-commands-system%soversion
Summary: Library of gz-sim-user-commands-system
Group: System/Libraries

%description -n libgz-sim-user-commands-system%soversion
This package contains library libgz-sim-user-commands-system of gz-sim.

%package -n libgz-sim-velocity-control-system%soversion
Summary: Library of gz-sim-velocity-control-system
Group: System/Libraries

%description -n libgz-sim-velocity-control-system%soversion
This package contains library libgz-sim-velocity-control-system of gz-sim.

%package -n libgz-sim-wheel-slip-system%soversion
Summary: Library of gz-sim-wheel-slip-system
Group: System/Libraries

%description -n libgz-sim-wheel-slip-system%soversion
This package contains library libgz-sim-wheel-slip-system of gz-sim.

%package -n libgz-sim-wind-effects-system%soversion
Summary: Library of gz-sim-wind-effects-system
Group: System/Libraries

%description -n libgz-sim-wind-effects-system%soversion
This package contains library libgz-sim-wind-effects-system of gz-sim.

%package -n libgz-sim-devel
Summary: Development files for gz-sim
Group: Development/C++

%description -n libgz-sim-devel
This package contains development files system

%prep
%setup
%autopatch -p1

%build
%cmake -GNinja -Wno-dev \
       -DQWT_WIN_INCLUDE_DIR=%_includedir/qt6
%cmake_build

%install
%cmake_install
install -Dpm0644 "%_cmake__builddir"/gz-sim%soversion.desktop %buildroot%_desktopdir/gz-sim%soversion.desktop
install -Dpm0644 "%_cmake__builddir"/gz-logo%soversion.svg %buildroot%_pixmapsdir/gz-logo%soversion.svg

%check
export GZ_SIM_SERVER_CONFIG_PATH="%buildroot%_datadir/gz/gz-sim/server.config"
export GZ_SIM_SYSTEM_PLUGIN_PATH="%buildroot%_libdir"

export CMAKE_PREFIX_PATH="%buildroot%_prefix"
Xvfb :99 -screen 0 1920x1080x24 2>/dev/null &
XVFB_PID=$!
export DISPLAY=:99
export GZ_RENDERING_PLUGIN_PATH="%buildroot%_libdir"
export GZ_RENDERING_DATA_PATH="%buildroot%_datadir/gz/gz-rendering"

# We don't build python module, so all tests with python are not working
excludes_python=(
  "actor_TEST"
  "joint_TEST"
  "light_TEST"
  "link_TEST"
  "model_TEST"
  "sensor_TEST"
  "testFixture_TEST"
  "world_TEST"
  "INTEGRATION_python_system_loader"
)
# These tests try to download from the internet.
# Build environment doesn't have a connection, so they are excluded.
excludes_download=(
  "UNIT_SdfGenerator_TEST"
  "INTEGRATION_breadcrumbs"
  "INTEGRATION_drive_to_pose_controller_system"
  "INTEGRATION_follow_actor_system"
  "INTEGRATION_model_photo_shoot_default_joints"
  "INTEGRATION_model_photo_shoot_random_joints"
  "INTEGRATION_save_world"
  "INTEGRATION_spacecraft"
  "INTEGRATION_sdf_include"
  "INTEGRATION_examples_build"
  "UNIT_Util_TEST"
)
# See https://github.com/gazebosim/gz-sim/issues/3306
excludes_other=(
  "UNIT_Gui_TEST"
  "INTEGRATION_apply_link_wrench_system"
  "INTEGRATION_material"
  "INTEGRATION_thruster"
)
# This test is known to be problematic; See:
# https://github.com/gazebosim/gz-sim/pull/1771
# https://github.com/gazebosim/gz-sim/issues/1886
# https://github.com/gazebosim/gz-sim/pull/1897
# https://github.com/gazebosim/gz-sim/pull/1902
#
# INTEGRATION_lookup_wheel_slip_system relies on bit-exact DART/bullet
# heightmap physics; fails on Sisyphus builders due to FP non-determinism
# (vehicle rotates in the opposite direction than the test expects).
excludes_flaky=(
  "UNIT_Gui_clean_exit_TEST"
  "INTEGRATION_lookup_wheel_slip_system"
)
excludes_python_regex=$(IFS='|'; echo "${excludes_python[*]}")
excludes_download_regex=$(IFS='|'; echo "${excludes_download[*]}")
excludes_other_regex=$(IFS='|'; echo "${excludes_other[*]}")
excludes_flaky_regex=$(IFS='|'; echo "${excludes_flaky[*]}")

%ctest \
  --parallel 1 \
  -E "$excludes_python_regex|$excludes_download_regex|$excludes_other_regex|$excludes_flaky_regex" \
  #
trap 'kill -TERM "$XVFB_PID" 2>/dev/null || true; wait "$XVFB_PID" 2>/dev/null || true' EXIT

%files
%doc AUTHORS README.md
%_datadir/gz/gz-sim
%_desktopdir/gz-sim%soversion.desktop
%_pixmapsdir/gz-logo%soversion.svg
%_libexecdir/ruby/gz/cmdsim%soversion.rb
%_libexecdir/ruby/gz/cmdmodel%soversion.rb
%_libdir/gz-sim-%soversion/plugins
%_libdir/python/gz
%_datadir/gz/gz2.completion.d/sim%soversion.bash_completion.sh
%_datadir/gz/gz2.completion.d/model%soversion.bash_completion.sh
%_datadir/gz/sim%soversion.yaml
%_datadir/gz/model%soversion.yaml
%_prefix/libexec/gz/sim%soversion/gz-sim-*

%files -n libgz-sim%soversion
%_libdir/libgz-sim.so.%soversion
%_libdir/libgz-sim.so.%version

%files -n libgz-sim-ackermann-steering-system%soversion
%_libdir/libgz-sim-ackermann-steering-system.so.%soversion
%_libdir/libgz-sim-ackermann-steering-system.so.%version

%files -n libgz-sim-acoustic-comms-system%soversion
%_libdir/libgz-sim-acoustic-comms-system.so.%soversion
%_libdir/libgz-sim-acoustic-comms-system.so.%version

%files -n libgz-sim-advanced-lift-drag-system%soversion
%_libdir/libgz-sim-advanced-lift-drag-system.so.%soversion
%_libdir/libgz-sim-advanced-lift-drag-system.so.%version

%files -n libgz-sim-air-pressure-system%soversion
%_libdir/libgz-sim-air-pressure-system.so.%soversion
%_libdir/libgz-sim-air-pressure-system.so.%version

%files -n libgz-sim-air-speed-system%soversion
%_libdir/libgz-sim-air-speed-system.so.%soversion
%_libdir/libgz-sim-air-speed-system.so.%version

%files -n libgz-sim-altimeter-system%soversion
%_libdir/libgz-sim-altimeter-system.so.%soversion
%_libdir/libgz-sim-altimeter-system.so.%version

%files -n libgz-sim-apply-joint-force-system%soversion
%_libdir/libgz-sim-apply-joint-force-system.so.%soversion
%_libdir/libgz-sim-apply-joint-force-system.so.%version

%files -n libgz-sim-apply-link-wrench-system%soversion
%_libdir/libgz-sim-apply-link-wrench-system.so.%soversion
%_libdir/libgz-sim-apply-link-wrench-system.so.%version

%files -n libgz-sim-breadcrumbs-system%soversion
%_libdir/libgz-sim-breadcrumbs-system.so.%soversion
%_libdir/libgz-sim-breadcrumbs-system.so.%version

%files -n libgz-sim-buoyancy-engine-system%soversion
%_libdir/libgz-sim-buoyancy-engine-system.so.%soversion
%_libdir/libgz-sim-buoyancy-engine-system.so.%version

%files -n libgz-sim-buoyancy-system%soversion
%_libdir/libgz-sim-buoyancy-system.so.%soversion
%_libdir/libgz-sim-buoyancy-system.so.%version

%files -n libgz-sim-camera-video-recorder-system%soversion
%_libdir/libgz-sim-camera-video-recorder-system.so.%soversion
%_libdir/libgz-sim-camera-video-recorder-system.so.%version

%files -n libgz-sim-collada-world-exporter-system%soversion
%_libdir/libgz-sim-collada-world-exporter-system.so.%soversion
%_libdir/libgz-sim-collada-world-exporter-system.so.%version

%files -n libgz-sim-comms-endpoint-system%soversion
%_libdir/libgz-sim-comms-endpoint-system.so.%soversion
%_libdir/libgz-sim-comms-endpoint-system.so.%version

%files -n libgz-sim-contact-system%soversion
%_libdir/libgz-sim-contact-system.so.%soversion
%_libdir/libgz-sim-contact-system.so.%version

%files -n libgz-sim-detachable-joint-system%soversion
%_libdir/libgz-sim-detachable-joint-system.so.%soversion
%_libdir/libgz-sim-detachable-joint-system.so.%version

%files -n libgz-sim-diff-drive-system%soversion
%_libdir/libgz-sim-diff-drive-system.so.%soversion
%_libdir/libgz-sim-diff-drive-system.so.%version

%files -n libgz-sim-dvl-system%soversion
%_libdir/libgz-sim-dvl-system.so.%soversion
%_libdir/libgz-sim-dvl-system.so.%version

%files -n libgz-sim-elevator-system%soversion
%_libdir/libgz-sim-elevator-system.so.%soversion
%_libdir/libgz-sim-elevator-system.so.%version

%files -n libgz-sim-environment-preload-system%soversion
%_libdir/libgz-sim-environment-preload-system.so.%soversion
%_libdir/libgz-sim-environment-preload-system.so.%version

%files -n libgz-sim-environmental-sensor-system%soversion
%_libdir/libgz-sim-environmental-sensor-system.so.%soversion
%_libdir/libgz-sim-environmental-sensor-system.so.%version

%files -n libgz-sim-follow-actor-system%soversion
%_libdir/libgz-sim-follow-actor-system.so.%soversion
%_libdir/libgz-sim-follow-actor-system.so.%version

%files -n libgz-sim-forcetorque-system%soversion
%_libdir/libgz-sim-forcetorque-system.so.%soversion
%_libdir/libgz-sim-forcetorque-system.so.%version

%files -n libgz-sim-gui%soversion
%_libdir/libgz-sim-gui.so.%soversion
%_libdir/libgz-sim-gui.so.%version

%files -n libgz-sim-hydrodynamics-system%soversion
%_libdir/libgz-sim-hydrodynamics-system.so.%soversion
%_libdir/libgz-sim-hydrodynamics-system.so.%version

%files -n libgz-sim-imu-system%soversion
%_libdir/libgz-sim-imu-system.so.%soversion
%_libdir/libgz-sim-imu-system.so.%version

%files -n libgz-sim-joint-controller-system%soversion
%_libdir/libgz-sim-joint-controller-system.so.%soversion
%_libdir/libgz-sim-joint-controller-system.so.%version

%files -n libgz-sim-joint-position-controller-system%soversion
%_libdir/libgz-sim-joint-position-controller-system.so.%soversion
%_libdir/libgz-sim-joint-position-controller-system.so.%version

%files -n libgz-sim-joint-state-publisher-system%soversion
%_libdir/libgz-sim-joint-state-publisher-system.so.%soversion
%_libdir/libgz-sim-joint-state-publisher-system.so.%version

%files -n libgz-sim-joint-trajectory-controller-system%soversion
%_libdir/libgz-sim-joint-trajectory-controller-system.so.%soversion
%_libdir/libgz-sim-joint-trajectory-controller-system.so.%version

%files -n libgz-sim-kinetic-energy-monitor-system%soversion
%_libdir/libgz-sim-kinetic-energy-monitor-system.so.%soversion
%_libdir/libgz-sim-kinetic-energy-monitor-system.so.%version

%files -n libgz-sim-label-system%soversion
%_libdir/libgz-sim-label-system.so.%soversion
%_libdir/libgz-sim-label-system.so.%version

%files -n libgz-sim-lens-flare-system%soversion
%_libdir/libgz-sim-lens-flare-system.so.%soversion
%_libdir/libgz-sim-lens-flare-system.so.%version

%files -n libgz-sim-lift-drag-system%soversion
%_libdir/libgz-sim-lift-drag-system.so.%soversion
%_libdir/libgz-sim-lift-drag-system.so.%version

%files -n libgz-sim-lighter_than_air_dynamics-system%soversion
%_libdir/libgz-sim-lighter_than_air_dynamics-system.so.%soversion
%_libdir/libgz-sim-lighter_than_air_dynamics-system.so.%version

%files -n libgz-sim-linearbatteryplugin-system%soversion
%_libdir/libgz-sim-linearbatteryplugin-system.so.%soversion
%_libdir/libgz-sim-linearbatteryplugin-system.so.%version

%files -n libgz-sim-log-system%soversion
%_libdir/libgz-sim-log-system.so.%soversion
%_libdir/libgz-sim-log-system.so.%version

%files -n libgz-sim-log-video-recorder-system%soversion
%_libdir/libgz-sim-log-video-recorder-system.so.%soversion
%_libdir/libgz-sim-log-video-recorder-system.so.%version

%files -n libgz-sim-logical-camera-system%soversion
%_libdir/libgz-sim-logical-camera-system.so.%soversion
%_libdir/libgz-sim-logical-camera-system.so.%version

%files -n libgz-sim-logicalaudiosensorplugin-system%soversion
%_libdir/libgz-sim-logicalaudiosensorplugin-system.so.%soversion
%_libdir/libgz-sim-logicalaudiosensorplugin-system.so.%version

%files -n libgz-sim-magnetometer-system%soversion
%_libdir/libgz-sim-magnetometer-system.so.%soversion
%_libdir/libgz-sim-magnetometer-system.so.%version

%files -n libgz-sim-mecanum-drive-system%soversion
%_libdir/libgz-sim-mecanum-drive-system.so.%soversion
%_libdir/libgz-sim-mecanum-drive-system.so.%version

%files -n libgz-sim-model-photo-shoot-system%soversion
%_libdir/libgz-sim-model-photo-shoot-system.so.%soversion
%_libdir/libgz-sim-model-photo-shoot-system.so.%version

%files -n libgz-sim-multicopter-control-system%soversion
%_libdir/libgz-sim-multicopter-control-system.so.%soversion
%_libdir/libgz-sim-multicopter-control-system.so.%version

%files -n libgz-sim-multicopter-motor-model-system%soversion
%_libdir/libgz-sim-multicopter-motor-model-system.so.%soversion
%_libdir/libgz-sim-multicopter-motor-model-system.so.%version

%files -n libgz-sim-navsat-system%soversion
%_libdir/libgz-sim-navsat-system.so.%soversion
%_libdir/libgz-sim-navsat-system.so.%version

%files -n libgz-sim-odometry-publisher-system%soversion
%_libdir/libgz-sim-odometry-publisher-system.so.%soversion
%_libdir/libgz-sim-odometry-publisher-system.so.%version

%files -n libgz-sim-opticaltactileplugin-system%soversion
%_libdir/libgz-sim-opticaltactileplugin-system.so.%soversion
%_libdir/libgz-sim-opticaltactileplugin-system.so.%version

%files -n libgz-sim-particle-emitter-system%soversion
%_libdir/libgz-sim-particle-emitter-system.so.%soversion
%_libdir/libgz-sim-particle-emitter-system.so.%version

%files -n libgz-sim-perfect-comms-system%soversion
%_libdir/libgz-sim-perfect-comms-system.so.%soversion
%_libdir/libgz-sim-perfect-comms-system.so.%version

%files -n libgz-sim-performer-detector-system%soversion
%_libdir/libgz-sim-performer-detector-system.so.%soversion
%_libdir/libgz-sim-performer-detector-system.so.%version

%files -n libgz-sim-physics-system%soversion
%_libdir/libgz-sim-physics-system.so.%soversion
%_libdir/libgz-sim-physics-system.so.%version

%files -n libgz-sim-pose-publisher-system%soversion
%_libdir/libgz-sim-pose-publisher-system.so.%soversion
%_libdir/libgz-sim-pose-publisher-system.so.%version

%files -n libgz-sim-python-system-loader-system%soversion
%_libdir/libgz-sim-python-system-loader-system.so.%soversion
%_libdir/libgz-sim-python-system-loader-system.so.%version

%files -n libgz-sim-rendering%soversion
%_libdir/libgz-sim-rendering.so.%soversion
%_libdir/libgz-sim-rendering.so.%version

%files -n libgz-sim-rf-comms-system%soversion
%_libdir/libgz-sim-rf-comms-system.so.%soversion
%_libdir/libgz-sim-rf-comms-system.so.%version

%files -n libgz-sim-scene-broadcaster-system%soversion
%_libdir/libgz-sim-scene-broadcaster-system.so.%soversion
%_libdir/libgz-sim-scene-broadcaster-system.so.%version

%files -n libgz-sim-sensors-system%soversion
%_libdir/libgz-sim-sensors-system.so.%soversion
%_libdir/libgz-sim-sensors-system.so.%version

%files -n libgz-sim-shader-param-system%soversion
%_libdir/libgz-sim-shader-param-system.so.%soversion
%_libdir/libgz-sim-shader-param-system.so.%version

%files -n libgz-sim-spacecraft-thruster-model-system%soversion
%_libdir/libgz-sim-spacecraft-thruster-model-system.so.%soversion
%_libdir/libgz-sim-spacecraft-thruster-model-system.so.%version

%files -n libgz-sim-thermal-sensor-system%soversion
%_libdir/libgz-sim-thermal-sensor-system.so.%soversion
%_libdir/libgz-sim-thermal-sensor-system.so.%version

%files -n libgz-sim-thermal-system%soversion
%_libdir/libgz-sim-thermal-system.so.%soversion
%_libdir/libgz-sim-thermal-system.so.%version

%files -n libgz-sim-thruster-system%soversion
%_libdir/libgz-sim-thruster-system.so.%soversion
%_libdir/libgz-sim-thruster-system.so.%version

%files -n libgz-sim-touchplugin-system%soversion
%_libdir/libgz-sim-touchplugin-system.so.%soversion
%_libdir/libgz-sim-touchplugin-system.so.%version

%files -n libgz-sim-track-controller-system%soversion
%_libdir/libgz-sim-track-controller-system.so.%soversion
%_libdir/libgz-sim-track-controller-system.so.%version

%files -n libgz-sim-tracked-vehicle-system%soversion
%_libdir/libgz-sim-tracked-vehicle-system.so.%soversion
%_libdir/libgz-sim-tracked-vehicle-system.so.%version

%files -n libgz-sim-trajectory-follower-system%soversion
%_libdir/libgz-sim-trajectory-follower-system.so.%soversion
%_libdir/libgz-sim-trajectory-follower-system.so.%version

%files -n libgz-sim-triggered-publisher-system%soversion
%_libdir/libgz-sim-triggered-publisher-system.so.%soversion
%_libdir/libgz-sim-triggered-publisher-system.so.%version

%files -n libgz-sim-user-commands-system%soversion
%_libdir/libgz-sim-user-commands-system.so.%soversion
%_libdir/libgz-sim-user-commands-system.so.%version

%files -n libgz-sim-velocity-control-system%soversion
%_libdir/libgz-sim-velocity-control-system.so.%soversion
%_libdir/libgz-sim-velocity-control-system.so.%version

%files -n libgz-sim-wheel-slip-system%soversion
%_libdir/libgz-sim-wheel-slip-system.so.%soversion
%_libdir/libgz-sim-wheel-slip-system.so.%version

%files -n libgz-sim-wind-effects-system%soversion
%_libdir/libgz-sim-wind-effects-system.so.%soversion
%_libdir/libgz-sim-wind-effects-system.so.%version

%files -n libgz-sim-drive-to-pose-controller-system%soversion
%_libdir/libgz-sim-drive-to-pose-controller-system.so.%soversion
%_libdir/libgz-sim-drive-to-pose-controller-system.so.%version

%files -n libgz-sim-entity-semantics-system%soversion
%_libdir/libgz-sim-entity-semantics-system.so.%soversion
%_libdir/libgz-sim-entity-semantics-system.so.%version

%files -n libgz-sim-free-space-explorer-system%soversion
%_libdir/libgz-sim-free-space-explorer-system.so.%soversion
%_libdir/libgz-sim-free-space-explorer-system.so.%version

%files -n libgz-sim-lookup-wheel-slip-system%soversion
%_libdir/libgz-sim-lookup-wheel-slip-system.so.%soversion
%_libdir/libgz-sim-lookup-wheel-slip-system.so.%version

%files -n libgz-sim-devel
%_includedir/gz/sim%soversion
%_libdir/libgz-sim*.so
%_cmakedir/gz-sim*
%_pkgconfigdir/gz-sim*.pc

%changelog
* Wed Apr 29 2026 Anton Farygin <rider@altlinux.org> 10.1.1-alt2
- Exclude flaky INTEGRATION_lookup_wheel_slip_system test from %%check
  (FP non-determinism in DART/bullet heightmap physics).

* Tue Apr 21 2026 Pavel Petrykin <silverducks@altlinux.org> 10.1.1-alt1
- New version.
- Fix segfault due to missing dependency on GNOME (ALT 46849).

* Mon Feb 2 2026 Pavel Petrykin <silverducks@altlinux.org> 10.1.0-alt1
- New version.
- Fix save world file dialog (ALT 57554).
- Fix missing plugins (ALT 47207).
- Fix segfault when selecting Sun or Ground_plane (ALT 46849).
- Fix GUI not launching (ALT 57609).

* Fri Dec 26 2025 Pavel Petrykin <silverducks@altlinux.org> 10.0.0-alt1
- New version.

* Wed Jan 15 2025 Michael Shigorin <mike@altlinux.org> 9.0.0-alt2
- E2K: builds fine.
- Minor spec cleanup.

* Mon Nov 11 2024 Andrey Cherepanov <cas@altlinux.org> 9.0.0-alt1
- New version.

* Tue Apr 02 2024 Andrey Cherepanov <cas@altlinux.org> 8.2.0-alt1
- New version.
- Used ogre2 rendering engine.

* Thu Jan 25 2024 Andrey Cherepanov <cas@altlinux.org> 8.0.0-alt1
- New version.
- Built with ogre-next.

* Wed Sep 27 2023 Andrey Cherepanov <cas@altlinux.org> 7.6.0-alt1
- New version.

* Wed Sep 20 2023 Andrey Cherepanov <cas@altlinux.org> 7.5.0-alt2
- FTBFS: removed libavresample-devel.

* Sat Aug 26 2023 Michael Shigorin <mike@altlinux.org> 7.5.0-alt1.1
- E2K: build without dart

* Tue Aug 01 2023 Andrey Cherepanov <cas@altlinux.org> 7.5.0-alt1
- New version.

* Thu Jun 22 2023 Andrey Cherepanov <cas@altlinux.org> 6.14.0-alt2
- Moved .so files to main library package.
- Built with DART.
- Used ogre instead of ogre2 by default.

* Mon Jun 19 2023 Andrey Cherepanov <cas@altlinux.org> 6.14.0-alt1
- Initial build for Sisyphus.
