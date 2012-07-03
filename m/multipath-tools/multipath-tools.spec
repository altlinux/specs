%set_verify_elf_method unresolved=relaxed

Name: multipath-tools
Version: 0.4.9
Release: alt3

Summary: Tools to manage multipath devices with device-mapper
License: GPLv2+
Group: System/Configuration/Hardware

Url: http://christophe.varoqui.free.fr
Source: %name-%version.tar.bz2
# git://git.kernel.org/pub/scm/linux/storage/multipath-tools
Packager: Konstantin Pavlov <thresh@altlinux.org>

# Automatically added by buildreq on Tue Apr 07 2009
BuildRequires: libaio-devel libdevmapper-devel libncurses-devel libreadline-devel

%description
This package provides the tools to manage multipath devices by
instructing the device-mapper multipath module what to do.
The tools are:
- multipath: lists and configures multipath devices.
- multipathd: monitors paths; as paths fail and come back, it may
  initiate path group switches.
- kpartx: maps linear devmaps upon device partitions, which makes
  multipath maps partitionable.

%prep
%setup

%build
# non-SMP build
make

%install
mkdir -p %buildroot{/sbin,%_man8dir,%_initdir,%_localstatedir/multipath}
%makeinstall_std

mkdir -p %buildroot%_initdir
install -pm755 multipathd/multipathd.init.alt %buildroot%_initdir/multipathd
cp multipath.conf.annotated %buildroot%_sysconfdir/multipath.conf

mkdir -p %buildroot/lib/udev/rules.d
mv %buildroot/etc/udev/rules.d/multipath.rules %buildroot/lib/udev/rules.d/40-multipath.rules
mv %buildroot/etc/udev/rules.d/kpartx.rules %buildroot/lib/udev/rules.d/40-kpartx.rules

%post
%post_service multipathd

%preun
%preun_service multipathd

