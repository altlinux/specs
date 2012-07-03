%define sover 0
%define oname metis
Name: %{oname}0
Version: 4.0.3
Release: alt3
Summary: Family of Multilevel Partitioning Algorithms
License: GPL
Group: Sciences/Mathematics
Url: http://glaros.dtc.umn.edu/gkhome/views/metis
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: %oname.pc

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
%make_build
sed -i 's|@VERSION@|%version|' %oname.pc

%install
install -d %buildroot%_bindir
install -d %buildroot%_libdir
install -d %buildroot%_includedir/%name
install -d %buildroot%_docdir/%name
install -d %buildroot%_datadir/%name
install -d %buildroot%_pkgconfigdir

for i in graphchk kmetis mesh2dual mesh2nodal oemetis onmetis partdmesh \
	partnmesh pmetis
do
	install -m755 $i %buildroot%_bindir
done
mv Graphs/mtest Graphs/metis_test
install -m755 Graphs/metis_test %buildroot%_bindir
rm -f Graphs/metis_test
install -m644 libmetis.a %buildroot%_libdir
install -m644 Doc/manual.ps %buildroot%_docdir/%name
install -m644 Graphs/* %buildroot%_datadir/%name
install -m644 Lib/*.h %buildroot%_includedir/%name

install -m644 %oname.pc %buildroot%_pkgconfigdir/%name.pc

# shared library

pushd %buildroot%_libdir
ar x lib%oname.a
gcc -shared *.o -lm \
	-Wl,-soname,lib%name.so.%sover \
	-o lib%name.so.%sover
ln -s lib%name.so.%sover lib%name.so
rm -f *.o
popd

#files
#doc CHANGES
#_bindir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*

#files -n lib%name-devel-doc
#_docdir/%name

#files examples
#_datadir/%name

%changelog
* Sun Jun 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt3
- Removed native directory: %_libexecdir/metis

* Fri Sep 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt2
- Renamed this version: libmetis -> libmetis0

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

