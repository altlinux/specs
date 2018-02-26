Name: libghttp
Version: 1.0.9
Release: alt6

Summary: GNOME HTTP client library
License: LGPL
Group: System/Libraries

URL: http://www.gnome.org/
# ftp://ftp.gnome.org/pub/gnome/sources/libghttp/1.0/
Source: libghttp-%version.tar.bz2
Packager: Repocop Q. A. Robot <repocop@altlinux.org>

# autotools
Patch0: libghttp-1.0.9-alt-ac25.patch

# debian
Patch10: libghttp-1.0.9-deb-http_proxy.patch
Patch11: libghttp-1.0.9-deb-sprintf-locale.patch
Patch12: libghttp-1.0.9-deb-malloc.patch
Patch13: libghttp-1.0.9-deb-flush_chunked.patch

%package devel
Summary: GNOME HTTP client development
Group: Development/GNOME and GTK+
Requires: libghttp = %version-%release

%package devel-static
Summary: GNOME HTTP client static library
Group: Development/GNOME and GTK+
Requires: libghttp-devel = %version-%release

%description
gHTTP is a GNOME library for making HTTP 1.1 requests.

This library has been replaced in the GNOME project by gnome-vfs,
and is orphaned upstream.  New projects will probably want to use
gnome-vfs or libcurl instead of libghttp.

%description devel
gHTTP is a GNOME library for making HTTP 1.1 requests.
This package contains include files for libghttp development.

This library has been replaced in the GNOME project by gnome-vfs,
and is orphaned upstream.  New projects will probably want to use
gnome-vfs or libcurl instead of libghttp.

This library is fully compliant with HTTP 1.1 as defined in the
draft 5 update of RFC 2068.

%description devel-static
gHTTP is a GNOME library for making HTTP 1.1 requests.
This package contains the static version of the library.

This library has been replaced in the GNOME project by gnome-vfs,
and is orphaned upstream.  New projects will probably want to use
gnome-vfs or libcurl instead of libghttp.

This library is fully compliant with HTTP 1.1 as defined in the
draft 5 update of RFC 2068.

%prep
%setup -q
%patch0 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1

%build
autoreconf -fisv
%def_disable static
%configure %{subst_enable static}
%make_build

%install
%makeinstall

# split docs
%define pkgdocdir %_docdir/libghttp-%version
mkdir -p %buildroot%pkgdocdir
cp -p AUTHORS ChangeLog doc/ghttp.html %buildroot%pkgdocdir/

%files
%_libdir/*.so.*
%dir %pkgdocdir
%pkgdocdir/AUTHORS

%files devel
%_includedir/*.h
%_libdir/*.so
%_libdir/*.sh
#_libdir/*.a
%dir %pkgdocdir
%pkgdocdir/ChangeLog
%pkgdocdir/ghttp.html

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Mon Nov 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.9-alt6
- Rebuilt for soname set-versions

* Wed Feb 03 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.0.9-alt5.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libghttp
  * postun_ldconfig for libghttp
  * postclean-05-filetriggers for spec file

* Wed Apr 11 2007 Alexey Tourbin <at@altlinux.ru> 1.0.9-alt5
- rebuild

* Sat May 15 2004 Alexey Tourbin <at@altlinux.ru> 1.0.9-alt4
- libghttp-devel-static packaged conditionally
- docs split between libghttp and libghttp-devel
- updated descriptions after Debian GNU/Linux package
- integrated patches from Debian GNU/Linux:
 + http_proxy environment support (debian bug#127195)
 + http_req.c to always call LC_NUMERIC=C (debian bug#92175, formely mdk-fixlocale.patch)
 + failure handling for malloc function ghttp_request_new() (debian bug#211215)
 + chunked encoding allocation and flushing (debian bug#165101)

* Tue Oct 21 2003 Alexey Tourbin <at@altlinux.ru> 1.0.9-alt3
- build explicitely with libtool-1.4
- mdk-fixlocale.patch: fix HTTP numbering (due to use of locale in sprintf)
- includedir.patch dropped
- *.la files removed

* Sat Sep 21 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.9-alt2
- spec cleanup
- static build disabled by default
- includedir patch
- patch for autoconf 2.5x

* Fri May 11 2001 AEN <aen@logic.ru> 1.0.9-alt1
- new version

* Thu Dec 14 2000 AEN <aen@logic.ru>
- 1.0.8

* Mon Nov 28 2000 AEN <aen@logic.ru>
- build for RE

* Fri Aug 25 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 1.0.7-1mdk
- Release 1.0.7

* Mon Jul 24 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 1.0.6-1mdk
- release 1.0.6 (from helix)
- update BM

* Fri Jul 21 2000 dam's <damien@mandrakesoft.com> 1.0.4-9mdk
- BM + macrozification

* Mon Apr 10 2000 Daouda Lo <daouda@mandrakesoft.com> 1.0.4-8mdk
- adjust group.

* Thu Jan 13 2000 Pixel <pixel@mandrakesoft.com>
- libtoolize --force

* Sun Nov  7 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Clean-Up specs.

* Tue Nov 02 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- rebuild for new environment

* Wed Jun 30 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 1.0.4.

* Tue May 11 1999 Bernhard Rosenkränzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Thu Mar 18 1999 Michael Fulbright <drmike@redhat.com>
- version 1.0.2

* Sun Mar 14 1999 Michael Fulbright <drmike@redhat.com>
- version 1.0.0

* Mon Jan 18 1999 Michael Fulbright <drmike@redhat.com>
- version 0.99.2

* Wed Jan 06 1999 Michael Fulbright <drmike@redhat.com>
- built with gnome-libs 0.99.2
