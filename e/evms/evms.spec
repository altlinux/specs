%def_with x
%def_enable gpt
%def_disable ha
%def_disable ogfs
%def_disable ocfs2
%def_disable static

Name: evms
Version: 2.5.5
Release: alt23

Summary: Enterprise Volume Management System utilities
License: GPL
Group: System/Kernel and hardware
Url: http://www.sourceforge.net/projects/evms

Source: %name-%version-%release.tar.bz2

BuildRequires: glib2-devel libe2fs-devel libncurses-devel libreadline-devel libuuid-devel

%if_with x
BuildRequires: gtk+-devel
%endif

%if_enabled ha
BuildRequires: libdevmapper-devel heartbeat
%endif

%package -n lib%name
Summary: Enterprise Volume Management System libraries
Group: System/Libraries

%package -n lib%name-devel
Summary: Enterprise Volume Management System development part
Group: Development/C
Requires: lib%name = %version-%release
Provides: %name-devel = %version-%release

%package -n lib%name-devel-static
Summary: Enterprise Volume Management System static libs
Group: Development/C
Requires: lib%name = %version-%release

%package -n %name-cli
Summary: EVMS commandline tool
Group: System/Kernel and hardware
Requires: evms = %version-%release

%package -n %name-ncurses
Summary: EVMS UI
Group: System/Kernel and hardware
Requires: evms = %version-%release

%package -n %name-gui
Summary: EVMS GUI
Group: System/Kernel and hardware
Requires: evms = %version-%release

%description
This package contains the user-space tools needed to manage EVMS (Enterprise
Volume Management System) volumes.

In order to use these user-space tools, you must also have your kernel patched
with the most recent EVMS code. This code is available in the source package
on the project web page http://www.sf.net/projects/evms/

Please see the EVMS-HOWTO on the project web page or in the source package
for detailed instructions on patching your kernel with EVMS and using the
tools after installation.

%description -n lib%name
This package contains libs needed to manage EVMS (Enterprise
Volume Management System) volumes.

%description -n lib%name-devel
This package contains develop tools needed to manage EVMS (Enterprise
Volume Management System) volumes.

%description -n lib%name-devel-static
This package contains static libs for develop tools needed to manage EVMS
(Enterprise Volume Management System) volumes.

%description -n %name-cli
Command line tool for EVMS

%description -n %name-ncurses
Ncurses ui tool for EVMS

%description -n %name-gui
GTK+ ui tool for EVMS

%prep
%setup

%build
%autoreconf
%add_optflags -DEVMS_DEBUG
%configure  --libdir=/%_lib --sbindir=/sbin \
    --disable-s390 \
    %{subst_enable gpt} \
    %{subst_enable ocfs2} \
    %{subst_enable ogfs} \
    %{subst_enable ha} \
    %{!?_with_x: --disable-gui --disable-gtktest} \
    %{subst_enable static} \
    #

make LD_LIBRARY_PATH=%buildroot/%_lib
make -C tests evms_deactivate

