%define ghc_version 7.4.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name happy
%define f_pkg_name happy
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.18.9
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
URL: http://www.haskell.org/happy/
Source: %name-%version.tar
Summary: Happy is a parser generator for Haskell



# Automatically added by buildreq on Tue Mar 20 2012 (-bb)
# optimized out: elfutils ghc7.4.1 ghc7.4.1-common ghc7.4.1-transformers libgmp-devel pkg-config python-base
BuildRequires: ghc7.4.1-alex ghc7.4.1-mtl

%description
Happy is a parser generator for Haskell

%prep
%setup

%build
%hs_configure2
%hs_build

%install
runghc Setup copy --destdir=%buildroot
rm -f %buildroot%_datadir/doc/%name-%version/LICENSE

%files
%_bindir/happy
%_datadir/%name-%version

%changelog
* Tue Mar 20 2012 Denis Smirnov <mithraen@altlinux.ru> 1.18.9-alt1
- Spec created by cabal2rpm 0.20_08
