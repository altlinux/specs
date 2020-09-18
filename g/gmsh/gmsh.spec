Name: gmsh
Summary: Automatic 3D finite element grid generator
Version: 4.6.0
Release: alt1
Group: Sciences/Mathematics
License: GPLv2
URL: https://gmsh.info/

Source: %name-%version.tar

Requires: getdp

# Can't build with libopenblas, use libatlas.
# Libatlas exists only for following architectures:
ExclusiveArch: %ix86 amd64 x86_64

BuildPreReq: rpm-macros-cmake rpm-build-python
BuildRequires: cmake gcc-c++ gcc-fortran
BuildRequires: libglvnd-devel libfltk-devel libGLU-devel
BuildRequires: libX11-devel libXft-devel
BuildRequires: libXcursor-devel libXinerama-devel
BuildRequires: libXext-devel libXfixes-devel libXrender-devel
BuildRequires: fontconfig-devel libfreetype-devel
BuildRequires: libjpeg-devel zlib-devel libpng-devel
BuildRequires: libatlas-devel liblapack-devel OCE-devel

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

%build
%cmake_insource -DCMAKE_BUILD_TYPE=Release
%make_build VERBOSE=1

%install
%makeinstall_std

%files
%_bindir/%name
%_man1dir/%name.*
%dir %_docdir/%name
%doc %_docdir/%name/*.txt

%files demos
%_docdir/%name/demos
%_docdir/%name/tutorial

%changelog
* Fri Sep 18 2020 Vladislav Zavjalov <slazav@altlinux.org> 4.6.0-alt1
- Version 4.6.0, return the package to Altlinux.
- Cleanup spec, build in the default upstream configuration.
- No library, no python/julia/c/c++ interfaces.

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 2.8.5-alt2.svn20140707.1
- NMU: added BR: texinfo

* Thu Mar 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.5-alt2.svn20140707
- Rebuilt with OpenCASCADE 6.8.0

* Tue Jul 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.5-alt1.svn20140707
- New snapshot

* Thu Jun 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.5-alt1.svn20140618
- Version 2.8.5

* Wed Nov 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.4-alt1.svn20131112
- Version 2.8.4

* Fri Sep 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.1-alt2.svn20130710
- Rebuilt with OpenCASCADE 6.6.0

* Wed Jul 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.1-alt1.svn20130710
- Version 2.8.1

* Wed Jun 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.2-alt1.svn20130201
- Version 2.7.2

* Tue May 07 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.2-alt6.svn20130201
- Fixed build

* Thu Feb 07 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.2-alt5.svn20130201
- Rebuilt with OpenCASCADE 6.5.4

* Fri Feb 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.2-alt4.svn20130201
- New snapshot

* Wed Oct 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.2-alt4.svn20120814
- Rebuilt with gcc 4.7

* Wed Sep 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.2-alt3.svn20120814
- Rebuilt with libpng15

* Wed Sep 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.2-alt2.svn20120814
- Rebuilt with external ANN, ParMetis, Mmg3d and Netgen
- Built with OpenCASCADE

* Wed Aug 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.2-alt1.svn20120814
- Version 2.6.2

* Wed Jul 18 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt7.svn20100906
- Fixed build

* Sat Jul 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt6.svn20100906
- Rebuilt with PETSc 3.2_p7-alt3

* Thu Jul 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt5.svn20100906
- Rebuilt with OpenMPI 1.6

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

