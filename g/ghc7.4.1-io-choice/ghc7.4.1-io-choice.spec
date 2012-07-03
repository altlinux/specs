%define ghc_version 7.4.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name io-choice
%define f_pkg_name io-choice
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.0.1
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
URL: ???
Source: %name-%version.tar
Summary: Choice for IO and lifted IO



# Automatically added by buildreq on Mon Mar 19 2012 (-bb)
# optimized out: elfutils ghc7.4.1 ghc7.4.1-base-unicode-symbols ghc7.4.1-common ghc7.4.1-monad-control ghc7.4.1-transformers ghc7.4.1-transformers-base libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.4.1-alex ghc7.4.1-lifted-base

%description
Choice for IO and lifted IO

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
* Sat Mar 17 2012 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1
- Spec created by cabal2rpm 0.20_08
