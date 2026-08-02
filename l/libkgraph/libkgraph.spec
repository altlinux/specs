%define        _unpackaged_files_terminate_build 1
%define        nomen KGraph
%define        pkgname kgraph
%define        pypiname %pkgname

%def_disable   python

Name:          lib%{pkgname}
Version:       0.1p2
Release:       alt0.1
Summary:       A library for k-nearest neighbor search
License:       BSD-2-Clause
Group:         Sciences/Mathematics
Url:           https://github.com/aaalgo/kgraph
Vcs:           https://github.com/aaalgo/kgraph.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libgomp-devel
BuildRequires: boost-devel
BuildRequires: boost-program_options-devel
BuildRequires: pkgconfig(openblas)
#BuildRequires: xsimd-devel
%if_enabled python
BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(numpy)
BuildRequires: libnumpy-py3-devel
%endif

%description
KGraph: A Library for Approximate Nearest Neighbor Search.

KGraph is a library for k-nearest neighbor (k-NN) graph construction and online
k-NN search using a k-NN Graph as index. KGraph implements heuristic algorithms
that are extremely generic and fast:

* KGraph works on abstract objects. The only assumption it makes is that a
  similarity score can be computed on any pair of objects, with a user-provided
  function.
* KGraph is among the fastest of libraries for k-NN search according to recent
  benchmark.

For best generality, the C++ API should be used. A python wrapper is provided
under the module name kgraph, which supports Euclidean and Angular distances on
rows of NumPy matrices.


%package       devel
Group:         Development/C++
Summary:       A library for k-nearest neighbor search development files.

Requires:      cmake
Requires:      gcc-c++
Requires:      libgomp-devel
Requires:      boost-devel
Requires:      boost-program_options-devel
Requires:      pkgconfig(openblas)
#Requires:      xsimd-devel
%if_enabled python
Requires:      rpm-build-pyproject
Requires:      python3(setuptools)
Requires:      python3(wheel)
Requires:      python3(numpy)
Requires:      libnumpy-py3-devel
%endif

%description   devel
A library for k-nearest neighbor search development files.

KGraph: A Library for Approximate Nearest Neighbor Search.

KGraph is a library for k-nearest neighbor (k-NN) graph construction and online
k-NN search using a k-NN Graph as index. KGraph implements heuristic algorithms
that are extremely generic and fast:

* KGraph works on abstract objects. The only assumption it makes is that a
  similarity score can be computed on any pair of objects, with a user-provided
  function.
* KGraph is among the fastest of libraries for k-NN search according to recent
  benchmark.

For best generality, the C++ API should be used. A python wrapper is provided
under the module name kgraph, which supports Euclidean and Angular distances on
rows of NumPy matrices.


%package       devel-static
Group:         Development/C++
Summary:       A library for k-nearest neighbor search static files.

Requires:      %name-devel = %EVR

%description   devel-static
A library for k-nearest neighbor search static files.

KGraph: A Library for Approximate Nearest Neighbor Search.

KGraph is a library for k-nearest neighbor (k-NN) graph construction and online
k-NN search using a k-NN Graph as index. KGraph implements heuristic algorithms
that are extremely generic and fast:

* KGraph works on abstract objects. The only assumption it makes is that a
  similarity score can be computed on any pair of objects, with a user-provided
  function.
* KGraph is among the fastest of libraries for k-NN search according to recent
  benchmark.

For best generality, the C++ API should be used. A python wrapper is provided
under the module name kgraph, which supports Euclidean and Angular distances on
rows of NumPy matrices.


%if_enabled python
%package       -n python3-module-%pypiname
Summary:       Python interface to kgraph
Group:         Development/Python3

%description   -n python3-module-%pypiname
Python interface to kgraph.

KGraph: A Library for Approximate Nearest Neighbor Search.

KGraph is a library for k-nearest neighbor (k-NN) graph construction and online
k-NN search using a k-NN Graph as index. KGraph implements heuristic algorithms
that are extremely generic and fast:

* KGraph works on abstract objects. The only assumption it makes is that a
  similarity score can be computed on any pair of objects, with a user-provided
  function.
* KGraph is among the fastest of libraries for k-NN search according to recent
  benchmark.

For best generality, the C++ API should be used. A python wrapper is provided
under the module name kgraph, which supports Euclidean and Angular distances on
rows of NumPy matrices.
%endif


%prep
%setup

%build
%cmake
%cmake_build
%if_enabled python
%pyproject_build
%endif

%install
%cmakeinstall_std
%if_enabled python
%pyproject_install
%endif


%files
%doc README*
%_libdir/%{name}*.so.*

%files         devel
%doc README*
%_libdir/%{name}*.so
%_includedir/%{pkgname}*
%_datadir/cmake/Modules/Find%{nomen}.cmake

%files         devel-static
%doc README*
%_libdir/%{name}*.a

%if_enabled python
%files         -n python3-module-%pypiname
%doc README*
%python3_sitelibdir/%{pypiname}*.so
%python3_sitelibdir/%{pypiname}*/METADATA
%endif


%changelog
* Sat Aug 01 2026 Pavel Skrylev <majioa@altlinux.org> 0.1p2-alt0.1
- ^ 0.1-alt0.git2143fd6 -> 0.1p2
- - disabled python

* Tue Mar 19 2024 Stanislav Levin <slev@altlinux.org> 0.1-alt0.git2143fd6.3
- NMU: added missing build dependency on setuptools.

* Mon Mar 04 2024 Pavel Skrylev <majioa@altlinux.org> 0.1-alt0.git2143fd6.2
- ! fixed placement and containment of find module for the package

* Thu Feb 01 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.1-alt0.git2143fd6.1
- NMU:
  + Fixed FTBFS on aarch64 (don't force SSE2 here)
  + Build only on aarch64 and x86 as the thing requires either x86 SSE2+
    or ARM NEON

* Wed Jan 31 2024 Pavel Skrylev <majioa@altlinux.org> 0.1-alt0.git2143fd6
- initial build the git ref 2143fd6 for Sisyphus
