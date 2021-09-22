%define _unpackaged_files_terminate_build 1

%define itkver 4.12

Name: convert3d
Version: 1.1.0
Release: alt3.git61a9bf2
Summary: Convert 3D images between common file formats
Group: Sciences/Medicine
License: GPLv3
URL: http://www.itksnap.org/pmwiki/pmwiki.php?n=Convert3D.Documentation

ExclusiveArch: %ix86 x86_64

# https://github.com/pyushkevich/c3d.git
Source: %name-%version.tar

Patch1: %name-alt-build.patch
Patch2: %name-alt-install.patch

BuildRequires: gcc-c++ cmake
BuildRequires: libitk%itkver-devel
BuildRequires: qt5-base-devel

Requires: lib%name = %EVR

%define _description \
Convert3d is a command-line tool for converting 3D images \
between common file formats. \
The tool also includes a growing list of commands for image manipulation, \
such as thresholding and resampling. \
The tool can also be used to obtain information about image files.

%description 

%_description
%package gui
Summary: Convert 3D images between common file formats
Group: Sciences/Medicine
Requires: %name = %EVR

%description gui 

%_description
%package -n lib%name
Summary: Convert 3D images between common file formats
Group: System/Libraries

%description -n lib%name 

This package contains shared libraries.

%_description
%package -n lib%name-devel
Summary: Convert 3D images between common file formats
Group: Development/C++
Requires: lib%name = %EVR
# Following dependencies are duplicates from build dependencies
Requires: libitk%itkver-devel

%description -n lib%name-devel 

This package contains development files.

%_description
%prep
%setup
%patch1 -p1
%patch2 -p1

%build
%cmake \
	%_cmake_skip_rpath \
	-DBUILD_GUI:BOOL=ON \
	-DCMAKE_CXX_STANDARD=14 \
	%nil

%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/c2d
%_bindir/c3d
%_bindir/c3d_affine_tool
%_bindir/c4d

%files gui
%_bindir/c3d_gui
%_libexecdir/c3d_gui-%version/Convert3DGUI

%files -n lib%name
%_libdir/lib*.so.*

%files -n lib%name-devel
%_libdir/lib*.so
%_includedir/*

%changelog
* Wed Sep 22 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.0-alt3.git61a9bf2
- Fixed build with gcc-11.

* Tue Jun 01 2021 Arseny Maslennikov <arseny@altlinux.org> 1.1.0-alt2.git61a9bf2.1
- NMU: spec: adapted to new cmake macros.

* Mon Feb 24 2020 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2.git61a9bf2
- rebuild with new gbcm

* Thu Jul 18 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.0-alt1.git61a9bf2
- Initial build for ALT.
