%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl
%define ARCH LINUXgcc

%define somver 0
%define sover %somver.2.4
Name: freepooma
Version: 2.4.1
Release: alt3.cvs20090410
Summary: Element-wise, data-parallel, and stencil-based physics computations
License: MIT
Group: Sciences/Mathematics
Url: http://www.nongnu.org/freepooma/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# cvs -d:pserver:anonymous@cvs.sv.gnu.org:/sources/freepooma co .
Source: %name-%version.tar.gz

Requires: lib%name = %version-%release

BuildPreReq: gcc-fortran gcc-c++ libcheetah-devel pdtoolkit libpdtoolkit-devel
BuildPreReq: %mpiimpl-devel
BuildPreReq: libhdf5-mpi-devel libfftw3-mpi-devel makedepend libpete-devel
BuildPreReq: doxygen graphviz chrpath

%description
FreePOOMA is a C++ library supporting element-wise, data-parallel, and
stencil-based physics computations using one or more processors.  The
library automatically handles all interprocessor communication,
obviating the need for any explicit communication code.  The library
supports high-level syntax close to mathematical or algorithmic syntax
(like Fortran 95), easing the conversion from algorithms to code.

FreePOOMA is based on POOMA, originally developed at Los Alamos
National Laboratory.

%package -n lib%name
Summary: Shared libraries of FreePOOMA
Group: System/Libraries

%description -n lib%name
FreePOOMA is a C++ library supporting element-wise, data-parallel, and
stencil-based physics computations using one or more processors.  The
library automatically handles all interprocessor communication,
obviating the need for any explicit communication code.  The library
supports high-level syntax close to mathematical or algorithmic syntax
(like Fortran 95), easing the conversion from algorithms to code.

This package contains shared libraries of FreePOOMA.

%package -n lib%name-devel
Summary: Development files of FreePOOMA
Group: Development/Other
Requires: %name = %version-%release
Requires: lib%name = %version-%release

%description -n lib%name-devel
FreePOOMA is a C++ library supporting element-wise, data-parallel, and
stencil-based physics computations using one or more processors.  The
library automatically handles all interprocessor communication,
obviating the need for any explicit communication code.  The library
supports high-level syntax close to mathematical or algorithmic syntax
(like Fortran 95), easing the conversion from algorithms to code.

This package contains development files of FreePOOMA.

%package -n lib%name-devel-doc
Summary: Documentation for FreePOOMA
Group: Development/Documentation
BuildArch: noarch
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-doc
FreePOOMA is a C++ library supporting element-wise, data-parallel, and
stencil-based physics computations using one or more processors.  The
library automatically handles all interprocessor communication,
obviating the need for any explicit communication code.  The library
supports high-level syntax close to mathematical or algorithmic syntax
(like Fortran 95), easing the conversion from algorithms to code.

This package contains development documentation for FreePOOMA.

%prep
%setup

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib -L%mpidir/lib"

mkdir _ex
cp -fR examples/* _ex/
sed -i 's|@MPIDIR@|%mpidir|g' \
	config/arch/%ARCH.conf configure scripts/configure
sed -i 's|@SOMVER@|%somver|g' config/arch/%ARCH.conf
sed -i "s|^\(PROJECT_ROOT\).*|\1 = $PWD|g" $(find ./ -name makefile)
export PDTDIR=%prefix
export PETEDIR=%prefix
export FFTWDIR=%prefix
export CHEETAHDIR=%prefix
export HDF5DIR=%mpidir
export POOMASUITE=%ARCH
./configure --v \
	--shared \
	--prefix %prefix \
	--arch %ARCH \
	--with-fortran \
	--mpi \
	--hdf5 \
	--fftw \
	--opt \
	--pool \
	--c mpicc \
	--carg -fpermissive \
	--cpp mpicxx \
	--cpparg -fpermissive \
	--f77 mpif77 \
	--f77arg -fpermissive
sed -i '26a\\#define POOMA_CHEETAH POOMA_YES' \
	lib/LINUXgcc/PoomaConfiguration.h
#make_build
%make
#make_build examples
pushd docs/reference
%make html
rm -f *.doxygen Makefile
popd

%install
install -d %buildroot%_bindir
install -d %buildroot%_libdir
install -d %buildroot%_includedir/%name
install -d %buildroot%_docdir/%name

install -m644 lib/%ARCH/libpooma.so \
	%buildroot%_libdir/libpooma.so.%sover
ln -s libpooma.so.%sover \
	%buildroot%_libdir/libpooma.so.%somver
ln -s libpooma.so.%somver \
	%buildroot%_libdir/libpooma.so
ln -s libpooma.so \
	%buildroot%_libdir/libpooma-gcc-ex.so
install -m644 lib/%ARCH/*.h %buildroot%_includedir/%name

install -d %buildroot%_docdir/%name/examples
cp -fR _ex/* %buildroot%_docdir/%name/examples/

pushd src
rm -fR $(find ./ -type d -name tests)
for dir in $(find ./ -type d ! -name %ARCH); do
	if [ $(ls $dir/*.h|wc -l) -ne 0 ]; then
		install -d %buildroot%_includedir/%name/$dir
		install -p -m644 $dir/*.h %buildroot%_includedir/%name/$dir
	fi
done
popd

install -p -m644 docs/*.* %buildroot%_docdir/%name
mv docs/reference/html docs/reference/reference
mv docs/reference/reference %buildroot%_docdir/%name/

%files
%doc CREDITS LICENSE* README*
#_bindir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%files -n lib%name-devel-doc
%_docdir/%name

%changelog
* Thu Jul 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.1-alt3.cvs20090410
- Rebuilt with OpenMPI 1.6

* Wed Jun 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.1-alt2.cvs20090410
- Fixed build

* Wed Mar 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.1-alt1.cvs20090410.4
- Rebuilt with shared libfftw3-mpi
- Added -g into compiler flags

* Sun Feb 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.1-alt1.cvs20090410.3
- Rebuilt for debuginfo

* Wed Oct 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.1-alt1.cvs20090410.2
- Fixed overlinking of libraries
- Rebuilt for soname set-versions

* Fri Sep 04 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.1-alt1.cvs20090410.1
- Built shared library instead static

* Sun May 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.1-alt1.cvs20090410
- Initial build for Sisyphus

