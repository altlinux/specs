Name: cinelerra
Version: 2.2.0CV
Release: alt2.20111217

# inline mmx assembly can cause text relocations
%set_verify_elf_method textrel=relaxed

Packager: Sergey Kurakin <kurakin@altlinux.org>

Summary: Complete production environment for audio and video
Summary(ru_RU.UTF8): Полнофункциональная система нелинейного видеомонтажа и аудиопроцессинга
License: GPL
Group: Video
Url: http://cinelerra.org/
Provides: hvirtual = 1.0.0
Obsoletes: hvirtual

Requires: libguicast = %version-%release
Requires: libquicktimehv = %version-%release
Requires: libmpeg3hv = %version-%release

Source: %name-%version.tar

Source1: %name-16x16.xpm
Source2: %name-32x32.xpm
Source3: %name-48x48.xpm
# manually generated from debian/*.sgml
Source4: %name.1
Source5: mplexhi.1
Source6: mplexlo.1
# fix this patch later!
Patch1: guicast-2.0-alt-prelink-am.patch
Patch6: cinelerra-1.2.2-gcc4-alt-renderfarmfsclient.patch
Patch7: cinelerra-2.1-alt-desktop.patch
Patch8: cinelerra-2.1-alt-cinelerra-makefile.am.patch
#Patch32: cinelerra-ffmpeg.patch
Patch34: cinelerra-2.1-remove-fontts.patch
Patch35: cinelerra-2.1.5-alt-fix_locale.patch
#Patch36: cinelerra-2.1-ffmpeg.patch
Patch37: cinelerra-2.1-faac.patch
Patch38: cinelerra-2.1-freefont2.patch
Patch39: cinelerra-2.1.5-alt-titler_font.patch
Patch40: cinelerra-2.1-alt-constant_macros.patch
Patch41: cinelerra-2.1-alt-libav.patch
%def_without libsndfilehv

# Automatically added by buildreq on Fri Mar 11 2011
BuildRequires: gcc-c++ imake libICE-devel libXv-devel libXxf86vm-devel liba52-devel libalsa-devel libavc1394-devel libavcodec-devel libdv-devel libesd-devel libfaad-devel libfftw3-devel libfreetype-devel libiec61883-devel libjpeg-devel liblame-devel libmjpegtools-devel libpng-devel libpostproc-devel libswscale-devel libtheora-devel libtiff-devel libuuid-devel libvorbis-devel libx264-devel openexr-devel texi2html xorg-cf-files nasm

%description
Cinelerra is a complete audio and video authoring
tool. It understands a lot of multimedia formats
(quicktime, avi, ogg) and audio/video compression
codecs (divx, xvid, mpeg1/2, ...)

It's about transforming the impossible into reality. The best program
for video and audio manipulation. Install this, if you need editing
and creating video.

%description -l ru_RU.UTF8
Полнофункциональная система нелинейного видеомонтажа и аудиопроцессинга.
Большое количество видео и аудио фильтров, возможность создания
собственных профессиональных фильмов. Если вам необходим видеомонтаж
под Linux -- это лучшая программа для решения ваших задач.

%package -n libguicast
Group: System/Libraries
Summary: A toolkit library
%description -n libguicast
libguicast is a toolkit library mainly used by HeroineVirtual's
softwares

%package -n libguicast-devel
Group: Development/C
Requires: libguicast = %version-%release
Summary: A toolkit library
%description -n libguicast-devel
libguicast is a toolkit library mainly used by HeroineVirtual's
softwares

This package holds development files for the libguicast library

%if_with libsndfilehv
%package -n libsndfilehv
Group: System/Libraries
Summary: A custom modified Cinelerra's libsndfile library
%description -n libsndfilehv
Custom modified Cinelerra's libsndfile library
%endif

