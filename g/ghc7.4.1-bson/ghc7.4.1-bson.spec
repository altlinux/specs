%define ghc_version 7.4.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name bson
%define f_pkg_name bson
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.1.7
Release: alt1
License: OtherLicense
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
URL: http://github.com/TonyGen/bson-haskell
Source: %name-%version.tar
Summary: BSON documents are JSON-like objects with a standard binary encoding



# Automatically added by buildreq on Thu Mar 22 2012 (-bb)
# optimized out: elfutils ghc7.4.1 ghc7.4.1-common ghc7.4.1-mtl ghc7.4.1-parsec ghc7.4.1-text ghc7.4.1-transformers libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.4.1-alex ghc7.4.1-c2hs ghc7.4.1-compact-string-fix ghc7.4.1-cpphs ghc7.4.1-cryptohash ghc7.4.1-data-binary-ieee754 ghc7.4.1-happy ghc7.4.1-network

%description
A BSON Document is an untyped (dynamically type-checked) record. I.e. it is
a list of name-value pairs, where a Value is a single sum type with
constructors for basic types (Bool, Int, Float, String, and Time), compound
types (List, and (embedded) Document), and special types (Binary,
Javascript, ObjectId, RegEx, and a few others).

A BSON Document is serialized to a standard binary encoding defined at
<http://bsonspec.org>. This implements version 1 of that spec. 

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
* Tue Mar 20 2012 Denis Smirnov <mithraen@altlinux.ru> 0.1.7-alt1
- Spec created by cabal2rpm 0.20_08
