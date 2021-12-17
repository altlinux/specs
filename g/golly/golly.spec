Summary: Exploring Conway's Game of Life and other cellular automata
Name: golly
Version: 4.1
Release: alt1

License: GPL
Url: http://golly.sourceforge.net/
Source: %name-%version-src.tar.gz
Source1: %name.sh
Source2: %name.desktop
Group: Education

%add_python_req_skip glife golly

Requires: %name-data = %EVR

# Automatically added by buildreq on Wed Dec 15 2021
# optimized out: at-spi2-atk fontconfig glibc-kernheaders-generic glibc-kernheaders-x86 libImageMagick6-common libat-spi2-core libcairo-gobject libgdk-pixbuf libglvnd-devel libgpg-error libstdc++-devel libwayland-client libwayland-cursor libwayland-egl libwxBase3.1-devel libwxGTK3.1-gl python3 python3-base sh4
BuildRequires: ImageMagick-tools gcc-c++ libGLU-devel libSDL2-devel libwxGTK3.1-devel python3-dev zlib-devel

%description
Welcome to Golly, a sophisticated tool for exploring Conway's
Game of Life and other cellular automata.

- Unbounded universe (limited only by memory).
- Fast, memory-efficient conventional algorithm.
- Use hashing to see large patterns evolve at huge time scales.
- Responsive even while generating or garbage collecting.
- Reads RLE, Life 1.05/1.06, dblife, and macrocell formats.
- Can also read common graphic formats: BMP, PNG, GIF, TIFF.
- Includes a state-of-the-art pattern collection.
- Supports other Life-like rules and Wolfram's 1D rules.
- Fast loading of large patterns.
- Paste in patterns from the clipboard.
- Unlimited undo/redo.
- Unbounded zooming out for astronomical patterns.
- Auto fit option keeps a generating pattern within view.
- Full screen option (no menu/status/tool/scroll bars).
- Supports multiple layers, including cloned layers.
- HTML-based help with integrated Life Lexicon.
- Scriptable via Perl or Python.
- User-configurable keyboard shortcuts.
- Free, open source and cross-platform (Windows, Mac, Linux).
- We also provide bgolly, a GUI-less version.

%package data
Summary: Data files for %name, cellular automata emulation software
BuildArch: noarch
Group: Education
%description data
%summary

%prep
%setup -n %name-%version-src

%build
cd gui-wx
%make_build -f makefile-gtk GOLLYDIR=%_datadir/%name

for N in 16 32 48; do convert icons/appicon$N.ico $N.png; done

%install
install -d %buildroot/%_bindir %buildroot/%_datadir/%name
install golly %buildroot/%_bindir/
install bgolly %buildroot/%_bindir/
cp -a Help Patterns Rules Scripts %buildroot/%_datadir/%name/

for N in 16 32 48; do
  install -D gui-wx/$N.png %buildroot%_iconsdir/hicolor/${N}x$N/apps/%name.png
done

install -D %SOURCE2 %buildroot%_desktopdir/%name.desktop

%files
%doc docs/*
%_bindir/*
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_desktopdir/*

%files data
%_datadir/%name

%changelog
* Tue Dec 14 2021 Fr. Br. George <george@altlinux.ru> 4.1-alt1
- Autobuild version bump to 4.1
- Remove already broken PERL support
- No upstream configure any more

* Tue Feb 20 2018 Fr. Br. George <george@altlinux.ru> 3.1-alt1
- Autobuild version bump to 3.1

* Mon Sep 18 2017 Fr. Br. George <george@altlinux.ru> 3.0-alt1
- Autobuild version bump to 3.0

* Wed Mar 15 2017 Fr. Br. George <george@altlinux.ru> 2.8-alt1
- Autobuild version bump to 2.8
- Separate data package

* Tue Jul 14 2015 Fr. Br. George <george@altlinux.ru> 2.7-alt1
- Autobuild version bump to 2.7

* Thu Feb 06 2014 Fr. Br. George <george@altlinux.ru> 2.6-alt1
- Autobuild version bump to 2.6

* Thu Aug 22 2013 Fr. Br. George <george@altlinux.ru> 2.5-alt1
- Autobuild version bump to 2.5
- Fix build

* Sun Jul 22 2012 Fr. Br. George <george@altlinux.ru> 2.4-alt1
- Autobuild version bump to 2.4

* Thu Jan 12 2012 Fr. Br. George <george@altlinux.ru> 2.3-alt1
- Autobuild version bump to 2.3

* Mon Nov 07 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2-alt2.1
- Rebuild with Python-2.7

* Mon Nov 07 2011 Fr. Br. George <george@altlinux.ru> 2.2-alt2
- Hack against Perl5.14

* Fri Jan 14 2011 Fr. Br. George <george@altlinux.ru> 2.2-alt1
- Autobuild version bump to 2.2
- Build switched to configure/make/make install
- Move away perl 5.12 patch -- doesn't build with it

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 2.1-alt2.1
- rebuilt with perl 5.12

* Wed Sep 29 2010 Fr. Br. George <george@altlinux.ru> 2.1-alt2
- Fix system-wide and local directories

* Wed Sep 29 2010 Fr. Br. George <george@altlinux.ru> 2.1-alt1
- Autobuild version bump to 2.1

* Tue Sep 28 2010 Fr. Br. George <george@altlinux.ru> 2.0-alt1
- Version up

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt2.1
- Rebuilt with python 2.6

* Tue Nov 18 2008 Fr. Br. George <george@altlinux.ru> 1.4-alt2
- x32 fix

* Tue Oct 28 2008 Fr. Br. George <george@altlinux.ru> 1.4-alt1
- Version up

* Sun Feb 17 2008 Fr. Br. George <george@altlinux.ru> 1.3-alt1
- Initial build from scratch

