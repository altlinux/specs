Name:    apriltag
Version: 3.4.5
Release: alt1

Summary: AprilTag is a visual fiducial system popular for robotics research
License: BSD-2-Clause
Group:   System/Libraries
URL:     https://april.eecs.umich.edu/software/apriltag
VCS:     https://github.com/AprilRobotics/apriltag

Source: %name-%version.tar
Patch0: use-cmake-install-libdir-for-python.patch

BuildRequires(pre): rpm-macros-cmake rpm-macros-python3
BuildRequires: cmake gcc-c++
BuildRequires: python3-dev python3-module-numpy libnumpy-py3-devel
BuildRequires: libopencv-devel

%description
It is a fast C library for detecting visual markers (fiducials) with improved
speed (>2x), accuracy on small tags, flexible layout and pose estimation,
minimal dependencies, and is widely used in robotics.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

%description devel
This package contains the headers and development files for %name.

%package -n python3-module-%name
Summary: Python 3 bindings for %name
Group: Development/Python3
Requires: %name = %EVR
Requires: python3-module-numpy

%description -n python3-module-%name
This package contains Python 3 bindings for the %name library.

%prep
%setup
%patch0 -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc LICENSE.md README.md
%_bindir/apriltag_demo
%_bindir/opencv_demo
%_libdir/libapriltag.so.*

%files devel
%_includedir/apriltag/
%_libdir/libapriltag.so
%_libdir/apriltag/
%_pkgconfigdir/apriltag.pc

%files -n python3-module-%name
%python3_sitelibdir/apriltag*.so

%changelog
* Sun Jul 12 2026 Sergey Palcheh <minergenon@altlinux.org> 3.4.5-alt1
- Initial build for Sisyphus
