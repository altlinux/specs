%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define h_pkg_name xmobar
%define f_pkg_name xmobar
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: xmobar
Version: 0.15
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://code.haskell.org/~arossato/xmobar
Source: %name-%version.tar
Summary: A Minimalistic Text Based Status Bar

Patch: %name-%version-%release.patch

# Automatically added by buildreq on Sun Mar 25 2012 (-bb)
# optimized out: elfutils fontconfig ghc7.4.2 ghc7.4.2-alsa-core ghc7.4.2-common ghc7.4.2-mtl ghc7.4.2-syb ghc7.4.2-text ghc7.4.2-timezone-series ghc7.4.2-transformers ghc7.4.2-utf8-string ghc7.4.2-x11 libX11-devel libXrender-devel libgmp-devel pkg-config python-base xorg-kbproto-devel xorg-randrproto-devel xorg-renderproto-devel xorg-xproto-devel
BuildRequires: ghc7.4.2-alex ghc7.4.2-alsa-mixer ghc7.4.2-c2hs ghc7.4.2-cpphs ghc7.4.2-happy ghc7.4.2-hinotify ghc7.4.2-hscolour ghc7.4.2-parsec ghc7.4.2-stm ghc7.4.2-timezone-olson ghc7.4.2-x11-xft libXext-devel libXft-devel libXinerama-devel libXrandr-devel libalsa-devel libwireless-devel

%description
Xmobar is a minimalistic text based status bar.

Inspired by the Ion3 status bar, it supports similar features, like dynamic
color management, output templates, and extensibility through plugins.

%prep
%setup -n %h_pkg_name-%version
%patch -p1

%build
%hs_configure2 -f "with_xft with_utf8 with_inotify with_datezone with_iwlib with_alsa"
%hs_build

%install
runghc Setup copy --destdir=%buildroot

%files
%_bindir/%name
%doc news.md readme.md

%changelog
* Mon Jul 23 2012 Denis Smirnov <mithraen@altlinux.ru> 0.15-alt1
- 0.15

* Mon Jul 23 2012 Denis Smirnov <mithraen@altlinux.ru> 0.14-alt3
- rebuild with new 7.4.2

* Sun Mar 25 2012 Denis Smirnov <mithraen@altlinux.ru> 0.14-alt2
- rebuild with ghc 7.14

* Mon Jan 09 2012 Denis Smirnov <mithraen@altlinux.ru> 0.14-alt1
- 0.14

* Wed Aug 03 2011 Denis Smirnov <mithraen@altlinux.ru> 0.13-alt1
- 0.13

* Wed Mar 09 2011 Denis Smirnov <mithraen@altlinux.ru> 0.12-alt2
- build -threaded version

* Thu Mar 03 2011 Denis Smirnov <mithraen@altlinux.ru> 0.12-alt1
- 0.12

* Sun Oct 10 2010 Denis Smirnov <mithraen@altlinux.ru> 0.11.1-alt9
- add xmobar.config-sample

* Thu Sep 16 2010 Denis Smirnov <mithraen@altlinux.ru> 0.11.1-alt8
- fix build requires

* Thu Sep 16 2010 Denis Smirnov <mithraen@altlinux.ru> 0.11.1-alt7
- build with MPD support

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 0.11.1-alt6
- auto rebuild

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 0.11.1-alt5
- auto rebuild

* Thu Sep 09 2010 Denis Smirnov <mithraen@altlinux.ru> 0.11.1-alt2
- first build for Sisyphus
