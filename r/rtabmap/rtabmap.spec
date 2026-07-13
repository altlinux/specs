%define major 0
%define minor 23
%define api_ver %major.%minor

Name:    rtabmap
Version: 0.23.8
Release: alt1

Summary: RTAB-Map library and standalone application
License: BSD-3-Clause
Group:   Sciences/Computer science
URL:     https://introlab.github.io/rtabmap/
VCS:     https://github.com/introlab/rtabmap

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: libopencv-devel pcl-devel libpcap-devel libpng-devel eigen3-devel
BuildRequires: eigen3-compat-devel libflann-devel-static libvtk-devel vtk-qt5
BuildRequires: qt5-base-devel openni-devel libfreenect-devel libdc1394-devel
BuildRequires: librealsense-devel libpdal-devel octomap-devel libopengv-devel libyaml-cpp-devel
Requires: lib%name = %EVR

ExclusiveArch: x86_64

%description
RTAB-Map (Real-Time Appearance-Based Mapping) is a RGB-D, Stereo and Lidar
Graph-Based SLAM approach based on an incremental appearance-based loop
closure detector. The loop closure detector uses a bag-of-words approach to
determinate how likely a new image comes from a previous location or a new
location. When a loop closure hypothesis is accepted, a new constraint is
added to the map`s graph, then a graph optimizer minimizes the errors in the
map. A memory management approach is used to limit the number of locations
used for loop closure detection and graph optimization, so that real-time
constraints on large-scale environnements are always respected. RTAB-Map can
be used alone with a handheld Kinect, a stereo camera or a 3D lidar for 6DoF
mapping, or on a robot equipped with a laser rangefinder for 3DoF mapping.

%package -n lib%name
Summary: RTAB-Map shared libraries
Group:   System/Libraries

%description -n lib%name
This package contains the RTAB-Map runtime shared libraries.

%package devel
Summary: Development files for RTAB-Map
Group:   Development/C++
Requires: lib%name = %EVR

%description devel
This package contains headers and CMake config files for building
applications against RTAB-Map.

%package tools
Summary: RTAB-Map command-line tools
Group:   Engineering
Requires: lib%name = %EVR

%description tools
This package contains additional RTAB-Map command-line tools and examples.

%prep
%setup

%build
%cmake \
    -DCMAKE_INSTALL_LIBDIR:PATH=%_lib \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=no \
    -DCMAKE_INSTALL_RPATH:STRING='' \
    -DWITH_CERES=OFF \
    -DWITH_PDAL=ON \
    -DWITH_OCTOMAP=ON \
    -DWITH_OPENGV=ON \
    -DWITH_FREENECT=ON \
    -DWITH_DC1394=ON \
    -DWITH_OPENNI2=OFF \
    -DWITH_FREENECT2=OFF \
    -DWITH_K4W2=OFF \
    -DWITH_K4A=OFF \
    -DWITH_FLYCAPTURE2=OFF \
    -DWITH_ZED=OFF \
    -DWITH_ZEDOC=OFF \
    -DWITH_MYNTEYE=OFF \
    -DWITH_G2O=OFF \
    -DWITH_GTSAM=OFF \
    -DWITH_MRPT=OFF \
    -DWITH_POINTMATCHER=OFF \
    -DWITH_FASTCV=OFF

%cmake_build

%install
%cmake_install

%files
%doc LICENSE README.md
%_bindir/rtabmap
%dir %_datadir/rtabmap
%_datadir/rtabmap/package.xml

%files -n lib%name
%_libdir/librtabmap_core.so.%{major}.%{minor}*
%_libdir/librtabmap_gui.so.%{major}.%{minor}*
%_libdir/librtabmap_utilite.so.%{major}.%{minor}*

%files devel
%_includedir/rtabmap-%api_ver/
%_libdir/librtabmap_core.so
%_libdir/librtabmap_gui.so
%_libdir/librtabmap_utilite.so
%_libdir/rtabmap-%api_ver/

%files tools
%_bindir/rtabmap-res_tool
%_bindir/rtabmap-res_tool-0.3.0
%_bindir/rtabmap-calibration
%_bindir/rtabmap-camera
%_bindir/rtabmap-cidsims_dataset
%_bindir/rtabmap-cleanupLocalGrids
%_bindir/rtabmap-console
%_bindir/rtabmap-databaseViewer
%_bindir/rtabmap-dataRecorder
%_bindir/rtabmap-detectMoreLoopClosures
%_bindir/rtabmap-export
%_bindir/rtabmap-extractObject
%_bindir/rtabmap-euroc_dataset
%_bindir/rtabmap-globalBundleAdjustment
%_bindir/rtabmap-info
%_bindir/rtabmap-kitti_dataset
%_bindir/rtabmap-lidar_viewer
%_bindir/rtabmap-odometryViewer
%_bindir/rtabmap-recovery
%_bindir/rtabmap-reduceGraph
%_bindir/rtabmap-report
%_bindir/rtabmap-reprocess
%_bindir/rtabmap-rgbd_camera
%_bindir/rtabmap-rgbd_dataset

%changelog
* Wed Jul 08 2026 Sergey Palcheh <minergenon@altlinux.org> 0.23.8-alt1
- Initial build for Sisyphus
