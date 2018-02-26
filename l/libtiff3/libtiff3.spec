Name: libtiff3
Version: 3.5.7
Release: alt8

Summary: A library of functions for manipulating TIFF format image files
License: BSD-like
Group: System/Libraries

Source: ftp://ftp.remotesensing.org/pub/libtiff/tiff-v%version.tar.bz2

Patch1: libtiff-3.5.7-chris-bound.patch
Patch2: libtiff-3.5.7-alt-bound-try2.patch
Patch3: libtiff-3.5.7-up-ChopUpSingleUncompressedStrip.patch
Patch4: libtiff-3.5.7-suse-alt-bound-fix2.patch
Patch5: libtiff-3.5.7-alt-ycbcrsubsampling.patch
Patch6: libtiff-3.7.1-alt-tiffdump.patch
Patch7: libtiff-3.5.7-cvs-20050506-CheckDirCount.patch

Patch10: tiff-v3.5-shlib.patch
Patch11: libtiff-3.5.5-codecs.patch
Patch12: libtiff-3.5.5-stupid_cd_output.patch
Patch13: libtiff-3.5.5-buildroot.patch
Patch14: libtiff-3.5.7-64bit.patch
Patch15: libtiff-v3.5.7-largefile.patch
Patch16: libtiff-v3.5.7-exit.patch
Patch17: tiff-v3.5.7-alt-fax2tiff.patch

# Automatically added by buildreq on Sun Dec 27 2009
BuildRequires: libjpeg-devel zlib-devel

%description
The %name package contains a compatibility version of libtiff library.

This package should be installed only if you need libtiff.so.3
and can't rebuild the software in question with contemporary version.

%prep
%setup -n tiff-v%version
%patch1 -p1
%patch2 -p1
%patch3 -p0
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1                                                                                         
%patch15 -p1
%patch16 -p1
%patch17 -p1

find -type d -name CVS |xargs -r rm -rf
find -type d -name CVS -print0 |
	xargs -r0 rm -rf --

%build
perl -pi -e 's|(DIR_.*)="?/usr/lib"?|\1="%_libdir"|' config.site
./configure --target=%_target_platform \
	--with-GCOPTS="$RPM_OPT_FLAGS" << EOF
no
%_bindir
%_libdir
%_includedir
%_mandir
%_docdir/%name-%version
bsd-source-cat
yes
EOF
cd libtiff
ln -s libtiff.so.3.5 libtiff.so
cd ..
COPTS="%optflags" make

%install
install -pDm644 libtiff/libtiff.so.3.5 %buildroot%_libdir/libtiff.so.%version

%files
%_libdir/*.so.*
%doc COPYRIGHT README

%changelog
* Sun Dec 27 2009 Michael Shigorin <mike@altlinux.org> 3.5.7-alt8
- rebuilt for Sisyphus, thanks Denis G. Samsonenko
  + needed e.g. for Canon's proprietary printer drivers
- merged with the very latest updates/Master/2.4 spec and patches
- added -lm to libtiff-3.5.5-codecs.patch
- simplified installation even more
- minor spec cleanup

* Fri Jul 03 2009 Denis G. Samsonenko <d.g.samsonenko@gmail.com> 3.5.7-alt4.0.sdg1
- build as libtiff3 to provide libtiff.so.3

* Wed May 11 2005 Dmitry V. Levin <ldv@altlinux.org> 3.5.7-alt6.M24.3
- Fixed one more potential heap overflow bug.

* Thu Dec 23 2004 Dmitry V. Levin <ldv@altlinux.org> 3.5.7-alt6.M24.2
- Fixed potential crash in tiffdump(1).

* Tue Dec 21 2004 Dmitry V. Levin <ldv@altlinux.org> 3.5.7-alt6.M24.1
- Additional integer overflow fixes in CheckMalloc().

* Wed Oct 27 2004 Dmitry V. Levin <ldv@altlinux.org> 3.5.7-alt6.M24
- Check for invalid YCbCr subsampling.

* Mon Oct 04 2004 Dmitry V. Levin <ldv@altlinux.org> 3.5.7-alt5
- Backported upstream fixes for several buffer overrun bugs,
  reported by Chris Evans (CAN-2004-0803).
- Fixed numerous integer overflows related to memory management
  which have security implications (CAN-2004-0886).

* Wed Oct 01 2003 Stanislav Ievlev <inger@altlinux.ru> 3.5.7-alt4
- fix building in hasher

* Thu Jan 16 2003 Stanislav Ievlev <inger@altlinux.ru> 3.5.7-alt3
- fix fax2tiff crash

* Tue Sep 10 2002 Stanislav Ievlev <inger@altlinux.ru> 3.5.7-alt2
- Rebuild with gcc3

* Sat Aug 24 2002 Rider <rider@altlinux.ru> 3.5.7-alt1
- 3.5.7
- patches from RedHat

* Mon Apr 15 2002 Rider <rider@altlinux.ru> 3.5.5-ipl3mdk
- rebuild

* Sat Jan 06 2001 Dmitry V. Levin <ldv@fandra.org> 3.5.5-ipl2mdk
- Fixed config and install.
- Split into %name, %name-utils and %name-devel.

* Wed Oct 18 2000 Dmitry V. Levin <ldv@fandra.org> 3.5.5-ipl1mdk
- RE adaptions.

* Mon Jun 26 2000 Alexandre Dussart <adussart@mandrakesoft.com> 3.5.5-1mdk
- 3.5.5
- Removed obsolete patch(check for libc6).
- Rewrittent some spec section to be more generic.
- Updated shlib patch.
- Removed LIBVER define.

* Tue Apr 18 2000 Warly <warly@linux-mandrake.com> 3.4-10mdk
- New group

* Sun Oct 31 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- Enable SMP check/build
- Use good macro (old one may have bziped whole dirs)
- defattr

* Mon Jul 12 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- bzip manpages

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 6)

* Wed Jan 13 1999 Cristian Gafton <gafton@redhat.com>
- build for glibc 2.1

* Wed Jun 10 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Wed Jun 10 1998 Michael Fulbright <msf@redhat.com>
- rebuilt against fixed jpeg libs (libjpeg-6b)

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Oct 13 1997 Donnie Barnes <djb@redhat.com>
- new version to replace the one from libgr
- patched for glibc
- added shlib support
