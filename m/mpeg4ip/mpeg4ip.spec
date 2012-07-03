%def_disable static

%def_disable faac

Name: mpeg4ip
Version: 1.5.0.1
Release: alt13.2

Summary: Set of linux video stream processing utilities
License: MPL
Group: Video
Url: http://www.mpeg4ip.net
Packager: Afanasov Dmitry <ender@altlinux.org>

Source: http://download.sourceforge.net/mpeg4ip/%name-%version.tar.gz
Patch: %name-ffmpeg-0.7.1.patch

# Automatically added by buildreq on Thu Dec 15 2005
BuildRequires: esound-devel fontconfig-devel freetype2-devel gcc-c++ glib2-devel id3lib-devel libSDL-devel liba52-devel libalsa-devel libatk-devel libaudio-devel libaudiofile-devel libcairo-devel libfaad-devel libglitz-devel libgtk+2-devel liblame-devel libmad-devel libmpeg2-devel libpango-devel libpng-devel libstdc++-devel libvorbis-devel nasm xvid-devel zlib-devel libx264-devel

BuildPreReq: libICE-devel libavformat-devel libpostproc-devel
BuildPreReq: libswscale-devel libavdevice-devel libavfilter-devel

%{?_enable_faac:BuildRequires: libfaac-devel}

%if_enabled static
BuildRequires: xorg-x11-devel-static
%endif

%description
The MPEG4IP project provides a standarts-based system
for encoding, streaming and playing encoded auido and video.
This package contains libraries of MPEG4IP project.

%package -n lib%name
Summary: MPEG4IP libraries
Group: Development/C

%description -n lib%name
MPEG4IP libraries.

%package -n libmp4v2
Summary: MP4V2 libraries
Group: Development/C

%description -n libmp4v2
MP4v2 libraries, part of mpeg4ip project

%package tools
Summary: MPEG4IP tools
Group: Video
Requires: lib%name = %version-%release

%description tools
MPEG4IP video, audio tools.

%package doc
Summary: MPEG4IP Documentation
Group: Video
BuildArch: noarch

%description doc
MPEG4IP Documentation.

%package -n lib%name-devel
Summary: MPEG4IP Development files
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
MPEG4IP Development files

%package player
Summary: MPEG4IP Player (console version)
Group: Video
Requires: lib%name = %version-%release
Requires: %name-player-plugins = %version-%release

%description player
MPEG4IP Player (Console version)

%package player-gui
Summary: MPEG4IP Player (GUI version)
Group: Video
Requires: lib%name = %version-%release
Requires: %name-player-plugins = %version-%release

%description player-gui
MPEG4IP Player (GUI version)

%package player-plugins
Summary: MPEG4IP Player plugins
Group: Video
Requires: lib%name = %version-%release

%description player-plugins
MPEG4IP Player plugins.

%package live
Summary: MPEG4IP Live streaming server
Group: Video
Requires: lib%name = %version-%release

%description live
MPEG4IP Live streaming server

%if_enabled static
%package -n lib%name-devel-static
Summary: MPEG4IP Static development files
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel-static
MPEG4IP Static development files
%endif

%prep
%setup -n %name-%version
%patch0 -p2
touch bootstrapped
# build player plugins as plugins, not libraries.
find ./player -name Makefile\* -print0 | xargs -r0 subst 's,\(\-module\),\1 -avoid-version,' --
find . -type f -name Makefile.\* |xargs fgrep -l -- -Werror |xargs sed -i 's,-Werror,,'
sed -i '/CFLAGS="$CFLAGS -Wall -Werror"/d' lib/rtp/configure.in

%build
touch {common/video/iso-mpeg4,lib/{rtp,SDLAudio}}/{NEWS,AUTHORS,ChangeLog}
%add_optflags -D__STDC_CONSTANT_MACROS
%autoreconf
%configure \
	%{subst_enable static} \
	--enable-server \
	--enable-player \
	--enable-mp4live \
	--without-arts \
	--enable-warns-as-err=no \
%ifarch %ix86 x86_64	
	--enable-mmx \
%endif
	#
make

%install
%make_install install DESTDIR=%buildroot -j1

