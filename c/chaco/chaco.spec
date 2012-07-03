%define somver 2
%define sover %somver.2.0
%define rname chaco2
Name: chaco
Version: 2.2
Release: alt7
Summary: Matrix Orders, Colorings, and Partitionings
License: LGPL v2.1
Group: Sciences/Mathematics
Url: http://www.sandia.gov/~bahendr/chaco.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: ftp://ftp.mcs.anl.gov/pub/petsc/externalpackages/Chaco-2.2.tar.gz

%description
Chaco contains a wide variety of algorithms and options, many of which were
invented by the authors. Some of the algorithms exploit the geometry of the
mesh, others its local connectivity or its global structure as captured by
eigenvectors of a related matrix. These methods can be mixed and matched in
several ways, and combinations often prove to be more effective than any single
technique in isolation. All these algorithms are accessed via a simple user
interface, or a call from other software. Innovations in Chaco include

  * Development of multilevel graph partitioning. This widely imitated approach
  has become the premiere algorithm combining very high quality with short
  calculation times.

  * Extension of spectral partitioning to enable the use of 2 or 3 Laplacian
  eigenvectors to quadrisect of octasect a graph.

  * Highly efficient and robust eigensolvers for use with spectral graph
  algorithms.

  * Generalization of the Kernighan-Lin/Fiduccia-Mattheyses algorithm to handle
  weighted graphs, arbitrary number of sets and lazy initiation.

  * Development of skewed partitioning to improve the mapping of a graph onto a
  target parallel architecture.

  * Various post-processing options to improve partitions in a number of ways.

%package docs
Summary: Documentation for Chaco, Software for Partitioning Graphs
Group: Development/C
BuildArch: noarch

%description docs
Chaco contains a wide variety of algorithms and options, many of which were
invented by the authors. Some of the algorithms exploit the geometry of the
mesh, others its local connectivity or its global structure as captured by
eigenvectors of a related matrix. These methods can be mixed and matched in
several ways, and combinations often prove to be more effective than any single
technique in isolation.

This package contains documentation for Chaco.

%package -n lib%name
Summary: Chaco graphs partitioning shared library
Group: System/Libraries

%description -n lib%name
Chaco contains a wide variety of algorithms and options, many of which were
invented by the authors. Some of the algorithms exploit the geometry of the
mesh, others its local connectivity or its global structure as captured by
eigenvectors of a related matrix. These methods can be mixed and matched in
several ways, and combinations often prove to be more effective than any single
technique in isolation.

This package contains a Chaco shared library.

%package -n lib%name-devel
Summary: Chaco graphs partitioning development library
Group: Development/C
Requires: lib%name = %version-%release
Conflicts: lib%name-devel < %version-%release
Obsoletes: lib%name-devel < %version-%release

%description -n lib%name-devel
Chaco contains a wide variety of algorithms and options, many of which were
invented by the authors. Some of the algorithms exploit the geometry of the
mesh, others its local connectivity or its global structure as captured by
eigenvectors of a related matrix. These methods can be mixed and matched in
several ways, and combinations often prove to be more effective than any single
technique in isolation.

This package contains a Chaco development library.

%package -n lib%name-devel-static
Summary: Chaco graphs partitioning static library
Group: Development/C
Requires: lib%name-devel = %version-%release
Conflicts: lib%name-devel < %version-%release

%description -n lib%name-devel-static
Chaco contains a wide variety of algorithms and options, many of which were
invented by the authors. Some of the algorithms exploit the geometry of the
mesh, others its local connectivity or its global structure as captured by
eigenvectors of a related matrix. These methods can be mixed and matched in
several ways, and combinations often prove to be more effective than any single
technique in isolation.

This package contains a Chaco static library.

%prep
%setup

%build
pushd code
SRCDIR=$PWD %make -j%__nprocs
popd

ar r lib%name.a $(find ./ -name '*.o')
ar d lib%name.a main.o
ranlib lib%name.a

%install
install -d %buildroot%_bindir
install -d %buildroot%_datadir/%name
install -d %buildroot%_libdir
install -d %buildroot%_docdir/%name

install -m755 exec/%name %buildroot%_bindir
rm -f exec/%name
install -p -m644 exec/* %buildroot%_datadir/%name
install -m644 lib%name.a %buildroot%_libdir
install -m644 doc/* %buildroot%_docdir/%name

#shared library

pushd %buildroot%_libdir
mkdir tmp
pushd tmp
ar x ../lib%name.a
gcc -shared * -lm \
	-Wl,-soname,lib%rname.so.%somver -o ../lib%rname.so.%sover
rm -f *
popd
rmdir tmp
ln -s lib%rname.so.%sover lib%rname.so.%somver
ln -s lib%rname.so.%somver lib%rname.so
popd

%files
%_bindir/*
%_datadir/%name

%files docs
%_docdir/%name

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so

#files -n lib%name-devel-static
#_libdir/*.a

%changelog
* Tue Nov 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt7
- Renamed libchaco.so -> libchaco2.so
- Disabled devel-static package

* Sun Mar 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt6
- Added -g into compiler flags

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt5
- Rebuilt for debuginfo

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt4
- Rebuilt for soname set-versions

* Sat Aug 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt3
- Added shared library

* Sun Jun 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt2
- Rebuild with PIC

* Wed May 27 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt1
- Initial build for Sisyphus

