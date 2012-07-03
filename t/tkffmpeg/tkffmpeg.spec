BuildRequires: desktop-file-utils
%define		_giconsdir %_iconsdir/hicolor/128x128/apps
%define		_24iconsdir %_iconsdir/hicolor/24x24/apps

%define		svn svn74

Summary:	FFmpeg video converter GUI
Summary(ru_RU.UTF8): Графический видеоконвертер на FFmpeg
Summary(uk_UA.UTF8): Графічний відеоконвертер на FFmpeg
Name:		tkffmpeg
Version:	0.0.81
Release:	alt0.1.%svn.qa1
License:	GPLv2
Group:		Video
Url:		http://tkffmpeg.sourceforge.net/
Source0:	%name-%svn.tar.bz2
Packager:	Motsyo Gennadi <drool@altlinux.ru>

Requires:	tk ffmpeg dvdauthor dvd+rw-tools tcl-img

BuildArch:	noarch

BuildRequires:	/usr/bin/convert

%description
This is a small FFmpeg GUI for video converting, based on Tk/Tcl

%description -l ru_RU.UTF8
Небольшой GUI для FFmpeg для конвертирования видео, основанный на Tk/Tcl

%description -l uk_UA.UTF8
Невеличкий GUI для FFmpeg для конвертування відео, оснований на Tk/Tcl

%prep
%setup -q -n %name-svn

%install
install -Dp -m 0755 %name %buildroot%_bindir/%name
install -Dp -m 0755 %name.tcl %buildroot%_datadir/%name/%name.tcl
install -Dp -m 0755 tray.tcl %buildroot%_datadir/%name/tray.tcl
install -Dp -m 0644 %name.desktop %buildroot%_desktopdir/%name.desktop

# langs
mkdir -p %buildroot%_datadir/%name
install -m 0644 default.ini %buildroot%_datadir/%name/default.ini
cp -r language %buildroot%_datadir/%name/

# Icons
mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir,%_giconsdir,%_24iconsdir}
install -m 0644 %name.png %buildroot%_giconsdir/%name.png
convert -resize 48x48 %name.png %buildroot%_liconsdir/%name.png
convert -resize 32x32 %name.png %buildroot%_niconsdir/%name.png
convert -resize 24x24 %name.png %buildroot%_24iconsdir/%name.png
convert -resize 16x16 %name.png %buildroot%_miconsdir/%name.png

ln -s %_miconsdir/%name.png %buildroot%_datadir/%name/%{name}16.png
ln -s %_24iconsdir/%name.png %buildroot%_datadir/%name/%{name}24.png
ln -s %_giconsdir/%name.png %buildroot%_datadir/%name/%name.png
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Video \
	--add-category=AudioVideoEditing \
	%buildroot%_desktopdir/tkffmpeg.desktop

