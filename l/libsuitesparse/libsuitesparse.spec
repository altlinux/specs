%define _unpackaged_files_terminate_build 1

%define cholmod_ver 3.0.14
%define umfpack_ver 5.7.9

%define _cmake__builddir BUILD

Name: libsuitesparse
Version: 5.10.1
Release: alt1

Summary: Shared libraries for sparse matrix calculations
License: LGPL and GPL
Group: Sciences/Mathematics
Url: http://faculty.cse.tamu.edu/davis/suitesparse.html

# https://github.com/DrTimothyAldenDavis/SuiteSparse.git
Source: %name-%version.tar

Source1: cholmod.pc
Source2: umfpack.pc

Patch1: %name-alt-rename-build-directory.patch
Patch2: %name-alt-link-with-libatomic-on-mipsel.patch

Patch2000: %name-e2k.patch

BuildRequires: libmetis-devel gcc-c++ libtbb-devel
BuildRequires: libblas-devel
BuildRequires: libgmp-devel
BuildRequires: libmpfr-devel

# Automatically added by buildreq on Sun Sep 14 2008
BuildRequires: gcc-fortran liblapack-devel texlive-latex-base
BuildRequires: libgomp-devel
BuildRequires: cmake

%package devel
Summary: Development files of SuiteSparse
Group: Development/Other
Requires: %name = %EVR
Conflicts: libumfpack-devel UFconfig

%package devel-static
Summary: Static libraries of SuiteSparse
Group: Development/Other
Requires: %name-devel = %EVR
Conflicts: %name-devel < %EVR

%package devel-doc
Summary: Documentation for %name
Group: Sciences/Mathematics
BuildArch: noarch

%package examples
Summary: Examples for %name
Group: Sciences/Mathematics
BuildArch: noarch

%package tools
Summary: %name tools
Group: Sciences/Mathematics
Requires: %name = %EVR

%description
Package contains a set of shared libraries to use efficient calculation
algorithms with sparse matricies.

%description devel
Package contains a set of development files to use efficient calculation
algorithms with sparse matricies in your programs.

%description devel-static
Package contains a set of static libraries to use efficient calculation
algorithms with sparse matricies in your programs.

%description devel-doc
Documentation for a set of static libraries that provide an efficient
calculation algorithms with sparse matricies for your programs.

%description examples
Examples for SuiteSparse.

%description tools
Package contains Mongoose executable.
Mongoose executable can read a Matrix Market file containing an adjacency
matrix and output timing and partitioning information to a plain-text file.
Simply call it with the following syntax:
mongoose <MM-input-file.mtx> [output-file]

%prep
%setup
install -m644 %SOURCE1 %SOURCE2 .
%patch1 -p1
%patch2 -p1
%ifarch %e2k
%patch2000 -p1
%endif

# Copy examples src
mkdir demos-src/
cp -rpf --parents $(find ./ -name Demo) demos-src/

%build
sed -i "s|@VERSION@|%cholmod_ver|" cholmod.pc
sed -i "s|@VERSION@|%umfpack_ver|" umfpack.pc

%ifnarch %e2k
# Remove rpath due to "RPATH contains illegal entry" error
sed -i 's/ -Wl,-rpath=$(INSTALL_LIB)//' SuiteSparse_config/SuiteSparse_config.mk
%endif
pushd GraphBLAS
%cmake -DCMAKE_INSTALL_LIBDIR=%_libdir -DCMAKE_INSTALL_INCLUDEDIR=%_includedir
popd
pushd Mongoose
%cmake -DCMAKE_INSTALL_BINDIR=%_bindir -DCMAKE_INSTALL_LIBDIR=%_libdir -DCMAKE_INSTALL_INCLUDEDIR=%_includedir
popd
pushd metis-5.1.0
export GKLIB_PATH=$(pwd)/GKlib
%cmake -DGKLIB_PATH=${GKLIB_PATH}
popd

export JOBS=%__nprocs
%make -C SuiteSparse_config MY_METIS_LIB=-lmetis MY_METIS_INC=%_includedir/metis
%make -C CCOLAMD MY_METIS_LIB=-lmetis MY_METIS_INC=%_includedir/metis
%make TOPDIR=$PWD LD_LIBRARY_PATH=%_builddir/%name-%version/lib MY_METIS_LIB=-lmetis MY_METIS_INC=%_includedir/metis
%make docs MY_METIS_LIB=-lmetis MY_METIS_INC=%_includedir/metis

%install
install -d %buildroot%_libdir
install -d %buildroot%_includedir/suitesparse

