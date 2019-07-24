%define _unpackaged_files_terminate_build 1

%define itkver 4.12

Name: greedy
Version: 1.0.1
Release: alt1.git79e69e3
Summary: Very fast greedy diffeomorphic registration code
Group: Sciences/Medicine
License: GPLv3
URL: https://sites.google.com/view/greedyreg/about

ExclusiveArch: %ix86 x86_64

# https://github.com/pyushkevich/greedy.git
Source: %name-%version.tar

Patch1: %name-alt-no-git.patch
Patch2: %name-alt-build.patch
Patch3: %name-alt-install.patch

BuildRequires: gcc-c++ cmake
BuildRequires: libitk%itkver-devel

Requires: lib%name = %EVR

%define _description \
Greedy is a tool for fast medical image registration. \
It was developed by Paul Yushkevich \
at the Penn Image Computing and Science Lab at the University of Pennsylvania. \
The motivation for developing greedy was to have a really fast \
CPU-based deformable image registration tool that could be used in applications \
where many images have to be registered in parallel \
- like multi-atlas image segmentation. \
 \
Greedy borrows many concepts (and some implementation strategies) \
from the Symmetric Normalization (SyN) in ANTS. \
But greedy is non-symmetric, which makes it faster \
(in applications like multi-atlas segmentation, \
symmetric property is not required). \
Greedy also uses highly optimized code for \
image metric computation that adds extra speed. \
 \
This work is funded by the NIH/NIBIB under \
grants R01 EB-017255 and R01 EB-014146 \
 \
Main Features \
- Greedy diffeomorphic image registration \
- Affine and rigid image registration (also, matching by moments of inertia) \
- Support for normalized cross-correlation, mutual information, and sum of squared differences metrics \
- Multiple images and multi-component images can be registered \
- Fast CPU-based implementation (takes advantage of multi-threading and SIMD) \
- Supports 2D and 3D registration \
- Masks can be supplied for restricting registration to a region \
- Supports NIFTI image format \
- Single executable for registration and image/mesh re-slicing \
- High-level API that can be called from other software (e.g., ITK-SNAP) \
- Free open-source software (licensed under GPL3) \
- It works!

%description %_description

%package -n lib%name
Summary: Very fast greedy diffeomorphic registration code
Group: System/Libraries

%description -n lib%name %_description

This package contains shared libraries.

%package -n lib%name-devel
Summary: Very fast greedy diffeomorphic registration code
Group: Development/C++
Requires: lib%name = %EVR
# Following dependencies are duplicates from build dependencies
Requires: libitk%itkver-devel

%description -n lib%name-devel %_description

This package contains development files.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%ifarch %ix86
%add_optflags -msse2 -mfpmath=sse
%endif

# get GREEDY_VERSION_GIT_ data from upstream commit being used to build this package
# git rev-parse --abbrev-ref HEAD
# git rev-parse HEAD
# git show -s --format=%%ci HEAD
%cmake \
	-DGREEDY_VERSION_GIT_BRANCH=master \
	-DGREEDY_VERSION_GIT_SHA1=79e69e3d7b4d1e88cf87218ca99d6d373d323f9f \
	-DGREEDY_VERSION_GIT_TIMESTAMP="2019-03-21 13:41:18 -0400" \
	%nil

%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/greedy

%files -n lib%name
%doc README.md
%_libdir/lib*.so.*

%files -n lib%name-devel
%_libdir/lib*.so
%_includedir/*

%changelog
* Wed Jul 17 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.1-alt1.git79e69e3
- Initial build for ALT.
