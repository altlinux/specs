%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

Name: silo
Version: 4.8
Release: alt8
Summary: A library for reading and writing a wide variety of scientific data
License: BSD
Group: Development/Tools
Url: http://wci.llnl.gov/codes/silo/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: https://wci.llnl.gov/codes/silo/silo-4.8/silo-4.8-bsd.tar.gz
Source1: https://wci.llnl.gov/codes/silo/silo-4.8/silo-4.8-bsd-smalltest.tar.gz

Requires: lib%name = %version-%release

BuildRequires(pre): rpm-macros-qt4 rpm-build-python
BuildPreReq: %mpiimpl-devel libhdf5-mpi-devel libnetcdf-mpi-devel libsz2-devel
BuildPreReq: libqt4-devel openpdt libopenpdt-devel pdbsql libreadline-devel
BuildPreReq: python-devel

%description
Silo is a library for reading and writing a wide variety of scientific data to
binary, disk files. The files Silo produces and the data within them can be
easily shared and exchanged between wholly independently developed applications
running on disparate computing platforms. Consequently, Silo facilitates the
development of general purpose tools for processing scientific data. One of the
more popular tools that process Silo data files is the VisIt visualization tool.

Silo supports gridless (point) meshes, structured meshes, unstructured-zoo and
unstructured-arbitrary-polyhedral meshes, block structured AMR meshes,
constructive solid geometry (CSG) meshes, piecewise-constant (e.g.
zone-centered) and piecewise-linear (e.g. node-centered) variables defined on
the node, edge, face or volume elements of meshes as well as the decomposition
of meshes into arbitrary subset hierarchies including materials and mixing
materials. In addition, Silo supports a wide variety of other useful objects to
address various scientific computing application needs. Although the Silo
library is a serial library, it has some key features which enable it to be
applied quite effectively and scalable in parallel.

%package -n lib%name
Summary: Shared libraries of Silo
Group: System/Libraries

%description -n lib%name
Silo is a library for reading and writing a wide variety of scientific data to
binary, disk files. The files Silo produces and the data within them can be
easily shared and exchanged between wholly independently developed applications
running on disparate computing platforms. Consequently, Silo facilitates the
development of general purpose tools for processing scientific data. One of the
more popular tools that process Silo data files is the VisIt visualization tool.

Silo supports gridless (point) meshes, structured meshes, unstructured-zoo and
unstructured-arbitrary-polyhedral meshes, block structured AMR meshes,
constructive solid geometry (CSG) meshes, piecewise-constant (e.g.
zone-centered) and piecewise-linear (e.g. node-centered) variables defined on
the node, edge, face or volume elements of meshes as well as the decomposition
of meshes into arbitrary subset hierarchies including materials and mixing
materials. In addition, Silo supports a wide variety of other useful objects to
address various scientific computing application needs. Although the Silo
library is a serial library, it has some key features which enable it to be
applied quite effectively and scalable in parallel.

This package contains shared libraries of Silo.

%package -n lib%name-devel
Summary: Development files of Silo
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
Silo is a library for reading and writing a wide variety of scientific data to
binary, disk files. The files Silo produces and the data within them can be
easily shared and exchanged between wholly independently developed applications
running on disparate computing platforms. Consequently, Silo facilitates the
development of general purpose tools for processing scientific data. One of the
more popular tools that process Silo data files is the VisIt visualization tool.

Silo supports gridless (point) meshes, structured meshes, unstructured-zoo and
unstructured-arbitrary-polyhedral meshes, block structured AMR meshes,
constructive solid geometry (CSG) meshes, piecewise-constant (e.g.
zone-centered) and piecewise-linear (e.g. node-centered) variables defined on
the node, edge, face or volume elements of meshes as well as the decomposition
of meshes into arbitrary subset hierarchies including materials and mixing
materials. In addition, Silo supports a wide variety of other useful objects to
address various scientific computing application needs. Although the Silo
library is a serial library, it has some key features which enable it to be
applied quite effectively and scalable in parallel.

This package contains development files of Silo.

%package docs
Summary: Documentation for Silo
Group: Documentation
BuildArch: noarch

%description docs
Silo is a library for reading and writing a wide variety of scientific data to
binary, disk files. The files Silo produces and the data within them can be
easily shared and exchanged between wholly independently developed applications
running on disparate computing platforms. Consequently, Silo facilitates the
development of general purpose tools for processing scientific data. One of the
more popular tools that process Silo data files is the VisIt visualization tool.

