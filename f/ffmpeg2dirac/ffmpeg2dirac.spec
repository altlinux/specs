Name: ffmpeg2dirac
Version: 0.2.0
Release: alt1

Summary: Dirac video encoder using ffmpeg
License: GPLv2
Group: Video
Url: http://diracvideo.org/
Source: http://diracvideo.org/download/ffmpeg2dirac/%name-%version.tar.gz

Patch0: kino-script-rename.patch
Patch1: libav.patch

Packager: Paul Wolneykien <manowar@altlinux.ru>

# Automatically added by buildreq on Tue Sep 13 2011
# optimized out: libavcodec-devel libavutil-devel libdc1394-22 libogg-devel libopencore-amrnb0 libopencore-amrwb0 libraw1394-11 pkg-config python-base python-modules python-modules-compiler python-modules-email
BuildRequires: libavdevice-devel libavformat-devel libdirac-devel libkate-devel libpostproc-devel libschroedinger-devel gcc-c++ libswscale-devel libtheora-devel libvorbis-devel scons

%description
This package provides a command-line tool to encode/recode various
video formats (basically everything that ffmpeg can read) into Dirac and
Theora royality free video codecs.

%package kino
Summary: Dirac video encoder using ffmpeg
Group: Video
BuildArch: noarch
Requires: kino

%description kino
This package provides the upstream version of a script for export of
a video from Kino editor into an Ogg media file with Dirac and Vorbis
streams using royality free codecs.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
scons APPEND_CCFLAGS='%optflags'

%install
scons install bindir=%buildroot%{_bindir} \
              mandir=%buildroot%{_mandir} \
	      %buildroot
install -D -m 0755 kino_export/ffmpeg2dirac.sh %buildroot%{_datadir}/kino/scripts/exports/ffmpeg2dirac.upstream.sh

%files
%_bindir/*
%_man1dir/*
%doc AUTHORS README subtitles.txt TODO

%files kino
%{_datadir}/kino/scripts/exports/ffmpeg2dirac.upstream.sh

%changelog
* Wed Aug 31 2011 Paul Wolneykien <manowar@altlinux.ru> 0.2.0-alt1
- Build v 0.2.0 for ALT Linux.
- Fixes for the new libav v0.7.1.

* Tue Sep 28 2010 Paul Wolneykien <manowar@altlinux.ru> 0.1.0-alt2
- Add Kino export script (with separate "upstream" title)

* Sun Sep 26 2010 Paul Wolneykien <manowar@altlinux.ru> 0.1.0-alt1
- Initial release for ALT Linux.
