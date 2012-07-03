%define ghc_version 7.4.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name pandoc-types
%define f_pkg_name pandoc-types
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.9.1
Release: alt1
License: GPL
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
URL: http://johnmacfarlane.net/pandoc
Source: %name-%version.tar
Summary: Types for representing a structured document



# Automatically added by buildreq on Sun Mar 18 2012 (-bb)
# optimized out: elfutils ghc7.4.1 ghc7.4.1-common libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.4.1-syb

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
* Sat Mar 17 2012 Denis Smirnov <mithraen@altlinux.ru> 1.9.1-alt1
- Spec created by cabal2rpm 0.20_08
