%set_automake_version 1.10
%set_autoconf_version 2.60

Name: fuse-encfs
Summary: Encrypted pass-thru filesystem for Linux
Version: 1.7.4
Release: alt1.3
License: GPL
Group: System/Kernel and hardware
Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name.tar
Url: http://pobox.com/~vgough/encfs

Patch1: encfs.link.patch
Patch2: encfs.static.char.patch
Patch3: 0001-boost-serialization-version-workaround.patch

# Automatically added by buildreq on Sun Feb 03 2008
BuildRequires: boost-devel gcc-c++ libattr-devel libfuse-devel libssl-devel librlog14-devel

BuildRequires: cvs

BuildRequires: libfuse-devel >= 2.1
BuildRequires: boost-devel boost-filesystem-devel

Requires: fuse
Requires: libssl >= 0.7.9g

Provides: encfs
Obsoletes: encfs

%description
EncFS implements an encrypted filesystem in userspace using FUSE.  FUSE
provides a Linux kernel module which allows virtual filesystems to be written
in userspace.  EncFS encrypts all data and filenames in the filesystem and
passes access through to the underlying filesystem.  Similar to CFS except that
it does not use NFS.

%prep
%setup -c %name-%version
## applied in upstream
#patch1 -p1
#patch2 -p2
## do we need it anymore???
#patch3 -p2

%build
CFLAGS="$CFLAGS -g -D_FILE_OFFSET_BITS=64"
export CFLAGS
%autoreconf
%configure \
    --enable-debug=no \
    --with-boost-system=boost_system-mt \
    --with-boost-filesystem=boost_filesystem-mt \
    --with-boost-serialization=boost_serialization-mt
%make_build SED=%_bindir/sed

# Testing for correct build
encfs/test

%install
%makeinstall_std
%find_lang encfs

%files -f encfs.lang
%_bindir/*
%_man1dir/*
%_libdir/*.so.*
%exclude %_libdir/*.so

%changelog
* Thu Apr 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.4-alt1.3
- Rebuilt with Boost 1.49.0

* Sun Dec 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.4-alt1.2
- Rebuilt with Boost 1.48.0

* Tue Aug 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.4-alt1.1
- Rebuilt with Boost 1.47.0

* Mon May 16 2011 Mykola Grechukh <gns@altlinux.ru> 1.7.4-alt1
- new version

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.2-alt1.2
- Rebuilt with Boost 1.46.1

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 1.7.2-alt1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Tue Sep 28 2010 Mykola Grechukh <gns@altlinux.ru> 1.7.2-alt1
- new version. Dropped obsolete patches

* Mon Jun 14 2010 Denis Smirnov <mithraen@altlinux.ru> 1.5.2-alt8
- fix build with new boost (thanks to slazav@)

* Sun Sep 13 2009 Denis Smirnov <mithraen@altlinux.ru> 1.5.2-alt7
- rebuild

* Wed Jul 22 2009 Denis Smirnov <mithraen@altlinux.ru> 1.5.2-alt6
- fix build

* Sun Jul 19 2009 Denis Smirnov <mithraen@altlinux.ru> 1.5.2-alt5
- not package %_libdir/*.so (fix SharedLibs Policy violation)

* Mon Jul 13 2009 Denis Smirnov <mithraen@altlinux.ru> 1.5.2-alt4
- fix build with new C++ libraries

* Mon Dec 08 2008 Denis Smirnov <mithraen@altlinux.ru> 1.5.2-alt3
- fix build with new librlog

* Mon Dec 01 2008 Denis Smirnov <mithraen@altlinux.ru> 1.5.2-alt2
- rebuild

* Sun Nov 30 2008 Evgeny Sinelnikov <sin@altlinux.ru> 1.5.2-alt1
- update to 1.5.2

* Sun Feb 03 2008 Denis Smirnov <mithraen@altlinux.ru> 1.4.1.1-alt1
- update to 1.4.1.1
- fix build on x86_64 (upstream)

* Wed Feb 21 2007 Denis Smirnov <mithraen@altlinux.ru> 1.3.1-alt6
- rebuild with new fuse

* Wed Jan 10 2007 Denis Smirnov <mithraen@altlinux.ru> 1.3.1-alt5
- don't require fixed version of fuse

* Fri Dec 15 2006 Denis Smirnov <mithraen@altlinux.ru> 1.3.1-alt4
- rebuild with last fuse

* Thu Oct 19 2006 Denis Smirnov <mithraen@altlinux.ru> 1.3.1-alt3
- rebuild with last fuse and rlog

* Tue Oct 17 2006 Denis Smirnov <mithraen@altlinux.ru> 1.3.1-alt2
- rebuild with gcc 4.1 (instead of 3.4)

* Mon Jun 19 2006 Denis Smirnov <mithraen@altlinux.ru> 1.3.1-alt1
- version update

* Sat Mar 25 2006 Denis Smirnov <mithraen@altlinux.ru> 1.3.0-alt1
- version update

* Sun Nov 27 2005 Denis Smirnov <mithraen@altlinux.ru> 1.2.4-alt3
- rebuild with new fuse

* Tue Nov 22 2005 Denis Smirnov <mithraen@altlinux.ru> 1.2.4-alt2
- rebuild with new fuse

* Wed Sep 28 2005 Denis Smirnov <mithraen@altlinux.ru> 1.2.4-alt1
- version update

* Sun Aug 07 2005 Denis Smirnov <mithraen@altlinux.ru> 1.2.3-alt1
- version update

* Wed Jun 08 2005 Denis Smirnov <mithraen@altlinux.ru> 1.2.2-alt1
- version update

* Sat Apr 23 2005 Denis Smirnov <mithraen@altlinux.ru> 1.2.1-alt1
- version update

* Fri Apr 22 2005 Denis Smirnov <mithraen@altlinux.ru> 1.2.0-alt4
- rebuild with new fuse and renamed

* Wed Apr 20 2005 Denis Smirnov <mithraen@altlinux.ru> 1.2.0-alt3
- rebuild with new fuse

* Tue Feb 15 2005 Denis Smirnov <mithraen@altlinux.ru> 1.2.0-alt2
- avfs-fuse renamed to fuse

* Fri Feb 11 2005 Denis Smirnov <mithraen@altlinux.ru> 1.2.0-alt1
- version update

* Thu Jan 20 2005 Denis Smirnov <mithraen@altlinux.ru> 1.1.11-alt1
- version update

* Mon Jan 03 2005 Denis Smirnov <mithraen@altlinux.ru> 1.1.9-alt5
- rebuild with new fuse

* Thu Dec 23 2004 Denis Smirnov <mithraen@altlinux.ru> 1.1.9-alt4
- rebuild with new fuse

* Tue Dec 07 2004 Denis Smirnov <mithraen@altlinux.ru> 1.1.9-alt3
- rebuild with new fuse

* Tue Nov 02 2004 Denis Smirnov <mithraen@altlinux.ru> 1.1.9-alt2
- requires fuse version

* Thu Oct 28 2004 Denis Smirnov <mithraen@altlinux.ru> 1.1.9-alt1
- first sisyphus build

