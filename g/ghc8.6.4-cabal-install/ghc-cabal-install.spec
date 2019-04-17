%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name cabal-install
%define f_pkg_name cabal-install
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 2.4.0.0
Release: alt1
License: BSD3
Packager: Evgeny Sinelnikov <sin@altlinux.org>
Group: Development/Haskell
Url: http://www.haskell.org/cabal/
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: The command-line interface for Cabal and Hackage.

BuildPreReq: haskell(abi) = %ghc_version
BuildPreReq: ghc%ghc_version-zlib
BuildPreReq: ghc%ghc_version-zip-archive
BuildPreReq: ghc%ghc_version-tar
BuildPreReq: ghc%ghc_version-resolv
BuildPreReq: ghc%ghc_version-random
BuildPreReq: ghc%ghc_version-network
BuildPreReq: ghc%ghc_version-network-uri
BuildPreReq: ghc%ghc_version-http
BuildPreReq: ghc%ghc_version-hashable
BuildPreReq: ghc%ghc_version-hackage-security
BuildPreReq: ghc%ghc_version-edit-distance
BuildPreReq: ghc%ghc_version-echo
BuildPreReq: ghc%ghc_version-async
BuildPreReq: zlib-devel

Conflicts: ghc7.6.1-cabal-install
Provides: cabal-install = %EVR
Conflicts: cabal-install < %EVR


%description
The \'cabal\' command-line program simplifies the process of managing
Haskell software by automating the fetching, configuration, compilation and
installation of Haskell libraries and programs.

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
%_man1dir/cabal.*

%changelog
* Wed Apr 17 2019 Evgeny Sinelnikov <sin@altlinux.org> 2.4.0.0-alt1
- Spec created by cabal2rpm 0.20_11
