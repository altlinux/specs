Name: djvu
Version: 3.5.22
Release: alt1.2

Summary: DjVu viewers, encoders and utilities
License: GPLv2+
Group: Publishing
Url: http://djvu.sourceforge.net/
Packager: Evgeny Sinelnikov <sin@altlinux.org>
# http://download.sourceforge.net/djvu/djvulibre-%version.tar.gz
Source: djvulibre-%version.tar
Patch: djvu-3.5.22-alt-glibc-2.11.3.patch

BuildRequires: browser-plugins-npapi-devel chrpath
# Automatically added by buildreq on Fri Nov 19 2010
BuildRequires: gcc-c++ imake libXt-devel libjpeg-devel libqt3-devel libtiff-devel xdg-utils xorg-cf-files

%def_disable static

%description
DjVu is a web-centric format and software platform for distributing documents
and images.  DjVu content downloads faster, displays and renders faster, looks
nicer on a screen, and consume less client resources than competing formats.
DjVu was originally developed at AT&T Labs-Research by Leon Bottou, Yann
LeCun, Patrick Haffner, and many others.  In March 2000, AT&T sold DjVu to
LizardTech Inc. who now distributes Windows/Mac plug-ins, and commercial
encoders (mostly on Windows)

In an effort to promote DjVu as a Web standard, the LizardTech management was
enlightened enough to release the reference implementation of DjVu under the
GNU GPL in October 2000.  DjVuLibre (which means free DjVu), is an enhanced
version of that code maintained by the original inventors of DjVu. It is
compatible with version 3.5 of the LizardTech DjVu software suite.

DjVulibre-3.5 contains:
- a standalone DjVu viewer based on the Qt library.
- A browser plugin that works with most Unix browsers.
- A full-fledged wavelet-based compressor for pictures.
- A simple compressor for bitonal (black and white) scanned pages.
- A compressor for palettized images (a la GIF/PNG).
- A set of utilities to manipulate and assemble DjVu images and documents.
- A set of decoders to convert DjVu to a number of other formats.
- An up-to-date version of the C++ DjVu Reference Library.

%package common
Summary: DjVu shared files
Group: Publishing
BuildArch: noarch

%description common
DjVu is a web-centric format and software platform for distributing documents
and images.  DjVu content downloads faster, displays and renders faster, looks
nicer on a screen, and consume less client resources than competing formats.
DjVu was originally developed at AT&T Labs-Research by Leon Bottou, Yann
LeCun, Patrick Haffner, and many others.  In March 2000, AT&T sold DjVu to
LizardTech Inc. who now distributes Windows/Mac plug-ins, and commercial
encoders (mostly on Windows)

In an effort to promote DjVu as a Web standard, the LizardTech management was
enlightened enough to release the reference implementation of DjVu under the
GNU GPL in October 2000.  DjVuLibre (which means free DjVu), is an enhanced
version of that code maintained by the original inventors of DjVu. It is
compatible with version 3.5 of the LizardTech DjVu software suite.

DjVulibre-3.5 contains:
- a standalone DjVu viewer based on the Qt library.
- A browser plugin that works with most Unix browsers.
- A full-fledged wavelet-based compressor for pictures.
- A simple compressor for bitonal (black and white) scanned pages.
- A compressor for palettized images (a la GIF/PNG).
- A set of utilities to manipulate and assemble DjVu images and documents.
- A set of decoders to convert DjVu to a number of other formats.
- An up-to-date version of the C++ DjVu Reference Library.

%package -n lib%name
Summary: DjVu encoder libraries
Group: System/Libraries

%description -n lib%name
DjVu shared libraries.

%package utils
Summary: DjVu utilites
Group: Publishing
Requires: lib%name = %version-%release

%description utils
DjVu encoder and support utilites.

%package xmltools
Summary: DjVu XML tools
Group: Publishing
Requires: lib%name = %version-%release

%description xmltools
DjVu XML tools.

%package viewer
Summary: standalone DjVu viewer
Group: Publishing
Requires: lib%name = %version-%release
Requires: %name-common = %version-%release

%description viewer
A standalone DjVu viewer based on the Qt library.

%package -n mozilla-plugin-%name
Summary: DjVu NPAPI plugin
Group: Networking/WWW
Requires: lib%name = %version-%release
Requires: %name-common = %version-%release
Requires: browser-plugins-npapi
Obsoletes: %name-plugin

%description -n mozilla-plugin-%name
DjVu NPAPI plugin.

