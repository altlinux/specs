%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name polyparse
%define f_pkg_name polyparse
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.13
Release: alt1

Summary: A variety of alternative parser combinator libraries.

License: LGPL
Group: Development/Haskell
Url: https://hackage.haskell.org/package/polyparse

Source: %name-%version.tar

BuildRequires: ghc8.6.4

%description
A variety of alternative parser combinator libraries, including the
original HuttonMeijer set. The Poly sets have features like good error
reporting, arbitrary token type, running state, lazy parsing, and so on.
Finally, Text.Parse is a proposed replacement for the standard Read class,
for better deserialisation of Haskell values from Strings.

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
* Wed Aug 28 2019 Grigory Ustinov <grenka@altlinux.org> 1.13-alt1
- Build new version.

* Tue Jul 30 2019 Grigory Ustinov <grenka@altlinux.org> 1.12.1-alt1
- Build new version for ghc8.6.4.

* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 1.8-alt1
- Spec created by cabal2rpm 0.20_08
