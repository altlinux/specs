Name: nsc2ke
Version: 1.0
Release: alt2
Summary: Computing 2D and axisymmetric flows on unstructured meshes
License: Free
Group: Sciences/Mathematics
Url: http://pauillac.inria.fr/cdrom_a_graver/www/nsc2ke/eng.htm
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://pauillac.inria.fr/cdrom_a_graver/ftp/nsc2ke/nsc2ke.tar.gz
Source: %name-%version.tar
Source1: http://pauillac.inria.fr/cdrom_a_graver/ftp/nsc2ke/nsc2ke.ps.gz

BuildPreReq: gcc-fortran

%description
NSC2KE is a Finite-Volume Galerkin program computing 2D and axisymmetric
flows on unstructured meshes. To solve the Euler part of the equations,
a Roe, an Osher and a Kinetic solvers are available. To compute
turbulent flows a k-epsilon model is available. Near-wall turbulence is
computed either by wall-laws or by a two-layer approach. Time dependant
problems can also be considered as a fourth order Runge-Kutta solver has
been used.

%package doc
Summary: The technical INRIA rapport from Rocquencourt
Group: Documentation
BuildArch: noarch

%description doc
NSC2KE is a Finite-Volume Galerkin program computing 2D and axisymmetric
flows on unstructured meshes. To solve the Euler part of the equations,
a Roe, an Osher and a Kinetic solvers are available. To compute
turbulent flows a k-epsilon model is available. Near-wall turbulence is
computed either by wall-laws or by a two-layer approach. Time dependant
problems can also be considered as a fourth order Runge-Kutta solver has
been used.

This package contains the technical INRIA rapport from Rocquencourt.

%prep
%setup
install -p -m644 %SOURCE1 .

%build
%make_build

%install
install -d %buildroot%_bindir
install -d %buildroot%_datadir/%name

install -m755 NSC2KE %buildroot%_bindir
install -p -m644 AXI.MESH DATA gnu.data MESH \
	%buildroot%_datadir/%name

%files
%doc READ_ME
%_bindir/*
%_datadir/%name

%files doc
%doc %name.ps.gz

%changelog
* Mon Mar 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Rebuilt for debuginfo

* Sat Jan 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

