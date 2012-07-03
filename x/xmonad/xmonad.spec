%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define h_pkg_name xmonad
%define f_pkg_name xmonad
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: xmonad
Version: 0.10
Release: alt3
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://xmonad.org
Source: %name-%version.tar
Source2: 01xmonad
Source3: xmonad.xpm

Patch: %name-%version-%release.patch

Summary: A tiling window manager

BuildRequires: ghc7.4.2-mtl ghc7.4.2-utf8-string ghc7.4.2-x11 libXext-devel libXinerama-devel

%description
xmonad is a tiling window manager for X. Windows are arranged automatically
to tile the screen without gaps or overlap, maximising screen use. All
features of the window manager are accessible from the keyboard: a mouse is
strictly optional. xmonad is written and extensible in Haskell. Custom
layout algorithms, and other extensions, may be written by the user in
config files. Layouts are applied dynamically, and different layouts may be
used on each workspace. Xinerama is fully supported, allowing windows to be
tiled on several screens.

%prep
%setup
%patch -p1

%build
%hs_configure2
%hs_build

%install
%hs_install

mv %buildroot%_datadir/%name-%version/man/xmonad.hs %buildroot%_docdir/%name-%version/
install -m 644 -D man/xmonad.1 %buildroot%_man1dir/xmonad.1

%hs_gen_filelist

install -m0644 -D %SOURCE2 %buildroot%_sysconfdir/X11/wmsession.d/01xmonad

install -m0644 -D %SOURCE3 %buildroot%_iconsdir/%name.xpm

%files -f %name-files.nonprof
%_bindir/xmonad
%hs_pkgconfdir/%f_pkg_name-%version.conf
%_docdir/%name-%version
%_man1dir/xmonad.1.*
%_sysconfdir/X11/wmsession.d/01xmonad
%_iconsdir/xmonad.xpm
%_docdir/%name-%version

%changelog
* Sun Jul 01 2012 Denis Smirnov <mithraen@altlinux.ru> 0.10-alt3
- rebuild with ghc 7.4.2

* Fri Jun 15 2012 Denis Smirnov <mithraen@altlinux.ru> 0.10-alt2
- fix *dm support (Closes: #24192)

* Mon Mar 19 2012 Denis Smirnov <mithraen@altlinux.ru> 0.10-alt1
- 0.10

* Thu Mar 03 2011 Denis Smirnov <mithraen@altlinux.ru> 0.9.2-alt2
- fix build

* Thu Mar 03 2011 Denis Smirnov <mithraen@altlinux.ru> 0.9.2-alt1
- 0.9.2

* Tue Oct 19 2010 Denis Smirnov <mithraen@altlinux.ru> 0.9.1-alt7
- rebuild

* Sat Oct 02 2010 Denis Smirnov <mithraen@altlinux.ru> 0.9.1-alt6
- add *dm support (Closes: #24192)

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 0.9.1-alt5
- auto rebuild

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 0.9.1-alt4
- auto rebuild

* Fri Sep 10 2010 Denis Smirnov <mithraen@altlinux.ru> 0.9.1-alt1
- Spec created by cabal2rpm 0.20_08
