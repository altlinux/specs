%define _unpackaged_files_terminate_build 1
%define soversion 10

Name: gz-sensors
Version: 10.0.0
Release: alt1

Summary: Provides numerous sensor models designed to generate realistic data from simulation environments
License: Apache-2.0
Group: Development/C++
Vcs: https://github.com/gazebosim/gz-sensors
Url: https://gazebosim.org/libs/sensors/

Source: %name-%version.tar

# Same as for ogre-next via libgz-rendering-devel
ExclusiveArch: x86_64 %e2k

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: gz-cmake
BuildRequires: libprotobuf-devel
BuildRequires: libsdformat-devel
BuildRequires: libgz-msgs-devel >= 8.0.0
BuildRequires: libgz-transport-devel >= 11.0.0
BuildRequires: libgz-common-devel
BuildRequires: libgz-rendering-devel >= 6.0.0

BuildRequires: ctest
BuildRequires: xvfb-run

%description
Gazebo Sensors, a component of Gazebo, provides numerous sensor models designed
to generate realistic data from simulation environments. Gazebo Sensors is used
in conjunction with Gazebo Libraries, and especially relies on the rendering
capabilities from Gazebo Rendering and physics simulation from Gazebo Physics.

%package -n libgz-sensors%soversion
Summary: Library of gz-sensors
Group: System/Libraries

%description -n libgz-sensors%soversion
This package contains library libgz-sensors of gz-sensors

%package -n libgz-sensors-air_pressure%soversion
Summary: Library of gz-sensors
Group: System/Libraries

%description -n libgz-sensors-air_pressure%soversion
This package contains library libgz-sensors-air_pressure of gz-sensors

%package -n libgz-sensors-air_speed%soversion
Summary: Library of gz-sensors
Group: System/Libraries

%description -n libgz-sensors-air_speed%soversion
This package contains library libgz-sensors-air_speed of gz-sensors

%package -n libgz-sensors-altimeter%soversion
Summary: Library of gz-sensors
Group: System/Libraries

%description -n libgz-sensors-altimeter%soversion
This package contains library libgz-sensors-altimeter of gz-sensors

%package -n libgz-sensors-boundingbox_camera%soversion
Summary: Library of gz-sensors
Group: System/Libraries

%description -n libgz-sensors-boundingbox_camera%soversion
This package contains library libgz-sensors-boundingbox_camera of gz-sensors

%package -n libgz-sensors-camera%soversion
Summary: Library of gz-sensors
Group: System/Libraries

%description -n libgz-sensors-camera%soversion
This package contains library libgz-sensors-camera of gz-sensors

%package -n libgz-sensors-depth_camera%soversion
Summary: Library of gz-sensors
Group: System/Libraries

%description -n libgz-sensors-depth_camera%soversion
This package contains library libgz-sensors-depth_camera of gz-sensors

%package -n libgz-sensors-dvl%soversion
Summary: Library of gz-sensors
Group: System/Libraries

%description -n libgz-sensors-dvl%soversion
This package contains library libgz-sensors-dvl of gz-sensors

%package -n libgz-sensors-force_torque%soversion
Summary: Library of gz-sensors
Group: System/Libraries

%description -n libgz-sensors-force_torque%soversion
This package contains library libgz-sensors-force_torque of gz-sensors

%package -n libgz-sensors-gpu_lidar%soversion
Summary: Library of gz-sensors
Group: System/Libraries

%description -n libgz-sensors-gpu_lidar%soversion
This package contains library libgz-sensors-gpu_lidar of gz-sensors

%package -n libgz-sensors-imu%soversion
Summary: Library of gz-sensors
Group: System/Libraries

%description -n libgz-sensors-imu%soversion
This package contains library libgz-sensors-imu of gz-sensors

%package -n libgz-sensors-lidar%soversion
Summary: Library of gz-sensors
Group: System/Libraries

