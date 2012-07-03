%define gst_plugins gst-plugins
%define ver_major 0.10

%define _gst_libdir %_libdir/gstreamer-%ver_major
%define _gtk_docdir %_datadir/gtk-doc/html

%def_enable gtk_doc

Name: %gst_plugins-bad
Version: %ver_major.23
Release: alt1
Summary: A set of GStreamer plugins that need more quality
Group: System/Libraries
License: LGPL
URL: http://gstreamer.freedesktop.org/

Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: lib%gst_plugins >= 0.10.3
Requires: gstreamer >= 0.10.3
Conflicts: %gst_plugins-good < %ver_major.15.4

Obsoletes: %gst_plugins-farsight <= 0.12.11
Provides: %gst_plugins-farsight = 0.12.20

Source0: %name-%version.tar
Source1: common.tar
Patch: %name-%version-%release.patch

BuildRequires: bzlib-devel gcc-c++ gst-plugins-devel gtk-doc intltool libSDL-devel libX11-devel
BuildRequires: libalsa-devel libcdaudio-devel libdca-devel libdirac-devel libdvdnav-devel libexif-devel
BuildRequires: libfaad-devel libgio-devel libgsm-devel libjasper-devel libmjpegtools-devel libmms-devel
BuildRequires: libmpcdec-devel libneon-devel liboil-devel libsoundtouch-devel libssl-devel libmodplug-devel
BuildRequires: libtimidity-devel libxvid-devel python-module-PyXML python-modules-email python-modules-encodings
BuildRequires: timidity-instruments libcelt-devel libdc1394-devel libkate-devel libtiger-devel
BuildRequires: libvpx-devel librtmp-devel liborc-devel orc libofa-devel libmusicbrainz-devel libass-devel
BuildRequires: libzbar-devel

%description
GStreamer Bad Plug-ins is a set of plug-ins that aren't up to par
compared to the rest.  They might be close to being good quality, but
they're missing something - be it a good code review, some
documentation, a set of tests, a real live maintainer, or some actual
wide use.  If the blanks are filled in they might be upgraded to
become part of either gst-plugins-good or gst-plugins-ugly, depending
on the other factors.

%package devel
Summary: Development files for GStreamer plugins
Group: Development/C

%description devel
This package contains the libraries, headers and other files necessary
to develop GStreamer plugins.

%package doc
Summary: Documentation for %name
Group: Documentation
BuildArch: noarch

%description doc
This package contains documentation for %name

%prep
%setup -q -a1
%patch -p1

touch ABOUT-NLS config.rpath

%build
gtkdocize
%autoreconf
%configure \
    --disable-examples \
    --enable-experimental \
    %{subst_enable gtk_doc} \
    --disable-static \
    --with-html-dir=%_gtk_docdir

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %name-%ver_major

