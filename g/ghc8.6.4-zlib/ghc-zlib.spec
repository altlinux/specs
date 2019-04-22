%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name zlib
%define f_pkg_name zlib
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.6.2
Release: alt1
License: BSD3
Packager: Evgeny Sinelnikov <sin@altlinux.org>
Group: Development/Haskell
Url: http://hackage.haskell.org/package/zlib
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Compression and decompression in the gzip and zlib formats

BuildPreReq: haskell(abi) = %ghc_version
BuildPreReq: zlib-devel


%description
This package provides a pure interface for compressing and decompressing
streams of data represented as lazy 'ByteString's. It uses the
<https://en.wikipedia.org/wiki/Zlib zlib C library> so it has high
performance. It supports the \"zlib\", \"gzip\" and \"raw\" compression
formats.

It provides a convenient high level API suitable for most tasks and for the
few cases where more control is needed it provides access to the full zlib
feature set.

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
* Wed Apr 17 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.6.2-alt1
- Spec created by cabal2rpm 0.20_11
