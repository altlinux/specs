Name: reiserfsprogs
Version: 3.6.21
Release: alt1

Summary: The utilities to create Reiserfs volume
License: GPL
Group: System/Kernel and hardware

Url: ftp://ftp.kernel.org/pub/linux/utils/fs/reiserfs/
Source: %url/%name-%version.tar.bz2
Patch0: reiserfsprogs-3.6.2-make-the-force-option-works-in-resize_reiserfs.patch
Patch1: 02-mkreiserfs-quiet.diff
Patch2: broken-inline.diff
Patch3: reiserfs-large-block-warning.diff 
Patch4: reiserfsprogs-fsck-mapid.diff
Patch5: reiserfsprogs-external-journal-changes.diff
Patch6: reiserfsprogs-remove-stupid-fsck_sleep.diff
Patch7: reiserfsprogs-progress.diff
Patch8: reiserfsprogs-reorder-libs.diff
Patch9: reiserfsprogs-mkfs-use-o_excl.diff
Patch10: reiserfsprogs-3.6.19-alt-debian-headers.patch
Packager: Michael Shigorin <mike@altlinux.org>

Obsoletes: reiserfs-utils
Conflicts: progsreiserfs
Provides: reiserfs-utils = %version-%release

# Automatically added by buildreq on Tue Aug 31 2010
BuildRequires: libuuid-devel

%description
Reiserfs is a file system using a plug-in based object oriented
variant on classical balanced tree algorithms. The results when
compared to the ext2fs conventional block allocation based file system
running under the same operating system and employing the same
buffering code suggest that these algorithms are overall more
efficient, and are becoming more so every passing month.  Loosely
speaking, every month we find another performance cranny that needs
work, and we fix it, and every month we find some way of improving our
overall general usage performance. The improvement in small file space
and time performance suggests that we may now revisit a common OS
design assumption that one should aggregate small objects using layers
above the file system layer. Being more effective at small files DOES
NOT make us less effective for other files, this is a general purpose
FS, and our overall traditional FS usage performance is high enough to
establish that. Reiserfs has a commitment to opening up the FS design
to contributions, and we are now now adding plug-ins so that you can
create your own types of directories and files.

%prep
%setup
%patch0 -p0
#patch1 -p1
%patch2
#patch3 -p1
#patch4 -p1
#patch5 -p1
#patch6 -p1
#patch7 -p1
#patch8 -p1
#patch9 -p1
#patch10 -p1

%build
%configure
%make OPTFLAGS="%optflags"

%install
mkdir -p %buildroot%_man8dir/
%makeinstall
mv %buildroot/%_sbindir %buildroot/sbin
ln -s mkreiserfs %buildroot/sbin/mkfs.reiserfs
ln -s reiserfsck %buildroot/sbin/fsck.reiserfs
ln -s mkreiserfs.8 %buildroot%_man8dir/mkfs.reiserfs.8
ln -s reiserfsck.8 %buildroot%_man8dir/fsck.reiserfs.8

%files
%doc README ChangeLog COPYING
/sbin/*
%_mandir/*/*

%changelog
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
