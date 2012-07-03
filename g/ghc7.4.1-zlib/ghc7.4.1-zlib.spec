%define ghc_version 7.4.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name zlib
%define f_pkg_name zlib
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.5.3.3
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
URL: ???
Source: %name-%version.tar
Summary: Compression and decompression in the gzip and zlib formats



# Automatically added by buildreq on Sat Mar 17 2012 (-bb)
# optimized out: elfutils ghc7.4.1-common ghc7.4.1-prof libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.4.1 zlib-devel

%description
This package provides a pure interface for compressing and decompressing
streams of data represented as lazy 'ByteString's. It uses the zlib C
library so it has high performance. It supports the \"zlib\", \"gzip\" and
\"raw\" compression formats.

It provides a convenient high level API suitable for most tasks and for the
few cases where more control is needed it provides access to the full zlib
feature set.

%prep
%setup

%build
%hs_configure2 -v
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
* Sat Mar 17 2012 Denis Smirnov <mithraen@altlinux.ru> 0.5.3.3-alt1
- Spec created by cabal2rpm 0.20_08
