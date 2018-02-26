%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define somver 0
%define sover %somver.0.0

Name: pswarm
%define pyname %{name}_py
Version: 1.5
Release: alt9
Summary: Global optimization solver for bound and linear constrained problems
License: LGPL v2.1
Group: Sciences/Mathematics
Url: http://www.norg.uminho.pt/aivaz/pswarm/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://www.norg.uminho.pt/aivaz/pswarm/software/PPSwarm_v1_5.zip

Requires: lib%name = %version-%release

BuildPreReq: unzip liblapack-devel python-devel R-devel
BuildPreReq: %mpiimpl-devel gcc-fortran libnumpy-devel libmpe2-devel

%description
 PSwarm is a global optimization solver for bound and linear constrained
problems (for which the derivatives of the objective function are
unavailable, inaccurate or expensive).

 The algorithm combines pattern search and particle swarm. Basically, it
applies a directional direct search in the poll step (coordinate search
in the pure simple bounds case) and particle swarm in the search step.

 PSwarm makes no use of derivative information of the objective
function. It has been shown to be efficient and robust for smooth and
nonsmooth problems, both in serial and in parallel.

 The code provides an interface with Python and R. The C code includes a
parallel version using MPI. PSwarm can also be run through the NEOS
server (under the Global Optimization category). You can use PSwarm with
Python problems using the OpenOpt framework.

%package -n lib%name
Summary: Shared libraries of PSwarm
Group: System/Libraries

%description -n lib%name
 PSwarm is a global optimization solver for bound and linear constrained
problems (for which the derivatives of the objective function are
unavailable, inaccurate or expensive).

 The algorithm combines pattern search and particle swarm. Basically, it
applies a directional direct search in the poll step (coordinate search
in the pure simple bounds case) and particle swarm in the search step.

This package contains shared libraries of PSwarm.

%package -n lib%name-devel
Summary: Development files of PSwarm
Group: Development/C
Requires: lib%name = %version-%release
Requires: python-module-%pyname = %version-%release

%description -n lib%name-devel
 PSwarm is a global optimization solver for bound and linear constrained
problems (for which the derivatives of the objective function are
unavailable, inaccurate or expensive).

 The algorithm combines pattern search and particle swarm. Basically, it
applies a directional direct search in the poll step (coordinate search
in the pure simple bounds case) and particle swarm in the search step.

This package contains development files of PSwarm.

%package -n lib%name-devel-static
Summary: Static libraries of PSwarm
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
 PSwarm is a global optimization solver for bound and linear constrained
problems (for which the derivatives of the objective function are
unavailable, inaccurate or expensive).

 The algorithm combines pattern search and particle swarm. Basically, it
applies a directional direct search in the poll step (coordinate search
in the pure simple bounds case) and particle swarm in the search step.

This package contains static libraries of PSwarm.

%package -n python-module-%pyname
Summary: Python interface of PSwarm
Group: Development/Python
%setup_python_module %pyname

%description -n python-module-%pyname
 PSwarm is a global optimization solver for bound and linear constrained
problems (for which the derivatives of the objective function are
unavailable, inaccurate or expensive).

 The algorithm combines pattern search and particle swarm. Basically, it
applies a directional direct search in the poll step (coordinate search
in the pure simple bounds case) and particle swarm in the search step.

This package contains Python interface of PSwarm.

%package -n python-module-%{name}_test
Summary: Test for Python interface of PSwarm
Group: Development/Python
Requires: python-module-%pyname = %version-%release
%setup_python_module %{name}_test

%description -n python-module-%{name}_test
 PSwarm is a global optimization solver for bound and linear constrained
problems (for which the derivatives of the objective function are
unavailable, inaccurate or expensive).

 The algorithm combines pattern search and particle swarm. Basically, it
applies a directional direct search in the poll step (coordinate search
in the pure simple bounds case) and particle swarm in the search step.

This package contains test for Python interface of PSwarm.

%package -n R-%name
Summary: R interface of PSwarm
Group: Sciences/Mathematics

%description -n R-%name
 PSwarm is a global optimization solver for bound and linear constrained
problems (for which the derivatives of the objective function are
unavailable, inaccurate or expensive).

 The algorithm combines pattern search and particle swarm. Basically, it
applies a directional direct search in the poll step (coordinate search
in the pure simple bounds case) and particle swarm in the search step.

This package contains R interface of PSwarm.

%prep
%setup
rm -f ampl *.dll libs/*
%if "%_python_version" != "2.5"
sed -i 's|2\.5|%_python_version|g' makefile
%endif
sed -i 's|@MPIDIR@|%mpidir|' makefile
sed -i 's|@SOMVER@|%somver|' makefile
sed -i 's|@SOVER@|%sover|' makefile

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-R,%mpidir/lib -L%mpidir/lib"

for i in parallel_linear parallel \
	serial_linear serial \
	r_linear r \
	py_linear py
do
	%make_build $i
done

%install
install -d %buildroot%_bindir
install -m755 %name.parallel* %name.serial* \
	%buildroot%_bindir
ln -s %name.parallel_linear %buildroot%_bindir/%name

install -d %buildroot%_libdir
install -m644 *.a %buildroot%_libdir
cp -P *.so* %buildroot%_libdir/
install -d %buildroot%_includedir/%name
install -p -m644 *.h %buildroot%_includedir
install -p -m644 include/* %buildroot%_includedir/%name

RLIBDIR=$(pkg-config libR --variable=rlibdir)
install -d %buildroot$RLIBDIR
install -m644 pswarm_r*.so %buildroot$RLIBDIR
pushd %buildroot
find ./$RLIBDIR -type f |sed 's|.\(.*\)|\1|' > \
	$OLDPWD/R-files
popd

install -d %buildroot%python_sitelibdir/pswarm_test
install -m644 pswarm_py*.so %buildroot%python_sitelibdir
touch __init__.py
install -p -m644 *.py %buildroot%python_sitelibdir/pswarm_test

%files
%doc lgpl.txt README.txt
%_bindir/*

%files -n lib%name
%_libdir/*.so.*
%_libdir/*.sol

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%files -n lib%name-devel-static
%_libdir/*.a

%files -n python-module-%pyname
%python_sitelibdir/%{pyname}*

%files -n python-module-%{name}_test
%python_sitelibdir/%{name}_test

%files -n R-%name -f R-files
%doc *.r

%changelog
* Mon Jun 25 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt9
- Rebuilt with OpenMPI 1.6

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt8
- Fixed RPATH

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5-alt7.1
- Rebuild with Python-2.7

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt7
- Enabled interface with R

* Sat Apr 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt6
- Built with GotoBLAS2 instead of ATLAS
- Disabled interface with R

* Mon Mar 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt5
- Rebuilt for debuginfo

* Sat Nov 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt4
- Rebuilt for soname set-versions

* Fri Jun 11 2010 Alexey Tourbin <at@altlinux.ru> 1.5-alt3.1
- Rebuilt with libR-2.11.so

* Fri Mar 05 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt3
- Rebuilt with reformed NumPy
- Added shared libraries

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt2
- Rebuilt with python 2.6

* Tue Aug 04 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1
- Initial build for Sisyphus

