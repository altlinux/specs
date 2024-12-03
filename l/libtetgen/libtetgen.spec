%define        _unpackaged_files_terminate_build 1
%define        oname tetgen

Name:          lib%oname
Version:       1.6.0
Release:       alt1
Summary:       A Quality Tetrahedral Mesh Generator and a 3D Delaunay Triangulator
License:       MIT
Group:         Sciences/Mathematics
Url:           https://wias-berlin.de/software/index.jsp?id=TetGen&lang=1
Vcs:           https://github.com/libigl/tetgen.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++

%description
TetGen is a program for generating tetrahedral meshes from arbitrary 3D
polyhedral domains. TetGen generates exactly constrained Delaunay
tetrahedralizations, boundary-conforming Delaunay meshes and Voronoi partitions.

TetGen provides various functions to generate high-quality and adaptive
tetrahedral meshes suitable for numerical methods such as finite element or
finite volume methods.

TetGen is written in C++. It can be compiled either into a standalone program
called from the command line or into a library for linking with other programs.
All common operating systems, such as Unix/Linux, MacOS, Windows, etc. are
supported.


%package       -n %oname
Group:         Sciences/Mathematics
Summary:       Executables for %name

%description   -n %oname
Executable for %name.

TetGen is a program for generating tetrahedral meshes from arbitrary 3D
polyhedral domains. TetGen generates exactly constrained Delaunay
tetrahedralizations, boundary-conforming Delaunay meshes and Voronoi partitions.

TetGen provides various functions to generate high-quality and adaptive
tetrahedral meshes suitable for numerical methods such as finite element or
finite volume methods.

TetGen is written in C++. It can be compiled either into a standalone program
called from the command line or into a library for linking with other programs.
All common operating systems, such as Unix/Linux, MacOS, Windows, etc. are
supported.



%package       devel
Group:         Development/C++
Summary:       Development files for %name

Requires:      cmake
Requires:      gcc-c++

%description   devel
Development files for %name.

TetGen is a program for generating tetrahedral meshes from arbitrary 3D
polyhedral domains. TetGen generates exactly constrained Delaunay
tetrahedralizations, boundary-conforming Delaunay meshes and Voronoi partitions.

TetGen provides various functions to generate high-quality and adaptive
tetrahedral meshes suitable for numerical methods such as finite element or
finite volume methods.

TetGen is written in C++. It can be compiled either into a standalone program
called from the command line or into a library for linking with other programs.
All common operating systems, such as Unix/Linux, MacOS, Windows, etc. are
supported.


%prep
%setup

%build
%cmake -DARCH:STRING=%_arch \
       -DBUILD_EXECUTABLE=ON \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \

%cmake_build

%install
%cmakeinstall_std

%files
%doc README*
%_libdir/%{name}.*so.*
%_libdir/%{name}*.*so.*

%files         -n %oname
%doc README*
%_bindir/%{oname}

%files         devel
%doc README*
%_includedir/%{oname}*
%_cmakedir/*
%_libdir/%{name}*.*so


%changelog
* Fri Nov 29 2024 Pavel Skrylev <majioa@altlinux.org> 1.6.0-alt1
- initial build for Sisyphus
