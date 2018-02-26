Name: blas
Packager: Paul Wolneykien <manowar@altlinux.ru>
Version: 3.9.2
Release: alt1
Group: System/Libraries
URL: http://www.netlib.org/blas/
License: Public Domain
Summary: Basic Linear Algebra Reference implementation

Source: %name-%version.tar
Patch0: make-libdir.patch
Patch1: x86-32-do-not-optimize.patch

BuildRequires: gcc-fortran texlive-latex-recommended

%description
Basic Linear Algebra Reference implementation.

BLAS (Basic Linear Algebra Subroutines) is a set of efficient
routines for most of the basic vector and matrix operations.
They are widely used as the basis for other high quality linear
algebra software, for example lapack and linpack.  This
implementation is the Fortran 77 reference implementation found
at netlib.

%package -n lib%{name}3gf
Group: System/Libraries
Summary: Basic Linear Algebra Reference implementation, shared library

%description -n lib%{name}3gf
Basic Linear Algebra Reference implementation, shared library.

BLAS (Basic Linear Algebra Subroutines) is a set of efficient
routines for most of the basic vector and matrix operations.
They are widely used as the basis for other high quality linear
algebra software, for example lapack and linpack.  This
implementation is the Fortran 77 reference implementation found
at netlib.

This package contains a shared version of the library.

%package -n lib%name-devel
Group: Development/Other
Summary: Basic Linear Algebra Subroutines 3, development files
Requires: lib%{name}3gf = %version-%release

%description -n lib%name-devel
Basic Linear Algebra Subroutines 3, development files.

BLAS (Basic Linear Algebra Subroutines) is a set of efficient
routines for most of the basic vector and matrix operations.
They are widely used as the basis for other high quality linear
algebra software, for example lapack and linpack.  This
implementation is the Fortran 77 reference implementation found
at netlib.

This package contains the set of files for development with BLAS.

%package -n lib%name-test
Group: Development/Other
Summary: Basic Linear Algebra Subroutines 3, testing programs
Requires: lib%{name}3gf = %version-%release

%description -n lib%name-test
Basic Linear Algebra Subroutines 3, testing programs.

BLAS (Basic Linear Algebra Subroutines) is a set of efficient
routines for most of the basic vector and matrix operations.
They are widely used as the basis for other high quality linear
algebra software, for example lapack and linpack.  This
implementation is the Fortran 77 reference implementation found
at netlib.

This package contains a set of programs which test the integrity
of an installed blas-compatible shared library.  These programs
may therefore be used to test the libraries provided by the
blas package as well as those provided by the atlas packages.
The programs are dynamically linked -- one can explicitly select
a library to test by setting the LD_LIBRARY_PATH or LD_PRELOAD
environment variables.  Likewise, one can display the library
selected using the ldd program in an identical environment.

%package -n lib%name-doc
Group: Documentation
Summary: Basic Linear Algebra Subroutines 3, documentation
BuildArch: noarch

%description -n lib%name-doc
Basic Linear Algebra Subroutines 3, documentation.

BLAS (Basic Linear Algebra Subroutines) is a set of efficient
routines for most of the basic vector and matrix operations.
They are widely used as the basis for other high quality linear
algebra software, for example lapack and linpack.  This
implementation is the Fortran 77 reference implementation found
at netlib.

This package contains some supporting documentation.

%prep
%setup
%patch0 -p1
%patch1 -p1
%make -f debian/rules debian/patch_applied
sed -i -e 's/\$(shell[[:space:]]\+dpkg.*arch.*)/%_arch/g' debian/rules
sed -i -e 's/\$(shell[[:space:]]\+dpkg.*arch.*)/%_arch/g' cblas/testing/Makefile
sed -i -e 's/i386/i586/g' debian/rules
sed -i -e 's/i386/i586/g' cblas/testing/Makefile

%build
%make -f debian/rules build
%make -f debian/rules debian/patched-docs/cinterface.pdf
%make -f debian/rules debian/test_results
%make -f debian/rules `echo man/manl/* | sed -e 's/\.l/.3/g'`

%install
install -d -m0755 %buildroot

# Shared libraries
install -d -m0755 %buildroot%_libdir
install -m0644 -t %buildroot%_libdir *.so.3gf.[0-9]
cp -a *.so *.so.3gf %buildroot%_libdir/

# Development files
install -d -m0755 %buildroot%_includedir/c%name
install -m0644 -t %buildroot%_includedir/c%name cblas/src/*.h

# Test programs
install -d -m0755 %buildroot%_bindir
install -m0755 -t %buildroot%_bindir $(find test/ cblas/testing -type f -perm /0100 | tr '\n' ' ')

# Manual pages
install -d -m0755 %buildroot%_man3dir
install -m0644 -t %buildroot%_man3dir man/man*/*.3

%check
[ -f debian/test_results ] && grep -vi 'FAIL' debian/test_results

%files -n lib%{name}3gf
%_libdir/*.so.*
%doc debian/changelog

%files -n lib%name-devel
%_libdir/*.so
%_includedir/c%name

%files -n lib%name-test
%_bindir/*
%_man3dir/*.3*

%files -n lib%name-doc
%doc doc/faq.html
%doc debian/patched-docs/cinterface.pdf

%changelog
* Tue Jan 17 2012 Paul Wolneykien <manowar@altlinux.ru> 3.9.2-alt1
- Initial build for ALT Linux. Based on the Ubuntu package.
