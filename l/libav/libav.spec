# vim: set ft=spec fdm=marker :

# {{{ Macros
%define set_disable() %{expand:%%force_disable %{1}} %{expand:%%undefine _enable_%{1}}
%define set_enable() %{expand:%%force_enable %{1}} %{expand:%%undefine _disable_%{1}}
%define subst_enable_with() %{expand:%%{?_enable_%{1}:--enable-%{2}} } %{expand:%%{?_disable_%{1}:--disable-%{2}} }
# }}}

# {{{ Enable/Disable stuff
%def_enable gpl
%def_enable version3
%def_enable libxvid
%def_enable libx264
%def_enable postproc
%def_enable libmp3lame
%def_enable libvorbis
%def_enable libcdio
%def_disable libfaac
%def_enable libpulse
%def_disable nonfree
%def_enable libgsm
%def_enable libdc1394
%def_enable shared
%def_enable static
%def_enable pthreads
%def_enable zlib
%def_enable mmx
%def_disable iwmmxt
%def_disable memalign_hack
%def_enable avserver
%def_enable avplay
%def_enable avprobe
%def_disable libdirac
%def_enable libschroedinger
%def_disable avisynth
%def_disable libnut
%def_enable libtheora
%def_disable debug
%def_enable bzlib
%def_enable vaapi
%def_enable vdpau
%def_enable libopencore_amrwb
%def_enable libopencore_amrnb
%def_enable libvpx
%def_enable libv4l2
%def_enable libspeex
%def_enable librtmp
%def_disable frei0r

%if_disabled gpl
%set_disable libxvid
%set_disable libx264
%set_disable postproc
%endif

%if_disabled version3
%set_disable libopencore_amrwb
%set_disable libopencore_amrnb
%endif

%if_disabled nonfree
%set_disable libfaac
%endif

%if_enabled mmx
%set_verify_elf_method textrel=relaxed
%endif
# }}}

Name: libav
Version: 0.8.2
Release: alt1
Epoch: 1

%define gitrev 43e5fda4

Summary: Hyper fast MPEG1/MPEG4/H263/RV and AC3/MPEG audio encoder
License: %{!?_enable_gpl:L}GPL%{?_enable_version3:3}
Group: System/Libraries
Url: http://libav.org

Source0: %name-%version-%release.tar

# {{{ BuildRequires
BuildRequires: libfreetype-devel texi2html
BuildRequires: libX11-devel libXext-devel libXvMC-devel libXfixes-devel
BuildRequires: yasm
BuildRequires: libalsa-devel
BuildRequires: perl-podlators

%{?_enable_avplay:BuildRequires: libSDL-devel}
%{?_enable_libmp3lame:BuildRequires: liblame-devel}
%{?_enable_libvorbis:BuildRequires: libvorbis-devel}
%{?_enable_libfaac:BuildRequires: libfaac-devel}
%{?_enable_libcdio:BuildRequires: libcdio-devel}
%{?_enable_libgsm:BuildRequires: libgsm-devel}
%{?_enable_libpulse:BuildRequires: libpulseaudio-devel}
%{?_enable_libxvid:BuildRequires: libxvid-devel}
%{?_enable_libx264:BuildRequires: libx264-devel >= 118}
%{?_enable_libdc1394:BuildRequires: libdc1394-devel libraw1394-devel}
%{?_enable_libdirac:BuildRequires: libdirac-devel >= 0.9.1-alt1 libstdc++-devel gcc4.1-c++}
%{?_enable_libschroedinger:BuildRequires: libschroedinger-devel}
%{?_enable_libnut:BuildRequires: libnut-devel}
%{?_enable_libtheora:BuildRequires: libtheora-devel}
%{?_enable_bzlib:BuildRequires: bzlib-devel}
%{?_enable_vaapi:BuildRequires: libva-devel}
%{?_enable_vdpau:BuildRequires: libvdpau-devel}
%{?_enable_libopencore_amrwb:BuildRequires: libopencore-amrwb-devel}
%{?_enable_libopencore_amrnb:BuildRequires: libopencore-amrnb-devel}
%{?_enable_libvpx:BuildRequires: libvpx-devel}
%{?_enable_libv4l2:BuildRequires: libv4l-devel}
%{?_enable_librtmp:BuildRequires: librtmp-devel}
%{?_enable_frei0r:BuildRequires: frei0r-devel}
%{?_enable_libspeex:BuildRequires: libspeex-devel}
# }}}

# {{{ Packages
%package doc
Summary: Documentation files for libav project.
Group: Video
BuildArch: noarch
Provides: ffmpeg-doc = %epoch:%version-%release
Obsoletes: ffmpeg-doc

%package -n avserver
Summary: A streaming server for both audio and video
Group: Video
Requires: libavcodec53 = %epoch:%version-%release
Requires: libavformat53 = %epoch:%version-%release
Provides: ffserver = %epoch:%version-%release
Obsoletes: ffserver

%package -n avplay
Summary: A very simple media player using the libav and SDL libraries
Group: Video
Requires: libavcodec53 = %epoch:%version-%release
Requires: libavformat53 = %epoch:%version-%release
Provides: ffplay = %epoch:%version-%release
Obsoletes: ffplay

%package -n avprobe
Summary:  Multimedia streams analyzer
Group: Video
Requires: libavcodec53 = %epoch:%version-%release
Requires: libavformat53 = %epoch:%version-%release
Provides: ffprobe = %epoch:%version-%release
Obsoletes: ffprobe

%package -n avconv
Summary: Hyper fast MPEG1/MPEG4/H263/RV and AC3/MPEG audio encoder
Group: Video
Requires: libavcodec53 = %epoch:%version-%release
Requires: libavformat53 = %epoch:%version-%release
Requires: libavutil51 = %epoch:%version-%release
Requires: libavdevice = %epoch:%version-%release
Requires: libavfilter = %epoch:%version-%release
Provides: ffmpeg = %epoch:%version-%release
Obsoletes: ffmpeg

