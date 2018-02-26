Name: wv
Version: 1.2.9
Release: alt1

%def_disable static

Summary: MSWord 6/7/8/9 binary file -> open format converters
License: GPL
Group: Office

Url: http://wvware.sf.net/
Source: http://prdownloads.sourceforge.net/wvware/%name-%version.tar.bz2
Packager: Damir Shayhutdinov <damir@altlinux.ru>

# Automatically added by buildreq on Fri Oct 14 2005
BuildRequires: common-licenses glib2-devel libgsf-devel libpng-devel libxml2-devel pkg-config zlib-devel
# Manually removed: gcc-c++ libstdc++-devel

Requires: lib%name = %version-%release
Obsoletes: mswordview

%package print
Summary: MSWord 6/7/8/9 binary file -> open format converters (print friendly)
Group: Office
Requires: %name = %version-%release
Provides: wv-tetex
Obsoletes: wv-tetex

%package -n lib%name
Summary: MSWord 6/7/8/9 binary file -> open format converters (shared library)
Group: Office

%package -n lib%name-devel
Summary: MSWord 6/7/8/9 binary file -> open format converters (development)
Group: Development/C
Requires: lib%name = %version-%release
Provides: %name-devel
Obsoletes: %name-devel

%if_enabled static
%package -n lib%name-devel-static
Summary: MSWord 6/7/8/9 binary file -> open format converters (static libraries)
Group: Development/C
Requires: lib%name-devel = %version-%release
%endif	# enabled static

%description
Wv is a family of programs that understand the Microsoft Word 6/7/8/9
binary file format and are able to convert Word
documents into various open formats.

%description print
Tetex-dependent converters for Microsoft Word 6/7/8/9 from the Wv family.
These can convert Word documents into DVI, PostScript and PDF.

%description -n lib%name
Wv is a family of programs that understand the Microsoft Word 6/7/8/9
binary file format and are able to convert Word
documents into various open formats.

This package contains libwv, the Wv shared library.

%description -n lib%name-devel
Wv is a family of programs that understand the Microsoft Word 6/7/8/9
binary file format and are able to convert Word
documents into various open formats.

This is the development package for libwv, the Wv shared library.

%if_enabled static
%description -n lib%name-devel-static
Wv is a family of programs that understand the Microsoft Word 6/7/8/9
binary file format and are able to convert Word
documents into various open formats.

This package contains the libwv.a static library.
%endif	# enabled static

%prep
%setup

rm -f COPYING
ln -s %_licensedir/GPL-2 COPYING

%build
sed -i 's@CFLAGS =@AM_CFLAGS =@' GNUmakefile.am
sed -i 's@CPPFLAGS =@AM_CPPFLAGS =@' GNUmakefile.am
./autogen.sh

%configure --disable-dependency-tracking \
    %{subst_enable static}

%make_build

%install
%makeinstall

%files
%doc --no-dereference COPYING
%doc README
%_bindir/wvAbw
%_bindir/wvCleanLatex
%_bindir/wvConvert
%_bindir/wvDocBook
%_bindir/wvHtml
%_bindir/wvLatex
%_bindir/wvRTF
%_bindir/wvSummary
%_bindir/wvText
%_bindir/wvVersion
%_bindir/wvWare
%_bindir/wvWml
%_datadir/wv
%_man1dir/wvAbw.1*
%_man1dir/wvCleanLatex.1*
%_man1dir/wvHtml.1*
%_man1dir/wvLatex.1*
%_man1dir/wvRTF.1*
%_man1dir/wvSummary.1*
%_man1dir/wvText.1*
%_man1dir/wvVersion.1*
%_man1dir/wvWare.1*
%_man1dir/wvWml.1*

%files print
%_bindir/wvDVI
%_bindir/wvMime
%_bindir/wvPDF
%_bindir/wvPS
%_man1dir/wvDVI.1*
%_man1dir/wvMime.1*
%_man1dir/wvPDF.1*
%_man1dir/wvPS.1*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%changelog
* Sat Oct 08 2011 Michael Shigorin <mike@altlinux.org> 1.2.9-alt1
- NMU: 1.2.9
- minor spec cleanup

* Tue Nov 09 2010 Damir Shayhutdinov <damir@altlinux.ru> 1.2.4-alt5
- Rebuilt to generate symbol provides.

* Tue Oct 06 2009 Grigory Batalov <bga@altlinux.ru> 1.2.4-alt4
- Remove hardcoded tetex dependence due to successful automatic search.
- Remove conflict on wv-tetex (ALT #19935).

* Sun Nov 23 2008 Damir Shayhutdinov <damir@altlinux.ru> 1.2.4-alt3
- Removed obsolete ldconfig calls

* Tue Jan 15 2008 Damir Shayhutdinov <damir@altlinux.ru> 1.2.4-alt2
- Fix build with new autotools.

* Fri Mar 02 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.2.4-alt1
- 1.2.4
- Cleanup spec a bit.
- Added Packager tag.

* Fri Mar 31 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.2.1-alt1.1
- Rebuild with libgsf-1.so.114 .

* Sun Mar 12 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.2.1-alt1
- Release 1.2.1

* Tue Nov 15 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.2.0-alt1.1
- rebuild with libgsf-1.so.113 .

* Fri Oct 14 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.2.0-alt1
- 1.2.0
- Buildreq

* Sat Dec 04 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.3-alt2
- Bugfix: wv-print provides wv-tetex

* Fri Dec 03 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.3-alt1
- Updated to upstream release 1.0.3
- Patch0 gone upstream
- Buildreq

* Sat Sep 13 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.0-alt1
- New version

* Fri Jun 13 2003 Mikhail Zabaluev <mhz@altlinux.ru> 0.7.6-alt1
- New version
- Following the codebase changes, introduced libwv package for the shared lib
- Libified development subpackages, static build disabled by default
- New separation of utility packages: main and -print. The latter replaces
  -tetex except Latex converters, which go to main, as they don't actually
  require tetex.
- Fixed manpage installation and libpng configure test [Patch0]
- Fixed the filelist
- Symlinked COPYING to GPL-2 in the common licenses directory

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
