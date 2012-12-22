%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name pandoc-types
%define f_pkg_name pandoc-types
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.9.1
Release: alt2
License: GPL
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://johnmacfarlane.net/pandoc
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Types for representing a structured document



# Automatically added by buildreq on Sat Dec 22 2012 (-bb)
# optimized out: elfutils ghc7.4.2-common ghc7.6.1 ghc7.6.1-common libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.6.1-cpphs ghc7.6.1-doc ghc7.6.1-hscolour ghc7.6.1-syb

%description
This package contains definitions for the 'Pandoc' data structure, which is
used by pandoc to represent structured documents. These definitions used to
live in the pandoc package, but starting with pandoc 1.7, they have been
split off, so that other packages can use them without drawing in all of
pandoc's dependencies, and pandoc itself can depend on packages (like
citeproc-hs) that use them.

@Text.Pandoc.Builder@ provides functions for building up @Pandoc@
structures programmatically.

@Text.Pandoc.Generic@ provides generic functions for manipulating Pandoc
documents.

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
* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 1.9.1-alt2
- rebuild

* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 1.9.1-alt1
- Spec created by cabal2rpm 0.20_08