%files -f %name-%ver_major.lang
%doc AUTHORS NEWS README RELEASE
%_libdir/*.so.*
%dir %_gst_libdir
%_gst_libdir/*.so
%_datadir/glib-2.0/schemas/*.xml

%files devel
%_includedir/gstreamer-0.10
%_libdir/*.so
%_pkgconfigdir/*.pc

%if_enabled gtk_doc
%files doc
%_gtk_docdir/gst-plugins-bad-plugins-0.10
%_gtk_docdir/gst-plugins-bad-libs-0.10
%endif

%changelog
* Tue Feb 21 2012 Valery Inozemtsev <shrek@altlinux.ru> 0.10.23-alt1
- 0.10.23

* Sat Jan 28 2012 Valery Inozemtsev <shrek@altlinux.ru> 0.10.22-alt3
- rebuild with libvpx.so.1

* Sun Jul 03 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.10.22-alt2
- disabled vdpau plugin

* Sun May 15 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.10.22-alt1
- 0.10.22

* Sat Jan 22 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.10.21-alt1
- 0.10.21

* Wed Oct 27 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.20-alt5
- rebuild with celt-0.8.1

* Mon Oct 25 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.20-alt4
- enabled jack plugin

* Thu Oct 07 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.20-alt3
- obsoletes gst-plugins-farsight

* Mon Oct 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.20-alt2
- rebuild with libcrypto.so.10

* Fri Sep 03 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.20-alt1
- 0.10.20

* Sun Jul 25 2010 Dmitry V. Levin <ldv@altlinux.org> 0.10.19-alt2.1
- Reverted previous change (libfaac is non-free, see ALT#21711).

* Mon Jul 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.19-alt2
- reenabled faac plugin

* Mon May 31 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.19-alt1
- 0.10.19

* Thu May 20 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.18.2-alt2
- added VP8

* Sun May 16 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.18.2-alt1
- 0.10.18.2 pre-release

* Sat Mar 06 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.18-alt1
- 0.10.18

* Thu Mar 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.17.4-alt1
- 0.10.17.4 pre-release

* Sun Jan 31 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.17-alt3
- rebuild with celt-0.7.1

* Thu Dec 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.17-alt2
- rebuild with celt-0.7.0

* Tue Nov 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.17-alt1
- 0.10.17

* Sat Oct 24 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.16-alt1
- 0.10.16

* Thu Oct 22 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.15-alt1
- 0.10.15

* Fri Oct 16 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.14.4-alt1
- 0.10.14.4 pre-release

* Fri Oct 16 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.14.3-alt1
- 0.10.14.3 pre-release

* Tue Oct 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.14.2-alt1
- 0.10.14.2 pre-release

* Fri Sep 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.14-alt2
- drop libfaac (closes: #21715)

* Sun Aug 30 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.14-alt1
- 0.10.14

* Tue Aug 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.13.4-alt1
- 0.10.13.4 pre-release

* Thu Jul 30 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.13-alt4
- build celt plugin

* Tue Jul 07 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.13-alt3
- disabled ladspa plugin

* Mon Jul 06 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.13-alt2
- disabled jack plugin

* Thu Jun 18 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.13-alt1
- 0.10.13

* Sun May 31 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.12-alt2
- build resindvd plugin

* Thu May 21 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.12-alt1
- 0.10.12

* Sat Mar 21 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.11-alt1
- 0.10.11

* Sat Mar 14 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.10-alt2
- rebuild with libfaad.so.2

* Tue Jan 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.10-alt1
- 0.10.10

* Mon Dec 15 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.9-alt5
- fixed build x264 plugin

* Mon Nov 24 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.9-alt4
- enabled experimental

* Tue Nov 11 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.9-alt2.M41.1
- build for branch 4.1

* Tue Nov 11 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.9-alt3
- enabled timidity plugin

* Thu Nov 06 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.9-alt2
- disabled directfb plugin

* Sun Oct 26 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.9-alt1
- 0.10.9
- disabled x264

* Tue Oct 21 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.8.3-alt1
- 0.10.8.3 pre-release

* Mon Oct 06 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.8-alt2
- updated build dependencies

* Tue Aug 05 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.8-alt1
- 0.10.8

* Tue Jun 24 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.7-alt3
- rebuild with libneon.so.27

* Thu May 15 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.7-alt2
- rebuild

* Thu Apr 24 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.7-alt1
- 0.10.7

* Thu Feb 21 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.6-alt2
- join together subpackage

* Thu Feb 21 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.6-alt1
- 0.10.6
- spec cleanup
- update build dependencies

* Mon Sep 10 2007 Igor Zubkov <icesik@altlinux.org> 0.10.5-alt1
- 0.10.4 -> 0.10.5
- enable new plugins:
  + jack

* Sat Apr 28 2007 Igor Zubkov <icesik@altlinux.org> 0.10.4-alt3
- disable swfdec plugin (it's don't compile with fresh libswfdec)

* Thu Apr 12 2007 Igor Zubkov <icesik@altlinux.org> 0.10.4-alt2
- fix linking of gst-plugins-gsm (closes #11457)

* Thu Feb 22 2007 Igor Zubkov <icesik@altlinux.org> 0.10.4-alt1
- 0.10.3 -> 0.10.4
- disable v2l2 plugin

* Wed Sep 06 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.10.3-alt2.1
- Rebuild with libdirectfb-0.9.so.25 .

* Mon Jun 05 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.3-alt2
- Added missing filelist for soundtouch
- Disabled soundtouch until bug 9677 is resolved

* Sun Jun 04 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.3-alt1
- Updated to 0.10.3
- Patch0 has gone upstream
- Added musicbrainz plugin
- Added video4linux2 plugin
- Added soundtouch
- Added modplug, xingheader to audio-formats

* Mon Mar 13 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.1-alt1
- Initial release for Sisyphus after the plugin split in the 0.9 branch
- Patch0: fix bitrotten autogen.sh
