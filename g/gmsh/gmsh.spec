%define mpiimpl openmpi
%define mpidir %_libexecdir/%mpiimpl
%define hdf5dir %mpidir
%define petsc_dir %_libexecdir/petsc-real

Name: gmsh
Summary: Automatic 3D finite element grid generator
Version: 2.5.1
Release: alt4.svn20100906
Group: Graphics
License: GPL v2
URL: http://www.geuz.org/gmsh/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://geuz.org/svn/gmsh/trunk/
# login/password: gmsh:gmsh
Source: %name-%version.tar.gz
Source1: CMakeCache.txt

Requires: libcgns-mpi

BuildPreReq: libfltk-devel libjpeg-devel zlib-devel libpng-devel
BuildPreReq: libnetgen-devel libann-devel libchaco-devel chrpath
BuildPreReq: libtetgen-devel getfemxx libGL-devel libGLU-devel libX11-devel
BuildPreReq: libXft-devel libXext-devel libhdf5-mpi-devel %mpiimpl-devel
BuildPreReq: liblapack-devel texlive-base-bin libcairo-devel libavcodec53
BuildPreReq: cmake libICE-devel libSM-devel
BuildPreReq: libXtst-devel libXau-devel libtaucs-devel libgmp-devel
BuildPreReq: libcgns-mpi-devel libXcomposite-devel libpixman-devel
BuildPreReq: libXcursor-devel libXdmcp-devel libXinerama-devel libXpm-devel
BuildPreReq: libXrandr-devel libXt-devel libXv-devel libXxf86misc-devel
BuildPreReq: libslepc-real-devel flex libamesos10
BuildPreReq: libepetraext10 libifpack10 libtrilinos10 libgaleri10

%description
Gmsh is an automatic 3D finite element grid generator with a built-in CAD engine
and post-processor. Its design goal is to provide a simple meshing tool for
academic problems with parametric input and advanced visualization capabilities.

Gmsh is built around four modules: geometry, mesh, solver and post-processing.
The specification of any input to these modules is done either interactively
using the graphical user interface or in ASCII text files using Gmsh's own
scripting language.

%package demos
Summary: Tutorial and demo files for Gmsh
Group: Graphics
BuildArch: noarch

%description demos
Gmsh is an automatic 3D finite element grid generator with a built-in CAD engine
and post-processor. Its design goal is to provide a simple meshing tool for
academic problems with parametric input and advanced visualization capabilities.

Gmsh is built around four modules: geometry, mesh, solver and post-processing.
The specification of any input to these modules is done either interactively
using the graphical user interface or in ASCII text files using Gmsh's own
scripting language.

This package contains tutorial and demo files for Gmsh.

%prep
%setup
install -p -m644 %SOURCE1 .
sed -i 's|@LIBDIR@|%_libdir|g' CMakeCache.txt
sed -i 's|@MPIDIR@|%mpidir|g' CMakeCache.txt
sed -i 's|@PETSC_DIR@|%petsc_dir|g' CMakeCache.txt

sed -i 's|@LIBDIR@|%_libdir|g' CMakeLists.txt

# avoid conflict with defs.h in other packages
ln -s defs.h contrib/Chaco/main/chaco_defs.h
CHACO_FILES="$(egrep -R 'defs\.h' contrib/Chaco/|awk -F : '{print $1}')"
sed -i 's|defs\.h|chaco_defs.h|' $CHACO_FILES

%build
mpi-selector --set %mpiimpl
source %_bindir/petsc-real.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib:%_libdir/oski -L%mpidir/lib -L%_libdir/oski"
export LD_LIBRARY_PATH=%_libdir/oski

cmake .
%make_build VERBOSE=1
%make info

%install
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib:%_libdir/oski -L%mpidir/lib -l%_libdir/oski"
export LD_LIBRARY_PATH=%_libdir/oski

%makeinstall_std

for i in %buildroot%_bindir/*; do
	chrpath -r %mpidir/lib:%petsc_dir/lib $i
done

install -d %buildroot%_infodir
install -m644 doc/texinfo/*.info* %buildroot%_infodir

install -p -m644 doc/*.html %buildroot%_docdir/%name

# antirepocop
rm -fR %buildroot%_includedir

%filter_from_requires /^debug.*(libcgns\.so.*/s/^/libcgns-mpi-debuginfo\t/

%files
%dir %_docdir/%name
%doc %_docdir/%name/*.txt
%doc %_docdir/%name/*.html
%_bindir/*
%_man1dir/*
%_infodir/*

%files demos
%dir %_docdir/%name
%_docdir/%name/demos
%_docdir/%name/tutorial

%changelog
* Wed Jun 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt4.svn20100906
- Fixed build

* Wed Feb 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt3.svn20100906
- Built without OSMesa

* Mon Dec 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt2.svn20100906
- Rebuilt with PETSc 3.2

* Mon May 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1.svn20100906.8
- Rebuilt with cgns 3.1.3

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1.svn20100906.7
- Rebuilt with FLTK 1.3.0.r8575

* Thu Apr 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1.svn20100906.6
- Rebuilt

* Tue Apr 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1.svn20100906.5
- Built with GotoBLAS2 instead of ATLAS

* Mon Mar 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1.svn20100906.4
- Rebuilt for debuginfo

* Fri Mar 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1.svn20100906.3
- Added -g into compiler flags

* Mon Jan 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1.svn20100906.2
- Rebuilt with libfltk13

* Wed Nov 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1.svn20100906.1
- Fixed clear() function in Geo/MZoneBoundary.h

* Sun Nov 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1.svn20100906
- Version 2.5.1

* Mon Aug 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.0-alt1.svn20100620.1
- Enabled MPI parallelization
- Rebuilt with PETSc 3.1

* Mon Jun 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.0-alt1.svn20100620
- Version 2.5.0

* Thu Dec 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.3-alt1.svn20091216
- Version 2.4.3

* Tue Nov 10 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.2-alt1.svn20091109
- Version 2.4.2
- Rebuilt with texlive instead of tetex

* Mon Sep 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.1-alt1
- Initial build for Sisyphus

