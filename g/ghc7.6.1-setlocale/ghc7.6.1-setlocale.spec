%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name setlocale
%define f_pkg_name setlocale
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.0.3
Release: alt1
License: PublicDomain
Packager: Igor Zubkov <icesik@altlinux.org>
Group: Development/Haskell
Url: http://hackage.haskell.org/package/setlocale
Source0: setlocale-%version.tar.gz
Summary: A Haskell interface to setlocale()

# Automatically added by buildreq on Wed Feb 26 2014
# optimized out: ghc7.6.1 ghc7.6.1-common libcloog-isl4 libffi-devel libgmp-devel pkg-config
BuildRequires: ghc7.6.1-cpphs

%description
A Haskell interface to @setlocale()@.

%prep
%setup -q -n setlocale-%version

%build
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

%files -f %name-files.all

%changelog
* Thu Feb 27 2014 Igor Zubkov <icesik@altlinux.org> 0.0.3-alt1
- Spec created by cabal2rpm 0.20_08
