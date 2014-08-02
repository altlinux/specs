%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define oname Scientific

%def_without python3

Name: python-module-%oname
Version: 2.9.3
Release: alt1
Summary: Collection of Python modules for scientific computing
License: CeCILL
Group: Development/Python
Url: http://sourcesup.cru.fr/projects/scientific-py/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: ScientificPython-%version.tar

BuildPreReq: libnumpy-devel libnetcdf-mpi-devel %mpiimpl-devel
BuildPreReq: python-module-Numeric-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel libnumpy-py3-devel
BuildPreReq: python-tools-2to3
%endif

%description
ScientificPython is a collection of Python modules that are useful
for scientific computing. In this collection you will find modules
that cover basic geometry (vectors, tensors, transformations, vector
and tensor fields), quaternions, automatic derivatives, (linear)
interpolation, polynomials, elementary statistics, nonlinear
least-squares fits, unit calculations, Fortran-compatible text
formatting, 3D visualization via VRML, and two Tk widgets for simple
line plots and 3D wireframe models.

%package -n python3-module-%oname
Summary: Collection of Python modules for scientific computing
Group: Development/Python3

%description -n python3-module-%oname
ScientificPython is a collection of Python modules that are useful
for scientific computing. In this collection you will find modules
that cover basic geometry (vectors, tensors, transformations, vector
and tensor fields), quaternions, automatic derivatives, (linear)
interpolation, polynomials, elementary statistics, nonlinear
least-squares fits, unit calculations, Fortran-compatible text
formatting, 3D visualization via VRML, and two Tk widgets for simple
line plots and 3D wireframe models.

%package -n python3-module-%oname-devel
Summary: Development files of Scientific Python
Group: Development/Python3
BuildArch: noarch
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-devel
ScientificPython is a collection of Python modules that are useful
for scientific computing. In this collection you will find modules
that cover basic geometry (vectors, tensors, transformations, vector
and tensor fields), quaternions, automatic derivatives, (linear)
interpolation, polynomials, elementary statistics, nonlinear
least-squares fits, unit calculations, Fortran-compatible text
formatting, 3D visualization via VRML, and two Tk widgets for simple
line plots and 3D wireframe models.

This package contains development files of Scientific Python.

%package -n python3-module-%oname-tests
Summary: Tests and examples for Scientific Python
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
ScientificPython is a collection of Python modules that are useful
for scientific computing. In this collection you will find modules
that cover basic geometry (vectors, tensors, transformations, vector
and tensor fields), quaternions, automatic derivatives, (linear)
interpolation, polynomials, elementary statistics, nonlinear
least-squares fits, unit calculations, Fortran-compatible text
formatting, 3D visualization via VRML, and two Tk widgets for simple
line plots and 3D wireframe models.

This package contains tests and examples for Scientific Python.

%package -n %oname-py3-mpi
Summary: MPI support for Scientific Python
Group: Networking/Other
Requires: python3-module-%oname = %version-%release

%description -n %oname-py3-mpi
ScientificPython is a collection of Python modules that are useful
for scientific computing. In this collection you will find modules
that cover basic geometry (vectors, tensors, transformations, vector
and tensor fields), quaternions, automatic derivatives, (linear)
interpolation, polynomials, elementary statistics, nonlinear
least-squares fits, unit calculations, Fortran-compatible text
formatting, 3D visualization via VRML, and two Tk widgets for simple
line plots and 3D wireframe models.

This package contains MPI support for Scientific Python.

%package devel
Summary: Development files of Scientific Python
Group: Development/Python
BuildArch: noarch
Requires: %name = %version-%release

%description devel
ScientificPython is a collection of Python modules that are useful
for scientific computing. In this collection you will find modules
that cover basic geometry (vectors, tensors, transformations, vector
and tensor fields), quaternions, automatic derivatives, (linear)
interpolation, polynomials, elementary statistics, nonlinear
least-squares fits, unit calculations, Fortran-compatible text
formatting, 3D visualization via VRML, and two Tk widgets for simple
line plots and 3D wireframe models.

This package contains development files of Scientific Python.

%package doc
Summary: Documentation for Scientific Python
Group: Development/Documentation
BuildArch: noarch

%description doc
ScientificPython is a collection of Python modules that are useful
for scientific computing. In this collection you will find modules
that cover basic geometry (vectors, tensors, transformations, vector
and tensor fields), quaternions, automatic derivatives, (linear)
interpolation, polynomials, elementary statistics, nonlinear
least-squares fits, unit calculations, Fortran-compatible text
formatting, 3D visualization via VRML, and two Tk widgets for simple
line plots and 3D wireframe models.

This package contains documentation for Scientific Python.

%package tests
Summary: Tests and examples for Scientific Python
Group: Development/Python
Requires: %name = %version-%release

