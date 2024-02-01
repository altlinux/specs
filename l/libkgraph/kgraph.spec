%define        _unpackaged_files_terminate_build 1
%define        origname kgraph
%define        pypiname %origname

Name:          lib%{origname}
Version:       0.1
Release:       alt0.git2143fd6.1
Summary:       A library for k-nearest neighbor search
License:       BSD-2-Clause
Group:         Sciences/Mathematics
Url:           https://github.com/aaalgo/kgraph
Vcs:           https://github.com/aaalgo/kgraph.git
# XXX: xsimd supports on x86 SSE and ARM neon
ExclusiveArch: aarch64 %ix86 x86_64

Source:        %name-%version.tar
Patch:         config.patch
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libgomp-devel
BuildRequires: boost-devel
BuildRequires: boost-program_options-devel
BuildRequires: xsimd-devel
BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(wheel)
BuildRequires: python3(numpy)
BuildRequires: libnumpy-py3-devel
BuildRequires: libopenblas-devel

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%ifarch x86_64 %ix86
%add_optflags -msse2
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


%prep
%setup
%autopatch

%build
%cmake_insource
%cmake_build
%pyproject_build

%install
%cmakeinstall_std
%pyproject_install


%files
%doc README*
%_libdir/%{name}*.so.*

%files         devel
%doc README*
%_libdir/%{name}*.so
%_includedir/%{origname}*
%_datadir/cmake/%{origname}

%files         devel-static
%doc README*
%_libdir/%{name}*.a

%files         -n python3-module-%pypiname
%doc README*
%python3_sitelibdir/%{pypiname}*.so
%python3_sitelibdir/%{pypiname}*/METADATA


%changelog
* Thu Feb 01 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.1-alt0.git2143fd6.1
- NMU:
  + Fixed FTBFS on aarch64 (don't force SSE2 here)
  + Build only on aarch64 and x86 as the thing requires either x86 SSE2+
    or ARM NEON

* Wed Jan 31 2024 Pavel Skrylev <majioa@altlinux.org> 0.1-alt0.git2143fd6
- initial build the git ref 2143fd6 for Sisyphus
