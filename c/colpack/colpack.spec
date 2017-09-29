Name: colpack
Version: 1.0.10
Release: alt1
Summary: Graph Coloring for Computing Derivatives
License: LGPL v3
Group: Sciences/Mathematics
Url: http://cscapes.cs.purdue.edu/coloringpage/software.htm

# https://github.com/CSCsw/ColPack.git
Source: %name-%version.tar
Patch1: %name-%version-alt-build.patch

BuildRequires: gcc-c++ libgomp-devel

Requires: lib%name = %version-%release

%description
ColPack: Graph Coloring for Computing Derivatives.

%package -n lib%name
Summary: Shared library of Graph Coloring for Computing Derivatives
Group: System/Libraries

%description -n lib%name
ColPack: Graph Coloring for Computing Derivatives.

This package contains shared library of ColPack.

%package -n lib%name-devel
Summary: Development files of Graph Coloring for Computing Derivatives
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
ColPack: Graph Coloring for Computing Derivatives.

This package contains development files of ColPack.

%package examples
Summary: Examples for Graph Coloring for Computing Derivatives
Group: Sciences/Mathematics
Requires: lib%name = %version-%release

%description examples
ColPack: Graph Coloring for Computing Derivatives.

This package contains examples for ColPack.

%prep
%setup
%patch1 -p1

%build
%autoreconf
%configure \
	--enable-static=no \
	--enable-examples
#	--enable-openmp \
%make_build

%install
%makeinstall_std

install -d %buildroot%_bindir
install -m755 .libs/ColPack %buildroot%_bindir
mv %buildroot%prefix/examples/Basic/* %buildroot%_bindir/
mv %buildroot%prefix/examples/Matrix_Compression_and_Recovery/*/* \
	%buildroot%_bindir/

ln -s ColPack %buildroot%_includedir/%name

%pre -n lib%name-devel
rm -fR %_includedir/%name

%files
%doc AUTHORS ChangeLog NEWS README.md Main/Main.cpp
%_bindir/ColPack

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%files examples
%doc SampleDrivers/Basic/*.cpp
%doc SampleDrivers/Matrix_Compression_and_Recovery/*/*.cpp
%_bindir/*
%exclude %_bindir/ColPack

%changelog
* Thu Sep 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.10-alt1
- Updated to upstream version 1.0.10.

* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.9-alt1.git20150217
- Snapshot from git

* Tue Jun 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.9-alt1
- Version 1.0.9

* Thu Sep 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt2
- Fixed install of devel package

* Wed Sep 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt1
- Version 1.0.8

* Thu Dec 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.4-alt1
- Version 1.0.4

* Mon Apr 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1
- Version 1.0.3

* Wed Feb 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt2
- Rebuilt for debuginfo

* Sun Nov 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus

