%define ghc_version 7.4.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name alex
%define f_pkg_name alex
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 3.0.1
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
URL: http://www.haskell.org/alex/
Source: %name-%version.tar
Summary: Alex is a tool for generating lexical analysers in Haskell



# Automatically added by buildreq on Mon Mar 19 2012 (-bb)
# optimized out: elfutils ghc7.4.1 ghc7.4.1-common ghc7.4.1-random libgmp-devel pkg-config
BuildRequires: ghc7.4.1-quickcheck

%description
Alex is a tool for generating lexical analysers in Haskell

%prep
%setup

%build
%hs_configure2
%hs_build

%install
runghc Setup copy --destdir=%buildroot

%files
%_bindir/alex
%_datadir/%name-%version

%changelog
* Sat Mar 17 2012 Denis Smirnov <mithraen@altlinux.ru> 3.0.1-alt1
- Spec created by cabal2rpm 0.20_08
