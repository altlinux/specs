Name: calculix-ccx
Version: 2.23
Release: alt3

Summary: A Free Software Three-Dimensional Structural Finite Element Program
License: GPL-2.0-or-later
Group: Engineering
Url: https://www.dhondt.de/

# http://www.dhondt.de/ccx_2.23.src.tar.bz2
Source0: %name-%version.tar
Source99: %name.watch

BuildRequires: gcc-fortran
BuildRequires: libarpack-ng-devel
BuildRequires: fdupes
BuildRequires: liblapack-devel
BuildRequires: libopenblas-devel
BuildRequires: libspooles-devel-static
BuildRequires: libgomp-devel

%description
CalculiX is a package designed to solve field problems. The method used is
the finite element method.
With CalculiX Finite Element Models can be built, calculated and
post-processed. The pre- and post-processor is an interactive 3D-tool using
the openGL API. The solver is able to do linear and non-linear calculations.
Static, dynamic and thermal solutions are available. Both programs can be
used independently. Because the solver makes use of the abaqus input format
it is possible to use commercial pre-processors as well. In turn the
pre-processor is able to write mesh related data for nastran, abaqus, ansys,
code-aster and for the free-cfd codes dolfyn, duns, ISAAC and OpenFOAM.

%prep
%setup

%build
%make_build -C ccx_*/src -f Makefile_MT \
	CC="gcc -std=c99" \
	FC=gfortran \
	CFLAGS="-g -Wall -I%_includedir/spooles -Wno-return-mismatch -Wno-implicit -O2 -fopenmp -DARCH=Linux -DSPOOLES -DARPACK -DMATRIXSTORAGE -DUSE_MT=1" \
	FFLAGS="-g -Wall -O2 -fopenmp -cpp -fallow-argument-mismatch" \
	LIBS="%_libdir/spoolesMT.a %_libdir/spooles.a -larpack -llapack -lopenblas -lpthread -lm"

%install
install -Dpm 0755 ccx_*/src/ccx_*_MT %buildroot%_bindir/ccx

%files
%_bindir/ccx

%changelog
* Fri Sep 04 2026 Ulysses Apokin <ulysses@altlinux.org> 2.23-alt3
- Fix build with with libspooles-devel-static >= 2.2-alt13.

* Thu Jul 16 2026 Ivan A. Melnikov <iv@altlinux.org> 2.23-alt2
- NMU: Build with liblapack-devel instead of obsolete
  liblapack3-devel.

* Wed Jun 03 2026 Ulysses Apokin <ulysses@altlinux.org> 2.23-alt1
- Initial build for Sisyphus.
