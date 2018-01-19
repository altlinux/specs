%def_disable static

Name: xfsprogs
Version: 4.14.0
Release: alt1

Summary: Utilities for managing the XFS filesystem
License: LGPL v2.1 (libhandle), GPL v2 (the rest)
Group: System/Kernel and hardware

Url: http://xfs.org
Source: %name-%version-%release.tar
Patch: %name-%version-alt.patch

Requires: libxfs = %version-%release
Conflicts: xfsdump < 3.0.0-alt1

%set_libtool_version 1.5

BuildPreReq: rpm-build >= 4.0.4-alt96.11

# makefiles are buggy
BuildConflicts: libxfs-devel

# Automatically added by buildreq on Wed May 27 2009 (-bi)
BuildRequires: libuuid-devel libblkid-devel

%description
XFS is a high performance journaling filesystem which originated
on the SGI IRIX platform.  It is completely multi-threaded, can
support large files and large filesystems, extended attributes,
variable block sizes, is extent based, and makes extensive use of
Btrees (directories, extents, free space) to aid both performance
and scalability.

Refer to the documentation at http://oss.sgi.com/projects/xfs/
for complete details.  This implementation is on-disk compatible
with the IRIX version of XFS.

This package contains a set of commands to use the XFS filesystem,
including mkfs.xfs.

%package -n libxfs
Summary: XFS filesystem-specific libraries
Group: System/Libraries

%description -n libxfs
This package contains the library needed to run programs dynamically
linked with libxfs.

%package -n libxfs-devel
Summary: XFS filesystem-specific devel libraries and headers
Group: Development/C
Requires: libxfs = %version-%release

%description -n libxfs-devel
libxfs-devel contains the libraries and header files needed to
develop XFS filesystem-specific programs.

You should install libxfs-devel if you want to develop XFS
filesystem-specific programs, If you install libxfs-devel, you'll
also want to install xfsprogs.

%if_enabled static
%package -n libxfs-devel-static
Summary: XFS filesystem-specific static libraries
Group: Development/C
Requires: libxfs-devel = %version-%release

%description -n libxfs-devel-static
libxfs-devel-static contains the static libraries needed to
develop XFS filesystem-specific programs.

You should install libxfs-devel-static if you want to develop XFS
filesystem-specific programs.

If you install libxfs-devel-static, you'll also want to install xfsprogs.
%endif

%prep
%setup
sed 's|^\(hardcode_into_libs\)=.*$|\1=no|' < %_bindir/libtool-default > libtool
install -pm755 include/install-sh install-sh

%build
libtoolize --copy --force
aclocal -I m4
autoconf
%configure \
	--libdir=/%_lib \
	--libexecdir=%_libdir
make DEBUG=-DNDEBUG LIBTOOL="`pwd`/libtool"

%install
make DIST_ROOT=%buildroot install install-dev
mkdir -p %buildroot%_libdir

for f in %buildroot/%_lib/*.so; do
	t=`objdump -p "$f" |awk '/SONAME/ {print $2}'`
	[ -n "$t" ]
	ln -nsf ../../%_lib/"$t" "%buildroot%_libdir/${f##*/}"
done

