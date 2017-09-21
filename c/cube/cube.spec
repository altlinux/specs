Name: cube
License: BSD
Group: Development/Tools
Summary: Performance report explorer for Scalasca and Score-P
Version: 4.3.5
Release: alt1
Url: http://www.scalasca.org/software/cube-4.x/download.html

Source: %name-%version.tar
Source2: status.m4
Patch1: %name-%version-fedora-nocheck.patch
Patch2: %name-%version-alt-linking.patch

BuildRequires: gcc-c++ libqt4-devel zlib-devel uncrustify doxygen
BuildRequires: libdbus-devel flex graphviz texlive-base-bin menu chrpath

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
%setup
%patch1 -p1
%patch2 -p2

# configure.ac uses some macros not provided by autoconf, just copy file with them from previous cube version
cp %SOURCE2 vendor/common/build-config/m4/status.m4

%build
%add_optflags -I%_includedir/dbus-1.0 -L%buildroot%_libexecdir
%autoreconf
%configure \
	--with-backend-compression=full \
	--with-compression=full \
	--with-frontend-compression=full
pushd build-backend
%make_build libcube4.la
%make_build libcube4w.la
popd
export TOPDIR=$PWD
%make_build

%install
install -d %buildroot%_libdir
cp -P $(find ./ -name 'libcube4.so*') %buildroot/%_libdir/
cp -P $(find ./ -name 'libcube4w.so*') %buildroot/%_libdir/
%makeinstall_std

# remove RPATH
for i in %buildroot%_bindir/* %buildroot%_libdir/*.so* %buildroot%_libdir/cube-plugins/*.so* ; do
	chrpath -d $i ||:
done

# remove unpackaged files
find %buildroot -name '*.la' -delete
find %buildroot -name '*.a' -delete

%files
%_bindir/*
%exclude %_bindir/cube-config*
%_datadir/cube
%_datadir/icons/*

%files -n lib%name
%_libdir/*.so.*
%_libdir/cube-plugins/*.so*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_bindir/cube-config*

%files docs
%_docdir/*

%changelog
* Thu Sep 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.3.5-alt1
- Updated to upstream version 4.3.5.

* Fri Jun 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.3-alt1
- Version 4.2.3

* Wed May 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.2-alt1
- Version 4.2.2

* Thu Sep 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2-alt1
- Initial build for Sisyphus

