%def_with quicktime

Name: kino
Version: 1.3.4
Release: alt7

Summary: Non-linear DV editor
Group: Video
License: GPL

Url: http://www.kinodv.org
Source: http://dl.sf.net/%name/%name-%version.tar.gz
Source1: %name-48x48.xpm
Source2: %name-32x32.xpm
Source3: %name-16x16.xpm
Source4: Kino.desktop
Source5: kino-1.3.4-ru.po.bz2
Patch1: kino-1.3.4-alt-alsa-default.patch
Patch2: kino-1.3.4-alt-makefile-libxml2.patch
Patch3: kino-1.3.4-v4l1.patch

Packager: Michael Shigorin <mike@altlinux.org>

%define desktop_file_utils_ver 0.8

Requires(post,postun): desktop-file-utils >= %desktop_file_utils_ver
Requires(post,postun): shared-mime-info >= 0.15-alt2

BuildPreReq: desktop-file-utils >= %desktop_file_utils_ver

%if_with quicktime
BuildPreReq: libquicktime-devel >= 0.9.7-alt4
%endif

BuildRequires: gcc-c++ imake libSM-devel libXext-devel libXv-devel libalsa-devel libavc1394-devel libdv-devel libglade-devel libiec61883-devel libsamplerate-devel xorg-cf-files libavformat-devel liblame-devel perl-XML-Parser liba52-devel xorg-xextproto-devel libxml2-devel
BuildRequires: libdc1394-devel libv4l-devel libgsm-devel

%description
Kino is a non-linear DV editor for GNU/Linux. It features excellent
integration with IEEE 1394 for capture, VTR control, and recording back
to the camera. It captures video to disk in AVI format in both type-1 DV
and type-2 DV (separate audio stream) encodings.

You can load multiple video clips into a playlist, cut and paste
portions of video/audio, and save it to a playlist. Most edit and
navigation commands are mapped to equivalent vi key commands. Also, Kino
can load playlists and  save the composite playlist as a new DV AVI
file. Finally, Kino can save a single frame of video (a still) in
numerous file formats (based upon file extension).

Currently, Kino does not support other video file formats or encodings.
It does not support multiple layers or tracks of video and audio. It
does not do image processing, titling, transitions, or effects. We plan
to implement most of these features, but first we chose to focus on the
basics of IEEE 1394, video, audio, and file input and output. We place a
lot of emphasis on quality, stability, performance, and workflow.

For more information, please read the NEWS file, which contains
functional changes and important notices for each new version. The
ChangeLog contains a more detailed, technical account of the changes in
each version. Valuable information is contained in these files unless
you can read C/C++ source  code. Also, the discussion forums on the user
website above are very helpful.

%package devel
Group: Development/C++
Summary: Header files for kino plugin development
Requires: %name = %version-%release
BuildArch: noarch

%description devel
This package contains the headers files needed to build extensions for kino.

%package dvdauthor
Group: Video
Summary: K3B/dvdauthor integration
Requires: k3b qdvdauthor dvd+rw-tools
BuildArch: noarch

%description dvdauthor
This package contains optional scripts to be able to prepare and burn
a DVD right from Kino

%prep
%setup
%patch1 -p1
%patch2 -p2
%patch3 -p1
bzcat %SOURCE5 > po/ru.po

%build
export LDFLAGS=-export-dynamic
%autoreconf
%configure \
	%{subst_with quicktime} \
	--with-avcodec

touch po/stamp-it
%make_build

