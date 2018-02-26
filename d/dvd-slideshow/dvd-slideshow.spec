Name: dvd-slideshow
Summary: Creates a standard DVD with menus from a list of images
%define MainVersion 0.8.2
%define MinorVersion 2
Version: %MainVersion.%MinorVersion
Release: alt1

Packager: Ildar Mulyukov <ildar@altlinux.ru>

Source: %name-%MainVersion-%MinorVersion.tar.gz
Url: http://dvd-slideshow.sourceforge.net
License: GPL2
Group: Graphics
BuildArch: noarch

Requires: sox dvdauthor lame ffmpeg
#Found by /usr/lib/rpm/find-requires:
#Requires: /bin/bash, /etc/bashrc, /usr/bin/flvtool2, GraphicsMagick-ImageMagick-compat, coreutils, ffmpeg, findutils, genisoimage, grep, lame, sed, sox-base, sudo, vcdimager, vorbis-tools
%add_findreq_skiplist %_bindir/*
Requires: /bin/bash /usr/bin/flvtool2 /usr/bin/composite /usr/bin/convert /usr/bin/identify coreutils findutils genisoimage grep lame sed vcdimager vorbis-tools


%description
DVD-slideshow makes a DVD slideshow video with menus from a batch of pictures.
It consists of a set of scripts:
* dvd-slideshow reads a text file list of all the pictures you want in one
  slideshow and creates a DVD-compatible MPEG movie with your audio track and
  specified timing.
* dvd-menu makes a top-level DVD menu with the output files from
  dvd-slideshow.
* gallery2slideshow makes the input file for dvd-slideshow from your Gallery
  album.
* jigl2slideshow makes the input file for dvd-slideshow from your jigl album.

NOTE: You'll need an ogg or mp2 or mp3 encoder if you wish to add audio.

%prep
%setup -n %name-%MainVersion-%MinorVersion

%install
mkdir -p %buildroot/{%_bindir,%_man1dir}
cp -a man/*.1 %buildroot/%_man1dir/
cp -a \
	dir2slideshow dvd-menu dvd-slideshow gallery1-to-slideshow jigl2slideshow \
	%buildroot/%_bindir/

%files
%doc TODO.txt doc/* dvd-slideshowrc
%_bindir/*
%_man1dir/*

%changelog
* Mon Oct 25 2010 Ildar Mulyukov <ildar@altlinux.ru> 0.8.2.2-alt1
- new version (closes: #24267)
- fix requires

* Wed Mar 21 2007 Alexey Morsov <swi@altlinux.ru> 0.8.0.1-alt1
- new version

* Thu Dec 21 2006 Alexey Morsov <swi@altlinux.ru> 0.7.5-alt1
- Add packager
- pack for sisyphus
- some fix in spec

* Sun Dec 17 2006 Motsyo Gennadi <drool@altlinux.ru> 0.7.5-alt0.M24.1
- packing for ALT Linux 2.4 Master

* Thu Mar 23 2006 Lenny Cartier <lenny@mandriva.com> 0.7.5-2mdk
- url

* Mon Mar 13 2006 Austin Acton <austin@mandriva.org> 0.7.5-1mdk
- New release 0.7.5

* Fri Jan 27 2006 Austin Acton <austin@mandriva.org> 0.7.4-1mdk
- New release 0.7.4

* Tue Jan 24 2006 Austin Acton <austin@mandriva.org> 0.7.3-1mdk
- New release 0.7.3

* Wed Nov 23 2005 Lenny Cartier <lenny@mandriva.com> 0.7.2-1mdk
- 0.7.2

* Fri Mar 4 2005 Austin Acton <austin@mandrake.org> 0.7.1-1mdk
- 0.7.1
- source URL
- move optional config file to docdir
- add manpages

* Fri Feb 18 2005 Austin Acton <austin@mandrake.org> 0.7.0-1mdk
- 0.7.0

* Sat May 15 2004 Austin Acton <austin@mandrake.org> 0.6.0-1mdk
- 0.6.0

* Mon Mar 1 2004 Austin Acton <austin@mandrake.org> 0.5.4-1mdk
- 0.5.4

* Mon Jan 26 2004 Austin Acton <austin@mandrake.org> 0.5.2-1mdk
- 0.5.2

* Mon Jan 19 2004 Austin Acton <austin@mandrake.org> 0.5.0-1mdk
- 0.5.0
- better URL
- dvd-mainmenu becomes dvd-menu

* Wed Jan 14 2004 Austin Acton <austin@mandrake.org> 0.4.8-1mdk
- 0.4.8
- noarch

* Thu Jan 8 2004 Austin Acton <austin@linux.ca> 0.4.6-1mdk
- initial package
