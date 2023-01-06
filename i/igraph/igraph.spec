%define soname 3

Name: igraph
Version: 0.10.3
Release: alt1
Summary: Library for creating and manipulating graphs

License: GPL-2.0+
Group: System/Libraries
Url: https://igraph.org/

Source: https://github.com/igraph/igraph/releases/download/%version/igraph-%version.tar.gz

BuildRequires: gcc-c++
BuildRequires: cmake rpm-build-ninja
BuildRequires: libxml2-devel
BuildRequires: libgmp-devel
BuildRequires: libarpack-ng-devel
BuildRequires: liblapack-devel
BuildRequires: libopenblas-devel
BuildRequires: libglpk-devel
# CMake Error at src/CMakeLists.txt:28 (flex_target):
#   Unknown CMake command "flex_target"
BuildRequires: flex
# BuildRequires: python3
BuildRequires: /proc

%description
igraph wants to be an efficient platform for
1) complex network analysis and
2) developing and implementing graph algorithms.
It provides flexible and efficient data structures for graphs and related
tasks. It also provides implementation to many classic and new graph
algorithms like: maximum flows, graph isomorphism, scale-free
networks, community structure finding, etc.

%package -n lib%name%soname
Summary: %summary
Group: System/Libraries

%description -n lib%name%soname
igraph wants to be an efficient platform for
1) complex network analysis and
2) developing and implementing graph algorithms.
It provides flexible and efficient data structures for graphs and related
tasks. It also provides implementation to many classic and new graph
algorithms like: maximum flows, graph isomorphism, scale-free
networks, community structure finding, etc.

%package -n lib%name-devel
Summary: Development files for igraph
Group: Development/C
Provides: %name-devel = %EVR

%description -n lib%name-devel
The lib%name-devel package contains the header files and some
documentation needed to develop application with %name.

%prep
%setup
# Cannot find out the version number of this package; IGRAPH_VERSION is missing.
#
# The official igraph tarballs should contain this file, therefore you are
# most likely trying to compile a development version yourself. The development
# versions need Git to be able to determine the version number of igraph.
#
# It seems like you do have Git but it failed to determine the package version number.
#
# We build from git repository instead tarball.
sed -i 's|set(PACKAGE_VERSION "NOTFOUND")|set(PACKAGE_VERSION "%version")|' \
    etc/cmake/version.cmake

%build
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DBUILD_SHARED_LIBS=ON \
    -DIGRAPH_ENABLE_LTO=AUTO \
    -DIGRAPH_ENABLE_TLS=1 \
    -DIGRAPH_USE_INTERNAL_BLAS=0 \
    -DIGRAPH_USE_INTERNAL_LAPACK=0 \
    -DIGRAPH_USE_INTERNAL_ARPACK=0 \
    -DIGRAPH_USE_INTERNAL_GLPK=0 \
    -DIGRAPH_USE_INTERNAL_GMP=0 \
    -DIGRAPH_USE_INTERNAL_PLFIT=1 \
    -DBLA_VENDOR=OpenBLAS \
    -DBLAS_LIBRARIES=%_libdir/libopenblas.so \
    -DLAPACK_LIBRARIES=%_libdir/liblapack.so \
    -DIGRAPH_GRAPHML_SUPPORT=1 \
    -DCMAKE_INSTALL_INCLUDEDIR=include/ \
#
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install
install -Dm0644 doc/igraph.3 %buildroot%_man3dir/igraph.3
find . -name '.arch-ids' | xargs rm -rf

%files -n lib%name%soname
%doc COPYING
%doc AUTHORS CHANGELOG.md doc/html/ ACKNOWLEDGEMENTS.md doc/licenses/
%_libdir/libigraph.so.%{soname}*

%files -n lib%name-devel
%doc examples
%_includedir/igraph
%_libdir/libigraph.so
%_pkgconfigdir/igraph.pc
%_libdir/cmake/igraph/
%_man3dir/igraph.3*

%changelog
* Fri Jan 06 2023 Leontiy Volodin <lvol@altlinux.org> 0.10.3-alt1
- New version (0.10.3).

* Wed Oct 19 2022 Leontiy Volodin <lvol@altlinux.org> 0.10.2-alt1
- New version (0.10.2).

* Fri Sep 16 2022 Leontiy Volodin <lvol@altlinux.org> 0.10.1-alt1.1
- Applied some suggestions for improvements by upstream.

* Wed Sep 14 2022 Leontiy Volodin <lvol@altlinux.org> 0.10.1-alt1
- New version (0.10.1).

* Tue Sep 06 2022 Leontiy Volodin <lvol@altlinux.org> 0.10.0-alt1
- New version (0.10.0).
- Built with openblas instead blas.

* Tue Jun 07 2022 Leontiy Volodin <lvol@altlinux.org> 0.9.9-alt1
- New version (0.9.9).

* Mon Apr 11 2022 Leontiy Volodin <lvol@altlinux.org> 0.9.8-alt1
- New version (0.9.8).

* Thu Mar 24 2022 Leontiy Volodin <lvol@altlinux.org> 0.9.7-alt1
- New version (0.9.7).
- Updated url.

* Mon Jan 17 2022 Leontiy Volodin <lvol@altlinux.org> 0.9.6-alt1
- New version (0.9.6).

* Mon Nov 22 2021 Leontiy Volodin <lvol@altlinux.org> 0.9.5-alt1
- New version (0.9.5).

* Sat Oct 23 2021 Igor Vlasenko <viy@altlinux.org> 0.9.4-alt1.1
- NMU: added Provides: %name-devel for compatibility

* Fri Oct 22 2021 Leontiy Volodin <lvol@altlinux.org> 0.9.4-alt1
- Initial build for ALT Sisyphus (thanks fedora for the spec).
- Built as require for rw and sagemath.
