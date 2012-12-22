%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name mongoDB
%define f_pkg_name mongodb
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.3.1
Release: alt1
License: OtherLicense
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://github.com/selectel/mongodb-haskell
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Driver (client) for MongoDB, a free, scalable, fast, document DBMS



# Automatically added by buildreq on Sat Dec 22 2012 (-bb)
# optimized out: elfutils ghc7.6.1 ghc7.6.1-base-unicode-symbols ghc7.6.1-common ghc7.6.1-cryptohash ghc7.6.1-data-binary-ieee754 ghc7.6.1-monad-control ghc7.6.1-monadrandom ghc7.6.1-mtl ghc7.6.1-network ghc7.6.1-parsec ghc7.6.1-random ghc7.6.1-text ghc7.6.1-transformers ghc7.6.1-transformers-base libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.6.1-bson ghc7.6.1-cpphs ghc7.6.1-doc ghc7.6.1-happy ghc7.6.1-hscolour ghc7.6.1-lifted-base ghc7.6.1-random-shuffle

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

%changelog
* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 1.3.1-alt1
- Spec created by cabal2rpm 0.20_08
