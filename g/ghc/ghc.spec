%define ghc_major 9.6
%define ghc_version 9.6.6

%define warn_description This package only contains bindings to current "stable" ghc release - %ghc_major

%def_with docs

Name: ghc
Version: %ghc_version
Release: alt1

Summary: Metapackage for current stable GHC
License: BSD-3-Clause and HaskellReport
Group: Development/Haskell
Url: http://haskell.org/ghc/

BuildRequires(Pre): rpm-build-haskell-extra
BuildArch: noarch

Requires: ghc%ghc_major = %version
Requires: ghc%ghc_major-common = %version

Conflicts: ghc%ghc_major > %version
Conflicts: ghc%ghc_major < %version

%description
GHC is a state-of-the-art programming suite for Haskell.  Included is
an optimising compiler generating good code for a variety of
platforms, together with an interactive system for convenient, quick
development.  The distribution includes space and time profiling
facilities, a large collection of libraries, and support for various
language extensions, including concurrency, exceptions, and foreign
language interfaces (C, C++, whatever).

%warn_description

%package doc
Summary: Documentation for GHC
Group: Development/Haskell

%description doc
Preformatted documentation for the Glasgow Haskell Compiler
(GHC) and its libraries. Install it if you like to have local
access to the documentation in PostScript and HTML format.
Alternatively, the documentation is available online at
http://haskell.org/ghc/documentation.html

%warn_description

%package doc-index
Summary: GHC library documentation indexing
Group: Development/Haskell

BuildArch: noarch

%description doc-index
The package enables re-indexing of installed library documention.

%warn_description

%package devel
Summary: GHC development libraries meta package
Group: Development/Haskell

Requires: %name = %EVR
Requires: ghc%ghc_major-devel

%description devel
This is a meta-package for all the development library packages in GHC

%warn_description

# Next strings are taken from ghc%%ghc_major spec
# Only %%ghc_lib_subpackage replaced via %%ghc_lib_subpackage_empty
%ghc_lib_subpackage_empty -n ghc -v %version

%define basepkg_version 4.18.2.1
%ghc_lib_subpackage_empty -n array -v 0.5.6.0
%ghc_lib_subpackage_empty -n base -v 4.18.2.1
%ghc_lib_subpackage_empty -n binary -v 0.8.9.1
%ghc_lib_subpackage_empty -n bytestring -v 0.11.5.3
%ghc_lib_subpackage_empty -n Cabal-syntax -v 3.10.3.0
%ghc_lib_subpackage_empty -n Cabal -v 3.10.3.0
%ghc_lib_subpackage_empty -n containers -v 0.6.7
%ghc_lib_subpackage_empty -n deepseq -v 1.4.8.1
%ghc_lib_subpackage_empty -n directory -v 1.3.8.5
%ghc_lib_subpackage_empty -n exceptions -v 0.10.7
%ghc_lib_subpackage_empty -n filepath -v 1.4.300.1
%ghc_lib_subpackage_empty -n ghc-bignum -v 1.3
%ghc_lib_subpackage_empty -n ghc-boot-th -v 9.6.6
%ghc_lib_subpackage_empty -n ghc-boot -v 9.6.6
%ghc_lib_subpackage_empty -n ghc-compact -v 0.1.0.0
%ghc_lib_subpackage_empty -n ghc-heap -v 9.6.6
%ghc_lib_subpackage_empty -n ghci -v 9.6.6
%ghc_lib_subpackage_empty -n ghc-prim -v 0.10.0
%ghc_lib_subpackage_empty -n haskeline -v 0.8.2.1
%ghc_lib_subpackage_empty -n hpc -v 0.6.2.0
%ghc_lib_subpackage_empty -n integer-gmp -v 1.1
%ghc_lib_subpackage_empty -n libiserv -v 9.6.6
%ghc_lib_subpackage_empty -n mtl -v 2.3.1
%ghc_lib_subpackage_empty -n parsec -v 3.1.16.1
%ghc_lib_subpackage_empty -n pretty -v 1.1.3.6
%ghc_lib_subpackage_empty -n process -v 1.6.19.0
%ghc_lib_subpackage_empty -n stm -v 2.5.1.0
%ghc_lib_subpackage_empty -n template-haskell -v 2.20.0.0
%ghc_lib_subpackage_empty -n terminfo -v 0.4.1.6
%ghc_lib_subpackage_empty -n text -v 2.0.2
%ghc_lib_subpackage_empty -n time -v 1.12.2
%ghc_lib_subpackage_empty -n transformers -v 0.6.1.0
%ghc_lib_subpackage_empty -n ucd2haskell -v 0.3.0
%ghc_lib_subpackage_empty -n unix -v 2.8.4.0
%ghc_lib_subpackage_empty -n xhtml -v 3000.2.2.1

%files

%files doc

%files doc-index

%files devel

%changelog
* Tue Mar 18 2025 Leonid Znamenok <respublica@altlinux.org> 9.6.6-alt1
- Bumped to GHC 9.6.6

* Wed Feb 19 2025 Leonid Znamenok <respublica@altlinux.org> 9.2.8-alt1
- Initial build for Sisyphus