%install
mkdir -p %buildroot{%_sysconfdir,%_libdir,%_sbindir/sbin}
%make_install DESTDIR=%buildroot prefix=%buildroot%_prefix install
install -pD -m 0755 altlinux/startevms %buildroot/sbin
install -pm0755 tests/evms_deactivate %buildroot/sbin
install -pm0644 tests/evms_deactivate.8 %buildroot%_man8dir
mv %buildroot/sbin/%{?_with_x:{evmsn,evmsgui}}%{!?_with_x:evmsn} %buildroot%_sbindir/
for f in %buildroot/%_lib/*.so; do
ln -sf ../../%_lib/`readlink $f` %buildroot%_libdir/${f##*/}
done
rm -f %buildroot/%_lib/*.so

mkdir -p %buildroot%_sysconfdir/sysconfig
cat <<EOF > %buildroot%_sysconfdir/sysconfig/%name
# if 'yes' tune evms.conf during evms startup
# to avoid scans on nonexistent legacy devices
EVMS_RECONFIG=no
EOF

%files
%doc doc/linuxrc ChangeLog INSTALL* README PLUGIN.IDS TERMINOLOGY
%config(noreplace) %_sysconfdir/sysconfig/%name
/sbin/startevms
/sbin/%{name}_*
%_man8dir/%{name}_*

%files -n lib%name
%config(noreplace) %_sysconfdir/%name.conf
/%_lib/%name
/%_lib/lib%name-*.so.*

%files -n lib%name-devel
%_libdir/lib%name.so
%_includedir/%name

%if_enabled static
%files -n lib%name-devel-static
%_libdir/lib%name.a
%endif #static

%files -n %name-cli
/sbin/%name
%if_enabled ha
/sbin/%{name}d*
%endif
%_man8dir/%name.*

%files -n %name-ncurses
%_sbindir/%{name}n

%if_with x
%files -n %name-gui
%_sbindir/%{name}gui
%endif

%changelog
* Thu Feb 09 2012 Timur Aitov <timonbl4@altlinux.org> 2.5.5-alt23
- btrfs plugin: fixed test for mkfs.btrfs

* Mon Oct 24 2011 Timur Aitov <timonbl4@altlinux.org> 2.5.5-alt22
- btrfs plugin: test for mkfs.btrfs
- raid10: check count of selected object

* Wed Sep 21 2011 Timur Aitov <timonbl4@altlinux.org> 2.5.5-alt21
- dos plugin: fixed creation logical partition

* Thu Aug 25 2011 Timur Aitov <timonbl4@altlinux.org> 2.5.5-alt20
- added BIOS_BOOT_PARTITION type to GPT

* Thu Jul 07 2011 Timur Aitov <timonbl4@altlinux.org> 2.5.5-alt19
- added md RAID10 level support
- fixed name for raid ver.1.0
- btrfs plugin: fixed allocate memory

* Wed May 25 2011 Timur Aitov <timonbl4@altlinux.org> 2.5.5-alt18
- BtrFS FSIM

* Thu Apr 28 2011 Andriy Stepanov <stanv@altlinux.ru> 2.5.5-alt17
- Align on 2048 sectors boundary DOS segments. Not on cylinder boundary.
  TODO: do same for GPT segments.

* Mon Apr 25 2011 Andriy Stepanov <stanv@altlinux.ru> 2.5.5-alt16
- Fix Partition table header size.

* Mon Apr 25 2011 Andriy Stepanov <stanv@altlinux.ru> 2.5.5-alt15
- Use GPT_VERSION_1 in revision "Partition table header".

* Tue Oct 26 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5.5-alt14
- made ext4 the default for ext filesystem family
- added md RAID6 level support

* Mon Jun 22 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5.5-alt13
- Ext2/3: allow ext4 create, off by default

* Wed Jun 17 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5.5-alt12
- CVS snapshot @ 20090212
- fixed raid create regression (#20453)

* Sat Dec  6 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5.5-alt11
- obsolete by filetriggers macros removed

* Mon Oct 27 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5.5-alt10
- fixed build on recent toolchain
- CVS snapshot @ 20080827

* Thu Apr  3 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5.5-alt9
- avoid excessive fatresize invocations (#14445)

* Tue Feb 26 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5.5-alt8
- CVS snapshot @ 20080108
- cease use of asm/page.h

* Fri Dec  7 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5.5-alt7
- fixed incompatibility in lvm pv metadata between lvm & evms

* Wed Jun 20 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5.5-alt6
- disallow consecutive shrink ops below min_fs_size
- do not try to discover ramdisks

* Thu Apr  5 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5.5-alt5
- ntfs plugin: cache min_fs_size in private_date, closes \#10830
- lvm2 plugin: restrict vg & lv names
- fat plugin: do not pretend on fsck
- gpt plugin: handle cciss devices uniform with dos partitions
- suppress error when activating container on already active md

* Tue Apr  3 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5.5-alt4
- removed conflict with lvm2

* Sun Mar 11 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5.5-alt3
- enable gpt plugin build, closes \#10316
- packaged evms_deactivate utility, closes \#11013
- moved evms.conf to libevms subpackage, closes \#11049

* Thu Dec 21 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5.5-alt2
- allow create swap on fresh volume
- fix use of unitialised mem in xfs fsim

* Sun Aug 06 2006 L.A. Kostis <lakostis@altlinux.ru> 2.5.5-alt1
- change Packager.
- 2.5.5 first try:
	- add -ismounted patch (tnx to sbolshakov@);
	- remove FAT FSIM patch (added by upstream);
	- remove -internal-api-fix patch (fixed in upstream);
	- remove -plugins_md_cleanup patch (fixed in upstream);
	- update -alt-config patch (make device_size_prompt = no in evms.conf);
	- don't package evmsd (until linux-ha tools get ready).

* Mon Jun 26 2006 LAKostis <lakostis at altlinux.ru> 2.5.3-alt2
- NMU.
- fix build w/ --as-needed.

* Sat Jan 07 2006 LAKostis <lakostis at altlinux.ru> 2.5.3-alt1.2
- NMU.
- move kernel-feat to separate packages.
- s/kernel-headers-std26-up/linux-libc-headers/
- applied patch removing too deep kernel-specific deps in 
  plugins/md.
- Added switch for static/nonstatic builds.
- Added autoreconf instead autoconf.

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.5.3-alt1.1
- Rebuilt with libreadline.so.5.
 
* Wed Sep 21 2005 Zhenja Kaliuta <tren@altlinux.ru> 2.5.3-alt1
- New upstream release
- Removed md-raid patch from 2.4 branch
- Added fix to internal api (patch 9)

* Thu Apr 14 2005 Kachalov Anton <mouse@altlinux.ru> 2.5.2-alt1
- New upstream release
- FAT FSIM
- x86_64 support
- Disable MD specific patches due to resctructured source since 2.5.1

* Wed Dec 22 2004 Zhenja Kaliuta <tren@altlinux.ru> 2.5.0-alt1
- New upstream release

* Mon Oct 25 2004 Zhenja Kaluta <tren@altlinux.ru> 2.4.0-alt1
- New upstream release

* Tue Jun 22 2004 Zhenja Kaluta <tren@altlinux.ru> 2.3.3-alt3
- Fixed expr bug

* Thu May 13 2004 Zhenja Kaluta <tren@altlinux.ru> 2.3.3-alt2
- Removed db-claim

* Thu May 13 2004 Zhenja Kaluta <tren@altlinux.ru> 2.3.3-alt1
- New upstream release

* Tue May 11 2004 Zhenja Kaluta <tren@altlinux.ru> 2.3.2-alt3
- Removed lvm depends for 2.6

* Wed Apr 28 2004 Zhenja Kaluta <tren@altlinux.ru> 2.3.2-alt2
- Fixed library symlink

* Tue Apr 27 2004 Zhenja Kaluta <tren@altlinux.ru> 2.3.2-alt1
- New upstream release
- Updated cli-print_value.patch
- Updated pipe patch

* Mon Apr 26 2004 Zhenja Kaluta <tren@altlinux.ru> 2.3.1-alt1
- New upstream release

* Thu Apr 15 2004 Zhenja Kaluta <tren@altlinux.ru> 2.3.0-alt4
- Added nodm branch

* Wed Mar 17 2004 Zhenja Kaluta <tren@altlinux.ru> 2.3.0-alt3
- Removed bbr support
- Added snapshoting and multipath from udm patches

* Wed Mar 17 2004 Zhenja Kaluta <tren@altlinux.ru> 2.3.0-alt2
- Updated for 2.6.3 with 2.6.0-udm3

* Fri Mar 12 2004 Zhenja Kaluta <tren@altlinux.ru> 2.3.0-alt1
- New upstream release
- md-discover.patch updated for 2.3.0
- patches for 2.4.25 and 2.6.3 only

* Thu Mar 11 2004 Zhenja Kaluta <tren@altlinux.ru> 2.2.2-alt12
- Moved labels to macros
- Added engine-is_mounted patch

* Thu Mar  4 2004 Ed V. Bartosh <ed@altlinux.org> 2.2.2-alt11
- Changed directory name for the kernel patches (26 -> 2.6, 24 -> 2.4)

* Wed Mar  3 2004 Zhenja Kaluta <tren@altlinux.ru> 2.2.2-alt10
- Updated for 2.6.3

* Tue Mar  2 2004 Zhenja Kaluta <tren@altlinux.ru> 2.2.2-alt9
- md_discovery.c: flush cache before analyzing object
- raid1_discovery.c: prevent discovery in degraded mode

* Thu Feb 19 2004 Zhenja Kaluta <tren@altlinux.ru> 2.2.2-alt8
- Fixed symlinks

* Wed Feb 11 2004 Zhenja Kaluta <tren@altlinux.ru> 2.2.2-alt7
- special thanks to Sergey Bolshakov for nice scripting
- changed files order
- added conditional X
- added arm patches
- added additional config file
- changed init procedure

* Tue Feb 10 2004 Zhenja Kaluta <tren@altlinux.ru> 2.2.2-alt6
- Fixed library symlinks

* Mon Feb  9 2004 Pavel S. Mironchik <tibor@altlinux.ru> 2.2.2-alt5
- startup for rc.sysinit added

* Thu Feb  5 2004 Zhenja Kaluta <tren@altlinux.ru> 2.2.2-alt4
- Updated for 2.6.2
- removed /etc/evms.conf depend

* Thu Feb  5 2004 Zhenja Kaluta <tren@altlinux.ru> 2.2.2-alt3
- Added noncurses patch to remove ncurses depend for evms-cli

* Tue Feb 03 2004 Alexey Kotovich <a.kotovich@sam-solutions.net> 2.2.2-alt2
- delayed discovery patch was added
- print_value patch was adapted

* Mon Jan 19 2004 Alexey Kotovich <a.kotovich@sam-solutions.net> 2.2.2-alt1
- new release

* Thu Jan 15 2004 Zhenja Kaluta <tren@altlinux.ru> 2.2.1-alt5
- Adopted for 2.6.1

* Thu Jan 15 2004 Zhenja Kaluta <tren@altlinux.ru> 2.2.1-alt4
- Added 2.6 patches

* Tue Dec 16 2003 Zhenja Kaluta <tren@altlinux.ru> 2.2.1-alt3
- Adopted for 2.4.22 kernel

* Mon Dec 15 2003 Zhenja Kaluta <tren@altlinux.ru> 2.2.1-alt2
- removed some patches (adopted for 2.4.21)
- changed xfs vfs lock patch for aw kernel

* Fri Dec 12 2003 Alexey Kotovich <a.kotovich@sam-solutions.net> 2.2.1-alt1
- new release
