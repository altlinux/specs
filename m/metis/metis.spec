%define sover 1
Name: metis
Version: 5.0.2
Release: alt2
Summary: Family of Multilevel Partitioning Algorithms
License: GPL
Group: Sciences/Mathematics
Url: http://glaros.dtc.umn.edu/gkhome/views/metis
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %name.pc

BuildPreReq: cmake gcc-c++ libpcre-devel

%description
METIS is a software package for partitioning unstructured graphs,
partitioning meshes, and computing fill-reducing orderings of sparse
matrices.

%package -n lib%name
Summary: Shared library of METIS
Group: System/Libraries

%description -n lib%name
METIS is a software package for partitioning unstructured graphs,
partitioning meshes, and computing fill-reducing orderings of sparse
matrices.

This package contains shared library of METIS.

%package -n lib%name-devel
Summary: Development files of METIS
Group: Development/C
Requires: lib%name = %version-%release
Conflicts: lib%name-devel < %version-%release
Obsoletes: lib%name-devel < %version-%release

%description -n lib%name-devel
METIS is a software package for partitioning unstructured graphs,
partitioning meshes, and computing fill-reducing orderings of sparse
matrices.

This package contains development files of METIS.

%package -n lib%name-devel-doc
Summary: Development documentation of METIS
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
METIS is a software package for partitioning unstructured graphs,
partitioning meshes, and computing fill-reducing orderings of sparse
matrices.

This package contains development documentation of METIS.

%package examples
Summary: Example graphs for METIS
Group: Development/Documentation
BuildArch: noarch

%description examples
METIS is a software package for partitioning unstructured graphs,
partitioning meshes, and computing fill-reducing orderings of sparse
matrices.

METIS is written in ANSI C and should compile on Unix systems that have
a ANSI C compiler.

This package contains example graphs for METIS.

%prep
%setup
install -m644 %SOURCE1 .

%build
FLAGS="%optflags -I%_includedir/pcre"
cmake \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING="$FLAGS" \
	-DCMAKE_CXX_FLAGS:STRING="$FLAGS" \
	-DCMAKE_Fortran_FLAGS:STRING="$FLAGS" \
	-DCMAKE_STRIP:FILEPATH="bin/echo" \
	-DPCRE:BOOL=ON \
	-DSOVER=%sover \
	.

%make_build VERBOSE=1
sed -i 's|@VERSION@|%version|' %name.pc

%install
%makeinstall_std
%ifarch x86_64
	install -d %buildroot%_libdir
	mv %buildroot%_libexecdir/* %buildroot%_libdir/
%endif

install -d %buildroot%_includedir/%name
mv %buildroot%_includedir/*.h %buildroot%_includedir/%name/

install -d %buildroot%_docdir/%name
install -d %buildroot%_datadir/%name
install -d %buildroot%_pkgconfigdir

install -m644 manual/*.pdf %buildroot%_docdir/%name
install -m644 graphs/* %buildroot%_datadir/%name

install -m644 %name.pc %buildroot%_pkgconfigdir

%pre -n lib%name-devel
rm -fR %_libexecdir/metis

%files
%doc Changelog LICENSE.txt
%_bindir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*

%files -n lib%name-devel-doc
%_docdir/%name

%files examples
%_datadir/%name

%changelog
* Fri Jun 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0.2-alt2
- Removed native directory %_libexecdir/metis

* Wed Dec 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0.2-alt1
- Version 5.0.2

* Fri Sep 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0.1-alt1
- Version 5.0.1

* Thu Apr 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt1
- Version 4.0.3
- Disabled devel-static package

* Fri Feb 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt9
- Moved libraries into %_libdir

* Wed Feb 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt8
- Rebuilt for debuginfo

* Wed Oct 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt7
- Rebuilt for soname set-versions

* Tue Jul 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt6
- Moved shared libraries and headers into /usr/lib/metis

* Fri Jul 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt5
- Avoided conflict with parmetis

* Fri Aug 28 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt4
- Added shared library and pkg-config file

* Sun Jun 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt3
- Rebuild with PIC

* Wed May 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt2
- Rebuild with gcc 4.4

* Fri Apr 24 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1
- Initial build for Sisyphus

