Name: djvu
Version: 3.5.28
Release: alt1

Summary: DjVu viewers, encoders and utilities
License: GPLv2+
Group: Publishing
Url: http://djvu.sourceforge.net/

# http://download.sourceforge.net/djvu/djvulibre-%version.tar.gz
Source: djvulibre-%version.tar
Patch: djvulibre-3.5.22-rh-cdefs.patch

# Automatically added by buildreq on Sat Apr 13 2013
# optimized out: libstdc++-devel
BuildRequires: gcc-c++ libjpeg-devel libtiff-devel xdg-utils

%def_disable static

%description
DjVu is a web-centric format and software platform for distributing documents
and images. DjVu can advantageously replace PDF, PS, TIFF, JPEG, and GIF for
distributing scanned documents, digital documents, or high-resolution pictures.
DjVu content downloads faster, displays and renders faster, looks nicer on a
screen, and consume less client resources than competing formats. DjVu images
display instantly and can be smoothly zoomed and panned with no lengthy
re-rendering.

DjVuLibre is a free (GPL'ed) implementation of DjVu, including decoders,
simple encoders, and utilities.  The viewer and browser plugin are in
their own separate packages.

%package common
Summary: DjVu shared files
Group: Publishing
BuildArch: noarch

%description common
DjVu is a web-centric format and software platform for distributing documents
and images. DjVu can advantageously replace PDF, PS, TIFF, JPEG, and GIF for
distributing scanned documents, digital documents, or high-resolution pictures.
DjVu content downloads faster, displays and renders faster, looks nicer on a
screen, and consume less client resources than competing formats. DjVu images
display instantly and can be smoothly zoomed and panned with no lengthy
re-rendering.

This package contains data files shared among DjVu subpackages.

%package -n lib%name
Summary: DjVu encoder runtime library
Group: System/Libraries
Requires: %name-common = %EVR

%description -n lib%name
This package contains DjVu encoder runtime library.

%package utils
Summary: DjVu utilites
Group: Publishing
Requires: lib%name = %EVR

%description utils
This package contains DjVu encoder and support utilites.

%package xmltools
Summary: DjVu XML tools
Group: Publishing
Requires: lib%name = %EVR

%description xmltools
This package contains DjVu XML tools.

%package doc
Summary: DjVu documenation
Group: Publishing
BuildArch: noarch

%description doc
This package contains documentaion about DjVu technology,
can be also used as test samples.

%package -n lib%name-devel
Summary: Development files for lib%name
Group: Development/C++
Requires: lib%name = %EVR
Provides: %name-devel = %EVR
Obsoletes: %name-devel < %EVR

%description -n lib%name-devel
This package contains development files for lib%name.

%package -n lib%name-devel-static
Summary: static version of libdjvu
Group: Development/C++
Requires: lib%name-devel = %EVR

%description -n lib%name-devel-static
Static version of lib%name for apps using DjVu
technology.

%prep
%setup -n djvulibre-%version
%patch -p1

%build
%autoreconf
%configure %{subst_enable static} --enable-threads
%make_build V=1 OPTS='%optflags' \
	PNGICONS="$(cd desktopfiles && echo prebuilt-hi*-djvu.png |sed s/prebuilt-//g)"

%install
%makeinstall_std \
	PNGICONS="$(cd desktopfiles && echo prebuilt-hi*-djvu.png |sed s/prebuilt-//g)"
find %buildroot%_datadir/djvu -name 'prebuilt-hi*-djvu.png' -delete

pushd desktopfiles
for f in hi*-djvu.png; do
	i=${f%%-djvu.png};
	i=${i#hi}
	install -Dpm644 "$f" \
		%buildroot%_iconsdir/hicolor/"$i"x"$i"/mimetypes/image-vnd.djvu.mime.png
done
install -Dpm644 djvulibre-mime.xml %buildroot%_datadir/mime/packages/djvulibre-mime.xml
popd

%define docdir %_docdir/%name-%version
mkdir -p %buildroot%docdir
cp -a COPYRIGHT NEWS README doc %buildroot%docdir/

%find_lang %name
%set_verify_elf_method strict

%files common
%_datadir/djvu/
%_iconsdir/*/*/*/*.png
%_iconsdir/*/scalable/*/*.svgz
%_datadir/mime*/*
%dir %docdir/
%docdir/[CNR]*

%files doc
%dir %docdir/
%docdir/doc/

%files -f %name.lang -n lib%name
%_libdir/*.so.*

%files utils
%_bindir/*
%_mandir/man?/*
%exclude %_bindir/*xml*
%exclude %_mandir/man?/*xml*

%files xmltools
%_bindir/*xml*
%_mandir/man?/*xml*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif #static

%changelog
* Wed Mar 30 2022 L.A. Kostis <lakostis@altlinux.ru> 3.5.28-alt1
- Updated to 3.5.28.

* Wed Jun 03 2020 L.A. Kostis <lakostis@altlinux.ru> 3.5.27-alt1
- Updated to 3.5.27.
- Remove deprecated desktop files install.
- Added scalable icons.

* Sat Apr 13 2013 Dmitry V. Levin <ldv@altlinux.org> 3.5.25.3-alt1
- Updated to 3.5.25.3.

* Tue Dec 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.22-alt1.3
- Fixed build with glibc 2.16 and gcc 4.7

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

