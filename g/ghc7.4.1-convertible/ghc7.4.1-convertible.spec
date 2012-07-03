%define ghc_version 7.4.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name convertible
%define f_pkg_name convertible
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.0.11.1
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
URL: http://hackage.haskell.org/cgi-bin/hackage-scripts/package/convertible
Source: %name-%version.tar
Summary: Typeclasses and instances for converting between types



# Automatically added by buildreq on Tue Mar 20 2012 (-bb)
# optimized out: elfutils ghc7.4.1 ghc7.4.1-common ghc7.4.1-transformers libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.4.1-alex ghc7.4.1-c2hs ghc7.4.1-cpphs ghc7.4.1-happy ghc7.4.1-mtl ghc7.4.1-text

%description
convertible provides a typeclass with a single function that is designed to
help convert between different types: numeric values, dates and times, and
the like. The conversions perform bounds checking and return a pure Either
value. This means that you need not remember which specific function
performs the conversion you desire.

Also included in the package are optional instances that provide conversion
for various numeric and time types, as well as utilities for writing your
own instances.

Finally, there is a function that will raise an exception on
bounds-checking violation, or return a bare value otherwise, implemented in
terms of the safer function described above.

Convertible is also used by HDBC 2.0 for handling marshalling of data to
and from databases.

Convertible is backed by an extensive test suite and passes tests on GHC
and Hugs.

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
* Tue Mar 20 2012 Denis Smirnov <mithraen@altlinux.ru> 1.0.11.1-alt1
- Spec created by cabal2rpm 0.20_08
