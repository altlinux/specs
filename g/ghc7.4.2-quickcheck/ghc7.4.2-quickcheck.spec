%define ghc_version 7.4.2
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name QuickCheck
%define f_pkg_name quickcheck
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 2.5
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://code.haskell.org/QuickCheck
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Automatic testing of Haskell programs



# Automatically added by buildreq on Sat Jun 30 2012 (-bb)
# optimized out: elfutils ghc7.4.2 ghc7.4.2-common libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.4.2-doc ghc7.4.2-random

%description
QuickCheck is a library for random testing of program properties.

The programmer provides a specification of the program, in the form of
properties which functions should satisfy, and QuickCheck then tests that
the properties hold in a large number of randomly generated cases.

Specifications are expressed in Haskell, using combinators defined in the
QuickCheck library. QuickCheck provides combinators to define properties,
observe the distribution of test data, and define test data generators.

%prep
%setup
%patch -p1

%build
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

%files -f %name-files.nonprof
%hs_pkgconfdir/%f_pkg_name-%version.conf
%_docdir/%name-%version

%changelog
* Sat Jun 30 2012 Denis Smirnov <mithraen@altlinux.ru> 2.5-alt1
- Spec created by cabal2rpm 0.20_08
