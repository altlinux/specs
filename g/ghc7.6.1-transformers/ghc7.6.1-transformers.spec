%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name transformers
%define f_pkg_name transformers
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.3.0.0
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://hackage.haskell.org/package/transformers
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Concrete functor and monad transformers



# Automatically added by buildreq on Sat Dec 22 2012 (-bb)
# optimized out: elfutils ghc7.4.2-common ghc7.6.1-common libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.6.1 ghc7.6.1-doc

%description
A portable library of functor and monad transformers, inspired by the paper
\"Functional Programming with Overloading and Higher-Order Polymorphism\",
by Mark P Jones, in /Advanced School of Functional Programming/, 1995
(<http://web.cecs.pdx.edu/~mpj/pubs/springschool.html>).

This package contains:

* the monad transformer class (in "Control.Monad.Trans.Class")

* concrete functor and monad transformers, each with associated operations
and functions to lift operations associated with other transformers.

It can be used on its own in portable Haskell code, or with the monad
classes in the @mtl@ or @monads-tf@ packages, which automatically lift
operations introduced by monad transformers through other transformers.

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
* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.3.0.0-alt1
- Spec created by cabal2rpm 0.20_08
