Name: libmusicbrainz
Version: 2.1.5
Release: alt5
Summary: A software library for accesing MusicBrainz servers
Group: System/Libraries
License: LGPL
Url: http://www.musicbrainz.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar.gz

Patch0: libmusicbrainz-2.1.5-alt-comsocket.patch
Patch1: libmusicbrainz-2.1.5-alt-gcc43.patch

BuildRequires: gcc-c++ libexpat-devel

%description
The MusicBrainz client library allows applications to make metadata
lookup to a MusicBrainz server, generate signatures from WAV data and
create CD Index Disk ids from audio CD roms.

%package devel
Summary: Headers for developing programs that will use lib%name
Group: Development/C++
Requires: %name = %version-%release

%description devel
This package contains the headers that programmers will need to develop
applications which will use lib%name.

%prep
%setup -q

%patch0 -p1
%patch1 -p1

%build
%autoreconf
%configure \
    --disable-static

%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc docs/*.txt
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%changelog
* Sun Mar 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.5-alt5
- Rebuilt for debuginfo

* Tue Nov 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.1.5-alt4
- rebuild

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.1.5-alt3
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Mon Oct 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.1.5-alt2
- fixed build with gcc4.3

* Mon Jul 16 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.1.5-alt1
- 2.1.5:
  + Fix the patch for buffer overflows in rdfparse.c.
  + Fixed buffer overflow in MBHttp::WriteToBuffer.

* Wed Dec 06 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.1.4-alt1
- 2.1.4:
  + Fixed buffer overflows in the RDF parsing and HTTP code.
  + Fixed memory leaks in RDFExtract.
  + Fixed invalid memory access in the HTTP code.

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.1.1-alt1.1
- Rebuilt with libstdc++.so.6.

* Tue May 25 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.1.1-alt1
- 2.1.1

* Fri Dec 05 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.0.2-alt2
- do not package .la files.

* Wed Aug 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.0.2-alt1
- new version.

* Thu Feb 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.1.0-alt1
- Adopted for Sisyphus.

* Wed Jan 29 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.1.0-4mdk
- rebuild

* Wed Dec 11 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.1.0-3mdk
- rebuild against new gcc (ppc)

* Thu May 30 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.1.0-2mdk
- rebuild against new gcc

* Sun May 05 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.1.0-1mdk
- 1.1.0

* Wed Dec 12 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.0.1-1mdk
- 1.0.1

* Mon Jul 09 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.0.0-2mdk
- rebuild

* Wed Apr 25 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.0.0-1mdk
- updated by Götz Waschk <waschk@linux-mandrake.com> :
	- 1.0.0

* Mon Jan 22 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.0.0pre6-1mdk
- rebuild
- apply library policy

* Thu Dec 21 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.0.0pre1-2mdk
- rebuild

* Mon Sep 25 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.0.0pre1-1mdk
- new in contribs

* Fri Sep 22 2000 Robert Kaye <rob@emusic.com> 1.0.0pre1
- First attempt to create a spec file for this library
