%def_disable static

Name: wv2
Version: 0.4.2
Release: alt2


Summary: MSWord 6/7/8/9 binary file format -> HTML converter
License: GPL
Group: Office
Url: http://wvWare.sourceforge.net/

Obsoletes: mswordview

BuildRequires: gcc-c++ glib2-devel glibc-devel libgsf-devel
BuildRequires: libstdc++-devel libxml2-devel pkg-config zlib-devel
BuildRequires: cmake kde-common-devel
%if_enabled static
BuildRequires: glib2-devel-static glibc-devel-static libgsf-devel-static libstdc++-devel-static libxml2-devel-static
%endif

Source: http://prdownloads.sourceforge.net/wvware/%name-%version.tar.bz2
Patch1: wv2-0.4.2-alt-glib2.32.patch

%package -n lib%name
Summary: MSWord 6/7/8/9 binary file format -> HTML converter library
Group: Development/C
License: LGPL

%package -n lib%name-devel
Summary: MSWord 6/7/8/9 binary file format -> HTML converter (development)
Group: Development/C
License: LGPL
Requires: lib%name = %version-%release
Provides: %name-devel = %version-%release

%package -n lib%name-devel-static
Summary: MSWord 6/7/8/9 binary file format -> HTML converter (development)
Group: Development/C
License: LGPL
Requires: lib%name-devel = %version-%release
Provides: %name-devel-static = %version-%release

%description
Wv2 is a library that understands the Microsoft Word 6/7/8/9
binary file format and is able to convert Word
documents into HTML, which can then be read with a browser.

%description -n lib%name
Wv2 is a library that understands the Microsoft Word 6/7/8/9
binary file format and is able to convert Word
documents into HTML, which can then be read with a browser.

This is the development package with shared library.

%description -n lib%name-devel
Wv2 is a library that understands the Microsoft Word 6/7/8/9
binary file format and is able to convert Word
documents into HTML, which can then be read with a browser.

This is the development package with headers

%description -n lib%name-devel-static
Wv2 is a library that understands the Microsoft Word 6/7/8/9
binary file format and is able to convert Word
documents into HTML, which can then be read with a browser.

This is the development package with static library.


%prep
%setup -q
%patch1 -p1


%build
%Kbuild

%install
%Kinstall


