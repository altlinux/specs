%define __GIVARO_USE_OPENMP 0
%define soname 9

%def_disable static
%def_without doc

%if_enabled static
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%endif

Name: givaro
Version: 4.2.0
Release: alt5.gitfc6cac7
Summary: C++ library for arithmetic and algebraic computations

License: CECILL-B
Group: System/Libraries
Url: https://github.com/linbox-team/givaro

Source: https://github.com/linbox-team/%name/releases/download/v%version/%name-%version.tar.gz

%if_with doc
BuildRequires: doxygen texlive-dist
%endif
BuildRequires: gcc-c++
BuildRequires: ghostscript-utils ghostscript
BuildRequires: libgmp-devel libgmpxx-devel

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
%autopatch -p1

# Regenerate configure after monkeying with configure.ac
%autoreconf

%build
%configure \
%if_disabled static
  --disable-static \
%endif
  --enable-shared \
%if_with doc
  --enable-doc \
  --with-docdir="%_docdir/%name-devel" \
%else
  --disable-doc \
%endif
  --disable-simd \
#
chmod a+x givaro-config

%make_build

%install
%makeinstall_std

# We don't want libtool archives
rm -f %buildroot%_libdir/lib%name.la

# We don't want these files with the doxygen-generated files
rm -f %buildroot%_docdir/%name-devel/givaro-html/{AUTHORS,COPYING,INSTALL}

%check
export LD_LIBRARY_PATH=$PWD/src/.libs
make check

%files -n lib%name%soname
%doc AUTHORS ChangeLog README.md
%doc COPYING COPYRIGHT Licence_CeCILL-B_V1-en.txt Licence_CeCILL-B_V1-fr.txt
%_libdir/lib%name.so.%{soname}*

%files -n lib%name-devel
%if_with doc
%_docdir/%name-devel/
%endif
%_bindir/%name-config
%dir %_datadir/%name/
%_datadir/%name/%name-makefile
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
* Thu Aug 22 2024 Leontiy Volodin <lvol@altlinux.org> 4.2.0-alt5.gitfc6cac7
- Built without docs because segmentation fault.

* Mon Aug 12 2024 Leontiy Volodin <lvol@altlinux.org> 4.2.0-alt4.gitfc6cac7
- Update to commit fc6cac7820539c900dde332326c71461ba7b910b
  (v4.2.0.0.84.gfc6c).

* Thu Jun 22 2023 Leontiy Volodin <lvol@altlinux.org> 4.2.0-alt3
- Fixed build with gcc13.

* Tue Jul 19 2022 Leontiy Volodin <lvol@altlinux.org> 4.2.0-alt2
- Fixed build with new linbox.

* Wed Jun 22 2022 Leontiy Volodin <lvol@altlinux.org> 4.2.0-alt1
- New version (4.2.0).

* Wed Oct 20 2021 Leontiy Volodin <lvol@altlinux.org> 4.1.1-alt1
- Initial build for ALT Sisyphus (thanks fedora for the spec).
- Built as require for sagemath.
- Applied patches from fedora and debian.
