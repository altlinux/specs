%define ghc_version 7.4.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name largeword
%define f_pkg_name largeword
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.0.1
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
URL: http://trac.haskell.org/largeword/wiki
Source: %name-%version.tar
Summary: Provides Word128, Word192 and Word256 and a way of producing other large words if required.



# Automatically added by buildreq on Sat Mar 17 2012 (-bb)
# optimized out: elfutils ghc7.4.1-common ghc7.4.1-prof libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.4.1

%description
Provides Word128, Word192 and Word256 and a way of producing other large
words if required.

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
* Sat Mar 17 2012 Denis Smirnov <mithraen@altlinux.ru> 1.0.1-alt1
- Spec created by cabal2rpm 0.20_08