%files -n lib%name
%doc AUTHORS ChangeLog README THANKS TODO
%dir %_libdir/wvWare
%_libdir/*.so.*

%files -n lib%name-devel
%doc AUTHORS ChangeLog README THANKS TODO
%doc doc
%_bindir/%name-config
%_includedir/%name
%_libdir/*.so
%_libdir/wvWare/*.cmake

%if_enabled static
%doc AUTHORS
%files -n lib%name-devel-static
%_libdir/*.a
%endif


%changelog
* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 0.4.2-alt2
- fix to build with new glib2

* Tue Apr 20 2010 Sergey V Turchin <zerg@altlinux.org> 0.4.2-alt0.M51.1
- build for M51

* Fri Dec 04 2009 Sergey V Turchin <zerg@altlinux.org> 0.4.2-alt1
- new version

* Tue Dec 02 2008 Sergey V Turchin <zerg at altlinux dot org> 0.2.3-alt2
- remove deprecated macroses
- add patches to fix build with new gcc

* Fri Jan 26 2007 Sergey V Turchin <zerg at altlinux dot org> 0.2.3-alt1
- new version

* Tue Jun 13 2006 Sergey V Turchin <zerg at altlinux dot org> 0.2.2-alt4
- add patch to fix array overflow

* Fri Jan 27 2006 Sergey V Turchin <zerg at altlinux dot org> 0.2.2-alt3
- fix build on x86_64

* Fri Jun 10 2005 Sergey V Turchin <zerg at altlinux dot org> 0.2.2-alt2
- rebuild

* Thu Jul 08 2004 Sergey V Turchin <zerg at altlinux dot org> 0.2.2-alt1
- new verion

* Thu Jan 22 2004 Sergey V Turchin <zerg at altlinux dot org> 0.2.1-alt2
- fix requires

* Tue Jan 20 2004 Sergey V Turchin <zerg at altlinux dot org> 0.2.1-alt1
- New version

* Sun Apr 27 2003 Mikhail Zabaluev <mhz@altlinux.ru> 0.7.5-alt1
- New version
- Fixed filelist
- Removed Windows-specific stuff from notes
- Fixed configure options and rebuilt buildreqs

* Tue Dec 17 2002 Mikhail Zabaluev <mhz@altlinux.ru> 0.7.4-alt1
- 0.7.4
- rebuild with libwmf 0.2.8

* Thu Sep 26 2002 Stanislav Ievlev <inger@altlinux.ru> 0.7.2-alt1.2
- rebuild with libwmf 0.2.6
- added hack to build (we need to rebuild all programs with -I/usr/include -L/usr/lib)

* Mon Jun 17 2002 Mikhail Zabaluev <mhz@altlinux.ru> 0.7.2-alt1
- 0.7.2
- Filelist cleanup
- Abolished -devel-static; when libwv.so becomes norm, add it again
- (inger)fixed build

* Thu Nov 29 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.7.0-alt1
- 0.7.0
- Rebuild with new libwmf 0.2.2
- Removed charset patch - in wv now

* Sat Nov 03 2001 Rider <rider@altlinux.ru> 0.6.7-alt1
- 0.6.7

* Thu Oct 11 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.6.5-alt4
- Rebuilt with libpng.so.3

* Mon Aug 20 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.6.5-alt3
- Rebuilt with new libwmf
- Some spec cleanup
- Added wv-tetex & wv-devel-static packages

* Mon Jun 4 2001 AEN <aen@logic.ru> 0.6.5-alt2
- %files fixed

* Thu May 10 2001 Rider <rider@altlinux.ru> 0.6.5-alt1
- 0.6.5

* Tue Feb 6 2001  AEN <aen@logic.ru>
- build for new release

* Thu May 25 2000 AEN <aen@logic.ru>
- 0.5.44
- 1251 support

* Fri Mar 31 2000 François Pons <fpons@mandrakesoft.com> 0.5.14bw6-2mdk
- updated Group.

* Thu Nov 04 1999 John Buswell <johnb@mandrakesoft.com>
- updated to mswordview-0.5.14-bw6
- added install of config-mswordview
- Build Release

* Fri Jul 30 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- updated to  mswordview-0.5.14-bw3

* Thu Jul 15 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Fix path problems.

* Wed Jul 14 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Fix compilations problem.
- 0.5.14-bw2

* Sat Apr 24 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Update to 5.8.
- Mandrake adaptations.

* Tue Dec 29 1998 Ryan Weaver <ryanw@infohwy.com>
  [mswordview-0.5.2-1]
- Updated to MSWordView-0.5.2
- Changes up to 0.5.2
  * implemented auto text color colour check for table cells, no more
    black on black, or black on blue. i must look closely at what other
    auto changes word makes.
  * some uber-simple greyscaling code when table look says no-color.
  * verified it works under AIX, made a few changes that showed up due
    to its stricter malloc, theres probably a few more malloc related
    issues hiding in there.
  * column breaks show up as well now.
  * the various types of section breaks are distinguisable from the
    others, and from page breaks.
  * a few changes to make sure formatting and tables get on better
    together.
  * sequence field supported, i.e caption numbering, i just use the last
    fields that msword left in there.
  * changed hyperlinking so that it works with bookmarks that are in
    comments (annotations).
  * i now support multiple bookmarks that end on the same location.
  * multiple bookmarks that start on the same location should be supported,
    but no examples yet.
  * the comment author initials are extracted and used in the main document
    when referencing comments.
  * comments now end when they are supposed to, only the correct comments get
    included, should work for fastsave, not tested.
  * removed unused variables, sorted out a few other warnings, maybe itll
    squeak by the irix compiler now ?
  * names and initial info for comments is extracted as well, and stuck in a
    table at the end of the document.
  * fixed the <a name= for comments, should work in fast saved.
  * custom graphics for annotations.
