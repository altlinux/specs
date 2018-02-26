%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define h_pkg_name xmobar
%define f_pkg_name xmobar
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: xmobar
Version: 0.14
Release: alt2
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://code.haskell.org/~arossato/xmobar
Source: %name-%version.tar
Summary: A Minimalistic Text Based Status Bar

Patch: %name-%version-%release.patch

# Automatically added by buildreq on Sun Mar 25 2012 (-bb)
# optimized out: elfutils fontconfig ghc7.4.1 ghc7.4.1-alsa-core ghc7.4.1-common ghc7.4.1-mtl ghc7.4.1-syb ghc7.4.1-text ghc7.4.1-timezone-series ghc7.4.1-transformers ghc7.4.1-utf8-string ghc7.4.1-x11 libX11-devel libXrender-devel libgmp-devel pkg-config python-base xorg-kbproto-devel xorg-randrproto-devel xorg-renderproto-devel xorg-xproto-devel
BuildRequires: ghc7.4.1-alex ghc7.4.1-alsa-mixer ghc7.4.1-c2hs ghc7.4.1-cpphs ghc7.4.1-happy ghc7.4.1-hinotify ghc7.4.1-hscolour ghc7.4.1-parsec ghc7.4.1-stm ghc7.4.1-timezone-olson ghc7.4.1-x11-xft libXext-devel libXft-devel libXinerama-devel libXrandr-devel libalsa-devel libwireless-devel

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
%doc LICENSE README samples

%changelog
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
