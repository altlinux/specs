%define ghc_version 7.4.2
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name cryptohash
%define f_pkg_name cryptohash
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.7.5
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://github.com/vincenthz/hs-cryptohash
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: collection of crypto hashes, fast, pure and practical



# Automatically added by buildreq on Sun Jul 01 2012 (-bb)
# optimized out: elfutils ghc7.4.2 ghc7.4.2-cereal ghc7.4.2-common ghc7.4.2-entropy ghc7.4.2-largeword ghc7.4.2-tagged libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.4.2-alex ghc7.4.2-cpphs ghc7.4.2-crypto-api ghc7.4.2-doc ghc7.4.2-happy

%description
A collection of crypto hashes, with a practical incremental and one-pass,
pure APIs, with performance close to the fastest implementations available
in others languages.

The implementations are made in C with a haskell FFI wrapper that hide the
C implementation.

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
%hs_pkgconfdir/%f_pkg_name-%version.conf
%_docdir/%name-%version

%changelog
* Sat Jun 30 2012 Denis Smirnov <mithraen@altlinux.ru> 0.7.5-alt1
- Spec created by cabal2rpm 0.20_08
