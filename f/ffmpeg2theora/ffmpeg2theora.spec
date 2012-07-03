Name: ffmpeg2theora
Version: 0.26
Release: alt1.1

Summary: Theora video encoder using ffmpeg
License: GPLv3+
Group: Video
Url: http://www.v2v.cc/~j/ffmpeg2theora/
# http://www.v2v.cc/~j/ffmpeg2theora/downloads/%name-%version.tar.bz2
Source: %name-%version.tar
Patch0: ffmpeg2theora-0.24-deb-alt-man.patch
Patch1: ffmpeg2theora-0.26-alt-libav07.patch

# Automatically added by buildreq on Tue Jun 15 2010
BuildRequires: gcc-c++ libavdevice-devel libavformat-devel libkate-devel libpostproc-devel libswscale-devel libtheora-devel libvorbis-devel scons

%description
This package provides a command-line tool to encode/recode various
video formats (basically everything that ffmpeg can read) into Theora,
the free video codec.

%prep
%setup
%patch0 -p1
%patch1 -p2

%build
scons APPEND_CCFLAGS='%optflags'

%install
install -pDm755 %name %buildroot%_bindir/%name
install -pDm644 %name.1 %buildroot%_man1dir/%name.1

%files
%_bindir/*
%_man1dir/*
%doc AUTHORS ChangeLog

%changelog
* Mon Oct 24 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.26-alt1.1
- rebuilt with libav-0.7

* Tue Jun 15 2010 Dmitry V. Levin <ldv@altlinux.org> 0.26-alt1
- Updated to 0.26.
- Cleaned up specfile.
- Updated build requirements.
- Imported and updated manpage fix from Debian package.

* Thu Feb 05 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.23-alt2
- rebuild with libavcodec.so.52

* Sun Dec 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.23-alt1
- 0.23

* Mon Oct 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.22-alt1
- 0.22

* Wed Oct 15 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.21-alt2
- build with libkate

* Wed Oct 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.21-alt1
- 0.21

* Tue Dec 18 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.20-alt2
- rebuild with ffmpeg-11199

* Tue Dec 04 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.20-alt1
- 0.20:
  + add postprocessing filters, denoise, deblock, dering
  + new preset
  + several bugfixes

* Mon Oct 08 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.19-alt1
- 0.19

* Thu Jun 28 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.17-alt2
- fixed build dependencies

* Sun Feb 25 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.17-alt1
- 0.17

* Sat Dec 30 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.16-alt3.1
- Rebuilt due to libavformat.so.50 -> libavformat.so.51 soname change.

* Fri Jun 30 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.16-alt3
- real fixed build dependencies

* Mon Jun 05 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.16-alt2
- fixed build dependencies

* Mon May 29 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.16-alt1
- 0.16

* Mon Nov 14 2005 Kachalov Anton <mouse@altlinux.ru> 0.15-alt1
- 0.15

* Sun Jul 10 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.13-alt1
- 0.13

* Mon Feb 14 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.12-alt1
- 0.12

* Sun Oct 24 2004 Valery Inozemtsev <shrek@altlinux.ru> 0.11-alt1
- initial release