%description -n libgz-sensors-lidar%soversion
This package contains library libgz-sensors-lidar of gz-sensors

%package -n libgz-sensors-logical_camera%soversion
Summary: Library of gz-sensors
Group: System/Libraries

%description -n libgz-sensors-logical_camera%soversion
This package contains library libgz-sensors-logical_camera of gz-sensors

%package -n libgz-sensors-magnetometer%soversion
Summary: Library of gz-sensors
Group: System/Libraries

%description -n libgz-sensors-magnetometer%soversion
This package contains library libgz-sensors-magnetometer of gz-sensors

%package -n libgz-sensors-navsat%soversion
Summary: Library of gz-sensors
Group: System/Libraries

%description -n libgz-sensors-navsat%soversion
This package contains library libgz-sensors-navsat of gz-sensors

%package -n libgz-sensors-rendering%soversion
Summary: Library of gz-sensors
Group: System/Libraries

%description -n libgz-sensors-rendering%soversion
This package contains library libgz-sensors-rendering of gz-sensors

%package -n libgz-sensors-rgbd_camera%soversion
Summary: Library of gz-sensors
Group: System/Libraries

%description -n libgz-sensors-rgbd_camera%soversion
This package contains library libgz-sensors-rgbd_camera of gz-sensors

%package -n libgz-sensors-segmentation_camera%soversion
Summary: Library of gz-sensors
Group: System/Libraries

%description -n libgz-sensors-segmentation_camera%soversion
This package contains library libgz-sensors-segmentation_camera of gz-sensors

%package -n libgz-sensors-thermal_camera%soversion
Summary: Library of gz-sensors
Group: System/Libraries

%description -n libgz-sensors-thermal_camera%soversion
This package contains library libgz-sensors-thermal_camera of gz-sensors

%package -n libgz-sensors-wide_angle_camera%soversion
Summary: Library of gz-sensors
Group: System/Libraries

%description -n libgz-sensors-wide_angle_camera%soversion
This package contains library libgz-sensors-wide_angle_camera of gz-sensors

%package -n libgz-sensors-devel
Summary: Development files for gz-sensors
Group: Development/C++

%description -n libgz-sensors-devel
%summary

%prep
%setup

%build
%cmake -GNinja -Wno-dev
%cmake_build

%install
%cmake_install

%check
export CMAKE_PREFIX_PATH="%buildroot%_prefix"
Xvfb :99 -screen 0 1920x1080x24 2>/dev/null &
XVFB_PID=$!
export DISPLAY=:99
export GZ_RENDERING_PLUGIN_PATH="%buildroot%_libdir"
export GZ_RENDERING_DATA_PATH="%buildroot%_datadir/gz/gz-rendering"
%ctest --parallel 1
trap 'kill -TERM "$XVFB_PID" 2>/dev/null || true; wait "$XVFB_PID" 2>/dev/null || true' EXIT

%files -n libgz-sensors%soversion
%doc AUTHORS README.md
%_libdir/libgz-sensors.so.%soversion
%_libdir/libgz-sensors.so.%version

%files -n libgz-sensors-air_pressure%soversion
%_libdir/libgz-sensors-air_pressure.so.%soversion
%_libdir/libgz-sensors-air_pressure.so.%version

%files -n libgz-sensors-air_speed%soversion
%_libdir/libgz-sensors-air_speed.so.%soversion
%_libdir/libgz-sensors-air_speed.so.%version

%files -n libgz-sensors-altimeter%soversion
%_libdir/libgz-sensors-altimeter.so.%soversion
%_libdir/libgz-sensors-altimeter.so.%version

%files -n libgz-sensors-boundingbox_camera%soversion
%_libdir/libgz-sensors-boundingbox_camera.so.%soversion
%_libdir/libgz-sensors-boundingbox_camera.so.%version

