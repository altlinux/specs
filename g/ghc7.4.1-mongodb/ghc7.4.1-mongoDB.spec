%define ghc_version 7.4.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name mongoDB
%define f_pkg_name mongodb
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.2.0
Release: alt1
License: OtherLicense
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
URL: http://github.com/TonyGen/mongoDB-haskell
Source: %name-%version.tar
Summary: Driver (client) for MongoDB, a free, scalable, fast, document DBMS



# Automatically added by buildreq on Thu Mar 22 2012 (-bb)
# optimized out: elfutils ghc7.4.1 ghc7.4.1-base-unicode-symbols ghc7.4.1-common ghc7.4.1-compact-string-fix ghc7.4.1-cryptohash ghc7.4.1-data-binary-ieee754 ghc7.4.1-monad-control ghc7.4.1-monadrandom ghc7.4.1-mtl ghc7.4.1-network ghc7.4.1-parsec ghc7.4.1-random ghc7.4.1-text ghc7.4.1-transformers ghc7.4.1-transformers-base libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.4.1-alex ghc7.4.1-bson ghc7.4.1-c2hs ghc7.4.1-cpphs ghc7.4.1-happy ghc7.4.1-lifted-base ghc7.4.1-random-shuffle

%description
This package lets you connect to MongoDB servers and update/query their
data. Please see the example in Database.MongoDB and the tutorial from the
homepage. For information about MongoDB itself, see www.mongodb.org.

%prep
%setup

%build
%hs_configure2
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
* Tue Mar 20 2012 Denis Smirnov <mithraen@altlinux.ru> 1.2.0-alt1
- Spec created by cabal2rpm 0.20_08
