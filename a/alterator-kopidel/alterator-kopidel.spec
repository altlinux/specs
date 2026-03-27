%define _unpackaged_files_terminate_build 1
%def_with check

%define _common_libdir %prefix/lib
%define _common_libexecdir %prefix/libexec

Name: alterator-kopidel
Version: 1.1.0
Release: alt1

Summary: Creating a bootable image that copies the file system
License: GPL-3.0-or-later
Group: System/Configuration/Other
Url: https://www.altlinux.org/Alterator-kopidel
Vcs: https://altlinux.space/rauty/alterator-kopidel
BuildArch: noarch

Source: %name-%version.tar

Requires: alterator
Requires: alterator-setup
Requires: alterator-sh-functions
Requires: alterator-l10n
Requires: rsync
Requires: grub-common
Requires: mtools
Requires: squashfs-tools
Requires: make-initrd-bootchain
Requires: alt-uefi-certs

# Dependencies of the altinst squashfs image:
Requires: alterator-vm
Requires: alterator-grub
Requires: libevms
Requires: installer-alterator-fs >= 1.0.0
Requires: installer-common-stage2
Requires: installer-scripts-remount-stage2
Requires: console-scripts
Requires: kbd

BuildRequires(pre): rpm-macros-alterator
%ifarch %e2k
BuildRequires: guile20-devel libguile20-devel
%else
BuildRequires: guile22-devel
%endif
BuildRequires: alterator-fbi
%if_with check
BuildRequires: bats
BuildRequires: /proc
BuildRequires: /dev
BuildRequires: shellcheck
%endif

%description
If you want to make a complete copy of the file system and install
it on other machines, then you have found what you were looking for!

%prep
%setup -q

%build
%make_build

%install
%makeinstall \
	common_libdir=%buildroot%_common_libdir \
	common_libexecdir=%buildroot%_common_libexecdir \
#

%check
%make test
%make shellcheck

%post
%post_service alteratord

%files
%_alterator_backend3dir/kopidel
%_alterator_datadir/applications/kopidel.desktop
%_datadir/alterator-kopidel/
%_datadir/alterator/ui/kopidel/
%_sbindir/kopidel
%_sysconfdir/bash_completion.d/alterator-kopidel
%_common_libdir/alterator-kopidel/
%_common_libexecdir/alterator-kopidel/
%_localstatedir/alterator-kopidel/

%changelog
* Fri Mar 27 2026 Ajrat Makhmutov <rauty@altlinux.org> 1.1.0-alt1
- Fix rsync stderr handling in squashfs image creation.
- Fix swapped efi/efiremovable conditions in create_install_scripts.
- Add full LVM support (Closes: 56560, 56000).
- Change the vm profile name from workstation to kopidel.
- Remove unused data/grub-efi.cfg.
- Redesign install_grub step with using grub-efi-install with fall
  back to grub-install for EFI when grub-efi-install is absent.
- Fix broken exdrive validation in fast_check_in_exdrive.
- Fix missing $ on avoided_mount_flag variable in workdirs-list.sh.

* Fri Feb 20 2026 Ajrat Makhmutov <rauty@altlinux.org> 1.0.7-alt1
- Add new installer-common-base-stage2 to the squashfs packages.

* Mon Oct 20 2025 Ajrat Makhmutov <rauty@altlinux.org> 1.0.6-alt1
- CLI: Disable debug output.
- Wait until all the queued udev events are processed for the dev in use only.

* Sun Oct 19 2025 Ajrat Makhmutov <rauty@altlinux.org> 1.0.5-alt1
- CLI: Specify that the -s, --step flag is for testing only (Closes: 56014).

* Fri Oct 17 2025 Ajrat Makhmutov <rauty@altlinux.org> 1.0.4-alt1
- Speed up the search for ignored files
  when using regular expressions (Closes: 55999).

* Sat Oct 11 2025 Ajrat Makhmutov <rauty@altlinux.org> 1.0.3-alt1
- Fix not ignoring regular expressions from
  the default-ignored-files.txt (Closes: 56016).
- UI: Fix the compression warning when switching
  to another image creating method (Closes: 55998).
- libexec/check-fs-features.sh: Remove ntfs from BAD_FS (Closes: 55997).
- Add the ability to run the kopidel from a regular user (Closes: 55996).
- Add the restart of the alteratord service after installation.

