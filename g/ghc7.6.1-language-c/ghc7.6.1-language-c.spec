%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name language-c
%define f_pkg_name language-c
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Serial: 1
Version: 0.3.2.1
Release: alt2
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://www.sivity.net/projects/language.c/
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Analysis and generation of C code



# Automatically added by buildreq on Sat Dec 22 2012 (-bb)
# optimized out: elfutils ghc7.6.1 ghc7.6.1-common libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.6.1-alex ghc7.6.1-cpphs ghc7.6.1-doc ghc7.6.1-happy ghc7.6.1-hscolour ghc7.6.1-syb

%description
Language C is a haskell library for the analysis and generation of C code.
It features a complete, well tested parser and pretty printer for all of
C99 and a large set of GNU extensions.

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
* Fri Feb 08 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:0.3.2.1-alt2
- Downgraded version back to 0.3.2.1 (to fix FTBFS of c2hs).

* Thu Nov 26 2015 Ivan Zakharyaschev <imz@altlinux.org> 0.4.7-alt1
- updated with the help of cabal2gear.

* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.3.2.1-alt1
- Spec created by cabal2rpm 0.20_08
