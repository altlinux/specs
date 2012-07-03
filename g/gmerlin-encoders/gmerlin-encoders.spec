Name: gmerlin-encoders
Version: 1.0.0
Release: alt1
Summary: Various encoders plugins for gmerlin

Group: Sound
License: GPL
Url: http://gmerlin.sourceforge.net/
Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source: %name-%version.tar.gz
Patch: %name-0.2.9-autotools.patch
Patch1: %name-%version-ffmpeg.patch

# Automatically added by buildreq on Sun Sep 25 2011
# optimized out: libavcodec-devel libavutil-devel libgavl-devel libogg-devel libxml2-devel pkg-config
BuildRequires: libavformat-devel libflac-devel libgmerlin-devel liblame-devel libmjpegtools-devel libspeex-devel libtheora-devel libvorbis-devel

BuildRequires: liblame-devel libmjpegtools-devel libspeex-devel libtheora-devel libvorbis-devel

%description
Various encoders plugins for package gmerlin.
(see http://effectc.sourceforge.net)

%prep
%setup
%patch  -p1
%patch1 -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
%find_lang %name
rm -f %buildroot%_libdir/gmerlin/plugins/*.la

%files -f %name.lang
%doc AUTHORS COPYING README
%dir %_libdir/gmerlin/plugins
%_libdir/gmerlin/plugins/*.so

%changelog
* Sat Sep 24 2011 Hihin Ruslan <ruslandh@altlinux.ru> 1.0.0-alt1
- New Version

* Sun Apr 25 2010 Hihin Ruslan <ruslandh@altlinux.ru> 0.2.9-alt1
- initial build for ALT Linux Sisyphus



