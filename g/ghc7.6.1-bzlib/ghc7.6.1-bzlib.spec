%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name bzlib
%define f_pkg_name bzlib
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.5.0.4
Release: alt2
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://hackage.haskell.org/package/bzlib
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Compression and decompression in the bzip2 format



# Automatically added by buildreq on Sat Dec 22 2012 (-bb)
# optimized out: elfutils ghc7.4.2-common ghc7.6.1 ghc7.6.1-common libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: bzlib-devel ghc7.6.1-cpphs ghc7.6.1-doc ghc7.6.1-hscolour

%description
This package provides a pure interface for compressing and decompressing
streams of data represented as lazy 'ByteString's. It uses the bz2 C
library so it has high performance.

It provides a convenient high level API suitable for most tasks and for the
few cases where more control is needed it provides access to the full bzip2
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
* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.5.0.4-alt2
- rebuild

* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.5.0.4-alt1
- Spec created by cabal2rpm 0.20_08
