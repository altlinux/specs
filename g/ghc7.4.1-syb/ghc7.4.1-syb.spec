%define ghc_version 7.4.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name syb
%define f_pkg_name syb
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.3.6
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
URL: http://www.cs.uu.nl/wiki/GenericProgramming/SYB
Source: %name-%version.tar
Summary: Scrap Your Boilerplate



# Automatically added by buildreq on Sat Mar 17 2012 (-bb)
# optimized out: elfutils ghc7.4.1-common ghc7.4.1-prof libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.4.1

%description
This package contains the generics system described in the /Scrap Your
Boilerplate/ papers (see
<http://www.cs.uu.nl/wiki/GenericProgramming/SYB>). It defines the @Data@
class of types permitting folding and unfolding of constructor
applications, instances of this class for primitive types, and a variety of
traversals. 

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
* Sat Mar 17 2012 Denis Smirnov <mithraen@altlinux.ru> 0.3.6-alt1
- Spec created by cabal2rpm 0.20_08
