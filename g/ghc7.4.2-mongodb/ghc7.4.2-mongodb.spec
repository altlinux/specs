%define ghc_version 7.4.2
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name mongoDB
%define f_pkg_name mongodb
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.3.0
Release: alt1
License: OtherLicense
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://github.com/selectel/mongodb-haskell
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Driver (client) for MongoDB, a free, scalable, fast, document DBMS



# Automatically added by buildreq on Sun Jul 01 2012 (-bb)
# optimized out: elfutils ghc7.4.2 ghc7.4.2-base-unicode-symbols ghc7.4.2-cereal ghc7.4.2-common ghc7.4.2-crypto-api ghc7.4.2-cryptohash ghc7.4.2-data-binary-ieee754 ghc7.4.2-entropy ghc7.4.2-largeword ghc7.4.2-monad-control ghc7.4.2-monadrandom ghc7.4.2-mtl ghc7.4.2-network ghc7.4.2-parsec ghc7.4.2-random ghc7.4.2-tagged ghc7.4.2-text ghc7.4.2-transformers ghc7.4.2-transformers-base libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.4.2-alex ghc7.4.2-bson ghc7.4.2-cpphs ghc7.4.2-doc ghc7.4.2-happy ghc7.4.2-hscolour ghc7.4.2-lifted-base ghc7.4.2-random-shuffle

%description
This package lets you connect to MongoDB servers and update/query their
data. Please see the example in Database.MongoDB and the tutorial from the
homepage. For information about MongoDB itself, see www.mongodb.org.

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
* Sat Jun 30 2012 Denis Smirnov <mithraen@altlinux.ru> 1.3.0-alt1
- Spec created by cabal2rpm 0.20_08
