%define ghc_version 7.4.2
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name vector
%define f_pkg_name vector
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.9.1
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://code.haskell.org/vector
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Efficient Arrays



# Automatically added by buildreq on Sun Jul 01 2012 (-bb)
# optimized out: elfutils ghc7.4.2 ghc7.4.2-common libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.4.2-alex ghc7.4.2-cpphs ghc7.4.2-doc ghc7.4.2-happy ghc7.4.2-primitive

%description


An efficient implementation of Int-indexed arrays (both mutable and
immutable), with a powerful loop optimisation framework .

It is structured as follows:

["Data.Vector"] Boxed vectors of arbitrary types.

["Data.Vector.Unboxed"] Unboxed vectors with an adaptive representation
based on data type families.

["Data.Vector.Storable"] Unboxed vectors of 'Storable' types.

["Data.Vector.Primitive"] Unboxed vectors of primitive types as defined by
the @primitive@ package. "Data.Vector.Unboxed" is more flexible at no
performance cost.

["Data.Vector.Generic"] Generic interface to the vector types.

Each module has a @Safe@ version with is marked as @Trustworthy@ (see
<http://hackage.haskell.org/trac/ghc/wiki/SafeHaskell>).

There is also a (draft) tutorial on common uses of vector.

* <http://haskell.org/haskellwiki/Numeric_Haskell:_A_Vector_Tutorial>

Please use the project trac to submit bug reports and feature requests.

* <http://trac.haskell.org/vector>

Changes in version 0.9.1

* New functions: @unsafeFromForeignPtr0@ and @unsafeToForeignPtr0@

* Small performance improvements

* Fixes for GHC 7.4

Changes in version 0.9

* 'MonadPlus' instance for boxed vectors

* Export more @construct@ and @constructN@ from @Safe@ modules

* Require @primitive-0.4.0.1@

Changes in version 0.8

* New functions: @constructN@, @constructrN@

* Support for GHC 7.2 array copying primitives

* New fixity for @(!)@

* Safe Haskell support (contributed by David Terei)

* 'Functor', 'Monad', 'Applicative', 'Alternative', 'Foldable' and
'Traversable' instances for boxed vectors (/WARNING: they tend to be slow
and are only provided for completeness/)

* 'Show' instances for immutable vectors follow containers conventions

* 'Read' instances for all immutable vector types

* Performance improvements

%prep
%setup
%patch -p1

%build
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

%files -f %name-files.all
%hs_pkgconfdir/%f_pkg_name-%version.conf
%_docdir/%name-%version

%changelog
* Sat Jun 30 2012 Denis Smirnov <mithraen@altlinux.ru> 0.9.1-alt1
- Spec created by cabal2rpm 0.20_08
