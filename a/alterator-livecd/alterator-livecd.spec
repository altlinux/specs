%define _altdata_dir %_datadir/alterator

Summary: special steps for LiveCD installers

Name: alterator-livecd
Version: 0.7.4
Release: alt1

Packager: Stanislav Ievlev <inger@altlinux.org>

Requires: squashfsprogs
Requires: libshell
Requires: alterator-l10n >= 2.5-alt1
Requires: alterator-browser-qt >= 2.17.0
Requires: alterator-lookout => 2.4-alt1
BuildRequires: rpm-macros-alterator

BuildArch: noarch

Source:%name-%version.tar

License: GPL
Group: System/Configuration/Other

BuildPreReq: alterator >= 4.10-alt6

%description
special steps for LiveCD installers

%prep
%setup -q

%install
%makeinstall

%files
%_sbindir/*
%_bindir/*
%_datadir/alterator/steps/*
%_datadir/alterator/ui/*
%_datadir/alterator-livecd/
%_libexecdir/alterator/hooks/*
%_alterator_backend3dir/*

%changelog
* Thu May 24 2012 Mikhail Efremov <sem@altlinux.org> 0.7.4-alt1
- Mount /run to the newly installed system.

* Thu Aug 04 2011 Mikhail Efremov <sem@altlinux.org> 0.7.3-alt1
- Allow slideshow on 512Mb.
- Changed start title.

* Wed Jul 20 2011 Mikhail Efremov <sem@altlinux.org> 0.7.2-alt1
- Don't use global variable in do_install()/.
- Fix perms on root directory of installed system.
- rm-slideshow hook: Don't remove slides, use slideshow.conf.
- rm-slideshow hook: Change memory limit to 512Mb.

* Thu Jul 14 2011 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt1
- Fix 'step' slideshow parameter.
- Drop debug print.

* Thu Jul 14 2011 Mikhail Efremov <sem@altlinux.org> 0.7-alt1
- Fix requires.
- Make slideshow configurable.

* Thu Jun 30 2011 Mikhail Efremov <sem@altlinux.org> 0.6-alt2
- Add rm-slideshow hook.
- Add slideshow.

* Tue Jun 21 2011 Mikhail Efremov <sem@altlinux.org> 0.6-alt1
- Add Russian start/finish notes.
- Use custom text at start and finish steps.

* Mon Jun 06 2011 Mikhail Efremov <sem@altlinux.org> 0.5-alt1
- finish: Unmount mountpoints with dots in name too.
- start: Don't unmount hidden directories in root.
- finish: Run all on livecd root.
- finish: Run postinstall scripts when loaded.
- Install stages consistent with installer.
- Don't exceed 100%% in progress bar.

* Wed Apr 20 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt2
- add $destdir setting in livecd-functions

* Wed Apr 13 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt1
- Add chroot after install

* Wed Aug 26 2009 Andrey Cherepanov <cas@altlinux.org> 0.3-alt2
- Fix absent icons for specific steps

* Mon Aug 10 2009 Stanislav Ievlev <inger@altlinux.org> 0.3-alt1
- move profile data out from general framework package
- livecd-start backend: reverse order of mount points
- i18n
- livecd-install ui: remove unused code

* Fri Jun 19 2009 Andriy Stepanov <stanv@altlinux.ru> 0.2-alt1
- Add hook, to save timezone, NTP settings.
  Go away from chroot

* Wed Jun 17 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt18
- Remove LiveCD user from sudoers file

* Tue Jun 16 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt17
- Add $target_dir to hook remount_rw.sh

* Tue Jun 16 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt16
- add hook to restore default rootfs RW remounter

* Tue Jun 16 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt15
- Correct pkg list for remove

* Mon Jun 15 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt14
- save Xkbmap
  Update pkg list for remove
  Start/Stop services in installed system.

* Tue Jun 09 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt13
- Revert "Revert "Leave alterator-livecd package in installed system.""
  Save locale settings
  Remove livecd-save-nfs package in installed system
  Revert "Leave alterator-livecd package in installed system."
  Fix rm -rf invocation for temporary directories

* Tue Jun 09 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt12
- Leave alterator-livecd package in installed system.
  Leave /etc/mtab for alterator-lilo
  Mount {proc,sys,dev} after installation has finished.
  Empty temporary directories

* Mon Jun 08 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt11
- Icons now auto removed with LiveCD user homedir
  Mount proc, sys, dev to target_dir
  Fix typo in remount_rw name

* Fri Jun 05 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt10
- Remove remout_rw package after installation
  Add antihooks
  Add hook remove icons from Desktop

* Thu Jun 04 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt9
- Remove livecd-specific packages. Add datetime. Copy xorg.conf.


* Thu Jun 04 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt8
- Add steps: users, root. Do chroot to /mnt/destination.

* Tue Jun 02 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt7
- restore-kernel.sh
  fstab.sh

* Tue Jun 02 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt6
- Add hook for restore /etc/fstab

* Tue Jun 02 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt5
- Add scripts dir

* Mon Jun 01 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt4
- Fixed:
  unpacked squashfs size
  destination dir

* Fri May 29 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt3
- Add dependency to rpm-macros-alterator

* Fri May 29 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt2
- Progressbar
  check free space
  update fstab

* Fri May 22 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial build

