%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define h_pkg_name transformers-base
%define f_pkg_name transformers-base
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.4.1
Release: alt1
License: BSD3
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>
Group: Development/Haskell
URL: https://github.com/mvv/transformers-base
Source: %name-%version.tar
Summary: Lift computations from the bottom of a transformer stack
BuildRequires: ghc ghc-transformers
BuildRequires(pre): rpm-build-haskell



%description
This package provides a straightforward port of @monadLib@'s BaseM
typeclass to @transformers@. 

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
* Fri Jan 27 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.1-alt1
- Spec created by cabal2rpm 0.20_08
