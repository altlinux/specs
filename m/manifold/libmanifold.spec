%set_verify_elf_method strict
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_with tbb
%def_with assimp
%def_with clipper2
%def_with python

%define soname 3

Name: manifold
Version: 3.3.2
Release: alt2
Summary: Geometry library for topological robustness
License: Apache-2.0
Group: System/Libraries
Url: https://github.com/elalish/manifold
Vcs: https://github.com/elalish/manifold

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires: gcc-c++
%if_with tbb
BuildRequires: tbb-devel
%endif
%if_with assimp
BuildRequires: libassimp-devel libpoly2tri-devel libminizip-devel
%endif
%if_with clipper2
BuildRequires: libClipper2-devel
%endif
%if_with python
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-nanobind
%endif

%description
Manifold is a geometry library dedicated to creating and operating on manifold
triangle meshes. A manifold mesh is a mesh that represents a solid object, and
so is very important in manufacturing, CAD, structural analysis, etc. Manifold
also supports arbitrary vertex properties and enables mapping of materials for
rendering use-cases. Our primary goal is reliability: guaranteed manifold
output without caveats or edge cases. Our secondary goal is performance:
efficient algorithms that make extensive use of parallelization, or pipelining
when only a single thread is available.

%package -n lib%name%{soname}
Summary: %name library
Group: System/Libraries
Provides: lib%name = %EVR

%package -n python3-module-%name
Summary: Python3 module for %name
Group: Development/Python3

%description -n lib%name%{soname}
Manifold is a geometry library dedicated to creating and operating on manifold
triangle meshes. A manifold mesh is a mesh that represents a solid object, and
so is very important in manufacturing, CAD, structural analysis, etc. Manifold
also supports arbitrary vertex properties and enables mapping of materials for
rendering use-cases. Our primary goal is reliability: guaranteed manifold
output without caveats or edge cases. Our secondary goal is performance:
efficient algorithms that make extensive use of parallelization, or pipelining
when only a single thread is available.

%package -n lib%name-devel
Summary: %name development headers and libraries
Group: Development/C++

%description -n lib%name-devel
%name development headers and libraries

%description -n python3-module-%name
Python3 module for %name

%prep
%setup

%build
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DMANIFOLD_TEST=OFF \
%if_with tbb
	-DMANIFOLD_PAR=ON \
%endif
%if_with assimp
	-DMANIFOLD_EXPORT=ON \
%endif
%if_with clipper2
	-DMANIFOLD_CROSS_SECTION=ON \
%endif
%if_with python
	-DMANIFOLD_PYBIND=ON \
%endif
%ifarch %ix86 %e2k
	-DMANIFOLD_STRICT=OFF \
%endif
	-DMANIFOLD_DOWNLOADS=OFF \
	-DMANIFOLD_OPTIMIZED=ON
%cmake_build

%install
%cmake_install

%files -n lib%name%{soname}
%_libdir/lib%{name}*.so.*

%files -n lib%name-devel
%_libdir/lib%{name}*.so
%_includedir/%name
%_pkgconfigdir/%name.pc
%_libdir/cmake/%name

%if_with python
%files -n python3-module-%name
%python3_sitelibdir/*.so
%python3_sitelibdir/*.pyi
%endif

%changelog
* Sat May 09 2026 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 3.3.2-alt2
- e2k build fix

* Thu Nov 20 2025 L.A. Kostis <lakostis@altlinux.ru> 3.3.2-alt1
- 3.3.2.
- enable python bindings.
- %%ix86: disable Werror.

* Wed Aug 13 2025 L.A. Kostis <lakostis@altlinux.ru> 3.2.1-alt1
- 3.2.1.

* Fri Jul 18 2025 L.A. Kostis <lakostis@altlinux.ru> 3.2.0-alt1
- Initial build for ALTLinux.
