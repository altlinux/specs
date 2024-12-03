%define        _unpackaged_files_terminate_build 1

Name:          geogram
Version:       1.9.1.2
Release:       alt1
Summary:       Geogram library by INRIA
License:       BSD-3-Clause
Group:         Sciences/Mathematics
Url:           https://brunolevy.github.io/geogram/
Vcs:           https://github.com/BrunoLevy/geogram.git

%ifarch loongarch64
%def_disable legacy_numeric
%else
%def_enable legacy_numeric
%endif

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: hostinfo
BuildRequires: gcc-c++
BuildRequires: doxygen
BuildRequires: liblua5.3-devel
#BuildRequires: libexploragram-devel
#BuildRequires: libhlbfgs-devel
BuildRequires: libglfw3-devel
BuildRequires: libdnet-devel
BuildRequires: libgomp14-devel
BuildRequires: libGLU-devel
BuildRequires: libXxf86vm-devel
BuildRequires: libXcursor-devel
BuildRequires: libXinerama-devel
BuildRequires: libXi-devel
BuildRequires: libGLU-devel
BuildRequires: libXrandr-devel
BuildRequires: libimgui-devel
BuildRequires: libImGuiColorTextEdit-devel
BuildRequires: librply-devel
BuildRequires: libmeshb-devel
BuildRequires: amgcl-devel
BuildRequires: libxatlas-devel
BuildRequires: libtetgen-devel
BuildRequires: libtriangle-devel
BuildRequires: zlib-devel

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

%build
%cmake -DVORPALINE_PLATFORM:STRING=AltLinux-gcc \
       -DARCH:STRING=%_arch \
       -DGEOGRAM_SYSTEM_NAME=%name \
       -DGEOGRAMGFX_SYSTEM_NAME=%{name}_gfx \
       -DVORPALINE_BUILD_DYNAMIC:BOOL=ON \
       -DGEOGRAM_USE_SYSTEM_GLFW3:BOOL=ON \
       -DGEOGRAM_WITH_HLBFGS:BOOL=OFF \
       -DVORPALINE_VERSION_RC:BOOL=OFF \
       -DGEOGRAM_WITH_LUA:BOOL=OFF \
       -DGEOGRAM_WITH_THIRD_PARTIES:BOOL=OFF \
       -DCMAKE_INSTALL_DOCDIR=%_docdir/%name \
%if_enabled legacy_numeric
       -DGEOGRAM_WITH_LEGACY_NUMERICS:BOOL=ON \
%else
       -DGEOGRAM_WITH_LEGACY_NUMERICS:BOOL=OFF \
%endif
       -DGEOGRAM_WITH_EXPLORAGRAM:BOOL=OFF

%cmake_build %{?_enable_legacy_numeric:-j1}

%install
%cmakeinstall_std


%files
%doc README*
%_bindir/geo*
%_docdir/%{name}/

%files         -n vorpalite
%_bindir/vorp*

%files         -n lib%{name}
%doc README*
%_libdir/lib%{name}.*so.*
%if_enabled legacy_numeric
%_libdir/lib%{name}_num*.so.*
%endif

%files         -n lib%{name}-gfx
%_libdir/lib%{name}_gfx*.so.*

%files         -n lib%{name}-devel
%_includedir/%{name}/
%_libdir/cmake/*
%_pkgconfigdir/%{name}.pc
%_libdir/lib%{name}.*so
%if_enabled legacy_numeric
%_libdir/lib%{name}_num*.so
%endif
   
%files         -n lib%{name}-gfx-devel
%_includedir/%{name}_gfx/
%_pkgconfigdir/%{name}_gfx.pc
%_libdir/lib%{name}_gfx*.so

%changelog
* Fri Nov 22 2024 Pavel Skrylev <majioa@altlinux.org> 1.9.1.2-alt1
- 1.7.9 -> 1.9.1p2

* Mon Jan 29 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.7.9-alt2
- NMU: fixed FTBFS on LoongArch:
  + disabled legacy numeric libraries
  + explained that loongarch64 is 64-bit

* Thu Jan 25 2024 Pavel Skrylev <majioa@altlinux.org> 1.7.9-alt1
- initial build for Sisyphus
