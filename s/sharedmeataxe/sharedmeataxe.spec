%define soname 0

Name: sharedmeataxe
Version: 1.0
Release: alt1

Summary: Matrix representations over finite fields

License: GPL-2.0+
Group: Sciences/Mathematics
Url: https://users.fmi.uni-jena.de/~king/SharedMeatAxe/
# Watch https://github.com/simon-king-jena/SharedMeatAxe

Source: http://users.minet.uni-jena.de/~king/SharedMeatAxe/shared_meataxe-%version.tar.gz

# BuildPreReq: help2man
BuildRequires: gcc doxygen texlive-dist

%description
The SharedMeatAxe is a dynamic (shared) library together with a set of
programs for working with matrices over finite fields.  It is a fork of
the C MeatAxe, and differs from it mainly by the implementation of
asymptotically fast matrix multiplication and by providing a dynamic
(as opposed to static) library and an autotoolized build system.

MeatAxe's primary purpose is the calculation of modular character
tables, although it can be used for other purposes, such as
investigating subgroup structure, module structure etc.  Indeed, there
is a set of programs to compute automatically the submodule lattice of
a given module.

The primitive objects are of two types: matrices and permutations.
Permutation objects can be handled, but not as smoothly as you might
expect.  For example, it is hoped that programs such as split (zsp) and
multiply (zmu) will be able to work with mixed types, but at present
ZSP is restricted to matrices only, and ZMU can multiply a matrix by a
permutation, but not vice versa.

%package -n libmtx%soname
Summary: Library of matrix representations over finite fields
Group: System/Libraries

%description -n libmtx%soname
This package contains the SharedMeatAxe library, which provides
functions for working with matrix representations over finite fields.
Permutation representations are supported to some extent, too.

%package -n libmtx-devel
Summary: Header files and libraries for SharedMeatAxe development
Group: Development/C

%description -n libmtx-devel
This package contains the header files and library links for building
applications that use the SharedMeatAxe library.

%package doc
Summary: API documentation for %name
Group: Documentation
BuildArch: noarch

%description doc
API documentation for %name.

%prep
%setup -n shared_meataxe-%version

%build
%configure --disable-silent-rules

# Get rid of undesirable hardcoded rpaths.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -i libtool

# Build the library and programs
%make_build

# Build the documentation
mkdir html
DOCDIR=$PWD/html SRCDIR=$PWD doxygen etc/Doxyfile

%install
%makeinstall_std

# We do not want the libtool archives
rm -f %buildroot%_libdir/*.la

%check
LD_LIBRARY_PATH=$PWD/src/.libs make check

%files
%doc NEWS
%_bindir/*

%files -n libmtx%soname
%doc AUTHORS README
%doc COPYING
%_libdir/libmtx.so.%{soname}*

%files -n libmtx-devel
%doc ChangeLog
%_includedir/meataxe.h
%_libdir/libmtx.so

%files doc
%doc html

%changelog
* Mon Nov 22 2021 Leontiy Volodin <lvol@altlinux.org> 1.0-alt1
- Initial build for ALT Sisyphus (thanks fedora and archlinux for the spec).
- Built as require for sagemath.
