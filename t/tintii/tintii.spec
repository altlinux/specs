Name: tintii
Version: 2.6.1
Release: alt2

Summary: A photo editor for colour-select effects
License: BSD (revised)
Group: Graphics

Url: http://www.indii.org/software/tintii
Source0: http://www.indii.org/files/tint/releases/%name-%version.tar.gz
Source1: tintii-48.png
Source2: tintii-32.png
Source3: tintii-16.png
Source100: tintii.watch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Tue Oct 25 2011 (-bi)
# optimized out: elfutils fontconfig libgdk-pixbuf libstdc++-devel
BuildRequires: boost-devel-headers gcc-c++ libgomp-devel libwxGTK-devel

%description
Welcome to tintii, a photo editor for colour-select effects.

It automatically clusters the colours of a photo into groups,
and allows each colour to be switched on or off to create the
desired effect.

tintii's predecessor, a less powerful but somewhat simpler one,
is called tint; you might want to have a look at it too.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
install -d %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Version=1.0
Encoding=UTF-8
Type=Application
Name=tintii
GenericName=Image Tinter
Comment=Photo editor for colour-select effects
Exec=tintii
Icon=tintii
Terminal=false
Categories=Graphics;2DGraphics;RasterGraphics;GTK;
EOF
install -pDm644 %SOURCE1 %buildroot%_liconsdir/%name.png
install -pDm644 %SOURCE2 %buildroot%_niconsdir/%name.png
install -pDm644 %SOURCE3 %buildroot%_miconsdir/%name.png

%files
%_bindir/%name
%_datadir/%name/
%_desktopdir/%name.desktop
%_liconsdir/%name.png
%_niconsdir/%name.png
%_miconsdir/%name.png
%doc README

%changelog
* Wed May 09 2012 Michael Shigorin <mike@altlinux.org> 2.6.1-alt2
- added watch file
  + NB: 2.6.2 seems to be win32/osx-only release

* Sun Mar 18 2012 Michael Shigorin <mike@altlinux.org> 2.6.1-alt1
- 2.6.1

* Sun Mar 11 2012 Michael Shigorin <mike@altlinux.org> 2.6.0-alt1
- 2.6.0

* Fri Oct 28 2011 Michael Shigorin <mike@altlinux.org> 2.5.3-alt4
- pulled an icon out of thin splash image (thx vova1971@)
- uncompressed the gear-generated tarball

* Tue Oct 25 2011 Michael Shigorin <mike@altlinux.org> 2.5.3-alt3
- backdated real@'s changelog entry

* Tue Oct 25 2011 Michael Shigorin <mike@altlinux.org> 2.5.3-alt2
- dropped Provides:/Obsoletes: tint (quite different by now)

* Tue Oct 25 2011 Michael Shigorin <mike@altlinux.org> 2.5.3-alt1
- 2.5.3
  + upstream moved from scons to autocrap, hooray!
- dropped the patch
- spec cleanup
- buildreq

* Tue Jul 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.2-alt1.1
- Rebuilt with updated wxGTK2.9

* Thu Apr 21 2011 Michael Shigorin <mike@altlinux.org> 2.5.2-alt1
- 2.5.2

* Fri Mar 12 2010 Michael Shigorin <mike@altlinux.org> 2.2.0-alt2
- gratefully accepted FTBFS fix by raorn@

* Tue Sep 29 2009 Michael Shigorin <mike@altlinux.org> 2.2.0-alt1
- 2.2.0
- buildreq

* Wed May 13 2009 Michael Shigorin <mike@altlinux.org> 2.1.0-alt1
- 2.1.0
- updated an Url:

* Thu Mar 26 2009 Michael Shigorin <mike@altlinux.org> 2.0.0-alt1
- 2.0.0
  + name changed from Tint to tintii
  + no more samples/
- removed patch
- BR: s/tetex-latex/texlive-latex-base/

* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 1.0.1-alt2
- applied repocop patch

* Tue Aug 28 2007 Michael Shigorin <mike@altlinux.org> 1.0.1-alt1
- built for ALT Linux
- added rough sketch of a desktop file
  (borrowed/trimmed-down gimp's one)
- hardwired icon path with a band-aid patch to allow tint be
  run from any directory, not only build one
- buildreq
- NB: successful build requires fixed scons, 0.97-alt1 is broken

