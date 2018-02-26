%define mpiimpl openmpi
%define mpidir %_libexecdir/%mpiimpl

%define sover 0

Name: mct
Version: 2.6.0
Release: alt5
Summary: The Model Coupling Toolkit
License: MIT
Group: Development/Tools
Url: http://www.mcs.anl.gov/research/projects/mct/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://www.mcs.anl.gov/research/projects/mct/MCT.tar.gz

BuildPreReq: %mpiimpl-devel
BuildPreReq: /usr/bin/latex

%description
MCT is a set of open-source software tools for creating coupled models. MCT is
fully parallel and can be used to couple message-passing parallel models to
create a parallel coupled model. MCT is available as a small library and a set
of Fortran90 modules.

MCT provides model interoperability through a simple API. Two models that
declare and use MCT datatypes can be coupled with a minimum of effort.

MCT provides the following core coupling services:

    * a component model registry
    * domain decomposition descriptors
    * communications schedulers for parallel MxN intercomponent data transfer
      and MxM intracomponent data redistribution
    * a flexible and indexible (i.e., random-access) field data storage datatype
    * a time averaging and accumulation buffer datatype
    * a general spatial grid representation capable of supporting unstructured
      grids
    * parallel tools for intergrid interpolation implemented as matrix-vector
      multiplication spatial integration and averaging tools (including paired
      integrals to support conservative interpolation)
    * tools for merging data from multiple components for use by another
      component.
    * a programming model similar to that of the Message Passing Interface. 

MCT can be used in single or multiple executable systems and allows sequential
or concurrent execution.

%package -n lib%name
Summary: Shared libraries of MCT
Group: System/Libraries

%description -n lib%name
MCT is a set of open-source software tools for creating coupled models. MCT is
fully parallel and can be used to couple message-passing parallel models to
create a parallel coupled model. MCT is available as a small library and a set
of Fortran90 modules.

MCT provides model interoperability through a simple API. Two models that
declare and use MCT datatypes can be coupled with a minimum of effort.

This package contains shared libraries of MCT.

%package -n lib%name-devel
Summary: Development files of MCT
Group: Development/Other
Requires: lib%name = %version-%release
Requires: %mpiimpl-devel

%description -n lib%name-devel
MCT is a set of open-source software tools for creating coupled models. MCT is
fully parallel and can be used to couple message-passing parallel models to
create a parallel coupled model. MCT is available as a small library and a set
of Fortran90 modules.

MCT provides model interoperability through a simple API. Two models that
declare and use MCT datatypes can be coupled with a minimum of effort.

This package contains development files of MCT.

%package -n lib%name-devel-static
Summary: Static libraries of MCT
Group: Development/Other
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
MCT is a set of open-source software tools for creating coupled models. MCT is
fully parallel and can be used to couple message-passing parallel models to
create a parallel coupled model. MCT is available as a small library and a set
of Fortran90 modules.

MCT provides model interoperability through a simple API. Two models that
declare and use MCT datatypes can be coupled with a minimum of effort.

This package contains static libraries of MCT.

%package -n lib%name-devel-doc
Summary: Documentation for MCT
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
MCT is a set of open-source software tools for creating coupled models. MCT is
fully parallel and can be used to couple message-passing parallel models to
create a parallel coupled model. MCT is available as a small library and a set
of Fortran90 modules.

MCT provides model interoperability through a simple API. Two models that
declare and use MCT datatypes can be coupled with a minimum of effort.

This package contains development documentation for MCT.

%prep
%setup
rm -f $(find ./ -name .cvsignore)

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-R,%mpidir/lib -L%mpidir/lib"

#autoreconf
MPILIBS="-L%mpidir/lib -Wl,--no-as-needed -lmpi_f90 -Wl,--as-needed"
MPILIBS="$MPILIBS -lmpi_f77 -lmpi -Wl,-R%mpidir/lib"
%configure \
	MPILIBS="$MPILIBS" \
	MPIHEADER="-I%mpidir/include" \
	FC=mpif77 F90=mpif90 CC=mpicc \
	OPT="%optflags %optflags_shared"

%make
%make examples
mv examples/climate_sequen1/climate examples/climate.seq

pushd doc
%make
popd

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-R,%mpidir/lib -L%mpidir/lib"

%makeinstall

install -d %buildroot%_bindir
install -d %buildroot%_datadir/%name/data
install -d %buildroot%_docdir/lib%name-devel

pushd examples
rm -f $(find ./ -name '*.o')
mv climate.seq climate_concur1/climate simple/twocon simple/twoseq* \
	%buildroot%_bindir/
popd
install -p -m644 data/* %buildroot%_datadir/%name/data

install -m644 doc/*.dvi %buildroot%_docdir/lib%name-devel

#shared libraries

pushd %buildroot%_libdir
for i in libmpeu libmct; do
	mpif90 -shared -Wl,--whole-archive $i.a -Wl,--no-whole-archive \
		-Wl,-R%mpidir/lib \
		-o $i.so.%sover -Wl,-soname,$i.so.%sover -L$PWD $LIB -Wl,-z,defs
	ln -s $i.so.%sover $i.so
	LIB=-lmpeu
done
popd

%files
%doc COPYRIGHT examples
%_bindir/*
%_datadir/%name

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%files -n lib%name-devel-static
%_libdir/*.a

%files -n lib%name-devel-doc
%_docdir/lib%name-devel

%changelog
* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0-alt5
- Fixed RPATH
- Disabled devel-static package

* Thu Feb 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0-alt4
- Rebuilt for debuginfo

* Sat Nov 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0-alt3
- Added shared libraries

* Wed Mar 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0-alt2
- Disabled autoreconf

* Wed Jun 10 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0-alt1
- Initial build for Sisyphus