%files
%doc AUTHOR README FAQ TODO ChangeLog multipath.conf.annotated multipath.conf.synthetic
/sbin/*
/lib/udev/kpartx_id
%config /lib/udev/rules.d/*.rules
%config(noreplace) %attr(644,root,root) %_sysconfdir/multipath.conf
%_man5dir/*
%_man8dir/*
%_initdir/multipathd
%_localstatedir/multipath
/%_lib/multipath
/%_lib/libmultipath.so.0

%changelog
* Tue Feb 15 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.9-alt3
- rebuild with new libdevmapper versioning

* Mon Mar 01 2010 Konstantin Pavlov <thresh@altlinux.org> 0.4.9-alt2
- Rebase to 0.4.9 b68400c7.
- Apply 0012-RH-udev-sync-support.patch from Fedora devel (fixes #23041).
- Apply 0022-RHBZ-557845-RHEL5-style-partitions.patch from Fedora devel.
- Install udev rules to /lib/udev/rules.d instead of /etc/udev/rules.d.

* Wed Oct 14 2009 Pavlov Konstantin <thresh@altlinux.ru> 0.4.9-alt1
- Rebase to 0.4.9 aa0a885e1.
- Remove devmap_name (redundant with dmsetup, following upstream).
- Blacklist all devices by default (closes #21769).

* Thu Sep 24 2009 Pavlov Konstantin <thresh@altlinux.ru> 0.4.8-alt3
- Fix another wrong scsi_id invocation in libmultipath.

* Wed Aug 26 2009 Pavlov Konstantin <thresh@altlinux.ru> 0.4.8-alt2
- Apply a bunch of Fedora patches, notable changes are:
  + kpartx now works with logical partitions
  + fix for CVE-2009-0115
  + support for newer scsi_id invocation scheme.
- Some cosmetic spec file changes (spelling, descriptions rewrite).
- Added cciss_id utility.
- Added default configuration file.
- Added init script for multipathd.

* Tue Apr 07 2009 Michael Shigorin <mike@altlinux.org> 0.4.8-alt1
- 0.4.8: please see the site for changes that may require
  you altering your config file
- built with libaio
- added kpartx to main package
- buildreq
- NB: I don't have multipath-capable hardware, maintainer wanted

* Tue Sep 02 2008 Michael Shigorin <mike@altlinux.org> 0.4.7-alt4
- BR: glibc-kernheaders instead
- exclude devmap_name from main subpackage

* Mon Sep 01 2008 Michael Shigorin <mike@altlinux.org> 0.4.7-alt3
- BR: kernel-headers-std-def (provides broke?)

* Mon Apr 09 2007 Michael Shigorin <mike@altlinux.org> 0.4.7-alt2
- fixed build
- spec cleanup
- added %_sysconfdir/udev/rules.d/multipath.rules

* Thu Mar 30 2006 Eugene Prokopiev <enp@altlinux.ru> 0.4.7-alt1
- build with new version and without external patches

* Wed Aug 31 2005 Nick S. Grechukh <gns@altlinux.ru> 0.4.4-alt0.18
- initial build for ALT Linux Sisyphus

* Thu Jun 16 2005 - lmb@suse.de
- Remove stray newline character from /dev/disk/by-name/ entries
  (#85798, #86763)
- Clear /dev/disk/by-name/ on boot. (#85978)
- scsi_id now handles EMC Symmetrix; remove work-around for #86760.
* Tue Jun 07 2005 - lmb@suse.de
- Import fixes from upstream.
- Hardware table updates for IBM ESS and EMC CX (#81688).
- Reinstate paths correctly after failure/restore cycle (#85781,
  [#86444]).
- Create map names again and fix segfault in devmap_name (#85798).
* Tue May 24 2005 - hare@suse.de
- Fix segmentation fault with EMC Symmetrix (#85614).
- Update EMC Symmetrix entry in hwtable.
* Mon May 23 2005 - hare@suse.de
- Add hwtable entry for IBM DS6000. (#63903)
- Do a rescan for devices if multipath command line option is set.
* Fri May 20 2005 - hare@suse.de
- Fix devmap_name to use mapname and return proper status (#84748).
* Thu May 12 2005 - lmb@suse.de
- Don't complain about default prio callout command (#81695).
- Reflect recent changes in boot.multipath as well as multipathd init
  scripts.
- Actually fail paths when they are detected to be failed by multipathd
  (#81679).
- killproc/startproc/checkproc can't be used with multipathd because of
  the way the daemon switches to its own namespace (#80443).
* Mon May 09 2005 - hare@suse.de
- Use proper path checker for SGI TPC arrays.
- Update hwtable entries for SGI TP9400 and SGI TP9500.
- Write correct PID file (#80443).
* Mon Apr 25 2005 - lmb@suse.de
- Update to 0.4.4: pp_alua now licensed as GPL (#78628).
- multipath-tools-oom-adj.patch: oom_adj to a valid value.
* Thu Apr 21 2005 - lmb@suse.de
- Update to 0.4.4-pre18 which fixes the multipathd to initialize
  correctly in the absence of a configuration file (79239).
* Wed Apr 20 2005 - lmb@suse.de
- Put multipath cache back into /dev because /var might not be mounted.
- Correct hwtable entry SGI TP9400, TP9500 and IBM 3542.
* Wed Apr 20 2005 - lmb@suse.de
- Update to 0.4.4-pre16
- Build against device-mapper.1.01.xx correctly.
* Tue Apr 19 2005 - lmb@suse.de
- Build w/o device-mapper update again.
* Mon Apr 18 2005 - lmb@suse.de
- Update to 0.4.4-pre14
- Build versus device-mapper-1.01.01 to prevent deadlocks in
  kernel-space.
- Fix devmap_name to work with udev.
- Fix startup of multipathd w/o configuration file present.
* Fri Apr 15 2005 - lmb@suse.de
- Add path priority checker for EMC CLARiiON and make necessary
  adjustments so that it gets called by default (#62491).
- Set the default udev dir to '/dev'
* Fri Apr 15 2005 - hare@suse.de
- Fix to allocate default strings (#78056)
- Fix default entry for TPC9500.
* Wed Apr 13 2005 - hare@suse.de
- Added pp_alua path priority checker.
- Update to multipath-tools-0.4.4-pre12.
* Mon Apr 11 2005 - hare@suse.de
- Update to multipath-tools-0.4.4-pre10.
* Fri Apr 08 2005 - hare@suse.de
- Update multipath to handle only true multipath devices (#62491).
- Update kpartx to use the device mapper target name if available.
- Add boot.multipath script for early set up of multipath targets.
* Thu Mar 31 2005 - hare@suse.de
- Update devmap_name to select targets by table type (#62493).
* Tue Jan 25 2005 - lmb@suse.de
- Update to 0.4.2 and fix some bugs + add support for the extended DM
  multipath kernel module. (#47491)
* Thu Nov 11 2004 - hare@suse.de
- Fix bugs to make it work on S/390 (#47491).
* Fri Nov 05 2004 - hare@suse.de
- Update to version 0.3.6 (#47491).
- Fix multipath init script
- Install configuration file example.
- Install multipathd in /sbin instead of /usr/bin.
* Tue Jul 20 2004 - fehr@suse.de
- updated README mp-tools-issues.pdf (see #40640)
* Wed Jun 09 2004 - fehr@suse.de
- added pdf with README to package (see #40640)
* Thu Jun 03 2004 - fehr@suse.de
- updated to version 0.2.1
- removed patches zero-currpath.patch and rm-newline-in-name.patch
  already contained in 0.2.1
* Thu Jun 03 2004 - fehr@suse.de
- added patch zero-currpath.patch (see bugzilla #40640)
* Wed May 26 2004 - uli@suse.de
- fixed to build on s390x
* Wed May 26 2004 - fehr@suse.de
- added patch rm-newline-in-name.patch (see bugzilla #40640)
* Tue May 25 2004 - fehr@suse.de
- created initial version of a SuSE package from version 0.2.0 of
  multipath tools
