Name:		smplayer-skins
Version:	 15.2.0
Release:	alt2
Summary:	Skins for SMPlayer
License:	GPLv2
Group:		Video
Url:		http://smplayer.sourceforge.net/

Source0:	%name-%version.tar.bz2

BuildArch:	noarch

%description
This package provides skin themes for SMPlayer.
SMPlayer is a graphical user interface (GUI) for the award-winning mplayer
and also for mpv. But apart from providing access for the most common
and useful options of mplayer and mpv, SMPlayer adds other interesting features
like the possibility to play Youtube videos or search and download subtitles.
One of the main features is the ability to remember the state of a
played file, so when you play it later it will be resumed at the same point
and with the same settings.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/smplayer/themes
ls -1 themes/*/main.css | \
while read f ; do
    cp -ar `dirname $f` %buildroot/%_datadir/smplayer/themes/
done

%files
%_datadir/smplayer/themes/*

%changelog
* Fri Nov 27 2015 Sergey V Turchin <zerg@altlinux.org> 15.2.0-alt2
- don't require smplayer (ALT#31519)

* Thu Jun 11 2015 Motsyo Gennadi <drool@altlinux.ru> 15.2.0-alt1
- initial build for ALT Linux