# Workaround bug in makefiles
rm -f %buildroot/%_lib/*.{so,*a}
rm -rf %buildroot%_datadir/doc/%name

%find_lang %name

%files -f %name.lang
/sbin/*
%_sbindir/*
%_mandir/man[85]/*
%doc doc/CHANGES.gz doc/CREDITS README

%files -n libxfs
/%_lib/*.so.*

%files -n libxfs-devel
%_libdir/*.so
%dir %_includedir/xfs
%_includedir/xfs/handle.h
%_includedir/xfs/jdm.h
%_includedir/xfs/linux.h
%_includedir/xfs/xfs.h
%_includedir/xfs/xfs_fs.h
%_includedir/xfs/xfs_arch.h
%_includedir/xfs/xfs_da_format.h
%_includedir/xfs/xfs_format.h
%_includedir/xfs/xfs_log_format.h
%_includedir/xfs/xfs_types.h
%_includedir/xfs/xqm.h
%_man3dir/*

%if_enabled static
%files -n libxfs-devel-static
%_libdir/*.a
%endif

%changelog
* Fri Jan 19 2018 Michael Shigorin <mike@altlinux.org> 4.14.0-alt1
- 4.14.0

* Sat Apr  1 2017 Terechkov Evgenii <evg@altlinux.org> 4.10.0-alt1
- 4.10.0 (ALT#33290)
- Drop libxfs-qa-devel subpackage (all header now in libxfs-devel)

* Thu Nov 26 2015 Michael Shigorin <mike@altlinux.org> 3.1.11-alt1
- 3.1.11
  + reset to pristine source, effectively reverting all patches
- applied patch series extracted from opensuse 13.1 updates'
  3.1.11-2.3.1 package to fix CVE-2012-2150

* Fri Apr 12 2013 Andrey Cherepanov <cas@altlinux.org> 3.1.8-alt2
- Create new package libxfs-qa-devel with full pack of includes

* Sun Apr 22 2012 Michael Shigorin <mike@altlinux.org> 3.1.8-alt1
- 3.1.8

* Wed Sep 07 2011 Michael Shigorin <mike@altlinux.org> 3.1.5-alt1
- 3.1.5

* Sat Sep 25 2010 Michael Shigorin <mike@altlinux.org> 3.1.3-alt1
- 3.1.3
- fixed installation with PLD patch from Gentoo over sbolshakov@'s
  partial fixups for 3.0.0
- disabled static subpackage by default (would need fixing)

* Mon Apr 12 2010 Michael Shigorin <mike@altlinux.org> 3.1.1-alt1.1
- fix symlink installation

* Tue Feb 23 2010 Michael Shigorin <mike@altlinux.org> 3.1.1-alt1
- 3.1.1
  + includes enhanced 4kb sector support (fixes: #23017)

* Wed May 27 2009 Michael Shigorin <mike@altlinux.org> 3.0.1-alt1
- 3.0.1
- built with libtool-1.5; notified upstream of FTBFS with 2.2
- clarified License: (thanks PLD spec)
- buildreq

* Wed Apr 15 2009 Michael Shigorin <mike@altlinux.org> 3.0.0-alt2.1
- built for Sisyphus

* Wed Apr  1 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0.0-alt2
- reflect binary transition between xfsprogs & xfsdump packages

* Wed Mar 25 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0.0-alt1
- 3.0.0 released

* Sat Dec  6 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.10.1-alt1
- 2.10.1 released

* Wed Mar 12 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.9.7-alt1
- 2.9.7 released

* Tue Sep 11 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.9.4-alt1
- 2.9.4 released

* Thu Nov  2 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.8.16-alt1
- 2.8.16 released
- patches rediffed/applied:
  + xfsprogs-2.8.11-alt-quiet-fsck.patch
  + xfsprogs-2.8.11-alt-shlib.patch

* Thu Sep 14 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.8.11-alt1
- 2.8.11

* Tue Mar 28 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.7.11-alt1
- 2.7.11 released

* Mon Jan 16 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.6.13-alt1
- 2.6.13 (thanks to rider@)

* Sat May 15 2004 Alexander Bokovoy <ab@altlinux.ru> 2.6.4-alt1
- 2.6.4

* Thu Dec 11 2003 Alexander Bokovoy <ab@altlinux.ru> 2.6.0-alt1
- 2.6.0
- Build everything dynamically

* Thu Aug 21 2003 Dmitry V. Levin <ldv@altlinux.org> 2.3.9-alt3
- Explicitly use old libtool for build.

* Wed Aug 13 2003 Dmitry V. Levin <ldv@altlinux.org> 2.3.9-alt2
- Removed explicit kernel dependencies.
- Corrected interpackage dependencies.
- Updated build dependencies.
- Fixed -devel packaging.
- Specfile cleanup.

* Tue May 20 2003 Alexander Bokovoy <ab@altlinux.ru> 2.3.9-alt1
- 2.3.9, changed maintainer
- Updated buildrequires
- Removed outdated patches
- Spec clean up

* Fri Dec 27 2002 Konstantin Volckov <goldhead@altlinux.ru> 2.0.6-alt1
- 2.0.6
- Fixed buildrequires

* Wed Apr 10 2002 Konstantin Volckov <goldhead@altlinux.ru> 2.0.1-alt0.1cvs
- CVS version

* Wed Nov 21 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.3.13-alt1
- 1.3.13

* Wed Oct 31 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.3.7-alt1
- 1.3.7

* Thu Sep 20 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.3.5-alt1
- First build for Sisyphus

* Fri Sep  7 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.3.5-2mdk
- Fix provides.

* Fri Sep  7 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.3.5-1mdk
- 1.3.5.
- Split lib in subpackage.
- Rework the spec.

* Wed May  2 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.2.0-1mdk
- Fist attempt based on the SGI spec.


