%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define h_pkg_name bson
%define f_pkg_name bson
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.1.7
Release: alt1
License: OtherLicense
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>
Group: Development/Haskell
URL: http://github.com/TonyGen/bson-haskell
Source: %name-%version.tar
Summary: BSON documents are JSON-like objects with a standard binary encoding
BuildRequires: ghc ghc-binary ghc-cryptohash ghc-mtl ghc-network ghc-compact-string-fix ghc-data-binary-ieee754
BuildRequires(pre): rpm-build-haskell



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
* Fri Jan 27 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.7-alt1
- Spec created by cabal2rpm 0.20_08
