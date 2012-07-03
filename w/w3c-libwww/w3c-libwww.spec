%set_verify_elf_method unresolved=relaxed

Name: w3c-libwww
Version: 5.4.1
Release: alt3.1

Summary: HTTP library of common code
License: W3C
Group: System/Libraries
Url: http://www.w3.org/Library

Source: %name-%version-cvs.tar
Patch1: w3c-libwww-5.3.2-incdir.patch
Patch2: %name-alt-makefile-library.patch
Patch3: %name-alt-makefile-expat.patch
Patch4: %name-alt-makefile-SSL.patch
Patch5: %name-alt-makefile-pics.patch
Patch6: %name-alt-perl.patch
Patch7: %name-alt-makefile-install-fix.patch
Patch8: %name-5.4.1-alt-DSO.patch

BuildRequires: expat-devel openssl-devel zlib-devel

%description
Libwww is a general-purpose Web API written in C for Unix and Windows (Win32).
With a highly extensible and layered API, it can accommodate many different
types of applications including clients, robots, etc. The purpose of libwww
is to provide a highly optimized HTTP sample implementation as well as other
Internet protocols and to serve as a testbed for protocol experiments.

%package devel
Summary: Libraries and header files for programs that use libwww
Group: Development/C
Requires: %name = %version-%release
Requires: expat-devel

%description devel
Static libraries and header files for libwww, which are available as public
libraries.

%package apps
Summary: Applications built using Libwww web library: e.g. Robot, command line tool, etc
Group: Networking/WWW
Requires: %name = %version-%release

%description apps
Web applications built using Libwww: Robot, Command line tool,
line mode browser.  The Robot can crawl web sites faster, and
with lower load, than any other web walker that we know of,
due to its extensive pipelining and use of HTTP/1.1.

The command line tool (w3c) is very useful for manipulation of
Web sites that implement more than just HTTP GET (e.g. PUT,
 POST, etc.).

The line mode browser is a minimal line mode web browser;
often useful to convert to ascii text.  Currently unavailable
until someone updates it to some new interfaces. (hint, hint...)

%prep
%setup -n %name
%patch1 -p1
%patch2
%patch3
%patch4
%patch5
%patch6
%patch7 -p2
%patch8 -p2
touch wwwconf.h.in
%autoreconf

%build
%configure \
	--enable-shared \
	--with-gnu-ld \
	--with-regex \
	--with-zlib \
	--with-ssl \
	--with-md5 \
	--with-expat \
	--enable-reentrant
%make

%install
%makeinstall_std

%files
%_libdir/*.so.*
%_datadir/%name

%files devel
%_bindir/*-config
%_libdir/*.so
%_libdir/*.*a
%_includedir/*
%doc *.html Icons/*/*.gif

%files apps
%_bindir/webbot
%_bindir/w3c
%_bindir/www

%changelog
* Wed Jun 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.1-alt3.1
- Fixed build

* Mon Apr 18 2011 Dmitry V. Levin <ldv@altlinux.org> 5.4.1-alt3
- Rebuilt for debuginfo.

* Fri Oct 01 2010 Dmitry V. Levin <ldv@altlinux.org> 5.4.1-alt2
- Rebuilt with libssl.so.10.

* Wed Aug 26 2009 Andrey Rahmatullin <wrar@altlinux.ru> 5.4.1-alt1
- fix build

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 5.4.1-alt0.1.1.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 5.4.1-alt0.1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Mon Mar 27 2006 Vladimir Lettiev <crux@altlinux.ru> 5.4.1-alt0.1
- cvs version
- build with system libexpat
- Fix build with -Wl, --as-needed

* Sun Dec 04 2005 Vladimir Lettiev <crux@altlinux.ru> 5.4.0-alt2
- SECURITY FIX:
  CVE-2005-3183 (DoS) - Fixed incorrect bounds checking in HTBoundary_put_block()
  function in Library/src/HTBound.c. (Patch adopted from RH#159597)

* Mon May 10 2004 ALT QA Team Robot <qa-robot@altlinux.org> 5.4.0-alt1.1
- Rebuilt with openssl-0.9.7d.

* Wed Oct 30 2002 AEN <aen@altlinux.ru> 5.4.0-alt1
- new version

* Sat Mar 17 2001 Mikhail Zabaluev <zabaluev@parascript.com> 5.3.2-ipl2mdk
- Changed group of the devel package to Development/C
- Built with --enable-reentrant configure option.

* Fri Dec 22 2000 Dmitry V. Levin <ldv@fandra.org> 5.3.2-ipl1mdk
- 5.3.2

* Sun Dec 10 2000 Dmitry V. Levin <ldv@fandra.org> 5.3.1-ipl1mdk
- RE adaptions.

* Wed Oct 25 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 5.3.1-1mdk
- Release 5.3.1
- compiled with ssl and md5 support

* Wed May 03 2000 Lenny Cartier <lenny@mandrakesoft.com> 5.2.8-4mdk
- fix group
- build release

* Mon Apr 12 1999 Jeff Johnson <jbj@redhat.com>
- repackage for Red Hat 6.0.
