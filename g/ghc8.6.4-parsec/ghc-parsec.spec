%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name parsec
%define f_pkg_name parsec
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 3.1.14.0
Release: alt1
License: BSD3
Packager: Grigory Ustinov <grenka@altlinux.org>
Group: Development/Haskell
Url: https://hackage.haskell.org/package/parsec
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Monadic parser combinators

BuildRequires: ghc8.6.4 ghc8.6.4-doc


%description
Parsec is designed from scratch as an industrial-strength parser library.
It is simple, safe, well documented (on the package homepage), has
extensive libraries, good error messages, and is fast. It is defined as a
monad transformer that can be stacked on arbitrary monads, and it is also
parametric in the input stream type.

The main entry point is the "Text.Parsec" module which provides defaults
for parsing 'Char'acter data.

The "Text.ParserCombinators.Parsec" module hierarchy contains the legacy
@parsec-2@ API and may be removed at some point in the future.

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
* Thu Aug 29 2019 Grigory Ustinov <grenka@altlinux.org> 3.1.14.0-alt1
- Build new version for ghc8.6.4.
