Summary: Exploring Conway's Game of Life and other cellular automata
Name: golly
Version: 2.3
Release: alt1

License: GPL
Url: http://golly.sourceforge.net/
Source: %name-%version-src.tar.gz
Source1: %name.sh
Source2: %name.desktop
Group: Education
Packager: Fr. Br. George <george@altlinux.ru>

# TODO: split binary and data
%add_python_req_skip glife golly

Patch: %name-2.1-opensave-alt.patch
Patch1: %name-1.3-perl_syntax-alt.patch
Patch3: %name-gcc43.patch

# Automatically added by buildreq on Tue Sep 28 2010
BuildRequires: ImageMagick-tools gcc-c++ libwxGTK-devel perl-devel python-devel zlib-devel

BuildRequires: perl-Math-BigInt

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

%prep
%setup -n %name-%version-src
#patch -p1
%patch1 -p0
#patch3 -p1
#find . -name ".??*" | xargs rm
sed -i 's/NEEDED +libperl\[/NEEDED +libperl[-/' configure

%build
#autoreconf
#sed -i 's/libperl\[0/libperl[-0/g' configure
sed -i '/#include <EXTERN.h>/a\
#define PERL_GLOBAL_STRUCT
' wxperl.cpp
%configure --with-perl-shlib=%_libdir/perl5/CORE/libperl.so

%make_build
for N in 16 32 48; do convert appicon$N.ico $N.png; done

%install
%makeinstall
for N in 16 32 48; do
  install -D $N.png %buildroot%_iconsdir/hicolor/${N}x$N/apps/%name.png
done

install -D %SOURCE2 %buildroot%_desktopdir/%name.desktop

%files
%exclude %_datadir/doc/%name
%doc README TODO
%_bindir/*
%_datadir/%name
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_desktopdir/*

%changelog
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

