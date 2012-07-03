%define ghc_version 7.4.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name HUnit
%define f_pkg_name hunit
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 1.2.4.2
Release: alt2
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
URL: http://hunit.sourceforge.net/
Source: %name-%version.tar
Summary: A unit testing framework for Haskell



# Automatically added by buildreq on Sat Mar 17 2012 (-bb)
# optimized out: elfutils ghc7.4.1-common ghc7.4.1-prof libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.4.1

%description
HUnit is a unit testing framework for Haskell, inspired by the JUnit tool
for Java, see: <http://www.junit.org>.

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
* Sun Mar 18 2012 Denis Smirnov <mithraen@altlinux.ru> 1.2.4.2-alt2
- rebuild

* Sat Mar 17 2012 Denis Smirnov <mithraen@altlinux.ru> 1.2.4.2-alt1
- Spec created by cabal2rpm 0.20_08