%package -n libavcodec53
Summary: libav codec library
Group: System/Libraries
Provides: libavcodec = %epoch:%version-%release
Obsoletes: libavcodec < %epoch:%version-%release
%{?_enable_libdirac:Requires: libdirac >= 0.9.1-alt1}

%package -n libavcodec-devel
Summary: Development files for libavcodec
Group: Development/C
Requires: libavcodec53 = %epoch:%version-%release
Requires: libavutil-devel = %epoch:%version-%release

%package -n libavcodec-devel-static
Summary: Static development files for libavcodec
Group: Development/C
Requires: libavcodec-devel = %epoch:%version-%release

%package -n libavformat53
Summary: libav file format library
Group: System/Libraries
Requires: libavcodec53 = %epoch:%version-%release
Provides: libavformat = %epoch:%version-%release
Obsoletes: libavformat < %epoch:%version-%release

%package -n libavformat-devel
Summary: Development files for libavcodec
Group: Development/C
Requires: libavformat53 = %epoch:%version-%release
Requires: libavcodec-devel = %epoch:%version-%release

%package -n libavformat-devel-static
Summary: Static development files for libavformat
Group: Development/C
Requires: libavformat-devel = %epoch:%version-%release

%package -n libavutil51
Summary: libav utility library
Group: System/Libraries
Provides: libavutil = %epoch:%version-%release

%package -n libavutil-devel
Summary: Development files for libavutil
Group: Development/C
Requires: libavutil51 = %epoch:%version-%release

%package -n libavutil-devel-static
Summary: Static development files for libavutil
Group: Development/C
Requires: libavutil-devel = %epoch:%version-%release

%package -n libpostproc
Summary: libav video postprocessing library
Group: System/Libraries

%package -n libpostproc-devel
Summary: Development files for libpostproc
Group: Development/C
Requires: libpostproc = %epoch:%version-%release
Requires: libavutil-devel = %epoch:%version-%release

%package -n libpostproc-devel-static
Summary: Static development files for libpostproc
Group: Development/C
Requires: libpostproc-devel = %epoch:%version-%release

%package -n libswscale
Summary: libav image rescaling library
Group: System/Libraries

%package -n libswscale-devel
Summary: Development files for libswscale
Group: Development/C
Requires: libswscale = %epoch:%version-%release
Requires: libavutil-devel = %epoch:%version-%release

%package -n libswscale-devel-static
Summary: Static development files for libswscale
Group: Development/C
Requires: libswscale-devel = %epoch:%version-%release

%package -n libavdevice
Summary: libav device handling library
Group: System/Libraries

%package -n libavdevice-devel
Summary: Development files for libavdevice
Group: Development/C
Requires: libavdevice = %epoch:%version-%release

%package -n libavdevice-devel-static
Summary: Static development files for libavdevice
Group: Development/C
Requires: libavdevice-devel = %epoch:%version-%release

%package -n libavfilter
Summary: libav filter handling library
Group: System/Libraries

%package -n libavfilter-devel
Summary: Development files for libavfilter
Group: Development/C
Requires: libavfilter = %epoch:%version-%release

%package -n libavfilter-devel-static
Summary: Static development files for libavfilter
Group: Development/C
Requires: libavfilter-devel = %epoch:%version-%release

# }}}

# {{{ Descriptions

%description
%name is a hyper fast realtime audio/video encoder, a streaming
server and a generic audio and video file converter.

It can grab from a standard Video4Linux video source and convert it
into several file formats based on DCT/motion compensation encoding.
Sound is compressed in MPEG audio layer 2 or using an AC3 compatible
stream.

%description doc
This package contains documentation for libav project.

%description -n avserver
avserver is a streaming server for both audio and video. It supports
several live feeds, streaming from files and time shifting on live
feeds.

%description -n avplay
avplay is a very simple and portable media player using the libav
libraries and the SDL library. It is mostly used as a testbed for the
various libav APIs

%description -n avprobe
avprobe is a simple multimedia streams analyzer with a command-line
interface based on the libav project libraries.

%description -n avconv
avconv is a hyper fast realtime audio/video encoder, a streaming
server and a generic audio and video file converter.

It can grab from a standard Video4Linux video source and convert it
into several file formats based on DCT/motion compensation encoding.
Sound is compressed in MPEG audio layer 2 or using an AC3 compatible
stream.

%description -n libavcodec53
This package contains libavcodec, the libav project codec library.

%description -n libavcodec-devel
This package contains development files for libavcodec.

%description -n libavformat53
This package contains libavformat, the libav project file format library.

%description -n libavformat-devel
This package contains development files for libavformat.

%description -n libavutil51
This package contains libavutil, the libav project utility library.

%description -n libavutil-devel
This package contains development files for libavutil.

%description -n libpostproc
This package contains libpostproc, the libav project video postprocessing library.

%description -n libpostproc-devel
This package contains development files for libpostproc

%description -n libswscale
This package contains libswscale, the libav project image rescaling library.

%description -n libswscale-devel
This package contains development files for libswscale.

%description -n libavdevice
This package contains libavdevice, the libav project device handling library.

%description -n libavdevice-devel
This package contains development files for libavdevice.

%description -n libavfilter
This package contains libavfilter, the libav project filter handling library.

%description -n libavfilter-devel
This package contains development files for libavfilter.

%description -n libavformat-devel-static
This package contains static development files for libavformat.

%description -n libavcodec-devel-static
This package contains static development files for libavcodec.

%description -n libpostproc-devel-static
This package contains static development files for libpostproc

