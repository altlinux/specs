%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name mtl
%define f_pkg_name mtl
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 2.1.2
Release: alt2
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://github.com/ekmett/mtl
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Monad classes, using functional dependencies



# Automatically added by buildreq on Sat Dec 22 2012 (-bb)
# optimized out: elfutils ghc7.4.2-common ghc7.6.1 ghc7.6.1-common libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.6.1-cpphs ghc7.6.1-doc ghc7.6.1-hscolour ghc7.6.1-transformers

%description
Monad classes using functional dependencies, with instances for various
monad transformers, inspired by the paper /Functional Programming with
Overloading and Higher-Order Polymorphism/, by Mark P Jones, in /Advanced
School of Functional Programming/, 1995
(<http://web.cecs.pdx.edu/~mpj/pubs/springschool.html>).

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
* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 2.1.2-alt2
- rebuild

* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 2.1.2-alt1
- Spec created by cabal2rpm 0.20_08
