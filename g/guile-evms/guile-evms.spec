Name: guile-evms
Version: 0.4
Release: alt11

Summary: Guile bindings for EVMS
License: GPL
Group: Development/Scheme

Buildrequires: guile18-devel libblkid-devel libe2fs-devel libevms-devel swig

Source: %name-%version-%release.tar

%description
Guile bindings for EVMS, volume management library
http://evms.sourceforge.net

%prep
%setup

%build
make

%install
make install DESTDIR=%buildroot

%files
%_libdir/libguile-evms.so*
%_datadir/guile/site/evms.scm

%changelog
* Thu Jul 07 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4-alt11
- revert back to pre-alt10 state (#25774, #25861)

* Tue Jun 21 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4-alt10
- no more mkswap on already existing swap partition (#25774)

* Thu May 26 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4-alt9
- recognize btrfs plugin as fsim

* Tue Sep 21 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4-alt8
- allow / on lvm (#23801)

* Mon Dec 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4-alt7
- buildreqs fixed 

* Wed Jun 17 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4-alt6
- offer `relatime' mount option by default

* Mon Jun  1 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4-alt4
- disallow "/" and "/boot" placement on LVM (#19805, #19807)

* Sun Apr 12 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4-alt3
- fix regression around swapon invocation (#19555, #19556)

* Wed Apr  8 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4-alt2
- added swapon invocation at final stage

* Tue Dec  9 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4-alt1
- rebuilt with guile 1.8

* Fri Jul 20 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt12
- added missing comma in ntfs mount options string, closes \#12378

* Thu Jul 12 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt11
- changed ntfs mount options to ntfs-3g

* Wed May 23 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt10
- fixed vfat mount options, closes \#11821

* Tue Apr  3 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt9
- offer sane mount point & options for fat/ntfs
- added /opt to well-known mountpoints
- do not format /opt & /usr/local by default
- set default 1 for fstab's fs_freq
- do not rely on uncertain libblkid in swap case

* Fri Mar 30 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt8
- clear memoised object/plugin pool before engine open

* Mon Mar 26 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt7
- fixed handling of empty/nonexistent drive model
- do not force mkfs on "/home" or "/mnt/..." by default
- offer sane defaults for well-known mount point options

* Fri Mar  9 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt6
- attached context to task procs
- made inactive `check order' option

* Thu Mar  1 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt5
- fixed hang on sysfs read, \#10953

* Thu Feb 22 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt4
- fixed blkrrpart on cciss/rd devices
- revert to old value when setmntent cancelled
- disk model getter added
- be stricter on acceptable mountpoints

* Thu Feb  8 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt3
- fstab order fixed

* Tue Jan 30 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt2
- do not try to mount swaps
- fixup incorrectly assigned mntpass values

* Fri Jan 26 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt1
- workaround UUID inconsistency between evms volume and bottomed partition

* Fri Dec 22 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt8
- installer mode: force mkfs during finalize in certain cases

* Tue Dec 19 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt7
- only `mount options' for swap
- dump all swaps into fstab
- reread partition table of each disk at exit

* Tue Dec 12 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt6
- reset possibly assigned mountpoint on fsim removal
- validate mountpoints

* Tue Dec  5 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt5
- assume swapfs as fsim
- do not expose evms names on compat volumes, if possible

* Wed Nov 29 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt4
- mount at exit all assigned volumes when in installer mode

* Mon Nov 20 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt3
- added wrappers for getmntent() and blkid_get_tag_value()

* Tue Nov  7 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt2
- raise exception on unsuccessful option value setting

* Mon Oct 23 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt1
- added task-like interface to mount-related ops
- storage names mangled to prevent clashes with alterator's naming scheme

* Mon Oct  2 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt1
- Initial build.