%description -n libswscale-devel-static
This package contains static development files for libswscale

%description -n libavutil-devel-static
This package contains static development files for libavutil.

%description -n libavdevice-devel-static
This package contains static development files for libavdevice.

%description -n libavfilter-devel-static
This package contains static development files for libavfilter.

# }}}

# {{{ Prep
%prep
%setup
sed -i 's/UNKNOWN/%version/' version.sh
# }}}

# {{{ Build
%build
%add_optflags -frename-registers
%ifarch x86_64
%add_optflags %optflags_shared
%else
%ifarch %ix86
%add_optflags %{?_enable_mmx:-DRUNTIME_CPUDETECT}
%endif
%endif
./configure \
    --prefix=%_prefix \
    --libdir=%_libdir \
    --shlibdir=%_libdir \
    --mandir=%_mandir \
    %{subst_enable gpl} \
    %{subst_enable postproc} \
    %{subst_enable pthreads} \
    %{subst_enable shared} \
    %{subst_enable static} \
    %{subst_enable libvorbis} \
    %{subst_enable libfaac} \
    %{subst_enable libpulse} \
    %{subst_enable libxvid} \
    %{subst_enable libx264} \
    %{subst_enable libmp3lame} \
    %{subst_enable libcdio} \
    %{subst_enable libgsm} \
    %{subst_enable libdc1394} \
    %{subst_enable zlib} \
    %{subst_enable mmx} \
    %{subst_enable iwmmxt} \
    %{subst_enable_with memalign_hack memalign-hack} \
    %{subst_enable avserver} \
    %{subst_enable avplay} \
    %{subst_enable avprobe} \
    %{subst_enable libdirac} \
    %{subst_enable libschroedinger} \
    --enable-avfilter \
    %{subst_enable avisynth} \
    %{subst_enable libnut} \
    %{subst_enable libtheora} \
    %{subst_enable version3} \
    %{subst_enable_with libopencore_amrwb libopencore-amrwb} \
    %{subst_enable_with libopencore_amrnb libopencore-amrnb} \
    --enable-hardcoded-tables \
    --enable-runtime-cpudetect \
    --enable-x11grab \
    --enable-bzlib \
    %{subst_enable libvpx} \
    %{subst_enable libv4l2} \
    %{subst_enable libspeex} \
    %{subst_enable frei0r} \
    %{subst_enable nonfree} \
    %{subst_enable librtmp} \
    %{subst_enable vaapi} \
    %{subst_enable vdpau} \
%if_enabled debug
    --enable-debug \
    --disable-stripping \
%else
    --disable-debug \
%endif
    --enable-pic \
    --extra-cflags="%optflags" \
    --extra-version='%release\ \(git.%gitrev\)'

%make

# }}}

# {{{ Install
%install
%make_install \
		INCDIR="%buildroot%_includedir" \
		DESTDIR="%buildroot" \
		MANDIR="%buildroot%_mandir" install

%{?_enable_avserver:install -pD -m640 doc/avserver.conf %buildroot%_sysconfdir/avserver.conf}

