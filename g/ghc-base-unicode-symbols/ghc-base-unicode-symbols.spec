%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define h_pkg_name base-unicode-symbols
%define f_pkg_name base-unicode-symbols
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.2.2.3
Release: alt1
License: BSD3
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>
Group: Development/Haskell
URL: http://haskell.org/haskellwiki/Unicode-symbols
Source: %name-%version.tar
Summary: Unicode alternatives for common functions and operators
BuildRequires: ghc 
BuildRequires(pre): rpm-build-haskell



%description
This package defines new symbols for a number of functions, operators and
types in the base package.

All symbols are documented with their actual definition and information
regarding their Unicode code point. They should be completely
interchangeable with their definitions.

For further Unicode goodness you can enable the @UnicodeSyntax@ language
extension \[1\]. This extension enables Unicode characters to be used to
stand for certain ASCII character sequences, i.e. &#x2192; instead of @->@,
&#x2200; instead of @forall@ and many others.

Original idea by P&#xE9;ter Divi&#xE1;nszky.

\[1\]
<http://www.haskell.org/ghc/docs/latest/html/users_guide/syntax-extns.html#
unicode-syntax> 

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
* Fri Jan 27 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.2.3-alt1
- Spec created by cabal2rpm 0.20_08