%description tests
ScientificPython is a collection of Python modules that are useful
for scientific computing. In this collection you will find modules
that cover basic geometry (vectors, tensors, transformations, vector
and tensor fields), quaternions, automatic derivatives, (linear)
interpolation, polynomials, elementary statistics, nonlinear
least-squares fits, unit calculations, Fortran-compatible text
formatting, 3D visualization via VRML, and two Tk widgets for simple
line plots and 3D wireframe models.

This package contains tests and examples for Scientific Python.

%package -n %oname-mpi
Summary: MPI support for Scientific Python
Group: Networking/Other
Requires: %name = %version-%release

%description -n %oname-mpi
ScientificPython is a collection of Python modules that are useful
for scientific computing. In this collection you will find modules
that cover basic geometry (vectors, tensors, transformations, vector
and tensor fields), quaternions, automatic derivatives, (linear)
interpolation, polynomials, elementary statistics, nonlinear
least-squares fits, unit calculations, Fortran-compatible text
formatting, 3D visualization via VRML, and two Tk widgets for simple
line plots and 3D wireframe models.

This package contains MPI support for Scientific Python.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
sed -i 's|@INCLUDES@|%buildroot%python3_includedir%_python3_abiflags|' \
	../python3/Src/MPI/compile.py
sed -i 's|@PYPATH@|%python3_sitelibdir|' \
	../python3/Src/MPI/impipython
%endif

sed -i 's|@INCLUDES@|%buildroot%_includedir/python%_python_version|' \
	Src/MPI/compile.py
sed -i 's|@PYPATH@|%python_sitelibdir|' \
	Src/MPI/impipython

%build
%add_optflags -I%mpidir/include/netcdf-3 -fno-strict-aliasing
export NETCDF_PREFIX=%mpidir
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib -L%mpidir/lib"

%python_build_debug --netcdf_prefix=%mpidir

%if_with python3
pushd ../python3
%python3_build_debug --netcdf_prefix=%mpidir
popd
%endif

%install
CFLAGS="-I%mpidir/include/netcdf-3 -I%mpidir/include"
export CFLAGS="$CFLAGS -fno-strict-aliasing"
export NETCDF_PREFIX=%mpidir
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib -L%mpidir/lib"

%if_with python3
pushd ../python3
%python3_install
export PYTHONPATH=%buildroot%python3_sitelibdir
pushd Src/MPI
python3 compile.py
#chrpath -r %mpidir/lib mpipython
install -p -m755 impipython %buildroot%_bindir/impipython.py3
popd
popd
%endif

%python_install

# MPI support

mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export PYTHONPATH=%buildroot%python_sitelibdir
pushd Src/MPI
python compile.py
#chrpath -r %mpidir/lib mpipython
install -p -m755 *mpipython %buildroot%_bindir
popd

# Tests and examples

cp -fR Examples Tests %buildroot%python_sitelibdir/%oname/

for i in $(find %buildroot%python_sitelibdir/%oname -type d)
do
	touch $i/__init__.py
done
pushd %buildroot%python_sitelibdir/%oname/Examples
rm -f BSP/example4.py
popd

%files
%doc LICENSE PKG-INFO README README.MPI
%_bindir/*
%exclude %_bindir/impipython
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/Tests
%exclude %python_sitelibdir/*/Examples

%files devel
%python_includedir

%files -n %oname-mpi
%_bindir/impipython

%files doc
%doc Doc

%files tests
%python_sitelibdir/*/Tests
%python_sitelibdir/*/Examples

%if_with python3
%files -n python3-module-%oname
%doc LICENSE PKG-INFO README README.MPI
%_bindir/*.py3
%exclude %_bindir/impipython.py3
%python3_sitelibdir/*

%files -n python3-module-%oname-devel
%_includedir/%python3_includedir%_python3_abiflags
%endif

%changelog
* Sat Aug 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.9.3-alt1
- Version 2.9.3

* Fri Oct 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.9.2-alt3
- Rebuilt with python-module-Numeric

* Wed Feb 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.9.2-alt1
- Version 2.9.2

* Fri Sep 14 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.9.1-alt3
- Rebuilt with libnetcdf 4.2.1.1

* Mon Jun 25 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.9.1-alt2
- Rebuilt with OpenMPI 1.6

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.9.1-alt1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.9.1-alt1.1
- Rebuild with Python-2.7

* Thu Apr 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.9.1-alt1
- Version 2.9.1

* Sun Apr 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.9.0-alt6
- Rebuilt with libnetcdf7

* Sat Mar 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.9.0-alt5
- Rebuilt for debuginfo

* Tue Nov 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.9.0-alt4
- Rebuilt with Pyro4 4.2

* Wed Nov 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.9.0-alt3
- Set develpackage as noarch

* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.9.0-alt2
- Rebuilt for soname set-versions
- Fixed overlinking

* Thu Feb 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.9.0-alt1
- Initial build for Sisyphus

