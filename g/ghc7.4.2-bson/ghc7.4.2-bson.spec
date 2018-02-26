%define ghc_version 7.4.2
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name bson
%define f_pkg_name bson
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.2.1
Release: alt1
License: OtherLicense
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://github.com/selectel/bson-haskell
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: BSON documents are JSON-like objects with a standard binary encoding.



# Automatically added by buildreq on Sun Jul 01 2012 (-bb)
# optimized out: elfutils ghc7.4.2 ghc7.4.2-common ghc7.4.2-mtl ghc7.4.2-parsec ghc7.4.2-text ghc7.4.2-transformers libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.4.2-alex ghc7.4.2-cpphs ghc7.4.2-cryptohash ghc7.4.2-data-binary-ieee754 ghc7.4.2-doc ghc7.4.2-happy ghc7.4.2-network

%description
A BSON Document is an untyped (dynamically type-checked) record. I.e. it is
a list of name-value pairs, where a Value is a single sum type with
constructors for basic types (Bool, Int, Float, String, and Time), compound
types (List, and (embedded) Document), and special types (Binary,
Javascript, ObjectId, RegEx, and a few others).

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
* Sat Jun 30 2012 Denis Smirnov <mithraen@altlinux.ru> 0.2.1-alt1
- Spec created by cabal2rpm 0.20_08
