%def_disable static

Name: xapian-core
Version: 1.2.12
Release: alt1

Summary: The Xapian Probabilistic Information Retrieval Library
License: GPL
Group: Databases

Url: http://www.xapian.org
Source: http://www.oligarchy.co.uk/xapian/%version/%name-%version.tar.gz
Source100: %name.watch
Patch: xapian-core-1.0.17-alt-libtool.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Wed May 05 2010
BuildRequires: gcc-c++ libblkid libe2fs libpasswdqc libss libtic libuuid-devel libwrap libzio pam0_userpass python-base zlib-devel

%description
Xapian is an Open Source Probabilistic Information Retrieval Library.
It offers a highly adaptable toolkit that allows developers to easily
add advanced indexing and search facilities to applications.

This is core package.

%package -n libxapian
Summary: Xapian search engine libraries
Group: System/Libraries

%description -n libxapian
Xapian is an Open Source Probabilistic Information Retrieval Library.
It offers a highly adaptable toolkit that allows developers to easily
add advanced indexing and search facilities to applications.

This package provides the libraries for applications using Xapian
functionality.

%package -n libxapian-devel
Group: Development/C++
Summary: Files needed for building packages which use Xapian
Requires: libxapian = %version

%description -n libxapian-devel
This package provides the files needed for building packages which
use Xapian library.

%if_enabled static
%package -n libxapian-devel-static
Group: Development/C++
Summary: Files needed for building packages which use Xapian statically
Requires: libxapian-devel = %version

%description -n libxapian-devel-static
This package provides the files needed for building packages which
link against Xapian library statically or use XO_LIB_XAPIAN macroo
and build with libtool.
%endif

%package -n %name-doc
Group: Development/Documentation
Summary: Developer's documentation for Xapian
Obsoletes: xapian-doc < 0.9.9
Provides: xapian-doc = %version-%release
BuildArch: noarch

%description -n %name-doc
Xapian is an Open Source Probabilistic Information Retrieval Library.
It offers a highly adaptable toolkit that allows developers to easily
add advanced indexing and search facilities to applications.

This package contains API reference in HTML and PostScript.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure %{subst_enable static}
%make_build
gzip -9nf ChangeLog

%install
%makeinstall_std
rm -rf %buildroot%_datadir/doc/xapian-core/

%if_enabled static
# should we still support this?
%else
rm -f %buildroot%_libdir/libxapian.a
%endif

