%define _name openshot

%define ver_major 0.1
%define api_ver 1.0
%def_disable doc

Name: lib%_name
Version: %ver_major.3
Release: alt1

Summary: OpenShot Video Library
Group: System/Libraries
License: GPLv3
Url: https://launchpad.net/%name

Source: %url/%ver_major/%version/+download/%name-%version.tar.gz

%define __python %nil
BuildRequires: gcc-c++ cmake libgomp-devel libunittest-cpp-devel jsoncpp-devel
BuildRequires: %name-audio-devel qt5-multimedia-devel libzeromq-cpp-devel libImageMagick-devel
BuildRequires: libavcodec-devel libavformat-devel libavutil-devel
BuildRequires: libavresample-devel libswscale-devel libavdevice-devel
BuildRequires: rpm-build-python3 python3-devel swig

%description
libopenshot is an open-source, cross-platform C++ library dedicated to
delivering high quality video editing, animation, and playback solutions
to the world. This is the same library which powers OpenShot Video Editor
(version 2.0+) and it could power your next video editing application!
C++, Python, and Ruby are fully supported, and other languages can be
added if requested.

%package devel
Summary: OpenShot Video Library development package
Group: Development/C++
Requires: %name = %version-%release

%description devel
This package contains development libraries and header files
that are needed to write applications that use %name.

%package -n python3-module-%_name
Summary: Python3 bindings for OpenShot Video Library
Group: Development/Python3
Requires: %name = %version-%release

%description -n python3-module-%_name
This package provides Python3 bindings for OpenShot Video Library.

%prep
%setup -D -c -n %name-%version

%build
%cmake -DUSE_SYSTEM_JSONCPP:BOOL=ON
%cmake_build

%install
%cmakeinstall_std

%files
%_libdir/%name.so.*
%doc AUTHORS README

%files devel
%_includedir/%name/
%_libdir/%name.so

%files -n python3-module-%_name
%python3_sitelibdir/*

%changelog
* Fri Jan 27 2017 Yuri N. Sedunov <aris@altlinux.org> 0.1.3-alt1
- first build for Sisyphus


