%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define somver 0
%define sover %somver.0.0

Name: adios
Version: 1.7.0
Release: alt1
Summary: The Adaptable IO System (ADIOS)
License: BSD
Group: Sciences/Mathematics
Url: http://www.olcf.ornl.gov/center-projects/adios/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://users.nccs.gov/~pnorbert/adios-1.7.0.tar.gz
Source1: http://users.nccs.gov/~pnorbert/ADIOS-UsersManual-1.7.0.pdf
Source2: https://users.nccs.gov/~lot/skel/skel-doc-1.6.0.pdf
Source3: http://users.nccs.gov/~pnorbert/ADIOS-DevManual-1.6.0.pdf
Source4: https://users.nccs.gov/~pnorbert/ADIOS-VisualizationSchema-1.1.pdf
Source5: %name.conf

%add_verify_elf_skiplist %_libdir/%name/examples/C/*

BuildPreReq: libmxml-devel %mpiimpl-devel libhdf5-mpi-devel
BuildPreReq: libnetcdf-mpi-devel libmpe2-devel libmxml-devel
BuildPreReq: python-modules-xml cmake bzlib-devel zlib-devel
BuildPreReq: libsz2-devel liblustre-devel glib2-devel libnumpy-devel

Requires: python-module-%name = %version-%release

%description
The Adaptable IO System (ADIOS) provides a simple, flexible way for
scientists to desribe the data in their code that may need to be
written, read, or processed outside of the running simulation. By
providing an external to the code XML file describing the various
elements, their types, and how you wish to process them this run, the
routines in the host code (either Fortran or C) can transparently change
how they process the data.

%package -n python-module-%name
Summary: Python module of the Adaptable IO System (ADIOS)
Group: Development/Python

%description -n python-module-%name
The Adaptable IO System (ADIOS) provides a simple, flexible way for
scientists to desribe the data in their code that may need to be
written, read, or processed outside of the running simulation. By
providing an external to the code XML file describing the various
elements, their types, and how you wish to process them this run, the
routines in the host code (either Fortran or C) can transparently change
how they process the data.

This package contains python module of ADIOS.

%package -n lib%name
Summary: Shared libraries of the Adaptable IO System (ADIOS)
Group: System/Libraries

%description -n lib%name
The Adaptable IO System (ADIOS) provides a simple, flexible way for
scientists to desribe the data in their code that may need to be
written, read, or processed outside of the running simulation. By
providing an external to the code XML file describing the various
elements, their types, and how you wish to process them this run, the
routines in the host code (either Fortran or C) can transparently change
how they process the data.

This package contains shared libraries of ADIOS.

%package -n lib%name-devel
Summary: Development files of the Adaptable IO System (ADIOS)
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
The Adaptable IO System (ADIOS) provides a simple, flexible way for
scientists to desribe the data in their code that may need to be
written, read, or processed outside of the running simulation. By
providing an external to the code XML file describing the various
elements, their types, and how you wish to process them this run, the
routines in the host code (either Fortran or C) can transparently change
how they process the data.

This package contains development files of ADIOS.

%package examples
Summary: Examples for the Adaptable IO System (ADIOS)
Group: Sciences/Mathematics

%description examples
The Adaptable IO System (ADIOS) provides a simple, flexible way for
scientists to desribe the data in their code that may need to be
written, read, or processed outside of the running simulation. By
providing an external to the code XML file describing the various
elements, their types, and how you wish to process them this run, the
routines in the host code (either Fortran or C) can transparently change
how they process the data.

This package contains examples for ADIOS.

%package doc
Summary: Documentation for the Adaptable IO System (ADIOS)
Group: Documentation
BuildArch: noarch

%description doc
The Adaptable IO System (ADIOS) provides a simple, flexible way for
scientists to desribe the data in their code that may need to be
written, read, or processed outside of the running simulation. By
providing an external to the code XML file describing the various
elements, their types, and how you wish to process them this run, the
routines in the host code (either Fortran or C) can transparently change
how they process the data.

This package contains documentation for ADIOS.

%prep
%setup
install -p -m644 %SOURCE1 %SOURCE2 %SOURCE3 %SOURCE4 %SOURCE5 .

sed -i 's|@BUILDROOT@|%buildroot|' wrappers/numpy/setup*
%ifarch x86_64
LIBSUFF=64
%endif
sed -i "s|@64@|$LIBSUFF|" wrappers/numpy/setup*

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"
export MPIDIR=%mpidir
TOPDIR=$PWD

%add_optflags -I%mpidir/include -I%mpidir/include/netcdf %optflags_shared
%add_optflags -I$TOPDIR/src/public

export CFLAGS="%optflags"
. ./%name.conf

mkdir BUILD
pushd BUILD
cmake \
%if %_lib == lib64
	-DLIB_SUFFIX=64 \
%endif
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_Fortran_FLAGS:STRING="%optflags" \
	-DCXXFLAGS:STRING="%optflags" \
	-DFCFLAGS:STRING="%optflags" \
	-DNC4PAR:BOOL=ON \
	-DPHDF5:BOOL=ON \
	-DMPIDIR:PATH=%mpidir \
	-DMPILIBS:STRING="-L%mpidir/lib -lmpi_f90 -lmpi_f77 -lmpi_cxx -lmpi" \
	-DCMAKE_INSTALL_RPATH:STRING=%mpidir/lib \
	-DCMAKE_SKIP_RPATH:BOOL=ON \
	-DSOMVER:STRING=%somver \
	-DSOVER:STRING=%sover \
	..

%make VERBOSE=1
popd

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"
export MPIDIR=%mpidir

pushd BUILD
%makeinstall_std
#cp -P src/libadios_internal_nompi.so* %buildroot%_libdir/
popd

install -d %buildroot%_datadir/%name
mv %buildroot%_bindir/adios_config.flags %buildroot%_datadir/%name/

pushd wrappers/numpy
export PATH=$PATH:%buildroot%_bindir
export CFLAGS=-I%buildroot%_includedir
%make MPI=y python
%python_install
popd
install -m644 utils/skel/lib/skel_suite.py \
	utils/skel/lib/skel_template.py \
	utils/skel/lib/skel_test_plan.py \
	%buildroot%python_sitelibdir/

rm -f $(find examples -name '*.o') \
	examples/staging/stage_write/writer_adios

install -d %buildroot%_libdir/%name
cp -fR examples %buildroot%_libdir/%name/

install -d %buildroot%python_sitelibdir
mv %buildroot%_libdir/python/*.py %buildroot%python_sitelibdir/

%files
%doc AUTHORS COPYING ChangeLog KNOWN_BUGS NEWS README TODO
%_sysconfdir/*
%_bindir/*
%exclude %_bindir/adios_config

%files -n lib%name
%_libdir/*.so.*

%files -n python-module-%name
%python_sitelibdir/*
%exclude %python_sitelibdir/argparse.py*

%files -n lib%name-devel
%_bindir/adios_config
%_libdir/*.so
%_includedir/*
%_datadir/%name
%_libdir/FindADIOS.cmake

%files examples
%_libdir/%name

%files doc
%doc *.pdf

%changelog
* Tue Jun 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt1
- Version 1.7.0

* Tue Jun 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt2
- Fixed build

* Tue May 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt1
- Version 1.6.0

* Thu Jun 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt2
- Rebuilt with new libhdf5

* Mon Jun 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1
- Version 1.5.0

* Fri Feb 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1
- Version 1.4.1

* Mon Sep 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1
- Version 1.4.0

* Tue Jun 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt4
- Rebuilt with OpenMPI 1.6

* Sat Jun 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt3
- Fixed build

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt2
- Fixed RPATH

* Thu Dec 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1
- Version 1.3.1

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.1-alt6.1
- Rebuild with Python-2.7

* Wed Sep 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt6
- Rebuilt with libhdf5-7-mpi

* Sun Apr 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt5
- Rebuilt with libnetcdf7

* Sun Feb 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt4
- Rebuilt for debuginfo

* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt3
- Rebuilt for soname set-versions

* Tue Oct 12 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt2
- Fixed overlinking of libraries

* Tue Sep 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1
- Initial build for Sisyphus

