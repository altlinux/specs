%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define somver 0
%define sover %somver.0.0

Name: adios
Version: 1.3.1
Release: alt4
Summary: The Adaptable IO System (ADIOS)
License: BSD
Group: Sciences/Mathematics
Url: http://www.nccs.gov/user-support/center-projects/adios/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://users.nccs.gov/~pnorbert/adios-1.3.1.tar.gz
Source1: http://users.nccs.gov/~pnorbert/ADIOS-UsersManual-1.3.1.pdf

%add_verify_elf_skiplist %_libdir/%name/examples/C/*

BuildPreReq: libmxml-devel %mpiimpl-devel libhdf5-mpi-devel
BuildPreReq: libnetcdf-mpi-devel libmpe2-devel

%description
The Adaptable IO System (ADIOS) provides a simple, flexible way for
scientists to desribe the data in their code that may need to be
written, read, or processed outside of the running simulation. By
providing an external to the code XML file describing the various
elements, their types, and how you wish to process them this run, the
routines in the host code (either Fortran or C) can transparently change
how they process the data.

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
install -p -m644 %SOURCE1 .

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"
export MPIDIR=%mpidir

#autoreconf
%add_optflags -I%mpidir/include -I%mpidir/include/netcdf-3 %optflags_shared
%configure \
	--enable-shared \
	--enable-static=no \
	--disable-fortran \
	--with-mpi=%mpidir \
	--with-phdf5=%mpidir \
	--with-nc4par=%mpidir \
	--with-nc4par-incdir=%mpidir/include/netcdf-3
#make_build
%make

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"
export MPIDIR=%mpidir

%makeinstall_std

install -d %buildroot%_datadir/%name
mv %buildroot%_bindir/adios_config.flags %buildroot%_datadir/%name/

rm -f $(find examples -name '*.o')

install -d %buildroot%_libdir/%name
cp -fR examples %buildroot%_libdir/%name/

mkdir -p %buildroot%_libdir/tmp
pushd %buildroot%_libdir
LIBS="$(ls *.a)"
pushd tmp
for i in $LIBS; do
	LIB=$(echo $i|sed 's|\(.*\)\.a|\1|')
	ar x ../$i
	mpicc -shared * -Wl,-soname,$LIB.so.%somver -o ../$LIB.so.%sover \
		-Wl,-rpath,%mpidir/lib -lnetcdf -lhdf5 -lmxml -lpthread $ADDLIB
	ln -s $LIB.so.%sover ../$LIB.so.%somver
	ln -s $LIB.so.%somver ../$LIB.so
	rm -f *
done
popd
popd
rmdir %buildroot%_libdir/tmp

rm -f %buildroot%_libdir/*_nompi.so*

%files
%doc AUTHORS COPYING ChangeLog KNOWN_BUGS NEWS README TODO
%_bindir/*
%exclude %_bindir/adios_config

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_bindir/adios_config
%_libdir/*.so
%_includedir/*
%_datadir/%name

%files examples
%_libdir/%name

%files doc
%doc *.pdf

%changelog
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

