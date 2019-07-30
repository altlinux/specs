%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name cpphs
%define f_pkg_name cpphs
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.20.8
Release: alt1

Summary: A liberalised re-implementation of cpp, the C pre-processor.

License: LGPL
Group: Development/Haskell
Url: http://haskell.org/cpphs/

Source: %name-%version.tar

BuildRequires: ghc8.6.4 ghc8.6.4-doc ghc8.6.4-old-time ghc8.6.4-polyparse

%description
Cpphs is a re-implementation of the C pre-processor that is both more
compatible with Haskell, and itself written in Haskell so that it can be
distributed with compilers.

This version of the C pre-processor is pretty-much feature-complete and
compatible with traditional (K&R) pre-processors. Additional features
include: a plain-text mode; an option to unlit literate code files; and an
option to turn off macro-expansion.

%prep
%setup

%build
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

%files -f %name-files.all

%changelog
* Tue Jul 30 2019 Grigory Ustinov <grenka@altlinux.org> 1.20.8-alt1
- Build new version for ghc8.6.4.

* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 1.15-alt2
- rebuild

* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 1.15-alt1
- Spec created by cabal2rpm 0.20_08
