%define		_biconsdir %_iconsdir/hicolor/64x64/apps

%define		_gmimedir %_iconsdir/hicolor/128x128/mimetypes
%define		_bmimedir %_iconsdir/hicolor/64x64/mimetypes
%define		_lmimedir %_iconsdir/hicolor/48x48/mimetypes
%define		_nmimedir %_iconsdir/hicolor/32x32/mimetypes
%define		_mmimedir %_iconsdir/hicolor/16x16/mimetypes

Summary:	Qt Easy Video Encoder
Name:		qeven
Version:	0.3.2
Release:	alt1
Packager:	Motsyo Gennadi <drool@altlinux.ru>
License:	GPLv3
Group:		Video
Url:		http://qt-apps.org/content/show.php/QEVEN?content=108799
Source0:	%{name}_%{version}.tar.bz2
Source1:	application-vnd.qeven.png
Source2:	qeven.desktop
Source3:	qeven.xml

Requires:	mplayer mencoder

BuildRequires:	/usr/bin/convert gcc-c++ libqt4-devel

%description
"Qt Easy Video Encoder"(QEVEN) allows to encode for several
video format (VCD,DVD,SVCD,DIVX,XVID,FLV). It was develop using Qt4 and C++.
Use MEncoder and MPlayer.

%prep
%setup -n %{name}_%{version}

%build
export PATH=$PATH:%_qt4dir/bin
qmake "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" "PREFIX=%prefix"
%make_build

%install
install -Dp -m 0755 QEVEN %buildroot%_bindir/%name
install -Dp -m 0644 %SOURCE2 %buildroot%_desktopdir/%name.desktop
mkdir -p %buildroot%_datadir/%name/translation
cp translation/*.qm %buildroot%_datadir/%name/translation/

# Icons
install -Dp -m 0644 Image/"qeven(64x64).png" %buildroot%_biconsdir/%name.png
mkdir -p %buildroot{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 48x48 Image/"qeven(64x64).png" %buildroot%_liconsdir/%name.png
convert -resize 32x32 Image/"qeven(64x64).png" %buildroot%_niconsdir/%name.png
convert -resize 16x16 Image/"qeven(64x64).png" %buildroot%_miconsdir/%name.png

# Mime types
install -Dp -m 0644 %SOURCE3 %buildroot%_datadir/mime/packages/%name.xml
install -Dp -m 0644 %SOURCE1 %buildroot%_gmimedir/application-vnd.qeven.png
mkdir -p %buildroot{%_bmimedir,%_lmimedir,%_nmimedir,%_mmimedir}
convert -resize 64x64 %SOURCE1 %buildroot%_bmimedir/application-vnd.qeven.png
convert -resize 48x48 %SOURCE1 %buildroot%_lmimedir/application-vnd.qeven.png
convert -resize 32x32 %SOURCE1 %buildroot%_nmimedir/application-vnd.qeven.png
convert -resize 16x16 %SOURCE1 %buildroot%_mmimedir/application-vnd.qeven.png

%files
%dir %_datadir/%name
%dir %_datadir/%name/translation
%_bindir/*
%_desktopdir/*.desktop
%_datadir/%name/translation/*.qm
%_datadir/mime/packages/*.xml
%_biconsdir/%name.png
%_liconsdir/%name.png
%_niconsdir/%name.png
%_miconsdir/%name.png

%_gmimedir/*.png
%_bmimedir/*.png
%_lmimedir/*.png
%_nmimedir/*.png
%_mmimedir/*.png

%changelog
* Sat Aug 20 2011 Motsyo Gennadi <drool@altlinux.ru> 0.3.2-alt1
- initial build for ALT Linux
