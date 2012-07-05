%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

Name: freefem3d
Version: 1.0pre10
Release: alt5
Summary: 3D solver of partial differential equations
License: GPLv2+
Group: Sciences/Mathematics
Url: http://www.freefem.org/ff3d/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: %mpiimpl-devel perl-devel
BuildPreReq: libX11-devel libvtk-devel libqt4-devel
BuildPreReq: texlive-latex-base texlive-base-bin
BuildPreReq: texlive-latex-recommended

%description
ff3d, as well as its cousins, is a PDE solver driven by a user-friendly
language. It solves many kind of problems such as elasticity, fluids
(Stokes and Navier-Stokes) and a lot more. The user has to enter the
equation associated with the problem, giving either the PDE in strong
formulation or weak (variational) formulation.

ff3d can use either the Finite Elements method (the mesh of the geometry
being provided by the user) or a Fictitious Domain like approach where
the geometry is described using Constructive Solid Geometry (CSG). This
description is done using the POV-Ray language but others such as VRML
could be added.

The processing of the results is left to the user. One can use various
graphic tools: output in the MEdit mesh format or VTK are supported. The
implementation of a Qt-VTK based GUI module is underway.

%package docs
Summary: Documentation for freefem3d
Group: Documentation
BuildArch: noarch

%description docs
ff3d, as well as its cousins, is a PDE solver driven by a user-friendly
language. It solves many kind of problems such as elasticity, fluids
(Stokes and Navier-Stokes) and a lot more. The user has to enter the
equation associated with the problem, giving either the PDE in strong
formulation or weak (variational) formulation.

This package contains documentation for freefem3d.

%prep
%setup

%build
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"
export PATH=%_qt4dir/bin:$PATH

%add_optflags -I%_includedir/vtk-5.10
%autoreconf
%configure \
	--enable-optimize \
	--enable-gui \
	--enable-pthread \
	--with-x
%make_build

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%makeinstall_std

%files
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%_bindir/*
%_man1dir/*

%files docs
%_docdir/%name

%changelog
* Thu Jul 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0pre10-alt5
- Rebuilt with OpenMPI 1.6

* Sat Jun 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0pre10-alt4
- Rebuilt with VTK 5.10.0

* Mon May 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0pre10-alt3
- Fixed build

* Fri Sep 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0pre10-alt2
- Rebuilt with VTK 5.8.0

* Wed May 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0pre10-alt1
- Initial build for Sisyphus

