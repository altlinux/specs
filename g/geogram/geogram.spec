Name:          geogram
Version:       1.7.9
Release:       alt1
Summary:       Geogram library by INRIA
License:       WTFPL
Group:         Sciences/Mathematics
Url:           http://alice.loria.fr/index.php/software/4-library/75-geogram.html
Vcs:           https://github.com/alicevision/geogram.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
Patch:         patch.patch
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: hostinfo
BuildRequires: gcc-c++
BuildRequires: doxygen
BuildRequires: libtetgen-devel
BuildRequires: libtriangle-devel
BuildRequires: liblua5.3-devel
#BuildRequires: libexploragram-devel
#BuildRequires: libhlbfgs-devel
BuildRequires: libglfw3-devel
BuildRequires: libdnet-devel
BuildRequires: libgomp13-devel
BuildRequires: libGLU-devel
BuildRequires: libXxf86vm-devel
BuildRequires: libXcursor-devel
BuildRequires: libXinerama-devel
BuildRequires: libXi-devel
BuildRequires: libGLU-devel
BuildRequires: libXrandr-devel

%description
Geogram is a programming library of geometric algorithms. It includes a simple
yet efficient Mesh data structure (for surfacic and volumetric meshes), exact
computer arithmetics (a-la Shewchuck, implemented in GEO::expansion ), a
predicate code generator (PCK : Predicate Construction Kit), standard geometric
predicates (orient/insphere), Delaunay triangulation, Voronoi diagram, spatial
search data structures, spatial sorting) and less standard ones (more general
geometric predicates, intersection between a Voronoi diagram and a triangular
or tetrahedral mesh embedded in n dimensions). The latter is used by
FWD/WarpDrive, the first algorithm that computes semi-discrete Optimal
Transport in 3d that scales up to 1 million Dirac masses.


%package       -n lib%{name}
Group:         System/Libraries
Summary:       Library code for %name

%description   -n lib%{name}
Geogram is a programming library of geometric algorithms. It includes a simple
yet efficient Mesh data structure (for surfacic and volumetric meshes), exact
computer arithmetics (a-la Shewchuck, implemented in GEO::expansion ), a
predicate code generator (PCK : Predicate Construction Kit), standard geometric
predicates (orient/insphere), Delaunay triangulation, Voronoi diagram, spatial
search data structures, spatial sorting) and less standard ones (more general
geometric predicates, intersection between a Voronoi diagram and a triangular
or tetrahedral mesh embedded in n dimensions). The latter is used by
FWD/WarpDrive, the first algorithm that computes semi-discrete Optimal
Transport in 3d that scales up to 1 million Dirac masses.


%package       -n lib%{name}-devel
Group:         Development/C++
Summary:       Development files for %name

Requires:      lib%{name} = %EVR
Requires:      cmake
Requires:      hostinfo
Requires:      gcc-c++
Requires:      doxygen
Requires:      libtetgen-devel
Requires:      libtriangle-devel
Requires:      liblua5.3-devel
Requires:      libglfw3-devel
Requires:      libdnet-devel
Requires:      libgomp13-devel
Requires:      libGLU-devel
Requires:      libXxf86vm-devel
Requires:      libXcursor-devel
Requires:      libXinerama-devel
Requires:      libXi-devel
Requires:      libGLU-devel
Requires:      libXrandr-devel

%description   -n lib%{name}-devel
Geogram is a programming library of geometric algorithms. It includes a simple
yet efficient Mesh data structure (for surfacic and volumetric meshes), exact
computer arithmetics (a-la Shewchuck, implemented in GEO::expansion ), a
predicate code generator (PCK : Predicate Construction Kit), standard geometric
predicates (orient/insphere), Delaunay triangulation, Voronoi diagram, spatial
search data structures, spatial sorting) and less standard ones (more general
geometric predicates, intersection between a Voronoi diagram and a triangular
or tetrahedral mesh embedded in n dimensions). The latter is used by
FWD/WarpDrive, the first algorithm that computes semi-discrete Optimal
Transport in 3d that scales up to 1 million Dirac masses.


%package       -n lib%{name}-gfx
Group:         System/Libraries
Summary:       Library code for %name

