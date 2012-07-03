%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define h_pkg_name text
%define f_pkg_name text
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.11.1.5
Release: alt1.1
License: BSD3
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>
Group: Development/Haskell
URL: https://bitbucket.org/bos/text
Source: %name-%version.tar
Summary: An efficient packed Unicode text type.
BuildRequires: ghc ghc-deepseq
BuildRequires(pre): rpm-build-haskell



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
* Sat Aug 13 2011 Denis Smirnov <mithraen@altlinux.ru> 0.11.1.5-alt1.1
- rebuild with shared objects support

* Wed Aug 03 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.11.1.5-alt1
- Spec created by cabal2rpm 0.20_08
