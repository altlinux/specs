%define ghc_version 7.4.2
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
Url: http://hackage.haskell.org/cgi-bin/hackage-scripts/package/convertible
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Typeclasses and instances for converting between types



# Automatically added by buildreq on Sat Jun 30 2012 (-bb)
# optimized out: elfutils ghc7.4.2 ghc7.4.2-common ghc7.4.2-transformers libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.4.2-doc ghc7.4.2-mtl ghc7.4.2-text

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
%patch -p1

%build
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

%files -f %name-files.nonprof
%hs_pkgconfdir/%f_pkg_name-%version.conf
%_docdir/%name-%version

%changelog
* Sat Jun 30 2012 Denis Smirnov <mithraen@altlinux.ru> 1.0.11.1-alt1
- Spec created by cabal2rpm 0.20_08