%files -n libgz-sensors-camera%soversion
%_libdir/libgz-sensors-camera.so.%soversion
%_libdir/libgz-sensors-camera.so.%version

%files -n libgz-sensors-depth_camera%soversion
%_libdir/libgz-sensors-depth_camera.so.%soversion
%_libdir/libgz-sensors-depth_camera.so.%version

%files -n libgz-sensors-dvl%soversion
%_libdir/libgz-sensors-dvl.so.%soversion
%_libdir/libgz-sensors-dvl.so.%version

%files -n libgz-sensors-force_torque%soversion
%_libdir/libgz-sensors-force_torque.so.%soversion
%_libdir/libgz-sensors-force_torque.so.%version

%files -n libgz-sensors-gpu_lidar%soversion
%_libdir/libgz-sensors-gpu_lidar.so.%soversion
%_libdir/libgz-sensors-gpu_lidar.so.%version

%files -n libgz-sensors-imu%soversion
%_libdir/libgz-sensors-imu.so.%soversion
%_libdir/libgz-sensors-imu.so.%version

%files -n libgz-sensors-lidar%soversion
%_libdir/libgz-sensors-lidar.so.%soversion
%_libdir/libgz-sensors-lidar.so.%version

%files -n libgz-sensors-logical_camera%soversion
%_libdir/libgz-sensors-logical_camera.so.%soversion
%_libdir/libgz-sensors-logical_camera.so.%version

%files -n libgz-sensors-magnetometer%soversion
%_libdir/libgz-sensors-magnetometer.so.%soversion
%_libdir/libgz-sensors-magnetometer.so.%version

%files -n libgz-sensors-navsat%soversion
%_libdir/libgz-sensors-navsat.so.%soversion
%_libdir/libgz-sensors-navsat.so.%version

%files -n libgz-sensors-rendering%soversion
%_libdir/libgz-sensors-rendering.so.%soversion
%_libdir/libgz-sensors-rendering.so.%version

%files -n libgz-sensors-rgbd_camera%soversion
%_libdir/libgz-sensors-rgbd_camera.so.%soversion
%_libdir/libgz-sensors-rgbd_camera.so.%version

%files -n libgz-sensors-segmentation_camera%soversion
%_libdir/libgz-sensors-segmentation_camera.so.%soversion
%_libdir/libgz-sensors-segmentation_camera.so.%version

%files -n libgz-sensors-thermal_camera%soversion
%_libdir/libgz-sensors-thermal_camera.so.%soversion
%_libdir/libgz-sensors-thermal_camera.so.%version

%files -n libgz-sensors-wide_angle_camera%soversion
%_libdir/libgz-sensors-wide_angle_camera.so.%soversion
%_libdir/libgz-sensors-wide_angle_camera.so.%version

%files -n libgz-sensors-devel
%_includedir/gz/sensors%soversion
%_libdir/libgz-sensors*.so
%_cmakedir/gz-sensors*
%_pkgconfigdir/gz-sensors*.pc

%changelog
* Thu Dec 25 2025 Pavel Petrykin <silverducks@altlinux.org> 10.0.0-alt1
- New version.

* Wed Jan 15 2025 Michael Shigorin <mike@altlinux.org> 9.0.0-alt2
- E2K: builds fine.
- Minor spec cleanup.

* Mon Nov 11 2024 Andrey Cherepanov <cas@altlinux.org> 9.0.0-alt1
- New version.

* Mon Oct 02 2023 Andrey Cherepanov <cas@altlinux.org> 8.0.0-alt1
- New version.

* Wed Aug 02 2023 Andrey Cherepanov <cas@altlinux.org> 7.2.0-alt1
- New version.

* Thu Jun 22 2023 Andrey Cherepanov <cas@altlinux.org> 6.7.0-alt2
- Moved .so files to main package.

* Sat May 27 2023 Andrey Cherepanov <cas@altlinux.org> 6.7.0-alt1
- Initial build for Sisyphus.
