%define _sbindir /sbin

Name: reiserfsprogs
Version: 3.6.22
Release: alt1
Summary: The utilities to create Reiserfs volume
License: GPLv2 with "Anti-Plagiarism" modification
Group: System/Kernel and hardware
Url: http://git.kernel.org/?p=linux/kernel/git/jeffm/%name.git;a=summary
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Obsoletes: reiserfs-utils
Conflicts: progsreiserfs
Provides: reiserfs-utils = %version-%release

# Automatically added by buildreq on Tue Aug 31 2010
BuildRequires: libuuid-devel

%description
Reiserfs is a file system using a plug-in based object oriented variant
on classical balanced tree algorithms.
This package contains utilities for create, resize, check, repair, tune, debug
Reiserfs.


%prep
%setup
%patch -p1


%build
%autoreconf
%configure --enable-largefile
%make_build V=1


%install
%makeinstall_std
ln -s mkreiserfs.8 %buildroot%_man8dir/mkfs.reiserfs.8
ln -s reiserfsck.8 %buildroot%_man8dir/fsck.reiserfs.8


%files
%doc README COPYING
%_sbindir/*
%_man8dir/*


%changelog
* Sat Feb 09 2013 Led <led@altlinux.ru> 3.6.22-alt1
- 3.6.22
- fixed URL
- fixed License
- cleaned up and fixed description
- cleaned up spec

* Tue Aug 31 2010 Michael Shigorin <mike@altlinux.org> 3.6.21-alt1
- 3.6.21 (thanks led@ for every hint on this one)
- applied cooker patch to fix linking against libblkid
  (replaced force-resize patch with theirs version too)
- patch{1,3,4,5,6,9} applied upstream
- patch10 failed to apply cleanly (is it still needed?)
- buildreq

* Fri Mar 21 2008 Michael Shigorin <mike@altlinux.org> 3.6.19-alt4
- adapted Debian patch to fix build against current kernel headers;
  thanks Kirill Shutemov (kas@)

* Sun Apr 08 2007 Michael Shigorin <mike@altlinux.org> 3.6.19-alt3
- applied openSUSE patches from reiserfs-3.6.19-50 package:
  + O_EXCL to reiserfs_create()'s open() call
  + progress bar and silenced journal replay messages with -a
  + removed fsck_sleep call that causes reiserfsck to stay in the
    background for 5s, causing problems with multipath and kpartx
  + fix for off-by-one in memory allocation of oid map.
    Would cause crash on file systems with OID 2^32-2 in use
  + better defaults for journals on external devices..
  + warning for block sizes > 4k
- added (but didn't apply) progress/spinner patch -- nobody
  asked for that, and it needed another libs reordering fix,
  and that fix would need another one to link with --as-needed

* Sun Apr 08 2007 Michael Shigorin <mike@altlinux.org> 3.6.19-alt2
- minor spec cleanup
- updated url to be easier to monitor
- added Packager:

* Fri Oct 29 2004 Anton Farygin <rider@altlinux.ru> 3.6.19-alt1
- new version

* Thu Jun 03 2004 Anton Farygin <rider@altlinux.ru> 3.6.17-alt2
- added conflicts with progsreiserfs

* Tue May 18 2004 Anton Farygin <rider@altlinux.ru> 3.6.17-alt1
- 3.6.17

* Wed May 12 2004 Anton Farygin <rider@altlinux.ru> 3.6.14-alt1
- first build for Sisyphus, based on specfile from MDK
