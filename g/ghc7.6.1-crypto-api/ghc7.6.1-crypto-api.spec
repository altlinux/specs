%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name crypto-api
%define f_pkg_name crypto-api
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.10.2
Release: alt2
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://trac.haskell.org/crypto-api/wiki
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: A generic interface for cryptographic operations



# Automatically added by buildreq on Sat Dec 22 2012 (-bb)
# optimized out: elfutils ghc7.4.2-common ghc7.6.1 ghc7.6.1-common libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.6.1-cereal ghc7.6.1-cpphs ghc7.6.1-doc ghc7.6.1-entropy ghc7.6.1-hscolour ghc7.6.1-largeword ghc7.6.1-tagged

%description
A generic interface for cryptographic operations (hashes, ciphers,
randomness).

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
* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.10.2-alt2
- rebuild

* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.10.2-alt1
- Spec created by cabal2rpm 0.20_08
