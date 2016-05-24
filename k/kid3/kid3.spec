Name:		kid3
Version:	1.3
Release:	alt3

Group:		Sound
Summary:	Kid3 - Efficient ID3 tag editor
Url:		http://kid3.sourceforge.net/
License:	GPLv2+

Packager:	Motsyo Gennadi <drool@altlinux.ru>

Source0:	http://kent.dl.sourceforge.net/sourceforge/kid3/%name-%version.tar.gz
Patch0:		%name-1.3-desktopdir.diff
Patch1:		%name-1.3-alt_scalabledir.diff
Patch2:		%name-1.3-desktop_ru_uk.diff
Patch3:   %name-1.3-alt-DSO.patch

# Automatically added by buildreq on Tue May 05 2009 (-bi)
BuildRequires: gcc-c++ id3lib-devel imake kdelibs-devel libXt-devel libflac++-devel libmpeg4ip-devel libqt3-devel libtag-devel libtunepimp-devel xml-utils xorg-cf-files libvorbis-devel

%description
If you want to easily tag multiple MP3, Ogg/Vorbis, FLAC,
MPC, MP4/AAC, MP2, Speex, TrueAudio and WavPack files
(e.g. full albums) without typing the same information
again and again and have control over both ID3v1 and ID3v2
tags, then Kid3 is the program you are looking for.

With Kid3 you can:

- Edit ID3v1.1 tags
- Edit all ID3v2.3 and ID3v2.4 frames
- Convert between ID3v1.1, ID3v2.3 and ID3v2.4 tags
- Edit tags in MP3, Ogg/Vorbis, FLAC, MPC, MP4/AAC, MP2, Speex,
  TrueAudio and WavPack files.
- Edit tags of multiple files, e.g. the artist, album, year and genre
  of all files of an album typically have the same values and can be
  set together.
- Generate tags from filenames
- Generate filenames from tags
- Generate playlist files
- Automatic case conversion and string translation
- Import and export album data
- Import from gnudb.org, TrackType.org, MusicBrainz, Discogs

%package -n kde3-kid3
Group:		Sound
Summary:	Kid3 - Efficient ID3 tag editor
Provides: kid3 = %version-%release
Obsoletes: kid3 < %version-%release
%description -n kde3-kid3
If you want to easily tag multiple MP3, Ogg/Vorbis, FLAC,
MPC, MP4/AAC, MP2, Speex, TrueAudio and WavPack files
(e.g. full albums) without typing the same information
again and again and have control over both ID3v1 and ID3v2
tags, then Kid3 is the program you are looking for.

With Kid3 you can:

- Edit ID3v1.1 tags
- Edit all ID3v2.3 and ID3v2.4 frames
- Convert between ID3v1.1, ID3v2.3 and ID3v2.4 tags
- Edit tags in MP3, Ogg/Vorbis, FLAC, MPC, MP4/AAC, MP2, Speex,
  TrueAudio and WavPack files.
- Edit tags of multiple files, e.g. the artist, album, year and genre
  of all files of an album typically have the same values and can be
  set together.
- Generate tags from filenames
- Generate filenames from tags
- Generate playlist files
- Automatic case conversion and string translation
- Import and export album data
- Import from gnudb.org, TrackType.org, MusicBrainz, Discogs


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p2
sed -i -e 's|/lib /usr/lib\b|/%_lib %_libdir|g' configure # lib64 rpaths
sed -i -e 's|/usr/lib/|%_libdir/|g' configure

%build
%add_optflags -I%_includedir/tqtinterface
%K3configure
%make_build

%install
%K3install

%K3find_lang --with-kde %name

%files -n kde3-kid3 -f %name.lang
%doc AUTHORS ChangeLog
%_K3bindir/*
%_K3datadir/applications/*
%_kde3_iconsdir/hicolor/*/apps/*.*
%_K3datadir/apps/%name/*

%changelog
* Tue May 24 2016 Sergey V Turchin <zerg@altlinux.org> 1.3-alt3
- rename package

* Wed Jul 18 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt2.1
- Fixed build

* Fri Mar 04 2011 Timur Aitov <timonbl4@altlinux.org> 1.3-alt2
- move to alternate place

* Sun Nov 08 2009 Motsyo Gennadi <drool@altlinux.ru> 1.3-alt1
- 1.3

* Sat May 09 2009 Motsyo Gennadi <drool@altlinux.ru> 1.2-alt2
- fix build with gcc4.4

* Tue May 05 2009 Motsyo Gennadi <drool@altlinux.ru> 1.2-alt1
- packaged from scratch
