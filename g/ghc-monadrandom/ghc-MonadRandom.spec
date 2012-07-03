%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define h_pkg_name MonadRandom
%define f_pkg_name monadrandom
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.1.6
Release: alt1
License: OtherLicense
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>
Group: Development/Haskell
URL: http://hackage.haskell.org/package/MonadRandom
Source: %name-%version.tar
Summary: Random-number generation monad.
BuildRequires: ghc ghc-mtl
BuildRequires(pre): rpm-build-haskell



%description
Support for computations which consume random values.

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
* Fri Jan 27 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.6-alt1
- Spec created by cabal2rpm 0.20_08
