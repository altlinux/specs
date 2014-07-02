%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

Name: exodusii
Version: 5.14.0
%define somver 0
%define sover %somver.%version
Release: alt7.git20140623
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
BuildPreReq: libcurl-devel

%description
EXODUS II is a model developed to store and retrieve transient data for
finite element analyses. It is used for preprocessing, postprocessing,
as well as code to code data transfer. ExodusII is based on netcdf.
Includes the nemesis parallel extension.

%package -n lib%name
Summary: Shared libraries of EXODUS II
Group: System/Libraries
Requires: libnetcdf7-mpi

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

%package -n python-module-exodus
Summary: Python binding for EXODUS II
Group: Development/Python
Requires: lib%name = %version-%release

%description -n python-module-exodus
EXODUS II is a model developed to store and retrieve transient data for
finite element analyses. It is used for preprocessing, postprocessing,
as well as code to code data transfer. ExodusII is based on netcdf.
Includes the nemesis parallel extension.

This package contains python binding for EXODUS II.

%prep
%setup
install -p -m644 %SOURCE1 exodus
install -p -m644 %SOURCE1 nemesis
%ifarch x86_64
LIB64=64
%endif
sed -i "s|@64@|$LIB64|g" exodus/CMakeCache.txt nemesis/CMakeCache.txt
sed -i "s|@PWD@|$PWD|g" exodus/CMakeCache.txt nemesis/CMakeCache.txt

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

pushd exodus
cmake \
%ifarch x86_64
	-DLIB_SUFFIX:STRING="64" \
%endif
	-DSOMVER:STRING="%somver" \
	-DSOVER:STRING="%sover" \
	-DNETCDF_SO_ROOT=%_libdir \
	-DPYTHON_INSTALL=%python_sitelibdir \
	.
%make_build VERBOSE=1
popd
pushd nemesis
cmake \
%ifarch x86_64
	-DLIB_SUFFIX:STRING="64" \
%endif
	-DSOMVER:STRING="%somver" \
	-DSOVER:STRING="%sover" \
	.
%make_build VERBOSE=1
popd

pushd exodus
doxygen
popd

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

pushd exodus
%makeinstall_std
popd
pushd nemesis
%makeinstall_std
popd

install -d %buildroot%_includedir/%name
mv %buildroot%_includedir/*.h %buildroot%_includedir/%name/

mv nemesis/README README.Nemesis

%filter_from_requires /^debug.*(libnetcdf\.so.*/s/^/libnetcdf7-mpi-debuginfo\t/
%filter_from_requires /^debug.*(libhdf5\.so.*/s/^/libhdf5-8-mpi-debuginfo\t/

%files -n lib%name
%doc exodus/COPYRIGHT exodus/README README.Nemesis ChangeLog
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%files -n lib%name-devel-doc
#doc exodus/html exodus/doc/* nemesis/doc/*
%doc exodus/html exodus/doc/*

%files -n python-module-exodus
%python_sitelibdir/*

%changelog
* Wed Jul 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.14.0-alt7.git20140623
- New snapshot

* Thu May 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.14.0-alt7.git20140509
- New snapshot

* Tue Nov 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.14.0-alt7.git20130820
- New snapshot

* Mon Feb 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.14.0-alt7.git20120917
- New snapshot

* Sat Aug 18 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.14.0-alt7
- New snapshot

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

