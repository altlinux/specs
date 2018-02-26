%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define h_pkg_name xmonad-utils
%define f_pkg_name xmonad-utils
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %f_pkg_name
Version: 0.1.2
Release: alt9
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
URL: http://www.haskell.org/haskellwiki/Xmonad-utils 
Source: %name-%version.tar
Summary: A small collection of X utilities
# Automatically added by buildreq on Mon Mar 19 2012 (-bb)
# optimized out: elfutils ghc7.4.1 ghc7.4.1-common ghc7.4.1-syb libX11-devel libgmp-devel pkg-config
BuildRequires: ghc7.4.1-random ghc7.4.1-x11 libXext-devel libXinerama-devel

%description
A small collection of X utilities useful when running XMonad. It includes:

* hxsel, which returns the text currently in the X selection;

* hslock, a simple X screen lock;

* hmanage: an utility to toggle the override-redirect property of any
window;

* and hhp, a simple utility to hide the pointer, similar to unclutter.

%prep
%setup

%build
%hs_configure2
%hs_build

%install
runghc Setup copy --destdir=%buildroot

%files
%_bindir/*

%changelog
* Mon Mar 19 2012 Denis Smirnov <mithraen@altlinux.ru> 0.1.2-alt9
- rebuild with ghc 7.4.1

* Tue Mar 08 2011 Denis Smirnov <mithraen@altlinux.ru> 0.1.2-alt8
- fix build with ghc 7

* Sun Oct 24 2010 Denis Smirnov <mithraen@altlinux.ru> 0.1.2-alt7
- rebuild

* Tue Oct 19 2010 Denis Smirnov <mithraen@altlinux.ru> 0.1.2-alt6
- rebuild

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 0.1.2-alt5
- auto rebuild

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 0.1.2-alt4
- auto rebuild

* Fri Sep 10 2010 Denis Smirnov <mithraen@altlinux.ru> 0.1.2-alt1
- Spec created by cabal2rpm 0.20_08