# remove non-packaged files.
rm -f %buildroot%_libdir/mp4player_plugin/*.la

%if_disabled static
rm -f %buildroot%_libdir/mp4player_plugin/*.a
%endif

#strange .mpt file. go to docs for now...
mkdir -p %buildroot%_docdir/%name-%version
mv %buildroot/%_mandir/manm/* %buildroot%_docdir/%name-%version/

cp -Rv ./doc/* %buildroot%_datadir/doc/%name-%version/
find %buildroot%_datadir/doc/%name-%version -iname "*makefile*" -print0 | xargs -0 rm -f --
rm -rf %buildroot%_datadir/doc/%name-%version/{mp4v2,programs}

%files -n lib%name
%_libdir/*.so.*
%exclude %_libdir/libmp4v2.so.*

%files -n libmp4v2
%_libdir/libmp4v2.so.*

%files doc
%_man1dir/*
%_datadir/doc/%name-%version

%files -n lib%name-devel
%_bindir/mpeg4ip-config
%_libdir/*.so
%_includedir/*
%_man3dir/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%files player
%_bindir/mp4player

%files player-plugins
%dir %_libdir/mp4player_plugin
%_libdir/mp4player_plugin/*.so

#files player-gui
#_bindir/gmp4player

%files live
%_bindir/mp4live

%files tools
%_bindir/*
#exclude %_bindir/gmp4player
%exclude %_bindir/mp4player
%exclude %_bindir/mpeg4ip-config
%exclude %_bindir/mp4live

# TODO: fix checking of x264, when x264 will upgraded

%changelog
* Fri Apr 27 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.0.1-alt13.2
- rebuilt on arm

* Fri Feb 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0.1-alt13.1
- Rebuilt with libav 0.8

* Mon Aug 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0.1-alt13
- Rebuilt with ffmpeg 0.7.1

* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0.1-alt12
- Rebuilt for debuginfo
- BuildRequires: replaced xorg-x11-devel by libICE-devel

* Tue Dec 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0.1-alt11
- Rebuilt for soname set-versions and without arts

* Mon Nov 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0.1-alt10
- Fixed build

* Wed Feb 03 2010 Afanasov Dmitry <ender@altlinux.org> 1.5.0.1-alt9
- Disable faac encoder due to license troubles.
- Rebuild with libx264.so.85.
- Change packager.

* Wed May 13 2009 Pavlov Konstantin <thresh@altlinux.ru> 1.5.0.1-alt8
- Fix build with newer toolchain.

* Mon Apr 20 2009 Pavlov Konstantin <thresh@altlinux.ru> 1.5.0.1-alt7
- Fix build with newer ffmpeg.
- Also, use swscale instead of img_convert.

* Mon Oct 27 2008 Pavlov Konstantin <thresh@altlinux.ru> 1.5.0.1-alt6
- Fix build with gcc 4.3, thanks gentoo folks.

* Wed Jan 02 2008 Pavlov Konstantin <thresh@altlinux.ru> 1.5.0.1-alt5
- Fix build with new auto*. 

* Mon Nov 26 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.5.0.1-alt4
- Fix nasm detection.

* Tue Oct 24 2006 Pavlov Konstantin <thresh@altlinux.ru> 1.5.0.1-alt2
- Remove unneded -Werror stuff to fix building.
- Merge patches into the source tree.
- Fix building in regards to ffmpeg api change.

* Thu Oct 05 2006 Pavlov Konstantin <thresh@altlinux.ru> 1.5.0.1-alt1
- 1.5.0.1 release.

* Fri Aug 18 2006 Pavlov Konstantin <thresh@altlinux.ru> 1.5-alt4
- Added patch to deal with x264 changes (thx led@, closes #9887).

* Tue Jul 04 2006 Pavlov Konstantin <thresh@altlinux.ru> 1.5-alt3
- moved libmp4v2 to separate package.

* Tue Jul 04 2006 Pavlov Konstantin <thresh@altlinux.ru> 1.5-alt2
- moving includes to %%_includedir.

* Tue May 16 2006 Pavlov Konstantin <thresh@altlinux.ru> 1.5-alt1
- New version.
- linux-libc-headers.
- patch1 by damir@ to build on current sisyphus.

* Mon Dec 05 2005 Pavlov Konstantin <thresh@altlinux.ru> 1.4.1-alt1
- 1.4.1 release.
- x86_64 specfile fixes.
- altered buildreqs.

* Fri Jun 17 2005 Pavlov Konstantin <thresh@altlinux.ru> 1.3-alt1
- 1.3 release.

* Fri Mar 25 2005 Pavlov Konstantin <thresh@altlinux.ru> 1.2-alt1
- Initial build for ALT Linux Sisyphus.

