Name: vorbisgain
Version: 0.37
Release: alt1

Summary: Adds tags to Ogg Vorbis files to adjust the volume
License: GPL 2.1
Group: Sound

Url: http://sjeng.sourceforge.net/vorbisgain.html
Source: http://sjeng.org/ftp/vorbis/%name-%version.tar.gz
Patch: vorbisgain-0.37-double-fclose.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Tue Jan 30 2007
BuildRequires: libvorbis-devel

BuildRequires: libvorbis-devel libogg-devel

%description
VorbisGain is a utility that uses a psychoacoustic method to correct the
volume of an Ogg Vorbis file to a predefined standardized loudness.

It is meant as a replacement for the normalization that is commonly used
before encoding. Although normalization will ensure that each song has
the same peak volume, this unfortunately does not say anything about the
apparent loudness of the music, with the end result being that many
normalized files still don't sound equally loud. VorbisGain uses
psychoacoustics to address this deficiency. Moreover, unlike
normalization, it's a lossless procedure which works by adding tags to
the file. Additionally, it will add hints that can be used to prevent
clipping on playback. It is based upon the ReplayGain technology.

The end result is that the file ends up with superior playback quality
compared to a non-VorbisGain'ed file.

It needs player support to work. Non-supporting players will play back
the files without problems, but you'll miss out on the benefits.
Nowadays most good players such as ogg123 and mplayer are already
compatible. xmms will support this feature from release 1.2.8.

%prep
%setup -q
%patch -p1

%build
%configure --enable-recursive
%make

%install
%makeinstall

%files
%_bindir/*
%_man1dir/*
%doc NEWS README vorbisgain.txt

%changelog
* Mon Jan 29 2007 Michael Shigorin <mike@altlinux.org> 0.37-alt1
- 0.37
- built for ALT Linux (based on largely cleaned up Mandriva spec
  and to some degree on Dag Wieers' spec)
- rediffed patch from Dag Wieers' package

* Sun Oct 12 2003 Han Boetes <han@linux-mandrake.com> 0.34-1mdk
- Bump!

* Mon Apr 21 2003 Han Boetes <han@linux-mandrake.com> 0.32-3mdk
- Remove the patch again. OpenBSD-guru's say it's nonsense and
  vorbisgain segfaults.
- Added a patch to clean up configure

* Tue Mar 18 2003 Han Boetes <han@linux-mandrake.com> 0.32-2mdk
- added patches and updates that can also be found in the OpenBSD-port
- mplayer and ogg123 support this extension BTW :)

* Tue Mar  4 2003 Han Boetes <han@linux-mandrake.com> 0.32-1mdk
- This rpm works, the program works, just nothing supports it yet.
  We have to wait for xmms-1.2.8. Ow well. :)