%description   -n lib%{name}-gfx
Geogram is a programming library of geometric algorithms. It includes a simple
yet efficient Mesh data structure (for surfacic and volumetric meshes), exact
computer arithmetics (a-la Shewchuck, implemented in GEO::expansion ), a
predicate code generator (PCK : Predicate Construction Kit), standard geometric
predicates (orient/insphere), Delaunay triangulation, Voronoi diagram, spatial
search data structures, spatial sorting) and less standard ones (more general
geometric predicates, intersection between a Voronoi diagram and a triangular
or tetrahedral mesh embedded in n dimensions). The latter is used by
FWD/WarpDrive, the first algorithm that computes semi-discrete Optimal
Transport in 3d that scales up to 1 million Dirac masses.


%package       -n lib%{name}-gfx-devel
Group:         Development/C++
Summary:       Development files for %name

Requires:      lib%{name}-gfx = %EVR
Requires:      lib%{name}-devel = %EVR

%description   -n lib%{name}-gfx-devel
Geogram is a programming library of geometric algorithms. It includes a simple
yet efficient Mesh data structure (for surfacic and volumetric meshes), exact
computer arithmetics (a-la Shewchuck, implemented in GEO::expansion ), a
predicate code generator (PCK : Predicate Construction Kit), standard geometric
predicates (orient/insphere), Delaunay triangulation, Voronoi diagram, spatial
search data structures, spatial sorting) and less standard ones (more general
geometric predicates, intersection between a Voronoi diagram and a triangular
or tetrahedral mesh embedded in n dimensions). The latter is used by
FWD/WarpDrive, the first algorithm that computes semi-discrete Optimal
Transport in 3d that scales up to 1 million Dirac masses.


%package       -n vorpalite
Group:         Sciences/Mathematics
Summary:       Vorpalite executables for %name

%description   -n vorpalite
Geogram is a programming library of geometric algorithms. It includes a simple
yet efficient Mesh data structure (for surfacic and volumetric meshes), exact
computer arithmetics (a-la Shewchuck, implemented in GEO::expansion ), a
predicate code generator (PCK : Predicate Construction Kit), standard geometric
predicates (orient/insphere), Delaunay triangulation, Voronoi diagram, spatial
search data structures, spatial sorting) and less standard ones (more general
geometric predicates, intersection between a Voronoi diagram and a triangular
or tetrahedral mesh embedded in n dimensions). The latter is used by
FWD/WarpDrive, the first algorithm that computes semi-discrete Optimal
Transport in 3d that scales up to 1 million Dirac masses.


%prep
%setup
%autopatch

%build
%cmake -DVORPALINE_PLATFORM:STRING=AltLinux-gcc \
       -DARCH:STRING=%_arch \
       -DVORPALINE_BUILD_DYNAMIC:BOOL=ON \
       -DGEOGRAM_USE_SYSTEM_GLFW3:BOOL=ON \
       -DGEOGRAM_WITH_HLBFGS:BOOL=OFF \
       -DGEOGRAM_WITH_EXPLORAGRAM:BOOL=OFF

%cmake_build -j1

%install
%cmakeinstall_std


%files
%doc README*
%_bindir/geo*

%files         -n vorpalite
%_bindir/vorp*
%_docdir/%{name}/

%files         -n lib%{name}
%doc README*
%_libdir/lib%{name}.*so.*
%_libdir/lib%{name}_num*.so.*

%files         -n lib%{name}-gfx
%_libdir/lib%{name}_gfx*.so.*

%files         -n lib%{name}-devel
%_includedir/%{name}1/%{name}/
%_libdir/cmake/*
%_pkgconfigdir/%{name}1.pc
%_libdir/lib%{name}.*so
%_libdir/lib%{name}_num*.so
   
%files         -n lib%{name}-gfx-devel
%_includedir/%{name}1/%{name}_gfx/
%_pkgconfigdir/%{name}_gfx1.pc
%_libdir/lib%{name}_gfx*.so

%changelog
* Thu Jan 25 2024 Pavel Skrylev <majioa@altlinux.org> 1.7.9-alt1
- initial build for Sisyphus
