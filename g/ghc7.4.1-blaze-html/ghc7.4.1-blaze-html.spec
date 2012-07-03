%define ghc_version 7.4.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name blaze-html
%define f_pkg_name blaze-html
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.4.3.1
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
URL: http://jaspervdj.be/blaze
Source: %name-%version.tar
Summary: A blazingly fast HTML combinator library for Haskell



# Automatically added by buildreq on Tue Mar 20 2012 (-bb)
# optimized out: elfutils ghc7.4.1 ghc7.4.1-common ghc7.4.1-text libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.4.1-alex ghc7.4.1-blaze-builder

%description
A blazingly fast HTML combinator library for the Haskell programming
language. The Text.Blaze module is a good starting point, as well as this
tutorial: <http://jaspervdj.be/blaze/tutorial.html>. 

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
* Mon Mar 19 2012 Denis Smirnov <mithraen@altlinux.ru> 0.4.3.1-alt1
- Spec created by cabal2rpm 0.20_08
