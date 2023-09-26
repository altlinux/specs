%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name network
%define f_pkg_name network
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 2.8.0.0
Release: alt1.1
License: BSD3
Packager: Evgeny Sinelnikov <sin@altlinux.org>
Group: Development/Haskell
Url: https://github.com/haskell/network
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Low-level networking interface

BuildPreReq: haskell(abi) = %ghc_version


%description
This package provides a low-level networking interface.

In network-2.6 the @Network.URI@ module was split off into its own package,
network-uri-2.6. If you're using the @Network.URI@ module you can
automatically get it from the right package by adding this to your .cabal
file:

> library > build-depends: network-uri-flag

%prep
%setup
%patch -p1

%build
%autoreconf
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

%files -f %name-files.all

%changelog
* Tue Sep 26 2023 Ivan A. Melnikov <iv@altlinux.org> 2.8.0.0-alt1.1
- NMU: spec: call %%autoreconf (fixes build on loongarch64)

* Wed Apr 17 2019 Evgeny Sinelnikov <sin@altlinux.org> 2.8.0.0-alt1
- Spec created by cabal2rpm 0.20_11
