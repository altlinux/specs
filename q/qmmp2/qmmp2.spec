%add_findreq_skiplist %_datadir/qmmp/scripts/*.sh

%define major 2
%define sover 2
%define libqmmp libqmmp%sover
%define libqmmpui libqmmpui%sover

%define rname qmmp
Name: qmmp%major
Version: 2.1.5
Release: alt1
Epoch: 1
%K5init no_altplace appdata

Group: Sound
Summary: Qmmp - Qt-based multimedia player
Url: http://qmmp.ylsoftware.com/
License: GPL-2.0

Source: %rname-%version.tar
Patch2: alt-def-plugins.patch
Patch3: alt-def-statusicon.patch
Patch4: alt-hide-on-close.patch
Patch5: alt-def-id3v1-encoding.patch

BuildRequires(pre): rpm-build-kf5 rpm-build-wlskins
BuildRequires: cmake doxygen qt6-tools-devel qt6-multimedia-devel
BuildRequires: libmms-devel libtag-devel
%ifnarch %arm
BuildRequires: projectm-devel
%endif
BuildRequires: libalsa-devel libjack-devel libpulseaudio-devel pipewire-libs-devel
BuildRequires: libbs2b-devel libcddb-devel libcdio-paranoia-devel libcurl-devel libenca-devel
BuildRequires: libavformat-devel libwildmidi-devel
BuildRequires: libfaad-devel libflac-devel libgme-devel libopusfile-devel libsamplerate-devel libsoxr-devel
BuildRequires: libmad-devel libmpg123-devel
BuildRequires: libmodplug-devel libvorbis-devel libwavpack-devel
BuildRequires: libshout2-devel
#BuildRequires: libmpcdec0-devel
#BuildRequires: libarchive-devel
#BuildRequires: libsidplayfp-devel

%description
Qmmp is an audio-player, written with help of Qt library.
The user interface is similar to winamp or xmms.

Supported formats:
- MPEG1 layer 2/3
- Ogg Vorbis
- Opus
- Native FLAC, Ogg FLAC
- Musepack
- WavePack
- tracker modules (mod, s3m, it, xm, etc)
- ADTS AAC
- CD Audio
- WMA, Monkey's Audio (and other formats provided by FFmpeg library)
- PCM WAVE (and other formats provided by libsndfile library)
- midi
- chiptune formats (AY, GBS, GYM, HES, KSS, NSF, NSFE, SAP, SPC, VGM, VGZ, VTX)

DSP effects:
- BS2B effect
- sample rate converter
- LADSPA effects
- extra stereo
- crossfade (Experimental)

Visual effects:
- projectM visualization
- spectrum analyzer

Output system support:
- OSS
- ALSA (Linux)
- Pulse Audio
- JACK
- WaveOut (Win32)

Other features:
- XMMS and Winamp 2.x skins support
- 10-band equalizer
- MP3, Vorbis, AAC, AAC+ streams support
- mms support
- MPRIS (1.0 and 2.0)
- removable device detection (via HAL or UDisks)
- video playback via Mplayer
- lyrics (using lyrics.wikia.com)
- cover art support
- CUE sheet support
- embedded CUE support (for FLAC and WavPack)
- multiple playlists
- automatic charset detection for cue files and ShoutCast metadata
- playlist formats: m3u, pls, xspf
- ReplayGain support
- Last.fm/Libre.fm scrobbler
- CDDB support

%package -n qmmp
Group: Sound
Summary: Qmmp - Qt-based multimedia player
Requires: unzip winamplike-skins
%description -n qmmp
%{description}

%package devel
Summary: Qmmp header files
Group: Development/C++
Provides: qmmp-devel = %version-%release libqmmp-devel = %version-%release
Obsoletes: qmmp-devel < %version-%release libqmmp-devel < %version-%release
%description devel
%name-devel contains the header files needed to develop
programs which make use of Qmmp.

%package -n %libqmmp
Summary: Qmmp library
Group: System/Libraries
%description -n %libqmmp
Qmmp Shared library

%package -n %libqmmpui
Summary: Qmmp library
Group: System/Libraries
%description -n %libqmmpui
Qmmp Shared library

%prep
%setup -n %rname-%version
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%K5build \
    -DQMMP_DEFAULT_OUTPUT=pipewire \
    -DQMMP_DEFAULT_UI=qsui \
    #
cd doc && doxygen Doxyfile

%install
%K5install
%K5install_move data solid

# allow to find skins
mkdir -p %buildroot/%_datadir/%rname
ln -s `relative %_wlskindir %_datadir/%rname/skins` %buildroot/%_datadir/%rname/skins
# return desktop-files names
#for f in qmmp qmmp-dir qmmp-enqueue ; do
#    mv  %buildroot/%_desktopdir/${f}{-%major,}.desktop
#done

%files -n qmmp
%doc AUTHORS ChangeLog* README* doc/html
%_bindir/%rname
%_libdir/%rname-%major.*/
%_desktopdir/%{rname}*.desktop
%_datadir/%rname/
%_datadir/solid/actions/%{rname}*.desktop
%_iconsdir/hicolor/*/apps/%{rname}*.*
%_datadir/metainfo/*%{rname}*.xml

%files -n %libqmmp
%_libdir/libqmmp.so.%sover
%_libdir/libqmmp.so.%sover.*

%files -n %libqmmpui
%_libdir/libqmmpui.so.%sover
%_libdir/libqmmpui.so.%sover.*

%files devel
%_includedir/%{rname}*
%_pkgconfigdir/%{rname}*.pc
%_K5link/lib*.so

%changelog
* Fri Dec 15 2023 Sergey V Turchin <zerg@altlinux.org> 1:2.1.5-alt1
- initial build