%package -n libquicktimehv
Group: System/Libraries
Summary: Quicktime 4 Linux Cinelerra internal library
%description -n libquicktimehv
Quicktime 4 Linux was the first convenient way to read and write
uncompressed Quicktime movies on Linux. Today Quicktime 4 Linux
is intended for content creation and uncompressed movies. These
usually arise during the production phase and not the consumer
phase of a movie. It has improvements in colormodel support,
bit depth, accuracy, reliability, and codecs, while not
stressing economy.

Users wishing for a consumer library should use OpenQuicktime or FFMPEG.

For more informations, see http://heroinewarrior.com/quicktime.php3

%package -n libquicktimehv-devel
Group: Development/C
Requires: libquicktimehv = %version-%release
Summary: Quicktime 4 Linux (Cinelerra internal) library (development files)
%description -n libquicktimehv-devel
Quicktime 4 Linux was the first convenient way to read and write
uncompressed Quicktime movies on Linux. Today Quicktime 4 Linux
is intended for content creation and uncompressed movies. These
usually arise during the production phase and not the consumer
phase of a movie. It has improvements in colormodel support,
bit depth, accuracy, reliability, and codecs, while not
stressing economy.

Users wishing for a consumer library should use OpenQuicktime or FFMPEG.

This package holds development files for the Quicktime 4 Linux library

For more informations, see http://heroinewarrior.com/quicktime.php3

