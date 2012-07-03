%def_enable gpl

%def_with ffmpeg
%def_without faac
%def_with x264
%def_with lame
%def_without libdv
%def_with libjpeg
%def_with libpng
%def_with faad2
%def_with alsa
%def_with gtk
%def_with doxygen
%def_with opengl
%def_with vorbis

%def_disable static
%define _unpackaged_files_terminate_build 1

%define upstreamname libquicktime
%define _pkgdocdir %_docdir/%upstreamname-%version
%define pluginsdir %_libdir/%upstreamname-%version
%define abiver 111
%define libname %upstreamname%abiver
%define corename %libname-core
Name: %libname
Version: 1.2.2
Release: alt1.4

Summary: A library for manipulating QuickTime files
%if_with gpl
License: GPL
%else
License: LGPL
%endif
Group: Video
Url: http://libquicktime.sourceforge.net
Packager: Afanasov Dmitry <ender@altlinux.org>

# http://dl.sf.net/libquicktime/libquicktime-%version.tar.gz
Source: libquicktime-%version.tar
Patch1: libquicktime-1.1.1-soname_hack-alt.patch
Patch2: libquicktime-1.0.2-alt-fix-libswscale.patch
Patch3: libquicktime-%version-alt-versioned-gettext-domain.patch
Patch4: libquicktime-1.1.1-libav07.patch

Patch100: libquicktime-%version-alt-changes.patch

%define dv_ver 0.102

# Automatically added by buildreq on Sun Jan 29 2006
BuildRequires: gcc-c++ libstdc++-devel 
BuildRequires: fontconfig freetype2 glib2-devel pkg-config libX11-devel zlib-devel
BuildRequires: libpango-devel libXaw-devel libICE-devel libXext-devel libXv-devel
BuildRequires: yasm nasm
BuildRequires: libavc1394-devel libraw1394-devel

%{?_with_ffmpeg:BuildRequires: libavcodec-devel libswscale-devel}
%{?_with_faac:BuildRequires: libfaac-devel}
%{?_with_x264:BuildRequires: libx264-devel}
%{?_with_lame:BuildRequires: liblame-devel}
%{?_with_libdv:BuildRequires: libdv-devel >= %dv_ver}
%{?_with_libjpeg:BuildRequires: libjpeg-devel}
%{?_with_libpng:BuildRequires: libpng-devel}
%{?_with_faad2:BuildRequires: libfaad-devel}
%{?_with_alsa:BuildRequires: libalsa-devel}
%{?_with_vorbis:BuildRequires: libogg-devel libvorbis-devel}
%{?_with_gtk:BuildRequires: libgtk+2-devel}
%{?_with_opengl:BuildRequires: libGL-devel}
%{?_with_doxygen:BuildRequires: doxygen}

# for documentation

%description
Libquicktime is a library for reading and writing QuickTime files on
UNIX systems. Video CODECs supported by this library are OpenDivX, MJPA,
JPEG Photo, PNG, RGB, YUV 4:2:2, and YUV 4:2:0 compression.  Supported
audio CODECs are Ogg Vorbis, IMA4, ulaw, and any linear PCM format.

Libquicktime is based on the quicktime4linux library. Libquicktime add
features such as a GNU build tools-based build process and dynamically
loadable CODECs.

%package -n %libname-core
Summary: library for reading and writing QuickTime files
Group: Video
Provides: libquicktime = %version-%release

Obsoletes: libquicktime-xanim, libquicktime-svq, libquicktime-cinepak
Provides: libquicktime-xanim = %version-%release, libquicktime-svq  = %version-%release, libquicktime-cinepak = %version-%release

%description -n %libname-core
Libquicktime is a library for reading and writing QuickTime files on
UNIX systems. Video CODECs supported by this library are OpenDivX, MJPA,
JPEG Photo, PNG, RGB, YUV 4:2:2, and YUV 4:2:0 compression.  Supported
audio CODECs are Ogg Vorbis, IMA4, ulaw, and any linear PCM format.

Libquicktime is based on the quicktime4linux library. Libquicktime add
features such as a GNU build tools-based build process and dynamically
loadable CODECs.

%package -n %upstreamname-devel
Summary: Header files for libquicktime
Group: Development/C
Requires: %corename = %version-%release
Requires: glib2-devel
Requires: libpng-devel
Requires: libjpeg-devel
Requires: libdv-devel
Requires: libraw1394-devel
Requires: libavc1394-devel
Requires: libogg-devel
Requires: libvorbis-devel

