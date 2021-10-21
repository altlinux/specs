%define soname 9

%def_enable static

%if_enabled static
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%endif

Name: givaro
Version: 4.1.1
Release: alt1
Summary: C++ library for arithmetic and algebraic computations

License: CECILL-B
Group: Development/C
Url: https://casys.gricad-pages.univ-grenoble-alpes.fr/givaro/

Source: https://github.com/linbox-team/%name/releases/download/v%version/%name-%version.tar.gz
# Fix a memory leak.  The original code creates a temporary object, then does
# not dispose of it.  This change prevents creation of the temporary.
# https://github.com/linbox-team/givaro/pull/134
Patch: %name-mem-leak.patch
# Sagemath patch to fix issues with long long and flint
Patch1: %name-26932_recintvsflint_longlong.patch
# Debian's patch
Patch2: givaro-makefile.patch

BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: ghostscript-utils ghostscript
BuildRequires: libgmp-devel libgmpxx-devel
BuildRequires: texlive-dist

%description
Givaro is a C++ library for arithmetic and algebraic computations.
Its main features are implementations of the basic arithmetic of many
mathematical entities: Primes fields, Extensions Fields, Finite Fields,
Finite Rings, Polynomials, Algebraic numbers, Arbitrary precision
integers and rationals (C++ wrappers over gmp) It also provides
data-structures and templated classes for the manipulation of basic
algebraic objects, such as vectors, matrices (dense, sparse, structured),
univariate polynomials (and therefore recursive multivariate).

%package -n lib%name%soname
Group: Development/C
Summary: %summary

%description -n lib%name%soname
Givaro is a C++ library for arithmetic and algebraic computations.
Its main features are implementations of the basic arithmetic of many
mathematical entities: Primes fields, Extensions Fields, Finite Fields,
Finite Rings, Polynomials, Algebraic numbers, Arbitrary precision
integers and rationals (C++ wrappers over gmp) It also provides
data-structures and templated classes for the manipulation of basic
algebraic objects, such as vectors, matrices (dense, sparse, structured),
univariate polynomials (and therefore recursive multivariate).

%package -n lib%name-devel
Summary: Files useful for %name development
Group: Development/C
Provides: bundled(jquery)

%description -n lib%name-devel
The libraries and header files for using %name for development.

%if_enabled static
%package -n lib%name-devel-static
Summary: Files used for static linking with %name
Group: Development/C

%description -n lib%name-devel-static
The static libraries for using %name for development.
%endif

%prep
%setup
%patch -p1
%patch1 -p1
%patch2 -p1

# Remove parts of the configure script that select non-default architectures
# and ABIs.
subst '/INSTR_SET/,/fabi-version/d' configure.ac

# Regenerate configure after monkeying with configure.ac
%autoreconf

%build
%ifarch %ix86
# Excess precision leads to test failures
%global optflags %optflags -ffloat-store
%endif
%ifarch s390x
%global optflags %optflags -ffp-contract=off
%endif

%configure \
    --enable-doc \
    --docdir=%_docdir/%name-devel \
#
chmod a+x givaro-config

# Get rid of undesirable hardcoded rpaths, and workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build

%install
%makeinstall_std

# We don't want libtool archives
rm -f %buildroot%_libdir/lib%name.la

# Documentation is installed in the wrong place
mkdir -p %buildroot%_docdir
mv %buildroot%prefix/docs %buildroot%_docdir/%name-devel

# We don't want these files with the doxygen-generated files
rm -f %buildroot%_docdir/%name-devel/givaro-html/{AUTHORS,COPYING,INSTALL}

%if_disabled static
rm -f %buildroot%_libdir/lib%name.a
%endif

%check
export LD_LIBRARY_PATH=$PWD/src/.libs
make check

%files -n lib%name%soname
%doc AUTHORS ChangeLog README.md
%doc COPYING COPYRIGHT Licence_CeCILL-B_V1-en.txt Licence_CeCILL-B_V1-fr.txt
%_libdir/lib%name.so.%{soname}*

%files -n lib%name-devel
%_docdir/%name-devel/
%_bindir/%name-config
%_bindir/%name-makefile
%_includedir/%name/
%_includedir/gmp++/
%_includedir/recint/
%_includedir/%name-config.h
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc

%if_enabled static
%files -n lib%name-devel-static
%_libdir/lib%name.a
%endif

%changelog
* Wed Oct 20 2021 Leontiy Volodin <lvol@altlinux.org> 4.1.1-alt1
- Initial build for ALT Sisyphus (thanks fedora for the spec).
- Built as require for sagemath.
- Applied patches from fedora and debian.
