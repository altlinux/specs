%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%define itkver 4.12

Name: itk-snap
Version: 3.8.0
Release: alt8
Summary: Software application used to segment structures in 3D medical images
Group: Sciences/Medicine
License: GPLv3
URL: http://www.itksnap.org/pmwiki/pmwiki.php

ExclusiveArch: %ix86 x86_64

# https://git.code.sf.net/p/itk-snap/src
Source: %name-%version.tar

Source1: itk-snap.desktop

Patch1: %name-alt-no-git.patch
Patch2: %name-alt-build.patch
Patch3: %name-alt-unbundle.patch
Patch4: %name-alt-glibc-compat.patch
Patch5: %name-alt-vtk-9.1-compat.patch

BuildRequires(pre): rpm-build-ubt
BuildRequires: gcc-c++ cmake
BuildRequires: libitk%itkver-devel
BuildRequires: qt5-declarative-devel
BuildRequires: libcurl-devel

# unbundled dependencies
BuildRequires: libgreedy-devel
BuildRequires: libconvert3d-devel
BuildRequires: jsoncpp-devel

Requires: greedy
Requires: convert3d

%define _description \
ITK-SNAP is a software application \
used to segment structures in 3D medical images. \
It is the product of a decade-long collaboration between \
Paul Yushkevich, Ph.D., of the Penn Image Computing and Science Laboratory (PICSL) \
at the University of Pennsylvania, \
and Guido Gerig, Ph.D., of the Scientific Computing and Imaging Institute (SCI) \
at the University of Utah, whose vision was to create a tool \
that would be dedicated to a specific function, \
segmentation, and would be easy to use and learn. \
ITK-SNAP is free, open-source, and multi-platform. \
 \
ITK-SNAP provides semi-automatic segmentation using active contour methods, \
as well as manual delineation and image navigation. \
In addition to these core functions, ITK-SNAP offers many supporting utilities. \
 \
Some of the core advantages of ITK-SNAP include: \
- Linked cursor for seamless 3D navigation \
- Manual segmentation in three orthogonal planes at once \
- A modern graphical user interface based on Qt \
- Support for many different 3D image formats, including NIfTI and DICOM \
- Support for concurrent, linked viewing, and segmentation of multiple images \
- Support for color, multi-channel, and time-variant images \
- 3D cut-plane tool for fast post-processing of segmentation results \
- Extensive tutorial and video documentation \
 \
Compared to other, larger open-source image analysis tools, \
ITK-SNAP design focuses specifically on the problem of image segmentation, \
and extraneous or unrelated features are kept to a minimum. \
The design also emphasizes interaction and ease of use, \
with the bulk of the development effort dedicated to the user interface.

%description %_description

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

# remove unbundled libraries
rm -rf Common/JSon

%build
%add_optflags -D_FILE_OFFSET_BITS=64

# get SNAP_VERSION_GIT_ data from upstream commit being used to build this package
# git rev-parse --abbrev-ref HEAD
# git rev-parse HEAD
# git show -s --format=%%ci HEAD
%cmake \
	-DSNAP_VERSION_GIT_BRANCH=master \
	-DSNAP_VERSION_GIT_SHA1=7a104c25401ce23599dc8d32ea80f3daae80f379 \
	-DSNAP_VERSION_GIT_TIMESTAMP="2019-06-12 06:53:09 -0400" \
%ifnarch %e2k
	-DOpenGL_GL_PREFERENCE=GLVND \
%endif
	-DSNAP_PACKAGE_QT_PLUGINS:BOOL=OFF \
	-DCMAKE_CXX_STANDARD=14 \
	%nil

%cmake_build

%install
%cmakeinstall_std

# install desktop file and icon
install -d %buildroot%_desktopdir
install -m644 %SOURCE1 %buildroot%_desktopdir/

install -d %buildroot%_datadir/%name
install -m644 GUI/Qt/Resources/logo_square.png %buildroot%_datadir/%name/

%files
%doc COPYING
%doc README.md ReleaseNotes.md
%doc Documentation
%_bindir/itksnap
%_bindir/itksnap-wt
%_libexecdir/snap-%version/ITK-SNAP
%_libdir/lib*.so*
%_desktopdir/*.desktop
%dir %_datadir/%name
%_datadir/%name/logo_square.png

%changelog
* Mon Jan 24 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 3.8.0-alt8
- Rebuilt with VTK-9.1.0.

* Tue Oct 05 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.8.0-alt7
- Fixed build with gcc-11.

* Tue Jun 08 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.8.0-alt6
- Added compatibility to p9.

* Thu Jun 03 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.8.0-alt5
- Added desktop file.

* Fri May 14 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.8.0-alt4
- Rebuilt with VTK-9.0.1.

* Tue Jan 12 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.8.0-alt3
- Fixed build with new glibc.

* Mon Feb 24 2020 Igor Vlasenko <viy@altlinux.ru> 3.8.0-alt2
- rebuild with new gbcm

* Thu Jul 18 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 3.8.0-alt1
- Initial build for ALT.
