%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define h_pkg_name compact-string-fix
%define f_pkg_name compact-string-fix
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.3.2
Release: alt1
License: BSD3
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>
Group: Development/Haskell
URL: http://twan.home.fmf.nl/compact-string/
Source: %name-%version.tar
Summary: Same as compact-string except with a small fix so it builds on ghc-6.12
BuildRequires: ghc 
BuildRequires(pre): rpm-build-haskell



%description
Fast, packed, strict strings with a list interface. Based on
"Data.ByteString". Multiple encodings are supported. This is the same
package as compact-string-0.3.1 except for a small fix to work with the new
Exception library. Once Twan updates that package, this package will be
deprecated. build-type: Simple 

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
* Fri Jan 27 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.2-alt1
- Spec created by cabal2rpm 0.20_08