%description -n %upstreamname-devel
Header files for libquicktime.

%package -n %upstreamname-devel-doc
Summary: Development documentation for libquicktime
Group: Development/C
#Requires: %upstreamname-devel = %version-%release
BuildArch: noarch

%description -n %upstreamname-devel-doc
Development documentation (API reference) for libquicktime.

%package -n %libname-utils
Summary: Useful tools to operate at QuickTime files
Group: Video
Requires: %corename = %version-%release
Provides: %upstreamname-utils = %version-%release

%description -n %libname-utils
Useful tools to operate on QuickTime files.

%package -n %libname-plugins
Summary: Set of libquicktime plugins to support additional formats
Group: Video
Requires: %corename = %version-%release

%{?_with_faac:Requires: %libname-faac = %version-%release}
%{?_with_ffmpeg:Requires: %libname-ffmpeg = %version-%release}
%{?_with_x264:Requires: %libname-x264 = %version-%release}
%{?_with_faad2:Requires: %libname-faad2 = %version-%release}
%{?_with_lame:Requires: %libname-lame = %version-%release}
%{?_with_vorbis:Requires: %libname-vorbis = %version-%release}
%{?_with_libdv:Requires: %libname-dv = %version-%release}

Provides: %upstreamname-plugins = %version-%release

%description -n %libname-plugins
%summary

%package -n %libname-vorbis
Summary: Libquicktime plugin supporting the Ogg Vorbis codec
Group: Video
Requires: %corename = %version-%release
Provides: %upstreamname-vorbis = %version-%release

%description -n %libname-vorbis
Libquicktime plugin supporting the Ogg Vorbis codec.


%package -n %libname-ffmpeg
Summary: Libquicktime plugin supporting the ffmpeg codec
Group: Video
Requires: %corename = %version-%release
Provides: %upstreamname-ffmpeg = %version-%release

%description -n %libname-ffmpeg
Libquicktime plugin supporting the ffmpeg codec

%package -n %libname-lame
Summary: Libquicktime plugin supporting the Lame codec
Group: Video
Requires: %corename = %version-%release
Provides: %upstreamname-lame = %version-%release

%description -n %libname-lame
Libquicktime plugin supporting the Lame codec.

%package dv
Summary: Libquicktime plugin supporting the DV codec
Group: Video
Requires: %corename = %version-%release
Requires: libdv >= %dv_ver
Provides: %upstreamname-dv = %version-%release

%description dv
Libquicktime plugin supporting the DV codec.


%package -n %libname-faac
Summary: Libquicktime plugin supporting the Faac codec
Group: Video
Requires: %corename = %version-%release
Provides: %upstreamname-faac = %version-%release

%description -n %libname-faac
Libquicktime plugin supporting the Faac codec.


%package -n %libname-faad2
Summary: Libquicktime plugin supporting the Faad2 codec
Group: Video
Requires: %corename = %version-%release
Provides: %upstreamname-faad2 = %version-%release

%description -n %libname-faad2
Libquicktime plugin supporting the Faad2 codec.


%package -n %libname-x264
Summary: Libquicktime plugin supporting the x264 codec
Group: Video
Requires: %corename = %version-%release
Provides: %upstreamname-x264 = %version-%release

%description -n %libname-x264
Libquicktime plugin supporting the x264 codec.


%package -n %upstreamname-devel-static
Summary: Static libquicktime libraries
Group: Development/C
Requires: %upstreamname-devel = %version-%release

%description -n %upstreamname-devel-static
Static libquicktime libraries.


%prep
%setup -q -n %upstreamname-%version
%patch1 -p1
#patch2 -p1
%patch3 -p1
%patch4 -p1

%patch100 -p1

subst 's/^\(AM_GNU_GETTEXT_VERSION.*\)/# \1/' configure.ac;
subst 's/^SOVERSION.*/SOVERSION=%abiver/' configure.ac;

%build
%autoreconf

%define _optlevel 3
%configure \
    %{subst_enable gpl} \
    %{subst_enable static} \
    %{subst_with x264} \
    %{subst_with faac} \
    %{subst_with ffmpeg} \
    %{subst_with lame} \
    %{subst_with libdv} \
    %{subst_with libjpeg} \
    %{subst_with libpng} \
    %{subst_with faad2} \
    %{subst_with alsa} \
    %{subst_with gtk} \
    %{subst_with doxygen} \
    %{subst_with opengl} \
    --with-cpuflags="$CFLAGS" \
%ifnarch i586 i686 athlon
    --disable-mmx \
