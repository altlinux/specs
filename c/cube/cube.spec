%define _unpackaged_files_terminate_build 1

%ifarch %e2k ppc64le
%def_disable qtwebengine
%else
%def_enable qtwebengine
%endif

Name: cube
Version: 4.5
Release: alt2
License: BSD-3-Clause
Group: Development/Tools
Summary: Performance report explorer for Scalasca and Score-P
Url: http://www.scalasca.org/software/cube-4.x/download.html

Source: cubelib-%version.tar
Source1: cubew-%version.tar
Source2: cubegui-%version.tar

Patch1: cube-fedora-no-version-check.patch
Patch2: cube-alt-linking.patch

BuildRequires: gcc-c++ zlib-devel uncrustify doxygen
BuildRequires: libdbus-devel flex graphviz texlive-base-bin
BuildRequires: chrpath
BuildRequires: qt5-base-devel
%if_enabled qtwebengine
BuildRequires: qt5-webengine-devel
%endif

Requires: lib%name = %EVR

%description
Cube, which is used as performance report explorer for Scalasca and
Score-P, is a generic tool for displaying a multi-dimensional
performance space consisting of the dimensions (i) performance metric,
(ii) call path, and (iii) system resource. Each dimension can be
represented as a tree, where non-leaf nodes of the tree can be collapsed
or expanded to achieve the desired level of granularity. In addition,
Cube can display multi-dimensional Cartesian process topologies.

The Cube 4.x series report explorer and the associated Cube4 data format
is provided for Cube files produced with the Score-P performance
instrumentation and measurement infrastructure or the Scalasca version
2.x trace analyzer (and other compatible tools). However, for backwards
compatibility, Cube 4.x can also read and display Cube 3.x data.

%package -n lib%name
Summary: Shared libraries of Cube
Group: System/Libraries

%description -n lib%name
Cube, which is used as performance report explorer for Scalasca and
Score-P, is a generic tool for displaying a multi-dimensional
performance space consisting of the dimensions (i) performance metric,
(ii) call path, and (iii) system resource. Each dimension can be
represented as a tree, where non-leaf nodes of the tree can be collapsed
or expanded to achieve the desired level of granularity. In addition,
Cube can display multi-dimensional Cartesian process topologies.

This package contains shared libraries of Cube.

%package -n lib%name-devel
Summary: Development files of Cube
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
Cube, which is used as performance report explorer for Scalasca and
Score-P, is a generic tool for displaying a multi-dimensional
performance space consisting of the dimensions (i) performance metric,
(ii) call path, and (iii) system resource. Each dimension can be
represented as a tree, where non-leaf nodes of the tree can be collapsed
or expanded to achieve the desired level of granularity. In addition,
Cube can display multi-dimensional Cartesian process topologies.

This package contains development files of Cube.

%package -n lib%{name}gui
Summary: Shared libraries of Cube
Group: System/Libraries

%description -n lib%{name}gui
Cube, which is used as performance report explorer for Scalasca and
Score-P, is a generic tool for displaying a multi-dimensional
performance space consisting of the dimensions (i) performance metric,
(ii) call path, and (iii) system resource. Each dimension can be
represented as a tree, where non-leaf nodes of the tree can be collapsed
or expanded to achieve the desired level of granularity. In addition,
Cube can display multi-dimensional Cartesian process topologies.

This package contains shared libraries of Cube.

%package -n lib%{name}gui-devel
Summary: Development files of Cube
Group: Development/C++
Requires: lib%{name}gui = %EVR

%description -n lib%{name}gui-devel
Cube, which is used as performance report explorer for Scalasca and
Score-P, is a generic tool for displaying a multi-dimensional
performance space consisting of the dimensions (i) performance metric,
(ii) call path, and (iii) system resource. Each dimension can be
represented as a tree, where non-leaf nodes of the tree can be collapsed
or expanded to achieve the desired level of granularity. In addition,
Cube can display multi-dimensional Cartesian process topologies.

This package contains development files of Cube.

%package docs
Summary: Documentation for Cube
Group: Documentation
BuildArch: noarch

%description docs
Cube, which is used as performance report explorer for Scalasca and
Score-P, is a generic tool for displaying a multi-dimensional
performance space consisting of the dimensions (i) performance metric,
(ii) call path, and (iii) system resource. Each dimension can be
represented as a tree, where non-leaf nodes of the tree can be collapsed
or expanded to achieve the desired level of granularity. In addition,
Cube can display multi-dimensional Cartesian process topologies.