%if_enabled postproc
install -d -m 0755 %buildroot%_includedir/postproc
for f in %buildroot%_includedir/libpostproc/*; do
    ln -sf ../libpostproc/$(basename "$f") %buildroot%_includedir/postproc/
done
%endif

bzip2 --best --force --keep -- Changelog

# }}}

# {{{ Files

%files doc
%doc doc/faq.html doc/avconv.html doc/ffmpeg.html
%doc doc/optimization.txt
%doc CREDITS
%doc Changelog.*

%files -n libavcodec53
%_libdir/libavcodec.so.*

%files -n libavcodec-devel
%_includedir/libavcodec
%_libdir/libavcodec.so
%_pkgconfigdir/libavcodec.pc

%files -n libavformat53
%_libdir/libavformat.so.*

%files -n libavformat-devel
%_includedir/libavformat
%_pkgconfigdir/libavformat.pc
%_libdir/libavformat.so

%files -n libavutil51
%_libdir/libavutil.so.*

%files -n libavutil-devel
%_includedir/libavutil
%_libdir/libavutil.so
%_pkgconfigdir/libavutil.pc

%files -n libavdevice
%_libdir/libavdevice.so.*

%files -n libavdevice-devel
%_includedir/libavdevice
%_libdir/libavdevice.so
%_pkgconfigdir/libavdevice.pc

%files -n libavfilter
%_libdir/libavfilter.so.*

%files -n libavfilter-devel
%_includedir/libavfilter
%_libdir/libavfilter.so
%_pkgconfigdir/libavfilter.pc

%files -n libpostproc
%_libdir/libpostproc.so.*

%files -n libpostproc-devel
%_pkgconfigdir/libpostproc.pc
%_includedir/postproc
%_includedir/libpostproc
%_libdir/libpostproc.so

%files -n libswscale
%_libdir/libswscale.so.*

%files -n libswscale-devel
%_includedir/libswscale
%_pkgconfigdir/libswscale.pc
%_libdir/libswscale.so

%if_enabled static
%files -n libavformat-devel-static
%_libdir/libavformat.a

%files -n libavcodec-devel-static
%_libdir/libavcodec.a

%files -n libavutil-devel-static
%_libdir/libavutil.a

%files -n libpostproc-devel-static
%_libdir/libpostproc.a

%files -n libswscale-devel-static
%_libdir/libswscale.a

%files -n libavdevice-devel-static
%_libdir/libavdevice.a

%files -n libavfilter-devel-static
%_libdir/libavfilter.a
%endif

%files -n avconv
%_bindir/avconv
%_bindir/ffmpeg
%_man1dir/avconv.*
%_man1dir/ffmpeg.*
%_datadir/avconv

%if_enabled avserver
%files -n avserver
%doc doc/avserver.html
%config(noreplace) %_sysconfdir/*
%_bindir/avserver
%_man1dir/avserver.*
%endif

%if_enabled avplay
%files -n avplay
%doc doc/avplay.html
%_bindir/avplay
%_man1dir/avplay.*
%endif

%if_enabled avprobe
%files -n avprobe
%doc doc/avprobe.html
%_bindir/avprobe
%_man1dir/avprobe.*
%endif

# }}}

# {{{ Changelog
%changelog
* Sat May 05 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:0.8.2-alt1
- 0.8.2 released

* Fri Mar 16 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:0.8.1-alt1
- 0.8.1 released

* Tue Jan 31 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:0.8-alt2
- backport libav#212 from head

* Sun Jan 29 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:0.8-alt1
- 0.8 released

* Wed Jan 11 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:0.7.4-alt1
- 0.7.4 released

* Tue Dec 27 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:0.7.3-alt1
- 0.7.3 released

* Tue Oct 04 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:0.7.2-alt1
- 0.7.2 released

* Fri Sep 02 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:0.7.1-alt3
- reenable vaapi acceleration, lost somehow during ffmpeg->libav transition

* Mon Aug 08 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:0.7.1-alt2
- fix posprocess breakage (#26004)

* Mon Aug 01 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:0.7.1-alt1
- 0.7.1 release

* Tue Jun 21 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:0.7-alt1
- 0.7 released

* Fri Jun 17 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:0.7-alt0.1
- 0.7 rc1 released

* Sun Apr 17 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:0.6-alt7
- moved to and updated from libav upstream

* Thu Mar 10 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:0.6-alt5
- actually enable debuginfo

* Thu Mar 10 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:0.6-alt4
- rebuilt for debuginfo

* Tue Nov 30 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:0.6-alt3
- 25846 revision from trunk

* Thu Nov 04 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:0.6-alt2
- 25671 revision from trunk

* Thu Nov 04 2010 Igor Vlasenko <viy@altlinux.ru> 1:0.6-alt1.svn24911.1
- NMU: rebuild with new pkgconfig and rpm-build >=4.0.4-alt100.2

* Wed Aug 25 2010 Konstantin Pavlov <thresh@altlinux.org> 1:0.6-alt1.svn24911
- 24911 revision from trunk.

* Mon Jul 26 2010 Konstantin Pavlov <thresh@altlinux.org> 1:0.6-alt1.svn24504
- 24504 revision from trunk.
- Introducing new libavcore library.

* Wed Jun 30 2010 Konstantin Pavlov <thresh@altlinux.org> 1:0.6-alt1.svn23903
- 23903 revision from trunk.
- Build with librtmp.

* Mon Jun 21 2010 Konstantin Pavlov <thresh@altlinux.org> 1:0.6-alt1.svn23677
- 23677 revision from trunk.
- Bumping version as we are already past 0.6 release.
- Built without faad (removed upstream).
- Build with libvorbis.

* Sun May 30 2010 Konstantin Pavlov <thresh@altlinux.org> 1:0.5-alt1.svn23389
- 23389 revision from trunk.
- Build with libvpx.
- Build with libv4l2.

* Thu May 13 2010 Konstantin Pavlov <thresh@altlinux.org> 1:0.5-alt1.svn23107
- 23107 revision from trunk.

* Tue Mar 16 2010 Konstantin Pavlov <thresh@altlinux.org> 1:0.5-alt1.svn22565
- 22565 revision from trunk.

* Tue Mar 02 2010 Konstantin Pavlov <thresh@altlinux.org> 1:0.5-alt1.svn22144
- 22144 revision from trunk.

* Wed Feb 24 2010 Konstantin Pavlov <thresh@altlinux.org> 1:0.5-alt1.svn22019
- 22019 revision from trunk.
- Merge changes by ender@:
  + obsolete old libavcodec,
  + use explicit requires for packages.

* Wed Feb 03 2010 Afanasov Dmitry <ender@altlinux.org> 1:0.5-alt1.svn21489.1
- Build with libx264.so.84.

* Thu Jan 28 2010 Konstantin Pavlov <thresh@altlinux.org> 1:0.5-alt1.svn21489
- 21489 revision from trunk.

* Mon Jan 25 2010 Konstantin Pavlov <thresh@altlinux.org> 1:0.5-alt1.svn21449
- 21449 revision from trunk.

* Mon Nov 30 2009 Konstantin Pavlov <thresh@altlinux.org> 1:0.5-alt1.svn20668
- 20668 revision from trunk.

* Thu Nov 12 2009 Konstantin Pavlov <thresh@altlinux.org> 1:0.5-alt1.svn20524
- 20524 revision from trunk.
- Enable libxvid support (closes #16348).

* Wed Oct 14 2009 Konstantin Pavlov <thresh@altlinux.org> 1:0.5-alt1.svn20231
- 20231 revision from trunk.

* Sun Sep 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.5-alt1.svn19530.1
- fixed SA36760

* Fri Sep 25 2009 Konstantin Pavlov <thresh@altlinux.org> 1:0.5-alt1.svn20024
- 20024 revision from trunk.

* Tue Sep 15 2009 Konstantin Pavlov <thresh@altlinux.org> 1:0.5-alt1.svn19854
- 19854 revision from trunk.

* Mon Aug 24 2009 Konstantin Pavlov <thresh@altlinux.org> 1:0.5-alt1.svn19692
- 19692 revision from trunk.

* Thu Aug 06 2009 Konstantin Pavlov <thresh@altlinux.org> 1:0.5-alt1.svn19598
- 19598 revision from trunk.

* Wed Jul 29 2009 Konstantin Pavlov <thresh@altlinux.org> 1:0.5-alt1.svn19530
- 19530 revision from trunk.

* Tue Jul 28 2009 Konstantin Pavlov <thresh@altlinux.org> 1:0.5-alt1.svn19527
- 19527 revision from trunk.

* Thu Jun 18 2009 Konstantin Pavlov <thresh@altlinux.org> 1:0.5-alt1.svn19217
- 19217 revision from trunk.
- OpencoreAMR support merged into the main tree.

* Mon Jun 01 2009 Pavlov Konstantin <thresh@altlinux.ru> 1:0.5-alt1.svn19071
- 19071 revision from trunk.
- Applied patch to decode H264 using VA-API.

* Fri May 29 2009 Pavlov Konstantin <thresh@altlinux.ru> 1:0.5-alt1.svn18980
- 18980 revision from trunk.
- Drop libamr?b dlopen support.
- Provide AMR support through libopencore-amr.
- Drop libfaac support. The library isnt LGPL, we couldnt link with it.
  (see http://lists.mplayerhq.hu/pipermail/ffmpeg-devel/2009-April/068819.html
  and above for clarifications).

* Wed Apr 22 2009 Pavlov Konstantin <thresh@altlinux.ru> 1:0.5-alt1.svn18660
- 18660 revision from trunk.
- Enable VAAPI support through libva.

* Tue Mar 24 2009 Pavlov Konstantin <thresh@altlinux.ru> 1:0.5-alt1.svn18177
- 18177 revision from trunk.

* Tue Mar 24 2009 Pavlov Konstantin <thresh@altlinux.ru> 1:0.5-alt1
- 0.5 release.
- Remove support for openchrome xvmc (see #13453).

* Wed Feb 04 2009 Pavlov Konstantin <thresh@altlinux.ru> 16989-alt1
- 16989 revision (fixes CVE-2009-0385).

* Wed Jan 28 2009 Pavlov Konstantin <thresh@altlinux.ru> 16843-alt1
- 16843 revision.

* Wed Jan 28 2009 Pavlov Konstantin <thresh@altlinux.ru> 16817-alt1
- 16817 revision.

* Mon Jan 12 2009 Pavlov Konstantin <thresh@altlinux.ru> 16564-alt1
- 16564 revision.

* Mon Jan 05 2009 Pavlov Konstantin <thresh@altlinux.ru> 16439-alt1
- 16439 revision.

* Tue Dec 09 2008 Pavlov Konstantin <thresh@altlinux.ru> 16042-alt1
- 16042 revision.
- remove post/postun ldconfig stuff.
- Added needed Requires to -devel subpackages.

* Tue Oct 14 2008 Pavlov Konstantin <thresh@altlinux.ru> 15615-alt1
- 15615 revision.

* Tue Sep 02 2008 Pavlov Konstantin <thresh@altlinux.ru> 15151-alt1
- 15151 revision.
- Added patch fixing libraries interdependancies problems.

* Tue Aug 26 2008 Pavlov Konstantin <thresh@altlinux.ru> 14974-alt1
- 14974 revision.

* Thu Aug 14 2008 Pavlov Konstantin <thresh@altlinux.ru> 14754-alt1
- 14754 revision.

* Sun Jul 20 2008 Pavlov Konstantin <thresh@altlinux.ru> 14311-alt1
- 14311 revision.

* Mon Jul 07 2008 Pavlov Konstantin <thresh@altlinux.ru> 14095-alt1
- 14095 revision.

* Mon Jun 16 2008 Pavlov Konstantin <thresh@altlinux.ru> 13779-alt1
- 13779 revision.

* Sun Apr 20 2008 Pavlov Konstantin <thresh@altlinux.ru> 12910-alt1
- 12910 revision. 

* Fri Feb 29 2008 Pavlov Konstantin <thresh@altlinux.ru> 12278-alt1
- 12278 revision.

* Sat Feb 09 2008 Pavlov Konstantin <thresh@altlinux.ru> 11882-alt1
- 11882 revision.

* Tue Jan 29 2008 Pavlov Konstantin <thresh@altlinux.ru> 11656-alt1
- 11656 revision.
- Bumped libdirac version to 0.9.1-alt1.
- Pack patches as well. As they are generated from git branches and master
  already has them, they're not applied and used only as references on
  what was used to get %%name-%%version-%%release source.

* Fri Jan 11 2008 Pavlov Konstantin <thresh@altlinux.ru> 11504-alt1
- 11504 revision.
- Added crc.h to libavutil-devel package.
- Reverted commits about visibility-hidden stuff.

* Tue Dec 18 2007 Pavlov Konstantin <thresh@altlinux.ru> 11261-alt1
- 11261 revision.

* Tue Dec 11 2007 Pavlov Konstantin <thresh@altlinux.ru> 11199-alt3
- Enable XVMC for openchrome, thanks Andrey Liakhovets for patches.
  See https://bugzilla.altlinux.org/show_bug.cgi?id=13453 for more details.

* Tue Dec 11 2007 Pavlov Konstantin <thresh@altlinux.ru> 11199-alt2
- Fix post/postun for libavdevice.

* Sun Dec 09 2007 Pavlov Konstantin <thresh@altlinux.ru> 11199-alt1
- 1191 revision.

* Wed Dec 05 2007 Pavlov Konstantin <thresh@altlinux.ru> 11171-alt1
- 11171 revision.

* Tue Dec 04 2007 Pavlov Konstantin <thresh@altlinux.ru> 11162-alt1
- 11162 revision.

* Fri Nov 30 2007 Pavlov Konstantin <thresh@altlinux.ru> 11113-alt2
- Fix x86_64 build.
- Fix avdevice pkg-config file generation.

* Fri Nov 30 2007 Pavlov Konstantin <thresh@altlinux.ru> 11113-alt1
- 11113 revision.

* Sun Nov 25 2007 Pavlov Konstantin <thresh@altlinux.ru> 11090-alt1
- 11090 revision.

* Fri Nov 23 2007 Pavlov Konstantin <thresh@altlinux.ru> 11077-alt1
- 11077 revision. 

* Tue Nov 13 2007 Pavlov Konstantin <thresh@altlinux.ru> 11006-alt1
- 11006 revision.
- Removed libogg occurencies from spec file.

* Tue Nov 06 2007 Pavlov Konstantin <thresh@altlinux.ru> 10924-alt1
- 10924 revision.

* Sat Oct 27 2007 Pavlov Konstantin <thresh@altlinux.ru> 10864-alt1
- 10864 revision.

* Fri Oct 19 2007 Pavlov Konstantin <thresh@altlinux.ru> 10782-alt1
- 10782 revision.

* Sun Sep 30 2007 Pavlov Konstantin <thresh@altlinux.ru> 10629-alt1
- 10629 revision.

* Tue Sep 25 2007 Pavlov Konstantin <thresh@altlinux.ru> 10567-alt1
- 10567 revision.

* Wed Sep 19 2007 Pavlov Konstantin <thresh@altlinux.ru> 10533-alt1
- 10533 revision.

* Sat Sep 08 2007 Pavlov Konstantin <thresh@altlinux.ru> 10435-alt1
- 10435 revision.

* Fri Aug 24 2007 Pavlov Konstantin <thresh@altlinux.ru> 10203-alt1
- 10203 revision.

* Mon Aug 20 2007 Pavlov Konstantin <thresh@altlinux.ru> 10150-alt1
- 10150 revision.

* Sat Aug 18 2007 Pavlov Konstantin <thresh@altlinux.ru> 10141-alt1
- 10141 revision.

* Wed Aug 15 2007 Pavlov Konstantin <thresh@altlinux.ru> 10119-alt1
- 10119 revision.

* Thu Aug 02 2007 Pavlov Konstantin <thresh@altlinux.ru> 9867-alt1
- 8967 revision.

* Mon Jul 30 2007 Pavlov Konstantin <thresh@altlinux.ru> 9831-alt1
- 9831 revision.
- In case of failed libamr* dlopen , report where to look for the libraries.

* Thu Jul 19 2007 Pavlov Konstantin <thresh@altlinux.ru> 9756-alt1
- 9756 revision.
- amr_*b renamed to libamr_*b, following upstream changes (fix #12373).
- Revert removal of externs from header files.

* Wed Jul 18 2007 Pavlov Konstantin <thresh@altlinux.ru> 9734-alt1
- 9734 revision.
- New naming scheme: %%svnrelease-altN.
- Dropped unneeded Serial.

* Tue Jul 17 2007 Pavlov Konstantin <thresh@altlinux.ru> 1:0.4.9-alt1.svn9711
- 9711 revision.

* Sun Jul 15 2007 Pavlov Konstantin <thresh@altlinux.ru> 1:0.4.9-alt1.svn9685
- 9685 revision.

* Fri Jul 13 2007 Pavlov Konstantin <thresh@altlinux.ru> 1:0.4.9-alt1.svn9620
- 9620 revision.

* Thu Jul 12 2007 Pavlov Konstantin <thresh@altlinux.ru> 1:0.4.9-alt1.svn9606
- 9606 revision.
- Lowered version due to ffmpeg author complaints.
- Added serial.

* Sun Jul 08 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn9546
- 9546 revision.

* Tue Jul 03 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn9465
- 9465 revision.

* Wed Jun 27 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn9446
- 9446 revision.

* Mon Jun 25 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn9424
- 9424 revision.

* Sun Jun 24 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn9414
- 9414 revision.

* Fri Jun 22 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn9386
- 9386 revision.

* Thu Jun 21 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn9376
- 9376 revision.
- Removed all Requires: from libavcodec devel subpackage. Beware!
- Introduced libavutil subpackage + devels.

* Wed Jun 20 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn9375
- 9375 revision.

* Thu Jun 14 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn9308
- 9308 revision.

* Tue Jun 12 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn9290
- 9290 revision.
- Applied some of debian patches, see git repo for more details
  (branch debian).

* Sat Jun 09 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn9262
- 9266 revision.
- Merged XVMC stuff from led's daedalus package.
- Merged svn revision fix.

* Fri Jun 08 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn9255
- 9255 revision.

* Thu Jun 07 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn9237
- 9237 revision.

* Wed Jun 06 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn9233
- 9233 revision.
- Added libXvMC-devel to buildrequires.

* Tue Jun 05 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn9221
- 9221 revision.
- Added dsputil.h to libavcodec-devel subpackage.

* Mon Jun 04 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn9210
- 9210 revision.
- Fixed #11962.
- Removed swscaler on/off toggle.

* Fri Jun 01 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn9166
- 9166 revision.

* Tue May 29 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn9146
- 9146 revision.
- Remove all occurences of libdts and dca from spec file.

* Thu May 17 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn9047
- 9047 revision.
- Applied patches 02 and 03 from #11760, thanks Sergey Vlasov (vsu@).
- Build with external libdts and force disabling internal dca decoder.
- BuildRequires change: use texi2html instead of tetex-core.

* Mon May 07 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn8927
- 8927 revision.
- Redone git repository:
  - each "big" patch is now in separate branch.
  - master branch is a merge of all those branches + spec file + gear-rules.
- Added libX11-devel and libXext-devel to Requires to libavcodec-devel.

* Wed May 02 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn8868
- 8868 revision.
- Enabled x11grab.

* Fri Apr 27 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn8850
- 8850 revision.
- Added amr-dlopen patch by led@:
   If you want your ffmpeg/vlc/mplayer/whateva to play amr sound, you
   probably need to install corresponding amr libraries from my repository.
   Read README.ALT-AMR in libavcodec package for further details.
- Removed patch fixing build problems on x86_64, looks fixed upstream.

* Sat Apr 14 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn8733
- 8733 revision.
- Added patch fixing build problems on x86_64.

* Tue Apr 10 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn8703
- 8703 revision.

* Sun Apr 08 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn8673
- 8673 revision.

* Tue Apr 03 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn8597
- 8597 revision.

* Mon Mar 26 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn8526
- 8526 revision.

* Thu Mar 22 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn8486
- 8486 revision.

* Sat Mar 17 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn8434
- 8434 revision.

* Thu Mar 15 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn8416
- 8416 revision.

* Fri Mar 09 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn8307
- 8307 revision.

* Fri Mar 09 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn8304
- 8304 revision.

* Wed Mar 07 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn8288
- 8288 revision.

* Sat Mar 03 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn8206
- 8206 revision.

* Thu Mar 01 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn8176
- 8176 revision.

* Tue Feb 27 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn8146
- 8146 revision.
- Turns out that noone used dts from ffmpeg, let's disable it.

* Tue Feb 27 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn8144
- 8144 revision.
- Even if ffmpeg has its own dca decoder, let's build it with external libdts.

* Sun Feb 25 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn8122
- 8122 revision.
- Removed (erroneous) optlevel setting (fixes #10924).
- Fixed optflags.

* Sat Feb 24 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn8100
- 8100 revision.
- Added liba52 Require for libavcodec-devel.

* Fri Feb 23 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn8088
- 8088 revision.

* Wed Feb 21 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn8045
- 8045 revision.
- Temporarily disable -ffast-math as it results in segfaulting (gcc bug?).
- Fixed .pc files concerning dirac.

* Tue Feb 20 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn8031
- 8031 revision.

* Tue Feb 20 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn8030
- 8030 revision.

* Sun Feb 18 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn8022
- 8022 revision.

* Sun Feb 18 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn8011
- 8011 revision.
- Stricted imlib2-devel version to >= 1.3.0-alt1.

* Sat Feb 17 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn8001
- 8001 revision.

* Sat Feb 17 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn7991
- 7991 revision.

* Fri Feb 09 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn7900
- 7900 revision.
- Added dirac 0.6 support.

* Mon Feb 05 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn7822
- 7822 revision.
- Packing lzo.h: fixed #10773.

* Fri Feb 02 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn7801
- 7801 revision.

* Wed Jan 31 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn7771
- 7771 revision.
- Disabled:
  - libvorbis. Native encoding/decoding are already supported.
  - libxvid. Native encoding already supported.

* Wed Jan 31 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn7769
- 7769 revision.

* Fri Jan 26 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn7714
- 7714 revision.
- Added intreadwrite.h to libavcodec-devel subpackage.
- Enabled theora encoder.

* Wed Jan 24 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn7685
- 7685 revision.

* Sun Jan 21 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn7601
- 7601 revision.

* Sat Jan 20 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn7590
- 7590 revision.

* Wed Jan 17 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn7567
- 7567 revision.

* Sun Jan 14 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn7474
- 7474 revision.
- Added riff.h to HEADERS target to make MPlayer buildable.

* Mon Jan 08 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn7430
- 7430 revision.

* Sat Jan 06 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn7409
- 7409 revision.

* Mon Dec 25 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn7375
- 7375 revision.

* Sat Dec 16 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn7322
- 7322 revision.
- Fixed pkg-config files generation.

* Thu Dec 14 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn7317
- 7317 revision.

* Tue Dec 12 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn7290
- 7290 revision.

* Tue Nov 28 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn7178
- 7178 revision. 

* Sat Nov 18 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn7117
- 7117 revision.

* Fri Nov 17 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn7113
- 7113 revision.

* Thu Nov 16 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn7103
- 7103 revision.

* Wed Nov 15 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn7070
- 7070 revision.
- Should fix x86_64 build.

* Tue Nov 14 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn7060
- 7060 revision.

* Mon Nov 13 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn6994
- 6994 revision.
- ffmpeg banner now prints out some info about reporting bugs.

* Sun Nov 12 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn6983
- 6983 revision.
- Added a switch to deal with libnut, disabling it until libnut gets stable.

* Tue Nov 07 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn6930
- 6930 revision.
- Removed internal liba52, using the external one
  (should fix build on x86_64).

* Tue Nov 07 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn6928
- 6928 revision.
- //'ed the "configuration" line in ffmpeg.c.
- enabled a52, disabled a52bin.

* Mon Nov 06 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn6917
- 6917 revision.
- removed $arch stuff from configure line, don't be more clever than ffmpeg
  configure.

* Fri Nov 03 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn6891
- 6891 revision.

* Tue Oct 31 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn6847
- 6847 revision.

* Sun Oct 29 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn6834
- 6834 revision.

* Thu Oct 26 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn6795
- 6795 revision.
- enabling mmx on x86_64.

* Sat Oct 21 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn6750
- 6750 revision.

* Fri Oct 20 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn6748
- 6748 revision.

* Thu Oct 19 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn6736
- 6736 revision. 

* Wed Oct 18 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn6729
- 6729 revision.

* Tue Oct 17 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn6721
- 6721 revision.
- Stricted buildrequires to libx264 >= 0.0-alt54.

* Tue Oct 17 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn6716
- 6716 revision.

* Mon Oct 16 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn6704
- 6704 revision.

* Sat Oct 14 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn6687
- 6687 revision.

* Tue Oct 10 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn6624
- 6624 revision.

* Fri Oct 06 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn6567
- 6567 revision.

* Tue Oct 03 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn6533
- 6533 revision.

* Wed Sep 20 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn6366
- 6366 revision.

* Fri Sep 15 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn6287
- 6287 revision.
- Added libswscale-* packages.
- Upstream support for VP5/VP6.

* Sat Aug 12 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn5987
- 5987.
- Added strict Requires for libavcodec in libavformat package
  (should fix undefined symbol: av_get_bits_per_sample in libavformat).
- Added strict Requires for libffmpeg-devel subpackage.
- Added switch to deal with swscaler. Default:off.

* Sat Aug 05 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn5935
- 5935 revision.
- Moved on to git.
- Specfile major cleanup/rewrite/changes:
    - get rid of amr.
    - get rid of patches (they're moved on to git).
    - removed lzo support (upstream).
    -tuned %files section.
   - tuned %install section.
- Added support for xvmc.
- Initial support for VC1.
- Added bswap.h into HEADERS of libavutil/Makefile.
- Enabled --shlibdir=%%_libdir in configure.

* Tue Jun 13 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn5470.0
- 5470 revision.

* Wed Jun 07 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.svn5457.2
- SVN revision 5457.
- Move to new naming.
- Updated patch4.
- Removed patch9.
- Fixed erroneus configure options (thx led@).
- Removed libffmpeg requires from ffmpeg package.

* Sat Jun 03 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt1.20060516.1
- Synced with debian package:
   separate packages:
    libavcodec (-devel)
    libavformat (-devel)
    libpostproc (-devel)
   virtual packages:
    libffmpeg: requires libavcodec libavformat libpostproc
    libffmpeg-devel: requires libavcodec-devel libavformat-devel libpostproc-devel
- Moved requires section from libffmpeg-devel to libavcodec-devel.

* Tue May 30 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.5.0-alt0.20060516.1
- Based on a specfile by led@, changes include:
    - disabled a52
    - enabled a52bin
    - added CFLAGS for runtime CPU detection in libpostproc
    - fixed %name-cvs-20060516-configure.patch
    - many changes in spec
    - added %name-cvs-20060516-configure.patch
    - added %name-cvs-20060516-Makefile.patch
    - added %name-cvs-20060516-amr.patch
    - added AMR support
    - added packages: %name-vhook, lib%name-devel-static, ffplay, ffserver

- AMR support disabled by default due to unknown legal status of codecs.
- Added Requires: libdc1394-devel libgsm-devel libdca-devel libraw1394-devel 
  liblzo-devel to libffmpeg-devel package.

* Thu May 11 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.4.9.cvs20060511-alt1
- current CVS version.
- added build fixing patch #7 (by lioka@, frankly :).
- enabled dts.

* Mon Apr 10 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.4.9.cvs20060410-alt3
- current CVS version.

* Sat Feb 25 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.4.9.cvs20060225-alt3
- enabling x264, faac, faad, mp3lame and a52.
- current CVS version.
- updated patches: nobanner, alt-config.
- removed alt-soname patch.
- added includedir install patch. (#6).
- removed 'enable-shared-pp' from configure (doesn't exist in upstream anymore).

* Thu Feb 02 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.4.9.cvs20051105-alt1.1
- Rebuilt for new pkg-config dependencies.

* Sun Nov 20 2005 Kachalov Anton <mouse@altlinux.ru> 0.4.9.cvs20051105-alt1
- update to 20051105 CVS
- provide soname for each library to proper package provides

* Wed Nov 02 2005 Grigory Batalov <bga@altlinux.ru> 0.4.9-alt3cvs20050406
- quote percent symbol in "10%% faster" comment
- relax textrel check

* Wed Apr 13 2005 Grigory Batalov <bga@altlinux.ru> 0.4.9-alt2cvs20050406
- ffmpeg-config shows build time options (instead of predefined)
- libpostproc is built as shared library
- specfile cleanup

* Thu Apr 07 2005 Grigory Batalov <bga@altlinux.ru> 0.4.9-alt1cvs20050406
- new cvs snapshot for DVD VOBU sectors support
- legal issues, arch improvements and ffmpeg-config from Debian

* Wed Dec 22 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.4.9-alt0.5cvs20041113
- new cvs snapshot to build vlc-0.8.1

* Mon May 31 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.4.8-alt6cvs20040520
- new cvs snapshot to build vlc-0.7.2

* Thu Apr 15 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.4.8-alt5cvs20040222
- new cvs snapshot to build vlc-0.7.1

* Thu Jan 08 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.4.8-alt4cvs20040103
- install postprocess.h while MPlayer doesn't provides libposproc.
- fix build with faad.

* Mon Jan 05 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.4.8-alt3cvs20040103
- new cvs snapshot to build vlc-0.7.

* Fri Nov 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.4.8-alt2
- build with faad support.
- fixed imlib2 detection.
- fixed TEXTREL bug.

* Thu Oct 02 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.4.8-alt1
- 0.4.8

* Fri Jul 04 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.4.6-alt1cvs20030622
- cvs snapshot to build vlc-0.6.
- summary, descriptions by avp.

* Mon Mar 24 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.4.6-alt1cvs20030304
- cvs snapshot to build vlc.

* Sat Dec 28 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.4.6-alt1
- official release.

* Thu Dec 12 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.4.6-alt0.4cvs20021212
- current cvs snapshot.

* Fri Nov 01 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.4.6-alt0.3cvs20021101
- current cvs snapshot.

* Sun Jul 21 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.4.6-alt0.2cvs20020721
- current cvs snapshot (libname changed to libavcodec).
- ffserver.conf from documentation added in filelist as a config.

* Sat May 25 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.4.6-alt0.1cvs20020525
- First build for Sisyphus.

# }}}
