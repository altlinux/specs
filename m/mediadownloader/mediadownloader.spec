%define		_giconsdir %_iconsdir/hicolor/128x128/apps

%define		git 20110226

Version:	1.5.0
Name:		mediadownloader
Release:	alt0.1.%git.1
Summary:	Media Downloader
License: 	GPLv3+
Group: 		Graphics
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Url:		http://mediadownloader.cz.cc/
Source0:	http://kent.dl.sourceforge.net/project/googleimagedown/project/v1.4/%name-v%version-src.tar.bz2
Source1:	%name.desktop
Patch0:		%name-v1.4.1-alt_phonondir.diff

Provides:	googleimagedownloader
Obsoletes:	googleimagedownloader < 1.3

BuildRequires: ImageMagick-tools gcc-c++ libGL-devel libqt4-devel
BuildRequires: phonon-devel libGLU-devel libXtst-devel

%description
   Media Downloader (ex GoogleImageDownloader) is an opensource software
that lets you search, watch and download with Google Image and YouTube.
Search results are displayed within a mouse scrollable view, most likely
as mobile devices does. You will see thumbnails that are conform with your
search criteria, doubleclick to view, rightclick to popup a menu and
choose to download the single image or video, remove from global downloads
or browse the web page. Set an image as wallpaper is only supported on
Gnome, Kde 3.5 and windows.
   Choose which to remove and download them into a specific folder with
choosen naming.

%prep
%setup -q -n MediaDownloader
%patch0 -p1

