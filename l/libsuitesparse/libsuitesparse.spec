Name: libsuitesparse
Version: 3.6.1
Release: alt2

Summary: Shared libraries for sparse matrix calculations
Packager: Paul Wolneykien <manowar@altlinux.ru>
License: LGPL, GPL
Group: Sciences/Mathematics
Url: http://www.cise.ufl.edu/research/sparse/SuiteSparse/

Source: SuiteSparse-%version.tar.gz
Source1: cholmod.pc
Source2: prepare_versions.sh
Source3: umfpack.pc

BuildPreReq: libmetis0-devel gcc-c++

# Automatically added by buildreq on Sun Sep 14 2008
BuildRequires: gcc-fortran liblapack-goto-devel texlive-latex-base

%package devel
Summary: Development files of SuiteSparse
Group: Development/Other
Requires: %name = %version-%release
Conflicts: %name-devel < %version-%release
Obsoletes: %name-devel < %version-%release
Conflicts: libumfpack-devel UFconfig

%package devel-static
Summary: Static libraries of SuiteSparse
Group: Development/Other
Requires: %name-devel = %version-%release
Conflicts: %name-devel < %version-%release

%package devel-doc
Summary: Documentation for %name
Group: Sciences/Mathematics
BuildArch: noarch

%package examples
Summary: Examples for %name
Group: Sciences/Mathematics
Requires: %name = %version-%release

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

%prep
%setup
install -m644 %SOURCE1 %SOURCE3 .
install -m755 %SOURCE2 .

%build
./prepare_versions.sh

%make TOPDIR=$PWD
%make doc

%install
%makeinstall NAME=%name VERSION=%version

install -d %buildroot%_pkgconfigdir
install -m644 *.pc %buildroot%_pkgconfigdir

for i in $(find ./ -name Demo); do
	rm -f $(find $i -name '*.m')
	install -d %buildroot%_libdir/%name/demos/$i
	cp -fR $i/* %buildroot%_libdir/%name/demos/$i/
done

%files
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*

#files devel-static
#_libdir/*.a

%files devel-doc
%_docdir/%name-%version

%files examples
%dir %_libdir/%name
%_libdir/%name/demos

%changelog
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
