%define ghc_version 7.4.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name haskell-src
%define f_pkg_name haskell-src
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.0.1.5
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
URL: ???
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Support for manipulating Haskell source code



# Automatically added by buildreq on Sun Mar 25 2012 (-bb)
# optimized out: elfutils ghc7.4.1 ghc7.4.1-common libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.4.1-alex ghc7.4.1-c2hs ghc7.4.1-cpphs ghc7.4.1-happy ghc7.4.1-hscolour ghc7.4.1-syb

%description
The 'haskell-src' package provides support for manipulating Haskell source
code. The package provides a lexer, parser and pretty-printer, and a
definition of a Haskell abstract syntax tree (AST). Common uses of this
package are to parse or generate Haskell 98 code.

%prep
%setup
%patch -p1

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
* Sun Mar 25 2012 Denis Smirnov <mithraen@altlinux.ru> 1.0.1.5-alt1
- Spec created by cabal2rpm 0.20_08
