%define oname openfvm
%define scalar_type complex
%define ldir %_libexecdir/petsc-%scalar_type

%define mpiimpl openmpi
%define mpidir %_libexecdir/%mpiimpl

Name: openfvm-%scalar_type
Version: 1.3
Release: alt2.svn20110401
Summary: General three-dimensional Computational Fluid Dynamics (CFD) solver

Group: Sciences/Mathematics
License: GPL v2 or later
URL: http://openfvm.sourceforge.net/
# https://openfvm.svn.sourceforge.net/svnroot/openfvm
Source: %oname-%version.tar.gz
Source1: openfvm
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Requires: gmsh gnuplot %oname-common = %version-%release

BuildPreReq: python-module-Pyro4 python-module-petsc-config
BuildPreReq: liblaspack-devel libpetsc-%scalar_type-devel
BuildPreReq: texlive-latex-extra libwxGTK2.9-devel libGL-devel
BuildPreReq: libGLUT-devel libamesos10-devel libepetraext10-devel
BuildPreReq: libifpack10-devel libaztecoo10-devel libepetra10-devel
BuildPreReq: libteuchos10-devel libtrilinos10-devel ghostscript-utils
BuildPreReq: chrpath libparmetis0-devel

%description
OpenFVM is a general CFD solver released under the GPL license. It was
developed to simulate the flow in complex 3D geometries. Therefore, the
mesh can be unstructured and contain control volumes with arbitrary
shape. The code uses the finite volume method to evaluate the partial
differential equations. As well as solving the velocity and pressure
fields, the code is capable of solving non-isothermal multiphase flow.

The code has two implementations: serial and parallel. The serial
version uses LASPACK as the linear matrix solver and the parallel one
uses the PETSc library. Both implementations use the open source tool
Gmsh for pre- and post-processing.

%package -n %oname-common
Summary: Scalar type independent files of OpenFVM
Group: Sciences/Mathematics
BuildArch: noarch

%description -n %oname-common
OpenFVM is a general CFD solver released under the GPL license. It was
developed to simulate the flow in complex 3D geometries. Therefore, the
mesh can be unstructured and contain control volumes with arbitrary
shape. The code uses the finite volume method to evaluate the partial
differential equations. As well as solving the velocity and pressure
fields, the code is capable of solving non-isothermal multiphase flow.

This package contains scalar type independent files of OpenFVM.

%package -n %oname-examples
Summary: Examples for OpenFVM
Group: Sciences/Mathematics
BuildArch: noarch
Requires: %name = %version-%release

%description -n %oname-examples
OpenFVM is a general CFD solver released under the GPL license. It was
developed to simulate the flow in complex 3D geometries. Therefore, the
mesh can be unstructured and contain control volumes with arbitrary
shape. The code uses the finite volume method to evaluate the partial
differential equations. As well as solving the velocity and pressure
fields, the code is capable of solving non-isothermal multiphase flow.

This package contains examples for OpenFVM.

%package -n %oname-doc
Summary: Documentation for for OpenFVM
Group: Documentation
BuildArch: noarch

%description -n %oname-doc
OpenFVM is a general CFD solver released under the GPL license. It was
developed to simulate the flow in complex 3D geometries. Therefore, the
mesh can be unstructured and contain control volumes with arbitrary
shape. The code uses the finite volume method to evaluate the partial
differential equations. As well as solving the velocity and pressure
fields, the code is capable of solving non-isothermal multiphase flow.

This package contains documentation for OpenFVM.

%prep
%setup
%if "%scalar_type" == "real"
install -m755 %SOURCE1 %oname
install -m755 %SOURCE1 %oname.ser
sed -i 's|@SUFF@||' %oname
sed -i 's|@SUFF@|.ser|' %oname.ser
%endif

%build
mpi-selector --set %mpiimpl
source %_bindir/petsc-%scalar_type.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-Rpath=%mpidir/lib -L%mpidir/lib"

%make_build -C Flow

%install
source %_bindir/petsc-%scalar_type.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-Rpath=%mpidir/lib -L%mpidir/lib"

%makeinstall_std -C Flow

%if "%scalar_type" == "real"
install -d %buildroot%_bindir
install -m755 %{oname}* %buildroot%_bindir
%endif

for i in %buildroot$PETSC_DIR/bin/*
do
	chrpath -r %mpidir/lib:$PETSC_DIR/lib $i ||:
done

%files
%doc copying
%ldir/bin/*

%if "%scalar_type" == "real"
%files -n %oname-common
%_bindir/*
%exclude %_bindir/%oname-test

%files -n %oname-examples
%dir %_datadir/%oname
%_datadir/%oname/examples
%_bindir/%oname-test

%files -n %oname-doc
%_docdir/%oname
%endif

%changelog
* Sat Dec 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt2.svn20110401
- Rebuilt with PETSc 3.2

* Wed Sep 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.svn20110401.1
- Rebuilt with libparmetis0 instead of libparmetis

* Thu May 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.svn20110401
- New snapshot

* Wed Apr 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.svn20100327.6
- Built with system LASPACK

* Thu Mar 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.svn20100327.5
- Rebuilt for debuginfo

* Sat Feb 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.svn20100327.4
- Rebuilt with parmetis 3.1.1-alt10

* Mon Nov 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.svn20100327.3
- Fixed string buffer overflow

* Fri Oct 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.svn20100327.2
- Rebuilt with wxGTK 2.9

* Tue Aug 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.svn20100327.1
- Rebuilt with python-module-Pyro4

* Fri Aug 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.svn20100327
- Version 1.3
- Rebuilt with PETSc 3.1

* Wed Jul 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.svn20091002.3
- Rebuilt with reformed ParMetis

* Thu Dec 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.svn20091002.2
- Rebuilt with Trilinos v10

* Thu Oct 15 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.svn20091002.1
- Fixed creating illustrations for documentation
- Added build requirements on optimized trilinos packages

* Tue Oct 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.svn20091002
- Initial build for Sisyphus
