Name: geeqie
Version: 1.1
Release: alt4

Summary: Graphics file browser utility
License: GPLv2+
Group: Graphics

Packager: Victor Forsiuk <force@altlinux.org>

Url: http://geeqie.sourceforge.net/
Source: http://download.sourceforge.net/geeqie/geeqie-%version.tar.gz

Patch: %name-1.1-alt-lfs.patch
Patch1: geeqie-1.0-libdir-fix.patch
# add -Wl,--as-needed without disturbing %%configure macro
Patch2: geeqie-1.1-LDFLAGS.patch
# from master branch to fix regression
Patch3: geeqie-1.1-bar_keywords.c.diff
# in upstream bug tracker
Patch4: geeqie-1.0-fix-fullscreen.patch
# bz 889897
# reported upstream: http://sourceforge.net/p/geeqie/patches/28/
Patch5: geeqie-1.0-double_generic_dialog_close.patch
# from master
Patch6: geeqie-1.1-editors-NULL.patch
# reported upstream
# https://sourceforge.net/tracker/?func=detail&atid=1054680&aid=3602709&group_id=222125
Patch7: geeqie-1.1-filedata-change-notification.patch
# reported upstream
# https://sourceforge.net/tracker/?func=detail&aid=3603866&group_id=222125&atid=1054680
Patch8: geeqie-1.1-filedata-avoid-history-abort.patch
# reported upstream
# https://sourceforge.net/tracker/?func=detail&aid=3605406&group_id=222125&atid=1054682
Patch9: geeqie-1.1-large-files.patch
# LCMS2 patch from Geeqie-devel mailing-list
Patch10: geeqie-1.1-lcms2.patch
# from master
Patch11: geeqie-1.1-percent-char-in-filenames.patch


BuildRequires: gcc-c++ gnome-doc-utils intltool libgtk+2-devel libjpeg-devel
BuildRequires: liblcms2-devel liblirc-devel libtiff-devel libexiv2-devel

%description
Geeqie is a lightweight image viewer. It was forked from GQview. The development
is focused on features for photo collection maintenance: raw format, Exif/IPTC/XMP
metadata and integration with programs like UFraw, ImageMagick, Gimp, gPhoto or
ExifTool.

%prep
%setup
%patch -p1
%patch1 -p1
%patch2 -p1 -b .LDFLAGS
%patch3 -p1 -b .keywords
%patch4 -p1 -b .fix-fullscreen
%patch5 -p1 -b .fix-dialog-close
%patch6 -p1 -b .editors-NULL
%patch7 -p1 -b .filedata-notification
%patch8 -p1 -b .filedata-avoid-history-abort
%patch9 -p1 -b .large-files
%patch10 -p1 -b .lcms2
%patch11 -p1 -b .percent-char-in-filenames

%build
%autoreconf
%configure --enable-lirc --enable-largefile --with-readmedir=%_datadir/geeqie
%make_build

%install
mkdir -p %buildroot/usr/share/geeqie/html
%makeinstall_std
install -pD -m644 geeqie.png %buildroot%_liconsdir/geeqie.png

%find_lang %name

%files -f %name.lang
%_bindir/*
%_datadir/geeqie/
%_libdir/geeqie/
%_desktopdir/*
%_pixmapsdir/*
%_liconsdir/*
%_man1dir/*

%changelog
* Thu Apr 03 2014 Yuri N. Sedunov <aris@altlinux.org> 1.1-alt4
- applied some patches from geeqie bugtracker and mailing list
- built against liblcms2 (ALT #29943)

* Tue Dec 03 2013 Yuri N. Sedunov <aris@altlinux.org> 1.1-alt2
- rebuilt against libexiv2.so.13

* Fri Jan 25 2013 Yuri N. Sedunov <aris@altlinux.org> 1.1-alt1
- 1.1
- removed obsolete patches, more fixes for lfs

* Sat Jul 28 2012 Denis Smirnov <mithraen@altlinux.ru> 1.0-alt5
- rebuild

* Wed Nov 02 2011 Yuri N. Sedunov <aris@altlinux.org> 1.0-alt4
- rebuilt against libexiv2.so.11

* Thu Oct 21 2010 Victor Forsiuk <force@altlinux.org> 1.0-alt3
- Patch to use arch-specific libdir instead of hardcoded /usr/lib.

* Tue Jun 01 2010 Victor Forsiuk <force@altlinux.org> 1.0-alt2
- 1.0

* Mon Jan 04 2010 Victor Forsyuk <force@altlinux.org> 1.0-alt1.beta2
- Rebuild with libexiv2.so.6.

* Mon Jul 20 2009 Victor Forsyuk <force@altlinux.org> 1.0-alt0.beta2
- 1.0 beta2.

* Thu Jun 18 2009 Victor Forsyuk <force@altlinux.org> 1.0-alt0.beta1
- 1.0 beta1.

* Thu Jul 31 2008 Victor Forsyuk <force@altlinux.org> 1.0-alt0.alpha2
- Update to 1.0 alpha2 and build with LIRC support.

* Fri Jun 13 2008 ALT QA Team Robot <qa-robot@altlinux.org> 1.0-alt0.alpha1.1
- Automated rebuild due to libexiv2.so.2 -> libexiv2.so.4 soname change.

* Thu May 15 2008 Victor Forsyuk <force@altlinux.org> 1.0-alt0.alpha1
- Initial build.
