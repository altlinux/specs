%define ghc_version 7.4.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name text
%define f_pkg_name text
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.11.1.13
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
URL: https://github.com/bos/text
Source: %name-%version.tar
Summary: An efficient packed Unicode text type.



# Automatically added by buildreq on Sat Mar 17 2012 (-bb)
# optimized out: elfutils ghc7.4.1-common ghc7.4.1-prof libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.4.1

%description


An efficient packed, immutable Unicode text type (both strict and lazy),
with a powerful loop fusion optimization framework.

The 'Text' type represents Unicode character strings, in a time and
space-efficient manner. This package provides text processing capabilities
that are optimized for performance critical use, both in terms of large
data quantities and high speed.

The 'Text' type provides character-encoding, type-safe case conversion via
whole-string case conversion functions. It also provides a range of
functions for converting 'Text' values to and from 'ByteStrings', using
several standard encodings.

Efficient locale-sensitive support for text IO is also supported.

These modules are intended to be imported qualified, to avoid name clashes
with Prelude functions, e.g.

> import qualified Data.Text as T

To use an extended and very rich family of functions for working with
Unicode text (including normalization, regular expressions, non-standard
encodings, text breaking, and locales), see the @text-icu@ package:
<http://hackage.haskell.org/package/text-icu>

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
* Sat Mar 17 2012 Denis Smirnov <mithraen@altlinux.ru> 0.11.1.13-alt1
- Spec created by cabal2rpm 0.20_08
