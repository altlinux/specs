%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name bitarray
%define f_pkg_name bitarray
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.0.1.1
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://code.haskell.org/~bkomuves/
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Mutable and immutable bit arrays

BuildPreReq: haskell(abi) = %ghc_version


%description
Mutable and immutable bit arrays.

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
* Sun Jun 21 2020 Denis Smirnov <mithraen@altlinux.ru> 0.0.1.1-alt1
- Spec created by cabal2rpm 0.20_10