Silo supports gridless (point) meshes, structured meshes, unstructured-zoo and
unstructured-arbitrary-polyhedral meshes, block structured AMR meshes,
constructive solid geometry (CSG) meshes, piecewise-constant (e.g.
zone-centered) and piecewise-linear (e.g. node-centered) variables defined on
the node, edge, face or volume elements of meshes as well as the decomposition
of meshes into arbitrary subset hierarchies including materials and mixing
materials. In addition, Silo supports a wide variety of other useful objects to
address various scientific computing application needs. Although the Silo
library is a serial library, it has some key features which enable it to be
applied quite effectively and scalable in parallel.

This package contains documentation for Silo.

%package -n python-module-%name
Summary: Python module of Silo
Group: Development/Python

%description -n python-module-%name
Silo is a library for reading and writing a wide variety of scientific data to
binary, disk files. The files Silo produces and the data within them can be
easily shared and exchanged between wholly independently developed applications
running on disparate computing platforms. Consequently, Silo facilitates the
development of general purpose tools for processing scientific data. One of the
more popular tools that process Silo data files is the VisIt visualization tool.

Silo supports gridless (point) meshes, structured meshes, unstructured-zoo and
unstructured-arbitrary-polyhedral meshes, block structured AMR meshes,
constructive solid geometry (CSG) meshes, piecewise-constant (e.g.
zone-centered) and piecewise-linear (e.g. node-centered) variables defined on
the node, edge, face or volume elements of meshes as well as the decomposition
of meshes into arbitrary subset hierarchies including materials and mixing
materials. In addition, Silo supports a wide variety of other useful objects to
address various scientific computing application needs. Although the Silo
library is a serial library, it has some key features which enable it to be
applied quite effectively and scalable in parallel.

This package contains Python module Silo.

%prep
%setup
tar -xzf %SOURCE1

sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' \
	*.m4 configure config/ltmain.sh

%install
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib -L%mpidir/lib"

export PYTHONVER=%_python_version
%add_optflags -DH5Z_class_t_vers=2

function buildIt() {
	%configure $1 \
		--enable-shared \
		--enable-optimization \
		--enable-portable-binary \
		--enable-fortran \
		--enable-silex \
		--enable-hzip \
		--enable-fpzip \
		--with-qt=%_qt4dir \
		--with-szlib=%prefix \
		CC="mpicc -g" CXX="mpicxx -g" FC="mpif90 -g" F77="mpif77 -g"
	%make_build
	%makeinstall_std
}
buildIt --enable-pythonmodule
%make clean
buildIt --with-hdf5=%mpidir/include,%mpidir/lib

install -d %buildroot%_docdir/%name
rm -f docs/Makefile*
install -p -m644 docs/* %buildroot%_docdir/%name

install -d %buildroot%python_sitelibdir/%name
mv %buildroot%_libdir/Silo.so %buildroot%python_sitelibdir/%name/
install -p -m644 tests/*.py %buildroot%python_sitelibdir/%name
touch %buildroot%python_sitelibdir/%name/__init__.py

%files
%doc COPYRIGHT FAQ
%_bindir/*

%files -n lib%name
%_libdir/*.so.*
%_libdir/*.settings

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%files docs
%_docdir/%name

%files -n python-module-%name
%python_sitelibdir/%name

%changelog
* Mon Jun 25 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.8-alt8
- Rebuilt with OpenMPI 1.6

* Wed Jun 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.8-alt7
- Fixed build

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.8-alt6
- Rebuilt with OpenPDT instead pdtoolkit
- Enabled silex

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.8-alt5
- Fixed RPATH

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.8-alt4.1
- Rebuild with Python-2.7

* Wed Sep 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.8-alt4
- Rebuilt with libhdf5-7-mpi

* Sun Apr 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.8-alt3
- Rebuilt with libnetcdf7
- Disabled devel-static package

* Sat Mar 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.8-alt2
- Rebuilt for debuginfo

* Mon Oct 25 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.8-alt1
- Version 4.8

* Fri Oct 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.7.2-alt2
- Fixed overlinking of libraries

* Mon Jul 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.7.2-alt1
- Version 4.7.2

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.7-alt4
- Rebuilt with python 2.6

* Fri Sep 04 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.7-alt3
- Rebuilt with shared library of PDToolkit

* Sun Jul 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.7-alt2
- Rebuilt

* Sat Jun 27 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.7-alt1
- Initial build for Sisyphus

