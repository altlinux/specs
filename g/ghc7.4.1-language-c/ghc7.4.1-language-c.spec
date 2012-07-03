%define ghc_version 7.4.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name language-c
%define f_pkg_name language-c
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.3.2.1
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
URL: http://www.sivity.net/projects/language.c/
Source: %name-%version.tar
Summary: Analysis and generation of C code



# Automatically added by buildreq on Tue Mar 20 2012 (-bb)
# optimized out: elfutils ghc7.4.1 ghc7.4.1-common libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.4.1-alex ghc7.4.1-happy ghc7.4.1-syb

%description
Language C is a haskell library for the analysis and generation of C code.
It features a complete, well tested parser and pretty printer for all of
C99 and a large set of GNU extensions.

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
* Sat Mar 17 2012 Denis Smirnov <mithraen@altlinux.ru> 0.3.2.1-alt1
- Spec created by cabal2rpm 0.20_08
