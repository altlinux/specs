%define lcname recordmydesktop
%define ucname recordMyDesktop

Name: %lcname-gtk
Version: 0.3.8
Release: alt2.1

Summary: Gtk frontend for recordmydesktop, screencasting program
Group: Video
License: GPLv2+
Url: http://sourceforge.net/projects/recordmydesktop/

Packager: Sergey Kurakin <kurakin@altlinux.org>

Source: gtk-%lcname-%version.tar.gz
Patch1: %name-0.3.7.2-alt-freedesktop.patch
Patch2: %name-0.3.8-alt-x86_64-build.patch
Patch3: %name-0.3.8-jack_lsp.patch

BuildPreReq: python-module-pygtk-devel >= 2.0
Requires: %lcname >= %version xwininfo

# Automatically added by buildreq on Mon Sep 22 2008 (-bi)
BuildRequires: python-devel ImageMagick

%description 
Gtk frontend for recordMyDesktop, screencasting program
that captures audio-video data of a linux desktop session,
producing an ogg-encapsulated theora-vorbis file.

%prep
%setup -q -n gtk-%lcname-%version
%patch1 -p1
%patch2 -p0
%patch3 -p1

%build
%configure
%make_build
convert -resize 16x16 src/gtk-%lcname.png gtk-%lcname-16.png
convert -resize 32x32 src/gtk-%lcname.png gtk-%lcname-32.png
convert -resize 48x48 src/gtk-%lcname.png gtk-%lcname-48.png

%install
%makeinstall
install -D -m 644 gtk-%lcname-16.png %buildroot%_miconsdir/gtk-%lcname.png
install -D -m 644 gtk-%lcname-32.png %buildroot%_niconsdir/gtk-%lcname.png
install -D -m 644 gtk-%lcname-48.png %buildroot%_liconsdir/gtk-%lcname.png
install -D -m 644 src/gtk-%lcname.svg %buildroot%_iconsdir/hicolor/scalable/apps/gtk-%lcname.svg
%find_lang gtk-%ucname

%files -f gtk-%ucname.lang
%_bindir/gtk-%ucname
%python_sitelibdir/%ucname/
%_desktopdir/gtk-%lcname.desktop
%_datadir/pixmaps/gtk-%lcname.png
%_miconsdir/gtk-%lcname.png
%_niconsdir/gtk-%lcname.png
%_liconsdir/gtk-%lcname.png
%_iconsdir/hicolor/scalable/apps/gtk-%lcname.svg
%doc AUTHORS ChangeLog NEWS README

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.8-alt2.1
- Rebuild with Python-2.7

* Fri Mar  5 2010 Sergey Kurakin <kurakin@altlinux.org> 0.3.8-alt2
- fixed x86_64 build
- fixed Advanced configuration dialog to working properly
  without jack installed, patch from Debian (LP #447011)
- fixed Select Window feature, xwininfo required

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.8-alt1.1
- Rebuilt with python 2.6

* Thu Dec  4 2008 Sergey Kurakin <kurakin@altlinux.org> 0.3.8-alt1
- 0.3.8 (mostly bugfix release)

* Thu Nov 20 2008 Sergey Kurakin <kurakin@altlinux.org> 0.3.7.2-alt3
- post-scripts removed (menus)
- fixed misprint in .desktop file

* Fri Sep 26 2008 Sergey Kurakin <kurakin@altlinux.ru> 0.3.7.2-alt2
- fixed repocop issues (iconsdir, freedesktop-desktop)

* Mon Sep 22 2008 Sergey Kurakin <kurakin@altlinux.ru> 0.3.7.2-alt1
- initial build for AltLinux Sisyphus