%makeinstall_std MY_METIS_LIB=-lmetis MY_METIS_INC=%_includedir/metis INSTALL=%buildroot%_exec_prefix INSTALL_LIB=%buildroot%_libdir INSTALL_DOC=%buildroot%_docdir/%name-%version INSTALL_INCLUDE=%buildroot%_includedir/suitesparse

# Remove unnecessary static libraries
rm -f %buildroot%_libdir/*.a

install -p -m644 CXSparse/Include/cs.h \
	%buildroot%_includedir/suitesparse/cx_cs.h
install -d %buildroot%_pkgconfigdir
install -m644 *.pc %buildroot%_pkgconfigdir

pushd demos-src/
for i in $(find ./ -name Demo); do
	rm -f $(find $i -name '*.m')
	wcl=$(ls $i |wc -l)
	if [ "$wcl" != "0" ]; then
		install -d %buildroot%_datadir/%name/demos/$i
		cp -fR $i/* %buildroot%_datadir/%name/demos/$i/
	fi
done
popd

install -d %buildroot%_docdir/%name-%version/ChangeLogs
for i in BTF CAMD AMD CCOLAMD CHOLMOD COLAMD CSparse CXSparse KLU LDL \
	RBio SPQR UMFPACK
do
	install -p -m644 $i/Doc/ChangeLog \
		%buildroot%_docdir/%name-%version/ChangeLogs/ChangeLog.$i
done

pushd UMFPACK/Doc
for i in *.pdf; do
	mv $i UMFPACK_$i
done
popd
install -d %buildroot%_docdir/%name-%version/pdf
for i in AMD CAMD CHOLMOD KLU LDL SPQR UMFPACK
do
	install -p -m644 $i/Doc/*.pdf %buildroot%_docdir/%name-%version/pdf
done

mv %buildroot%_docdir/%name-%version/*.pdf %buildroot%_docdir/%name-%version/pdf/

%files
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*

%files devel-doc
%_docdir/%name-%version

%files examples
%_datadir/%name/demos/

%files tools
%_bindir/mongoose

%changelog
* Wed Jul 28 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 5.10.1-alt1
- Updated to upstream version 5.10.1.

* Mon Jul 19 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 5.8.1-alt4
- Added patch for Elbrus.

* Thu Jun 10 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 5.8.1-alt3
- Fixed build with new cmake macros.

* Fri Mar 19 2021 Ivan A. Melnikov <iv@altlinux.org> 5.8.1-alt2
- Link with -latomic on mipsel.

* Thu Sep 17 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 5.8.1-alt1
- Updated to upstream version 5.8.1.

* Tue Jun 04 2019 Slava Aseev <ptrnine@altlinux.org> 5.4.0-alt1
- Updated to stable upstream version 5.4.0.

* Fri Nov 30 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 5.1.2-alt2
- Fixed build with new gcc.

* Wed Feb 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 5.1.2-alt1
- Updated to stable upstream version 5.1.2.

* Wed Jul 12 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.5.5-alt1
- Updated to upstream version 4.5.5

* Thu Nov 14 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1-alt1
- Version 4.2.1

* Mon Sep 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1
- Version 4.0.2
- Rebuilt with libmetis instead of libmetis0

* Sun Aug 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt5
- Built with OpenBLAS instead of GotoBLAS2

* Sun Jul 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt4
- Added cs.h for CXSparse as cx_cs.h

* Tue Jul 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt3
- Rebuilt with libmetis0 4.0.3-alt3

* Fri Sep 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt2
- Rebuilt with libmetis0 instead of libmetis

* Thu Sep 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1
- Version 3.6.1

* Fri Apr 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt3
- Rebuilt with GotoBLAS2 1.13-alt3

* Thu Apr 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt2
- Built with lapack-goto instead of lapack

* Sat Mar 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt1
- Version 3.6.0

* Fri Feb 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt7
- Rebuilt with metis 4.0.1-alt9

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt6
- Rebuilt for debuginfo

* Tue Oct 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt5
- Rebuilt for soname set-versions

* Fri Oct 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt4
- Fixed underlinking of libraries

* Tue Jul 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt3
- Rebuilt with reformed Metis

* Mon Dec 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt2
- Rebuilt with texlive instead of tetex

* Fri Aug 28 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1
- Version 3.4.0
- Added:
    + pkg-config files (ALT #21192)
    + shared libraries
    + examples

* Tue Nov 18 2008 Paul Wolneykien <manowar@altlinux.ru> 3.1-alt3
- Generate position independent code (PIC).

* Sat Nov 01 2008 Paul Wolneykien <manowar@altlinux.ru> 3.1-alt2
- Architacture independent documentation package.

* Mon Sep 08 2008 Paul Wolneykien <manowar@altlinux.ru> 3.1-alt1
- Initial release for ALTLinux.
