%define ghc_version 7.4.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name X11-xft
%define f_pkg_name x11-xft
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.3.1
Release: alt1
License: LGPL
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
URL: ???
Source: %name-%version.tar
Summary: Bindings to the Xft, X Free Type interface library, and some Xrender parts



# Automatically added by buildreq on Mon Mar 19 2012 (-bb)
# optimized out: elfutils fontconfig fontconfig-devel ghc7.4.1 ghc7.4.1-common ghc7.4.1-syb libX11-devel libXrender-devel libfreetype-devel libgmp-devel pkg-config python-base rpm-build-haskell xorg-renderproto-devel xorg-xproto-devel
BuildRequires: ghc7.4.1-utf8-string ghc7.4.1-x11 libXext-devel libXft-devel libXinerama-devel

%description
Bindings to the Xft, X Free Type interface library, and some Xrender parts

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
* Sat Mar 17 2012 Denis Smirnov <mithraen@altlinux.ru> 0.3.1-alt1
- Spec created by cabal2rpm 0.20_08
