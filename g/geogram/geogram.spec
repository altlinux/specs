%define        _unpackaged_files_terminate_build 1

%ifarch loongarch64
%def_disable   legacy_numeric
%else
%def_enable    legacy_numeric
%endif

Name:          geogram
Version:       1.10.1
Release:       alt1
Summary:       Geogram library by INRIA
License:       BSD-3-Clause AND MIT
Group:         Sciences/Mathematics
Url:           https://brunolevy.github.io/geogram/
Vcs:           https://github.com/BrunoLevy/geogram.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-cmake
BuildRequires: cmake
BuildRequires: ctest
BuildRequires: pkg-config
BuildRequires: hostinfo
BuildRequires: gcc-c++
BuildRequires: cmake(imgui)
BuildRequires: cmake(ImGuiColorTextEdit)
BuildRequires: pkgconfig(glfw3)
BuildRequires: pkgconfig(glu)
BuildRequires: pkgconfig(lua-5.4)
BuildRequires: pkgconfig(stb)
BuildRequires: pkgconfig(tbb)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xxf86vm)
BuildRequires: pkgconfig(zlib)
BuildRequires: amgcl-devel
BuildRequires: libann-devel
BuildRequires: libdnet-devel
#BuildRequires: libexploragram-devel
BuildRequires: libgomp-devel
#BuildRequires: libhlbfgs-devel
BuildRequires: libmeshb-devel
BuildRequires: libopennl-devel
BuildRequires: librply-devel
BuildRequires: libtetgen-devel
BuildRequires: libtriangle-devel
BuildRequires: libxatlas-devel

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
Requires:      cmake(imgui)
Requires:      cmake(ImGuiColorTextEdit)
Requires:      pkgconfig(glfw3)
Requires:      pkgconfig(glu)
Requires:      pkgconfig(lua-5.4)
Requires:      pkgconfig(stb)
Requires:      pkgconfig(tbb)
Requires:      pkgconfig(xcursor)
Requires:      pkgconfig(xi)
Requires:      pkgconfig(xinerama)
Requires:      pkgconfig(xrandr)
Requires:      pkgconfig(xxf86vm)
Requires:      pkgconfig(zlib)
Requires:      amgcl-devel
Requires:      libann-devel
Requires:      libdnet-devel
Requires:      libgomp-devel
Requires:      libmeshb-devel
Requires:      libopennl-devel
Requires:      librply-devel
Requires:      libtetgen-devel
Requires:      libtriangle-devel
Requires:      libxatlas-devel

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
Requires:      cmake(imgui)
Requires:      cmake(ImGuiColorTextEdit)
Requires:      pkgconfig(%{name})

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
       -DGEOGRAM_USE_SYSTEM_TEXT_EDITOR:BOOL=ON \
       -DGEOGRAM_LIB_ONLY:BOOL=OFF \
       -DGEOGRAM_TEST_INSTALL_PREFIX=%buildroot%_prefix \
       -DGEOGRAM_TEST_BUILD_JOBS=${NPROCS:-%__nprocs} \
       -DGEOGRAM_WITH_HLBFGS:BOOL=OFF \
       -DGEOGRAM_WITH_LUA:BOOL=OFF \
       -DGEOGRAM_WITH_THIRD_PARTIES:BOOL=OFF \
       -DGEOGRAM_WITH_TBB=ON \
       -DCMAKE_INSTALL_DOCDIR=%_docdir/%name \
%if_enabled legacy_numeric
       -DGEOGRAM_WITH_LEGACY_NUMERICS:BOOL=ON \
%else
       -DGEOGRAM_WITH_LEGACY_NUMERICS:BOOL=OFF \
%endif
       -DGEOGRAM_WITH_EXPLORAGRAM:BOOL=OFF

%cmake_build %{?_enable_legacy_numeric:-j1}

%install
%cmake_install


%check
%ctest


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
%doc src/lib/geogram_gfx/imgui_ext/IMGUI_STDLIB_LICENSE.txt
%_libdir/lib%{name}_gfx*.so.*

%files         -n lib%{name}-devel
%_includedir/%{name}/
%_cmakedir/modules/FindGeogram.cmake
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
* Tue Nov 10 2026 Pavel Skrylev <majioa@altlinux.org> 1.10.1-alt1
- ^ 1.10.0 -> 1.10.1
- + standalone ImGuiColorTextEdit support
- * build dependencies for the Geogram-enabled editor and compatible ImGui
- + CTest checks for installed editor, OpenNL, TetGen and Triangle integration
- * run %%check through %%ctest with consumer preparation handled by CMake
- * use unversioned CMake and pkg-config dependencies where RPM provides them
- * group development dependencies by type and sort them alphabetically
- * synchronize development dependencies with build requirements

* Sat Aug 08 2026 Pavel Skrylev <majioa@altlinux.org> 1.10.0-alt1
- ^ 1.9.9p21.2 -> 1.10.0

* Mon May 04 2026 Pavel Skrylev <majioa@altlinux.org> 1.9.9.21.2-alt0.1
- ^ 1.9.1p2 -> 1.9.9p21.2

* Fri Nov 22 2024 Pavel Skrylev <majioa@altlinux.org> 1.9.1.2-alt1
- ^ 1.7.9 -> 1.9.1p2

* Mon Jan 29 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.7.9-alt2
- NMU: fixed FTBFS on LoongArch:
  + disabled legacy numeric libraries
  + explained that loongarch64 is 64-bit

* Thu Jan 25 2024 Pavel Skrylev <majioa@altlinux.org> 1.7.9-alt1
- initial build for Sisyphus