%install
%makeinstall_std
install -p %SOURCE4 %buildroot%_desktopdir/Kino.desktop
mkdir -p %buildroot%_sysconfdir/kino-scripts
rm -f %buildroot%_libdir/kino-gtk2/*.{a,la}
%find_lang --with-gnome %name
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Application \
	--add-category=Video \
	--add-category=AudioVideoEditing \
	%buildroot%_desktopdir/Kino.desktop

%post
UUU=%_sbindir/update-usb.usermap
[ ! -x "$UUU" ] || "$UUU"

%postun
if [ "$1" = 0 ]; then
	UUU=%_sbindir/update-usb.usermap
	[ ! -x "$UUU" ] || "$UUU"
fi

%files -f %name.lang
%_bindir/*
%_datadir/%name/
%exclude %_datadir/%name/scripts/dvdauthor/
%_pixmapsdir/*
%_desktopdir/*
%_man1dir/*
%dir %_libdir/kino-gtk2/
# NB: *.so belong to kino package too, these are plugins!
%_libdir/kino-gtk2/*.so*
%_datadir/mime/packages/*.xml
%_sysconfdir/udev/rules.d/*
%dir %_sysconfdir/kino-scripts/
%doc AUTHORS BUGS ChangeLog NEWS README* TODO

%files devel
%_includedir/*

%files dvdauthor
%_datadir/%name/scripts/dvdauthor/

%changelog
* Mon Oct 31 2011 Michael Shigorin <mike@altlinux.org> 1.3.4-alt7
- devel, dvdauthor subpackages made noarch

* Sun Oct 30 2011 Michael Shigorin <mike@altlinux.org> 1.3.4-alt6
- added libdc1394, libgsm, libv4l to BuildRequires:
- added gentoo patch to build bundled ffmpeg with v4l2
  (see also debian bug #621996)

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.3.4-alt5.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for kino
  * altlinux-policy-obsolete-buildreq for kino

* Thu Apr 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.4-alt5
- fix build

* Sun Aug 01 2010 Vitaly Lipatov <lav@altlinux.ru> 1.3.4-alt4
- build without libfaac

* Wed Apr 07 2010 Michael Shigorin <mike@altlinux.org> 1.3.4-alt3
- added a patch partially reverting a change in 1.3.3
  regarding default audiodevice (was "default", became
  "/dev/dsp" to hold off pulseaudio, now "default" again)
  (closes: #23278)

* Sun Mar 21 2010 Michael Shigorin <mike@altlinux.org> 1.3.4-alt2
- dropped obsolete macros

* Fri Sep 11 2009 Michael Shigorin <mike@altlinux.org> 1.3.4-alt1
- 1.3.4
- included updated Russian translation by Alexandre Prokoudine
  (closes: #21528)

* Wed May 13 2009 Michael Shigorin <mike@altlinux.org> 1.3.3-alt2
- better rm(1) usage

* Sat Jan 31 2009 Michael Shigorin <mike@altlinux.org> 1.3.3-alt1
- 1.3.3
- purged all patches

* Sat Dec 06 2008 Michael Shigorin <mike@altlinux.org> 1.3.2-alt4
- applied repocop patch
- minor spec cleanup

* Mon Dec 01 2008 Michael Shigorin <mike@altlinux.org> 1.3.2-alt3
- updated BuildRequires

* Sat Aug 23 2008 Michael Shigorin <mike@altlinux.org> 1.3.2-alt2
- added kino.desktop with tatar translation (#16844)

* Fri Aug 22 2008 Michael Shigorin <mike@altlinux.org> 1.3.2-alt1
- 1.3.2
  + minor build-related fixes
  + yay, removed all patches -- merged/fixed upstream :)

* Fri Aug 15 2008 Michael Shigorin <mike@altlinux.org> 1.3.1-alt1
- 1.3.1
  + removed patch[1-3], applied upstream
  + added patch4 to fix paths to lib{av{format,codec},swscale}

* Sun Jul 06 2008 Michael Shigorin <mike@altlinux.org> 1.3.0-alt4
- applied patches by Philippe Troin <phil fifi org>
  to fix sloppy memory handling in a few places

* Wed Apr 16 2008 Michael Shigorin <mike@altlinux.org> 1.3.0-alt3
- rebuild

* Wed Mar 19 2008 Michael Shigorin <mike@altlinux.org> 1.3.0-alt2
- rebuild (H.264 FFMPEG export would segfault)
- fixed autogenerated %%post/%%postun requires
- removed obsolete patches

* Tue Feb 26 2008 Michael Shigorin <mike@altlinux.org> 1.3.0-alt1
- 1.3.0:
  + Updated export scripts for ffmpeg changes (x264, mp3)
  + Improved speed on SMP systems by enabling FFmpeg multi-threaded codecs
  + Improved import (DV conversion) progress dialog
  + Added gstreamer-based Ogg Theora to the blip.tv publishing script
  + Added quality level option to the blip.tv publishing script
  + Updated Hungarian translation
  + Added Ukranian translation by Yuri Chornoivan

* Tue Dec 11 2007 Michael Shigorin <mike@altlinux.org> 1.2.0-alt1
- 1.2.0:
  + New Ogg Theora export script that uses gstreamer
  + New Quicktime DV export script that uses ffmpeg
  + New variable substitution in Titler Video Filter!
  + Added Finnish translation by Antti Sokero
  + bugfixes
- thanks led@ for an alert

* Thu Oct 04 2007 Michael Shigorin <mike@altlinux.org> 1.1.1-alt1
- 1.1.1:
  + bugfix segfault on crash recovery with gtk+ version < 2.11
  1.1.0:
  + Heavily update English user manual
  + Major performance improvement in player engine when frame dropping enabled
  + Updated export scripts to improve compatibility
  + New Catalan translation
  + Bug fixes
- removed patch3 (unneeded)

* Wed Mar 14 2007 Michael Shigorin <mike@altlinux.org> 1.0.0-alt1
- 1.0.0
- removed old patches (merged upstream, hooray) but patch0
- removed debian menu generation (freedesktop menu in place)
- removed obsolete hotplug support (following upstream)
- cleared TODO in spec! (TODO: update ru/uk.po)
- added new and shiny udev support
- added patch3 to fix wrong absolute symlink kino2raw

* Thu Mar 08 2007 Michael Shigorin <mike@altlinux.org> 0.9.5-alt4
- fixed build with recent libavcodec
  (added missing define, thanks thresh@ and damir@)

* Fri Feb 23 2007 Michael Shigorin <mike@altlinux.org> 0.9.5-alt3
- fixed build (added liba52-devel to buildrequires by hand)

* Sat Feb 03 2007 Michael Shigorin <mike@altlinux.org> 0.9.5-alt2
- hasher build fix based on patch2 by Damir Shayhutdinov (damir@)
  for 0.9.4, based on ldv's fix from 0.9.3-alt2
  (attempt #2 to pass upstream...)

* Mon Jan 15 2007 Michael Shigorin <mike@altlinux.org> 0.9.5-alt1
- 0.9.5

* Sun Dec 24 2006 Michael Shigorin <mike@altlinux.org> 0.9.4-alt1
- 0.9.4
- updated buildrequires

* Sun Dec 24 2006 Michael Shigorin <mike@altlinux.org> 0.9.4-alt0.cvs20061224
- today's CVS (it's marked as 0.9.4 already internally)
- explicitly built against libavcodec (preferring it to libdv),
  thanks stefan/sfendt.de for buggin' on kino-dev@ :-)
  + didn't like libswscale hence CVS, thanks Dan for update
  + updated buildrequires
- updated Russian translation (merged upstream)
- changed Packager: to myself (seems like I'll be interested
  for a while, and project's developers list is nice)

* Fri Dec 22 2006 Michael Shigorin <mike@altlinux.org> 0.9.3-alt3
- moved %_libdir/kino-gtk2/*.so to %name package from -devel
  since these are plugins and .so are actually needed

* Mon Dec 18 2006 Michael Shigorin <mike@altlinux.org> 0.9.3-alt2
- applied looping build fix by Dmitry V. Levin (ldv@), thanks!

* Sun Nov 12 2006 Michael Shigorin <mike@altlinux.org> 0.9.3-alt1
- 0.9.3
- merged lav's 0.9.2-alt0.1 changelog afterhand
- attempt to rebuild with non-SMP make
- minor spec cleanup

* Sat Oct 28 2006 Michael Shigorin <mike@altlinux.org> 0.9.2-alt0.1a
- 0.9.2 (NMU)
- split DVD author scripts (with considerable external requirements)
  into a separate subpackage

* Fri Sep 15 2006 Vitaly Lipatov <lav@altlinux.ru> 0.9.2-alt0.1
- new version 0.9.2 (with rpmrb script)

* Thu Aug 10 2006 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt0.1cvs20060810
- snapshot alpha 0.9.1

* Mon Jun 26 2006 Vitaly Lipatov <lav@altlinux.ru> 0.9.0-alt0.1
- new version 0.9.0
- update buildreqs
- change Url

* Mon Feb 06 2006 Vitaly Lipatov <lav@altlinux.ru> 0.8.0-alt0.2
- update buildreqs
- rebuild with new X 7.0

* Sun Dec 18 2005 Vitaly Lipatov <lav@altlinux.ru> 0.8.0-alt0.1
- new version, rebuild with correct libquicktime

* Wed Nov 23 2005 Vitaly Lipatov <lav@altlinux.ru> 0.7.6-alt1.1
- rebuild

* Sat Aug 27 2005 Vitaly Lipatov <lav@altlinux.ru> 0.7.6-alt1
- new version (rebuilt with libquicktime, libraw1394.so.5)

* Tue Dec 14 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.7.5-alt1
- 0.7.5

* Mon Jun 07 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.7.1-alt0.5
- 0.7.1

* Sun Dec 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.7.0-alt0.5
- go to GNOME 2.

* Mon Dec 15 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.6.5-alt0.4
- 0.6.5

* Mon Feb 24 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.6.4-alt0.4
- new version.

* Wed Dec 04 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.6.1-alt0.4
- fixed menu entry and description.

* Thu Nov 21 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.6.1-alt0.3
- First build for Sisyphus.