%files
%dir %_datadir/%name
%dir %_datadir/%name/language
%doc README* AUTHORS Release.txt Change.log
%_bindir/*
%_datadir/%name/language/*.lng
%_datadir/%name/*.*
%_desktopdir/%name.desktop
%_miconsdir/%name.png
%_niconsdir/%name.png
%_24iconsdir/%name.png
%_liconsdir/%name.png
%_giconsdir/%name.png

%changelog
* Tue Jun 07 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.0.81-alt0.1.svn74.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for tkffmpeg
  * postclean-03-private-rpm-macros for the spec file

* Fri May 06 2011 Motsyo Gennadi <drool@altlinux.ru> 0.0.81-alt0.1.svn74
- svn74
  + 0.0.81 released

* Fri May 28 2010 Motsyo Gennadi <drool@altlinux.ru> 0.0.80-alt0.1.svn67.1
- fixed tktray support

* Thu May 27 2010 Motsyo Gennadi <drool@altlinux.ru> 0.0.80-alt0.1.svn67
- svn67
  + Added tray icon support
  + Changed icons
  + Create tkffmpeg files
  + Optimize programm code
  + Added "Copy" for audio and video codecs

* Sun Apr 18 2010 Motsyo Gennadi <drool@altlinux.ru> 0.0.77-alt0.1.svn55
- svn55
  + change icon + 128x128 size

* Thu Apr 08 2010 Motsyo Gennadi <drool@altlinux.ru> 0.0.77-alt0.1.svn54
- svn54

* Wed Feb 17 2010 Motsyo Gennadi <drool@altlinux.ru> 0.0.76-alt0.1.svn51
- svn51

* Thu Oct 15 2009 Motsyo Gennadi <drool@altlinux.ru> 0.0.68-alt0.1.svn47
- svn47:
  + add about file info
  + some changes

* Wed Aug 05 2009 Motsyo Gennadi <drool@altlinux.ru> 0.0.68-alt0.1.svn45
- svn44:
  + updated Change.log
  + updated spec-file for ALT Linux

* Mon Jul 13 2009 Motsyo Gennadi <drool@altlinux.ru> 0.0.68-alt0.1.svn43
- svn43:
  + fixed progress error

* Mon Jul 13 2009 Motsyo Gennadi <drool@altlinux.ru> 0.0.68-alt0.1.svn42
- svn42:
  + 0.0.68
  + Increased speed of execution of the program

* Thu Jul 09 2009 Motsyo Gennadi <drool@altlinux.ru> 0.0.67-alt0.1.svn41
- new svn41

* Mon Jun 29 2009 Motsyo Gennadi <drool@altlinux.ru> 0.0.67-alt0.1.svn38
- svn38:
  + 0.0.67
  + Add "Abort" button
  + Add progress bar
  + Optimize programm code
  + updated Russian adn Ukrainian translations

* Sat Jun 27 2009 Motsyo Gennadi <drool@altlinux.ru> 0.0.65-alt0.1.svn33
- svn33:
  + update readme
  + 0.0.65
  + added VideoDVD creation
  + updated English, Russian and Ukrainian translation

* Mon Jun 22 2009 Motsyo Gennadi <drool@altlinux.ru> 0.0.62-alt0.1.svn26
- svn26:
  + Change pid value
  + Change theme color

* Fri Jun 19 2009 Motsyo Gennadi <drool@altlinux.ru> 0.0.62-alt0.1.svn25
- svn25:
  + 0.0.62
  + Change kill error

* Fri Jun 19 2009 Motsyo Gennadi <drool@altlinux.ru> 0.0.61-alt0.1.svn24
- svn24:
  + added Ukrainian translation

* Thu Jun 18 2009 Motsyo Gennadi <drool@altlinux.ru> 0.0.61-alt0.1.svn23
- svn23:
  + 0.0.61
  + Change language pack
  + Change combobox error
  + Change Tk theme
  + Change Frame style
  + Add clear log window

* Wed Jun 17 2009 Motsyo Gennadi <drool@altlinux.ru> 0.0.6-alt0.1.svn21
- svn21:
  + 0.0.6
  + Change error if dirname with space
  + Add default.ini
  + Add advanced options window
  + Add multi-language
  + Add Russian language
  + Add verifying real media player programm
  + Optimize program code
  + add scritp for remove svn tags

* Sun Jun 14 2009 Motsyo Gennadi <drool@altlinux.ru> 0.0.5-alt0.1.svn10
- svn10:
  + fixed spec-file
  + fixed Release tag in spec-file for svn version
  + fixed changelog in spec-file
  + Change kill error
  + Change OutputFile Open error
  + Change small "k"
  + Change -y key

* Sat Jun 13 2009 Motsyo Gennadi <drool@altlinux.ru> 0.0.5-alt0.1.svn3
- initial build for ALT Linux svn3:
  + 0.0.5
  + changed version from 0.05 to 0.0.5
  + added README text
  + added AUTHORS text
  + added text of the LICENSE
  + added desktop-file
  + added spec-file (for ALT Linux)
