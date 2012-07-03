%define fftw_major_ver 3
%define fftw_ver %fftw_major_ver.0.1
%define mpi_impl openmpi
%define mpidir %_libexecdir/%mpi_impl
%def_disable static

Name: gromacs
Version: 4.0.7
Release: alt6

Summary: Molecular dynamics package
License: GPL
Group: Sciences/Chemistry

Url: http://www.gromacs.org
Source: ftp://ftp.gromacs.org/pub/gromacs/%name-%version.tar.gz
Patch: gromacs-4.0.3-alt-LIBS-LDADD.patch
Packager: Michael Shigorin <mike@altlinux.org>

Requires: %name-common = %version-%release
%set_libtool_version 1.5
# Automatically added by buildreq on Thu Mar 24 2011
# optimized out: gcc-c++ gcc-fortran glibc-pthread libICE-devel libatlas-devel libgfortran-devel libstdc++-devel mpi-selector openmpi xorg-xproto-devel
BuildRequires: imake libSM-devel libX11-devel libfftw3-devel libgsl-devel liblapack-devel openmpi-devel xorg-cf-files

BuildRequires: libfftw%fftw_major_ver-devel >= %fftw_ver
BuildRequires: gcc-fortran %mpi_impl-devel chrpath
BuildRequires: libX11-devel libgsl-devel
BuildRequires: liblapack-devel
BuildRequires: libopenmotif-devel

%description
GROMACS is a versatile and extremely well optimized package
to perform molecular dynamics computer simulations and
subsequent trajectory analysis. It is developed for
biomolecules like proteins, but the extremely high
performance means it is used also in several other field
like polymer chemistry and solid state physics.

This package provides single and double precision binaries.
The documentation is in the package gromacs-common.

N.B. All binaries have names starting with g_, for example
mdrun has been renamed to g_mdrun.

%package libs
Summary: GROMACS libraries
Group: Sciences/Chemistry
Requires: gromacs-common = %version-%release

%description libs
GROMACS is a versatile and extremely well optimized package
to perform molecular dynamics computer simulations and
subsequent trajectory analysis. It is developed for
biomolecules like proteins, but the extremely high
performance means it is used also in several other field
like polymer chemistry and solid state physics.

This package provides runtime libraries needed for the
single and double precision binaries.

%package mpi
Summary: GROMACS MPI binaries
Group: Sciences/Chemistry
Requires: gromacs-common = %version-%release

%description mpi
GROMACS is a versatile and extremely well optimized package
to perform molecular dynamics computer simulations and
subsequent trajectory analysis. It is developed for
biomolecules like proteins, but the extremely high
performance means it is used also in several other field
like polymer chemistry and solid state physics.

This package provides MPI single precision and double
precision binaries.

%package common
Summary: GROMACS shared data and man pages
Group: Sciences/Chemistry
BuildArch: noarch

%description common
GROMACS is a versatile and extremely well optimized package
to perform molecular dynamics computer simulations and
subsequent trajectory analysis. It is developed for
biomolecules like proteins, but the extremely high
performance means it is used also in several other field
like polymer chemistry and solid state physics.

This package includes architecture independent data and
man pages.

%package devel
Summary: GROMACS header files and development libraries
Group: Sciences/Chemistry
Requires: gromacs-common = %version-%release
Requires: gromacs-libs = %version-%release

%description devel
GROMACS is a versatile and extremely well optimized package
to perform molecular dynamics computer simulations and
subsequent trajectory analysis. It is developed for
biomolecules like proteins, but the extremely high
performance means it is used also in several other field
like polymer chemistry and solid state physics.

This package contains header files, development libraries,
and a program example for the GROMACS molecular
dynamics software. You need it if you want to write your
own analysis programs.

%package mpi-devel
Summary: GROMACS MPI development libraries
Group: Sciences/Chemistry
Requires: gromacs-mpi-libs = %version-%release
Requires: gromacs-devel =  %version-%release

%description mpi-devel
GROMACS is a versatile and extremely well optimized package
to perform molecular dynamics computer simulations and
subsequent trajectory analysis. It is developed for
biomolecules like proteins, but the extremely high
performance means it is used also in several other field
like polymer chemistry and solid state physics.

This package contains development libraries for GROMACS MPI.
You need it if you want to write your own analysis programs.

%package mpi-libs
Summary: GROMACS libraries
Group: Sciences/Chemistry
Requires: gromacs-common = %version-%release

%description mpi-libs
GROMACS is a versatile and extremely well optimized package
to perform molecular dynamics computer simulations and
subsequent trajectory analysis. It is developed for
biomolecules like proteins, but the extremely high
performance means it is used also in several other field
like polymer chemistry and solid state physics.

This package provides runtime libraries needed for the
MPI single and double precision binaries.

%package shell-extensions
Summary: GROMACS shell extensions
Group: Sciences/Chemistry
Obsoletes: %name-bash
Obsoletes: %name-zsh
Obsoletes: %name-csh