%package doc
Summary: docs about DjVu technology
Group: Publishing
BuildArch: noarch
Requires: %name-viewer

%description doc
Some useful documents about DjVu technology.
can be used as test samples.

%package -n lib%name-devel
Summary: devel headers for libdjvu
Group: Development/C++
Requires: lib%name = %version-%release
Provides: %name-devel = %version-%release
Obsoletes: %name-devel < %version-%release

%description -n lib%name-devel
Headers for lib%name for making apps using DjVu
technology.

%package -n lib%name-devel-static
Summary: static version of libdjvu
Group: Development/C++
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
Static version of lib%name for apps using DjVu
technology.

%prep
%setup -n djvulibre-%version
%patch -p2

%build
# hack for NPAPI location
sed -i 's,-rpath ${plugindir},-rpath %browser_plugins_path,' gui/nsdejavu/Makefile.in
sed -i 's,^plugindir[[:space:]]*=.*,plugindir = %browser_plugins_path,' gui/nsdejavu/Makefile.in

%configure %{subst_enable static} --enable-threads
make OPTS='%optflags' NSDEJAVU_LIBS='-lXext -lX11' #NO SMP

%install
%makeinstall_std
for f in %buildroot%_bindir/*; do
	readelf -d "$f" 2>/dev/null |fgrep -qs RPATH || continue
	chrpath -d "$f"
done

#install-gnome: FORCE
install -pD -m644 desktopfiles/hi22-djvu.png %buildroot%_iconsdir/hicolor/22x22/mimetypes/image-vnd.djvu.mime.png
install -pD -m644 desktopfiles/hi32-djvu.png %buildroot%_iconsdir/hicolor/32x32/mimetypes/image-vnd.djvu.mime.png
install -pD -m644 desktopfiles/hi48-djvu.png %buildroot%_iconsdir/hicolor/48x48/mimetypes/image-vnd.djvu.mime.png
install -pD -m644 desktopfiles/hi32-djview3.png %buildroot%_niconsdir/djvulibre-djview3.png
install -pD -m644 desktopfiles/djvulibre-mime.xml %buildroot%_datadir/mime/packages/djvulibre-mime.xml
install -pD -m644 desktopfiles/vnd.djvu.desktop %buildroot%_datadir/mimelnk/image/vnd.djvu.desktop
install -pD -m644 desktopfiles/djvulibre-djview3.desktop %buildroot%_desktopdir/djvulibre-djview3.desktop

%find_lang %name

rm -rf %buildroot%_mandir/ja

%files common
%doc README COPYRIGHT COPYING INSTALL NEWS TODO
%_datadir/djvu
%_iconsdir/*/*/*/*.png
%_datadir/mime*/*

%files doc
%doc doc

