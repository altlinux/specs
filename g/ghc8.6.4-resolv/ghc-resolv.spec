%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name resolv
%define f_pkg_name resolv
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.1.1.2
Release: alt1
License: GPL-2
Packager: Evgeny Sinelnikov <sin@altlinux.org>
Group: Development/Haskell
Url: http://hackage.haskell.org/package/resolv
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Domain Name Service (DNS) lookup via the libresolv standard library routines

BuildPreReq: haskell(abi) = %ghc_version
BuildPreReq: ghc%ghc_version-base16-bytestring


%description
This package implements an API for accessing the Domain Name Service (DNS)
resolver service via the standard libresolv system library (whose API is often
available directly via the standard libc C library) on Unix systems.

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
* Wed Apr 17 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.1.1.2-alt1
- Spec created by cabal2rpm 0.20_11
