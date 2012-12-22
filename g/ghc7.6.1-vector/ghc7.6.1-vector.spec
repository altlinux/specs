%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name vector
%define f_pkg_name vector
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.10.0.1
Release: alt2
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://code.haskell.org/vector
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Efficient Arrays



# Automatically added by buildreq on Sat Dec 22 2012 (-bb)
# optimized out: elfutils ghc7.4.2-common ghc7.6.1 ghc7.6.1-common libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.6.1-doc ghc7.6.1-primitive

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

There is also a (draft) tutorial on common uses of vector.

* <http://haskell.org/haskellwiki/Numeric_Haskell:_A_Vector_Tutorial>

Please use the project trac to submit bug reports and feature requests.

* <http://trac.haskell.org/vector>

Changes in version 0.10.0.1

* Require @primitive@ to include workaround for a GHC array copying bug

Changes in version 0.10

* @NFData@ instances

* More efficient block fills

* Safe Haskell support removed

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

%changelog
* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.10.0.1-alt2
- rebuild

* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.10.0.1-alt1
- Spec created by cabal2rpm 0.20_08
