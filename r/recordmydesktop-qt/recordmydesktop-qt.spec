%define lcname recordmydesktop
%define ucname recordMyDesktop

Name: %lcname-qt
Version: 0.3.8
Release: alt2.1

Summary: qt frontend for recordmydesktop, screencasting program
Group: Video
License: GPLv3+ & LGPLv3+
Url: http://sourceforge.net/projects/recordmydesktop/

Packager: Sergey Kurakin <kurakin@altlinux.org>

Source: qt-%lcname-%version.tar.gz
Patch1: %name-0.3.7.2-alt-freedesktop.patch
Patch2: %name-0.3.8-alt-x86_64-build.patch
Patch3: %name-0.3.8-alt-jack_lsp.patch

BuildPreReq: libqt4-devel >= 4.2
Requires: %lcname >= %version xwininfo

# Automatically added by buildreq on Thu Mar 04 2010 (-bi)
BuildRequires: ImageMagick-tools python-module-PyQt4

%description 
Qt frontend for recordMyDesktop, screencasting program
that captures audio-video data of a linux desktop session,
producing an ogg-encapsulated theora-vorbis file.

%prep
%setup -q -n qt-%lcname-%version
%patch1 -p1
%patch2 -p0
%patch3 -p0

%build
%configure
%make_build
convert -resize 16x16 src/qt-%lcname.png qt-%lcname-16.png
convert -resize 32x32 src/qt-%lcname.png qt-%lcname-32.png
convert -resize 48x48 src/qt-%lcname.png qt-%lcname-48.png

%install
%makeinstall
install -D -m 644 qt-%lcname-16.png %buildroot%_miconsdir/qt-%lcname.png
install -D -m 644 qt-%lcname-32.png %buildroot%_niconsdir/qt-%lcname.png
install -D -m 644 qt-%lcname-48.png %buildroot%_liconsdir/qt-%lcname.png
install -D -m 644 src/qt-%lcname.svg %buildroot%_iconsdir/hicolor/scalable/apps/qt-%lcname.svg
%find_lang qt-%ucname

%files -f qt-%ucname.lang
%_bindir/*
%python_sitelibdir/qt_%ucname/*
%_desktopdir/qt-%lcname.desktop
%_datadir/pixmaps/*
%_miconsdir/qt-%lcname.png
%_niconsdir/qt-%lcname.png
%_liconsdir/qt-%lcname.png
%_iconsdir/hicolor/scalable/apps/qt-%lcname.svg
%doc AUTHORS ChangeLog NEWS README

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.8-alt2.1
- Rebuild with Python-2.7

* Fri Mar  5 2010 Sergey Kurakin <kurakin@altlinux.org> 0.3.8-alt2
- fixed x86_64 build
- fixed Advanced configuration dialog to working properly
  without jack installed. Based on Debian patch for recordmydesktop-gtk
  (LP #447011)
- fixed Select Window feature, xwininfo required

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.8-alt1.1
- Rebuilt with python 2.6

* Thu Dec  4 2008 Sergey Kurakin <kurakin@altlinux.org> 0.3.8-alt1
- 0.3.8 (mostly bugfix release)
- license changed: GPLv3+ (the program itself) and LGPLv3+ (icons theme)

* Sun Nov 16 2008 Sergey Kurakin <kurakin@altlinux.org> 0.3.7.2-alt3
- post-scripts removed (menus)

* Fri Sep 26 2008 Sergey Kurakin <kurakin@altlinux.ru> 0.3.7.2-alt2
- fixed repocop issues (iconsdir, freedesktop-desktop)

* Mon Sep 22 2008 Sergey Kurakin <kurakin@altlinux.ru> 0.3.7.2-alt1
- initial build for AltLinux Sisyphus
