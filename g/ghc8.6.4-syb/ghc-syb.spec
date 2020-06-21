%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name syb
%define f_pkg_name syb
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.7.1
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://www.cs.uu.nl/wiki/GenericProgramming/SYB
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Scrap Your Boilerplate

BuildPreReq: haskell(abi) = %ghc_version


%description
This package contains the generics system described in the /Scrap Your
Boilerplate/ papers (see
<http://www.cs.uu.nl/wiki/GenericProgramming/SYB>). It defines the @Data@
class of types permitting folding and unfolding of constructor
applications, instances of this class for primitive types, and a variety of
traversals.

%prep
%setup
%patch -p1

%build
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

%files -f %name-files.all

%changelog
* Sun Jun 21 2020 Denis Smirnov <mithraen@altlinux.ru> 0.7.1-alt1
- Spec created by cabal2rpm 0.20_10
