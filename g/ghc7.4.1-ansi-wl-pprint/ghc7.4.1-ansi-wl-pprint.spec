%define ghc_version 7.4.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name ansi-wl-pprint
%define f_pkg_name ansi-wl-pprint
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.6.4
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
URL: http://github.com/batterseapower/ansi-wl-pprint
Source: %name-%version.tar
Summary: The Wadler/Leijen Pretty Printer for colored ANSI terminal output



# Automatically added by buildreq on Sat Mar 17 2012 (-bb)
# optimized out: elfutils ghc7.4.1 ghc7.4.1-common ghc7.4.1-prof libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.4.1-ansi-terminal

%description
This is a pretty printing library based on Wadler's paper "A Prettier
Printer". It has been enhanced with support for ANSI terminal colored
output using the ansi-terminal package.

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
* Sat Mar 17 2012 Denis Smirnov <mithraen@altlinux.ru> 0.6.4-alt1
- Spec created by cabal2rpm 0.20_08
