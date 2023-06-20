%define _unpackaged_files_terminate_build 1                                                                           
%define ver 6

Name:    gz-sim
Version: 6.14.0
Release: alt1

Summary: Open source robotics simulator. The latest version of Gazebo.
License: Apache-2.0
Group:   Other
Url:     https://github.com/gazebosim/gz-sim

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

ExcludeArch: %ix86

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: python3-dev
BuildRequires: libprotobuf-devel
BuildRequires: libfreeimage-devel
BuildRequires: libogre-devel
BuildRequires: libgperftools-devel
BuildRequires: libtinyxml2-devel
BuildRequires: tbb-devel
BuildRequires: libswscale-devel
BuildRequires: libavdevice-devel
BuildRequires: libavformat-devel
BuildRequires: libavfilter-devel
BuildRequires: libavcodec-devel
BuildRequires: libavutil-devel
BuildRequires: libavresample-devel
BuildRequires: libgts-devel
BuildRequires: libbullet3-devel
BuildRequires: libusb-devel
BuildRequires: libopenal-devel
BuildRequires: libhdf5-devel
BuildRequires: libcurl-devel
BuildRequires: libswresample-devel
BuildRequires: libpcre2-devel
BuildRequires: libpostproc-devel
BuildRequires: protobuf-compiler
BuildRequires: tinyxml-devel
BuildRequires: libtar-devel
BuildRequires: libsdformat-devel
BuildRequires: libgz-msgs-devel >= 8.0.0
BuildRequires: libgz-transport-devel >= 11.0.0
BuildRequires: libgz-common-devel
BuildRequires: libgz-fuel-tools-devel >= 7.0.0
BuildRequires: libgz-plugin-devel
BuildRequires: libgz-sensors-devel >= 6.0.0
BuildRequires: libgz-gui-devel
BuildRequires: libgz-physics-devel
BuildRequires: gz-tools-devel
BuildRequires: libsimbody-devel
BuildRequires: qt5-base-devel
BuildRequires: qt5-quick1-devel
BuildRequires: qt5-quickcontrols2-devel
BuildRequires: libqwt6-qt5-devel
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
BuildRequires: doxygen

# Requires to ign
Requires: gz-tools
Requires: libgz-sim = %EVR

%description
Gazebo simulates multiple robots in a 3D environment, with extensive dynamic
interaction between objects.

%package -n lib%name
Summary: Library of %name
Group: System/Libraries

%description -n lib%name
%summary

%package -n lib%{name}-devel
Summary: Development files for %name
Group: Development/C++

%description -n lib%{name}-devel
%summary
%prep
%setup

%build
%add_optflags -I%_includedir/bullet
%cmake -GNinja -Wno-dev \
       -DQWT_WIN_INCLUDE_DIR=%_includedir/qt5
%ninja_build -C "%_cmake__builddir"

%install
%ninja_install -C "%_cmake__builddir"
install -Dpm 0644 "%_cmake__builddir"/ignition-gazebo%ver.desktop %buildroot%_desktopdir/ignition-gazebo%ver.desktop
install -Dpm 0644 "%_cmake__builddir"/ignition-gazebo%ver.svg %buildroot%_pixmapsdir/ignition-gazebo%ver.svg

%files
%doc AUTHORS README.md
%_datadir/ignition/ignition-gazebo%ver
%_desktopdir/*.desktop
%_pixmapsdir/*.svg

%files -n lib%name
%_libexecdir/ruby/*
%_libdir/lib*.so.*
%_libdir/ign-gazebo-%ver/plugins
%_libdir/python/ignition
%_libdir/python/*.so
%_datadir/ignition/model*.yaml
%_datadir/gz/gz1.completion.d/*.bash_completion.sh
%_datadir/ignition/*.yaml

%files -n lib%{name}-devel
%_includedir/ignition/*
%_libdir/lib*.so
%_libdir/cmake/*
%_libdir/pkgconfig/*.pc

%changelog
* Mon Jun 19 2023 Andrey Cherepanov <cas@altlinux.org> 6.14.0-alt1
- Initial build for Sisyphus.