%description shell-extensions
GROMACS is a versatile and extremely well optimized package
to perform molecular dynamics computer simulations and
subsequent trajectory analysis. It is developed for
biomolecules like proteins, but the extremely high
performance means it is used also in several other field
like polymer chemistry and solid state physics.

This package provides the needed
shell extensions for GROMACS

%package tutor
Summary: GROMACS tutorial files
Group: Sciences/Chemistry
BuildArch: noarch

%description tutor
GROMACS is a versatile and extremely well optimized package
to perform molecular dynamics computer simulations and
subsequent trajectory analysis. It is developed for
biomolecules like proteins, but the extremely high
performance means it is used also in several other field
like polymer chemistry and solid state physics.

This package provides tutorials for the use of GROMACS.

%package doc
Summary: Documentation for GROMACS
Group: Development/Documentation
BuildArch: noarch

%description doc
This package contains documentation for GROMACS.

%prep
%setup
%patch -p0

sed -i 's|^\(AM_CPPFLAGS.*\)|\1 -g|' $(find ./ -name Makefile.am)

%build
# Set MPI environment
mpi-selector --set `mpi-selector --list | grep %mpi_impl`
source %_sysconfdir/profile.d/mpi-selector.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-R,%mpidir/lib -L%mpidir/lib"

sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=|g' acinclude.m4
%autoreconf

# params:
# 	$1 - float/double precision
# 	$2 - enable/disable MPI
# 	$3 - program suffix
function buildThis() {
	ln -s ../configure .
	%configure \
		--disable-rpath \
		--enable-static=no \
		--enable-shared \
		--enable-$1 \
		--enable-mpi \
		--enable-prefetch-forces \
		--enable-fortran \
		--with-gnu-ld \
		--with-fft=fftw%fftw_major_ver \
		--with-x \
		--with-gsl \
		--$2-mpi \
		--program-suffix=$3 \
		--with-external-blas=-lgoto2
	sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
		libtool
	sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
	%make_build
}

# Single precision
mkdir single
pushd single
buildThis float disable
popd

# Double precision
mkdir double
pushd double
buildThis double disable _d
popd

# MPI, single precision
mkdir mpi-single
pushd mpi-single
buildThis float enable _mpi
popd

# MPI, double precision
mkdir mpi-double
pushd mpi-double
buildThis double enable _mpi_d
popd

%install
export OMPI_LDFLAGS="-Wl,--as-needed,-R,%mpidir/lib -L%mpidir/lib"

# Single precision
pushd single
%makeinstall_std
popd

# Double precision
pushd double
%makeinstall_std
popd

# MPI, single precision
pushd mpi-single
%makeinstall_std
popd

# MPI, double precision
pushd mpi-double
%makeinstall_std
popd

# Rename binaries and man pages to prevent clashes
# (This is done here so that we don't need to mess with machine generated makefiles.
for bin in anadock do_dssp editconf eneconv genbox genconf genion genrestr \
	gmxcheck gmxdump grompp highway luck make_edi make_ndx mdrun mk_angndx ngmx \
	pdb2gmx protonate sigeps tpbconv trjcat trjconv trjorder wheel x2top xpm2ps \
	xrama
do
	mv %buildroot%_bindir/$bin %buildroot%_bindir/g_$bin
	mv %buildroot%_bindir/${bin}_d %buildroot%_bindir/g_${bin}_d
done

for bin in demux.pl xplor2gmx.pl; do
	mv %buildroot%_bindir/$bin %buildroot%_bindir/g_$bin
done

# MPI-enabled binaries (list will continue when the makefile has
# the possibility to compile all mpi-enabled files
for mpibin in mdrun; do
	mv %buildroot%_bindir/${mpibin}_mpi %buildroot%_bindir/g_${mpibin}_mpi
	mv %buildroot%_bindir/${mpibin}_mpi_d %buildroot%_bindir/g_${mpibin}_mpi_d
done

# Man pages
for bin in anadock do_dssp editconf eneconv genbox genconf genion genrestr \
	gmxcheck gmxdump grompp highway make_edi make_ndx mdrun mk_angndx ngmx \
	pdb2gmx protonate sigeps tpbconv trjcat trjconv trjorder wheel x2top xpm2ps \
	xrama
do
	mv %buildroot%_man1dir/$bin.1 %buildroot%_man1dir/g_$bin.1
	mv %buildroot%_man1dir/${bin}_d.1 %buildroot%_man1dir/g_${bin}_d.1
done

# Move completion files around
chmod a-x %buildroot%_bindir/completion.*
# Zsh
mkdir -p %buildroot%_datadir/zsh/site-functions
mv %buildroot%_bindir/completion.zsh \
	%buildroot%_datadir/zsh/site-functions/gromacs
# Bash
mkdir -p %buildroot%_sysconfdir/bash_completion.d
mv %buildroot%_bindir/completion.bash %buildroot%_sysconfdir/bash_completion.d/gromacs
# Tcsh
mv %buildroot%_bindir/completion.csh .

