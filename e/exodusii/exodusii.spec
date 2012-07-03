%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

Name: exodusii
Version: 5.14.0
%define somver 0
%define sover %somver.%version
Release: alt6
Summary: A model developed to store and retrieve transient data for finite element analyses
License: BSD
Group: Sciences/Mathematics
Url: http://sourceforge.net/projects/exodusii/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
# git://exodusii.git.sourceforge.net/gitroot/exodusii/exodusii
Source: %name-%version.tar.gz
Source1: CMakeCache.txt

BuildPreReq: doxygen graphviz
BuildPreReq: %mpiimpl-devel cmake libnetcdf-mpi-devel imake
BuildPreReq: netcdf7-mpi-tools slurm-utils libhdf5-mpi-devel

%description
EXODUS II is a model developed to store and retrieve transient data for
finite element analyses. It is used for preprocessing, postprocessing,
as well as code to code data transfer. ExodusII is based on netcdf.
Includes the nemesis parallel extension.

%package -n lib%name
Summary: Shared libraries of EXODUS II
Group: System/Libraries

%description -n lib%name
EXODUS II is a model developed to store and retrieve transient data for
finite element analyses. It is used for preprocessing, postprocessing,
as well as code to code data transfer. ExodusII is based on netcdf.
Includes the nemesis parallel extension.

This package contains shared libraries of EXODUS II.

%package -n lib%name-devel
Summary: Development files of EXODUS II
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
EXODUS II is a model developed to store and retrieve transient data for
finite element analyses. It is used for preprocessing, postprocessing,
as well as code to code data transfer. ExodusII is based on netcdf.
Includes the nemesis parallel extension.

This package contains development files of EXODUS II.

%package -n lib%name-devel-doc
Summary: Documentation for EXODUS II
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
EXODUS II is a model developed to store and retrieve transient data for
finite element analyses. It is used for preprocessing, postprocessing,
as well as code to code data transfer. ExodusII is based on netcdf.
Includes the nemesis parallel extension.

This package contains development documentation for EXODUS II.

%prep
%setup
install -p -m644 %SOURCE1 exodus
install -p -m644 %SOURCE1 nemesis
%ifarch x86_64
LIB64=64
%endif
sed -i "s|@64@|$LIB64|g" exodus/CMakeCache.txt nemesis/CMakeCache.txt

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

pushd exodus
cmake .
%make_build verbose=1
popd
pushd nemesis
#NETCDF_INC="-I%mpidir/include/netcdf-3"
#NETCDF_INC="$NETCDF_INC -I$PWD/../exodus/cbind/include"
#%make_build -f Makefile.standalone NETCDF_INC="$NETCDF_INC"
cmake .
%make_build VERBOSE=1
popd

pushd exodus
doxygen
popd

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

NETCDF_INC="-I%mpidir/include/netcdf-3"
NETCDF_INC="$NETCDF_INC -I$PWD/exodus/cbind/include"
pushd exodus
%makeinstall_std
popd

%ifarch x86_64
install -d %buildroot%_libdir
mv %buildroot%_libexecdir/* %buildroot%_libdir/
%endif

install -d %buildroot%_includedir/%name
mv %buildroot%_includedir/*.h %buildroot%_includedir/%name/

# nemesis

install -p -m644 nemesis/*.h %buildroot%_includedir/%name/
install -m644 nemesis/*.a %buildroot%_libdir

pushd %buildroot%_libdir
#for i in exoIIv2c nemesis nemIf; do
for i in exoIIv2c nemesis; do
	mpic++ -shared -Wl,--whole-archive lib$i.a -Wl,--no-whole-archive \
		-Wl,-soname,lib$i.so.%somver -o lib$i.so.%sover \
		-L%mpidir/lib -L. $ADDLIBS -lnetcdf -Wl,-R%mpidir/lib
	ln -s lib$i.so.%sover lib$i.so.%somver
	ln -s lib$i.so.%somver lib$i.so
	ADDLIBS="$ADDLIBS -l$i"
done
popd

mv nemesis/README README.Nemesis

%files -n lib%name
%doc exodus/COPYRIGHT exodus/README README.Nemesis ChangeLog
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%files -n lib%name-devel-doc
%doc exodus/html exodus/doc/* nemesis/doc/*

%changelog
* Mon Jun 25 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.14.0-alt6
- Rebuilt with OpenMPI 1.6

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.14.0-alt5
- Fixed RPATH

* Sat Dec 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.14.0-alt4
- Rebuilt with Boost 1.48.0

* Tue Nov 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.14.0-alt3
- Version 5.14.0

* Sun Nov 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10-alt3
- Moved headers into %_includedir/%name/

* Fri Sep 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10-alt2
- Added headers for nemesis

* Fri Sep 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10-alt1
- Version 5.10

* Sun Apr 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.98-alt2
- Rebuilt with libnetcdf7

* Wed Apr 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.98-alt1
- Version 4.98

* Fri Feb 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.96-alt3
- Rebuilt for debuginfo

* Tue Oct 12 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.96-alt2
- Fixed overlinking of libraries

* Fri Sep 24 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.96-alt1
- Initial build for Sisyphus

