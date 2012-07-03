%define gst_plugins gst-plugins
%define ver_major 0.10

%define _gst_libdir %_libdir/gstreamer-%ver_major
%define _gtk_docdir %_datadir/gtk-doc/html

Name: %gst_plugins-ugly
Version: %ver_major.19
Release: alt1
Summary: A set of encumbered GStreamer plugins
Group: System/Libraries
License: LGPL
URL: http://gstreamer.freedesktop.org/

Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: gstreamer >= 0.10.6
Requires: lib%gst_plugins >= 0.10.3

Provides: %gst_plugins-lame = %version-%release
Provides: %gst_plugins-mad = %version-%release

Conflicts: %gst_plugins-bad < 0.10.13

Source: %name-%version.tar
Source1: common.tar
Patch: %name-%version-%release.patch

BuildRequires: gcc-c++ gst-plugins-devel gtk-doc intltool liba52-devel libcdio-devel libid3tag-devel
BuildRequires: liblame-devel libmad-devel libmpeg2-devel liboil-devel libx264-devel python-module-PyXML
BuildRequires: python-modules-encodings libopencore-amrnb-devel libopencore-amrwb-devel libdvdread-devel
BuildRequires: liborc-devel orc

%description
GStreamer Ugly Plug-ins is a set of plug-ins that have good quality
and correct functionality, but distributing them might pose problems.
The license on either the plug-ins or the supporting
libraries might not be how the developers would like.
The code might be widely known to present patent problems.

%package devel-doc
Summary: Development documentation for GStreamer Ugly plugins
Group: Development/C
BuildArch: noarch

%description devel-doc
This package contains development documentation for GStreamer Ugly plugin
collection.

%prep
%setup -q -a1
%patch -p1

touch ABOUT-NLS config.rpath

%build
%autoreconf
%configure \
	--disable-examples \
	--enable-experimental \
	--enable-gtk-doc \
	--disable-static \
	--with-html-dir=%_gtk_docdir
%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %name-%ver_major

%files -f %name-%ver_major.lang
%doc AUTHORS NEWS README RELEASE
%dir %_gst_libdir
%_gst_libdir/*.so
%_datadir/gstreamer-%ver_major

%files devel-doc
%_gtk_docdir/%name-plugins-%ver_major

%changelog
* Tue Feb 21 2012 Valery Inozemtsev <shrek@altlinux.ru> 0.10.19-alt1
- 0.10.19

* Tue Jan 31 2012 Valery Inozemtsev <shrek@altlinux.ru> 0.10.18-alt1.2
- rebuild with libx264.so.120

* Mon Aug 01 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10.18-alt1.1
- rebuilt with recent x264

* Sun May 15 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.10.18-alt1
- 0.10.18

* Sat Jan 22 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.10.17-alt1
- 0.10.17

* Fri Nov 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.16-alt2
- rebuild with libx264.so.106

* Fri Sep 03 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.16-alt1
- 0.10.16

* Mon May 31 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.15-alt1
- 0.10.15

* Sun May 16 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.14.2-alt1
- 0.10.14.2 pre-release

* Sat Mar 06 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.14-alt1
- 0.10.14

* Thu Mar 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.13.4-alt1
- 0.10.13.4 pre-release

* Fri Feb 19 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.13.2-alt1
- 0.10.13.2 pre-release

* Thu Feb 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.13-alt3
- rebuild with libx264.so.85

* Tue Nov 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.13-alt2
- rebuild with new libcdio

* Thu Oct 22 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.13-alt1
- 0.10.13

* Fri Oct 16 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.12.3-alt1
- 0.10.12.3 pre-release

* Tue Oct 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.12.2-alt1
- 0.10.12.2 pre-release

* Sat Sep 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.12.1-alt3
- rebuild with libdvdread.so.4

* Wed Aug 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.12.1-alt2
- rebuild with new libcdio

* Tue Aug 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.12.1-alt1
- 0.10.12.1

* Tue Jul 28 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.12-alt2
- enabled amrnb plugin

* Thu Jun 18 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.12-alt1
- 0.10.12

* Sat Mar 21 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.11-alt1
- 0.10.11

* Wed Nov 19 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.10-alt1
- 0.10.10

* Mon Oct 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.9-alt2
- enabled cdio plugin

* Sun Oct 26 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.9-alt1
- 0.10.9

* Mon Oct 06 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.8-alt2
- updated build dependencies

* Sat May 24 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.8-alt1
- 0.10.8

* Thu May 15 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.7-alt3
- rebuild

* Thu Feb 21 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.7-alt2
- join together subpackage

* Thu Feb 21 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.10.7-alt1
- 0.10.7
- spec cleanup
- update build dependencies

* Mon Sep 10 2007 Igor Zubkov <icesik@altlinux.org> 0.10.6-alt1
- 0.10.5 -> 0.10.6

* Thu Feb 22 2007 Igor Zubkov <icesik@altlinux.org> 0.10.5-alt1
- 0.10.4 -> 0.10.5

* Thu Aug 24 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.4-alt1
- Release 0.10.4

* Mon Apr 03 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.3-alt1
- 0.10.3
- Added -subtitle package for dvdsub

* Wed Feb 22 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.2-alt1
- 0.10.2
- Added dvdread
- Added asfdemux to container-formats

* Mon Feb 20 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.10.1-alt1
- Initial release for Sisyphus after the plugin split of 0.9