%package -n libmpeg3hv
Group: System/Libraries
Summary: advanced editing and manipulation of MPEG streams (cinelerra's internal)
%description -n libmpeg3hv
Libmpeg3 supports advanced editing and manipulation of MPEG streams.
MPEG is normally a last mile format but with libmpeg3 you can edit
it like a first mile solution.

Unless you have a need for MPEG editing and copying, you're better
off using a consumer library like FFMPEG.

For more informations, see http://heroinewarrior.com/quicktime.php3

%package -n libmpeg3hv-devel
Group: Development/C
Requires: libmpeg3hv = %version-%release
Summary: advanced editing and manipulation of MPEG streams (development files)
%description -n libmpeg3hv-devel
Libmpeg3 supports advanced editing and manipulation of MPEG streams.
MPEG is normally a last mile format but with libmpeg3 you can edit
it like a first mile solution.

Unless you have a need for MPEG editing and copying, you're better
off using a consumer library like FFMPEG.

This package holds development files for the libmpeg3 library

For more informations, see http://heroinewarrior.com/quicktime.php3

%package -n libmpeg3hv-utils
Group: Video
Requires: libmpeg3hv = %version-%release
Summary: advanced editing and manipulation of MPEG streams (development files)
%description -n libmpeg3hv-utils
Libmpeg3 supports advanced editing and manipulation of MPEG streams.
MPEG is normally a last mile format but with libmpeg3 you can edit
it like a first mile solution.

Unless you have a need for MPEG editing and copying, you're better
off using a consumer library like FFMPEG.

This package holds utilities for the libmpeg3 library

For more informations, see http://heroinewarrior.com/quicktime.php3

%package manual
Group: Books/Other
Summary: Cinelerra CV manual, english
BuildArch: noarch
%description manual
This manual originates from "Secrets of Cinelerra", an excellent primer
written by Adam WILLIAMS. Nicolas MAUFRAIS combined the original
"Secrets of Cinelerra" with the contents from Wiki into a unified
document, packaged here.


%prep
%setup  -n %name-%version
%patch1 -p0
%patch6 -p1
%patch7 -p1
%patch8 -p1
#patch32 -p1
%patch34 -p1
%patch35 -p1
#patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1

%build
#./autogen.sh
AUTOPOINT=true %autoreconf

CONFFLAGS="--with-plugindir=%_libdir/%name \
	--enable-freetype2 \
	--with-external-ffmpeg \
	--disable-3dnow \
	--with-gnu-ld \
	--with-fontsdir=/usr/share/fonts \
"

#ifarch athlon
#  CONFFLAGS="$CONFFLAGS --enable-3dnow"
#  %%add_optflags -m3dnow
#endif
#ifarch i586
#  #remove_optflags -march=i586 -mtune=i686 -mcpu=i686
# anyway, it'll not run on p133/64mb -- p4/1GB is recommended :(
# furthermore, on old garbage like pmmx/pII/k6 we really need ALL optimizations
#  #add_optflags -march=pentium-mmx -mtune=i686
#endif

%ifarch powerpc
%else
	%define _optlevel 3
	%add_optflags -ffast-math -mmmx -minline-all-stringops -fprefetch-loop-arrays -funroll-loops
	#add_optflags -msse -m3dnow # athlonXP
	#add_optflags -msse -msse2 # p4
	CXXFLAGS="%optflags -fno-check-new"
	%ifarch ix86
		%add_optflags %optflags_kernel
		CONFFLAGS="$CONFFLAGS --enable-mmx --enable-x86 --enable-opengl"
		# uncomment --without-pic if build fails with --enable-x86 --enable-mmx
		# CONFFLAGS="$CONFFLAGS --without-pic"
	%endif
%endif

%configure $CONFFLAGS
%make_build

# manual
pushd doc
texi2html --nosec-nav --no-menu --split chapter cinelerra_cv_manual_en.texi --output=. --toc-file=index.html
rm -f manual_images_{intl,en}/*.xcf
popd

%install
%makeinstall plugindir=%buildroot%_libdir/%name

# rename the mpeg3 utils so they can be installed alongside SuSE native versions
pushd %buildroot%prefix/bin
#  mv mpeg3toc mpeg3toc.hv
#  mv mpeg3cat mpeg3cat.hv
#  mv mpeg3dump mpeg3dump.hv
  ln -s %_bindir/mpeg2enc %buildroot%_libdir/cinelerra/mpeg2enc.plugin
popd

%if_with chrpath
chrpath -d %buildroot%_libdir/libguicast.so.?.?.?
%endif

# hack to properly build foreign guicast
cp quicktime/colormodels.h %buildroot%_includedir/quicktime
cp quicktime/libdv.h %buildroot%_includedir/quicktime

# Install icons
# backwards compatibility with Master 2x/Compact 30
%{?!_niconsdir:%define _niconsdir %_iconsdir}
install -D -m 644 %SOURCE1 %buildroot%_miconsdir/%name.xpm
install -D -m 644 %SOURCE2 %buildroot%_niconsdir/%name.xpm
install -D -m 644 %SOURCE3 %buildroot%_liconsdir/%name.xpm
# replacing with new native icon
mv %buildroot%_pixmapsdir/cinelerra.xpm %buildroot%_liconsdir/%name.xpm

# man pages
install -d -m 755 %buildroot%_man1dir
install -D -m 644 %SOURCE4 %SOURCE5 %SOURCE6 %buildroot%_man1dir

#fixing *hv-flavour
mv %buildroot%_includedir/mpeg3 %buildroot%_includedir/mpeg3hv
mv %buildroot%_includedir/quicktime %buildroot%_includedir/quicktimehv
pushd %buildroot%_includedir; ln -s quicktimehv quicktime; popd

# libguicast-devel
install -d -m755 %buildroot%_includedir/guicast
install -m644 guicast/*.h guicast/*.inc %buildroot%_includedir/guicast
cp guicast/bootstrap %buildroot%_bindir/guicast_bootstrap1

%find_lang %name

%files -f %name.lang
%doc AUTHORS
%dir %_libdir/cinelerra
%_bindir/cinelerra
%_bindir/mplexlo
%_libdir/cinelerra/*.so
%exclude %_libdir/cinelerra/*.la
%_libdir/cinelerra/shapewipe
%_libdir/cinelerra/mpeg2enc.plugin
%_miconsdir/%name.xpm
%_niconsdir/%name.xpm
%_liconsdir/%name.xpm
%_desktopdir/%name.desktop
%_man1dir/*

%if_with libsndfilehv
%files -n libsndfilehv
%_libdir/libsndfile*.so*
%endif

%files -n libguicast
%_libdir/libguicast.so.?*

%files -n libguicast-devel
%_libdir/libguicast.so
%_includedir/guicast
%_bindir/guicast_bootstrap1

%files -n libmpeg3hv-devel
%docdir libmpeg3/docs
%_libdir/libmpeg3hv.*
%_includedir/mpeg3hv/

%files -n libmpeg3hv
%_libdir/libmpeg3hv-*.so*

%files -n libmpeg3hv-utils
%_bindir/mpeg*

%files -n libquicktimehv-devel
%docdir quicktime/docs
%_libdir/libquicktimehv.*
%_includedir/quicktime
%dir %_includedir/quicktimehv
%_includedir/quicktimehv/quicktime.h
%_includedir/quicktimehv/qtprivate.h
%_includedir/quicktimehv/colormodels.h
%_includedir/quicktimehv/libdv.h

%files -n libquicktimehv
%_libdir/libquicktimehv-*.so*

%files manual
%doc doc/*.html
%doc doc/manual_images_{en,intl}
%doc doc/README_en

%changelog
* Thu May 31 2012 Sergey Kurakin <kurakin@altlinux.org> 2.2.0CV-alt2.20111217
- 2011.12.17 upstream git snapshot fixes build (-lmp3lame)

* Wed Mar 28 2012 Sergey Kurakin <kurakin@altlinux.org> 2.2.0CV-alt1
- 2.2.0CV

* Mon Jan 30 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.5CV-alt3.2
- rebuilt with recent libav/x264, again

* Mon Aug 01 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.5CV-alt3.1
- rebuilt with recent libav/x264

* Mon Apr 25 2011 Sergey Kurakin <kurakin@altlinux.org> 2.1.5CV-alt3
- fixed font encoding issue (closes: #25499)

* Fri Mar 11 2011 Sergey Kurakin <kurakin@altlinux.org> 2.1.5CV-alt2
- fixed build (Buildreq)

* Fri Dec 10 2010 Sergey Kurakin <kurakin@altlinux.org> 2.1.5CV-alt1
- 2.1.5CV
- build with OpenGL

* Wed Nov 17 2010 Sergey Kurakin <kurakin@altlinux.org> 2.1-alt1.20100825
- 2010.08.25 upstream git snapshot:
  + fixed build with newest libx264
  + SOWT audio codec support
- directory ownership fixed
- build the user's manual as subpackage

* Wed Sep 22 2010 Sergey Kurakin <kurakin@altlinux.org> 2.1-alt1.20100721
- 20100721 snapshot from cinelerra-cv's git
- fixed build
- titler plugin: fixed search for available fonts
- repaired and reenabled locale-fix patch, originally written
  by ruslandh@ (closes: #23132)
- minor spec cleanup

* Wed Feb 03 2010 Afanasov Dmitry <ender@altlinux.org> 2.1-alt1.20091107.2
- rebuild with libx264.so.85

* Sat Nov 07 2009 Hihin Ruslan <ruslandh@altlinux.ru> 2.1-alt1.20091107.1
- add :
 cinelerra-2.1-faac.patch
 cinelerra-2.1-fix-freefont2.patch
 cinelerra-2.1-fix-font.patch
- default LC_MESSAGES="C"

* Sat Sep 19 2009 Hihin Ruslan <ruslandh@altlinux.ru> 2.1-alt1.1061.2
- add cinelerra-2.1-ffmpeg.patch

* Fri Feb 27 2009 Hihin Ruslan <ruslandh@altlinux.ru> 2.1-alt1.1061.1
- fixed in BuildRequires

* Mon Feb 02 2009 Hihin Ruslan <ruslandh@altlinux.ru> 2.1-alt0.9.1061.1
- add cinelerra-ffmpeg.patch, cinelerra-2.1-remove-fontts.patch,
  cinelerra-2.1-locale-fix.patch
- picked up from orphaned

* Thu Aug 07 2008 Igor Vlasenko <viy@altlinux.ru> 2.1-alt0.9.1061
- fixes in gettext
- svn revision 1061

* Fri May 30 2008 Igor Vlasenko <viy@altlinux.ru> 2.1-alt0.8.1056
- svn revision 1056

* Mon Oct 08 2007 Igor Vlasenko <viy@altlinux.ru> 2.1-alt0.7.1036
- svn revision 1036

* Mon Apr 02 2007 Igor Vlasenko <viy@altlinux.ru> 2.1-alt0.6.1007
- svn revision 1007

* Fri Feb 02 2007 Igor Vlasenko <viy@altlinux.ru> 2.1-alt0.6.986
- svn revision 986

* Mon Jan 22 2007 Igor Vlasenko <viy@altlinux.ru> 2.1-alt0.6.984
- new snapshot 984, spec sync with spec.in

* Mon Jan 15 2007 Igor Vlasenko <viy@altlinux.ru> 2.1-alt0.5.980
- svn revision 980
- merged 1.2.2-alt10
- --with-external-ffmpeg

* Wed Dec 13 2006 Igor Vlasenko <viy@altlinux.ru> 2.1-alt0.4.961
- svn revision 961
- opengl support disabled by default (nvidia specific)
- merged x86_64 support (a great thanks to rider@ for sandbox)

* Mon Sep 25 2006 Igor Vlasenko <viy@altlinux.ru> 2.1-alt0.2.909
- svn revision 909

* Fri Sep 22 2006 Igor Vlasenko <viy@altlinux.ru> 2.1-alt0.2.894
- import of heroines cinelerra 2.1 completed - new version 2.1
- svn revision 894

* Sat Sep 16 2006 Igor Vlasenko <viy@altlinux.ru> 2.0-alt0.1.885
- svn revision 885

* Wed Sep 13 2006 Igor Vlasenko <viy@altlinux.ru> 2.0-alt0.1
- first build for Daedalus

* Fri Jun 23 2006 Igor Vlasenko <viy@altlinux.ru> 2.0-alt0
- test build

* Mon May 29 2006 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt6
- C++ fixes for gcc 4
- built with libdts,

* Fri Mar 24 2006 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt5
- added %_bindir/guicast_bootstrap to libguicast-devel

* Fri Mar 24 2006 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt4
- removed useless rpath with chrpath
- added _niconsdir

* Sun Feb 05 2006 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt3
- prelink support with guicast-alt-prelink-am.patch
- ifarch ix86 for x86_64 support

* Mon Nov 21 2005 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt2
- added %_includedir/quicktime to libquicktimehv-devel
- added colormodels.h & libdv.h to libquicktimehv-devel
- fixed russian Summary && description

* Fri Oct 28 2005 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1
- removed phantom python build dependencies

* Mon Oct 10 2005 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt0.9
- picked up from orphaned;
- new version;
- new build process based on ``unofficial'' cvs.cinelerra.org
- my patch for Minolta Z3
- split into packages

* Fri Sep 12 2003 Alexander Belov <asbel@altlinux.ru> 1.1.7-alt1
- New version
- Added koi8 russian description and summary to package
- New BuildRequires

* Tue May 20 2003 Alexander Belov <asbel@altlinux.ru> 1.1.6-alt2
- Fixed instalation bug

* Fri May 16 2003 Alexander Belov <asbel@altlinux.ru> 1.1.6-alt1
- New version and new name of package

* Wed Oct 23 2002 AEN <aen@altlinux.ru> 1.0.0-alt2
- first build for Sisyphus, thnx to Alexander Belov!
- MS fonts removed

* Wed Oct 16 2002 Alexander Belov <asbel@mail.ru> 1.0.0-alt1
- Initial release
