Name: xvidcap
Version: 1.1.7
Release: alt11

Summary: xvidcap is a screen capture tool
Group: Video
License: GPL

Url: http://sourceforge.net/projects/xvidcap/
Source: http://prdownloads.sourceforge.net/%name/%name-%version.tar.gz
Patch0: xvidcap-1.1.7-alt-headers.patch
Patch1: xvidcap-1.1.7-alt-freedesktop.patch
Patch2: xvidcap-1.1.7-alt-configure.patch
Patch3: xvidcap-1.1.7-alt-build.patch
Patch4: xvidcap-1.1.7-alt-libav.patch

Packager: Sergey Kurakin <kurakin@altlinux.org>

Requires: dbus-tools-gui

#BuildRequires: db2latex-xsl libICE-devel perl-XML-Parser libavutil-devel
BuildRequires: ImageMagick-tools docbook2X gnome-doc-utils libXdamage-devel libXext-devel libXmu-devel libavdevice-devel libavformat-devel libdbus-glib-devel libglade-devel liblame-devel libswscale-devel libtheora-devel

Obsoletes: xvidcap-common <= 1.1.3

%description 
xvidcap is a screen capture enabling to capture videos off X-Window
desktop for illustration or documentation purposes. It is intended to be
a standards-based alternative to tools like Lotus ScreenCam.

It is recommended to install mplayer package for instant review.

%prep
%setup -q -n %name-%version
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p2
%patch4 -p2

%build
%autoreconf
%configure --enable-libmp3lame --enable-libtheora --without-forced-embedded-ffmpeg
%make_build

%install
%makeinstall
rm -rf %buildroot%_docdir/%name
rm -rf %buildroot%_mandir/??
mkdir -p %buildroot{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 16x16 %buildroot%_datadir/pixmaps/%name.png %buildroot%_miconsdir/%name.png
convert -resize 32x32 %buildroot%_datadir/pixmaps/%name.png %buildroot%_niconsdir/%name.png
convert -resize 48x48 %buildroot%_datadir/pixmaps/%name.png %buildroot%_liconsdir/%name.png
%find_lang %name --with-gnome

%files -f %name.lang
%_bindir/*
%_man1dir/*
%_desktopdir/%name.desktop
%_datadir/gnome/help/%name/
%_datadir/omf/%name/
%_pixmapsdir/%name.png
%_datadir/%name/
%_datadir/dbus-1/services/*
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%doc AUTHORS ChangeLog NEWS README

%changelog
* Sat Jun  2 2012 Sergey Kurakin <kurakin@altlinux.org> 1.1.7-alt11
- fixed build (-lX11)
- build with system libav instead of bundled ffmpeg

* Fri Apr 13 2012 Sergey Kurakin <kurakin@altlinux.org> 1.1.7-alt10
- build fixed

* Sun Apr 11 2010 Sergey Kurakin <kurakin@altlinux.org> 1.1.7-alt9
- fixed build with new xorg

* Thu Mar 18 2010 Sergey Kurakin <kurakin@altlinux.org> 1.1.7-alt8
- find lang with gnome (fix repocop issue)

* Sun Apr 19 2009 Sergey Kurakin <kurakin@altlinux.org> 1.1.7-alt7
- build with bundled ffmpeg to restore audio support
  (dropped build with system ffmpeg, featured in 1.1.7-alt1)

* Wed Apr  1 2009 Sergey Kurakin <kurakin@altlinux.org> 1.1.7-alt6
- fixed audio support with current ffmpeg

* Fri Mar 27 2009 Sergey Kurakin <kurakin@altlinux.org> 1.1.7-alt5
- fixed build (buildreq)
- build with current ffmpeg

* Mon Dec 01 2008 Michael Shigorin <mike@altlinux.org> 1.1.7-alt4
- fixed build (buildreq)

* Sun Nov 16 2008 Sergey Kurakin <kurakin@altlinux.org> 1.1.7-alt3
- post-scripts removed (menus)

* Fri Sep 26 2008 Sergey Kurakin <kurakin@altlinux.ru> 1.1.7-alt2
- fixed repocop issues (iconsdir, freedesktop-categories,
  freedesktop-desktop)

* Sat Sep 20 2008 Sergey Kurakin <kurakin@altlinux.ru> 1.1.7-alt1
- 1.1.7:
  + capture area follows mouse feature
  + xvidcap-dbus-client -- remote control utility for XVidCap
- build with system ffmpeg instead of embedded one
- Url fixed (http://xvidcap.sourceforge.net is obsolete)

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 1.1.6-alt2.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for xvidcap

* Tue Jan 29 2008 Michael Shigorin <mike@altlinux.org> 1.1.6-alt2
- added Obsoletes: xvidcap-common

* Sun Jun 03 2007 Michael Shigorin <mike@altlinux.org> 1.1.6-alt1
- 1.1.6:
  + fixed couple bugs
  + added basic minimize to tray support
  + russian/chinese translations
  + theora and vorbis supported (in AVI)
- added missing include (thanks thresh@ for a hint)
- updated buildrequires (thus fixed build; thanks led@ and
  ruslandh@ for bothering to run buildreq on their systems
  to collect overlapping but different deps, in particular,
  xdamage support seems to have had no chance to work in
  previous build due to missing headers during build)

* Wed Apr 25 2007 Michael Shigorin <mike@altlinux.org> 1.1.5-alt1
- 1.1.5:
  + xdamage support for speed
  + real mouse pointer capture
  + direct capture to SWF with sound (again)
  + ability to resize the capture area by dragging
  + displays the capture area dimensions on resize
  + various bugfixes

* Sun Jan 28 2007 Michael Shigorin <mike@altlinux.org> 1.1.4-alt1.1
- 1.1.4p1

* Tue Oct 17 2006 Michael Shigorin <mike@altlinux.org> 1.1.4-alt0.92
- 1.1.4rc2
- added Packager:
- added missing BuildRequires:
- removed subpackages (gvidcap is no more, xvidcap is everything now)
- removed packaged icon in favour of tarball one
- removed translated manpages for now
- removed Debian menu
- spec cleanup

* Wed Sep 27 2006 Michael Shigorin <mike@altlinux.org> 1.1.4-alt0.3
- 1.1.4-pre3
- patches removed
- added raorn's configure subst hack
- thanks wrar@ for help with wrestling brea^Wlinkage

* Wed Sep 27 2006 Michael Shigorin <mike@altlinux.org> 1.1.3-alt0.3
- adopted an orphan
- applied gentoo patches (1..3)
- macro abuse cleanup

* Sun Aug 22 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.1.3-alt0.2
- rebuild against current ffmpeg (close #5038).

* Tue Feb 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.1.3-alt0.1
- 1.1.3

* Mon Dec 15 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.1.1-alt0.1
- 1.1.1

* Thu Nov 13 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.1.0-alt0.1
- new version.
- gvidcap, xvidcap-common subpackages.

* Fri Oct 31 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.19-alt0.1
- First build for Sisyphus