* Sat Aug 30 2025 Ajrat Makhmutov <rauty@altlinux.org> 1.0.2-alt1
- CLI: Fix /image/Metadata directory creation for external drives.
- CLI: Implement Ctrl+C interrupt handling.
- CLI: Fix various typos.
- Add shellcheck static analysis.

* Wed Aug 27 2025 Ajrat Makhmutov <rauty@altlinux.org> 1.0.1-alt1
- Don't ignore regular files in user home directories by default.
- Add POSIX Extended regex type support to the list of ignored files.
- Remove references in descriptions about iso.
- Fix the non-use of the specified ignored list when calculating
  the minimal size of the partitions in the vm-profile.scm.
- CLI: add check for running as root.
- CLI: fix the non-use of the specified ignored list when
  calculating list of the available workdirs and exdrives.
- CLI: add translated outputs and remove unnecessary
  entries when updating the list of ignored files.
- CLI: fix an issue with errors before displaying the progress bar.
- Tests: add the build.log output if failed.
- Add the sbin/kopidel wrapper for using CLI from the git repo.

* Wed Jul 23 2025 Ajrat Makhmutov <rauty@altlinux.org> 1.0.0-alt1
- Create the razlivochniy.img instead of iso.
- Add the ability to create razlivochniy external storage
  devices (such as flash drives) instead of images.
- Create the hybrid bootable image if it is possible.
- For UEFI bootable image install only grub efi or efi removable.
- Add support for creating an image on file systems without
  the support of access rights and symbolic links (closes: 54050).
- Update the UI:
  + Change comboboxes to listboxes.
  + Add a button that updates ignored files.
  + Add the terminate building buitton.
  + Add asynchronous updating of the list of
    work directorsand external devices.
  + Add a warning for exdrive target about formatting.
  + Add a button to update the list of targets.
  + Add an update targets list when you toggle the target checkboxes.
  + Add 3 check states for the list of ignored files:
    Orange: not verified, green: verified, red: verification failed.
- CLI: don't require workdir or exdrive when only listing possible options.
- Remove the runtime dependency of alterator-preinstall.
- Stop displaying unnecessary information in the CLI.
- Add Vcs tag to the spec file.
- Update Url tag in the spec file.
- Move the executable .sh scripts from lib to the libexec.
- Add tests for the step of creating information about system partitions.

* Wed May 14 2025 Ajrat Makhmutov <rauty@altlinux.org> 0.1.3-alt1
- Add a working directory check to the CLI.
- Fix create_disk_partition_info for BTRFS only subvolume setup.
- Stop using stdbuf to handle steps stdout.
- Add support for translating the menuentry in grub.

* Thu Apr 24 2025 Ajrat Makhmutov <rauty@altlinux.org> 0.1.2-alt1
- Fix GUI arguments pass to steps executed via stdbuf.

* Sat Apr 05 2025 Ajrat Makhmutov <rauty@altlinux.org> 0.1.1-alt1
- Create smaller partitions first (closes: 53632).
- Add regular expression support to package names for the squashfs image.
- Add less to squashfs packages.
- Add libproc2_1 to squashfs packages.

* Wed Apr 02 2025 Ajrat Makhmutov <rauty@altlinux.org> 0.1.0-alt1
- Add CLI progress bar.
- Add --step flag to CLI.
- Ignore the exfat partitions when creating the vm-profile.scm.
- Add libsysfs2 to the squashfs image (closes: 53697).
- Ignore partitions which are not listed in the
  /etc/fstab when creating the vm-profile.scm.
- Add preinstall.d/00-cp-diskinfo.sh cleanup.
- Add X-Alterator-UI=qt to the desktop file (closes: 53477).

* Wed Feb 19 2025 Ajrat Makhmutov <rauty@altlinux.org> 0.0.4-alt1
- Ignore all NFS when copying (thx protvin@).

* Mon Jan 20 2025 Ajrat Makhmutov <rauty@altlinux.org> 0.0.3-alt1
- Add support for the new install2-init path.
- Remove dependency on installer-feature-alterator-setup-stage2.
- Clarify the license in the spec file.

* Sun Dec 22 2024 Ajrat Makhmutov <rauty@altlinux.org> 0.0.2-alt1
- Fix the creation of a workdir for the first use.

* Sat Dec 21 2024 Ajrat Makhmutov <rauty@altlinux.org> 0.0.1-alt1
- The first version of the new alterator module!
