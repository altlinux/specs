%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name hackage-security
%define f_pkg_name hackage-security
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.5.3.0
Release: alt1
License: BSD3
Packager: Evgeny Sinelnikov <sin@altlinux.org>
Group: Development/Haskell
Url: https://github.com/haskell/hackage-security
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: hackage-security

BuildPreReq: haskell(abi) = %ghc_version
BuildPreReq: ghc%ghc_version-zlib
BuildPreReq: ghc%ghc_version-tar
BuildPreReq: ghc%ghc_version-ed25519
BuildPreReq: ghc%ghc_version-cryptohash-sha256
BuildPreReq: ghc%ghc_version-base16-bytestring
BuildPreReq: ghc%ghc_version-base64-bytestring
BuildPreReq: ghc%ghc_version-network
BuildPreReq: ghc%ghc_version-network-uri
BuildPreReq: zlib-devel


%description
The hackage security library provides both server and client utilities for
securing the Hackage package server (<http://hackage.haskell.org/>). It is
based on The Update Framework (<http://theupdateframework.com/>), a set of
recommendations developed by security researchers at various universities
in the US as well as developers on the Tor project
(<https://www.torproject.org/>).

The current implementation supports only index signing, thereby enabling
untrusted mirrors. It does not yet provide facilities for author package
signing.

The library has two main entry points: "Hackage.Security.Client" is the
main entry point for clients (the typical example being @cabal@), and
"Hackage.Security.Server" is the main entry point for servers (the typical
example being @hackage-server@).

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
* Wed Apr 17 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.5.3.0-alt1
- Spec created by cabal2rpm 0.20_11