%endif

%make_build

%install
%make_install DESTDIR=%buildroot install

mkdir -p %buildroot%_pkgdocdir/doc
cp README TODO %buildroot%_pkgdocdir
cp doc/*.html %buildroot%_pkgdocdir/doc

%find_lang %libname

# remove non-packaged files
rm -f %buildroot%pluginsdir/*.la

%files -n %corename -f %libname.lang
%_libdir/*.so.*
%dir %pluginsdir
%pluginsdir/lqt_audiocodec.so
%{?_with_libjpeg:%pluginsdir/lqt_rtjpeg.so}
%{?_with_libpng:%pluginsdir/lqt_png.so}
%{?_with_libjpeg:%pluginsdir/lqt_mjpeg.so}
%pluginsdir/lqt_videocodec.so
%dir %_pkgdocdir
%_pkgdocdir/README
%_pkgdocdir/TODO

%files -n %libname-utils
%_bindir/*
%_man1dir/*

%files -n %libname-plugins

%if_with vorbis
%files -n %libname-vorbis
%pluginsdir/lqt_vorbis.so
%endif

%if_with ffmpeg
%files -n %libname-ffmpeg
%pluginsdir/lqt_ffmpeg.so
%endif

%if_with lame
%files -n %libname-lame
%pluginsdir/lqt_lame.so
%endif

%if_with libdv
%files -n %libname-dv
%pluginsdir/lqt_dv.so
%endif

%if_with faac
%files -n %libname-faac
%pluginsdir/lqt_faac.so
%endif

%if_with faad2
%files -n %libname-faad2
%pluginsdir/lqt_faad2.so
%endif

%if_with x264
%files -n %libname-x264
%pluginsdir/lqt_x264.so
%endif

%files -n %upstreamname-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%files -n %upstreamname-devel-doc
%_pkgdocdir/doc

%if_enabled static
%files -n %upstreamname-devel-static
%_libdir/*.a
%pluginsdir/*.a
%endif

%changelog
* Tue Jan 31 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.2-alt1.4
- artificial req on libffmpeg dropped

* Mon Jan 30 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.2-alt1.3
- rebuilt with recent libav/x264, again

* Mon Aug 01 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.2-alt1.2
- rebuilt with recent libav/x264

* Sun Mar 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1.1
- BuildRequires: replaced xorg-x11-devel by libX11-devel, libXaw-devel,
  libICE-devel, libXext-devel and libXv-devel

* Mon Jan 10 2011 Afanasov Dmitry <ender@altlinux.org> 1.2.2-alt1
- 1.2.2 release.

* Fri Dec 24 2010 Afanasov Dmitry <ender@altlinux.org> 1.2.1-alt1
- 1.2.1 release.
  + lqt-config was removed.

* Mon Dec 20 2010 Igor Vlasenko <viy@altlinux.ru> 1.1.5-alt1.1
- uploaded NMU of Eugeny A. Rostovtsev (REAL) <real at altlinux.org>:
  Fixed build

* Wed Feb 24 2010 Afanasov Dmitry <ender@altlinux.org> 1.1.5-alt1
- 1.1.5 release.

* Wed Feb 03 2010 Afanasov Dmitry <ender@altlinux.org> 1.1.4-alt2
- rebuild with libx264.so.85

* Mon Jan 25 2010 Afanasov Dmitry <ender@altlinux.org> 1.1.4-alt1
- 1.1.4 release.

* Sat Sep 26 2009 Afanasov Dmitry <ender@altlinux.org> 1.1.3-alt2
- disable faac (closes: #21718)
- update spec macroses

* Fri Aug 28 2009 Afanasov Dmitry <ender@altlinux.org> 1.1.3-alt1
- 1.1.3 release.

* Wed Jul 08 2009 Afanasov Dmitry <ender@altlinux.org> 1.1.2-alt1
- 1.1.2 release.

* Tue Jun 23 2009 Afanasov Dmitry <ender@altlinux.org> 1.1.1-alt5
- rebuild with libpng12-1.2.37-alt2

* Wed Apr 15 2009 Dmitry V. Levin <ldv@altlinux.org> 1.1.1-alt4
- Renamed to libquicktime111.

* Wed Apr 15 2009 Afanasov Dmitry <ender@altlinux.org> 1.1.1-alt3
- change packager

* Wed Apr 15 2009 Afanasov Dmitry <ender@altlinux.org> 1.1.1-alt2
- first build from gear
- add patch for versioning translation files. gettext domain now
  is %libname
- rewrite patch for versioned plugins directory. directory is set
  trough pkglibdir.
- rewrite dependancies:
  + plugins subpackage must require %libname-* when it has required
    %upstreamname-* packages.
  + move forgotten historical dependacies to the right place.

* Sun Apr 12 2009 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1
- new version
- added plugins subpackage
- sharedlibs policy:
  + pluginsdir is now versioned to allow compat libraries
  + versioned package name

* Sun Jan 04 2009 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt6
- fixed repocop warnings

* Fri Jan 02 2009 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt5
- replaced dependency on anyasm

* Sat Dec 20 2008 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt4
- removed obsolete dependency libjpeg-mmx-devel

* Fri Dec 12 2008 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt3
- temporally disabled x264 plugin

* Mon Sep 29 2008 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2
- fixed build with new ffmpeg

* Mon Jun 9 2008 Yury Aliaev <mutabor@altlinux.ru> 1.0.2-alt1
- new version
- reverted back OpenDivX support from 0.9.8
- development documentation put into the separate package devel-doc
- soname versioning hack added

* Sat Sep 16 2006 Igor Vlasenko <viy@altlinux.ru> 0.9.8-alt6
- enabled ffmpeg (current Sisyphus allows it again)

* Sat May 06 2006 Igor Vlasenko <viy@altlinux.ru> 0.9.8-alt5
- disabled ffmpeg
- faac plugin is enabled again

* Fri Feb 24 2006 Igor Vlasenko <viy@altlinux.ru> 0.9.8-alt4
- disabled CPU build detection --with-cpuflags

* Wed Feb 08 2006 Igor Vlasenko <viy@altlinux.ru> 0.9.8-alt3
- enabled ffmpeg

* Mon Feb 06 2006 Igor Vlasenko <viy@altlinux.ru> 0.9.8-alt2
- s/xorg-x11-devel-static/xorg-x11-devel/

* Sun Jan 29 2006 Igor Vlasenko <viy@altlinux.ru> 0.9.8-alt1
- new version;
- changed license to GPL (enables faad2 && faac codecs)
- removed libjpeg-mmx-devel on x86_64 (thanks to rider@)

* Sun Dec 18 2005 Igor Vlasenko <viy@altlinux.ru> 0.9.8-alt0.1.pre2
- new version 0.9.8-pre2

* Sun Dec 18 2005 Igor Vlasenko <viy@altlinux.ru> 0.9.7-alt4
- applied spec cleanup of Vitaly Lipatov
  (removed broken dependency gtk+-devel)

* Fri Sep 30 2005 Igor Vlasenko <viy@altlinux.ru> 0.9.7-alt3
- fix #6687 (license is LGPL, not GPL)
- plugins removed from main package again (fixed alt1.1)

* Thu Sep 22 2005 Igor Vlasenko <viy@altlinux.ru> 0.9.7-alt2
- merged Vitaly Lipatov work with my backport branch; thanks

* Fri Sep 09 2005 Vitaly Lipatov <lav@altlinux.ru> 0.9.7-alt1.1
- fix owner of %_libdir/libquicktime

* Sat Aug 27 2005 Vitaly Lipatov <lav@altlinux.ru> 0.9.7-alt1
- new version
- disable build with glib/gnome1 libraries

* Fri Aug 26 2005 Igor Vlasenko <viy@altlinux.ru> 0.9.7-alt0.M24.2
- added my patch to fix crashes on some MOVs

* Tue Jul 19 2005 Igor Vlasenko <viy@altlinux.org> 0.9.7-alt0.M24.1
- backport to M24, changed buildrequires

* Fri Jan 14 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.9.4-alt1
- 0.9.4

* Wed Jul 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.9.3-alt1
- 0.9.3
- obsoletes libquicktime-{xanim,svq,cinepak}
- new Lame plugin.

* Mon Jun 07 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.9.2-alt1.3
- rebuild with libdv-0.102

* Tue Dec 02 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.9.2-alt1.2
- do not package .la files.
- do not build devel-static subpackage by default.
- use %%set_verify_elf_method textrel=relaxed, I can't fix rtjpeg
  asm code.

* Mon Oct 13 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.9.2-alt1.1
- disabled ffmpeg plugin due not ready for new ffmpeg.

* Wed Oct 01 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.9.2-alt1
- 0.9.2 release.

* Wed Nov 20 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.9.2-alt0.8pre1
- 0.9.2pre1.

* Sun Jul 21 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.9.1-alt1
- First build for Sisyphus.
