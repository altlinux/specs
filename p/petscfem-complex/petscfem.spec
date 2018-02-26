%define mpiimpl openmpi
%define mpidir %_libexecdir/%mpiimpl

%define scalar_type complex
%define ldir %_libexecdir/petsc-%scalar_type

%define oname petscfem
%define somver 0
%define sover %somver.0.0

Name: %oname-%scalar_type
Version: 3.53.1
Release: alt3.beta
Summary: A General Purpose, Parallel, Multi-Physics FEM Program (%scalar_type scalars)
License: GPL v2+
Group: Sciences/Mathematics
Url: http://www.cimec.org.ar/petscfem
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %oname-%version.tar
Source1: mstorti.sty

BuildPreReq: libpetsc-%scalar_type-devel %mpiimpl-devel liblapack-devel
BuildPreReq: libnewmat-devel libparmetis0-devel libsuperlu-devel
BuildPreReq: libann-devel glib2-devel libopendx-devel libmetis0-devel
BuildPreReq: liblibretto-devel libmeschach-devel libscotch-devel
BuildPreReq: texlive-extra-utils svg2pdf latex2html doc++
BuildPreReq: libhypre-devel-doc ghostscript-utils chrpath
BuildPreReq: libtrilinos-devel libgaleri-devel c2html
BuildPreReq: transfig tgif rpm-macros-make perl-devel

Requires: lib%name = %version-%release

%description
This is PETSc-FEM, a general purpose, parallel, multi-physics FEM
(Finite Element Method) program for CFD (Computational Fluid Dynamics)
applications based on PETSc . PETSc-FEM comprises both a library that
allows the user to develop FEM (or FEM-like, i.e. non-structured mesh
oriented) programs, and a suite of application programs. It is written
in the C++ language with an OOP (Object Oriented Programming)
philosophy, keeping in mind the scope of efficiency.

%package -n lib%name
Summary: Shared library of PETSc-FEM (%scalar_type scalars)
Group: System/Libraries

%description -n lib%name
This is PETSc-FEM, a general purpose, parallel, multi-physics FEM
(Finite Element Method) program for CFD (Computational Fluid Dynamics)
applications based on PETSc . PETSc-FEM comprises both a library that
allows the user to develop FEM (or FEM-like, i.e. non-structured mesh
oriented) programs, and a suite of application programs. It is written
in the C++ language with an OOP (Object Oriented Programming)
philosophy, keeping in mind the scope of efficiency.

This package contains shared library of PETSc-FEM.

%package -n lib%name-devel
Summary: Development files of PETSc-FEM (%scalar_type scalars)
Group: Development/C++
BuildArch: noarch
Requires: lib%name = %version-%release
Requires: libpetsc-%scalar_type-devel

%description -n lib%name-devel
This is PETSc-FEM, a general purpose, parallel, multi-physics FEM
(Finite Element Method) program for CFD (Computational Fluid Dynamics)
applications based on PETSc . PETSc-FEM comprises both a library that
allows the user to develop FEM (or FEM-like, i.e. non-structured mesh
oriented) programs, and a suite of application programs. It is written
in the C++ language with an OOP (Object Oriented Programming)
philosophy, keeping in mind the scope of efficiency.

This package contains development files of PETSc-FEM.

%package -n %oname-docs
Summary: Documentation for PETSc-FEM
Group: Documentation
BuildArch: noarch

%description -n %oname-docs
This is PETSc-FEM, a general purpose, parallel, multi-physics FEM
(Finite Element Method) program for CFD (Computational Fluid Dynamics)
applications based on PETSc . PETSc-FEM comprises both a library that
allows the user to develop FEM (or FEM-like, i.e. non-structured mesh
oriented) programs, and a suite of application programs. It is written
in the C++ language with an OOP (Object Oriented Programming)
philosophy, keeping in mind the scope of efficiency.

This package contains development files of PETSc-FEM.

%prep
%setup
install -m644 %SOURCE1 doc
ln -s ../index.tex doc/manual
ln -s /usr/share/doc/libhypre-devel-doc/docxx.sty doc/manual

%build
source %_bindir/petsc-%scalar_type.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-R,%mpidir/lib:%ldir/lib -L%mpidir/lib -L%ldir/lib"

%add_optflags -I%_includedir/gotoblas
%make_ext -C src amplidl.o
for i in depend libpetscfem; do
	%make_ext $i SOMVER=%somver SOVER=%sover
done
%make_ext all SOMVER=%somver SOVER=%sover

%if "%scalar_type" == "real"
%make_build -C doc
%make_build -C doc/manual ps
export C2HTML=c2html
%make_build -C doc/manual man_html
%endif

%install
source %_bindir/petsc-%scalar_type.sh
install -d %buildroot%ldir/bin
install -d %buildroot%ldir/lib
install -d %buildroot%ldir/include/%name

install -m755 applications/*/*.bin %buildroot%ldir/bin
for i in %buildroot%ldir/bin/*; do
	chrpath -r %mpidir/lib:$PETSC_DIR/lib $i
done

install -m644 *.so.* %buildroot%ldir/lib
ln -s lib%oname.so.%sover %buildroot%ldir/lib/lib%oname.so.%somver
ln -s lib%oname.so.%somver %buildroot%ldir/lib/lib%oname.so

install -p -m644 src/*.h %buildroot%ldir/include/%name

%files
%doc README* PROJECTS TODO
%ldir/bin/*

%files -n lib%name
%ldir/lib/*.so.*

%files -n lib%name-devel
%ldir/lib/*.so
%ldir/include/*

%if "%scalar_type" == "real"
%files -n %oname-docs
%doc doc/*.pdf doc/OBJ/*.pdf doc/manual/html
%endif

%changelog
* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.53.1-alt3.beta
- Fixed RPATH

* Sat Dec 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.53.1-alt2.beta
- New snapshot

* Sat Nov 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.53.1-alt1.beta.7
- Rebuilt with perl 5.14.2

* Wed Sep 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.53.1-alt1.beta.6
- Rebuilt with libparmetis0 instead of libparmetis

* Sun Sep 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.53.1-alt1.beta.5
- Rebuilt with metis 5.0.1

* Thu May 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.53.1-alt1.beta.4
- New snapshot

* Wed Apr 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.53.1-alt1.beta.3
- Built with GotoBLAS instead of ATLAS

* Tue Mar 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.53.1-alt1.beta.2
- Rebuilt for debuginfo

* Sat Feb 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.53.1-alt1.beta.1
- Rebuilt with parmetis 3.1.1-alt10

* Fri Dec 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.53.1-alt1.beta
- Initial build for Sisyphus