# Remove .la files
rm -rf %buildroot/%_libdir/*.la

mv mpi-single/src/mdlib/.libs/libmd_mpi.so* %buildroot%_libdir/
mv mpi-double/src/mdlib/.libs/libmd_mpi_d.so* %buildroot%_libdir/

for i in %buildroot%_bindir/* %buildroot%_libdir/*.so.*
do
	chrpath -r %mpidir/lib $i ||:
done

%files
%_bindir/*
%exclude %_bindir/g_mdrun_mpi
%exclude %_bindir/g_mdrun_mpi_d
%exclude %_bindir/GMXRC.csh
%exclude %_bindir/GMXRC.zsh

%files libs
%_libdir/libgmx.so.*
%_libdir/libgmx_d.so.*
%_libdir/libgmxana.so.*
%_libdir/libgmxana_d.so.*
%_libdir/libmd.so.*
%_libdir/libmd_d.so.*

%files mpi
%_bindir/g_mdrun_mpi
%_bindir/g_mdrun_mpi_d

%files mpi-libs
%_libdir/libgmx_mpi.so.*
%_libdir/libgmx_mpi_d.so.*
%_libdir/libgmxana_mpi.so.*
%_libdir/libgmxana_mpi_d.so.*
%_libdir/libmd_mpi.so.*
%_libdir/libmd_mpi_d.so.*

%files common
%doc AUTHORS COPYING README
#_bindir/GMXRC
#_bindir/GMXRC.bash
%_man1dir/*
%_datadir/%name
%exclude %_datadir/%name/template
%exclude %_datadir/%name/tutor
%exclude %_datadir/%name/html

%files devel
%_includedir/%name
%_libdir/libgmx.so
%_libdir/libgmx_d.so
%_libdir/libgmxana.so
%_libdir/libgmxana_d.so
%_libdir/libmd.so
%_libdir/libmd_d.so
%_datadir/%name/template

%files mpi-devel
%_libdir/libgmx_mpi.so
%_libdir/libgmx_mpi_d.so
%_libdir/libgmxana_mpi.so
%_libdir/libgmxana_mpi_d.so
%_libdir/libmd_mpi.so
%_libdir/libmd_mpi_d.so

%files shell-extensions
%_datadir/zsh/site-functions/gromacs
%_bindir/GMXRC.zsh
%config(noreplace) %_sysconfdir/bash_completion.d/gromacs
%doc completion.csh
%_bindir/GMXRC.csh

%files tutor
%_datadir/%name/tutor

%files doc
%_datadir/%name/html

%changelog
* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.7-alt6
- Fixed RPATH

* Sun Apr 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.7-alt5
- Built with GotoBLAS2 instead of ATLAS

* Thu Mar 24 2011 Michael Shigorin <mike@altlinux.org> 4.0.7-alt4
- merged fixups by led@:
  + dropped superfluous BR
  + enabled parallel build
- re-adopting the package
- buildreq -u
- spec cleanup

* Fri Mar 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.7-alt3
- Rebuilt for debuginfo
- Enabled optimization (-O2)

* Thu Oct 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.7-alt2
- Fixed overlinking of libraries

* Wed Jun 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.7-alt1
- Version 4.0.7

* Mon May 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.5-alt1
- Version 4.0.5

* Wed Apr 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt1
- Version 4.0.4

* Fri Mar 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt3
- enable GSL extensions

* Tue Feb 10 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt2
- disable GSL extensions
- merge shell extensions into one package

* Thu Jan 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt1
- 4.0.3

* Thu Jan 04 2007 Michael Shigorin <mike@altlinux.org> 3.3.1-alt1
- built for ALT Linux (based on Mandriva contrib spec
  by Lenny Cartier <lenny/mandriva.com> and original
  one by Erik Lindahl <lindahl/gromacs.org>)
- disable GUI build by default

* Tue Apr 11 2006 Lenny Cartier <lenny@mandriva.com> 3.3.1-1mdk
- 3.3.1

* Mon Nov 07 2005 Nicolas Lécureuil <neoclust@mandriva.org> 3.3-2mdk
- Fix BuildRequires

* Thu Oct 20 2005 Lenny Cartier <lenny@mandriva.com> 3.3-1mdk
- 3.3

* Fri Jun 04 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.2.1-1mdk
- 3.2.1

* Wed Apr 30 2003 Lenny Cartier <lenny@mandrakesoft.com> 3.1.4-3mdk
- buildrequires

* Sun Feb 02 2003 Lenny Cartier <lenny@mandrakesoft.com> 3.1.4-2mdk
- rebuild

* Tue Dec 05 2002 Lenny Cartier <lenny@mandrakesoft.com> 3.1.4-1mdk
- from Austin Acton <aacton@yorkul.ca> :
	- initial package for Mandrake 9.0+
