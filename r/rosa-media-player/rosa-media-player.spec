Name:		rosa-media-player
Version:	1.5.1.4
Release:	alt1
Summary:	Multimedia player based on mplayer technology

License:	GPLv2+
Group:		Video
Url:		https://abf.rosalinux.ru/uxteam/ROSA_Media_Player/tree/develop
Source:		%name-%version.tar.gz
Packager:   Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre):	qt4-devel >= 4.2.0
BuildRequires:  libwildmidi-devel
BuildRequires:	libalsa-devel
BuildRequires:  gcc-c++ kdelibs zlib-devel

Requires:	mplayer >= 1.0
Requires:	mencoder
Requires:	ffmpeg
Requires:	xdg-utils

%description
Rosa Media Player (ROMP) - multimedia player that supports most of audio
and video formats such as Audio CD, DVD, Video CD, multimedia files in
AVi, ASF/WMV/WMA, MOV/MP4, RealMedia, Ogg Vorbis, NUT, NSV, VIVO, FLI,
NuppelVideo, yuv4mpeg, FILM (.cpk), RoQ, PVA and Matroska  formats
recorded with video codecs - DivX , MPEG-1, MPEG-2, MPEG-4, Sorenson,
WMV, RealVideo, x264 and audio codecs MP3, Musepack, Vorbis, RealAudio,
AC3/A52 (Dolby Digital), AAC (MPEG-4 audio), QuickTime, VIVO audio and
WMA and many other less widespread video and audio codecs. It also
supports streaming via HTTP/FTP, RTP/RTSP, MMS/MMST, MPST, SDP, capture
and record (via mencoder) of television signal. ROMP allows you to trim
a particular piece of video, extract audio from multimedia files and
record screen presentations and many other things.

%prep
%setup -q -n %name

%build
./get_romp_version.sh %version 1
make QMAKE=%_qt4dir/bin/qmake LRELEASE=%_qt4dir/bin/lrelease

%install
%makeinstall_std PREFIX=%_prefix

# remove wrongly put docs
rm -rf %buildroot%_datadir/doc

# strip binary
strip %buildroot%_bindir/%name

%files
%doc Copying.txt
%attr(755,root,root) %_bindir/%name
%_datadir/%name
%_iconsdir/hicolor/*/apps/rosamp.png
%_desktopdir/*.desktop

%changelog
* Wed Jan 23 2013 Andrey Cherepanov <cas@altlinux.org> 1.5.1.4-alt1
- New version 1.5.1-4

* Tue Jan 01 2013 Andrey Cherepanov <cas@altlinux.org> 1.5-alt2
- Build in Sisyphus (ALT #27485)

* Mon Aug 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_1
- new release

