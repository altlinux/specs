%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define h_pkg_name xmonad-contrib
%define f_pkg_name xmonad-contrib
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: xmonad-contrib
Version: 0.10
Release: alt3
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://xmonad.org/
Source: %name-%version.tar
Summary: Third party extensions for xmonad

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-haskell

BuildRequires: ghc7.4.2-random libXext-devel libXinerama-devel xmonad

%description
Third party tiling algorithms, configurations and scripts to xmonad, a
tiling window manager for X.

For an introduction to building, configuring and using xmonad extensions,
see "XMonad.Doc". In particular:

"XMonad.Doc.Configuring", a guide to configuring xmonad

"XMonad.Doc.Extending", using the contributed extensions library

"XMonad.Doc.Developing", introduction to xmonad internals and writing your
own extensions.

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
%hs_pkgconfdir/%f_pkg_name-%version.conf

%changelog
* Sun Jul 01 2012 Denis Smirnov <mithraen@altlinux.ru> 0.10-alt3
- cleanup

* Sun Jul 01 2012 Denis Smirnov <mithraen@altlinux.ru> 0.10-alt2
- rebuild with ghc 7.4.2

* Mon Mar 19 2012 Denis Smirnov <mithraen@altlinux.ru> 0.10-alt1
- 0.10

* Thu Mar 03 2011 Denis Smirnov <mithraen@altlinux.ru> 0.9.2-alt1
- 0.9.2

* Tue Sep 14 2010 Denis Smirnov <mithraen@altlinux.ru> 0.9.1-alt6
- fix build

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 0.9.1-alt5
- auto rebuild

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 0.9.1-alt4
- auto rebuild

* Fri Sep 10 2010 Denis Smirnov <mithraen@altlinux.ru> 0.9.1-alt1
- Spec created by cabal2rpm 0.20_08