%files
%_bindir/copydatabase
%_bindir/delve
%_bindir/quest
%_bindir/simpleexpand
%_bindir/simpleindex
%_bindir/simplesearch
%_bindir/xapian-check
%_bindir/xapian-chert-update
%_bindir/xapian-compact
%_bindir/xapian-inspect
%_bindir/xapian-metadata
%_bindir/xapian-progsrv
%_bindir/xapian-replicate
%_bindir/xapian-replicate-server
%_bindir/xapian-tcpsrv
%_man1dir/*.1*
%doc AUTHORS ChangeLog* NEWS PLATFORMS README

%files -n libxapian
%_libdir/*.so.*

%files -n libxapian-devel
%_bindir/xapian-config
%_includedir/xapian.h
%_includedir/xapian/
%_libdir/libxapian.so
%_libdir/cmake/xapian/
%_datadir/aclocal/xapian.m4

%if_enabled static
%files -n libxapian-devel-static
%_libdir/libxapian.a
%endif

%files -n %name-doc
%doc docs/*.html
%doc docs/apidoc.pdf
%doc docs/apidoc/html/
%doc HACKING

%changelog
* Thu Jun 28 2012 Michael Shigorin <mike@altlinux.org> 1.2.12-alt1
- new version (watch file uupdate)
  + minor bugfixes/enhancements in 1.2.11 which had incorrect soname

* Thu May 10 2012 Michael Shigorin <mike@altlinux.org> 1.2.10-alt1
- new version (watch file uupdate)
  + assorted fixes

* Fri Mar 16 2012 Michael Shigorin <mike@altlinux.org> 1.2.9-alt1
- 1.2.9

* Fri Aug 12 2011 Michael Shigorin <mike@altlinux.org> 1.2.7-alt1
- 1.2.7

* Thu Apr 14 2011 Michael Shigorin <mike@altlinux.org> 1.2.5-alt1
- 1.2.5: http://trac.xapian.org/wiki/ReleaseOverview/1.2.5

* Wed Mar 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3-alt1.1
- Rebuilt for debuginfo

* Tue Dec 21 2010 Michael Shigorin <mike@altlinux.org> 1.2.4-alt1
- 1.2.4: http://trac.xapian.org/wiki/ReleaseOverview/1.2.4
  + NB: remote database protocol change
  + Omega improvements
  + binding fixes
- [backdated] not published due to python module strict dep

* Mon Oct 04 2010 Michael Shigorin <mike@altlinux.org> 1.2.3-alt1
- 1.2.3
- added cmake files to devel subpackage

* Tue Jun 22 2010 Michael Shigorin <mike@altlinux.org> 1.0.21-alt1
- 1.0.21 (postponed soname change till 1.2.x)

* Wed May 05 2010 Michael Shigorin <mike@altlinux.org> 1.2.0-alt1
- 1.2.0
  + dropped quartz* utils (obsolete)
  + added a few utilities in return
- buildreq

* Wed May 05 2010 Michael Shigorin <mike@altlinux.org> 1.0.20-alt1
- 1.0.20

* Thu Apr 15 2010 Michael Shigorin <mike@altlinux.org> 1.0.19-alt1
- 1.0.19

* Mon Feb 15 2010 Michael Shigorin <mike@altlinux.org> 1.0.18-alt1
- 1.0.18: minor fixes/improvements

* Fri Jan 08 2010 Michael Shigorin <mike@altlinux.org> 1.0.17-alt3
- hacked xapian-config due to missing .la files (closes: #22629)

* Sun Dec 13 2009 Michael Shigorin <mike@altlinux.org> 1.0.17-alt2
- buildreq (thx repocop)
- gzip ChangeLog

* Thu Nov 19 2009 Michael Shigorin <mike@altlinux.org> 1.0.17-alt1
- 1.0.17

* Thu Aug 27 2009 Michael Shigorin <mike@altlinux.org> 1.0.15-alt1
- 1.0.15

* Fri Jul 24 2009 Michael Shigorin <mike@altlinux.org> 1.0.14-alt2
- noarch doc subpackage (repocop)
- minor spec cleanup

* Wed Jul 22 2009 Michael Shigorin <mike@altlinux.org> 1.0.14-alt1
- 1.0.14: more robust shared library

* Mon May 25 2009 Michael Shigorin <mike@altlinux.org> 1.0.13-alt1
- 1.0.13: minor fixes

* Tue Apr 21 2009 Michael Shigorin <mike@altlinux.org> 1.0.12-alt1
- 1.0.12: minor fixes/improvements

* Tue Apr 07 2009 Michael Shigorin <mike@altlinux.org> 1.0.11-alt1
- 1.0.11: http://trac.xapian.org/wiki/ReleaseOverview/1.0.11

* Wed Dec 24 2008 Michael Shigorin <mike@altlinux.org> 1.0.10-alt1
- 1.0.10: http://trac.xapian.org/wiki/ReleaseOverview/1.0.10
  + minor bugfixes

* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 1.0.9-alt2
- applied repocop patch

* Mon Nov 03 2008 Michael Shigorin <mike@altlinux.org> 1.0.9-alt1
- 1.0.9: http://trac.xapian.org/wiki/ReleaseOverview/1.0.9
  + spelling correction even faster
  + fixed issues due to excess precision

* Thu Sep 04 2008 Michael Shigorin <mike@altlinux.org> 1.0.8-alt1
- 1.0.8: http://trac.xapian.org/wiki/ReleaseOverview/1.0.8
  + assorted fixes and performance improvements

* Wed Jul 16 2008 Michael Shigorin <mike@altlinux.org> 1.0.7-alt1
- 1.0.7: http://trac.xapian.org/wiki/ReleaseOverview/1.0.7
  + performance enhancements in some cases
  + minor bugfixes

* Tue Mar 18 2008 Michael Shigorin <mike@altlinux.org> 1.0.6-alt1
- 1.0.6 (minor feature enhancements)
  + single-ended range value checks
  + faster stemmers
  + improvements to xapian-check,
    xapian-compact metadata handling

* Sat Dec 22 2007 Michael Shigorin <mike@altlinux.org> 1.0.5-alt1
- 1.0.5 (minor feature enhancements)

* Tue Oct 30 2007 Michael Shigorin <mike@altlinux.org> 1.0.4-alt1
- 1.0.4: http://wiki.xapian.org/ReleaseOverview/1.0.4
  + faster matcher
  + fixed flint bug introduced in 1.0.3
  + remote protocol minor version has been increased

* Mon Oct 01 2007 Michael Shigorin <mike@altlinux.org> 1.0.3-alt1
- 1.0.3:
  + Flint DB format extended to support user metadata,
    1.0.2 and earlier won't be able to read 1.0.3 DBs
    (upgrade is automatic on opening with newer version)
- added xapian-inspect

* Thu Jul 05 2007 Michael Shigorin <mike@altlinux.org> 1.0.2-alt1
- 1.0.2: http://wiki.xapian.org/ReleaseOverview/1.0.2
  + remote protocol version increased
  + optional Btree tables (1.0.2 is backwards compatible with
    1.0.0 and 1.0.1 databases but older versions won't be able
    to read DBs created or modified by 1.0.2)
  + QueryParser improvements, incl. precedence fixes for
    logical operators
  + misc. bugfixes in NumberValueRangeProcessor, matcher,
    delete_document(), exception handling during commit

* Mon Jun 11 2007 Michael Shigorin <mike@altlinux.org> 1.0.1-alt1
- 1.0.1: http://wiki.xapian.org/ReleaseOverview/1.0.1
  + warning: forced incompatible ABI change due to fixing
    possible double-free error introduced in 1.0.0
  + on a similar note, remote protocol version increased
  + upstream promises to try hard and avoid ABI breakage
    during 1.0.x (after 1.0.1 till 1.1.0)
  = basically we have to relink clients (of both library
    and server)

* Tue May 22 2007 Michael Shigorin <mike@altlinux.org> 1.0.0-alt1
- 1.0.0
- removed all patches
- added Packager:
- updated BuildRequires:
- added xapian-check

* Mon Mar 12 2007 Michael Shigorin <mike@altlinux.org> 0.9.10-alt1
- 0.9.10
- removed patch1

* Tue Nov 28 2006 Michael Shigorin <mike@altlinux.org> 0.9.9-alt2
- apply upstream patch referenced from 0.9.9 release notes
- apply another patch for NEAR bug (from recoll author)

* Thu Nov 09 2006 Michael Shigorin <mike@altlinux.org> 0.9.9-alt1
- 0.9.9
- renamed from xapian to xapian-core accordingly to upstream
- apidoc is now PDF instead of PS
- spec cleanup
- SMP make

* Fri Nov 03 2006 Michael Shigorin <mike@altlinux.org> 0.9.8-alt1
- 0.9.8

* Wed Oct 11 2006 Michael Shigorin <mike@altlinux.org> 0.9.7-alt1
- 0.9.7
- added xapian-progsrv

* Mon May 15 2006 Michael Shigorin <mike@altlinux.org> 0.9.6-alt1
- 0.9.6 (minor bugfixes)
  + added Ruby bindings
- added manpages

* Mon Apr 10 2006 Michael Shigorin <mike@altlinux.org> 0.9.5-alt1
- 0.9.5

* Fri Mar 10 2006 Michael Shigorin <mike@altlinux.org> 0.9.4-alt1
- 0.9.4
- removed patch1

* Mon Feb 06 2006 Michael Shigorin <mike@altlinux.org> 0.9.2-alt3
- thanks upstream developer Olly Betts <olly/survex.com> for
  checking our package and Dmitry Levin <ldv@> for libtool/xapian-config
  advice and patch
- finished implementing -devel-static subpackage, just in case;
  build disabled by default
- temporarily removed unicode query patch to check whether it was relevant
  to Cyrillic icase search with recoll

* Tue Dec 06 2005 Michael Shigorin <mike@altlinux.org> 0.9.2-alt2
- applied patch to enable unicode querying (disables stemming)
- see also recoll (qt frontend)

* Mon Dec 05 2005 Michael Shigorin <mike@altlinux.org> 0.9.2-alt1
- built for ALT Linux (recoll dependency)
- removed static libraries (anyone needing 'em adds devel-static
  and mails me a spec patch)
- moved API docs to subpackage
- spec cleanup

