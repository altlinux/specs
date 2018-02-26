%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define h_pkg_name transformers
%define f_pkg_name transformers
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.2.2.0
Release: alt2.1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
URL: ???
Source: %name-%version.tar
Summary: Concrete functor and monad transformers
BuildRequires: ghc 
BuildRequires(pre): rpm-build-haskell



%description
Haskell 98 part of a monad transformer library, inspired by the paper
\"Functional Programming with Overloading and Higher-Order Polymorphism\",
by Mark P Jones, in /Advanced School of Functional Programming/, 1995
(<http://web.cecs.pdx.edu/~mpj/pubs/springschool.html>).

This part contains the monad transformer class, the concrete monad
transformers, operations and liftings. It can be used on its own in Haskell
98 code, or with the monad classes in the @monads-fd@ or @monads-tf@
packages, which automatically lift operations introduced by monad
transformers through other transformers.

%prep
%setup

%build
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

cd %buildroot%_datadir/doc/%name-%version
rm -rf doc LICENSE examples

%files -f %name-files.nonprof
%hs_pkgconfdir/%f_pkg_name-%version.conf
%doc dist/doc/html
#%%doc LICENSE examples

%changelog
* Sat Aug 13 2011 Denis Smirnov <mithraen@altlinux.ru> 0.2.2.0-alt2.1
- rebuild with shared objects support

* Tue Aug 09 2011 Denis Smirnov <mithraen@altlinux.ru> 0.2.2.0-alt2
- rebuild

* Wed Dec 08 2010 Denis Smirnov <mithraen@altlinux.ru> 0.2.2.0-alt1
- Spec created by cabal2rpm 0.20_08