%build
export PATH=$PATH:%_qt4dir/bin
lrelease translations/*.ts
qmake "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" "LIBS+= -lXtst" mediadownloader.pro
%make_build VERBOSE=1

%install
install -Dp -m 0755 bin/%name %buildroot%_bindir/%name
install -Dp -m 0644 %SOURCE1 %buildroot%_desktopdir/%name.desktop

# Icons
%__mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir,%_giconsdir}
install -m 0644 icons/%name.png %buildroot%_giconsdir/%name.png
convert -resize 48x48 icons/%name.png %buildroot%_liconsdir/%name.png
convert -resize 32x32 icons/%name.png %buildroot%_niconsdir/%name.png
convert -resize 16x16 icons/%name.png %buildroot%_miconsdir/%name.png

%files
%doc README.txt
%_bindir/%name
%_desktopdir/%name.desktop
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_giconsdir/%name.png

%changelog
* Tue Apr 26 2011 Motsyo Gennadi <drool@altlinux.ru> 1.5.0-alt0.1.20110226.1
- fix build

* Thu Apr 07 2011 Motsyo Gennadi <drool@altlinux.ru> 1.5.0-alt0.1.20110226
- 1.5.0 released
- git snapshot from 20110226

* Mon Jan 03 2011 Motsyo Gennadi <drool@altlinux.ru> 1.4.3-alt0.1.20101230
- git snapshot from 20101230

* Wed Dec 15 2010 Motsyo Gennadi <drool@altlinux.ru> 1.4.3-alt0.1.20101214
- git snapshot from 20101214

* Tue Dec 14 2010 Motsyo Gennadi <drool@altlinux.ru> 1.4.3-alt0.1.20101211
- git snapshot from 20101211

* Tue Nov 23 2010 Motsyo Gennadi <drool@altlinux.ru> 1.4.3-alt0.1.20101122
- git snapshot from 20101122
- 1.4.3 beta

* Fri Nov 12 2010 Motsyo Gennadi <drool@altlinux.ru> 1.4.2-alt0.1.20101105
- git snapshot from 20101105
- fix build (libGLU-devel)

* Sun Oct 24 2010 Motsyo Gennadi <drool@altlinux.ru> 1.4.2-alt0.1.20101024
+ 1.4.2 betalfa
- git snapshot from 20101024

* Wed Oct 13 2010 Motsyo Gennadi <drool@altlinux.ru> 1.4.1-alt0.1.20101012.1
- fix patch for new version

* Wed Oct 13 2010 Motsyo Gennadi <drool@altlinux.ru> 1.4.1-alt0.1.20101012
- git snapshot from 20101012
  + fix also for gcc 4.5.1

* Fri Oct 08 2010 Motsyo Gennadi <drool@altlinux.ru> 1.4.1-alt0.1.20101008
- git snapshot from 20101008
- updated Russian and Ukrainian translations

* Thu Sep 30 2010 Motsyo Gennadi <drool@altlinux.ru> 1.4.1-alt0.1.20100930
- v.1.4.1 pre
- git snapshot from 20100930

* Tue Sep 21 2010 Motsyo Gennadi <drool@altlinux.ru> 1.4-alt1.20100921
- git snapshot from 20100921

* Sun Sep 19 2010 Motsyo Gennadi <drool@altlinux.ru> 1.4-alt1.20100918
- git snapshot from 20100918
- fixed and updated Russian and Ukrainian translations

* Sat Sep 18 2010 Motsyo Gennadi <drool@altlinux.ru> 1.4-alt1
- 1.4 release
- updated Russian & Ukrainian translations

* Sun Jul 25 2010 Motsyo Gennadi <drool@altlinux.ru> 1.3.2-alt1.20100724.3
- bugfix when closing zoomed image while downloading

* Sat Jul 24 2010 Motsyo Gennadi <drool@altlinux.ru> 1.3.2-alt1.20100724
- 1.3.2 (git snapshot from 20100724)

* Thu Jul 01 2010 Motsyo Gennadi <drool@altlinux.ru> 1.3-alt2
- git snapshot from 20100701
  + fixed regexp for video download

* Thu Jul 01 2010 Motsyo Gennadi <drool@altlinux.ru> 1.3-alt1
- 1.3 release

* Mon Jun 28 2010 Motsyo Gennadi <drool@altlinux.ru> 1.3-alt0.1.20100627
- git snapshot from 20100627

* Sun Jun 20 2010 Motsyo Gennadi <drool@altlinux.ru> 1.2.3.1-alt1.20100617
- git snapshot from 20100617
- renaming
- fixed and updated Ukrainian & Russian translations

* Fri Jun 11 2010 Motsyo Gennadi <drool@altlinux.ru> 1.2.3.1-alt1.20100610
- git snapshot from 20100610

* Sat May 22 2010 Motsyo Gennadi <drool@altlinux.ru> 1.2.3.1-alt1.20100519
- git snapshot from 20100519

* Tue May 11 2010 Motsyo Gennadi <drool@altlinux.ru> 1.2.3-alt1.20100506
- 1.2.3
  + fixed Safe Search parameter

* Tue Apr 13 2010 Motsyo Gennadi <drool@altlinux.ru> 1.2.2-alt1
- 1.2.2
- change Url to sf.net

* Mon Apr 12 2010 Motsyo Gennadi <drool@altlinux.ru> 1.2.1.1-alt1.20100412
- git snapshot from 20100412

* Sun Apr 11 2010 Motsyo Gennadi <drool@altlinux.ru> 1.2.1.1-alt1.20100411
- git snapshot from 20100411 + updated & fixed Russian and Ukrainian translations

* Fri Apr 09 2010 Motsyo Gennadi <drool@altlinux.ru> 1.2.1.1-alt1.20100408
- git snapshot from 20100408
  + Russian, Ukrainian, Italian translations. Button to hide top

* Thu Apr 01 2010 Motsyo Gennadi <drool@altlinux.ru> 1.2.1.1-alt1.20100401
- git snapshot from 20100401
  + fix n.2 cyrillic chars on pixmap description

* Wed Mar 31 2010 Motsyo Gennadi <drool@altlinux.ru> 1.2.1.1-alt1.20100331
- git snapshot from 20100331

* Mon Mar 29 2010 Motsyo Gennadi <drool@altlinux.ru> 1.2.1.1-alt1.20100320.1
- removed external app icon (upstream added)

* Mon Mar 29 2010 Motsyo Gennadi <drool@altlinux.ru> 1.2.1.1-alt1.20100320
- git snapshot from 20100320:
  + fixed non-english chars search
  + set background in gnome, kde3, windows with context menu

* Sun Mar 07 2010 Motsyo Gennadi <drool@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Tue Feb 16 2010 Motsyo Gennadi <drool@altlinux.ru> 1.2-alt0.2.20100215
- new git snapshot

* Sun Feb 14 2010 Motsyo Gennadi <drool@altlinux.ru> 1.2-alt0.2.20100214
- new git snapshot

* Sat Feb 06 2010 Motsyo Gennadi <drool@altlinux.ru> 1.1-alt1
- initial build for ALT Linux
