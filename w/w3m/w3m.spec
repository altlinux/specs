# -*- coding: utf-8; mode: rpm-spec -*-
# $Id: w3m.spec,v 1.2 2006/02/14 08:39:36 eugene Exp $

Name: w3m
Version: 0.5.2
Release: alt3.1
License: BSD
Group: Networking/WWW
Summary: w3m is a pager with Web browsing capability
Url: http://w3m.sourceforge.net/

Source: %name-%version.tar.gz
Patch: %name-0.5.2-alt-DSO.patch

# Patch0: w3m-0.5.1-fix-format-string.patch

Packager: Eugene Vlasov <eugvv@altlinux.ru>

%add_findreq_skiplist %_libexecdir/w3m/cgi-bin/w3mhelp.cgi

# Automatically added by buildreq on Fri Mar 25 2011
BuildRequires: imlib2-devel libgc-devel libgpm-devel libgtk+2-devel libssl-devel man zlib-devel

%description
w3m is a pager with WWW capability. It IS a pager, but it can be
used as a text-mode WWW browser with following features:
* When reading HTML document, you can follow links and view images
  (using external image viewer).
* It has 'internet message mode', which determines the type of document
  from header. If the Content-Type: field of the document is text/html,
  that document is displayed as HTML document.
* You can change URL description like 'http://hogege.net' in plain text
  into link to that URL.


%package img
Summary: A helper program to display the inline images for w3m
Group: Networking/WWW
Requires: ImageMagick
Requires: w3m = %version-%release

%description img
w3m-img package provides a helper program for w3m to display the inline
images on the terminal emulator in X Window System environments and the
linux framebuffer.


%prep
%setup -q
%patch0 -p2

%build
%add_optflags -I%_includedir/gc
export CPPFLAGS="$CPPFLAGS -I%_includedir/gc"
%configure --enable-m17n --enable-unicode --enable-nls --with-editor=/bin/vi --with-termlib=terminfo --disable-rpath 
%make

%install
make install DESTDIR=$RPM_BUILD_ROOT
#%makeinstall HELP_DIR=%buildroot%_datadir/w3m

%find_lang w3m

%files -f w3m.lang
%doc doc/README* doc/*.html doc/menu.* doc/keymap.* doc/HISTORY
%doc *_en.html NEWS TODO
%_bindir/w3m*
%_man1dir/w3m.1.*
%_man1dir/w3mman.1*
%_mandir/ja/man1/w3m.1.*
%_datadir/w3m/
%_libexecdir/w3m/
%exclude %_libexecdir/w3m/w3mimgdisplay

%files img
%_libexecdir/w3m/w3mimgdisplay

%changelog
* Tue Jun 19 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt3.1
- Fixed build

* Fri Mar 25 2011 Alexey Tourbin <at@altlinux.ru> 0.5.2-alt3
- added build dependency on zlib-devel

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 0.5.2-alt2.1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 0.5.2-alt2.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Thu May 29 2008 Eugene Vlasov <eugvv@altlinux.ru> 0.5.2-alt2
- Fixed BuildRequires

* Thu Jan 31 2008 Eugene Vlasov <eugvv@altlinux.ru> 0.5.2-alt1
- New version
- Fix for format string vulnerability merged into upstream

* Fri Dec 29 2006 Eugene Vlasov <eugvv@altlinux.ru> 0.5.1-alt5
- [SECURITY] fix format string vulnerability in file.c (inputAnswer) (thanks
  to ldv@ for notifying)

* Fri Oct 13 2006 Eugene Vlasov <eugvv@altlinux.ru> 0.5.1-alt4
- Build w3m-img with Imlib2 instead of GdkPixbuf

* Tue Feb 14 2006 Eugene Vlasov <eugvv@altlinux.ru> 0.5.1-alt3
- Fixed requires
- Build image display helper as separate package

* Mon Feb 13 2006 Anton Farygin <rider@altlinux.ru> 0.5.1-alt2
- NMU: fixed build for x86_64

* Wed May 12 2004 ALT QA Team Robot <qa-robot@altlinux.org> 0.5.1-alt1.1
- Rebuilt with openssl-0.9.7d.

* Mon May 03 2004 Ott Alex <ott@altlinux.ru> 0.5.1-alt1
- New version 

* Wed Feb 04 2004 Ott Alex <ott@altlinux.ru> 0.4.2-alt4
- Fix spec

* Tue Feb 03 2004 Ott Alex <ott@altlinux.ru> 0.4.2-alt3
- Fix dependences

* Mon Oct 13 2003 Ott Alex <ott@altlinux.ru> 0.4.2-alt2
- fixing spec

* Sat Oct 11 2003 Ott Alex <ott@altlinux.ru> 0.4.2-alt1
- build of new version

