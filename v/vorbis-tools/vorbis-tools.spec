Name: vorbis-tools
Version: 1.4.0
Release: alt1

Summary: The Vorbis General Audio Compression Codec tools
License: GPLv2
Group: Sound
URL: http://www.xiph.org/
# http://downloads.xiph.org/releases/vorbis/%name-%version.tar.gz
Source: %name-%version.tar
Patch: vorbis-tools-1.4.0-alt-fixes.patch

# Automatically added by buildreq on Fri Oct 22 2010
BuildRequires: libao-devel libcurl-devel libflac-devel libkate-devel libspeex-devel libvorbis-devel

%description
Ogg Vorbis is a fully open, non-proprietary, patent- and royalty-free,
general-purpose compressed audio format for audio and music at fixed
and variable bitrates from 16 to 128 kbps/channel.

The package contains an encoder, a decoder, a playback tool, a cut tool,
an informator, and a comment editor.

%prep
%setup
%patch -p1

%build
%configure
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%_bindir/*
%_man1dir/*
%doc AUTHORS CHANGES README

%changelog
* Fri Oct 22 2010 Dmitry V. Levin <ldv@altlinux.org> 1.4.0-alt1
- Updated to 1.4.0.
- Cleaned up specfile.

* Sun Aug 10 2008 Led <led@altlinux.ru> 1.2.0-alt3
- fixed spec
- added %name-1.2.0-alt.patch

* Wed May 14 2008 Led <led@altlinux.ru> 1.2.0-alt2
- added vorbis-tools-1.2.0-sec.patch (fixed vulnerable speex code)
  (thanks icesik@ for link)

* Mon Mar 17 2008 Led <led@altlinux.ru> 1.2.0-alt1
- 1.2.0:
  + added remote control support in (ogg123)
  + limited support for chained Ogg bitstreams (oggdec)
  + support decoding of multiple files into a single one (oggdec)
  + -k, switch for Skeleton bitstream encoding (oggenc)
  + proper 5.1 channel mapping support (oggenc)
  + recognizes Skeleton, Dirac, FLAC and Kate bitstreams (ogginfo)
  + support for creation of long comments (vorbiscomment)
  + support for multiplexed Vorbis (vorbiscomment)
- removed (fixed in upstream):
  + %name-1.1.1-iconv.patch
  + %name-1.1.1+flac-1.1.3-1.patch
  + %name-1.1.1+flac-1.1.3-2.patch
  + %name-1.1.1+flac-1.1.3-3.patch
  + %name-1.1.1-curl4.patch
- updated %name-1.2.0-configure.patch
- updated BuildRequires

* Mon Mar 17 2008 Led <led@altlinux.ru> 1.1.1-alt7
- fixed %%description

* Thu Dec 27 2007 Led <led@altlinux.ru> 1.1.1-alt6
- fixed %%changelog

* Wed Dec 26 2007 Led <led@altlinux.ru> 1.1.1-alt5
- fixed build with automake-1.10

* Wed Mar 07 2007 Led <led@altlinux.ru> 1.1.1-alt4
- rebuild with libFLAC.so.8

* Tue Feb 06 2007 Led <led@altlinux.ru> 1.1.1-alt3.1
- fixed %%changelog

* Mon Feb 05 2007 Led <led@altlinux.ru> 1.1.1-alt3
- added %name-1.1.1+flac-1.1.3-[123].patch (from Gentoo)
- fixed build with flac and speex: %name-1.1.1-configure.patch
- added %name-1.1.1-curl4.patch (from NetBSD)
- cleaned up spec

* Mon Jul 24 2006 Led <led@altlinux.ru> 1.1.1-alt2
- cleaned up spec
- enabled FLAC

* Mon Jul 10 2006 Led <led@altlinux.ru> 1.1.1-alt1.1
- added vorbis-tools-1.1.1-iconv.patch

* Thu Jul 07 2005 Andrey Astafiev <andrei@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Sat Nov 22 2003 Andrey Astafiev <andrei@altlinux.ru> 1.0update.1-alt1
- 1.0.1

* Mon Sep 15 2003 Andrey Astafiev <andrei@altlinux.ru> 1.0release-alt3
- Fixed to build with hasher.

* Thu Oct 31 2002 Rider <rider@altlinux.ru> 1.0release-alt2
- rebuild (gcc 3.2)

* Tue Jul 30 2002 Andrey Astafiev <andrei@altlinux.ru> 1.0release-alt1
- 1.0
- some temprorary changes to avoid using Serial.

* Thu Jan 03 2002 Andrey Astafiev <andrei@altlinux.ru> 1.0rc3-alt1
- 1.0rc3

* Thu Sep 27 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.0rc2-alt2
- A bit more specfile cleanup.

* Thu Sep 27 2001 Andrey Astafiev <andrei@altlinux.ru> 1.0rc2-alt1
- spec cleanup.

* Sat Sep 22 2001 Michael Shigorin <mike@lic145.kiev.ua>
- built for ALTLinux.

* Sun Aug 12 2001 Greg Maxwell <greg@linuxpower.cx>
- updated for rc2.

* Sun Jun 17 2001 Jack Moffitt <jack@icecast.org>
- updated for rc1.
- added ogginfo.

* Mon Jan 22 2001 Jack Moffitt <jack@icecast.org>
- updated for prebeta4 builds.

* Sun Oct 29 2000 Jack Moffitt <jack@icecast.org>
- initial spec file created.
