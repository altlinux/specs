%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name pureMD5
%define f_pkg_name puremd5
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 2.1.2.1
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://hackage.haskell.org/package/pureMD5
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: A Haskell-only implementation of the MD5 digest (hash) algorithm.



# Automatically added by buildreq on Sat Dec 22 2012 (-bb)
# optimized out: elfutils ghc7.6.1 ghc7.6.1-cereal ghc7.6.1-common ghc7.6.1-entropy ghc7.6.1-largeword ghc7.6.1-tagged libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.6.1-alex ghc7.6.1-c2hs ghc7.6.1-cpphs ghc7.6.1-crypto-api ghc7.6.1-doc ghc7.6.1-happy ghc7.6.1-hscolour

%description
A Haskell-only implementation of the MD5 digest (hash) algorithm. This now
supports the crypto-api class interface.

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
* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 2.1.2.1-alt1
- Spec created by cabal2rpm 0.20_08