This package contains documentation for Cube.

%prep
%setup -n cubelib-%version -b1 -b2

pushd ../cubegui-%version
%patch1 -p1
%patch2 -p2
popd

pushd ..
# Fiddle for cubelib not being installed when building cubegui
cat <<END >cubelib-config
#!/bin/sh
case \$1 in
--cppflags|--cflags) printf '%%s\n' -I$(pwd)/cubelib-%version/inst%_includedir/cubelib ;;
--ldflags)  printf '%%s\n' -L$(pwd)/cubelib-%version/inst%_libdir ;;
--libs) printf '%%s\n' '-lcube4 -lz' ;;
--interface-version) printf '%%s\n' 9:0:2 ;;
esac
END
chmod +x cubelib-config
popd

%build
export CC=gcc
export CXX=g++

%define unhardcode \
  sed -i -e 's/HARDCODE_INTO_LIBS"]="1"/HARDCODE_INTO_LIBS"]="0"/' \\\
         -e "s/hardcode_into_libs='yes'/hardcode_into_libs='no'/"

pushd ../cubew-%version
%autoreconf
pushd build-backend
%autoreconf
popd
pushd build-frontend
%autoreconf
popd
%configure \
	--enable-shared \
	--disable-static \
	--disable-silent-rules \
	%nil

%unhardcode build-backend/config.status
%make_build
popd

%autoreconf
pushd build-frontend
%autoreconf
popd
%configure \
	--enable-shared \
	--disable-static \
	--disable-silent-rules \
	%nil

%unhardcode build-frontend/config.status
%make_build

# Collect it for use by cubegui
make install DESTDIR=$(pwd)/inst
# Wrong paths in .la cause trouble
rm inst%_libdir/*.la

pushd ../cubegui-%version
# Kludge: For some reason the Qt dependencies are found as .so paths
# and libtool re-orders them with libcube4gui after what it
# should link against, and linking fails.
export LIBS="$LIBS -lQt5PrintSupport -lQt5Widgets -lQt5Gui -lQt5Network -lQt5Concurrent -lQt5Core"
%if_enabled qtwebengine
export LIBS="$LIBS -lQt5WebEngineWidgets"
%endif

%autoreconf
pushd build-frontend
%autoreconf
popd
%configure \
	--disable-static \
	--disable-silent-rules \
	--with-platform=linux \
	--with-cubelib=$(pwd)/.. \
	%nil

%unhardcode build-frontend/config.status
%make_build
popd

%install
%makeinstall_std -C ../cubew-%version
%makeinstall_std
%makeinstall_std -C ../cubegui-%version

chrpath -d -k %buildroot%_bindir/* %buildroot%_libdir/{,cube-plugins/}*.so  || :

# remove unpackaged files
find %buildroot -name '*.la' -delete
find %buildroot -name '*.a' -delete

%files
%_bindir/*
%exclude %_bindir/cube_server
%exclude %_bindir/cube*-config
%_libdir/libgraphwidgetcommon-plugin.so.*
%_libdir/cube-plugins
%_datadir/cubegui
%_datadir/icons/cubegui

%files -n lib%name
%_bindir/cube_server
%_libdir/*.so.*
%exclude %_libdir/lib%{name}4gui*.so.*
%exclude %_libdir/libgraphwidgetcommon-plugin.so.*
%_datadir/cubelib
%_datadir/cubew

%files -n lib%name-devel
%_bindir/cubelib-config
%_bindir/cubew-config
%_includedir/cubelib
%_includedir/cubew
%_libdir/*.so
%exclude %_libdir/lib%{name}4gui*.so

%files -n lib%{name}gui
%_libdir/lib%{name}4gui*.so.*

%files -n lib%{name}gui-devel
%_bindir/cubegui-config
%_includedir/cubegui
%_libdir/lib%{name}4gui*.so

%files docs
%_docdir/*

%changelog
* Thu Jan 27 2022 Sergey V Turchin <zerg@altlinux.org> 4.5-alt2
- build without qtwebengine on ppc64le

* Fri Sep 18 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 4.5-alt1
- Updated to upstream version 4.5.

* Thu Sep 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.3.5-alt1
- Updated to upstream version 4.3.5.

* Fri Jun 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.3-alt1
- Version 4.2.3

* Wed May 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.2-alt1
- Version 4.2.2

* Thu Sep 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2-alt1
- Initial build for Sisyphus