%files -f %name.lang -n lib%name
%_libdir/*.so.*

%files utils
%_bindir/*
%_mandir/man?/*
%exclude %_bindir/*xml*
%exclude %_bindir/djview*
%exclude %_mandir/man?/*xml*
%exclude %_mandir/man?/djview*
%exclude %_mandir/man?/nsdejavu*

%files xmltools
%_bindir/*xml*
%_mandir/man?/*xml*

%files viewer
%_bindir/djview*
%_mandir/man?/djview*
%_desktopdir/*.desktop

%files -n mozilla-plugin-%name
%browser_plugins_path/*.so*
%_mandir/man?/nsdejavu*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif #static

%changelog
* Tue Jul 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.22-alt1.2
- Fixed build

* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.22-alt1.1
- Rebuilt for debuginfo

* Fri Nov 19 2010 Dmitry V. Levin <ldv@altlinux.org> 3.5.22-alt1
- Updated to 3.5.22.
- Fixed interpackage dependencies.
- Updated build dependencies.
- Stripped RPATH from executables.
- Fixed plugin linkage.

* Wed Sep 30 2009 Alexey Gladkov <legion@altlinux.ru> 3.5.21-alt1.1
- NMU: Rebuilt with browser-plugins-npapi.

* Wed Nov 26 2008 Evgeny Sinelnikov <sin@altlinux.ru> 3.5.21-alt1
- update to new release
- clean spec for obsolete macroses
- fix filesystem intersections

* Sun Jan 27 2008 Evgeny Sinelnikov <sin@altlinux.ru> 3.5.20-alt0.1
- update to new release

* Wed Oct 10 2007 Evgeny Sinelnikov <sin@altlinux.ru> 3.5.19-alt0.1
- update to new release

* Fri Jan 19 2007 L.A. Kostis <lakostis@altlinux.ru> 3.5.17-alt2
- Added patches:
  + djvulibre-3.5.17-alt-xgl.patch - Djview sets variable
    XLIB_SKIP_ARGB_VISUALS to make sure that Xgl does not 
    select visuals with transparency.
  + djvulibre-3.5-alt-xtlib-dep.patch - fix undefined symbol 
    XtShellStrings in nsdejavu.so. It's just a hackaround, see related
    discusson in debian -
    http://bugs.donarmstrong.com/cgi-bin/bugreport.cgi?bug=377468
- Add djvu.1 manpage.

* Sat Jun 17 2006 LAKostis <lakostis at altlinux dot ru> 3.5.17-alt1.1
- cleanup requires for mozilla-plugin (closes #9621).

* Mon May 15 2006 LAKostis <lakostis at altlinux dot ru> 3.5.17-alt1
- 3.5.17.
- update %%url.
- update desktop files entries.
- cleanup buildreq & .spec.
- fix issue with missing -lpthread in libdjvulibre (due --as-needed ld flag).

* Wed Jan 04 2006 LAKostis <lakostis at altlinux dot ru> 3.5.16-alt0.cvs20060104
- latest cvs snapshot.
- add any2djvu.
- add static build switch.
- rename %%name-devel -> lib%%name-devel.

* Sat Dec 31 2005 LAKostis <lakostis at altlinux dot ru> 3.5.15-alt0.cvs20050807.1
- rebuild with new qt.
- remove unwanted menu files.
- fix -devel package.
- spec cleanup.

* Sun Aug 07 2005 LAKostis <lakostis at altlinux dot ru> 3.5.15-alt0.cvs20050807
- latest cvs snapshot.
- fix plugin location and naming.
- update package Buildreq/Req.
- spec cleanup.
- add -devel package.

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 3.5.14-alt1.cvs.1.1
- Rebuilt with libstdc++.so.6.

* Fri Sep 17 2004 ALT QA Team Robot <qa-robot@altlinux.org> 3.5.14-alt1.cvs.1
- Rebuilt with libtiff.so.4.

* Sat Aug 14 2004 LAKostis <lakostis at altlinux dot ru> 3.5.14-alt1.cvs
- version 3.5.14.
- fix for bug #4137.
- fix for djview menu entry.
- spec cleanups.
- add icons and mime-types.
- fixed SMP build.
- updated BuildRequires.

* Thu Sep 18 2003 LAKostis <lakostis at altlinux dot ru> 3.5.13-alt1.cvs
- version 3.5.13
- ripped out docs to separate package.
- spec cleanups.

* Thu Mar 11 2003 LAKostis <lakostis@altlinux.ru> 3.5.10-alt0.1cvs
- CVS snapshot.
- initial build for Sisyphus.

* Thu Feb  6 2003 Leon Bottou <leon@bottou.org> 3.5.10-2
- version 3.5.10-2
* Fri Jan 24 2003 Leon Bottou <leon@bottou.org> 3.5.10-1
- prepared for version 3.5.10
* Wed Oct  9 2002 Leon Bottou <leonb@users.sourceforge.net> 3.5.9-2
- fixed logic for uninstalling nsdejavu links.
- copy stuff from the freshrpms spec file.
* Sun Oct  6 2002 Leon Bottou <leonb@users.sourceforge.net> 3.5.9-1
- added logic to install nsdejavu for mozilla.
* Wed May 29 2002 Leon Bottou <leonb@users.sourceforge.net> 3.5.6-1
- bumped to version 3.5.6-1
* Mon Apr 1 2002  Leon Bottou <leonb@users.sourceforge.net> 3.5.5-2
- changed group to Applications/Publishing
* Tue Mar 25 2002 Leon Bottou <leonb@users.sourceforge.net> 3.5.5-2
* Tue Jan 22 2002 Leon Bottou <leonb@users.sourceforge.net> 3.5.4-2
- fixed for properly locating the man directory.
* Wed Jan 16 2002 Leon Bottou <leonb@users.sourceforge.net> 3.5.3-1
* Fri Dec  7 2001 Leon Bottou <leonb@users.sourceforge.net> 3.5.2-1
* Wed Dec  5 2001 Leon Bottou <leonb@users.sourceforge.net> 3.5.1-1
- created spec file for rh7.x.

